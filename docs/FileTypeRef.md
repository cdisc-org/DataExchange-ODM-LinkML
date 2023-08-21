# Slot: FileTypeRef


_Snapshot means that the document contains only the current state of the data and metadata it describes, and no transactional history. Transactional means that the document may contain more than one instance per data point. Query means the document contains only ClinicalData/Query elements._



URI: [odm:FileTypeRef](http://www.cdisc.org/ns/odm/v2.0/FileTypeRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents. The ODM element is the top-level (root) eleme... |  yes  |







## Properties

* Range: [FileType](FileType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: FileTypeRef
description: Snapshot means that the document contains only the current state of the
  data and metadata it describes, and no transactional history. Transactional means
  that the document may contain more than one instance per data point. Query means
  the document contains only ClinicalData/Query elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: FileTypeRef
domain_of:
- ODMFileMetadata
range: FileType

```
</details>