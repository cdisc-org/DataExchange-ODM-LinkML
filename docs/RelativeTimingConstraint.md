# Class: RelativeTimingConstraint

_The RelativeTimingConstraint element describes a relative timing constraint between 2 activities or groups of activities, represented by StudyEventGroups, StudyEvents, ItemGroups, or Items._




URI: [odm:RelativeTimingConstraint](http://www.cdisc.org/ns/odm/v2.0/RelativeTimingConstraint)


```mermaid
erDiagram
RelativeTimingConstraint {
    oid OID  
    nameType name  
    string predecessorOID  
    string successorOID  
    RelativeTimingConstraintType type  
    durationDatetime timepointRelativeTarget  
    durationDatetime timepointPreWindow  
    durationDatetime timepointPostWindow  
}
Description {

}
TranslatedText {
    languageType language  
    text type  
    contentType content  
}

RelativeTimingConstraint ||--|o Description : "description"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier. | direct |
| [name](name.md) | 1..1 <br/> [nameType](nameType.md) | Human readable name. | direct |
| [predecessorOID](predecessorOID.md) | 0..1 <br/> [string](string.md) | Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that occurs immed... | direct |
| [successorOID](successorOID.md) | 0..1 <br/> [string](string.md) | Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs immedi... | direct |
| [type](type.md) | 0..1 <br/> [RelativeTimingConstraintType](RelativeTimingConstraintType.md) | Defines how the timing is to be defined between the two activities, starting ... | direct |
| [timepointRelativeTarget](timepointRelativeTarget.md) | 1..1 <br/> [durationDatetime](durationDatetime.md) | The relative timing between two activities or groups of activities. | direct |
| [timepointPreWindow](timepointPreWindow.md) | 0..1 <br/> [durationDatetime](durationDatetime.md) | Adds a lower bound to a time window for the RelativeTimepointTarget. | direct |
| [timepointPostWindow](timepointPostWindow.md) | 0..1 <br/> [durationDatetime](durationDatetime.md) | Adds an upper bound to a time window for the RelativeTimepointTarget. | direct |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyTiming](StudyTiming.md) | [relativeTimingConstraint](relativeTimingConstraint.md) | range | [RelativeTimingConstraint](RelativeTimingConstraint.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/RelativeTimingConstraint](https://wiki.cdisc.org/display/PUB/RelativeTimingConstraint)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:RelativeTimingConstraint |
| native | odm:RelativeTimingConstraint |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RelativeTimingConstraint
description: The RelativeTimingConstraint element describes a relative timing constraint
  between 2 activities or groups of activities, represented by StudyEventGroups, StudyEvents,
  ItemGroups, or Items.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/RelativeTimingConstraint
rank: 1000
slots:
- OID
- name
- predecessorOID
- successorOID
- type
- timepointRelativeTarget
- timepointPreWindow
- timepointPostWindow
- description
slot_usage:
  OID:
    name: OID
    description: Unique identifier.
    comments:
    - Required
    identifier: true
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
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  name:
    name: name
    description: Human readable name.
    comments:
    - Required
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
    - Organization
    - Location
    - Query
    range: nameType
    required: true
  predecessorOID:
    name: predecessorOID
    description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that
      occurs immediately before the RelativeTimepointTarget.
    comments:
    - Required
    domain_of:
    - RelativeTimingConstraint
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  successorOID:
    name: successorOID
    description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs
      immediately after the RelativeTimepointTarget.
    comments:
    - Required
    domain_of:
    - RelativeTimingConstraint
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  type:
    name: type
    description: Defines how the timing is to be defined between the two activities,
      starting from the start or the end of the source activity, and ending at the
      start or the end of the target activity.
    comments:
    - Optional
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: RelativeTimingConstraintType
  timepointRelativeTarget:
    name: timepointRelativeTarget
    description: The relative timing between two activities or groups of activities.
    comments:
    - Required
    domain_of:
    - RelativeTimingConstraint
    range: durationDatetime
    required: true
  timepointPreWindow:
    name: timepointPreWindow
    description: Adds a lower bound to a time window for the RelativeTimepointTarget.
    comments:
    - Optional
    domain_of:
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    range: durationDatetime
  timepointPostWindow:
    name: timepointPostWindow
    description: Adds an upper bound to a time window for the RelativeTimepointTarget.
    comments:
    - Optional
    domain_of:
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    range: durationDatetime
  description:
    name: description
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
    maximum_cardinality: 1
class_uri: odm:RelativeTimingConstraint

```
</details>

### Induced

<details>
```yaml
name: RelativeTimingConstraint
description: The RelativeTimingConstraint element describes a relative timing constraint
  between 2 activities or groups of activities, represented by StudyEventGroups, StudyEvents,
  ItemGroups, or Items.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/RelativeTimingConstraint
rank: 1000
slot_usage:
  OID:
    name: OID
    description: Unique identifier.
    comments:
    - Required
    identifier: true
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
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  name:
    name: name
    description: Human readable name.
    comments:
    - Required
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
    - Organization
    - Location
    - Query
    range: nameType
    required: true
  predecessorOID:
    name: predecessorOID
    description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that
      occurs immediately before the RelativeTimepointTarget.
    comments:
    - Required
    domain_of:
    - RelativeTimingConstraint
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  successorOID:
    name: successorOID
    description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs
      immediately after the RelativeTimepointTarget.
    comments:
    - Required
    domain_of:
    - RelativeTimingConstraint
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  type:
    name: type
    description: Defines how the timing is to be defined between the two activities,
      starting from the start or the end of the source activity, and ending at the
      start or the end of the target activity.
    comments:
    - Optional
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: RelativeTimingConstraintType
  timepointRelativeTarget:
    name: timepointRelativeTarget
    description: The relative timing between two activities or groups of activities.
    comments:
    - Required
    domain_of:
    - RelativeTimingConstraint
    range: durationDatetime
    required: true
  timepointPreWindow:
    name: timepointPreWindow
    description: Adds a lower bound to a time window for the RelativeTimepointTarget.
    comments:
    - Optional
    domain_of:
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    range: durationDatetime
  timepointPostWindow:
    name: timepointPostWindow
    description: Adds an upper bound to a time window for the RelativeTimepointTarget.
    comments:
    - Optional
    domain_of:
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    range: durationDatetime
  description:
    name: description
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
    maximum_cardinality: 1
attributes:
  OID:
    name: OID
    description: Unique identifier.
    comments:
    - Required
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: RelativeTimingConstraint
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
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  name:
    name: name
    description: Human readable name.
    comments:
    - Required
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: name
    owner: RelativeTimingConstraint
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
    - Organization
    - Location
    - Query
    range: nameType
    required: true
  predecessorOID:
    name: predecessorOID
    description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that
      occurs immediately before the RelativeTimepointTarget.
    comments:
    - Required
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: predecessorOID
    owner: RelativeTimingConstraint
    domain_of:
    - RelativeTimingConstraint
    range: string
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  successorOID:
    name: successorOID
    description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs
      immediately after the RelativeTimepointTarget.
    comments:
    - Required
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: successorOID
    owner: RelativeTimingConstraint
    domain_of:
    - RelativeTimingConstraint
    range: string
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  type:
    name: type
    description: Defines how the timing is to be defined between the two activities,
      starting from the start or the end of the source activity, and ending at the
      start or the end of the target activity.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: type
    owner: RelativeTimingConstraint
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: RelativeTimingConstraintType
  timepointRelativeTarget:
    name: timepointRelativeTarget
    description: The relative timing between two activities or groups of activities.
    comments:
    - Required
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: timepointRelativeTarget
    owner: RelativeTimingConstraint
    domain_of:
    - RelativeTimingConstraint
    range: durationDatetime
    required: true
  timepointPreWindow:
    name: timepointPreWindow
    description: Adds a lower bound to a time window for the RelativeTimepointTarget.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: timepointPreWindow
    owner: RelativeTimingConstraint
    domain_of:
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    range: durationDatetime
  timepointPostWindow:
    name: timepointPostWindow
    description: Adds an upper bound to a time window for the RelativeTimepointTarget.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: timepointPostWindow
    owner: RelativeTimingConstraint
    domain_of:
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    range: durationDatetime
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: description
    owner: RelativeTimingConstraint
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
    maximum_cardinality: 1
class_uri: odm:RelativeTimingConstraint

```
</details>