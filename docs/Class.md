# Class: Class

_The Class element identifies which predefined Class within the model applies to the definition of the dataset._




URI: [odm:Class](http://www.cdisc.org/ns/odm/v2.0/Class)


```mermaid
erDiagram
Class {
    ItemGroupClass name  
}
SubClass {
    ItemGroupSubClass name  
    ItemGroupClassSubClass parentClass  
}

Class ||--}o SubClass : "subClass"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1..1 <br/> [ItemGroupClass](ItemGroupClass.md) | Name of the Class | direct |
| [subClass](subClass.md) | 0..* <br/> [SubClass](SubClass.md) | SubClass reference: This element contains SubClass definitions. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemGroupDef](ItemGroupDef.md) | [itemGroupClass](itemGroupClass.md) | range | [Class](Class.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Class](https://wiki.cdisc.org/display/PUB/Class)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Class |
| native | odm:Class |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Class
description: The Class element identifies which predefined Class within the model
  applies to the definition of the dataset.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Class
rank: 1000
slots:
- name
- subClass
slot_usage:
  name:
    name: name
    description: Name of the Class
    comments:
    - 'Conditional Required when ODM/@Context="Submission

      range: text

      Text must follow CDISC Controlled Terminology for General Observation Class.
      For analysis datasets, if the ItemGroupDef IsNonStandard attribute is used,
      the Class should not be provided.'
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
    range: ItemGroupClass
    required: true
  subClass:
    name: subClass
    multivalued: true
    domain_of:
    - Class
    range: SubClass
    inlined: true
    inlined_as_list: true
class_uri: odm:Class

```
</details>

### Induced

<details>
```yaml
name: Class
description: The Class element identifies which predefined Class within the model
  applies to the definition of the dataset.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Class
rank: 1000
slot_usage:
  name:
    name: name
    description: Name of the Class
    comments:
    - 'Conditional Required when ODM/@Context="Submission

      range: text

      Text must follow CDISC Controlled Terminology for General Observation Class.
      For analysis datasets, if the ItemGroupDef IsNonStandard attribute is used,
      the Class should not be provided.'
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
    range: ItemGroupClass
    required: true
  subClass:
    name: subClass
    multivalued: true
    domain_of:
    - Class
    range: SubClass
    inlined: true
    inlined_as_list: true
attributes:
  name:
    name: name
    description: Name of the Class
    comments:
    - 'Conditional Required when ODM/@Context="Submission

      range: text

      Text must follow CDISC Controlled Terminology for General Observation Class.
      For analysis datasets, if the ItemGroupDef IsNonStandard attribute is used,
      the Class should not be provided.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: name
    owner: Class
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
    range: ItemGroupClass
    required: true
  subClass:
    name: subClass
    description: 'SubClass reference: This element contains SubClass definitions.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: subClass
    owner: Class
    domain_of:
    - Class
    range: SubClass
    inlined: true
    inlined_as_list: true
class_uri: odm:Class

```
</details>