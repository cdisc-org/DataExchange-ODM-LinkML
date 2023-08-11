# Class: Annotation



URI: [odm:Annotation](http://www.cdisc.org/ns/odm/v2.0/Annotation)



```mermaid
 classDiagram
    class Annotation
      Annotation : CodingRef
        
          Annotation --|> Coding : CodingRef
        
      Annotation : CommentRef
        
          Annotation --|> Comment : CommentRef
        
      Annotation : FlagRef
        
          Annotation --|> Flag : FlagRef
        
      Annotation : ID
        
      Annotation : SeqNum
        
      Annotation : TransactionTypeRef
        
          Annotation --|> TransactionType : TransactionTypeRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [SeqNum](SeqNum.md) | 1..1 <br/> [PositiveInteger](PositiveInteger.md) |  | direct |
| [TransactionTypeRef](TransactionTypeRef.md) | 0..1 <br/> [TransactionType](TransactionType.md) |  | direct |
| [ID](ID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier for the leaf that is referenced | direct |
| [CommentRef](CommentRef.md) | 0..1 <br/> [Comment](Comment.md) |  | direct |
| [CodingRef](CodingRef.md) | 0..* <br/> [Coding](Coding.md) |  | direct |
| [FlagRef](FlagRef.md) | 0..* <br/> [Flag](Flag.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReferenceData](ReferenceData.md) | [AnnotationRef](AnnotationRef.md) | range | [Annotation](Annotation.md) |
| [ClinicalData](ClinicalData.md) | [AnnotationRef](AnnotationRef.md) | range | [Annotation](Annotation.md) |
| [SubjectData](SubjectData.md) | [AnnotationRef](AnnotationRef.md) | range | [Annotation](Annotation.md) |
| [StudyEventData](StudyEventData.md) | [AnnotationRef](AnnotationRef.md) | range | [Annotation](Annotation.md) |
| [ItemGroupData](ItemGroupData.md) | [AnnotationRef](AnnotationRef.md) | range | [Annotation](Annotation.md) |
| [ItemData](ItemData.md) | [AnnotationRef](AnnotationRef.md) | range | [Annotation](Annotation.md) |
| [Association](Association.md) | [AnnotationRef](AnnotationRef.md) | range | [Annotation](Annotation.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Annotation](https://wiki.cdisc.org/display/ODM2/Annotation)

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
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Annotation
slots:
- SeqNum
- TransactionTypeRef
- ID
- CommentRef
- CodingRef
- FlagRef
slot_usage:
  SeqNum:
    name: SeqNum
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
    required: true
  TransactionTypeRef:
    name: TransactionTypeRef
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  ID:
    name: ID
    domain_of:
    - leaf
    - Signature
    - Annotation
    range: oid
  CommentRef:
    name: CommentRef
    domain_of:
    - Annotation
    range: Comment
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
  FlagRef:
    name: FlagRef
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
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Annotation
slot_usage:
  SeqNum:
    name: SeqNum
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
    required: true
  TransactionTypeRef:
    name: TransactionTypeRef
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  ID:
    name: ID
    domain_of:
    - leaf
    - Signature
    - Annotation
    range: oid
  CommentRef:
    name: CommentRef
    domain_of:
    - Annotation
    range: Comment
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
  FlagRef:
    name: FlagRef
    multivalued: true
    domain_of:
    - Annotation
    range: Flag
    inlined: true
    inlined_as_list: true
attributes:
  SeqNum:
    name: SeqNum
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SeqNum
    owner: Annotation
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
    required: true
  TransactionTypeRef:
    name: TransactionTypeRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: TransactionTypeRef
    owner: Annotation
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  ID:
    name: ID
    description: Unique identifier for the leaf that is referenced.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: ID
    owner: Annotation
    domain_of:
    - leaf
    - Signature
    - Annotation
    range: oid
    required: true
  CommentRef:
    name: CommentRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CommentRef
    owner: Annotation
    domain_of:
    - Annotation
    range: Comment
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: CodingRef
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
  FlagRef:
    name: FlagRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: FlagRef
    owner: Annotation
    domain_of:
    - Annotation
    range: Flag
    inlined: true
    inlined_as_list: true
class_uri: odm:Annotation

```
</details>