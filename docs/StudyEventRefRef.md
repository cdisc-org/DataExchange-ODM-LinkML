# Slot: StudyEventRefRef

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