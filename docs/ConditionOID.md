# Slot: ConditionOID


_Reference to a ConditionDef defining the condition under which the transition must be executed. The ConditionOID references a ConditionDef element defining a condition that needs to be evaluated at the time of entering the branching state. When the condition evaluates to true, the branch is entered._



URI: [odm:ConditionOID](http://www.cdisc.org/ns/odm/v2.0/ConditionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TargetTransition](TargetTransition.md) | TargetTransition provides a reference to a Transition element that is the tar... |  yes  |
[Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ConditionOID
description: Reference to a ConditionDef defining the condition under which the transition
  must be executed. The ConditionOID references a ConditionDef element defining a
  condition that needs to be evaluated at the time of entering the branching state.
  When the condition evaluates to true, the branch is entered.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ConditionOID
domain_of:
- TargetTransition
- Criterion
range: oidref

```
</details>