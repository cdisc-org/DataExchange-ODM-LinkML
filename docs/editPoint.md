# Slot: editPoint


_Identifies the phase of data processing in which update action occurred._



URI: [odm:editPoint](http://www.cdisc.org/ns/odm/v2.0/editPoint)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |







## Properties

* Range: [EditPointType](EditPointType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: editPoint
description: Identifies the phase of data processing in which update action occurred.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: editPoint
domain_of:
- AuditRecord
range: EditPointType

```
</details>