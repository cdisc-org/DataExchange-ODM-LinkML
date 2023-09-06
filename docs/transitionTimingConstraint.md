# Slot: transitionTimingConstraint


_TransitionTimingConstraint reference: The TransitionTimingConstraint element defines a timing constraint on a transition between structural elements as defined in a workflow. As such, it is a non-blocking constraint. This means that the transition is set on hold as long as the timing condition is not fulfilled, and is executed as soon as the timing condition is fulfilled._



URI: [odm:transitionTimingConstraint](http://www.cdisc.org/ns/odm/v2.0/transitionTimingConstraint)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyTiming](StudyTiming.md) | The StudyTiming element defines a timing constraint within the study, which c... |  yes  |







## Properties

* Range: [TransitionTimingConstraint](TransitionTimingConstraint.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: transitionTimingConstraint
description: 'TransitionTimingConstraint reference: The TransitionTimingConstraint
  element defines a timing constraint on a transition between structural elements
  as defined in a workflow. As such, it is a non-blocking constraint. This means that
  the transition is set on hold as long as the timing condition is not fulfilled,
  and is executed as soon as the timing condition is fulfilled.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: transitionTimingConstraint
domain_of:
- StudyTiming
range: TransitionTimingConstraint

```
</details>