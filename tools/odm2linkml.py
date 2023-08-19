import argparse
from xsd2json import xsd2json
import json
from ODMLinkMLTransformer import ODMLinkMLTransformer
from linkml_validator.validator import Validator
from linkml.generators.linkmlgen import LinkmlGenerator
from linkml_runtime.linkml_model import Example
import scraper

parser = argparse.ArgumentParser()
parser.add_argument('xsd_schema_in', type=str, help='path to .xsd schema file')
parser.add_argument('--output', type=str, help='path to LinkML yaml file to output')
args = parser.parse_args()

# Build JSON representation of ODM XML Schema
xsd_schema_in = args.xsd_schema_in
output = args.output or 'ODM.yaml'
 
json_from_xml_schema = xsd2json(xsd_schema_in)

with open('json/' + output.replace('.yaml', '.json'), 'w+') as f:
    f.write(json_from_xml_schema)

# Feed JSON structure into LinkML transformer
structure = json.loads(json_from_xml_schema)
linkml_schema = ODMLinkMLTransformer(structure)
linkml_schema.create_schema()

# Supplement with wiki content
headers = scraper.connect()
print('Scraping class info from wiki for', output)
for klass in linkml_schema.class_names:
    scraped = scraper.scrape_wiki_content(klass, headers = headers)
    if not scraped:
        continue
    fixed_klass = 'ODMFileMetadata' if klass == 'ODM' else klass
    schema_description = linkml_schema.schema.schema.classes[fixed_klass]['description']
    wiki_description = scraped.get('description')
    linkml_schema.schema.schema.classes[fixed_klass]['description'] = schema_description or wiki_description
    wiki_examples = scraped.get('examples') or []
    fixed_examples = []
    example_number = 0
    for example in wiki_examples:
        example_number += 1
        example_object = Example(example)
        fixed_examples.append(example_object)
    # linkml_schema.schema.schema.classes[fixed_klass]['examples'] = fixed_examples

    attribute_table = scraped.get('attribute_table', [])
    for slot in attribute_table:
        description = slot.get('Definition')
        schema_slot_description = None
        slot_usage = None
        slot_name = slot.get('Attribute')
        if not slot_name:
            continue
        slot_name = linkml_schema.map_type(linkml_schema.hardcoded_name(slot_name))
        external_comments = []
        internal_notes = []
        usage = slot.get('Usage')
        if usage:
            # TODO: check wiki vs XML Schema for usage
            external_comments.append(usage)
        data_type = slot.get('Schema Datatype or Enumeration')
        range = None
        if data_type and len(data_type.split()) > 1:
            # TODO: make into enum, check wiki vs XML schema for range
            external_comments.append('enum values:' + data_type)
        elif data_type:# TODO: check wiki vs XML Schema for range
            external_comments.append('range:' + data_type)
            range = data_type
        rules = slot.get('Business Rule(s)')
        if rules:
            external_comments.append(rules)      
        
        # Defensive schema object access in case missing from imported schema
        try:
            slot_usage = linkml_schema.schema.schema.classes[fixed_klass]['slot_usage']
            try:
                this_slot_usage = linkml_schema.schema.schema.classes[fixed_klass]['slot_usage'][slot_name]
            except KeyError:
                print('slot', slot_name, 'from wiki page for class', fixed_klass, 'did not have a usage')
                this_slot_usage = None
        except KeyError:
            print('slot', slot_name, 'has no slot_usage')
        if this_slot_usage is None:
            continue
        try:
            schema_class_slot_description = this_slot_usage['description']
        except KeyError:
            schema_class_slot_description = None
        linkml_schema.schema.schema.classes[fixed_klass]['slot_usage'][slot_name]['description'] = \
            schema_class_slot_description or description

        slot_entry = None
        try:
            slot_entry = linkml_schema.schema.schema.slots[slot_name]            
            try:
                this_slot_entry = linkml_schema.schema.schema.slots[slot_name]['description']
            except KeyError:
                this_slot_entry = None
        except KeyError:
            print('slot', slot_name, 'from wiki page for class', fixed_klass, 'was not found in slots')

        if slot_entry:
            original_description = slot_entry['description']
            linkml_schema.schema.schema.slots[slot_name]['description'] =  \
                original_description or schema_class_slot_description or description
        
        if external_comments:
            linkml_schema.schema.schema.classes[fixed_klass]['slot_usage'][slot_name]['comments'] = \
                '\n'.join(external_comments)

# Write the schema out
yaml_text = LinkmlGenerator(schema = linkml_schema.schema_builder.schema, format='yaml').serialize()

with open(output, 'w+') as f:
    f.write(yaml_text)
print('Schema converted to LinkML file', output)

# Validate the schema (Validator object self-validates on creation)
print('Validating LinkML schema file')
validator = Validator(schema = output)