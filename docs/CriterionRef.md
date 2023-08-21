# Slot: CriterionRef


_Criterion reference: The Criterion represents either an inclusion or an exclusion criterion, depending on the parent element (i.e., InclusionCriteria, ExclusionCriteria)._



URI: [odm:CriterionRef](http://www.cdisc.org/ns/odm/v2.0/CriterionRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[InclusionCriteria](InclusionCriteria.md) | The InclusionCriteria is a container element for Criterion elements describin... |  yes  |
[ExclusionCriteria](ExclusionCriteria.md) | The ExclusionCriteria is a container element for Criterion elements describin... |  yes  |
[EntryCriteria](EntryCriteria.md) |  |  yes  |
[ExitCriteria](ExitCriteria.md) |  |  yes  |







## Properties

* Range: [Criterion](Criterion.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: CriterionRef
description: 'Criterion reference: The Criterion represents either an inclusion or
  an exclusion criterion, depending on the parent element (i.e., InclusionCriteria,
  ExclusionCriteria).'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: CriterionRef
domain_of:
- InclusionCriteria
- ExclusionCriteria
- EntryCriteria
- ExitCriteria
range: Criterion

```
</details>