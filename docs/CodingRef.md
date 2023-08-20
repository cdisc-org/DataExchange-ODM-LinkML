# Slot: CodingRef

URI: [odm:CodingRef](http://www.cdisc.org/ns/odm/v2.0/CodingRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |  yes  |
[SourceItems](SourceItems.md) | Identifies source items as needed to support automated data capture and end-t... |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist |  yes  |
[StudyIndication](StudyIndication.md) | This element describes a study indication (e |  yes  |
[StudyIntervention](StudyIntervention.md) | This element describes a study intervention (e |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |  yes  |
[StudyParameter](StudyParameter.md) | A StudyParameter defines a study design parameter for which the value or valu... |  yes  |
[ParameterValue](ParameterValue.md) | This element contains the value of the study parameter as text content |  yes  |
[Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |  yes  |
[Annotation](Annotation.md) | A general note about clinical data |  yes  |







## Properties

* Range: [Coding](Coding.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: CodingRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: CodingRef
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