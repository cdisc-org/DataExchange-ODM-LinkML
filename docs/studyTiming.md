# Slot: studyTiming


_StudyTiming reference: The StudyTiming element defines a timing constraint within the study, which can be an absolute timing constraint (e.g., start of the screening visit must be between 1 January 2022 and 31 December 2022), a relative timing constraint (e.g., visit 2 must be within 30 days after visit 1 with a window of +/- 1 week), a transition timing constraint (i.e., timing constraint on a transition within a defined workflow), or a duration timing constraint (e.g., the duration of visit 2 is planned to take hours with a window of 30 minutes)._



URI: [odm:studyTiming](http://www.cdisc.org/ns/odm/v2.0/studyTiming)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyTimings](StudyTimings.md) | The StudyTimings element is a container element for individual StudyTiming el... |  yes  |







## Properties

* Range: [StudyTiming](StudyTiming.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: studyTiming
description: 'StudyTiming reference: The StudyTiming element defines a timing constraint
  within the study, which can be an absolute timing constraint (e.g., start of the
  screening visit must be between 1 January 2022 and 31 December 2022), a relative
  timing constraint (e.g., visit 2 must be within 30 days after visit 1 with a window
  of +/- 1 week), a transition timing constraint (i.e., timing constraint on a transition
  within a defined workflow), or a duration timing constraint (e.g., the duration
  of visit 2 is planned to take hours with a window of 30 minutes).'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: studyTiming
domain_of:
- StudyTimings
range: StudyTiming

```
</details>