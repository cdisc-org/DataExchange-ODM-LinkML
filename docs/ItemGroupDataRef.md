# Slot: ItemGroupDataRef

URI: [odm:ItemGroupDataRef](http://www.cdisc.org/ns/odm/v2.0/ItemGroupDataRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit) |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |







## Properties

* Range: [ItemGroupData](ItemGroupData.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemGroupDataRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ItemGroupDataRef
domain_of:
- ReferenceData
- ClinicalData
- StudyEventData
- ItemGroupData
range: ItemGroupData

```
</details>