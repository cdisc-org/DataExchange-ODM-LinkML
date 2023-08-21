# Slot: StudyEventRefRef


_StudyEventRef reference: This element references a StudyEventDef as it occurs within a specific version of a study. The list of StudyEventRefs identifies the types of study events that are allowed to occur within the study._



URI: [odm:StudyEventRefRef](http://www.cdisc.org/ns/odm/v2.0/StudyEventRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[ExceptionEvent](ExceptionEvent.md) | An ExceptionEvent describes an event that occurs suddenly in a study and that... |  yes  |







## Properties

* Range: [StudyEventRef](StudyEventRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyEventRefRef
description: 'StudyEventRef reference: This element references a StudyEventDef as
  it occurs within a specific version of a study. The list of StudyEventRefs identifies
  the types of study events that are allowed to occur within the study.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: StudyEventRefRef
domain_of:
- StudyEventGroupDef
- ExceptionEvent
range: StudyEventRef

```
</details>