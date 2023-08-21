# Slot: Name


_General observation Sub Class._



URI: [odm:Name](http://www.cdisc.org/ns/odm/v2.0/Name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Alias](Alias.md) | An Alias provides an additional name for an element. The Context attribute sp... |  yes  |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |
[Standard](Standard.md) | The Standard element describes each standard used within the MetaDataVersion ... |  yes  |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[Class](Class.md) |  |  yes  |
[SubClass](SubClass.md) | This element contains SubClass definitions. |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |
[Resource](Resource.md) | Describes an external resource used as the source for the parent ItemGroup or... |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[Parameter](Parameter.md) | The Parameter element represents a method parameter used as part of a MethodS... |  yes  |
[ReturnValue](ReturnValue.md) | The ReturnValue element represents a return value used as part of a MethodSig... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |  yes  |
[StudyObjective](StudyObjective.md) |  |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |  yes  |
[StudyEstimand](StudyEstimand.md) |  |  yes  |
[Arm](Arm.md) | An Arm element provides the declaration of a study arm. Arms do not have any ... |  yes  |
[Epoch](Epoch.md) | The planned period of subjects' participation in the trial is divided into se... |  yes  |
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
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |
[Query](Query.md) | The Query element represents a request for clarification on a data item colle... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Name
description: General observation Sub Class.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Name
domain_of:
- Alias
- MetaDataVersion
- Standard
- StudyEventGroupDef
- StudyEventDef
- ItemGroupDef
- Class
- SubClass
- SourceItem
- Resource
- ItemDef
- CodeList
- MethodDef
- Parameter
- ReturnValue
- ConditionDef
- StudyObjective
- StudyEndPoint
- StudyTargetPopulation
- StudyEstimand
- Arm
- Epoch
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
- Organization
- Location
- Query
range: string
any_of:
- range: text
- range: name
- range: StandardName
- range: ItemGroupClass
- range: ItemGroupSubClass

```
</details>