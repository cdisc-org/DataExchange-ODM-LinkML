# Slot: GranularityRef


_Granularity is intended to give the sender a shorthand way to Describes the scope of information in the document, for certain common types of documents. All means the entire study; Metadata means the Study/MetaDataVersion element; AdminData and ReferenceData mean the corresponding elements; AllClinicalData means all of the ClinicalData collected for the study. SingleSite, means all of the Clinical Data for a single study site. SingleSubject means all of the Clinical Data for a single Subject._



URI: [odm:GranularityRef](http://www.cdisc.org/ns/odm/v2.0/GranularityRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents. The ODM element is the top-level (root) eleme... |  yes  |







## Properties

* Range: [Granularity](Granularity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: GranularityRef
description: Granularity is intended to give the sender a shorthand way to Describes
  the scope of information in the document, for certain common types of documents.
  All means the entire study; Metadata means the Study/MetaDataVersion element; AdminData
  and ReferenceData mean the corresponding elements; AllClinicalData means all of
  the ClinicalData collected for the study. SingleSite, means all of the Clinical
  Data for a single study site. SingleSubject means all of the Clinical Data for a
  single Subject.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: GranularityRef
domain_of:
- ODMFileMetadata
range: Granularity

```
</details>