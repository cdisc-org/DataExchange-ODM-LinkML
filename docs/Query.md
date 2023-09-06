# Class: Query

_The Query element represents a request for clarification on a data item collected for a clinical trial, specifically a request from a sponsor or sponsor’s representative to an investigator to resolve an error or inconsistency discovered during data review. Queries can be created manually by individuals such as site monitors or data managers or automatically by systems. The full text of the Query exists in the Value child element. The optional Name attribute provide the means to provide a short identifier that can be included in listing or user interfaces._




URI: [odm:Query](http://www.cdisc.org/ns/odm/v2.0/Query)


```mermaid
erDiagram
Query {
    oid oID  
    QuerySourceType source  
    text target  
    QueryType type  
    QueryStateType state  
    datetime lastUpdateDatetime  
    nameType name  
}
AuditRecord {
    EditPointType editPoint  
    YesOrNo usedMethod  
}
SourceID {
    text content  
}
ReasonForChange {
    text content  
}
DateTimeStamp {
    datetime content  
}
LocationRef {
    oidref locationOID  
}
UserRef {
    oidref userOID  
}
Value {
    positiveInteger seqNum  
    text content  
}

Query ||--|o Value : "value"
Query ||--}o AuditRecord : "auditRecord"
AuditRecord ||--|o UserRef : "userRef"
AuditRecord ||--|o LocationRef : "locationRef"
AuditRecord ||--|o DateTimeStamp : "dateTimeStamp"
AuditRecord ||--|o ReasonForChange : "reasonForChange"
AuditRecord ||--|o SourceID : "sourceID"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [oID](oID.md) | 1..1 <br/> [oid](oid.md) | Query unique identifier | direct |
| [source](source.md) | 1..1 <br/> [QuerySourceType](QuerySourceType.md) | Origin of the Query. | direct |
| [target](target.md) | 0..1 <br/> [text](text.md) | Element upon which the Query is raised. The parent element is the Target when... | direct |
| [type](type.md) | 0..1 <br/> [QueryType](QueryType.md) | Indicates whether Is the Query was raised manually by a user or automatically... | direct |
| [state](state.md) | 1..1 <br/> [QueryStateType](QueryStateType.md) | Status of the Query | direct |
| [lastUpdateDatetime](lastUpdateDatetime.md) | 1..1 <br/> [datetime](datetime.md) | When was this Query updated? Will correspond to the creation date or the last... | direct |
| [name](name.md) | 0..1 <br/> [nameType](nameType.md) | Name for a query that can be used to identify the query in a listing or user ... | direct |
| [value](value.md) | 0..1 <br/> [Value](Value.md) | Human-readable designation of the trial phase. | direct |
| [auditRecord](auditRecord.md) | 0..* <br/> [AuditRecord](AuditRecord.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Location](Location.md) | [query](query.md) | range | [Query](Query.md) |
| [ClinicalData](ClinicalData.md) | [query](query.md) | range | [Query](Query.md) |
| [SubjectData](SubjectData.md) | [query](query.md) | range | [Query](Query.md) |
| [StudyEventData](StudyEventData.md) | [query](query.md) | range | [Query](Query.md) |
| [ItemGroupData](ItemGroupData.md) | [query](query.md) | range | [Query](Query.md) |
| [ItemData](ItemData.md) | [query](query.md) | range | [Query](Query.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Query](https://wiki.cdisc.org/display/PUB/Query)

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
description: The Query element represents a request for clarification on a data item
  collected for a clinical trial, specifically a request from a sponsor or sponsor’s
  representative to an investigator to resolve an error or inconsistency discovered
  during data review. Queries can be created manually by individuals such as site
  monitors or data managers or automatically by systems. The full text of the Query
  exists in the Value child element. The optional Name attribute provide the means
  to provide a short identifier that can be included in listing or user interfaces.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Query
rank: 1000
slots:
- oID
- source
- target
- type
- state
- lastUpdateDatetime
- name
- value
- auditRecord
slot_usage:
  oID:
    name: oID
    description: Query unique identifier
    comments:
    - Must be unique within a Study.
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
  source:
    name: source
    description: Origin of the Query.
    domain_of:
    - Origin
    - Query
    range: QuerySourceType
    required: true
  target:
    name: target
    description: Element upon which the Query is raised. The parent element is the
      Target when the Target attribute is omitted.
    comments:
    - Optional
    domain_of:
    - Query
    range: text
  type:
    name: type
    description: Indicates whether Is the Query was raised manually by a user or automatically
      via an edit check.
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
    range: QueryType
  state:
    name: state
    description: Status of the Query
    domain_of:
    - Query
    range: QueryStateType
    required: true
  lastUpdateDatetime:
    name: lastUpdateDatetime
    description: When was this Query updated? Will correspond to the creation date
      or the last updated date?
    domain_of:
    - Query
    range: datetime
    required: true
  name:
    name: name
    description: Name for a query that can be used to identify the query in a listing
      or user interface.
    comments:
    - Optional
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
  value:
    name: value
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: Value
    maximum_cardinality: 1
  auditRecord:
    name: auditRecord
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
description: The Query element represents a request for clarification on a data item
  collected for a clinical trial, specifically a request from a sponsor or sponsor’s
  representative to an investigator to resolve an error or inconsistency discovered
  during data review. Queries can be created manually by individuals such as site
  monitors or data managers or automatically by systems. The full text of the Query
  exists in the Value child element. The optional Name attribute provide the means
  to provide a short identifier that can be included in listing or user interfaces.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Query
rank: 1000
slot_usage:
  oID:
    name: oID
    description: Query unique identifier
    comments:
    - Must be unique within a Study.
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
  source:
    name: source
    description: Origin of the Query.
    domain_of:
    - Origin
    - Query
    range: QuerySourceType
    required: true
  target:
    name: target
    description: Element upon which the Query is raised. The parent element is the
      Target when the Target attribute is omitted.
    comments:
    - Optional
    domain_of:
    - Query
    range: text
  type:
    name: type
    description: Indicates whether Is the Query was raised manually by a user or automatically
      via an edit check.
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
    range: QueryType
  state:
    name: state
    description: Status of the Query
    domain_of:
    - Query
    range: QueryStateType
    required: true
  lastUpdateDatetime:
    name: lastUpdateDatetime
    description: When was this Query updated? Will correspond to the creation date
      or the last updated date?
    domain_of:
    - Query
    range: datetime
    required: true
  name:
    name: name
    description: Name for a query that can be used to identify the query in a listing
      or user interface.
    comments:
    - Optional
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
  value:
    name: value
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: Value
    maximum_cardinality: 1
  auditRecord:
    name: auditRecord
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
  oID:
    name: oID
    description: Query unique identifier
    comments:
    - Must be unique within a Study.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: oID
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
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  source:
    name: source
    description: Origin of the Query.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: source
    owner: Query
    domain_of:
    - Origin
    - Query
    range: QuerySourceType
    required: true
  target:
    name: target
    description: Element upon which the Query is raised. The parent element is the
      Target when the Target attribute is omitted.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: target
    owner: Query
    domain_of:
    - Query
    range: text
  type:
    name: type
    description: Indicates whether Is the Query was raised manually by a user or automatically
      via an edit check.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: type
    owner: Query
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
    range: QueryType
  state:
    name: state
    description: Status of the Query
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: state
    owner: Query
    domain_of:
    - Query
    range: QueryStateType
    required: true
  lastUpdateDatetime:
    name: lastUpdateDatetime
    description: When was this Query updated? Will correspond to the creation date
      or the last updated date?
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: lastUpdateDatetime
    owner: Query
    domain_of:
    - Query
    range: datetime
    required: true
  name:
    name: name
    description: Name for a query that can be used to identify the query in a listing
      or user interface.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: name
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
    - Organization
    - Location
    - Query
    range: nameType
  value:
    name: value
    description: Human-readable designation of the trial phase.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: value
    owner: Query
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: Value
    maximum_cardinality: 1
  auditRecord:
    name: auditRecord
    description: 'AuditRecord reference: An AuditRecord carries information pertaining
      to the creation, deletion, or modification of clinical data. This information
      includes who performed that action, and where, when, and why that action was
      performed.AuditRecord information describes a change to clinical data, but is
      not itself clinical data. The value of some clinical data can always be changed
      by a subsequent transaction, but history cannot be changed, only added to.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: auditRecord
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