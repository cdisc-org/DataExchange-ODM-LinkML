# Class: StudyTiming


_The StudyTiming element defines a timing constraint within the study, which can be an absolute timing constraint (e.g., start of the screening visit must be between 1 January 2022 and 31 December 2022), a relative timing constraint (e.g., visit 2 must be within 30 days after visit 1 with a window of +/- 1 week), a transition timing constraint (i.e., timing constraint on a transition within a defined workflow), or a duration timing constraint (e.g., the duration of visit 2 is planned to take hours with a window of 30 minutes)._





URI: [odm:StudyTiming](http://www.cdisc.org/ns/odm/v2.0/StudyTiming)



```mermaid
 classDiagram
    class StudyTiming
      StudyTiming : AbsoluteTimingConstraintRef
        
          StudyTiming --|> AbsoluteTimingConstraint : AbsoluteTimingConstraintRef
        
      StudyTiming : DurationTimingConstraintRef
        
          StudyTiming --|> DurationTimingConstraint : DurationTimingConstraintRef
        
      StudyTiming : Name
        
      StudyTiming : OID
        
      StudyTiming : RelativeTimingConstraintRef
        
          StudyTiming --|> RelativeTimingConstraint : RelativeTimingConstraintRef
        
      StudyTiming : TransitionTimingConstraintRef
        
          StudyTiming --|> TransitionTimingConstraint : TransitionTimingConstraintRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier for a StudyTiming element. | direct |
| [Name](Name.md) | 1..1 <br/> [name](name.md) | Human readable identifier for a StudyTiming element. | direct |
| [AbsoluteTimingConstraintRef](AbsoluteTimingConstraintRef.md) | 0..* <br/> [AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | AbsoluteTimingConstraint reference: The element AbsoluteTimingConstraint is u... | direct |
| [RelativeTimingConstraintRef](RelativeTimingConstraintRef.md) | 0..* <br/> [RelativeTimingConstraint](RelativeTimingConstraint.md) | RelativeTimingConstraint reference: The RelativeTimingConstraint element desc... | direct |
| [TransitionTimingConstraintRef](TransitionTimingConstraintRef.md) | 0..* <br/> [TransitionTimingConstraint](TransitionTimingConstraint.md) | TransitionTimingConstraint reference: The TransitionTimingConstraint element ... | direct |
| [DurationTimingConstraintRef](DurationTimingConstraintRef.md) | 0..* <br/> [DurationTimingConstraint](DurationTimingConstraint.md) | DurationTimingConstraint reference: The DurationTimingConstraint constrains t... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyTimings](StudyTimings.md) | [StudyTimingRef](StudyTimingRef.md) | range | [StudyTiming](StudyTiming.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/StudyTiming](https://wiki.cdisc.org/display/ODM2/StudyTiming)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyTiming |
| native | odm:StudyTiming |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyTiming
description: The StudyTiming element defines a timing constraint within the study,
  which can be an absolute timing constraint (e.g., start of the screening visit must
  be between 1 January 2022 and 31 December 2022), a relative timing constraint (e.g.,
  visit 2 must be within 30 days after visit 1 with a window of +/- 1 week), a transition
  timing constraint (i.e., timing constraint on a transition within a defined workflow),
  or a duration timing constraint (e.g., the duration of visit 2 is planned to take
  hours with a window of 30 minutes).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyTiming
slots:
- OID
- Name
- AbsoluteTimingConstraintRef
- RelativeTimingConstraintRef
- TransitionTimingConstraintRef
- DurationTimingConstraintRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for a StudyTiming element.
    comments:
    - 'Required

      range:oid

      The StudyTiming/@OID value must be unique within the study.'
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
  Name:
    name: Name
    description: Human readable identifier for a StudyTiming element.
    comments:
    - 'Required

      range:name

      The StudyTiming/@Name value must be unique within the study.'
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
    range: name
    required: true
  AbsoluteTimingConstraintRef:
    name: AbsoluteTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: AbsoluteTimingConstraint
    inlined: true
    inlined_as_list: true
  RelativeTimingConstraintRef:
    name: RelativeTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: RelativeTimingConstraint
    inlined: true
    inlined_as_list: true
  TransitionTimingConstraintRef:
    name: TransitionTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: TransitionTimingConstraint
    inlined: true
    inlined_as_list: true
  DurationTimingConstraintRef:
    name: DurationTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: DurationTimingConstraint
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyTiming

```
</details>

### Induced

<details>
```yaml
name: StudyTiming
description: The StudyTiming element defines a timing constraint within the study,
  which can be an absolute timing constraint (e.g., start of the screening visit must
  be between 1 January 2022 and 31 December 2022), a relative timing constraint (e.g.,
  visit 2 must be within 30 days after visit 1 with a window of +/- 1 week), a transition
  timing constraint (i.e., timing constraint on a transition within a defined workflow),
  or a duration timing constraint (e.g., the duration of visit 2 is planned to take
  hours with a window of 30 minutes).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyTiming
slot_usage:
  OID:
    name: OID
    description: Unique identifier for a StudyTiming element.
    comments:
    - 'Required

      range:oid

      The StudyTiming/@OID value must be unique within the study.'
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
  Name:
    name: Name
    description: Human readable identifier for a StudyTiming element.
    comments:
    - 'Required

      range:name

      The StudyTiming/@Name value must be unique within the study.'
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
    range: name
    required: true
  AbsoluteTimingConstraintRef:
    name: AbsoluteTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: AbsoluteTimingConstraint
    inlined: true
    inlined_as_list: true
  RelativeTimingConstraintRef:
    name: RelativeTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: RelativeTimingConstraint
    inlined: true
    inlined_as_list: true
  TransitionTimingConstraintRef:
    name: TransitionTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: TransitionTimingConstraint
    inlined: true
    inlined_as_list: true
  DurationTimingConstraintRef:
    name: DurationTimingConstraintRef
    multivalued: true
    domain_of:
    - StudyTiming
    range: DurationTimingConstraint
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier for a StudyTiming element.
    comments:
    - 'Required

      range:oid

      The StudyTiming/@OID value must be unique within the study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: StudyTiming
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
  Name:
    name: Name
    description: Human readable identifier for a StudyTiming element.
    comments:
    - 'Required

      range:name

      The StudyTiming/@Name value must be unique within the study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: StudyTiming
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
    range: name
    required: true
  AbsoluteTimingConstraintRef:
    name: AbsoluteTimingConstraintRef
    description: 'AbsoluteTimingConstraint reference: The element AbsoluteTimingConstraint
      is used to specify when an activity, represented by either a StudyEventGroup
      or StudyEvent, can take place.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: AbsoluteTimingConstraintRef
    owner: StudyTiming
    domain_of:
    - StudyTiming
    range: AbsoluteTimingConstraint
    inlined: true
    inlined_as_list: true
  RelativeTimingConstraintRef:
    name: RelativeTimingConstraintRef
    description: 'RelativeTimingConstraint reference: The RelativeTimingConstraint
      element describes a relative timing constraint between 2 activities or groups
      of activities, represented by StudyEventGroups, StudyEvents, ItemGroups, or
      Items.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: RelativeTimingConstraintRef
    owner: StudyTiming
    domain_of:
    - StudyTiming
    range: RelativeTimingConstraint
    inlined: true
    inlined_as_list: true
  TransitionTimingConstraintRef:
    name: TransitionTimingConstraintRef
    description: 'TransitionTimingConstraint reference: The TransitionTimingConstraint
      element defines a timing constraint on a transition between structural elements
      as defined in a workflow. As such, it is a non-blocking constraint. This means
      that the transition is set on hold as long as the timing condition is not fulfilled,
      and is executed as soon as the timing condition is fulfilled.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: TransitionTimingConstraintRef
    owner: StudyTiming
    domain_of:
    - StudyTiming
    range: TransitionTimingConstraint
    inlined: true
    inlined_as_list: true
  DurationTimingConstraintRef:
    name: DurationTimingConstraintRef
    description: 'DurationTimingConstraint reference: The DurationTimingConstraint
      constrains the duration of an activity represented by a study, epoch, StudyEventGroupDef,
      StudyEventDef, ItemGroupDef, or ItemDef. It is used to constrain the duration
      of the visit, activity, or any other structural element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: DurationTimingConstraintRef
    owner: StudyTiming
    domain_of:
    - StudyTiming
    range: DurationTimingConstraint
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyTiming

```
</details>