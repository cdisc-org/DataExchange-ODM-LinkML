# Slot: QueryRef

URI: [odm:QueryRef](http://www.cdisc.org/ns/odm/v2.0/QueryRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects |  yes  |
[SubjectData](SubjectData.md) | Clinical data for a single subject |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit) |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |







## Properties

* Range: [Query](Query.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: QueryRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: QueryRef
domain_of:
- Location
- ClinicalData
- SubjectData
- StudyEventData
- ItemGroupData
- ItemData
range: Query

```
</details>