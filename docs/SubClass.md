# Class: SubClass

_This element contains SubClass definitions._




URI: [odm:SubClass](http://www.cdisc.org/ns/odm/v2.0/SubClass)


```mermaid
erDiagram
SubClass {
    ItemGroupSubClass name  
    ItemGroupClassSubClass parentClass  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1..1 <br/> [ItemGroupSubClass](ItemGroupSubClass.md) | Name of the SubClass | direct |
| [parentClass](parentClass.md) | 0..1 <br/> [ItemGroupClassSubClass](ItemGroupClassSubClass.md) | For a nested or multilevel SubClass, the ParentClass attribute is used to def... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Class](Class.md) | [subClass](subClass.md) | range | [SubClass](SubClass.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/SubClass](https://wiki.cdisc.org/display/PUB/SubClass)

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
- https://wiki.cdisc.org/display/PUB/SubClass
rank: 1000
slots:
- name
- parentClass
slot_usage:
  name:
    name: name
    description: Name of the SubClass
    comments:
    - 'Required

      range: text

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
    - Organization
    - Location
    - Query
    range: ItemGroupSubClass
    required: true
  parentClass:
    name: parentClass
    description: For a nested or multilevel SubClass, the ParentClass attribute is
      used to define the hierarchy.
    comments:
    - 'Optional

      range: text

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
- https://wiki.cdisc.org/display/PUB/SubClass
rank: 1000
slot_usage:
  name:
    name: name
    description: Name of the SubClass
    comments:
    - 'Required

      range: text

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
    - Organization
    - Location
    - Query
    range: ItemGroupSubClass
    required: true
  parentClass:
    name: parentClass
    description: For a nested or multilevel SubClass, the ParentClass attribute is
      used to define the hierarchy.
    comments:
    - 'Optional

      range: text

      Text must follow CDISC Controlled Terminology for Class or SubClass.'
    domain_of:
    - SubClass
    range: ItemGroupClassSubClass
attributes:
  name:
    name: name
    description: Name of the SubClass
    comments:
    - 'Required

      range: text

      Text must follow CDISC Controlled Terminology for SubClass.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: name
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
    - Organization
    - Location
    - Query
    range: ItemGroupSubClass
    required: true
  parentClass:
    name: parentClass
    description: For a nested or multilevel SubClass, the ParentClass attribute is
      used to define the hierarchy.
    comments:
    - 'Optional

      range: text

      Text must follow CDISC Controlled Terminology for Class or SubClass.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: parentClass
    owner: SubClass
    domain_of:
    - SubClass
    range: ItemGroupClassSubClass
class_uri: odm:SubClass

```
</details>