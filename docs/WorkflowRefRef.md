# Slot: WorkflowRefRef


_WorkflowRef reference: The WorkflowRef references a workflow definition_



URI: [odm:WorkflowRefRef](http://www.cdisc.org/ns/odm/v2.0/WorkflowRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |  yes  |
[StudyStructure](StudyStructure.md) | The StudyStructure element describes the general structure of a clinical stud... |  yes  |
[Arm](Arm.md) | An Arm element provides the declaration of a study arm. Arms do not have any ... |  yes  |
[ExceptionEvent](ExceptionEvent.md) | An ExceptionEvent describes an event that occurs suddenly in a study and that... |  yes  |







## Properties

* Range: [WorkflowRef](WorkflowRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: WorkflowRefRef
description: 'WorkflowRef reference: The WorkflowRef references a workflow definition'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: WorkflowRefRef
domain_of:
- StudyEventGroupDef
- StudyEventDef
- ItemGroupDef
- Protocol
- StudyStructure
- Arm
- ExceptionEvent
range: WorkflowRef

```
</details>