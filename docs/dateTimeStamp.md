# Slot: dateTimeStamp


_DateTimeStamp reference: Date and time when an action was performed._



URI: [odm:dateTimeStamp](http://www.cdisc.org/ns/odm/v2.0/dateTimeStamp)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data. This indica... |  yes  |







## Properties

* Range: [DateTimeStamp](DateTimeStamp.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: dateTimeStamp
description: 'DateTimeStamp reference: Date and time when an action was performed.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: dateTimeStamp
domain_of:
- AuditRecord
- Signature
range: DateTimeStamp

```
</details>