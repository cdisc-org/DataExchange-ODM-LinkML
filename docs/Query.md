# Class: Query



URI: [odm:Query](http://www.cdisc.org/ns/odm/v2.0/Query)



```mermaid
 classDiagram
    class Query
      Query : AuditRecordRef
        
          Query --|> AuditRecord : AuditRecordRef
        
      Query : LastUpdateDatetime
        
      Query : Name
        
      Query : OID
        
      Query : Source
        
          Query --|> QuerySourceType : Source
        
      Query : State
        
          Query --|> QueryStateType : State
        
      Query : Target
        
      Query : Type
        
          Query --|> QueryType : Type
        
      Query : ValueRef
        
          Query --|> Value : ValueRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier of the version within the XML document | direct |
| [Source](Source.md) | 1..1 <br/> [QuerySourceType](QuerySourceType.md) |  | direct |
| [Target](Target.md) | 0..1 <br/> [Text](Text.md) |  | direct |
| [Type](Type.md) | 0..1 <br/> [QueryType](QueryType.md) | Type of page for page references indicated in the PageRefs attribute | direct |
| [State](State.md) | 1..1 <br/> [QueryStateType](QueryStateType.md) |  | direct |
| [LastUpdateDatetime](LastUpdateDatetime.md) | 1..1 <br/> [Datetime](Datetime.md) |  | direct |
| [Name](Name.md) | 0..1 <br/> [Name](Name.md) | General observation Sub Class | direct |
| [ValueRef](ValueRef.md) | 1..1 <br/> [Value](Value.md) |  | direct |
| [AuditRecordRef](AuditRecordRef.md) | 0..* <br/> [AuditRecord](AuditRecord.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Location](Location.md) | [QueryRef](QueryRef.md) | range | [Query](Query.md) |
| [ClinicalData](ClinicalData.md) | [QueryRef](QueryRef.md) | range | [Query](Query.md) |
| [SubjectData](SubjectData.md) | [QueryRef](QueryRef.md) | range | [Query](Query.md) |
| [StudyEventData](StudyEventData.md) | [QueryRef](QueryRef.md) | range | [Query](Query.md) |
| [ItemGroupData](ItemGroupData.md) | [QueryRef](QueryRef.md) | range | [Query](Query.md) |
| [ItemData](ItemData.md) | [QueryRef](QueryRef.md) | range | [Query](Query.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Query](https://wiki.cdisc.org/display/ODM2/Query)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Query |
| native | odm:Query |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Query
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Query
slots:
- OID
- Source
- Target
- Type
- State
- LastUpdateDatetime
- Name
- ValueRef
- AuditRecordRef
slot_usage:
  OID:
    name: OID
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
  Source:
    name: Source
    domain_of:
    - Origin
    - Query
    range: QuerySourceType
    required: true
  Target:
    name: Target
    domain_of:
    - Query
    range: text
  Type:
    name: Type
    domain_of:
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyObjective
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: QueryType
  State:
    name: State
    domain_of:
    - Query
    range: QueryStateType
    required: true
  LastUpdateDatetime:
    name: LastUpdateDatetime
    domain_of:
    - Query
    range: datetime
    required: true
  Name:
    name: Name
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
  ValueRef:
    name: ValueRef
    domain_of:
    - TrialPhase
    - ParameterValue
    - ItemData
    - Query
    range: Value
    required: true
    minimum_cardinality: 1
    maximum_cardinality: 1
  AuditRecordRef:
    name: AuditRecordRef
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    inlined: true
    inlined_as_list: true
class_uri: odm:Query

```
</details>

### Induced

<details>
```yaml
name: Query
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Query
slot_usage:
  OID:
    name: OID
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
  Source:
    name: Source
    domain_of:
    - Origin
    - Query
    range: QuerySourceType
    required: true
  Target:
    name: Target
    domain_of:
    - Query
    range: text
  Type:
    name: Type
    domain_of:
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyObjective
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: QueryType
  State:
    name: State
    domain_of:
    - Query
    range: QueryStateType
    required: true
  LastUpdateDatetime:
    name: LastUpdateDatetime
    domain_of:
    - Query
    range: datetime
    required: true
  Name:
    name: Name
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
  ValueRef:
    name: ValueRef
    domain_of:
    - TrialPhase
    - ParameterValue
    - ItemData
    - Query
    range: Value
    required: true
    minimum_cardinality: 1
    maximum_cardinality: 1
  AuditRecordRef:
    name: AuditRecordRef
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier of the version within the XML document.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: Query
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
  Source:
    name: Source
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Source
    owner: Query
    domain_of:
    - Origin
    - Query
    range: QuerySourceType
    required: true
  Target:
    name: Target
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Target
    owner: Query
    domain_of:
    - Query
    range: text
  Type:
    name: Type
    description: Type of page for page references indicated in the PageRefs attribute.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Type
    owner: Query
    domain_of:
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyObjective
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: QueryType
  State:
    name: State
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: State
    owner: Query
    domain_of:
    - Query
    range: QueryStateType
    required: true
  LastUpdateDatetime:
    name: LastUpdateDatetime
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: LastUpdateDatetime
    owner: Query
    domain_of:
    - Query
    range: datetime
    required: true
  Name:
    name: Name
    description: General observation Sub Class.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: Query
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
  ValueRef:
    name: ValueRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ValueRef
    owner: Query
    domain_of:
    - TrialPhase
    - ParameterValue
    - ItemData
    - Query
    range: Value
    required: true
    minimum_cardinality: 1
    maximum_cardinality: 1
  AuditRecordRef:
    name: AuditRecordRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: AuditRecordRef
    owner: Query
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    inlined: true
    inlined_as_list: true
class_uri: odm:Query

```
</details>