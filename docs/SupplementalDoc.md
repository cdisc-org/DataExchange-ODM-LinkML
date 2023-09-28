# Class: SupplementalDoc

_Supplemental data definitions_




URI: [odm:SupplementalDoc](http://www.cdisc.org/ns/odm/v2.0/SupplementalDoc)


```mermaid
erDiagram
SupplementalDoc {

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

SupplementalDoc ||--}o DocumentRef : "documentRef"
DocumentRef ||--}o PDFPageRef : "pDFPageRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [documentRef](documentRef.md) | 0..* <br/> [DocumentRef](DocumentRef.md) | Links to a leaf element with the location of the document. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [supplementalDoc](supplementalDoc.md) | range | [SupplementalDoc](SupplementalDoc.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/SupplementalDoc](https://wiki.cdisc.org/display/PUB/SupplementalDoc)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SupplementalDoc |
| native | odm:SupplementalDoc |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SupplementalDoc
description: Supplemental data definitions
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SupplementalDoc
rank: 1000
slots:
- documentRef
slot_usage:
  documentRef:
    name: documentRef
    description: Links to a leaf element with the location of the document.
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
class_uri: odm:SupplementalDoc

```
</details>

### Induced

<details>
```yaml
name: SupplementalDoc
description: Supplemental data definitions
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SupplementalDoc
rank: 1000
slot_usage:
  documentRef:
    name: documentRef
    description: Links to a leaf element with the location of the document.
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
    description: Links to a leaf element with the location of the document.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: documentRef
    owner: SupplementalDoc
    domain_of:
    - AnnotatedCRF
    - SupplementalDoc
    - Origin
    - MethodDef
    - CommentDef
    range: DocumentRef
    inlined: true
    inlined_as_list: true
class_uri: odm:SupplementalDoc

```
</details>