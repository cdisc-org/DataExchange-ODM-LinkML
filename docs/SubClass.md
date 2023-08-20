# Class: SubClass


_This element contains SubClass definitions._





URI: [odm:SubClass](http://www.cdisc.org/ns/odm/v2.0/SubClass)



```mermaid
 classDiagram
    class SubClass
      SubClass : Name
        
          SubClass --|> ItemGroupSubClass : Name
        
      SubClass : ParentClass
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [Name](Name.md) | 1..1 <br/> [ItemGroupSubClass](ItemGroupSubClass.md) | Name of the SubClass | direct |
| [ParentClass](ParentClass.md) | 0..1 <br/> [ItemGroupClassSubClass](ItemGroupClassSubClass.md) | For a nested or multilevel SubClass, the ParentClass attribute is used to def... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Class](Class.md) | [SubClassRef](SubClassRef.md) | range | [SubClass](SubClass.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/SubClass](https://wiki.cdisc.org/display/ODM2/SubClass)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SubClass |
| native | odm:SubClass |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SubClass
description: This element contains SubClass definitions.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SubClass
slots:
- Name
- ParentClass
slot_usage:
  Name:
    name: Name
    description: Name of the SubClass
    comments:
    - 'Required

      range:text

      Text must follow CDISC Controlled Terminology for SubClass.'
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
    range: ItemGroupSubClass
    required: true
  ParentClass:
    name: ParentClass
    description: 'For a nested or multilevel SubClass, the ParentClass attribute is
      used to define the hierarchy. '
    comments:
    - 'Optional

      range:text

      Text must follow CDISC Controlled Terminology for Class or SubClass.'
    domain_of:
    - SubClass
    range: ItemGroupClassSubClass
class_uri: odm:SubClass

```
</details>

### Induced

<details>
```yaml
name: SubClass
description: This element contains SubClass definitions.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SubClass
slot_usage:
  Name:
    name: Name
    description: Name of the SubClass
    comments:
    - 'Required

      range:text

      Text must follow CDISC Controlled Terminology for SubClass.'
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
    range: ItemGroupSubClass
    required: true
  ParentClass:
    name: ParentClass
    description: 'For a nested or multilevel SubClass, the ParentClass attribute is
      used to define the hierarchy. '
    comments:
    - 'Optional

      range:text

      Text must follow CDISC Controlled Terminology for Class or SubClass.'
    domain_of:
    - SubClass
    range: ItemGroupClassSubClass
attributes:
  Name:
    name: Name
    description: Name of the SubClass
    comments:
    - 'Required

      range:text

      Text must follow CDISC Controlled Terminology for SubClass.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: SubClass
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
    range: ItemGroupSubClass
    required: true
  ParentClass:
    name: ParentClass
    description: 'For a nested or multilevel SubClass, the ParentClass attribute is
      used to define the hierarchy. '
    comments:
    - 'Optional

      range:text

      Text must follow CDISC Controlled Terminology for Class or SubClass.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ParentClass
    owner: SubClass
    domain_of:
    - SubClass
    range: ItemGroupClassSubClass
class_uri: odm:SubClass

```
</details>