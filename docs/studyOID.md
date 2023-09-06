# Slot: studyOID


_References the Study that provides a prior metadata version. This attribute allows an Include element to reference a metadata version in another study. Thus, it is possible for many studies to share a set of common metadata definitions_



URI: [odm:studyOID](http://www.cdisc.org/ns/odm/v2.0/studyOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Include](Include.md) | The Include metadata element allows a reference to a prior metadata version. |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |
[AdminData](AdminData.md) | Administrative information about users, locations, organizations, and electro... |  yes  |
[MetaDataVersionRef](MetaDataVersionRef.md) | A reference to a MetaDataVersion used at the containing Location. The Effecti... |  yes  |
[ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data. For ex... |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects. |  yes  |
[Association](Association.md) | An association permits an annotation to be placed on an ordered pair of entit... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: studyOID
description: References the Study that provides a prior metadata version. This attribute
  allows an Include element to reference a metadata version in another study. Thus,
  it is possible for many studies to share a set of common metadata definitions
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: studyOID
domain_of:
- Include
- SourceItem
- AdminData
- MetaDataVersionRef
- ReferenceData
- ClinicalData
- Association
- KeySet
range: oidref

```
</details>