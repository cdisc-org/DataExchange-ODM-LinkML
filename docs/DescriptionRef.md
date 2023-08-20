# Slot: DescriptionRef

URI: [odm:DescriptionRef](http://www.cdisc.org/ns/odm/v2.0/DescriptionRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study |  yes  |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements |  yes  |
[ValueListDef](ValueListDef.md) | The following table specifies the XML structure for valuelist metadata |  yes  |
[StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific v... |  yes  |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition |  yes  |
[CommentDef](CommentDef.md) | The Comment element allows referencing short comments self-contained in the X... |  yes  |
[Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |  yes  |
[StudyStructure](StudyStructure.md) | The StudyStructure element describes the general structure of a clinical stud... |  yes  |
[TrialPhase](TrialPhase.md) | The TrialPhase element designates the phase of the study in the clinical tria... |  yes  |
[StudyIndication](StudyIndication.md) | This element describes a study indication (e |  yes  |
[StudyIntervention](StudyIntervention.md) | This element describes a study intervention (e |  yes  |
[StudyObjective](StudyObjective.md) | Element NameStudyObjectiveParent ElementStudyObjectivesElement XPath(s)/ODM/S... |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |  yes  |
[StudyEstimand](StudyEstimand.md) | Element NameStudyEstimandParent ElementsStudyEstimandsElement XPath(s)/ODM/St... |  yes  |
[IntercurrentEvent](IntercurrentEvent.md) | Element NameInterCurrentEventParent ElementsStudyEstimandElement XPath(s)/ODM... |  yes  |
[SummaryMeasure](SummaryMeasure.md) | Element NameSummaryMeasureParent ElementsStudyEstimandElement XPath(s)/ODM/St... |  yes  |
[Arm](Arm.md) | An Arm element provides the declaration of a study arm |  yes  |
[Epoch](Epoch.md) | The planned period of subjects' participation in the trial is divided into se... |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |
[RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |  yes  |
[DurationTimingConstraint](DurationTimingConstraint.md) |  |  yes  |
[WorkflowDef](WorkflowDef.md) | A WorkflowDef defines an automated workflow for a study |  yes  |
[Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |  yes  |
[ExceptionEvent](ExceptionEvent.md) | An ExceptionEvent describes an event that occurs suddenly in a study and that... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |
[ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents |  yes  |







## Properties

* Range: [Description](Description.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: DescriptionRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: DescriptionRef
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
- ExceptionEvent
- Organization
- Location
- ODMFileMetadata
range: Description

```
</details>