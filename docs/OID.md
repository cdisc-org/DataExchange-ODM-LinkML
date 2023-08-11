# Slot: OID


_Unique identifier of the version within the XML document._



URI: [odm:OID](http://www.cdisc.org/ns/odm/v2.0/OID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) |  |  yes  |
[MetaDataVersion](MetaDataVersion.md) |  |  yes  |
[Standard](Standard.md) |  |  yes  |
[ValueListDef](ValueListDef.md) |  |  yes  |
[WhereClauseDef](WhereClauseDef.md) |  |  yes  |
[StudyEventGroupDef](StudyEventGroupDef.md) |  |  yes  |
[StudyEventDef](StudyEventDef.md) |  |  yes  |
[ItemGroupDef](ItemGroupDef.md) |  |  yes  |
[ItemDef](ItemDef.md) |  |  yes  |
[CodeList](CodeList.md) |  |  yes  |
[MethodDef](MethodDef.md) |  |  yes  |
[ConditionDef](ConditionDef.md) |  |  yes  |
[CommentDef](CommentDef.md) | The Comment element allows referencing short comments self-contained in the X... |  yes  |
[StudyIndication](StudyIndication.md) |  |  yes  |
[StudyIntervention](StudyIntervention.md) |  |  yes  |
[StudyObjective](StudyObjective.md) |  |  yes  |
[StudyEndPoint](StudyEndPoint.md) |  |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) |  |  yes  |
[StudyEstimand](StudyEstimand.md) |  |  yes  |
[Arm](Arm.md) |  |  yes  |
[Epoch](Epoch.md) |  |  yes  |
[StudyParameter](StudyParameter.md) |  |  yes  |
[StudyTiming](StudyTiming.md) |  |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) |  |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) |  |  yes  |
[RelativeTimingConstraint](RelativeTimingConstraint.md) |  |  yes  |
[DurationTimingConstraint](DurationTimingConstraint.md) |  |  yes  |
[WorkflowDef](WorkflowDef.md) |  |  yes  |
[Transition](Transition.md) |  |  yes  |
[Branching](Branching.md) |  |  yes  |
[Criterion](Criterion.md) |  |  yes  |
[ExceptionEvent](ExceptionEvent.md) |  |  yes  |
[User](User.md) |  |  yes  |
[Organization](Organization.md) |  |  yes  |
[Location](Location.md) |  |  yes  |
[SignatureDef](SignatureDef.md) |  |  yes  |
[Query](Query.md) |  |  yes  |







## Properties

* Range: [Oid](Oid.md)

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