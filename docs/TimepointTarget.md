# Slot: TimepointTarget


_The planned time between the 2 activities defined by the transition in the workflow._



URI: [odm:TimepointTarget](http://www.cdisc.org/ns/odm/v2.0/TimepointTarget)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TimepointTarget
description: The planned time between the 2 activities defined by the transition in
  the workflow.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: TimepointTarget
domain_of:
- TransitionTimingConstraint
- AbsoluteTimingConstraint
range: string
any_of:
- range: durationDatetime

```
</details>