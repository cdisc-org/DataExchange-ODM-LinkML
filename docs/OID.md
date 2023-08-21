# Slot: OID


_Unique identifier of the version within the XML document._



URI: [odm:OID](http://www.cdisc.org/ns/odm/v2.0/OID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study... |  yes  |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |
[Standard](Standard.md) | The Standard element describes each standard used within the MetaDataVersion ... |  yes  |
[ValueListDef](ValueListDef.md) | The following table specifies the XML structure for valuelist metadata. The V... |  yes  |
[WhereClauseDef](WhereClauseDef.md) | The WhereClauseDef element specifies a condition. |  yes  |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |  yes  |
[CommentDef](CommentDef.md) | The Comment element allows referencing short comments self-contained in the X... |  yes  |
[StudyIndication](StudyIndication.md) | This element describes a study indication (e.g., condition, disease) for the ... |  yes  |
[StudyIntervention](StudyIntervention.md) | This element describes a study intervention (e.g., medication, treatment, the... |  yes  |
[StudyObjective](StudyObjective.md) |  |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |  yes  |
[StudyEstimand](StudyEstimand.md) |  |  yes  |
[Arm](Arm.md) | An Arm element provides the declaration of a study arm. Arms do not have any ... |  yes  |
[Epoch](Epoch.md) | The planned period of subjects' participation in the trial is divided into se... |  yes  |
[StudyParameter](StudyParameter.md) | A StudyParameter defines a study design parameter for which the value or valu... |  yes  |
[StudyTiming](StudyTiming.md) | The StudyTiming element defines a timing constraint within the study, which c... |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |
[RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |  yes  |
[DurationTimingConstraint](DurationTimingConstraint.md) | The DurationTimingConstraint constrains the duration of an activity represent... |  yes  |
[WorkflowDef](WorkflowDef.md) | A WorkflowDef defines an automated workflow for a study. |  yes  |
[Transition](Transition.md) | A Transition defines a link between 2 structural elements in a workflow. When... |  yes  |
[Branching](Branching.md) | This element describes the branching in a workflow from a source (start) stru... |  yes  |
[Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |  yes  |
[ExceptionEvent](ExceptionEvent.md) | An ExceptionEvent describes an event that occurs suddenly in a study and that... |  yes  |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |
[SignatureDef](SignatureDef.md) | Provides Metadata for signatures included in the /ODM/ClinicalData. |  yes  |
[Query](Query.md) | The Query element represents a request for clarification on a data item colle... |  yes  |







## Properties

* Range: [oid](oid.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: OID
description: Unique identifier of the version within the XML document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: true
alias: OID
domain_of:
- Study
- MetaDataVersion
- Standard
- ValueListDef
- WhereClauseDef
- StudyEventGroupDef
- StudyEventDef
- ItemGroupDef
- ItemDef
- CodeList
- MethodDef
- ConditionDef
- CommentDef
- StudyIndication
- StudyIntervention
- StudyObjective
- StudyEndPoint
- StudyTargetPopulation
- StudyEstimand
- Arm
- Epoch
- StudyParameter
- StudyTiming
- TransitionTimingConstraint
- AbsoluteTimingConstraint
- RelativeTimingConstraint
- DurationTimingConstraint
- WorkflowDef
- Transition
- Branching
- Criterion
- ExceptionEvent
- User
- Organization
- Location
- SignatureDef
- Query
range: oid
required: true

```
</details>