# Slot: durationTarget


_Constrains the duration of an activity represented by a Study, Epoch, StudyEventGroupDef, StudyEventDef, ItemGroupDef or ItemDef. Specifies the planned duration of the referenced structural element._



URI: [odm:durationTarget](http://www.cdisc.org/ns/odm/v2.0/durationTarget)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DurationTimingConstraint](DurationTimingConstraint.md) | The DurationTimingConstraint constrains the duration of an activity represent... |  yes  |







## Properties

* Range: [durationDatetime](durationDatetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: durationTarget
description: Constrains the duration of an activity represented by a Study, Epoch,
  StudyEventGroupDef, StudyEventDef, ItemGroupDef or ItemDef. Specifies the planned
  duration of the referenced structural element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: durationTarget
domain_of:
- DurationTimingConstraint
range: durationDatetime

```
</details>