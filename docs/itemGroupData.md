# Slot: itemGroupData


_ItemGroupData reference: Clinical data corresponding to an ItemGroupRef defined in the active MetaDataVersion._



URI: [odm:itemGroupData](http://www.cdisc.org/ns/odm/v2.0/itemGroupData)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data. For ex... |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects. |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit). The model supports repeating study e... |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |







## Properties

* Range: [ItemGroupData](ItemGroupData.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: itemGroupData
description: 'ItemGroupData reference: Clinical data corresponding to an ItemGroupRef
  defined in the active MetaDataVersion.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: itemGroupData
domain_of:
- ReferenceData
- ClinicalData
- StudyEventData
- ItemGroupData
range: ItemGroupData

```
</details>