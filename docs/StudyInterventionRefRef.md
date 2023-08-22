# Slot: StudyInterventionRefRef


_StudyInterventionRef reference: The StudyInterventionRef references an intervention that is taken as the treatment for the estimand._



URI: [odm:StudyInterventionRefRef](http://www.cdisc.org/ns/odm/v2.0/StudyInterventionRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyInterventions](StudyInterventions.md) | The StudyInterventions element is a container element for individual StudyInt... |  yes  |
[StudyEstimand](StudyEstimand.md) | A precise description of the treatment effect reflecting the clinical questio... |  yes  |







## Properties

* Range: [StudyInterventionRef](StudyInterventionRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyInterventionRefRef
description: 'StudyInterventionRef reference: The StudyInterventionRef references
  an intervention that is taken as the treatment for the estimand.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: StudyInterventionRefRef
domain_of:
- StudyInterventions
- StudyEstimand
range: StudyInterventionRef

```
</details>