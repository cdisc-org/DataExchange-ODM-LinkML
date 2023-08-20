# Class: Parameter


_The Parameter element represents a method parameter used as part of a MethodSignature in MethodDef, ConditionDef, or RangeCheck._





URI: [odm:Parameter](http://www.cdisc.org/ns/odm/v2.0/Parameter)



```mermaid
 classDiagram
    class Parameter
      Parameter : DataTypeRef
        
          Parameter --|> DataType : DataTypeRef
        
      Parameter : DefinitionRef
        
      Parameter : Name
        
      Parameter : OrderNumber
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [Name](Name.md) | 1..1 <br/> [Name](Name.md) | The parameter name - typically the name of an ItemDef referenced in the ItemG... | direct |
| [DataTypeRef](DataTypeRef.md) | 1..1 <br/> [DataType](DataType.md) | Parameter datatype | direct |
| [DefinitionRef](DefinitionRef.md) | 0..1 <br/> [Text](Text.md) | A free-text definition of the parameter | direct |
| [OrderNumber](OrderNumber.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) | Position of the Parameter in the MethodSignature | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MethodSignature](MethodSignature.md) | [ParameterRef](ParameterRef.md) | range | [Parameter](Parameter.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Parameter](https://wiki.cdisc.org/display/ODM2/Parameter)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Parameter |
| native | odm:Parameter |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Parameter
description: The Parameter element represents a method parameter used as part of a
  MethodSignature in MethodDef, ConditionDef, or RangeCheck.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Parameter
slots:
- Name
- DataTypeRef
- DefinitionRef
- OrderNumber
slot_usage:
  Name:
    name: Name
    description: The parameter name - typically the name of an ItemDef referenced
      in the ItemGroupDef.
    comments:
    - 'Required

      range:name'
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
  DataTypeRef:
    name: DataTypeRef
    description: Parameter datatype.
    comments:
    - 'Required

      enum values:(text | integer | decimal | float | double | date | time | datetime
      | string | boolean | double | hexBinary | base64Binary | hexFloat | base64Float
      | partialDate | partialTime | partialDatetime | durationDatetime | intervalDatetime
      | incompleteDatetime | incompleteDate | incompleteTime | URI )'
    domain_of:
    - ItemDef
    - CodeList
    - Parameter
    - ReturnValue
    range: DataType
    required: true
  DefinitionRef:
    name: DefinitionRef
    description: A free-text definition of the parameter
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemDef
    - Parameter
    - ReturnValue
    range: text
  OrderNumber:
    name: OrderNumber
    description: Position of the Parameter in the MethodSignature
    comments:
    - 'Optional

      range:positiveInteger'
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    - CodeListItem
    - Parameter
    - ReturnValue
    - StudyEndPointRef
    range: positiveInteger
class_uri: odm:Parameter

```
</details>

### Induced

<details>
```yaml
name: Parameter
description: The Parameter element represents a method parameter used as part of a
  MethodSignature in MethodDef, ConditionDef, or RangeCheck.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Parameter
slot_usage:
  Name:
    name: Name
    description: The parameter name - typically the name of an ItemDef referenced
      in the ItemGroupDef.
    comments:
    - 'Required

      range:name'
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
  DataTypeRef:
    name: DataTypeRef
    description: Parameter datatype.
    comments:
    - 'Required

      enum values:(text | integer | decimal | float | double | date | time | datetime
      | string | boolean | double | hexBinary | base64Binary | hexFloat | base64Float
      | partialDate | partialTime | partialDatetime | durationDatetime | intervalDatetime
      | incompleteDatetime | incompleteDate | incompleteTime | URI )'
    domain_of:
    - ItemDef
    - CodeList
    - Parameter
    - ReturnValue
    range: DataType
    required: true
  DefinitionRef:
    name: DefinitionRef
    description: A free-text definition of the parameter
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemDef
    - Parameter
    - ReturnValue
    range: text
  OrderNumber:
    name: OrderNumber
    description: Position of the Parameter in the MethodSignature
    comments:
    - 'Optional

      range:positiveInteger'
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    - CodeListItem
    - Parameter
    - ReturnValue
    - StudyEndPointRef
    range: positiveInteger
attributes:
  Name:
    name: Name
    description: The parameter name - typically the name of an ItemDef referenced
      in the ItemGroupDef.
    comments:
    - 'Required

      range:name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: Parameter
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
  DataTypeRef:
    name: DataTypeRef
    description: Parameter datatype.
    comments:
    - 'Required

      enum values:(text | integer | decimal | float | double | date | time | datetime
      | string | boolean | double | hexBinary | base64Binary | hexFloat | base64Float
      | partialDate | partialTime | partialDatetime | durationDatetime | intervalDatetime
      | incompleteDatetime | incompleteDate | incompleteTime | URI )'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: DataTypeRef
    owner: Parameter
    domain_of:
    - ItemDef
    - CodeList
    - Parameter
    - ReturnValue
    range: DataType
    required: true
  DefinitionRef:
    name: DefinitionRef
    description: A free-text definition of the parameter
    comments:
    - 'Optional

      range:text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DefinitionRef
    owner: Parameter
    domain_of:
    - ItemDef
    - Parameter
    - ReturnValue
    range: text
  OrderNumber:
    name: OrderNumber
    description: Position of the Parameter in the MethodSignature
    comments:
    - 'Optional

      range:positiveInteger'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: OrderNumber
    owner: Parameter
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    - CodeListItem
    - Parameter
    - ReturnValue
    - StudyEndPointRef
    range: positiveInteger
class_uri: odm:Parameter

```
</details>