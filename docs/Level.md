# Slot: Level


_Defined level for the Study Objective_



URI: [odm:Level](http://www.cdisc.org/ns/odm/v2.0/Level)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyObjective](StudyObjective.md) | Element NameStudyObjectiveParent ElementStudyObjectivesElement XPath(s)/ODM/S... |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[StudyEstimand](StudyEstimand.md) | Element NameStudyEstimandParent ElementsStudyEstimandsElement XPath(s)/ODM/St... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Level
description: Defined level for the Study Objective
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Level
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