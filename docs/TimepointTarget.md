# Slot: TimepointTarget

URI: [odm:TimepointTarget](http://www.cdisc.org/ns/odm/v2.0/TimepointTarget)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TransitionTimingConstraint](TransitionTimingConstraint.md) |  |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TimepointTarget
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