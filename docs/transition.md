# Slot: transition


_Transition reference: A Transition defines a link between 2 structural elements in a workflow. When the execution of the transition is dependent upon a timing constraint that is either directly defined or calculated, a TransitionTimingConstraint must be defined, referencing the current Transition._



URI: [odm:transition](http://www.cdisc.org/ns/odm/v2.0/transition)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WorkflowDef](WorkflowDef.md) | A WorkflowDef defines an automated workflow for a study. |  yes  |







## Properties

* Range: [Transition](Transition.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: transition
description: 'Transition reference: A Transition defines a link between 2 structural
  elements in a workflow. When the execution of the transition is dependent upon a
  timing constraint that is either directly defined or calculated, a TransitionTimingConstraint
  must be defined, referencing the current Transition.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: transition
domain_of:
- WorkflowDef
range: Transition

```
</details>