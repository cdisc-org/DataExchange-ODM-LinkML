# Slot: coding


_Coding reference: Coding references a symbol from a defined code system. It uses a code defined in a terminology system to associate semantics with a given term, codelist, variable, or group of variables. The presence of a Coding element associates a meaning to its parent element. Including multiple Coding elements for a given parent indicates synonymous meanings provided by different code systems or code system versions._



URI: [odm:coding](http://www.cdisc.org/ns/odm/v2.0/coding)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |  yes  |
[SourceItems](SourceItems.md) | Identifies source items as needed to support automated data capture and end-t... |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |  yes  |
[StudyIndication](StudyIndication.md) | This element describes a study indication (e.g., condition, disease) for the ... |  yes  |
[StudyIntervention](StudyIntervention.md) | This element describes a study intervention (e.g., medication, treatment, the... |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |  yes  |
[StudyParameter](StudyParameter.md) | A StudyParameter defines a study design parameter for which the value or valu... |  yes  |
[ParameterValue](ParameterValue.md) | This element contains the value of the study parameter as text content. |  yes  |
[Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |  yes  |
[Annotation](Annotation.md) | A general note about clinical data. If an annotation has both a comment and f... |  yes  |







## Properties

* Range: [Coding](Coding.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: coding
description: 'Coding reference: Coding references a symbol from a defined code system.
  It uses a code defined in a terminology system to associate semantics with a given
  term, codelist, variable, or group of variables. The presence of a Coding element
  associates a meaning to its parent element. Including multiple Coding elements for
  a given parent indicates synonymous meanings provided by different code systems
  or code system versions.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: coding
domain_of:
- StudyEventGroupDef
- StudyEventDef
- ItemGroupDef
- Origin
- SourceItems
- SourceItem
- ItemDef
- CodeList
- CodeListItem
- StudyIndication
- StudyIntervention
- StudyTargetPopulation
- StudyParameter
- ParameterValue
- Criterion
- Annotation
range: Coding

```
</details>