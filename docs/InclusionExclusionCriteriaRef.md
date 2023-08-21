# Slot: InclusionExclusionCriteriaRef


_InclusionExclusionCriteria reference: The InclusionExclusionCriteria element can contain 2 lists of Criterion elements, represented by the 2 elements InclusionCriteria and ExclusionCriteria. Together, these criteria determine the eligibility of a subject for the study. The actual condition to be evaluated is contained in an ODM ConditionDef, which is referenced by each Criterion‟s ConditionOID attribute._



URI: [odm:InclusionExclusionCriteriaRef](http://www.cdisc.org/ns/odm/v2.0/InclusionExclusionCriteriaRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |  yes  |







## Properties

* Range: [InclusionExclusionCriteria](InclusionExclusionCriteria.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: InclusionExclusionCriteriaRef
description: 'InclusionExclusionCriteria reference: The InclusionExclusionCriteria
  element can contain 2 lists of Criterion elements, represented by the 2 elements
  InclusionCriteria and ExclusionCriteria. Together, these criteria determine the
  eligibility of a subject for the study. The actual condition to be evaluated is
  contained in an ODM ConditionDef, which is referenced by each Criterion‟s ConditionOID
  attribute.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: InclusionExclusionCriteriaRef
domain_of:
- Protocol
range: InclusionExclusionCriteria

```
</details>