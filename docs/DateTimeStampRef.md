# Slot: DateTimeStampRef

URI: [odm:DateTimeStampRef](http://www.cdisc.org/ns/odm/v2.0/DateTimeStampRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data |  yes  |







## Properties

* Range: [DateTimeStamp](DateTimeStamp.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: DateTimeStampRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: DateTimeStampRef
domain_of:
- AuditRecord
- Signature
range: DateTimeStamp

```
</details>