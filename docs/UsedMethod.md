# Slot: UsedMethod


_Indicates that the action was made by the system rather than a data entry form user action._



URI: [odm:UsedMethod](http://www.cdisc.org/ns/odm/v2.0/UsedMethod)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |







## Properties

* Range: [YesOrNo](YesOrNo.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: UsedMethod
description: Indicates that the action was made by the system rather than a data entry
  form user action.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: UsedMethod
domain_of:
- AuditRecord
range: YesOrNo

```
</details>