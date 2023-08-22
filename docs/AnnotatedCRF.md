# Class: AnnotatedCRF

_An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document that provides the mapping of data collection fields to the variables or discrete variable values contained within the datasets._




URI: [odm:AnnotatedCRF](http://www.cdisc.org/ns/odm/v2.0/AnnotatedCRF)


```mermaid
erDiagram
AnnotatedCRF {

}
DocumentRef {
    oid LeafID  
}
PDFPageRef {
    text PageRefs  
    positiveInteger FirstPage  
    positiveInteger LastPage  
    PDFPageType Type  
    text TitleRef  
}

AnnotatedCRF ||--}o DocumentRef : "DocumentRefRef"
DocumentRef ||--}o PDFPageRef : "PDFPageRefRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [DocumentRefRef](DocumentRefRef.md) | 0..* <br/> [DocumentRef](DocumentRef.md) | Links to a def:leaf element with the location of the document. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [AnnotatedCRFRef](AnnotatedCRFRef.md) | range | [AnnotatedCRF](AnnotatedCRF.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/AnnotatedCRF](https://wiki.cdisc.org/display/ODM2/AnnotatedCRF)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:AnnotatedCRF |
| native | odm:AnnotatedCRF |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnnotatedCRF
description: An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document
  that provides the mapping of data collection fields to the variables or discrete
  variable values contained within the datasets.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/AnnotatedCRF
rank: 1000
slots:
- DocumentRefRef
slot_usage:
  DocumentRefRef:
    name: DocumentRefRef
    description: Links to a def:leaf element with the location of the document.
    multivalued: true
    domain_of:
    - AnnotatedCRF
    - SupplementalDoc
    - Origin
    - MethodDef
    - CommentDef
    range: DocumentRef
    inlined: true
    inlined_as_list: true
class_uri: odm:AnnotatedCRF

```
</details>

### Induced

<details>
```yaml
name: AnnotatedCRF
description: An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document
  that provides the mapping of data collection fields to the variables or discrete
  variable values contained within the datasets.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/AnnotatedCRF
rank: 1000
slot_usage:
  DocumentRefRef:
    name: DocumentRefRef
    description: Links to a def:leaf element with the location of the document.
    multivalued: true
    domain_of:
    - AnnotatedCRF
    - SupplementalDoc
    - Origin
    - MethodDef
    - CommentDef
    range: DocumentRef
    inlined: true
    inlined_as_list: true
attributes:
  DocumentRefRef:
    name: DocumentRefRef
    description: Links to a def:leaf element with the location of the document.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: DocumentRefRef
    owner: AnnotatedCRF
    domain_of:
    - AnnotatedCRF
    - SupplementalDoc
    - Origin
    - MethodDef
    - CommentDef
    range: DocumentRef
    inlined: true
    inlined_as_list: true
class_uri: odm:AnnotatedCRF

```
</details>