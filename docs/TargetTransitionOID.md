# Slot: TargetTransitionOID


_Reference to the Transition that is one of the targets of the branching._



URI: [odm:TargetTransitionOID](http://www.cdisc.org/ns/odm/v2.0/TargetTransitionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TargetTransition](TargetTransition.md) | TargetTransition provides a reference to a Transition element that is the tar... |  yes  |
[DefaultTransition](DefaultTransition.md) | The DefaultTransition references the Transition that needs to be executed whe... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TargetTransitionOID
description: Reference to the Transition that is one of the targets of the branching.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: TargetTransitionOID
domain_of:
- TargetTransition
- DefaultTransition
range: oidref

```
</details>