# Slot: endConditionOID


_The EndConditionOID references a ConditionDef defining the condition under which the transition can be completed. As long as the condition is not met, the transition to the next actitivity or event must be considered to be temporary blocked. When the target structural element can be considered to be a "visit," the condition can be regarded as a visit entry criterion._



URI: [odm:endConditionOID](http://www.cdisc.org/ns/odm/v2.0/endConditionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Transition](Transition.md) | A Transition defines a link between 2 structural elements in a workflow. When... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: endConditionOID
description: The EndConditionOID references a ConditionDef defining the condition
  under which the transition can be completed. As long as the condition is not met,
  the transition to the next actitivity or event must be considered to be temporary
  blocked. When the target structural element can be considered to be a "visit," the
  condition can be regarded as a visit entry criterion.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: endConditionOID
domain_of:
- Transition
range: oidref

```
</details>