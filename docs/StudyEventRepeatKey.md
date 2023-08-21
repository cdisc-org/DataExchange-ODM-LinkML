# Slot: StudyEventRepeatKey


_A key used to distinguish between repeats of the same type of study event for a single subject._



URI: [odm:StudyEventRepeatKey](http://www.cdisc.org/ns/odm/v2.0/StudyEventRepeatKey)



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
name: StudyEventRepeatKey
description: A key used to distinguish between repeats of the same type of study event
  for a single subject.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: StudyEventRepeatKey
domain_of:
- StudyEventData
- KeySet
range: repeatKey

```
</details>