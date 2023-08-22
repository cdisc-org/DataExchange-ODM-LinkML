# Slot: StudyTargetPopulationRefRef


_StudyTargetPopulationRef reference: The StudyTargetPopulationRef references a StudyTargetPopulation to which the estimand applies._



URI: [odm:StudyTargetPopulationRefRef](http://www.cdisc.org/ns/odm/v2.0/StudyTargetPopulationRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |  yes  |
[StudyEstimand](StudyEstimand.md) | A precise description of the treatment effect reflecting the clinical questio... |  yes  |







## Properties

* Range: [StudyTargetPopulationRef](StudyTargetPopulationRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyTargetPopulationRefRef
description: 'StudyTargetPopulationRef reference: The StudyTargetPopulationRef references
  a StudyTargetPopulation to which the estimand applies.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: StudyTargetPopulationRefRef
domain_of:
- Protocol
- StudyEstimand
range: StudyTargetPopulationRef

```
</details>