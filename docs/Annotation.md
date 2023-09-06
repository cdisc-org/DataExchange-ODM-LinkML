# Class: Annotation

_A general note about clinical data. If an annotation has both a comment and flags, the flags should be related to the comment._




URI: [odm:Annotation](http://www.cdisc.org/ns/odm/v2.0/Annotation)


```mermaid
erDiagram
Annotation {
    positiveInteger seqNum  
    TransactionType transactionType  
    oid iD  
}
Flag {

}
FlagType {
    oidref codeListOID  
    nameType content  
}
FlagValue {
    oidref codeListOID  
    nameType content  
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
Comment {
    CommentType sponsorOrSite  
}
TranslatedText {
    languageType language  
    text type  
    contentType content  
}

Annotation ||--|o Comment : "comment"
Annotation ||--}o Coding : "coding"
Annotation ||--}o Flag : "flag"
Flag ||--|o FlagValue : "flagValue"
Flag ||--|o FlagType : "flagType"
Comment ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [seqNum](seqNum.md) | 1..1 <br/> [positiveInteger](positiveInteger.md) | When more than 1 Value element exists this attribute uniquely identifies each... | direct |
| [transactionType](transactionType.md) | 0..1 <br/> [TransactionType](TransactionType.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... | direct |
| [iD](iD.md) | 1..1 <br/> [oid](oid.md) | Unique identifier for the leaf that is referenced. | direct |
| [comment](comment.md) | 0..1 <br/> [Comment](Comment.md) | Comment reference: A free-text (uninterpreted) comment about clinical data. T... | direct |
| [coding](coding.md) | 0..* <br/> [Coding](Coding.md) | Coding reference: Coding references a symbol from a defined code system. It u... | direct |
| [flag](flag.md) | 0..* <br/> [Flag](Flag.md) | Flag reference: A machine-processable annotation. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReferenceData](ReferenceData.md) | [annotation](annotation.md) | range | [Annotation](Annotation.md) |
| [ClinicalData](ClinicalData.md) | [annotation](annotation.md) | range | [Annotation](Annotation.md) |
| [SubjectData](SubjectData.md) | [annotation](annotation.md) | range | [Annotation](Annotation.md) |
| [StudyEventData](StudyEventData.md) | [annotation](annotation.md) | range | [Annotation](Annotation.md) |
| [ItemGroupData](ItemGroupData.md) | [annotation](annotation.md) | range | [Annotation](Annotation.md) |
| [ItemData](ItemData.md) | [annotation](annotation.md) | range | [Annotation](Annotation.md) |
| [Association](Association.md) | [annotation](annotation.md) | range | [Annotation](Annotation.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Annotation](https://wiki.cdisc.org/display/PUB/Annotation)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Annotation |
| native | odm:Annotation |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Annotation
description: A general note about clinical data. If an annotation has both a comment
  and flags, the flags should be related to the comment.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Annotation
rank: 1000
slots:
- seqNum
- transactionType
- iD
- comment
- coding
- flag
slot_usage:
  seqNum:
    name: seqNum
    comments:
    - 'Required

      range: positiveInteger'
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
    required: true
  transactionType:
    name: transactionType
    comments:
    - 'Optional

      enum values: (Insert | Update | Remove | Upsert | Context)

      An empty Annotation (one with no annotation value, no comment and no flags)
      is not allowed unless the TransactionType is Remove. On Update, the entire value
      of the annotation is replaced.'
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  iD:
    name: iD
    domain_of:
    - Leaf
    - Signature
    - Annotation
    range: oid
  comment:
    name: comment
    domain_of:
    - Annotation
    range: Comment
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
  flag:
    name: flag
    multivalued: true
    domain_of:
    - Annotation
    range: Flag
    inlined: true
    inlined_as_list: true
class_uri: odm:Annotation

```
</details>

### Induced

<details>
```yaml
name: Annotation
description: A general note about clinical data. If an annotation has both a comment
  and flags, the flags should be related to the comment.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Annotation
rank: 1000
slot_usage:
  seqNum:
    name: seqNum
    comments:
    - 'Required

      range: positiveInteger'
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
    required: true
  transactionType:
    name: transactionType
    comments:
    - 'Optional

      enum values: (Insert | Update | Remove | Upsert | Context)

      An empty Annotation (one with no annotation value, no comment and no flags)
      is not allowed unless the TransactionType is Remove. On Update, the entire value
      of the annotation is replaced.'
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  iD:
    name: iD
    domain_of:
    - Leaf
    - Signature
    - Annotation
    range: oid
  comment:
    name: comment
    domain_of:
    - Annotation
    range: Comment
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
  flag:
    name: flag
    multivalued: true
    domain_of:
    - Annotation
    range: Flag
    inlined: true
    inlined_as_list: true
attributes:
  seqNum:
    name: seqNum
    description: When more than 1 Value element exists this attribute uniquely identifies
      each Value and defines the order of a Value in a list of Values.
    comments:
    - 'Required

      range: positiveInteger'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: seqNum
    owner: Annotation
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
    required: true
  transactionType:
    name: transactionType
    description: Identifies the transaction type when /ODM/@FileType is Transactional
      and there is no child element.
    comments:
    - 'Optional

      enum values: (Insert | Update | Remove | Upsert | Context)

      An empty Annotation (one with no annotation value, no comment and no flags)
      is not allowed unless the TransactionType is Remove. On Update, the entire value
      of the annotation is replaced.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: transactionType
    owner: Annotation
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  iD:
    name: iD
    description: Unique identifier for the leaf that is referenced.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: iD
    owner: Annotation
    domain_of:
    - Leaf
    - Signature
    - Annotation
    range: oid
    required: true
  comment:
    name: comment
    description: 'Comment reference: A free-text (uninterpreted) comment about clinical
      data. The comment may have come from the sponsor or the clinical site.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: comment
    owner: Annotation
    domain_of:
    - Annotation
    range: Comment
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
    owner: Annotation
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
  flag:
    name: flag
    description: 'Flag reference: A machine-processable annotation.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: flag
    owner: Annotation
    domain_of:
    - Annotation
    range: Flag
    inlined: true
    inlined_as_list: true
class_uri: odm:Annotation

```
</details>