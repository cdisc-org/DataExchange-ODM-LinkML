# Class: Alias



URI: [odm:Alias](http://www.cdisc.org/ns/odm/v2.0/Alias)



```mermaid
 classDiagram
    class Alias
      Alias : ContextRef
        
      Alias : Name
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ContextRef](ContextRef.md) | 1..1 <br/> [Text](Text.md) |  | direct |
| [Name](Name.md) | 1..1 <br/> [Text](Text.md) | General observation Sub Class | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEventDef](StudyEventDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [ItemGroupDef](ItemGroupDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [ItemDef](ItemDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [CodeList](CodeList.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [CodeListItem](CodeListItem.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [MethodDef](MethodDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [ConditionDef](ConditionDef.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |
| [Protocol](Protocol.md) | [AliasRef](AliasRef.md) | range | [Alias](Alias.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Alias](https://wiki.cdisc.org/display/ODM2/Alias)

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
see_also:
- https://wiki.cdisc.org/display/ODM2/Alias
slots:
- ContextRef
- Name
slot_usage:
  ContextRef:
    name: ContextRef
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: text
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
    range: text
    required: true
class_uri: odm:Alias

```
</details>

### Induced

<details>
```yaml
name: Alias
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Alias
slot_usage:
  ContextRef:
    name: ContextRef
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: text
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
    range: text
    required: true
attributes:
  ContextRef:
    name: ContextRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ContextRef
    owner: Alias
    domain_of:
    - Alias
    - FormalExpression
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
    range: text
    required: true
class_uri: odm:Alias

```
</details>