# Slot: ConditionOID


_Reference to a ConditionDef defining the condition under which the transition must be executed_



URI: [odm:ConditionOID](http://www.cdisc.org/ns/odm/v2.0/ConditionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TargetTransition](TargetTransition.md) | Provides a reference to a Transition element |  yes  |
[Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |  yes  |
[ExceptionEvent](ExceptionEvent.md) | An ExceptionEvent describes an event that occurs suddenly in a study and that... |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ConditionOID
description: Reference to a ConditionDef defining the condition under which the transition
  must be executed
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