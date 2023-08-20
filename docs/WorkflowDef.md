# Class: WorkflowDef


_A WorkflowDef defines an automated workflow for a study._





URI: [odm:WorkflowDef](http://www.cdisc.org/ns/odm/v2.0/WorkflowDef)



```mermaid
 classDiagram
    class WorkflowDef
      WorkflowDef : BranchingRef
        
          WorkflowDef --|> Branching : BranchingRef
        
      WorkflowDef : DescriptionRef
        
          WorkflowDef --|> Description : DescriptionRef
        
      WorkflowDef : Name
        
      WorkflowDef : OID
        
      WorkflowDef : TransitionRef
        
          WorkflowDef --|> Transition : TransitionRef
        
      WorkflowDef : WorkflowEndRef
        
          WorkflowDef --|> WorkflowEnd : WorkflowEndRef
        
      WorkflowDef : WorkflowStartRef
        
          WorkflowDef --|> WorkflowStart : WorkflowStartRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier for the workflow | direct |
| [Name](Name.md) | 1..1 <br/> [Name](Name.md) | Human readable label for the workflow | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) |  | direct |
| [WorkflowStartRef](WorkflowStartRef.md) | 0..1 <br/> [WorkflowStart](WorkflowStart.md) |  | direct |
| [WorkflowEndRef](WorkflowEndRef.md) | 0..* <br/> [WorkflowEnd](WorkflowEnd.md) |  | direct |
| [TransitionRef](TransitionRef.md) | 0..* <br/> [Transition](Transition.md) |  | direct |
| [BranchingRef](BranchingRef.md) | 0..* <br/> [Branching](Branching.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [WorkflowDefRef](WorkflowDefRef.md) | range | [WorkflowDef](WorkflowDef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/WorkflowDef](https://wiki.cdisc.org/display/ODM2/WorkflowDef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:WorkflowDef |
| native | odm:WorkflowDef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkflowDef
description: A WorkflowDef defines an automated workflow for a study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/WorkflowDef
slots:
- OID
- Name
- DescriptionRef
- WorkflowStartRef
- WorkflowEndRef
- TransitionRef
- BranchingRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the workflow.
    comments:
    - 'Required

      range:oid

      The OID attribute value must be unique within the Study.'
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
    description: 'Human readable label for the workflow. '
    comments:
    - 'Required

      range:name

      The Name attribute value must be unique within the Study.'
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
  DescriptionRef:
    name: DescriptionRef
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
    maximum_cardinality: 1
  WorkflowStartRef:
    name: WorkflowStartRef
    domain_of:
    - WorkflowDef
    range: WorkflowStart
    maximum_cardinality: 1
  WorkflowEndRef:
    name: WorkflowEndRef
    multivalued: true
    domain_of:
    - WorkflowDef
    range: WorkflowEnd
    inlined: true
    inlined_as_list: true
  TransitionRef:
    name: TransitionRef
    multivalued: true
    domain_of:
    - WorkflowDef
    range: Transition
    inlined: true
    inlined_as_list: true
  BranchingRef:
    name: BranchingRef
    multivalued: true
    domain_of:
    - WorkflowDef
    range: Branching
    inlined: true
    inlined_as_list: true
class_uri: odm:WorkflowDef

```
</details>

### Induced

<details>
```yaml
name: WorkflowDef
description: A WorkflowDef defines an automated workflow for a study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/WorkflowDef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the workflow.
    comments:
    - 'Required

      range:oid

      The OID attribute value must be unique within the Study.'
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
    description: 'Human readable label for the workflow. '
    comments:
    - 'Required

      range:name

      The Name attribute value must be unique within the Study.'
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
  DescriptionRef:
    name: DescriptionRef
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
    maximum_cardinality: 1
  WorkflowStartRef:
    name: WorkflowStartRef
    domain_of:
    - WorkflowDef
    range: WorkflowStart
    maximum_cardinality: 1
  WorkflowEndRef:
    name: WorkflowEndRef
    multivalued: true
    domain_of:
    - WorkflowDef
    range: WorkflowEnd
    inlined: true
    inlined_as_list: true
  TransitionRef:
    name: TransitionRef
    multivalued: true
    domain_of:
    - WorkflowDef
    range: Transition
    inlined: true
    inlined_as_list: true
  BranchingRef:
    name: BranchingRef
    multivalued: true
    domain_of:
    - WorkflowDef
    range: Branching
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier for the workflow.
    comments:
    - 'Required

      range:oid

      The OID attribute value must be unique within the Study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: WorkflowDef
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
    description: 'Human readable label for the workflow. '
    comments:
    - 'Required

      range:name

      The Name attribute value must be unique within the Study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: WorkflowDef
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
  DescriptionRef:
    name: DescriptionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
    owner: WorkflowDef
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
    maximum_cardinality: 1
  WorkflowStartRef:
    name: WorkflowStartRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: WorkflowStartRef
    owner: WorkflowDef
    domain_of:
    - WorkflowDef
    range: WorkflowStart
    maximum_cardinality: 1
  WorkflowEndRef:
    name: WorkflowEndRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: WorkflowEndRef
    owner: WorkflowDef
    domain_of:
    - WorkflowDef
    range: WorkflowEnd
    inlined: true
    inlined_as_list: true
  TransitionRef:
    name: TransitionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: TransitionRef
    owner: WorkflowDef
    domain_of:
    - WorkflowDef
    range: Transition
    inlined: true
    inlined_as_list: true
  BranchingRef:
    name: BranchingRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: BranchingRef
    owner: WorkflowDef
    domain_of:
    - WorkflowDef
    range: Branching
    inlined: true
    inlined_as_list: true
class_uri: odm:WorkflowDef

```
</details>