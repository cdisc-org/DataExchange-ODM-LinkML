# Slot: AuditRecordRef

URI: [odm:AuditRecordRef](http://www.cdisc.org/ns/odm/v2.0/AuditRecordRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferenceData](ReferenceData.md) |  |  yes  |
[ClinicalData](ClinicalData.md) |  |  yes  |
[SubjectData](SubjectData.md) |  |  yes  |
[StudyEventData](StudyEventData.md) |  |  yes  |
[ItemGroupData](ItemGroupData.md) |  |  yes  |
[ItemData](ItemData.md) |  |  yes  |
[Query](Query.md) |  |  yes  |







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