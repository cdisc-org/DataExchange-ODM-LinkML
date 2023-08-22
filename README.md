# CDISC Operational Data Model Structure Descriptions
Explore this repo to find the format that best suits your project

[Documentation here](https://cdisc-org.github.io/DataExchange-ODM-LinkML/) describes the model in-depth

# Motivation for expressing ODMv2 beyond XML

## FAIR clinical data (findable, accessible, interoperable, reusable)
Adopting CDISC exchange standards for apps and automation minimises technical debt and makes clinical data FAIR end-to-end

## Metadata-first, semantic datasets
Clinical data can be piped to analysis-ready datasets according to the Define-XML specs (ODMv1). Instead of using it an automation spec, however, implementers treated dataset creation as manual and Define creation as post-hoc bureucracy. The largely SAS-based community of clinical programmers found XML too inaccessible to take advantage of the data structure

With lessons learned from iterating on ODMv1, ODMv2 is a mature enough description of clinical data to bring to the semantic web. The intent is for a broader range of developers, data engineers and data scientists to get easy access to the benefits of structured data

## Convergence through utility
ODM expressed in every popular structured data format so that it is easier for developers to pick it up and apply to their project than to build their own model

# LinkML and JSON-LD
Between these 2 frameworks we can translate ODMv2 data & schemata into helpful representations

[LinkML](https://linkml.io/) can convert a schema into
* [JSON](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/jsonschema/ODM.schema.json)
* [GraphQL](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/graphql/ODM.graphql)
* [SQL](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/sqlschema/ODM.sql)
* [Python dataclasses](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/ODM.py)
* [RDF: OWL](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/owl/ODM.owl.ttl)
* [RDF: SCHACL](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/shacl/ODM.shacl.ttl)
* [Protobuf](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/protobuf/ODM.proto)
* [Excel](https://github.com/cdisc-org/DataExchange-ODM-LinkML/blob/main/excel/ODM.xlsx)
* [Markdown documentation on Github pages](https://cdisc-org.github.io/DataExchange-ODM-LinkML/)
* [... and more including Pydantic, Java, JS, TS](https://linkml.io/linkml/generators/index.html)

[JSON-LD](https://json-ld.org/) serialises RDF as JSON, helping to
* translate between a JSON file (e.g. Dataset-JSON) and a RDF graph according to a defined context
* add semantics to existing JSON used in applications
* frame structured data into different layouts
* tell the semantic web what your site/document/file contains (how Googling works)
* compact graph data into JSON form or expand it back, e.g. for an API

## Limitations in LinkML as of Q3 2023
- No translation either to or from XML Schema
- Scope for adoption limited to life sciences community so far, relatively young project
- Conversion to JSON-LD is not mature so JSON-LD needs separate handling
- Names in ODM need changing to avoid collisions between Slots/Types/Classes
- Handling of conditional slot population rules: exactly_one_of, any_of, all_of, none_of
- Capitalises Type names in documentation and Python outputs (to preserve case-sensitive names, remove camelcase applied to returned values in your installed LinkML source files e.g. `DocumentGenerator.name()`, `DocumentGenerator.link()` from linkml/generators/docgen.py)
- ER diagram rendered in markdown is too small and not zoomable if number of classes is large `--include-top-level-diagram --diagram-type er_diagram`

# How to generate schemata and documentation from source ODM XML
    git clone https://github.com/cdisc-org/DataExchange-ODM.git
    git clone https://github.com/cdisc-org/DataExchange-ODM-LinkML.git
    cd DataExchange-ODM-LinkML
    pip install -r requirements.txt
    
    python3 tools/odm2linkml.py ../DataExchange-ODM/schema/ODM.xsd --output ODM.yaml

    gen-project -d . ODM.yaml --exclude shex --exclude markdown

More detailed relationship and cardinality constraints still need to be ported from XML Schema before shex can be added.

As content is added, refresh documentation and diagrams using `mkdocs` to keep it up to date with the latest batch of generated .md files

    gen-doc ODM.yaml --directory docs/ --hierarchical-class-view
    mkdocs build

to check the updated documentation changes locally

    mkdocs serve

and eventually upload them to Github pages (you need to have set up your Github access, and it takes time for changes to be picked up)

    mkdocs gh-deploy

# Conversion to JSON-LD and LinkML

## Strategy
Break down the XML Schema into a consumable format, then pick one of the target frameworks to work on first. Ideally the one that most helps bootstrap the next format

JSON-LD first
* having the JSON framed with embedding makes it more readable. It might be useful to have it in this format when translating to LinkML YAML
* creates reusable `"@context"` for other XML schemata as JSON
* forms basis of JSON-LD representation of ODMv2 graph

Alternatively, LinkML YAML first
* more useful up-front
* translates to many representations for comprehension
* basic generator already in place for creation of JSON-LD from LinkML YAML

LinkML was chosen to start with as it is closer to a schema and can generate a primitive JSON-LD @context (unlike a schema, @context primarily applies semantics to structure)

Can then create JSON-LD @context knowing both input (ODM as JSON) and output (ODM as RDF via LinkML)


## Breakdown of XML schema structure as JSON
After flattening the .xsd schema files into a single schema, ODMv2 can be read in and explored as a Python dictionary via the `xmlschema` package (dicts are almost identical to JSON)

    xs:simpletype has many elements (78) | value (non-object) types
        { name of type, 
            xs:restriction{base, xs:pattern{value}, xs:union{[membertypes]}, xs:enumeration[value] }, 
            xs:annotation{[xs:documentation], xs:appinfo[{odm:Alias}]} }
    xs:attributeGroup has many elements ( 243 ) | group of attributes referred to by element
        {name of grouped attribute definition, [xs:attribute]}
    xs:group has many elements ( 122 ) | group of variables e.g. an extension, audit signature records
        {name of group, xs:sequence{xs:element[ref, minOccurs, maxOccurs, nillable]} }
    xs:complexType has many elements ( 146 ) | type for objects
        { name of type, abstract, mixed
        xs:sequence{minOccurs, maxOccurs, xs:element[{ref, maxOccurs, minOccurs, nillable}]
        xs:group{ref, minOccurs, maxOccurs}}
        xs:attributeGroup[{ref}]
        xs:annotation{[xs:documentation], xs:appinfo[{odm:Alias}]} }
        xs:complexContent{xs:restriction{base, [xs:attributeGroup]}}
    xs:element has many elements ( 146 ) | classes and their relationships
        {name, type, abstract, nillable, minOccurs, maxOccurs,
         xs:unique[{name, {xs:selector}, [{xs:field}]}]}


## Translation from XML Schema

* `xs:element` is a class

* `xs:complexType` is a class type or class slot type

* `xs:group` is a container referencing elements. In LinkML the direction of referencing is reversed. If element is found in a group, that element references the group via LinkML `in_subset`

* `xs:simpleType` is a primitive type or simple slot type

* `xs:attributeGroup` contain slots, referenced by a class at attributeGroup level. It lists someObjectDefinition with someObjectExtension to group them, bringing in any implementer-specific extensions to the model

Each `xs:attributeGroup` member looks like this i.e. the same slot can have a different label annotated from the point of view of its context

        {
          "name": "Name",
          "type": "StandardName",
          "use": "required",
          "xs:annotation": {
            "xs:documentation": [
              "Name of Standard."
            ]
          }
        }

* `xs:sequence` contains both self cardinality and relationships/cardinality to other classes
    * `xs:element` is list of relationships `ref` and their cardinalities `minOccurs` (int | 'unbounded'), `maxOccurs`, `nillable`
        * `mixed` is only applied to TranslatedText since there is content between the XML tags. In non-XML/HTML representations this would be given a key such as `"content"` or `"TranslatedText"`. Flickr use `"_content"` in their style guide to avoid collisions. Because `TranslatedText` is the only example of this in ODMv2 we give the content the attribute `TranslatedText`
        * `abstract` is false in all cases - there are no purely abstract classes to handle

* `xs:restriction` is rules around type and enumerated values of a slot
    * `base` is a primitive: 'xs:positiveInteger', 'xs:dateTime', 'xs:integer', 'xs:float', 'xs:time', 'xs:string', 'xs:hexBinary', 'xs:base64Binary', 'xs:date', 'xs:boolean', 'xs:decimal', 'xs:double', 'xs:anyURI'
    * `xs:enumeration` lists values and their NCI code, nested within a structure like this

            {
                "value": "ADaMIG",
                "xs:annotation": {
                    "xs:appinfo": [
                    {
                        "odm:Alias": [
                        {
                            "Name": "C170552",
                            "Context": "nci:ExtCodeID"
                        }
                        ]
                    }
                    ]
                }
            }

* `xs:documentation` list inside `xs:annotation` is a description. This could be label or a long multi-lined entry

* `xs:union: { memberTypes: [] } ` replaces `xs:restriction` when the type combines multiple other types

* `ref` references a named definition or class, e.g. in a relationship cardinality constraint

* `xs:simpleContent` contains `xs:extension` or restrictions on a text-only complextype; or on a simple type with only _content slot if it contains neither attributes nor elements.

* `xs:extension` consists of `base` and `xs:attributeGroup:[{ref}]` referencing the extension object

* `xs:complexContent` allows multiple attribute groups to be defined within the same class 
Only `Subclass` and `PDFPageRef` use this

* `odm:Alias` is an exact mapping to NCIT concept (more exact mappings can be added)

* `xs:choice` nests population rules via (exactly_one_of | all_of | any_of) for the following situations 
    * `FormalExpression` must have one of either `Code` or `ExternalCodeLib` populated
    * `RangeCheck` must have either `CheckValue`, or (`MethodSignature` and `FormalExpression`) populated


## Potential new functionality
LinkML has some [advanced features](https://linkml.io/linkml/schemas/advanced.html) that ODM could make use of

JSON-LD can transform CDISC JSON such Dataset-JSON into a semantic graph for enriched archiving, search, and retrieval


# Methods for converting ODM XML Schema (bundle of .xsd files)
## Rejected
* LinkML does not support XML Schema at all
* xml2dict (formerly Xml2json) works for simple XML, does not support XSD well
* GitHub - benscott/xsdtojson is incomplete / falls over with complex schema
* JSONIX Javascript lib is powerful but is no longer supported since the main author passed, and literal transformation from XML schema is rough - used in the Dataset-JSON hackathon to make a prototype Define-JSON
* Oxygen proprietary XML editor documentation mentions JSON schema creation from JSON and support for JSON schema handling within the JSON ecosystem. Could not find anything about XML schema to JSON schema. 

## Used
* xmlschema
* lxml


# Methods for creating LinkML schema
## Used
* LinkML generators applied to xmlschema object structure

## Not tried
* turn Python dataclass __dict__ into to linkml
* create JSON-LD @context for the xmlschema object structure