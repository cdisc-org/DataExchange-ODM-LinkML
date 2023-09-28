# Slot: level


_Defined level for the Study Objective_



URI: [odm:level](http://www.cdisc.org/ns/odm/v2.0/level)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyObjective](StudyObjective.md) | The reason for performing a study in terms of the scientific questions to be ... |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[StudyEstimand](StudyEstimand.md) | A precise description of the treatment effect reflecting the clinical questio... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: level
description: Defined level for the Study Objective
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: level
domain_of:
- StudyObjective
- StudyEndPoint
- StudyEstimand
range: string
any_of:
- range: StudyObjectiveLevel
- range: StudyEstimandLevel

```
</details>