import xmlschema
import json
import os
import re
import scraper
from lxml import etree

def xsd2json(schema_path, debug=False):
    with open(schema_path, 'r') as included_schema_file:
        included_schema_full = included_schema_file.read()
        root_element = etree.XML(included_schema_full.encode('utf-8'))
    root_components, import_map, prefix_map = isolate_imported_namespaces(root_element)

    # Recurse through xs:include files to combine into single parent XML schema
    unified_schema_content, import_map, prefix_map = flatten_xsd(
        root_components,
        base_dir_path = os.path.dirname(schema_path),
        import_map=import_map,
        prefix_map=prefix_map
    )

    # Apply combined namespace information to schema header
    complete_schema_content = insert_namespaces(unified_schema_content, import_map, prefix_map)

    if debug:
        with open("debug.xml", "w") as f:
            f.write(complete_schema_content)
        print("Target Namespace:", root_element.get('targetNamespace'))
        print("Namespaces:", xsd.namespaces)

    # Load combined schema into XMLSchema class instance to dump as JSON
    xsd = xmlschema.XMLSchema(complete_schema_content)
    combined_schema_dict = xsd.to_dict(complete_schema_content)

    return json.dumps(
        remove_at_prefix_from_json_keys(combined_schema_dict), 
        indent=2)

# xmlschema adds "@" sign prefix to identify XML tag attributes
def remove_at_prefix_from_json_keys(json_data):
    if isinstance(json_data, dict):
        return {key.lstrip('@'): remove_at_prefix_from_json_keys(value) 
                for key, value in json_data.items()}
    elif isinstance(json_data, list):
        return [remove_at_prefix_from_json_keys(item) 
                for item in json_data]
    else:
        return json_data


# Split namespace imports out of the content and into a separate map
# This allows XML schema to include other content while controlling collisions
# :param root_element: XML schema etree element
# :param base_dir_path: relative path to prepend for included schema
# :param import_map: dict tracking all unique imported namespaces and their sources
# :param prefix: dict tracking all unique imported prefixes
# :return: (<flattened schema string>, import_map, prefix_map)
def isolate_imported_namespaces(root_element, import_map = {}, prefix_map = {}):
    # Collect imported schema prefixes
    target = root_element.attrib['targetNamespace']
    for key, value in root_element.nsmap.items():
        key = ':'.join(['xmlns', key]) if key else 'xmlns'
        if key not in prefix_map.keys():
            prefix_map[key] = value

    for child in root_element:
        # Find and collect all xs:import elements and their namespaces
        for imp in child.xpath('//xs:import', namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'}):
            namespace = imp.get('namespace')
            schemaLocation = imp.get('schemaLocation')
            if import_map.get(namespace, None) is None:
                import_map[namespace] = schemaLocation
            root_element.remove(imp)

    return (etree.tostring(root_element, encoding='utf-8').decode('utf-8'), import_map, prefix_map)


# Resolve XML includes recursively (same namespace only)
# :param schema_content: XML schema as string
# :param base_dir_path: relative path to prepend for included schema
# :param import_map: dict tracking all unique imported namespaces
# :param prefix: dict tracking all unique imported prefixes
# :return: (<flattened schema string>, import_map, prefix_map)
def flatten_xsd(schema_content, base_dir_path = "", import_map = {}, prefix_map = {}):
    while 'xs:include' in schema_content:
        include_index = schema_content.find('xs:include')
        start_quote_index = schema_content.find('"', include_index)
        end_quote_index = schema_content.find('"', start_quote_index + 1)
        included_schema_path = schema_content[start_quote_index + 1:end_quote_index]
        print('including', included_schema_path, 'at index', include_index)

        with open(os.path.join(base_dir_path, included_schema_path), 'r') as included_schema_file:
            included_schema_raw = included_schema_file.read()
            included_schema_root = etree.XML(included_schema_raw.encode('utf-8'))
            imported_schema_string, import_map, prefix_map = isolate_imported_namespaces(included_schema_root, import_map, prefix_map)
        
        flattened_include, import_map, prefix_map = flatten_xsd(imported_schema_string, base_dir_path=base_dir_path, import_map=import_map, prefix_map = prefix_map)
        
        content_string = re.sub(r"<xs:schema[^>]*>|</xs:schema>|<\?xml.*\?>", "", flattened_include)

        schema_content = schema_content.replace(
            f'<xs:include schemaLocation="{included_schema_path}"/>',
            content_string
        )

    return (schema_content, import_map, prefix_map)


# Apply imports and prefixes to schema header
# :param schema_content: XML schema as string
# :param import_map: dict tracking all unique imported namespaces
# :param prefix: dict tracking all unique imported prefixes
# :return: XML schema string with harmonised header
def insert_namespaces(schema_content, import_map, prefix_map):
    start_index = schema_content.find('<xs:schema')
    end_index = schema_content.find('>', start_index)
    complete_schema_content = schema_content[:end_index+1]
    # Add combined namespace prefixes from prefix map to <xs:schema> tab
    schema_attributes = [attrib for attrib in complete_schema_content.split(' ') 
                         if not attrib.startswith('xmlns')]
    schema_tag_as_list = [schema_attributes[0]]
    schema_tag_as_list.extend([f'{prefix}="{target}"' for prefix, target in prefix_map.items()])
    schema_tag_as_list.extend(schema_attributes[1:])
    complete_schema_content = ' '.join(schema_tag_as_list)
    # Re-insert unique set of namespace sources after schema tag
    for key, value in import_map.items():
        namespace_import = f'<xs:import namespace="{key}" schemaLocation="{value}"/>'
        complete_schema_content += '\n' + namespace_import
    complete_schema_content += schema_content[end_index+1:]
    return complete_schema_content
