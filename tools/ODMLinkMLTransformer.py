import re
from dataclasses import dataclass, field
from linkml_runtime.linkml_model import ClassDefinition, SlotDefinition, \
    Prefix, EnumDefinition, SubsetDefinition, SubsetDefinitionName, \
    TypeDefinition, SchemaDefinition, Example
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.utils.schemaview import SchemaView
import scraper

# Names for unnamed XML elements
CONTENT_KEY = 'content'
LANGUAGE_KEY = 'language'
# Switch this to True for debugging
DEBUG = False


@dataclass
class ODMLinkMLTransformer():
    """
    Class for transforming ODM XML Schema structure into LinkML 
    """
    structure: dict = None
    schema: SchemaDefinition = None
    schema_builder: SchemaBuilder = None
    namespace: str = field(default = 'http://www.cdisc.org/ns/odm/v2.0')
    type_documentation: str = field(default = 'https://wiki.cdisc.org/display/PUB/Data+Formats')
    namespace_prefix: str = field(default = 'odm')
    look_up_membership: dict = None
    class_names: list = None
    slot_names: list = field(default_factory=lambda: [])
    type_names: list = None
    unique_keys: dict = field(default_factory=lambda: {})
    attribute_groups: list = None

    def create_schema(self):
        """
        Create LinkML from the structure that has been loaded to this class
        """
        self.schema_builder = SchemaBuilder(id = self.namespace, name = self.namespace_prefix)
        self.schema_builder.add_defaults()
        self.schema_builder.schema.title = 'CDISC Operational Data Model v2'
        self.schema_builder.schema.description = 'ODM is a vendor-neutral, platform-independent format for exchanging and archiving clinical and translational research data, along with their associated metadata, administrative data, reference data, and audit information.'
        self.schema_builder.schema.prefixes['ncit'] = Prefix('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
        self.schema_builder.schema.prefixes['xml'] = Prefix('xml', 'http://www.w3.org/XML/1998/namespace#')
        self.schema_builder.schema.prefixes['xhtml'] = Prefix('xhtml', 'http://www.w3.org/1999/xhtml#')
        self.schema = SchemaView(self.schema_builder.schema)

        groups = self.structure.get('xs:group', [])
        simple_types = self.structure.get('xs:simpleType', [])
        elements = self.structure.get('xs:element', [])
        self.attribute_groups = self.structure.get('xs:attributeGroup', [])
        self.class_names = [elem.get('name') for elem in elements]
        self.type_names = [t.get('name') or t.get('ref') for t in simple_types]

        _ = self.create_subsets(groups)
        _ = self.create_slots()
        _ = [self.create_simple_type(t, t.get('name')) for t in simple_types]
        _ = [self.create_class(elem) for elem in elements]
        _ = self.apply_class_relationships()
        _ = self.hardcoded_modifications()

    def hardcoded_modifications(self):
        """
        Content that is different from the Source Schema
        """
        # Changed ODMVersion simple type to ODMVersionType to avoid collision with slot name
        # Forced slot names to begin with lower-case letter to avoid collision with classes

        # New Type for renamed XML Schema-specific element: internationalisation/localisation attribute
        range = LANGUAGE_KEY + 'Type'
        self.schema.add_slot(
            SlotDefinition(name =LANGUAGE_KEY, range = range, 
                description = 'language context for internationalisation and localisation'))
        self.schema.add_type(
            TypeDefinition(uri = 'xml:lang', name = range, base = 'str',
                description = 'language context for internationalisation and localisation'))
        
        # New Slot for renamed XML Schema-specific elements: text between tags
        range = CONTENT_KEY + 'Type'
        self.schema.add_slot(
            SlotDefinition(name = CONTENT_KEY, range = range, inlined = True,
                description = 'multi-line text content from between XML tags'))
        self.schema.add_type(
            TypeDefinition(uri='xhtml:div', name = range, base = 'str',
                description = 'multi-line text content from between XML tags'))
        
        # Workaround for ODM root class name clash: ODMFileMetadata
        clashing_class = self.schema.get_class('ODM')
        if clashing_class:
            clashing_class.name = 'ODMFileMetadata'
            clashing_class.tree_root = True
            self.schema.add_class(clashing_class)
            self.schema.delete_class('ODM')

        # Improvements on XML: create direct references instead of oidref, simplify classes with a single attribute
        for class_name, class_def in self.schema.schema.classes.items():
            # print(class_name)
            for slot_name in class_def.slots:
                if 'any_of' in self.schema.schema.classes[class_name]['slot_usage'][slot_name]:
                    # add references to permitted ranges in slot_usage
                    ranges = self.schema.schema.classes[class_name]['slot_usage'][slot_name]['any_of']
                    reference_index = next((index for index, d in enumerate(ranges) if d.get('range') == 'oidref'), -1)
                    if reference_index >= 0:
                        any_of = self.schema.schema.classes[class_name]['slot_usage'][slot_name]['any_of']
                        any_of.pop(reference_index)
                        any_of_new = list(set(any_of + [{'range': r} for r in self.find_reference_targets(slot_name)]))
                        self.schema.schema.classes[class_name]['slot_usage'][slot_name]['any_of'] = any_of_new
                elif 'range' in self.schema.schema.classes[class_name]['slot_usage'][slot_name]:
                    # replace range reference in slot_usage
                    if self.schema.schema.classes[class_name]['slot_usage'][slot_name]['range'] == 'oidref':
                        matches = self.find_reference_targets(slot_name)
                        if len(matches) > 1:
                            self.schema.schema.classes[class_name]['slot_usage'][slot_name]['range'] = None
                            self.schema.schema.classes[class_name]['slot_usage'][slot_name]['any_of'] = [{'range': m} for m in matches]
                        if len(matches) == 1:
                            self.schema.schema.classes[class_name]['slot_usage'][slot_name]['range'] = matches[0]
                if len(self.schema.schema.slots[slot_name]['any_of']) > 0:
                    # add references to permitted ranges in slot
                    ranges = self.schema.schema.slots[slot_name]['any_of']
                    reference_index = next((index for index, d in enumerate(ranges) if d.get('range') == 'oidref'), -1)
                    if reference_index >= 0:
                        any_of = self.schema.schema.slots[slot_name]['any_of']
                        any_of.pop(reference_index)
                        any_of_new = any_of + [{'range': r} for r in self.find_reference_targets(slot_name)]
                        self.schema.schema.slots[slot_name]['any_of'] = any_of_new
                elif 'range' in self.schema.schema.slots[slot_name]:
                    # replace range reference in slot
                    if self.schema.schema.slots[slot_name]['range'] == 'oidref':
                        matches = self.find_reference_targets(slot_name)
                        if len(matches) > 1:
                            self.schema.schema.slots[slot_name]['range'] = None
                            self.schema.schema.slots[slot_name]['any_of'] = [{'range': m} for m in matches]
                        if len(matches) == 1:
                            self.schema.schema.slots[slot_name]['range'] = matches[0]

                # Simplify structures where the only slot is 'content' i.e. multi-line text from XML
                # Find references to these classes from slot ranges then remove the class, and instead make the slot range 'text'
                slot_usage = self.schema.schema.classes[class_name]['slot_usage'][slot_name]
                slot = self.schema.schema.slots[slot_name]
                multivalued = slot_usage['multivalued'] if 'multivalued' in slot_usage else False
                multivalued = multivalued or slot['multivalued'] if 'multivalued' in slot else False
                if not multivalued and len(class_def.slots) == 1:
                    range = slot_usage['range'] if 'range' in slot_usage else None
                    print('Consider removing', class_name, 'and replacing its references with', range, 'since it only has 1 slot', slot_name)

    # Feedback for XML Schema
    #               
    # DocumentRef.leafID is identifier 'oid' while SourceItem.leafID is reference 'oidref'
    # Consider giving different names since one is a reference and the other is an identifier
    #
    # Coding.commentOID is range 'text' when it should be 'oidref' for consistency with other ways this slot gets used
    # This does not get linked to CommentDef because links expect 'oidref' type in XML schema         
    #
    # Potential ambiguity issues with Signature/SignatureDef, Comment/CommentDef, Transition/TargetTransition
    
    def find_reference_targets(self, slot_name) -> list:
        """
        Detect direct references to classes by parsing name i.e. <prefixWords>OID
        such that "unitsItemOID" detects "ItemDef" as a reference target.
        Exceptions capture mappings not matching prefix or with ambiguous classes
        """
        exceptions = {
            'priorFileOID' : ['ODMFileMetadata'],
            'commentOID': ['CommentDef'],
            'leafID': ['Leaf'],
            'archiveLocationID': ['Leaf'],
            'targetTransitionOID': ['Transition'],
            'signatureOID': ['SignatureDef'],
            'startOID' : ['StudyEventGroupDef', 'StudyEventDef', 'ItemGroupDef', 'ItemDef'],
            'endOID' : ['StudyEventGroupDef', 'StudyEventDef', 'ItemGroupDef', 'ItemDef'],
            'predecessorOID' : ['StudyEventGroupDef', 'StudyEventDef', 'ItemGroupDef', 'ItemDef'],
            'successorOID' : ['StudyEventGroupDef', 'StudyEventDef', 'ItemGroupDef', 'ItemDef'],
            'structuralElementOID' : ['Study', 'Epoch', 'StudyEventGroupDef', 'StudyEventDef', 'ItemGroupDef', 'ItemDef'],
            'sourceOID' : ['StudyEventGroupDef', 'StudyEventDef', 'ItemGroupDef', 'ItemDef', 'Branching'],
            'targetOID' : ['StudyEventGroupDef', 'StudyEventDef', 'ItemGroupDef', 'ItemDef', 'Branching']
        }
        if slot_name in exceptions:
            return exceptions[slot_name]
        else:
            prefix_words = re.findall(r"[A-Z]?[a-z]+", slot_name.rstrip("OID"))
            potential_matches = [''.join(prefix_words[i:])  for i, _ in enumerate(prefix_words)]
            potential_matches = [m[0].upper() + m[1:] for m in potential_matches]
            potential_matches = potential_matches + [m + 'Def' for m in potential_matches]
            matches = [m for m in potential_matches if m in self.class_names]
            if len(matches):
                return matches
            print(f'no match for {slot_name} referencing any of {potential_matches}')
            return None

    @staticmethod
    def map_slot_name(ref) -> str:
        # Slot names that are not permissible Python names
        if not ref or not isinstance(ref, str):
            return None
        slot_map = {
            'Class': 'itemGroupClass',
            'xlink:href': 'href',
            'xml:lang': LANGUAGE_KEY,
            'xhtml:div': CONTENT_KEY
        }
        if ref in slot_map.keys():
            ref = slot_map[ref]
        
        return ref if ref in ['OID', 'ID'] else ref[0].lower() + ref[1:]
        
    @staticmethod
    def map_range(range) -> str:
        type_map = {
            'href': 'uriorcurie',
            LANGUAGE_KEY: LANGUAGE_KEY + 'Type',
            CONTENT_KEY: CONTENT_KEY + 'Type'
        }
        if range in type_map.keys():
            range = type_map[range]
            return range
        else:
            return None 

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
        # Correct any incompatible or colliding type names
        # Remove prefixes for LinkML type references
        if ref is None:
            return None
        result = re.search(r'{.*?}(\w+)', ref)
        ref = result.group(1) if result else ref
        ref = ref.replace('@', '')
        type_map = {
            'xs:anyURI': 'uriorcurie',
            'xs:ID': 'oid',
            'xs:IDREF': 'oid',
            'xlink:href': 'href',
            'xml:lang': LANGUAGE_KEY,
            'xhtml:div': CONTENT_KEY,
            'name': 'nameType',
            'subjectKey': 'subjectKeyType',
            'value': 'valueType'
        }
        if ref in type_map.keys():
            return type_map[ref]
        else:
            return ref.split(':')[-1].strip()
    
    @staticmethod
    def map_context(context) -> str:
        # determine prefix from provided xsd annotation context
        context_map = {
            'nci:ExtCodeID': 'ncit'
        }
        if context in context_map.keys():
            return context_map[context]
        else:
            print('Unmapped context:', context)
            return context 

    @staticmethod
    def is_identifier(range) -> bool:
        return bool(range in ['oid'])

    def print_debug(self, *args) -> None:
        if DEBUG:
            print(*args)
        

    def create_subsets(self, element_groups) -> None:
        # https://linkml.io/linkml-model/docs/SubsetDefinition
        self.look_up_membership = {}
        for g in element_groups:
            group = g.get('name')
            sequence = g.get('xs:sequence', {})
            value_list = [e for e in sequence.get('xs:element')] if sequence else None
            self.look_up_membership[group] = value_list
            self.print_debug('creating subset', group)
            subset = SubsetDefinition(group)
            subset.from_schema = self.namespace
            self.schema.schema.subsets[subset.name] = subset


    def create_slots(self) -> None:
        # https://linkml.io/linkml-model/docs/SlotDefinition/
        slots = {}
        slot_names = []
        for ag in self.attribute_groups:
            for attribute in ag.get('xs:attribute', []):
                ref = self.map_type(attribute.get('ref'))
                name = attribute.get('name') or ref
                range = self.map_type(attribute.get('type'))
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
            self.print_debug('creating slot', slot_name)
            name = slots[slot_name].get('name')
            description = slots[slot_name].get('description')
            ref = slots[slot_name].get('ref')
            ranges =  slots[slot_name].get('ranges', ref) 
            slot = SlotDefinition(name = self.map_slot_name(slot_name))
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
            if self.is_identifier(slot.range):
                slot.identifier = True
            self.schema.add_slot(slot)

        self.slot_names = slot_names
        return None


    # Assemble enumerations / controlled terminology
    def create_enumeration(self, enumerations, enum_name, alias, as_children = True) -> None:
        # https://linkml.io/linkml-model/docs/EnumDefinition
        self.print_debug('creating enumeration', enum_name)
        this_enum = EnumDefinition(name = enum_name)
        values = {}
        enum_meaning = None
        for v in enumerations:
            this_value = {}
            if isinstance(v, str):
                enum_value = v
            if isinstance(v, dict):
                enum_value = v.get('value')
                appinfo = v.get('xs:annotation', {}).get('xs:appinfo')
                if appinfo:
                    aliases = appinfo[0].get('odm:Alias', {})
                    enum_meaning = ':'.join([self.map_context(aliases[0].get('Context')), 
                                             aliases[0].get('Name')])
                enum_documentation = v.get('xs:annotation', {}).get('xs:documentation')
                enum_description = '\n'.join(enum_documentation) if enum_documentation else None
                this_value['description'] = enum_description or None
                this_value['meaning'] = enum_meaning or None
                this_value['is_a'] = enum_name if as_children else None
            values[enum_value] = this_value
        this_enum.permissible_values = values

        if alias:
            this_enum.conforms_to = self.map_context(alias[0].get('Context'))
            this_enum.aliases = alias[0].get('Name')
            this_enum.code_set = ':'.join([this_enum.conforms_to, this_enum.aliases])
        self.schema.add_enum(this_enum)


    # Assemble types and their restrictions
    def create_simple_type(self, element, type_name) -> None:
        # https://linkml.io/linkml-model/docs/TypeDefinition
        type_name = self.map_type(type_name)
        if self.schema.get_type(type_name):
            return None
        self.print_debug('creating type', type_name)
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
                    type.exact_mappings = [':'.join([self.map_context(a.get('Context')), 
                                                     a.get('Name')]) for a in alias]

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


    def get_attribs_from_group(self, name) -> [dict]:
        matches = [
            ag.get('xs:attribute') for ag in self.attribute_groups
            if ag['name'] == name
            ]
        if not matches:
            return None
        return  matches[0]


    @staticmethod
    def get_groups(element, look_up_membership) -> [str]:
        groups_found = []
        for name, ref_list in look_up_membership.items():
            if not ref_list:
                continue
            for ref in ref_list:
                if element == ref:
                    groups_found.append(name)
        return groups_found
    

    def map_reference(self, element, unique_list = None, min_occurs = None, max_occurs = None) -> dict:
        if not element:
            return None
        range = self.map_type(element.get('ref'))
        name = element.get('name') or range
        self.print_debug('mapping reference', name)
        min_occurs = min(min_occurs or 0, element.get('minOccurs', 0))
        max_occurs = max_occurs or element.get('maxOccurs')
        documentation = element.get('xs:annotation', {}).get('xs:documentation',[])
        return {
            'name': self.map_slot_name(name),
            'range': self.map_range(range) or range,
            'required': True if (int(min_occurs) and int(min_occurs) > 0) else None,
            'multivalued': True if max_occurs == 'unbounded' else None,
            'inlined': True if max_occurs == 'unbounded' else None,
            'inlined_as_list': True if max_occurs == 'unbounded' else None,
            'minimum_cardinality': int(min_occurs) or None,
            'maximum_cardinality': None if max_occurs == 'unbounded' else int(max_occurs),
            'description': '\n'.join(documentation) if documentation else None,
            'list_elements_unique': True if unique_list and name in unique_list else None
        } if name else None
    

    def process_attribute_group(self, slot_usage, attribute_group) -> dict:
        group_name = self.map_type(attribute_group.get('ref'))
        if not group_name:
            print('no attribute group found', attribute_group)
            return slot_usage
        self.print_debug('processing attribute group', group_name)
        attribs = self.get_attribs_from_group(name = group_name)
        if not attribs:
            return slot_usage
        for attrib in attribs:
            attrib_name = attrib.get('name') or self.map_type(attrib.get('ref'))
            if not attrib_name:
                self.print_debug('attribute has no name', attrib)
                return slot_usage
            attrib_name = self.map_slot_name(attrib_name)
            required = True if (attrib.get('use') == 'required') else None
            this_slot_usage = {'required': required}
            range = self.map_type(attrib.get('type')) or self.map_range(attrib_name)
            if self.is_identifier(range):
                this_slot_usage['identifier'] = True
            simpleType = attrib.get('xs:simpleType')
            if not range and not simpleType:
                print('no type/s provided for', attrib_name, 'in', group_name)
            if simpleType and simpleType.get('xs:union'):
                types = simpleType.get('xs:union', {}).get('memberTypes', {})
                range_list = [{'range': self.map_type(t)} for t in types]
                this_slot_usage['any_of'] = range_list
            else:
                this_slot_usage['range'] = range
            slot_usage[attrib_name] = this_slot_usage
        return slot_usage  


    def create_class(self, element) -> None:
        # https://linkml.io/linkml-model/docs/ClassDefinition/
        class_name = element.get('name')
        self.print_debug('creating class', class_name)
        if not class_name:
            print('no element name', element)
        matching_types = [t for t in self.structure.get('xs:complexType') if element.get('type') == t.get('name')]
        if not matching_types:
            print('no type definition found for', element.get('type'))
        props = matching_types[0]
        if not props:
            print('no class definition found for element', class_name)
            return None

        klass = ClassDefinition(class_name)
        if props.get('xs:annotation'):
            klass.description = '\n'.join(props.get('xs:annotation').get('xs:documentation'))
        klass.see_also = f'https://wiki.cdisc.org/display/PUB/{class_name}'
        # Handle unique relation constraints
        unique = element.get('xs:unique')
        selector_list = []
        if unique:
            if type(unique) == dict:
                unique = [unique]
            for un in unique:
                constraint_name = un.get('name')
                relation_targets = []
                for field in  un.get('xs:field'):
                    for xpath in field.values():
                        if not xpath:
                            continue
                        field = self.map_type(xpath)
                    relation_targets.append(field)

                selector = None
                for v in un.get('xs:selector').keys():
                    selector = self.map_type(v)
                    constraint = {constraint_name : {'unique_key_slots': relation_targets}}
                    selector_repr = ['.'.join([selector, t]) for t in relation_targets]
                    self.print_debug('creating unique constraint from', class_name, 'to', selector_repr)
                    self.unique_keys[selector] = constraint
                    selector_list.append(selector)

        # extract slots from groups listed at various levels
        slot_usage = {}
        slots = []
        slot_groups = []
        slot_groups.extend(props.get('xs:simpleContent', {}).get('xs:extension', {}).get('xs:attributeGroup', []))
        slot_groups.extend(props.get('xs:complexContent', {}).get('xs:restriction', {}).get('xs:attributeGroup', []))
        slot_groups.extend(props.get('xs:attributeGroup', []))
        for ag in slot_groups:
            slot_usage = self.process_attribute_group(slot_usage, ag)
        slots = [k for k in slot_usage.keys()]

        # Identify groups that have this class as a member
        groups_found = self.get_groups(class_name, self.look_up_membership)
        subsets = [SubsetDefinitionName(g) for g in groups_found]
        if groups_found:
            klass.in_subset = subsets[0]

        # Relationships to other classes
        sequence = props.get('xs:sequence')
        slot_usage, slots = self.process_refs(sequence, slot_usage, slots, selector_list)

        # Create a slot for unnamed content between XML tags
        xml_content_base = props.get('xs:simpleContent', {}).get('xs:extension', {}).get('base')
        match xml_content_base:
            case 'text' | 'datetime' | 'value' | 'name':
                xml_content_base = self.map_type(xml_content_base)
                slot_usage[CONTENT_KEY] = {'range': xml_content_base}
                slots.append(CONTENT_KEY)
                self.print_debug('xml content base type:', xml_content_base)
            case None:
                pass
            case _:
                print('content base new type:', xml_content_base)

        klass.slot_usage = slot_usage
        klass.slots = slots
        klass.class_uri = self.namespace_prefix + ':' + class_name
        self.schema.add_class(klass)


    def apply_class_relationships(self):
        for class_name, unique_keys in self.unique_keys.items():
            klass = None
            class_list = [klass for k, klass in self.schema.schema.classes.items() if class_name == k]
            if class_list:
                klass = class_list[0]
            if not klass:
                continue
            self.print_debug('adding unique keys to', class_name)
            self.schema.schema.classes.pop(class_name)
            klass['unique_keys'] = unique_keys
            self.schema.add_class(klass)


    def add_class_slot(self, element, unique_list = None, min_occurs = None, max_occurs = None):
        if type(element) is not dict:
            self.print_debug('element passed to add_class_slot was not dict type')
            return None
        else:
            mapped = self.map_reference(element, 
                                        unique_list = None,
                                        min_occurs = min_occurs,
                                        max_occurs = max_occurs)
        if not mapped:
            return None
        ref_name = mapped.get('name')
        range = mapped.get('range')
        if ref_name:
            this_slot = SlotDefinition(ref_name)
            this_slot['range'] = range
            if self.is_identifier(range):
                this_slot['identifier'] = True
            this_slot['description'] = mapped.get('description')
            this_slot['name'] = ref_name
            if ref_name not in self.slot_names:
                self.print_debug('adding class slot', ref_name)
                self.schema.add_slot(this_slot)

            return mapped
        else:
            print('No name found for', mapped)
            return None


    def process_refs(self, element, slot_usage, slots, selector_list, has_choice = False) -> [dict, list]:
        """
        Recursive processing of xs:sequence, xs:choice, xs:element and xs:group
        """
        if not element:
            return slot_usage, slots
        
        sequence_elements = None
        container_type = 'exactly_one_of'
        if has_choice:
            sequence_elements = element.get('xs:sequence', {}).get('xs:element', [])
            container_type = 'any_of' if sequence_elements else 'exactly_one_of'
            slot_usage[container_type] = {}
            for relation in sequence_elements:
                mapped = self.add_class_slot(relation, selector_list)
                if has_choice:
                    mapped['minimum_cardinality'] = None
                    mapped['required'] = None
                if not mapped:
                    continue
                ref_name = mapped.pop('name')
                slots.append(ref_name)
                slot_usage[ref_name] = mapped
                # TODO get conditionals/unions working e.g. via PostConditions
                # Unions and conditionals are not yet supported by LinkML e.g.
                # RangeCheck: exactly_one_of(all_of(FormalExpression, MethodSignature), CheckValue)
                # FormalExpression: exactly_one_of(Code, ExternalCodeLib)
                # slot_usage[container_type][ref_name] = mapped
        
        relations = element.get('xs:element', {})
        if type(relations) == dict:
            relations = [relations]
        for relation in relations:
            mapped = self.add_class_slot(relation, selector_list)
            if mapped:
                ref_name = mapped.pop('name')
                # if has_choice:
                #     slot_usage[container_type][ref_name] = mapped
                # else:
                #     slot_usage[ref_name] = mapped
                slot_usage[ref_name] = mapped
                slots.append(ref_name)

        group_list = element.get('xs:group', [])
        if type(group_list) == dict:
            group_list = [group_list]
        for group in group_list:
            extension_ref = self.map_type(group.get('ref'))
            subset = self.look_up_membership.get(extension_ref)
            if not subset:
                continue
            for ref in subset:
                mapped = self.add_class_slot(ref, 
                                             selector_list,
                                             min_occurs = group.get('minOccurs'),
                                             max_occurs = group.get('maxOccurs'))
                if mapped:
                    ref_name = mapped.pop('name')
                    slot_usage[ref_name] = mapped
                    slots.append(ref_name)

        choice = element.get('xs:choice')
        if choice:
            slot_usage, slots = self.process_refs(
                choice, slot_usage, slots, selector_list, has_choice = True
            )

        return slot_usage, slots


    def supplement_with_wiki(self) -> None:
        """
        Scrape ODMv2 wiki and add structured content
        """
        headers = scraper.connect()
        print('Scraping class info from wiki')
        for klass in self.class_names:
            scraped = scraper.scrape_wiki_content(klass, headers = headers)
            if not scraped:
                continue
            fixed_klass = 'ODMFileMetadata' if klass == 'ODM' else klass
            schema_description = self.schema.schema.classes[fixed_klass]['description']
            wiki_description = scraped.get('description')
            self.schema.schema.classes[fixed_klass]['description'] = schema_description or wiki_description
            wiki_examples = scraped.get('examples') or []
            fixed_examples = []
            example_number = 0
            for example in wiki_examples:
                example_number += 1
                example_object = Example(example)
                fixed_examples.append(example_object)
            # self.schema.schema.classes[fixed_klass]['examples'] = fixed_examples

            attribute_table = scraped.get('attribute_table', [])
            for slot in attribute_table:
                description = slot.get('Definition')
                schema_slot_description = None
                slot_usage = None
                slot_name = slot.get('Attribute')
                if not slot_name:
                    continue
                slot_name = self.map_slot_name(slot_name)
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
                    external_comments.append('enum values: ' + data_type)
                elif data_type:# TODO: check wiki vs XML Schema for range
                    external_comments.append('range: ' + data_type)
                    range = data_type
                rules = slot.get('Business Rule(s)')
                if rules:
                    external_comments.append(rules)      
                
                # Defensive schema object access in case missing from imported schema
                try:
                    slot_usage = self.schema.schema.classes[fixed_klass]['slot_usage']
                    try:
                        this_slot_usage = self.schema.schema.classes[fixed_klass]['slot_usage'][slot_name]
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
                self.schema.schema.classes[fixed_klass]['slot_usage'][slot_name]['description'] = \
                    schema_class_slot_description or description

                slot_entry = None
                try:
                    slot_entry = self.schema.schema.slots[slot_name]            
                    try:
                        this_slot_entry = self.schema.schema.slots[slot_name]['description']
                    except KeyError:
                        this_slot_entry = None
                except KeyError:
                    print('slot', slot_name, 'from wiki page for class', fixed_klass, 'was not found in slots')

                if slot_entry:
                    original_description = slot_entry['description']
                    self.schema.schema.slots[slot_name]['description'] =  \
                        original_description or schema_class_slot_description or description
                
                if external_comments:
                    self.schema.schema.classes[fixed_klass]['slot_usage'][slot_name]['comments'] = \
                        '\n'.join(external_comments)


    def record_enum_usage(self, enum_usage, range, slot_name) -> list:
        if range in list(self.schema.schema.enums.keys()):
            value = enum_usage[range] or [] if range in enum_usage.keys() else []
            value.append(slot_name)
            enum_usage[range] = value
        return enum_usage


    def patch_descriptions(self) -> None:
        """
        Handle missing descriptions
        """
        enum_usage = {}

        # Classes - throw error
        for class_name, klass in self.schema.schema.classes.items():
            if not klass['description']:
                print('No description found for class', class_name)
            slot_usage = klass['slot_usage']
            for slot_name in slot_usage:
                if slot_name not in self.schema.schema.slots.keys():
                    continue
                range = self.schema.schema.slots[slot_name]['range']
                enum_usage = self.record_enum_usage(enum_usage, range, slot_name)
                any_of = self.schema.schema.slots[slot_name]['any_of']
                for r in any_of:
                    enum_usage = self.record_enum_usage(enum_usage, r.get('range'), slot_name)

        # Slots - for references f'{class} reference: {description}'. throw error, otherwise
        for slot_name, slot in self.schema.schema.slots.items():
            range = slot['range']
            original_slot_description = slot['description']
            ref_description = None
            enum_usage = self.record_enum_usage(enum_usage, range, slot_name)
            any_of = slot['any_of']
            for r in any_of:
                enum_usage = self.record_enum_usage(enum_usage, r.get('range'), slot_name)
            if range in list(self.schema.schema.classes.keys()):
                try:
                    class_description = self.schema.schema.classes[range]['description'] or None
                except KeyError:
                    class_description = None
                ref_description = f'{range} reference: {class_description}'
            self.schema.schema.slots[slot_name]['description'] = original_slot_description or ref_description
        if not self.schema.schema.slots[slot_name]['description']:
            print('No description found for slot', slot_name)
        
        # Enumerations - report where they are used
        for enum_name, enum in self.schema.schema.enums.items():
            original_description = enum['description']
            description = None
            if enum_name in list(enum_usage.keys()):
                description = f'Enumeration used in {", ".join(list(set(enum_usage[enum_name])))}'
            self.schema.schema.enums[enum_name]['description'] = original_description or description
        if not self.schema.schema.enums[enum_name]['description']:
            print('No description or usage found for Enum:', enum_name)

        # Types - hardcode description where missing
        for type_name, type in self.schema.schema.types.items():
            if self.schema.schema.types[type_name]['from_schema'] != self.namespace:
                continue
            if not self.schema.schema.types[type_name]['description']:
                self.schema.schema.types[type_name]['description'] = self.type_documentation
            self.schema.schema.types[type_name]['see_also'] = self.type_documentation
        if not self.schema.schema.types[type_name]['description']:
            print('No description found for Type:', type_name)

        return None