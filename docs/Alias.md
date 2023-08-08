# Class: Alias



URI: [odm:Alias](http://www.cdisc.org/ns/odm/v2.0/Alias)



```mermaid
 classDiagram
    class Alias
      Alias : Context
        
      Alias : Name
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [Context](Context.md) | 1..1 <br/> [Text](Text.md) |  | direct |
| [Name](Name.md) | 1..1 <br/> [Text](Text.md) | General observation Sub Class | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [StudyEventDef](StudyEventDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [ItemGroupDef](ItemGroupDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [ItemDef](ItemDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [CodeList](CodeList.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [ConditionDef](ConditionDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [MethodDef](MethodDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [CodeListItem](CodeListItem.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [EnumeratedItem](EnumeratedItem.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Alias |
| native | odm:Alias |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Alias
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- Context
- Name
slot_usage:
  Context:
    name: Context
    domain_of:
    - FormalExpression
    - Alias
    - ODMFileMetadata
    range: text
    required: true
  Name:
    name: Name
    domain_of:
    - StudyEventGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - Parameter
    - ReturnValue
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
    - Query
    - MetaDataVersion
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - ConditionDef
    - MethodDef
    - Standard
    - Alias
    - Location
    range: text
    required: true
class_uri: odm:Alias
unique_keys:
  UC-P-1:
    unique_key_name: UC-P-1
    unique_key_slots:
    - Context

```
</details>

### Induced

<details>
```yaml
name: Alias
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  Context:
    name: Context
    domain_of:
    - FormalExpression
    - Alias
    - ODMFileMetadata
    range: text
    required: true
  Name:
    name: Name
    domain_of:
    - StudyEventGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - Parameter
    - ReturnValue
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
    - Query
    - MetaDataVersion
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - ConditionDef
    - MethodDef
    - Standard
    - Alias
    - Location
    range: text
    required: true
attributes:
  Context:
    name: Context
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Context
    owner: Alias
    domain_of:
    - FormalExpression
    - Alias
    - ODMFileMetadata
    range: text
    required: true
  Name:
    name: Name
    description: General observation Sub Class.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: Alias
    domain_of:
    - StudyEventGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - Parameter
    - ReturnValue
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
    - Query
    - MetaDataVersion
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - ConditionDef
    - MethodDef
    - Standard
    - Alias
    - Location
    range: text
    required: true
class_uri: odm:Alias
unique_keys:
  UC-P-1:
    unique_key_name: UC-P-1
    unique_key_slots:
    - Context

```
</details>