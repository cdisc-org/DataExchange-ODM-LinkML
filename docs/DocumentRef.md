# Class: DocumentRef


_Links to a leaf element with the location of the document._





URI: [odm:DocumentRef](http://www.cdisc.org/ns/odm/v2.0/DocumentRef)



```mermaid
 classDiagram
    class DocumentRef
      DocumentRef : leafID
        
      DocumentRef : PDFPageRefRef
        
          DocumentRef --|> PDFPageRef : PDFPageRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [leafID](leafID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier for the leaf element with the document location | direct |
| [PDFPageRefRef](PDFPageRefRef.md) | 0..* <br/> [PDFPageRef](PDFPageRef.md) | The PDFPageRef element is a container for page references in a PDF file | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnnotatedCRF](AnnotatedCRF.md) | [DocumentRefRef](DocumentRefRef.md) | range | [DocumentRef](DocumentRef.md) |
| [SupplementalDoc](SupplementalDoc.md) | [DocumentRefRef](DocumentRefRef.md) | range | [DocumentRef](DocumentRef.md) |
| [Origin](Origin.md) | [DocumentRefRef](DocumentRefRef.md) | range | [DocumentRef](DocumentRef.md) |
| [CommentDef](CommentDef.md) | [DocumentRefRef](DocumentRefRef.md) | range | [DocumentRef](DocumentRef.md) |
| [MethodDef](MethodDef.md) | [DocumentRefRef](DocumentRefRef.md) | range | [DocumentRef](DocumentRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:DocumentRef |
| native | odm:DocumentRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DocumentRef
description: Links to a leaf element with the location of the document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- leafID
- PDFPageRefRef
slot_usage:
  leafID:
    name: leafID
    domain_of:
    - SourceItem
    - DocumentRef
    range: oid
    required: true
  PDFPageRefRef:
    name: PDFPageRefRef
    description: The PDFPageRef element is a container for page references in a PDF
      file.
    multivalued: true
    domain_of:
    - DocumentRef
    range: PDFPageRef
    required: false
    minimum_cardinality: 0
class_uri: odm:DocumentRef
unique_keys:
  UC-SUPPD-1:
    unique_key_name: UC-SUPPD-1
    unique_key_slots:
    - leafID

```
</details>

### Induced

<details>
```yaml
name: DocumentRef
description: Links to a leaf element with the location of the document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  leafID:
    name: leafID
    domain_of:
    - SourceItem
    - DocumentRef
    range: oid
    required: true
  PDFPageRefRef:
    name: PDFPageRefRef
    description: The PDFPageRef element is a container for page references in a PDF
      file.
    multivalued: true
    domain_of:
    - DocumentRef
    range: PDFPageRef
    required: false
    minimum_cardinality: 0
attributes:
  leafID:
    name: leafID
    description: Unique identifier for the leaf element with the document location.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: leafID
    owner: DocumentRef
    domain_of:
    - SourceItem
    - DocumentRef
    range: oid
    required: true
  PDFPageRefRef:
    name: PDFPageRefRef
    description: The PDFPageRef element is a container for page references in a PDF
      file.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: PDFPageRefRef
    owner: DocumentRef
    domain_of:
    - DocumentRef
    range: PDFPageRef
    required: false
    minimum_cardinality: 0
class_uri: odm:DocumentRef
unique_keys:
  UC-SUPPD-1:
    unique_key_name: UC-SUPPD-1
    unique_key_slots:
    - leafID

```
</details>