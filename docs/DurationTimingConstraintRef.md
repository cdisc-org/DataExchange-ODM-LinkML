# Slot: DurationTimingConstraintRef


_DurationTimingConstraint reference: The DurationTimingConstraint constrains the duration of an activity represented by a study, epoch, StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef. It is used to constrain the duration of the visit, activity, or any other structural element._



URI: [odm:DurationTimingConstraintRef](http://www.cdisc.org/ns/odm/v2.0/DurationTimingConstraintRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyTiming](StudyTiming.md) | The StudyTiming element defines a timing constraint within the study, which c... |  yes  |







## Properties

* Range: [DurationTimingConstraint](DurationTimingConstraint.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: DurationTimingConstraintRef
description: 'DurationTimingConstraint reference: The DurationTimingConstraint constrains
  the duration of an activity represented by a study, epoch, StudyEventGroupDef, StudyEventDef,
  ItemGroupDef, or ItemDef. It is used to constrain the duration of the visit, activity,
  or any other structural element.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: DurationTimingConstraintRef
domain_of:
- StudyTiming
range: DurationTimingConstraint

```
</details>