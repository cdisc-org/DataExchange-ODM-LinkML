# Class: AnnotatedCRF

_An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document that provides the mapping of data collection fields to the variables or discrete variable values contained within the datasets._




URI: [odm:AnnotatedCRF](http://www.cdisc.org/ns/odm/v2.0/AnnotatedCRF)


```mermaid
erDiagram
AnnotatedCRF {

}
DocumentRef {
    oid leafID  
}
PDFPageRef {
    text pageRefs  
    positiveInteger firstPage  
    positiveInteger lastPage  
    PDFPageType type  
    text title  
}

AnnotatedCRF ||--}o DocumentRef : "documentRef"
DocumentRef ||--}o PDFPageRef : "pDFPageRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [documentRef](documentRef.md) | 0..* <br/> [DocumentRef](DocumentRef.md) | Links to a def:leaf element with the location of the document. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [annotatedCRF](annotatedCRF.md) | range | [AnnotatedCRF](AnnotatedCRF.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/AnnotatedCRF](https://wiki.cdisc.org/display/PUB/AnnotatedCRF)

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
- https://wiki.cdisc.org/display/PUB/AnnotatedCRF
rank: 1000
slots:
- documentRef
slot_usage:
  documentRef:
    name: documentRef
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
- https://wiki.cdisc.org/display/PUB/AnnotatedCRF
rank: 1000
slot_usage:
  documentRef:
    name: documentRef
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
  documentRef:
    name: documentRef
    description: Links to a def:leaf element with the location of the document.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: documentRef
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