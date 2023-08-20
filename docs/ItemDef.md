# Class: ItemDef


_An ItemDef describes a type of item that can occur within a study. Item properties include name, datatype, range, or codelist restrictions, and several other properties._





URI: [odm:ItemDef](http://www.cdisc.org/ns/odm/v2.0/ItemDef)



```mermaid
 classDiagram
    class ItemDef
      ItemDef : AliasRef
        
          ItemDef --|> Alias : AliasRef
        
      ItemDef : CDISCNotesRef
        
          ItemDef --|> CDISCNotes : CDISCNotesRef
        
      ItemDef : CodeListRefRef
        
          ItemDef --|> CodeListRef : CodeListRefRef
        
      ItemDef : CodingRef
        
          ItemDef --|> Coding : CodingRef
        
      ItemDef : CommentOID
        
      ItemDef : CRFCompletionInstructionsRef
        
          ItemDef --|> CRFCompletionInstructions : CRFCompletionInstructionsRef
        
      ItemDef : DataTypeRef
        
          ItemDef --|> DataType : DataTypeRef
        
      ItemDef : DefinitionRef
        
          ItemDef --|> Definition : DefinitionRef
        
      ItemDef : DescriptionRef
        
          ItemDef --|> Description : DescriptionRef
        
      ItemDef : DisplayFormat
        
      ItemDef : ImplementationNotesRef
        
          ItemDef --|> ImplementationNotes : ImplementationNotesRef
        
      ItemDef : Length
        
      ItemDef : Name
        
      ItemDef : OID
        
      ItemDef : PromptRef
        
          ItemDef --|> Prompt : PromptRef
        
      ItemDef : QuestionRef
        
          ItemDef --|> Question : QuestionRef
        
      ItemDef : RangeCheckRef
        
          ItemDef --|> RangeCheck : RangeCheckRef
        
      ItemDef : ValueListRefRef
        
          ItemDef --|> ValueListRef : ValueListRefRef
        
      ItemDef : VariableSet
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier for the ItemDef element | direct |
| [Name](Name.md) | 1..1 <br/> [Name](Name.md) | Human readable name for the ItemDef | direct |
| [DataTypeRef](DataTypeRef.md) | 1..1 <br/> [DataType](DataType.md) | Specification of the allowable values and the intended use of the correspondi... | direct |
| [Length](Length.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) | Specifies the number of characters allowed for the ItemData/Value when it is ... | direct |
| [DisplayFormat](DisplayFormat.md) | 0..1 <br/> [Text](Text.md) | Display format supports data visualization of numeric float and date values | direct |
| [VariableSet](VariableSet.md) | 0..1 <br/> [Text](Text.md) | ADaM variable set, e | direct |
| [CommentOID](CommentOID.md) | 0..1 <br/> [Oidref](Oidref.md) | Reference to a CommentDef with sponsor provided information related to this I... | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) |  | direct |
| [DefinitionRef](DefinitionRef.md) | 0..1 <br/> [Definition](Definition.md) | A free-text definition of the parameter | direct |
| [QuestionRef](QuestionRef.md) | 0..1 <br/> [Question](Question.md) |  | direct |
| [PromptRef](PromptRef.md) | 0..1 <br/> [Prompt](Prompt.md) |  | direct |
| [CRFCompletionInstructionsRef](CRFCompletionInstructionsRef.md) | 0..1 <br/> [CRFCompletionInstructions](CRFCompletionInstructions.md) |  | direct |
| [ImplementationNotesRef](ImplementationNotesRef.md) | 0..1 <br/> [ImplementationNotes](ImplementationNotes.md) |  | direct |
| [CDISCNotesRef](CDISCNotesRef.md) | 0..1 <br/> [CDISCNotes](CDISCNotes.md) |  | direct |
| [RangeCheckRef](RangeCheckRef.md) | 0..* <br/> [RangeCheck](RangeCheck.md) |  | direct |
| [CodeListRefRef](CodeListRefRef.md) | 0..1 <br/> [CodeListRef](CodeListRef.md) |  | direct |
| [ValueListRefRef](ValueListRefRef.md) | 0..1 <br/> [ValueListRef](ValueListRef.md) |  | direct |
| [CodingRef](CodingRef.md) | 0..* <br/> [Coding](Coding.md) |  | direct |
| [AliasRef](AliasRef.md) | 0..* <br/> [Alias](Alias.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [ItemDefRef](ItemDefRef.md) | range | [ItemDef](ItemDef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/ItemDef](https://wiki.cdisc.org/display/ODM2/ItemDef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemDef |
| native | odm:ItemDef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemDef
description: An ItemDef describes a type of item that can occur within a study. Item
  properties include name, datatype, range, or codelist restrictions, and several
  other properties.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemDef
slots:
- OID
- Name
- DataTypeRef
- Length
- DisplayFormat
- VariableSet
- CommentOID
- DescriptionRef
- DefinitionRef
- QuestionRef
- PromptRef
- CRFCompletionInstructionsRef
- ImplementationNotesRef
- CDISCNotesRef
- RangeCheckRef
- CodeListRefRef
- ValueListRefRef
- CodingRef
- AliasRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the ItemDef element.
    comments:
    - 'Required

      range:oid'
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
    description: Human readable name for the ItemDef.
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
    description: Specification of the allowable values and the intended use of the
      corresponding value elements.
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
  Length:
    name: Length
    description: Specifies the number of characters allowed for the ItemData/Value
      when it is represented as a text.
    comments:
    - 'Optional

      range:positiveInteger'
    domain_of:
    - ItemDef
    range: positiveInteger
  DisplayFormat:
    name: DisplayFormat
    description: 'Display format supports data visualization of numeric float and
      date values. '
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemDef
    range: text
  VariableSet:
    name: VariableSet
    description: ADaM variable set, e.g. Dose, Analysis Parameter, Treatment Timing.
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemDef
    range: text
  CommentOID:
    name: CommentOID
    description: Reference to a CommentDef with sponsor provided information related
      to this ItemDef,
    comments:
    - 'Optional

      range:oidref'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: oidref
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
  DefinitionRef:
    name: DefinitionRef
    domain_of:
    - ItemDef
    - Parameter
    - ReturnValue
    range: Definition
    maximum_cardinality: 1
  QuestionRef:
    name: QuestionRef
    domain_of:
    - ItemDef
    range: Question
    maximum_cardinality: 1
  PromptRef:
    name: PromptRef
    domain_of:
    - ItemDef
    range: Prompt
    maximum_cardinality: 1
  CRFCompletionInstructionsRef:
    name: CRFCompletionInstructionsRef
    domain_of:
    - ItemDef
    range: CRFCompletionInstructions
    maximum_cardinality: 1
  ImplementationNotesRef:
    name: ImplementationNotesRef
    domain_of:
    - ItemDef
    range: ImplementationNotes
    maximum_cardinality: 1
  CDISCNotesRef:
    name: CDISCNotesRef
    domain_of:
    - ItemDef
    range: CDISCNotes
    maximum_cardinality: 1
  RangeCheckRef:
    name: RangeCheckRef
    multivalued: true
    domain_of:
    - WhereClauseDef
    - ItemDef
    range: RangeCheck
    inlined: true
    inlined_as_list: true
  CodeListRefRef:
    name: CodeListRefRef
    domain_of:
    - MetaDataVersion
    - ItemDef
    range: CodeListRef
    maximum_cardinality: 1
  ValueListRefRef:
    name: ValueListRefRef
    domain_of:
    - ItemDef
    range: ValueListRef
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
  AliasRef:
    name: AliasRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
class_uri: odm:ItemDef

```
</details>

### Induced

<details>
```yaml
name: ItemDef
description: An ItemDef describes a type of item that can occur within a study. Item
  properties include name, datatype, range, or codelist restrictions, and several
  other properties.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemDef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the ItemDef element.
    comments:
    - 'Required

      range:oid'
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
    description: Human readable name for the ItemDef.
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
    description: Specification of the allowable values and the intended use of the
      corresponding value elements.
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
  Length:
    name: Length
    description: Specifies the number of characters allowed for the ItemData/Value
      when it is represented as a text.
    comments:
    - 'Optional

      range:positiveInteger'
    domain_of:
    - ItemDef
    range: positiveInteger
  DisplayFormat:
    name: DisplayFormat
    description: 'Display format supports data visualization of numeric float and
      date values. '
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemDef
    range: text
  VariableSet:
    name: VariableSet
    description: ADaM variable set, e.g. Dose, Analysis Parameter, Treatment Timing.
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemDef
    range: text
  CommentOID:
    name: CommentOID
    description: Reference to a CommentDef with sponsor provided information related
      to this ItemDef,
    comments:
    - 'Optional

      range:oidref'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: oidref
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
  DefinitionRef:
    name: DefinitionRef
    domain_of:
    - ItemDef
    - Parameter
    - ReturnValue
    range: Definition
    maximum_cardinality: 1
  QuestionRef:
    name: QuestionRef
    domain_of:
    - ItemDef
    range: Question
    maximum_cardinality: 1
  PromptRef:
    name: PromptRef
    domain_of:
    - ItemDef
    range: Prompt
    maximum_cardinality: 1
  CRFCompletionInstructionsRef:
    name: CRFCompletionInstructionsRef
    domain_of:
    - ItemDef
    range: CRFCompletionInstructions
    maximum_cardinality: 1
  ImplementationNotesRef:
    name: ImplementationNotesRef
    domain_of:
    - ItemDef
    range: ImplementationNotes
    maximum_cardinality: 1
  CDISCNotesRef:
    name: CDISCNotesRef
    domain_of:
    - ItemDef
    range: CDISCNotes
    maximum_cardinality: 1
  RangeCheckRef:
    name: RangeCheckRef
    multivalued: true
    domain_of:
    - WhereClauseDef
    - ItemDef
    range: RangeCheck
    inlined: true
    inlined_as_list: true
  CodeListRefRef:
    name: CodeListRefRef
    domain_of:
    - MetaDataVersion
    - ItemDef
    range: CodeListRef
    maximum_cardinality: 1
  ValueListRefRef:
    name: ValueListRefRef
    domain_of:
    - ItemDef
    range: ValueListRef
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
  AliasRef:
    name: AliasRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier for the ItemDef element.
    comments:
    - 'Required

      range:oid'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: ItemDef
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
    description: Human readable name for the ItemDef.
    comments:
    - 'Required

      range:name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: ItemDef
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
    description: Specification of the allowable values and the intended use of the
      corresponding value elements.
    comments:
    - 'Required

      enum values:(text | integer | decimal | float | double | date | time | datetime
      | string | boolean | double | hexBinary | base64Binary | hexFloat | base64Float
      | partialDate | partialTime | partialDatetime | durationDatetime | intervalDatetime
      | incompleteDatetime | incompleteDate | incompleteTime | URI )'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: DataTypeRef
    owner: ItemDef
    domain_of:
    - ItemDef
    - CodeList
    - Parameter
    - ReturnValue
    range: DataType
    required: true
  Length:
    name: Length
    description: Specifies the number of characters allowed for the ItemData/Value
      when it is represented as a text.
    comments:
    - 'Optional

      range:positiveInteger'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Length
    owner: ItemDef
    domain_of:
    - ItemDef
    range: positiveInteger
  DisplayFormat:
    name: DisplayFormat
    description: 'Display format supports data visualization of numeric float and
      date values. '
    comments:
    - 'Optional

      range:text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: DisplayFormat
    owner: ItemDef
    domain_of:
    - ItemDef
    range: text
  VariableSet:
    name: VariableSet
    description: ADaM variable set, e.g. Dose, Analysis Parameter, Treatment Timing.
    comments:
    - 'Optional

      range:text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: VariableSet
    owner: ItemDef
    domain_of:
    - ItemDef
    range: text
  CommentOID:
    name: CommentOID
    description: Reference to a CommentDef with sponsor provided information related
      to this ItemDef,
    comments:
    - 'Optional

      range:oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CommentOID
    owner: ItemDef
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: oidref
  DescriptionRef:
    name: DescriptionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
    owner: ItemDef
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
  DefinitionRef:
    name: DefinitionRef
    description: A free-text definition of the parameter
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DefinitionRef
    owner: ItemDef
    domain_of:
    - ItemDef
    - Parameter
    - ReturnValue
    range: Definition
    maximum_cardinality: 1
  QuestionRef:
    name: QuestionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: QuestionRef
    owner: ItemDef
    domain_of:
    - ItemDef
    range: Question
    maximum_cardinality: 1
  PromptRef:
    name: PromptRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: PromptRef
    owner: ItemDef
    domain_of:
    - ItemDef
    range: Prompt
    maximum_cardinality: 1
  CRFCompletionInstructionsRef:
    name: CRFCompletionInstructionsRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: CRFCompletionInstructionsRef
    owner: ItemDef
    domain_of:
    - ItemDef
    range: CRFCompletionInstructions
    maximum_cardinality: 1
  ImplementationNotesRef:
    name: ImplementationNotesRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: ImplementationNotesRef
    owner: ItemDef
    domain_of:
    - ItemDef
    range: ImplementationNotes
    maximum_cardinality: 1
  CDISCNotesRef:
    name: CDISCNotesRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: CDISCNotesRef
    owner: ItemDef
    domain_of:
    - ItemDef
    range: CDISCNotes
    maximum_cardinality: 1
  RangeCheckRef:
    name: RangeCheckRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: RangeCheckRef
    owner: ItemDef
    domain_of:
    - WhereClauseDef
    - ItemDef
    range: RangeCheck
    inlined: true
    inlined_as_list: true
  CodeListRefRef:
    name: CodeListRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: CodeListRefRef
    owner: ItemDef
    domain_of:
    - MetaDataVersion
    - ItemDef
    range: CodeListRef
    maximum_cardinality: 1
  ValueListRefRef:
    name: ValueListRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: ValueListRefRef
    owner: ItemDef
    domain_of:
    - ItemDef
    range: ValueListRef
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: CodingRef
    owner: ItemDef
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
  AliasRef:
    name: AliasRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: AliasRef
    owner: ItemDef
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
class_uri: odm:ItemDef

```
</details>