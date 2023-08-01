import argparse
from xsd2json import xsd2json
import json
import re
from linkml_runtime.linkml_model import ClassDefinition, SlotDefinition, Prefix, \
    EnumDefinition, SubsetDefinition, SubsetDefinitionName, TypeDefinition, \
    TypeDefinitionName, PermissibleValue
from linkml.generators.linkmlgen import LinkmlGenerator
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.utils.schemaview import SchemaView
from linkml_validator.validator import Validator

parser = argparse.ArgumentParser()
parser.add_argument('xsd_schema_in', type=str, help='path to .xsd schema file')
parser.add_argument('--output', type=str, help='path to LinkML yaml file to output')
parser.add_argument('--namespace', type=str, help='path to target namespace')
parser.add_argument('--prefix', type=str, help='prefix for target namespace')
args = parser.parse_args()

xsd_schema_in = args.xsd_schema_in or 'cdisc/odm/ODM.xsd'
output = args.output or 'ODM.yaml'
namespace = args.namespace or 'http://www.cdisc.org/ns/odm/v2.0'
namespace_prefix = args.prefix or 'odm'

json_from_xml_schema = xsd2json(xsd_schema_in)

structure = json.loads(json_from_xml_schema)

schema_builder = SchemaBuilder(id = namespace, name = namespace_prefix)
schema_builder.add_defaults()
schema_builder.schema.prefixes['nci'] = Prefix('nci', 'http://ncicb.nci.nih.gov/xml/odm/EVS/CDISC')
schema = SchemaView(schema_builder.schema)

def map_base(type):
    if not type:
        return None
    type_map = {
        'xs:string': 'str',
        'xs:positiveInteger': 'int', 
        'xs:dateTime': 'XSDDateTime', 
        'xs:integer': 'int',
        'xs:float': 'float',
        'xs:time': 'XSDTime',
        'xs:date': 'XSDDate',
        'xs:boolean': 'Bool',
        'xs:decimal': 'Decimal',
        'xs:double': 'float',
        'xs:anyURI': 'URIorCURIE',
        'xs:hexBinary': 'str',
        'xs:base64Binary': 'str',
        'xs:ID': 'str',
        'xs:XSID': 'str',
        'xs:IDREF': 'str'
    }
    if type in type_map.keys():
        type = type_map[type]
        return type
    else:
        return None
    
def map_type(ref) -> str:
    if ref is None:
        return None
    result = re.search(r'{.*?}(\w+)', ref)
    ref = result.group(1) if result else ref
    type_map = {
        'xs:anyURI': 'uriorcurie',
        'xs:ID': 'oid',
        'xs:IDREF': 'oid',
        'xlink:href': 'href',
        'xml:lang': '_language',
        'xhtml:div': '_content',
    }
    if ref in type_map.keys():
        return type_map[ref]
    else:
        return ref.split(':')[-1]
    
# New slots to support XML schema elements
schema.add_slot(SlotDefinition(name='language'))

# Assemble slots
attribute_groups = structure.get('xs:attributeGroup')
def get_attribs_from_group(name, attribute_groups=attribute_groups) -> [dict]:
    matches = [ag for ag in attribute_groups if ag['name'] == name]
    return matches[0].get('xs:attribute') if matches else None

def create_all_slots(schema, attribute_groups = attribute_groups) -> [str]:
    slots = {}
    slot_names = []
    for ag in attribute_groups:
        for attribute in ag.get('xs:attribute', []):
            ref = attribute.get('ref')
            name = attribute.get('name') or map_type(ref)
            range = map_type(attribute.get('type'))
            description = '\n'.join(attribute.get('annotation', {}).get('xs:documentation', []))
            # handle slot conflicts
            if name in slot_names:
                existing_range = slots.get(name, {}).get('ranges') or []
                if existing_range and range not in existing_range:
                    existing_range.append(range)
                    slots[name]['ranges'] = existing_range
                if len(slots[name].get('description','')) < len(description):
                    slots[name]['description'] = description 
            else:
                slots[name] = {'ranges': [range]}
                if description:
                    slots[name]['description'] = description
            slot_names.append(name)

    for slot_name in set(slot_names):
        name = slots[slot_name].get('name')
        description = slots[slot_name].get('description')
        ref = slots[slot_name].get('ref')
        ranges =  slots[slot_name].get('ranges', []) 
        slot = SlotDefinition(name = slot_name)
        if ref:
            slot.exact_mappings = [ref]
            slot.uri = namespace_prefix + ':' + ref
        if description:
            slot.description = description
        if ranges:
            if len(ranges) > 1:
                slot.any_of = [{'range' : r} for r in ranges]
            if len(ranges) == 1:
                slot.range = ranges[0]
        else:
            print('no range found for slot', slot_name, ranges, ref, description)
        schema.add_slot(slot)
    return slot_names

slot_names = create_all_slots(schema)

# Assemble subsets
element_groups = structure.get('xs:group')
look_up_membership = {}
for g in element_groups:
    sequence = g.get('xs:sequence', {})
    if not sequence:
        continue
    look_up_membership[g.get('name')] = [e for e in sequence.get('xs:element')]

for group, ref_list in look_up_membership.items():
    subset = SubsetDefinition(group)
    subset.from_schema = namespace
    schema.schema.subsets[subset.name] = subset

def get_groups(element, look_up_membership=look_up_membership) -> [str]:
    groups_found = []
    for name, ref_list in look_up_membership.items():
        for ref in ref_list:
            if element == ref.get('ref'):
                groups_found.append(name)
    return groups_found


# Assemble classes
for element in structure.get('xs:element'):
    element_name = element.get('name')
    matching_types = [t for t in structure.get('xs:complexType') if element.get('type') == t.get('name')]
    if not matching_types:
        print('no type definition found for', element.get('type'))
    props = matching_types[0]
    if not props:
        print('no class definition found for element', element_name)
        continue

    klass = ClassDefinition(element_name)
    if props.get('xs:annotation'):
        klass.description = '\n'.join(props.get('xs:annotation').get('xs:documentation'))

    restricted_attribute_group = props.get('xs:complexContent', {}).get('xs:restriction',{}).get('xs:attributeGroup')
    slot_groups = props.get('xs:attributeGroup') or restricted_attribute_group
    if slot_groups:
        slot_usage = []
        for ag in slot_groups:
            group_name = ag.get('ref')
            attribs = get_attribs_from_group(group_name)
            if not attribs:
                continue
            for attrib in attribs:
                if not attrib.get('name'):
                    continue
                required = (attrib.get('use') == 'required')
                this_slot_usage = {attrib.get('name')  : {'required': required}}
                range = map_type(attrib.get('type'))
                simpleType = attrib.get('xs:simpleType')
                if not range and not simpleType:
                    print('no type/s provided for', attrib.get('name'), 'in', group_name)
                if simpleType and simpleType.get('xs:union'):
                    types = simpleType.get('xs:union', {}).get('memberTypes', {})
                    range_list = [{'range': map_type(t)} for t in types]
                    this_slot_usage[attrib.get('name')]['any_of'] = range_list
                else:
                    this_slot_usage[attrib.get('name')]['range'] = range
                slot_usage.append(this_slot_usage)
        klass.slot_usage = slot_usage

    groups_found = get_groups(element_name)
    subsets = [SubsetDefinitionName(g) for g in groups_found] 
    if groups_found:
        klass.in_subset = SubsetDefinitionName(groups_found[0])
   
    # TODO Handle relationships and cardinality
    # minOccurs, maxOccurs
    # xs:unique[{name, {xs:selector}, [{xs:field}]}]}
    sequence = props.get('xs:sequence')
    # xs:sequence determines order of elements and included groups
    if sequence:
        if sequence.get('xs:element'):
            # map_type(ref), minOccurs, maxOccurs
            # TODO Support for explicitly referenced elements (slots, relationships)
            pass
        if sequence.get('xs:group'):
            # map_type(ref), minOccurs, maxOccurs
            #TODO Support for extensions
            pass
        
    klass.class_uri = namespace_prefix + ':' + element_name
    schema.add_class(klass)


# Assemble enumerations / controlled terminology
def create_enumeration(schema, enumerations, enum_name, alias, as_children = True) -> None:
    this_enum = EnumDefinition(name = enum_name)
    values = {}
    for v in enumerations:
        this_value = {}
        if isinstance(v, str):
            enum_value = v
        if isinstance(v, dict):
            enum_value = v.get('value')
            appinfo = v.get('xs:annotation', {}).get('xs:appinfo')
            if appinfo:
                aliases = appinfo[0].get('odm:Alias', {})
            enum_meaning = ':'.join([aliases[0].get('Context'), aliases[0].get('Name')]) if appinfo else None
            enum_documentation = v.get('xs:annotation', {}).get('xs:documentation')
            enum_description = '\n'.join(enum_documentation) if enum_documentation else None
            this_value['description'] = enum_description or None
            this_value['meaning'] = enum_meaning or None
            this_value['is_a'] = enum_name if as_children else None
        values[enum_value] = this_value
    this_enum.permissible_values = values

    if alias:
        this_enum.code_set = alias[0].get('Context')
        this_enum.aliases = alias[0].get('Name')
        this_enum.conforms_to = ':'.join([alias[0].get('Context'), alias[0].get('Name')])
    schema.add_enum(this_enum)
    return None


# Assemble types and their restrictions
def create_simple_type(schema, element, type_name) -> None:
    if schema.get_type(type_name):
        return None
    
    slot = TypeDefinition(type_name)
    restriction = element.get('xs:restriction', {})
    base = map_base(restriction.get('base'))
    if base:
        slot.base = base
    
    alias = {}
    if element.get('xs:annotation'):
        slot.description = '\n'.join(element.get('xs:annotation', {}).get('xs:documentation'))
        appinfo = element.get('xs:annotation', {}).get('xs:appinfo', {})
        if appinfo:
            alias = appinfo[0].get('odm:Alias')
            if alias:
                slot.exact_mappings = [':'.join([a.get('Context'), a.get('Name')]) for a in alias]
    


    # Assemble enumerations at current level
    enumerations = restriction.get('xs:enumeration', {})
    if enumerations:
        create_enumeration(schema, enumerations, type_name, alias)
        return None
        
    # Assemble inline enumerations from xs:union
    nested_types = element.get('xs:union', {}).get('xs:simpleType', [])
    if nested_types:
        nested_bases = [st.get('xs:restriction',{}).get('base') for st in nested_types]
        if nested_bases:
            slot.base = nested_bases[0]
            slot.typeof = TypeDefinitionName('string')
            # TODO Handle multiple nested base types
            # slot.any_of = [TypeDefinitionName(map_base(b) or map_type(b)) for b in nested_bases]

        nested_enumerations = nested_types[0].get('xs:restriction', {}).get('xs:enumeration', [])
        if nested_enumerations:
            enum_name = type_name + 'Enum'
            slot.base = enum_name
            create_enumeration(schema, nested_enumerations, enum_name, alias, as_children = False)
 
    member_types = element.get('xs:union', {}).get('memberTypes', [])
    if member_types:
        slot.base = member_types[0]
        slot.typeof = TypeDefinitionName('string')
        # TODO Handle multiple member types, typeof
        # slot.any_of = [TypeDefinitionName(t) for t in member_types]

    if not slot.base and not slot.typeof:
        print('no base provided for', element.get('name') ,'type')

    # Translate min/max length restrictions to pattern
    max_length = restriction.get('xs:maxLength', {}).get('value')
    min_length = restriction.get('xs:minLength', {}).get('value')
    pattern = restriction.get('xs:pattern', {}).get('value')
    if min_length:
        slot.pattern = f'.{{{min_length}, }}'
    if max_length:
        slot.pattern = f'.{{{min_length or 0}, {max_length}}}'    
    if pattern:
        slot.pattern = pattern

    slot.uri = namespace_prefix + ':' + type_name
    schema.add_type(slot)
    return None


for element in structure.get('xs:simpleType'):
    create_simple_type(schema, element, element.get('name', 'DEFAULT_TYPE_NONE_FOUND'))
   
yaml_text = LinkmlGenerator(schema = schema_builder.schema, format='yaml').serialize()

with open(output, 'w+') as f:
    f.write(yaml_text)
print('Schema converted to LinkML file', output)

# Throw errors if the schema is invalidvalidator = Validator(schema = output)