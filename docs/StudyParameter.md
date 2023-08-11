# Class: StudyParameter



URI: [odm:StudyParameter](http://www.cdisc.org/ns/odm/v2.0/StudyParameter)



```mermaid
 classDiagram
    class StudyParameter
      StudyParameter : CodingRef
        
          StudyParameter --|> Coding : CodingRef
        
      StudyParameter : OID
        
      StudyParameter : ParameterValueRef
        
          StudyParameter --|> ParameterValue : ParameterValueRef
        
      StudyParameter : ShortName
        
      StudyParameter : Term
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier of the version within the XML document | direct |
| [Term](Term.md) | 1..1 <br/> [Name](Name.md) |  | direct |
| [ShortName](ShortName.md) | 0..1 <br/> [Name](Name.md) |  | direct |
| [ParameterValueRef](ParameterValueRef.md) | 1..1 <br/> [ParameterValue](ParameterValue.md) |  | direct |
| [CodingRef](CodingRef.md) | 0..* <br/> [Coding](Coding.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudySummary](StudySummary.md) | [StudyParameterRef](StudyParameterRef.md) | range | [StudyParameter](StudyParameter.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/StudyParameter](https://wiki.cdisc.org/display/ODM2/StudyParameter)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyParameter |
| native | odm:StudyParameter |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyParameter
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyParameter
slots:
- OID
- Term
- ShortName
- ParameterValueRef
- CodingRef
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
  Term:
    name: Term
    domain_of:
    - StudyParameter
    range: name
    required: true
  ShortName:
    name: ShortName
    domain_of:
    - StudyParameter
    range: name
  ParameterValueRef:
    name: ParameterValueRef
    domain_of:
    - StudyParameter
    range: ParameterValue
    required: true
    minimum_cardinality: 1
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyParameter

```
</details>

### Induced

<details>
```yaml
name: StudyParameter
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyParameter
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
  Term:
    name: Term
    domain_of:
    - StudyParameter
    range: name
    required: true
  ShortName:
    name: ShortName
    domain_of:
    - StudyParameter
    range: name
  ParameterValueRef:
    name: ParameterValueRef
    domain_of:
    - StudyParameter
    range: ParameterValue
    required: true
    minimum_cardinality: 1
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
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
    owner: StudyParameter
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
  Term:
    name: Term
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Term
    owner: StudyParameter
    domain_of:
    - StudyParameter
    range: name
    required: true
  ShortName:
    name: ShortName
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ShortName
    owner: StudyParameter
    domain_of:
    - StudyParameter
    range: name
  ParameterValueRef:
    name: ParameterValueRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ParameterValueRef
    owner: StudyParameter
    domain_of:
    - StudyParameter
    range: ParameterValue
    required: true
    minimum_cardinality: 1
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: CodingRef
    owner: StudyParameter
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyParameter

```
</details>