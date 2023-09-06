# Slot: description


_Description reference: A free-text description of the containing metadata component, unless restricted by Business Rules._



URI: [odm:description](http://www.cdisc.org/ns/odm/v2.0/description)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study... |  yes  |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |
[ValueListDef](ValueListDef.md) | The following table specifies the XML structure for valuelist metadata. The V... |  yes  |
[StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific v... |  yes  |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |  yes  |
[CommentDef](CommentDef.md) | The Comment element allows referencing short comments self-contained in the X... |  yes  |
[Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |  yes  |
[StudyStructure](StudyStructure.md) | The StudyStructure element describes the general structure of a clinical stud... |  yes  |
[TrialPhase](TrialPhase.md) | The TrialPhase element designates the phase of the study in the clinical tria... |  yes  |
[StudyIndication](StudyIndication.md) | This element describes a study indication (e.g., condition, disease) for the ... |  yes  |
[StudyIntervention](StudyIntervention.md) | This element describes a study intervention (e.g., medication, treatment, the... |  yes  |
[StudyObjective](StudyObjective.md) | The reason for performing a study in terms of the scientific questions to be ... |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |  yes  |
[StudyEstimand](StudyEstimand.md) | A precise description of the treatment effect reflecting the clinical questio... |  yes  |
[IntercurrentEvent](IntercurrentEvent.md) | The IntercurrentEvent element describes an intercurrent event for an estimand... |  yes  |
[SummaryMeasure](SummaryMeasure.md) | The SummaryMeasure element describes a summary measure for an estimand (e.g.,... |  yes  |
[Arm](Arm.md) | An Arm element provides the declaration of a study arm. Arms do not have any ... |  yes  |
[Epoch](Epoch.md) | The planned period of subjects' participation in the trial is divided into se... |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |
[RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |  yes  |
[DurationTimingConstraint](DurationTimingConstraint.md) | The DurationTimingConstraint constrains the duration of an activity represent... |  yes  |
[WorkflowDef](WorkflowDef.md) | A WorkflowDef defines an automated workflow for a study. |  yes  |
[Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |
[ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents. The ODM element is the top-level (root) eleme... |  yes  |







## Properties

* Range: [Description](Description.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: description
description: 'Description reference: A free-text description of the containing metadata
  component, unless restricted by Business Rules.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: description
domain_of:
- Study
- MetaDataVersion
- ValueListDef
- StudyEventGroupRef
- StudyEventGroupDef
- StudyEventDef
- ItemGroupDef
- Origin
- ItemDef
- CodeList
- CodeListItem
- MethodDef
- ConditionDef
- CommentDef
- Protocol
- StudyStructure
- TrialPhase
- StudyIndication
- StudyIntervention
- StudyObjective
- StudyEndPoint
- StudyTargetPopulation
- StudyEstimand
- IntercurrentEvent
- SummaryMeasure
- Arm
- Epoch
- TransitionTimingConstraint
- AbsoluteTimingConstraint
- RelativeTimingConstraint
- DurationTimingConstraint
- WorkflowDef
- Criterion
- Organization
- Location
- ODMFileMetadata
range: Description

```
</details>