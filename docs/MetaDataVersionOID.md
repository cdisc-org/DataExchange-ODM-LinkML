# Slot: MetaDataVersionOID


_References a prior MetaDataVersion within the Study referenced by the StudyOID attribute._



URI: [odm:MetaDataVersionOID](http://www.cdisc.org/ns/odm/v2.0/MetaDataVersionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Include](Include.md) | The Include metadata element allows a reference to a prior metadata version. |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |
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
name: MetaDataVersionOID
description: References a prior MetaDataVersion within the Study referenced by the
  StudyOID attribute.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: MetaDataVersionOID
domain_of:
- Include
- SourceItem
- MetaDataVersionRef
- ReferenceData
- ClinicalData
- Association
- KeySet
range: oidref

```
</details>