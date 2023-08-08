# Slot: ConditionOID

URI: [odm:ConditionOID](http://www.cdisc.org/ns/odm/v2.0/ConditionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TargetTransition](TargetTransition.md) |  |  yes  |
[Criterion](Criterion.md) |  |  yes  |
[ExceptionEvent](ExceptionEvent.md) |  |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ConditionOID
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ConditionOID
domain_of:
- TargetTransition
- Criterion
- ExceptionEvent
range: oidref

```
</details>