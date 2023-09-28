# Slot: documentRef


_The DocumentRef element is a container for page references in a PDF file._



URI: [odm:documentRef](http://www.cdisc.org/ns/odm/v2.0/documentRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AnnotatedCRF](AnnotatedCRF.md) | An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document ... |  yes  |
[SupplementalDoc](SupplementalDoc.md) | Supplemental data definitions |  yes  |
[Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[CommentDef](CommentDef.md) | The Comment element allows referencing short comments self-contained in the X... |  yes  |







## Properties

* Range: [DocumentRef](DocumentRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: documentRef
description: The DocumentRef element is a container for page references in a PDF file.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: documentRef
domain_of:
- AnnotatedCRF
- SupplementalDoc
- Origin
- MethodDef
- CommentDef
range: DocumentRef

```
</details>