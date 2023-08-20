# Class: ItemGroupData


_Clinical data corresponding to an ItemGroupRef defined in the active MetaDataVersion. _





URI: [odm:ItemGroupData](http://www.cdisc.org/ns/odm/v2.0/ItemGroupData)



```mermaid
 classDiagram
    class ItemGroupData
      ItemGroupData : AnnotationRef
        
          ItemGroupData --|> Annotation : AnnotationRef
        
      ItemGroupData : AuditRecordRef
        
          ItemGroupData --|> AuditRecord : AuditRecordRef
        
      ItemGroupData : ItemDataRef
        
          ItemGroupData --|> ItemData : ItemDataRef
        
      ItemGroupData : ItemGroupDataRef
        
          ItemGroupData --|> ItemGroupData : ItemGroupDataRef
        
      ItemGroupData : ItemGroupDataSeq
        
      ItemGroupData : ItemGroupOID
        
      ItemGroupData : ItemGroupRepeatKey
        
      ItemGroupData : QueryRef
        
          ItemGroupData --|> Query : QueryRef
        
      ItemGroupData : SignatureRefRef
        
          ItemGroupData --|> Signature : SignatureRefRef
        
      ItemGroupData : TransactionTypeRef
        
          ItemGroupData --|> TransactionType : TransactionTypeRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ItemGroupOID](ItemGroupOID.md) | 1..1 <br/> [Oidref](Oidref.md) | Reference to an ItemGroupDef for the MetaDataVersion identified in the Clinic... | direct |
| [ItemGroupRepeatKey](ItemGroupRepeatKey.md) | 0..1 <br/> [RepeatKey](RepeatKey.md) | A key used to distinguish between repeats of the same type of item group | direct |
| [TransactionTypeRef](TransactionTypeRef.md) | 0..1 <br/> [TransactionType](TransactionType.md) | The TransactionType attribute need not be present in a Snapshot document | direct |
| [ItemGroupDataSeq](ItemGroupDataSeq.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) | Unique sequence # for each ItemGroupData child element (record) in the contai... | direct |
| [QueryRef](QueryRef.md) | 0..* <br/> [Query](Query.md) |  | direct |
| [ItemGroupDataRef](ItemGroupDataRef.md) | 0..* <br/> [ItemGroupData](ItemGroupData.md) |  | direct |
| [ItemDataRef](ItemDataRef.md) | 0..* <br/> [ItemData](ItemData.md) |  | direct |
| [AuditRecordRef](AuditRecordRef.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) |  | direct |
| [SignatureRefRef](SignatureRefRef.md) | 0..1 <br/> [Signature](Signature.md) |  | direct |
| [AnnotationRef](AnnotationRef.md) | 0..1 <br/> [Annotation](Annotation.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReferenceData](ReferenceData.md) | [ItemGroupDataRef](ItemGroupDataRef.md) | range | [ItemGroupData](ItemGroupData.md) |
| [ClinicalData](ClinicalData.md) | [ItemGroupDataRef](ItemGroupDataRef.md) | range | [ItemGroupData](ItemGroupData.md) |
| [StudyEventData](StudyEventData.md) | [ItemGroupDataRef](ItemGroupDataRef.md) | range | [ItemGroupData](ItemGroupData.md) |
| [ItemGroupData](ItemGroupData.md) | [ItemGroupDataRef](ItemGroupDataRef.md) | range | [ItemGroupData](ItemGroupData.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/ItemGroupData](https://wiki.cdisc.org/display/ODM2/ItemGroupData)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemGroupData |
| native | odm:ItemGroupData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemGroupData
description: 'Clinical data corresponding to an ItemGroupRef defined in the active
  MetaDataVersion. '
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemGroupData
slots:
- ItemGroupOID
- ItemGroupRepeatKey
- TransactionTypeRef
- ItemGroupDataSeq
- QueryRef
- ItemGroupDataRef
- ItemDataRef
- AuditRecordRef
- SignatureRefRef
- AnnotationRef
slot_usage:
  ItemGroupOID:
    name: ItemGroupOID
    description: Reference to an ItemGroupDef for the MetaDataVersion identified in
      the ClinicalData element.
    comments:
    - 'Required

      The values of ItemGroupOID must be unique within the parent element.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: oidref
    required: true
  ItemGroupRepeatKey:
    name: ItemGroupRepeatKey
    description: A key used to distinguish between repeats of the same type of item
      group.
    comments:
    - 'Conditional Required when the Repeating attribute for the ItemGroupDef element
      is "Yes" .

      The values of ItemGroupRepeatKey must be unique within the parent element. The
      ItemGroupRepeatKey is present only if the ItemGroupDef is repeating . For /ODM/ReferenceData/ItemGroupData
      , the ItemGroupOID and ItemGroupRepeatKey pair must be unique.'
    domain_of:
    - ItemGroupData
    - KeySet
    range: repeatKey
  TransactionTypeRef:
    name: TransactionTypeRef
    description: The TransactionType attribute need not be present in a Snapshot document.
    comments:
    - Conditional Required when the FileType attribute for the ODM element is Transactional.
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  ItemGroupDataSeq:
    name: ItemGroupDataSeq
    description: 'Unique sequence # for each ItemGroupData child element (record)
      in the container element. The ItemGroupDataSeq attribute doesn’t have any other
      meaning than the sequence in which the items are saved and exchanged for each
      ItemGroupDef. It is equivalent to the observation # in a dataset.'
    comments:
    - 'Conditional Required when the parent element is ReferenceData or ClinicalData,
      the ItemGroupDataSeq.

      ItemGroupDataSeq may only be used when ItemGroupData is a direct child of either
      ClinicalData or ReferenceData and the ItemGroupData represents a row in a dataset.
      The ItemGroupDataSeq and ItemGroupRepeatKey attributes are mutually exclusive.'
    domain_of:
    - ItemGroupData
    range: positiveInteger
  QueryRef:
    name: QueryRef
    multivalued: true
    domain_of:
    - Location
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Query
    inlined: true
    inlined_as_list: true
  ItemGroupDataRef:
    name: ItemGroupDataRef
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  ItemDataRef:
    name: ItemDataRef
    multivalued: true
    domain_of:
    - ItemGroupData
    range: ItemData
    inlined: true
    inlined_as_list: true
  AuditRecordRef:
    name: AuditRecordRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    maximum_cardinality: 1
  SignatureRefRef:
    name: SignatureRefRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Signature
    range: Signature
    maximum_cardinality: 1
  AnnotationRef:
    name: AnnotationRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Association
    range: Annotation
    maximum_cardinality: 1
class_uri: odm:ItemGroupData

```
</details>

### Induced

<details>
```yaml
name: ItemGroupData
description: 'Clinical data corresponding to an ItemGroupRef defined in the active
  MetaDataVersion. '
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemGroupData
slot_usage:
  ItemGroupOID:
    name: ItemGroupOID
    description: Reference to an ItemGroupDef for the MetaDataVersion identified in
      the ClinicalData element.
    comments:
    - 'Required

      The values of ItemGroupOID must be unique within the parent element.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: oidref
    required: true
  ItemGroupRepeatKey:
    name: ItemGroupRepeatKey
    description: A key used to distinguish between repeats of the same type of item
      group.
    comments:
    - 'Conditional Required when the Repeating attribute for the ItemGroupDef element
      is "Yes" .

      The values of ItemGroupRepeatKey must be unique within the parent element. The
      ItemGroupRepeatKey is present only if the ItemGroupDef is repeating . For /ODM/ReferenceData/ItemGroupData
      , the ItemGroupOID and ItemGroupRepeatKey pair must be unique.'
    domain_of:
    - ItemGroupData
    - KeySet
    range: repeatKey
  TransactionTypeRef:
    name: TransactionTypeRef
    description: The TransactionType attribute need not be present in a Snapshot document.
    comments:
    - Conditional Required when the FileType attribute for the ODM element is Transactional.
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  ItemGroupDataSeq:
    name: ItemGroupDataSeq
    description: 'Unique sequence # for each ItemGroupData child element (record)
      in the container element. The ItemGroupDataSeq attribute doesn’t have any other
      meaning than the sequence in which the items are saved and exchanged for each
      ItemGroupDef. It is equivalent to the observation # in a dataset.'
    comments:
    - 'Conditional Required when the parent element is ReferenceData or ClinicalData,
      the ItemGroupDataSeq.

      ItemGroupDataSeq may only be used when ItemGroupData is a direct child of either
      ClinicalData or ReferenceData and the ItemGroupData represents a row in a dataset.
      The ItemGroupDataSeq and ItemGroupRepeatKey attributes are mutually exclusive.'
    domain_of:
    - ItemGroupData
    range: positiveInteger
  QueryRef:
    name: QueryRef
    multivalued: true
    domain_of:
    - Location
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Query
    inlined: true
    inlined_as_list: true
  ItemGroupDataRef:
    name: ItemGroupDataRef
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  ItemDataRef:
    name: ItemDataRef
    multivalued: true
    domain_of:
    - ItemGroupData
    range: ItemData
    inlined: true
    inlined_as_list: true
  AuditRecordRef:
    name: AuditRecordRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    maximum_cardinality: 1
  SignatureRefRef:
    name: SignatureRefRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Signature
    range: Signature
    maximum_cardinality: 1
  AnnotationRef:
    name: AnnotationRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Association
    range: Annotation
    maximum_cardinality: 1
attributes:
  ItemGroupOID:
    name: ItemGroupOID
    description: Reference to an ItemGroupDef for the MetaDataVersion identified in
      the ClinicalData element.
    comments:
    - 'Required

      The values of ItemGroupOID must be unique within the parent element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemGroupOID
    owner: ItemGroupData
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: oidref
    required: true
  ItemGroupRepeatKey:
    name: ItemGroupRepeatKey
    description: A key used to distinguish between repeats of the same type of item
      group.
    comments:
    - 'Conditional Required when the Repeating attribute for the ItemGroupDef element
      is "Yes" .

      The values of ItemGroupRepeatKey must be unique within the parent element. The
      ItemGroupRepeatKey is present only if the ItemGroupDef is repeating . For /ODM/ReferenceData/ItemGroupData
      , the ItemGroupOID and ItemGroupRepeatKey pair must be unique.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemGroupRepeatKey
    owner: ItemGroupData
    domain_of:
    - ItemGroupData
    - KeySet
    range: repeatKey
  TransactionTypeRef:
    name: TransactionTypeRef
    description: The TransactionType attribute need not be present in a Snapshot document.
    comments:
    - Conditional Required when the FileType attribute for the ODM element is Transactional.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: TransactionTypeRef
    owner: ItemGroupData
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  ItemGroupDataSeq:
    name: ItemGroupDataSeq
    description: 'Unique sequence # for each ItemGroupData child element (record)
      in the container element. The ItemGroupDataSeq attribute doesn’t have any other
      meaning than the sequence in which the items are saved and exchanged for each
      ItemGroupDef. It is equivalent to the observation # in a dataset.'
    comments:
    - 'Conditional Required when the parent element is ReferenceData or ClinicalData,
      the ItemGroupDataSeq.

      ItemGroupDataSeq may only be used when ItemGroupData is a direct child of either
      ClinicalData or ReferenceData and the ItemGroupData represents a row in a dataset.
      The ItemGroupDataSeq and ItemGroupRepeatKey attributes are mutually exclusive.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemGroupDataSeq
    owner: ItemGroupData
    domain_of:
    - ItemGroupData
    range: positiveInteger
  QueryRef:
    name: QueryRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: QueryRef
    owner: ItemGroupData
    domain_of:
    - Location
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Query
    inlined: true
    inlined_as_list: true
  ItemGroupDataRef:
    name: ItemGroupDataRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemGroupDataRef
    owner: ItemGroupData
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  ItemDataRef:
    name: ItemDataRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemDataRef
    owner: ItemGroupData
    domain_of:
    - ItemGroupData
    range: ItemData
    inlined: true
    inlined_as_list: true
  AuditRecordRef:
    name: AuditRecordRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: AuditRecordRef
    owner: ItemGroupData
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    maximum_cardinality: 1
  SignatureRefRef:
    name: SignatureRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SignatureRefRef
    owner: ItemGroupData
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Signature
    range: Signature
    maximum_cardinality: 1
  AnnotationRef:
    name: AnnotationRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: AnnotationRef
    owner: ItemGroupData
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Association
    range: Annotation
    maximum_cardinality: 1
class_uri: odm:ItemGroupData

```
</details>