# Slot: studyEventData


_StudyEventData reference: Clinical data for a study event (visit). The model supports repeating study events (e.g., when the same set of information is collected for a series of patient visits)._



URI: [odm:studyEventData](http://www.cdisc.org/ns/odm/v2.0/studyEventData)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SubjectData](SubjectData.md) | Clinical data for a single subject. |  yes  |







## Properties

* Range: [StudyEventData](StudyEventData.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: studyEventData
description: 'StudyEventData reference: Clinical data for a study event (visit). The
  model supports repeating study events (e.g., when the same set of information is
  collected for a series of patient visits).'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: studyEventData
domain_of:
- SubjectData
range: StudyEventData

```
</details>