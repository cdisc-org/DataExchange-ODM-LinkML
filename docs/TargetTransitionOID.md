# Slot: TargetTransitionOID


_Reference to the Transition that is one of the targets of the branching._



URI: [odm:TargetTransitionOID](http://www.cdisc.org/ns/odm/v2.0/TargetTransitionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TargetTransition](TargetTransition.md) | Provides a reference to a Transition element |  yes  |
[DefaultTransition](DefaultTransition.md) | Element NameDefaultTransitionParent ElementsBranchingElement XPath(s)/ODM/Stu... |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





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