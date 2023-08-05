import re
from dataclasses import dataclass, InitVar, field
from linkml_runtime.linkml_model import ClassDefinition, SlotDefinition, Prefix, \
    EnumDefinition, SubsetDefinition, SubsetDefinitionName, TypeDefinition, \
    TypeDefinitionName, PermissibleValue, SchemaDefinition
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.utils.schemaview import SchemaView

@dataclass
class ODMLinkMLTransformer():
    '''
    Class for transforming ODM XML Schema structure into LinkML 
    '''
    structure: dict = None
    schema: SchemaDefinition = None
    schema_builder: SchemaBuilder = None
    namespace: str = field(default = 'http://www.cdisc.org/ns/odm/v2.0')
    namespace_prefix: str = field(default = 'odm')
    look_up_membership: dict = None

    def create_schema(self):
        '''
        Create LinkML from the structure that has been loaded to this class
        '''
        self.schema_builder = SchemaBuilder(id = self.namespace, name = self.namespace_prefix)
        self.schema_builder.add_defaults()
        self.schema_builder.schema.prefixes['nci'] = Prefix('nci', 'http://ncicb.nci.nih.gov/xml/odm/EVS/CDISC')
        self.schema_builder.schema.prefixes['xml'] = Prefix('xml', 'http://ncicb.nci.nih.gov/xml/odm/EVS/CDISC')
        self.schema_builder.schema.prefixes['xhtml'] = Prefix('xhtml', 'http://www.w3.org/1999/xhtml')
        self.schema = SchemaView(self.schema_builder.schema)

        groups = self.structure.get('xs:group', [])
        attribute_groups = self.structure.get('xs:attributeGroup', [])
        simple_types = self.structure.get('xs:simpleType', [])
        elements = self.structure.get('xs:element', [])

        self.create_subsets(groups)
        [self.create_simple_type(simple, simple.get('name')) for simple in simple_types]
        self.create_slots(attribute_groups)
        [self.create_class(elem, attribute_groups) for elem in elements]

        self.hardcoded_modifications()
        
    def hardcoded_modifications(self):
        '''
        Content that is different from the Source Schema
        '''
        # New Type for renamed XML Schema-specific element: internationalisation/localisation attribute
        self.schema.add_type(TypeDefinition(uri='xml:lang', name='_languageType', base='str',
                                    description='language context for internationalisation and localisation'))
        # New Type for renamed XML Schema-specific elements: text between tags
        self.schema.add_type(TypeDefinition(uri='xhtml:div', name='_contentType', base='str',
                                    description='multi-line text content from between XML tags'))

        # Workaround for ODM root class name clash: ODMFileMetadata
        clashing_class = self.schema.get_class('ODM')
        if clashing_class:
            clashing_class.name = 'ODMFileMetadata'
            self.schema.add_class(clashing_class)
            self.schema.delete_class('ODM')

    @staticmethod
    def map_base(type) -> str:
        # Map XML primitives to LinkML primitives
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
            return 'str'

    @staticmethod
    def map_type(ref) -> str:
        # Remove prefixes for LinkML type references
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

    def create_slots(self, attribute_groups) -> None:
        # https://linkml.io/linkml-model/docs/SlotDefinition/
        slots = {}
        slot_names = []
        for ag in attribute_groups:
            for attribute in ag.get('xs:attribute', []):
                ref = attribute.get('ref')
                name = attribute.get('name') or self.map_type(ref)
                range = self.map_type(attribute.get('type')) 
                if ref and not range:
                    range = self.map_type(ref) + 'Type'
                description = '\n'.join(attribute.get('xs:annotation', {}).get('xs:documentation', []))
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
            ranges =  slots[slot_name].get('ranges', ref) 
            slot = SlotDefinition(name = slot_name)
            if ref:
                slot.exact_mappings = [ref]
                slot.uri = self.namespace_prefix + ':' + ref
            if description:
                slot.description = description
            if ranges:
                if len(ranges) > 1:
                    slot.any_of = [{'range' : r} for r in ranges]
                if len(ranges) == 1:
                    slot.range = ranges[0]
            else:
                print('no range found for slot', slot_name, ranges, ref, description)
            self.schema.add_slot(slot)
        return None


    def create_subsets(self, element_groups) -> None:
        # https://linkml.io/linkml-model/docs/SubsetDefinition
        self.look_up_membership = {}
        for g in element_groups:
            sequence = g.get('xs:sequence', {})
            if not sequence:
                continue
            self.look_up_membership[g.get('name')] = [e for e in sequence.get('xs:element')]

        for group, ref_list in self.look_up_membership.items():
            subset = SubsetDefinition(group)
            subset.from_schema = self.namespace
            self.schema.schema.subsets[subset.name] = subset


    # Assemble enumerations / controlled terminology
    def create_enumeration(self, enumerations, enum_name, alias, as_children = True) -> None:
        # https://linkml.io/linkml-model/docs/EnumDefinition
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
        self.schema.add_enum(this_enum)


    # Assemble types and their restrictions
    def create_simple_type(self, element, type_name) -> None:
        # https://linkml.io/linkml-model/docs/TypeDefinition
        if self.schema.get_type(type_name):
            return None
        type = TypeDefinition(type_name)
        restriction = element.get('xs:restriction', {})
        base = self.map_base(restriction.get('base')) or 'str'
        if base:
            type.base = base
        
        alias = {}
        if element.get('xs:annotation'):
            type.description = '\n'.join(element.get('xs:annotation', {}).get('xs:documentation'))
            appinfo = element.get('xs:annotation', {}).get('xs:appinfo', {})
            if appinfo:
                alias = appinfo[0].get('odm:Alias')
                if alias:
                    type.exact_mappings = [':'.join([a.get('Context'), a.get('Name')]) for a in alias]

        # Assemble enumerations at current level
        enumerations = restriction.get('xs:enumeration', {})
        if enumerations:
            self.create_enumeration(enumerations, type_name, alias)
            return None
            
        # Assemble inline enumerations from xs:union
        nested_types = element.get('xs:union', {}).get('xs:simpleType', [])
        if nested_types:
            nested_bases = [st.get('xs:restriction',{}).get('base') for st in nested_types]
            if nested_bases:
                if len(nested_bases) == 1:
                    type.base = self.map_base(nested_bases[0]) or self.map_type(nested_bases[0])
                else:
                    type.any_of = [{self.map_base(b) or self.map_type(b): None} for b in nested_bases]

            nested_enumerations = nested_types[0].get('xs:restriction', {}).get('xs:enumeration', [])
            if nested_enumerations:
                enum_name = type_name + 'Enum'
                type.base = self.map_base(nested_types[0].get('xs:restriction', {}).get('base'))
                self.create_enumeration(nested_enumerations, enum_name, alias, as_children = False)
    
        member_types = element.get('xs:union', {}).get('memberTypes', [])
        if member_types:
            type.any_of = [{self.map_base(t): None} for t in member_types]

        if not type.base and not type.typeof:
            print('no base provided for', element.get('name') ,'type')

        # Translate min/max length restrictions to pattern
        max_length = restriction.get('xs:maxLength', {}).get('value')
        min_length = restriction.get('xs:minLength', {}).get('value')
        pattern = restriction.get('xs:pattern', {}).get('value')
        if min_length:
            type.pattern = f'.{{{min_length}, }}'
        if max_length:
            type.pattern = f'.{{{min_length or 0}, {max_length}}}'    
        if pattern:
            type.pattern = pattern

        type.uri = self.namespace_prefix + ':' + type_name
        self.schema.add_type(type)


    @staticmethod
    def get_attribs_from_group(name, attribute_groups) -> [dict]:
        matches = [ag.get('xs:attribute') for ag in attribute_groups if ag['name'] == name]
        attribs = matches[0]
        return attribs if attribs else None


    @staticmethod
    def get_groups(element, look_up_membership) -> [str]:
        groups_found = []
        for name, ref_list in look_up_membership.items():
            for ref in ref_list:
                if element == ref.get('ref'):
                    groups_found.append(name)
        return groups_found

    def map_cardinality(self, element) -> dict:
        min_occurs = element.get('minOccurs')
        max_occurs = element.get('maxOccurs')
        range = self.map_type(element.get('ref'))
        print(element)
        if min_occurs == max_occurs:
            cardinality = min_occurs
        else:
            max_occurs_repr = '*' if max_occurs == 'unbounded' else max_occurs or '*'
            cardinality = f"{min_occurs or '0'}..{max_occurs_repr}"
        return {
            'range': range,
            'required': bool(int(min_occurs) and int(min_occurs) > 0),
            'multivalued': bool(int(max_occurs) and int(max_occurs) > 1),
            'cardinality': cardinality,
            'description': '\n'.join(element.get('xs:annotation', {}).get('xs:documentation',[]))
        } if range else None


    def create_class(self, element, attribute_groups) -> None:
        # https://linkml.io/linkml-model/docs/ClassDefinition/
        element_name = element.get('name')
        matching_types = [t for t in self.structure.get('xs:complexType') if element.get('type') == t.get('name')]
        if not matching_types:
            print('no type definition found for', element.get('type'))
        props = matching_types[0]
        if not props:
            print('no class definition found for element', element_name)
            return None

        klass = ClassDefinition(element_name)
        if props.get('xs:annotation'):
            klass.description = '\n'.join(props.get('xs:annotation').get('xs:documentation'))

        # extract attributes from groups listed at various levels
        
        slot_usage = []
        slot_groups = []
        slot_groups.extend(props.get('xs:simpleContent', {}).get('xs:extension', {}).get('xs:attributeGroup', []))
        slot_groups.extend(props.get('xs:complexContent', {}).get('xs:restriction', {}).get('xs:attributeGroup', []))
        slot_groups.extend(props.get('xs:attributeGroup', []))
        for ag in slot_groups:
            group_name = self.map_type(ag.get('ref'))
            attribs = self.get_attribs_from_group(group_name, attribute_groups)
            if not attribs:
                continue
            for attrib in attribs:
                attrib_name = attrib.get('name') or self.map_type(attrib.get('ref'))
                if not attrib_name:
                    print(element_name, 'attribute has no name', attrib)
                    continue
                required = (attrib.get('use') == 'required')
                this_slot_usage = {attrib_name  : {'required': required}}
                range = self.map_type(attrib.get('type'))
                simpleType = attrib.get('xs:simpleType')
                if not range and not simpleType:
                    print('no type/s provided for', attrib_name, 'in', group_name)
                if simpleType and simpleType.get('xs:union'):
                    types = simpleType.get('xs:union', {}).get('memberTypes', {})
                    range_list = [{'range': self.map_type(t)} for t in types]
                    this_slot_usage[attrib_name]['any_of'] = range_list
                else:
                    this_slot_usage[attrib_name]['range'] = range
                slot_usage.append(this_slot_usage)

        groups_found = self.get_groups(element_name, self.look_up_membership)
        subsets = [SubsetDefinitionName(g) for g in groups_found]
        if groups_found:
            klass.in_subset = subsets[0]

        # TODO Handle relationships and cardinality
        '''
        Each {selector} can have only one {field}
        xs:unique[{name, {xs:selector}, [{xs:field}]}]}
        e.g. 
        {
          "name": "UC-CL-1",
          "xs:selector": {
            "xpath": "odm:CodeListItem"
          },
          "xs:field": [
            {
              "xpath": "@CodedValue"
            }
          ]
        }
        '''
        # minOccurs, maxOccurs
        # xs:sequence determines order of elements and included groups
        sequence = props.get('xs:sequence')
        if sequence:
            element_list = element.get('xs:element', [])
            group = element.get('xs:group')
            for seq_element in element_list:
                print(seq_element)
                relation = self.map_cardinality(seq_element)
                ref_name = relation.pop('range')
                if ref_name:
                    slot_usage.append({ref_name : relation})
                else:
                    print('No name found for sequence element', seq_element)
                pass

            if group:
                # self.map_type(ref), minOccurs, maxOccurs
                #TODO Add / reference relationships from _____ElementExtension 
                pass

        klass.slot_usage = slot_usage
        klass.class_uri = self.namespace_prefix + ':' + element_name
        self.schema.add_class(klass)
