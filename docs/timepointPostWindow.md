# Slot: timepointPostWindow


_Specifies the amount of time after the TimepointTarget, the time between the two activities, may be lengthened._



URI: [odm:timepointPostWindow](http://www.cdisc.org/ns/odm/v2.0/timepointPostWindow)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |
[RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |  yes  |







## Properties

* Range: [durationDatetime](durationDatetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: timepointPostWindow
description: Specifies the amount of time after the TimepointTarget, the time between
  the two activities, may be lengthened.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: timepointPostWindow
domain_of:
- TransitionTimingConstraint
- AbsoluteTimingConstraint
- RelativeTimingConstraint
range: durationDatetime

```
</details>