# Slot: StudyEventGroupRefRef


_StudyEventGroupRef reference: This element references a StudyEventGroupDef as it occurs within a specific version of a study. The list of StudyEventGroupRefs identifies the types of study group events that are allowed to occur within the study._



URI: [odm:StudyEventGroupRefRef](http://www.cdisc.org/ns/odm/v2.0/StudyEventGroupRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |  yes  |







## Properties

* Range: [StudyEventGroupRef](StudyEventGroupRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyEventGroupRefRef
description: 'StudyEventGroupRef reference: This element references a StudyEventGroupDef
  as it occurs within a specific version of a study. The list of StudyEventGroupRefs
  identifies the types of study group events that are allowed to occur within the
  study.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: StudyEventGroupRefRef
domain_of:
- StudyEventGroupDef
- Protocol
range: StudyEventGroupRef

```
</details>