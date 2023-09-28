# Slot: startConditionOID


_The StartConditionOID references a ConditionDef specifying a condition that must be met for the transition to start. For example, if the source structural element is a StudyEventGroupDef describing the activities for study screening and the target structural element is a StudyEventGroupDef describing study enrollment, the ConditionDef referenced by the StartConditionOID specifies the criteria that must be met for a subject to transition from screening to enrollment._



URI: [odm:startConditionOID](http://www.cdisc.org/ns/odm/v2.0/startConditionOID)



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
name: startConditionOID
description: The StartConditionOID references a ConditionDef specifying a condition
  that must be met for the transition to start. For example, if the source structural
  element is a StudyEventGroupDef describing the activities for study screening and
  the target structural element is a StudyEventGroupDef describing study enrollment,
  the ConditionDef referenced by the StartConditionOID specifies the criteria that
  must be met for a subject to transition from screening to enrollment.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: startConditionOID
domain_of:
- Transition
range: oidref

```
</details>