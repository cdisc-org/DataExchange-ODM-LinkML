# Motivation for expressing ODMv2 beyond XML
## FAIR clinical data (findable, accessible, interoperable, reusable)
ODM should be expressed in every popular structured data format so that it is the easiest resource for developers to reach to. Adopting CDISC exchange standards for apps and automation minimises technical debt and makes clinical data FAIR end-to-end.

## Metadata-first, semantic datasets
Clinical data can be piped to analysis-ready datasets according to the Define-XML specs (ODMv1). Instead of using it an automation spec, however, implementers have been treating dataset creation as manual and Define creation as post-hoc bureucracy. The largely SAS-based community of clinical programmers found XML too inaccessible to take advantage of the data structure.

With lessons learned from iterating on ODMv1, ODMv2 is a mature enough description of clinical data to bring to the semantic web. The intent is for a broader range of developers, data engineers and data scientists to get easy access to the benefits of structured data

# LinkML and JSON-LD
Between these 2 frameworks we can translate ODMv2 data & schemata into helpful representations

[LinkML](https://linkml.io/) can convert a schema into
* Markdown Documentation
* SQL Table Schema
* GraphQL Schema
* JSON Schema
* JSON, YAML
* Graphs and Shape Constraints (RDF, OWL, SHACL, SHEX)
* Python/Typescript/Java classes
* XLSX file with objects as tabs and attributes and columns
* CSV
* Mermaid entity-relationship diagrams

[JSON-LD](https://json-ld.org/) serialises RDF as JSON, helping to
* translate between a JSON file (e.g. Dataset-JSON) and a RDF graph according to a defined context
* add semantics to existing JSON used in applications
* frame structured data into different layouts
* tell the semantic web what your site/document/file contains (how Googling works)
* compact graph data into JSON form or expand it back, e.g. for an API

## Gaps in LinkML as of 2023-07-28
- No translation either to or from XML Schema
- Scope for adoption limited to life sciences community so far, relatively young project
- Conversion to JSON-LD is not mature so JSON-LD needs separate handling

# Steps to convert to JSON-LD and LinkML

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
After creating a flattening the .xsd schema files into a single schema, ODMv2 can be read in and explored as a Python dictionary via the `xmlschema` package (dicts are almost identical to JSON)

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

* `xs:attributeGroup` contain slots, referenced by a class at attributeGroup level. It lists someObjectDefinition with someObjectExtension to group them, bringing in any implementer-specific extensions to the model. Extensions could be ignored, as they are empty in the 'standard' schema (until there is demand from implementers who also use .xsd files)

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
    * `xs:group` is ignored at first
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

* `type` can take either a `xs:simpleType` or `xs:complexType`

* `ref` references a named definition or class, e.g. in a relationship cardinality constraint

* `xs:simpleContent` contains `xs:extension` or restrictions on a text-only complextype or on a simple type as content and contains noelements.

* `xs:extension` consists of `base` and `xs:attributeGroup:[{ref}]` referencing the extension object

* `xs:complexContent` allows multiple attribute groups to be 
Only `Subclass` and `PDFPageRef` use this

* `odm:Alias` is an exact mapping to NCIT concept (more exact mappings can be added)


## Potential new functionality
LinkML has some [advanced features](https://linkml.io/linkml/schemas/advanced.html) that ODM could make use of

JSON-LD can transform CDISC JSON such Dataset-JSON into a semantic graph for enriched archiving, search, and retrieval


# Solutions assessed for converting ODM XML Schema (bundle of .xsd files)
## Rejected
* LinkML does not support XML Schema at all
* xml2dict (formerly Xml2json) works for simple XML, does not support XSD well
* GitHub - benscott/xsdtojson is incomplete / falls over with complex schema
* JSONIX Javascript lib is powerful but is no longer supported since the main author passed, and literal transformation from XML schema is rough - used in the Dataset-JSON hackathon to make a prototype Define-JSON
* Oxygen proprietary XML editor documentation mentions JSON schema creation from JSON and support for JSON schema handling within the JSON ecosystem. Could not find anything about XML schema to JSON schema. 

## Useful / Worth another look
* xmlschema
* lxml

## To assess
* LinkML generators for LinkML
* See whether Python dataclass __dict__ can be turned into to linkml
* Consider building JSON-LD first to turn ODMv2 into a RDF graph


# Quick start
    git clone https://github.com/cdisc-org/DataExchange-ODM.git
    git clone https://github.com/cdisc-org/DataExchange-ODM-LinkML.git
    cd DataExchange-ODM-LinkML
    pip install -r requirements.txt
    
    python3 tools/odm2linkml.py ../DataExchange-ODM/schema/ODM.xsd --output ODM.yaml
    gen-project -d . ODM.yaml --exclude shex

More detailed relationship and cardinality constraints still need to be ported from XML Schema before shex can be added.

As content is added, refresh documentation and diagrams using `mkdocs` to keep it up to date with the latest batch of generated .md files

    mkdocs build

to explore the updated documentation changes locally

    mkdocs serve

and then upload them to where they are served

    mkdocs gh-deploy