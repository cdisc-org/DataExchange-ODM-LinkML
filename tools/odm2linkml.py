import argparse
from xsd2json import xsd2json
import json
from ODMLinkMLTransformer import ODMLinkMLTransformer
from linkml_validator.validator import Validator
from linkml.generators.linkmlgen import LinkmlGenerator

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

yaml_text = LinkmlGenerator(schema = linkml_schema.schema_builder.schema, format='yaml').serialize()

with open(output, 'w+') as f:
    f.write(yaml_text)
print('Schema converted to LinkML file', output)

# Validate the schema (Validator object self-validates on creation)
print('Validating LinkML schema file')
validator = Validator(schema = output)