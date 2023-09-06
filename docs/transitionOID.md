# Slot: transitionOID


_References the workflow Transition on which the timing constraint must be executed._



URI: [odm:transitionOID](http://www.cdisc.org/ns/odm/v2.0/transitionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: transitionOID
description: References the workflow Transition on which the timing constraint must
  be executed.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: transitionOID
domain_of:
- TransitionTimingConstraint
range: oidref

```
</details>