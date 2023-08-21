# Slot: TransitionOID


_References the workflow Transition on which the timing constraint must be executed._



URI: [odm:TransitionOID](http://www.cdisc.org/ns/odm/v2.0/TransitionOID)



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
name: TransitionOID
description: References the workflow Transition on which the timing constraint must
  be executed.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: TransitionOID
domain_of:
- TransitionTimingConstraint
range: oidref

```
</details>