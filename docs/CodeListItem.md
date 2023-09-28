# Class: CodeListItem

_Defines an individual member value of a codelist. It may include a display value in the child Decode element_




URI: [odm:CodeListItem](http://www.cdisc.org/ns/odm/v2.0/CodeListItem)


```mermaid
erDiagram
CodeListItem {
    valueType codedValue  
    decimal rank  
    YesOnly other  
    positiveInteger orderNumber  
    YesOnly extendedValue  
    oidref commentOID  
}
Alias {
    text context  
    text name  
}
Coding {
    text code  
    uriorcurie system  
    text systemName  
    text systemVersion  
    text label  
    uriorcurie href  
    uriorcurie ref  
    text commentOID  
}
Decode {

}
TranslatedText {
    languageType language  
    text type  
    contentType content  
}
Description {

}

CodeListItem ||--|o Description : "description"
CodeListItem ||--|o Decode : "decode"
CodeListItem ||--}o Coding : "coding"
CodeListItem ||--}o Alias : "alias"
Decode ||--}o TranslatedText : "translatedText"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [codedValue](codedValue.md) | 1..1 <br/> [valueType](valueType.md) | Value of the codelist item (as it would occur in clinical data). | direct |
| [rank](rank.md) | 0..1 <br/> [decimal](decimal.md) | Numeric significance of the CodeListItem relative to others in the CodeList. ... | direct |
| [other](other.md) | 0..1 <br/> [YesOnly](YesOnly.md) | Flag to indicate that the term represents "other" content. | direct |
| [orderNumber](orderNumber.md) | 0..1 <br/> [positiveInteger](positiveInteger.md) | Ordering on the CodeListItems (within a containing CodeListItem) for use when... | direct |
| [extendedValue](extendedValue.md) | 0..1 <br/> [YesOnly](YesOnly.md) |  | direct |
| [commentOID](commentOID.md) | 0..1 <br/> [oidref](oidref.md) | Reference to a CommentDef . | direct |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [decode](decode.md) | 0..1 <br/> [Decode](Decode.md) | Decode reference: The displayed value relating to the CodeListItem/@CodedValu... | direct |
| [coding](coding.md) | 0..* <br/> [Coding](Coding.md) | Coding reference: Coding references a symbol from a defined code system. It u... | direct |
| [alias](alias.md) | 0..* <br/> [Alias](Alias.md) | Alias reference: An Alias provides an additional name for an element. The Con... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CodeList](CodeList.md) | [codeListItem](codeListItem.md) | range | [CodeListItem](CodeListItem.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/CodeListItem](https://wiki.cdisc.org/display/PUB/CodeListItem)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:CodeListItem |
| native | odm:CodeListItem |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CodeListItem
description: Defines an individual member value of a codelist. It may include a display
  value in the child Decode element
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/CodeListItem
rank: 1000
slots:
- codedValue
- rank
- other
- orderNumber
- extendedValue
- commentOID
- description
- decode
- coding
- alias
slot_usage:
  codedValue:
    name: codedValue
    description: Value of the codelist item (as it would occur in clinical data).
    comments:
    - 'Required

      range: text'
    domain_of:
    - CodeListItem
    range: valueType
    required: true
  rank:
    name: rank
    description: Numeric significance of the CodeListItem relative to others in the
      CodeList. The Rank attribute may be used where the relative value corresponding
      to an enumeration cannot or should not be determined by its lexical order. For
      example, if you have a list of enumerated text values including "Low", "Medium",
      and "High" and wish to assign these relative numeric values 1, 2, and 3 respectively,
      you should include a Rank attribute for each CodeListItem defined. Without the
      applied rank attribute, the normal lexical ordering would be "High", "Low",
      and "Medium".
    comments:
    - 'Optional

      range: float'
    domain_of:
    - CodeListItem
    range: decimal
  other:
    name: other
    description: Flag to indicate that the term represents "other" content.
    comments:
    - 'Optional

      range: (Yes)'
    domain_of:
    - ItemRef
    - CodeListItem
    range: YesOnly
  orderNumber:
    name: orderNumber
    description: Ordering on the CodeListItems (within a containing CodeListItem)
      for use whenever a list of Items is presented to a user. The ordering does not
      imply anything about event scheduling, time ordering, or data correctness.
    comments:
    - 'Optional

      range: integer'
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
  extendedValue:
    name: extendedValue
    domain_of:
    - CodeListItem
    range: YesOnly
  commentOID:
    name: commentOID
    description: Reference to a CommentDef .
    comments:
    - 'Optional

      range: oidref'
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
  description:
    name: description
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
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  decode:
    name: decode
    domain_of:
    - CodeListItem
    range: Decode
    maximum_cardinality: 1
  coding:
    name: coding
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
  alias:
    name: alias
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
class_uri: odm:CodeListItem

```
</details>

### Induced

<details>
```yaml
name: CodeListItem
description: Defines an individual member value of a codelist. It may include a display
  value in the child Decode element
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/CodeListItem
rank: 1000
slot_usage:
  codedValue:
    name: codedValue
    description: Value of the codelist item (as it would occur in clinical data).
    comments:
    - 'Required

      range: text'
    domain_of:
    - CodeListItem
    range: valueType
    required: true
  rank:
    name: rank
    description: Numeric significance of the CodeListItem relative to others in the
      CodeList. The Rank attribute may be used where the relative value corresponding
      to an enumeration cannot or should not be determined by its lexical order. For
      example, if you have a list of enumerated text values including "Low", "Medium",
      and "High" and wish to assign these relative numeric values 1, 2, and 3 respectively,
      you should include a Rank attribute for each CodeListItem defined. Without the
      applied rank attribute, the normal lexical ordering would be "High", "Low",
      and "Medium".
    comments:
    - 'Optional

      range: float'
    domain_of:
    - CodeListItem
    range: decimal
  other:
    name: other
    description: Flag to indicate that the term represents "other" content.
    comments:
    - 'Optional

      range: (Yes)'
    domain_of:
    - ItemRef
    - CodeListItem
    range: YesOnly
  orderNumber:
    name: orderNumber
    description: Ordering on the CodeListItems (within a containing CodeListItem)
      for use whenever a list of Items is presented to a user. The ordering does not
      imply anything about event scheduling, time ordering, or data correctness.
    comments:
    - 'Optional

      range: integer'
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
  extendedValue:
    name: extendedValue
    domain_of:
    - CodeListItem
    range: YesOnly
  commentOID:
    name: commentOID
    description: Reference to a CommentDef .
    comments:
    - 'Optional

      range: oidref'
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
  description:
    name: description
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
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  decode:
    name: decode
    domain_of:
    - CodeListItem
    range: Decode
    maximum_cardinality: 1
  coding:
    name: coding
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
  alias:
    name: alias
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
  codedValue:
    name: codedValue
    description: Value of the codelist item (as it would occur in clinical data).
    comments:
    - 'Required

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: codedValue
    owner: CodeListItem
    domain_of:
    - CodeListItem
    range: valueType
    required: true
  rank:
    name: rank
    description: Numeric significance of the CodeListItem relative to others in the
      CodeList. The Rank attribute may be used where the relative value corresponding
      to an enumeration cannot or should not be determined by its lexical order. For
      example, if you have a list of enumerated text values including "Low", "Medium",
      and "High" and wish to assign these relative numeric values 1, 2, and 3 respectively,
      you should include a Rank attribute for each CodeListItem defined. Without the
      applied rank attribute, the normal lexical ordering would be "High", "Low",
      and "Medium".
    comments:
    - 'Optional

      range: float'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: rank
    owner: CodeListItem
    domain_of:
    - CodeListItem
    range: decimal
  other:
    name: other
    description: Flag to indicate that the term represents "other" content.
    comments:
    - 'Optional

      range: (Yes)'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: other
    owner: CodeListItem
    domain_of:
    - ItemRef
    - CodeListItem
    range: YesOnly
  orderNumber:
    name: orderNumber
    description: Ordering on the CodeListItems (within a containing CodeListItem)
      for use whenever a list of Items is presented to a user. The ordering does not
      imply anything about event scheduling, time ordering, or data correctness.
    comments:
    - 'Optional

      range: integer'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: orderNumber
    owner: CodeListItem
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
  extendedValue:
    name: extendedValue
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: extendedValue
    owner: CodeListItem
    domain_of:
    - CodeListItem
    range: YesOnly
  commentOID:
    name: commentOID
    description: Reference to a CommentDef .
    comments:
    - 'Optional

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: commentOID
    owner: CodeListItem
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
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: description
    owner: CodeListItem
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
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  decode:
    name: decode
    description: 'Decode reference: The displayed value relating to the CodeListItem/@CodedValue.
      This is often a label corresponding to a short name or alpha-numeric code. The
      actual Decode text is provided in a TranslatedText element so that it can be
      provided in different languages on a case report form or tabular data summary.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: decode
    owner: CodeListItem
    domain_of:
    - CodeListItem
    range: Decode
    maximum_cardinality: 1
  coding:
    name: coding
    description: 'Coding reference: Coding references a symbol from a defined code
      system. It uses a code defined in a terminology system to associate semantics
      with a given term, codelist, variable, or group of variables. The presence of
      a Coding element associates a meaning to its parent element. Including multiple
      Coding elements for a given parent indicates synonymous meanings provided by
      different code systems or code system versions.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: coding
    owner: CodeListItem
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
  alias:
    name: alias
    description: 'Alias reference: An Alias provides an additional name for an element.
      The Context attribute specifies the application domain in which this additional
      name is relevant.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: alias
    owner: CodeListItem
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
class_uri: odm:CodeListItem

```
</details>