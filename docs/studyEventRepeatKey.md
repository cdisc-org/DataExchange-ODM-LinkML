# Slot: studyEventRepeatKey


_A key used to distinguish between repeats of the same type of study event for a single subject._



URI: [odm:studyEventRepeatKey](http://www.cdisc.org/ns/odm/v2.0/studyEventRepeatKey)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit). The model supports repeating study e... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |  yes  |







## Properties

* Range: [repeatKey](repeatKey.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: studyEventRepeatKey
description: A key used to distinguish between repeats of the same type of study event
  for a single subject.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: studyEventRepeatKey
domain_of:
- StudyEventData
- KeySet
range: repeatKey

```
</details>