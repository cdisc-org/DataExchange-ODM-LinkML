# Slot: AuditRecordRef

URI: [odm:AuditRecordRef](http://www.cdisc.org/ns/odm/v2.0/AuditRecordRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects |  yes  |
[SubjectData](SubjectData.md) | Clinical data for a single subject |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit) |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |
[Query](Query.md) | The Query element represents a request for clarification on a data item colle... |  yes  |







## Properties

* Range: [AuditRecord](AuditRecord.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: AuditRecordRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: AuditRecordRef
domain_of:
- ReferenceData
- ClinicalData
- SubjectData
- StudyEventData
- ItemGroupData
- ItemData
- Query
range: AuditRecord

```
</details>