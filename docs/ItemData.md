# Class: ItemData



URI: [odm:ItemData](http://www.cdisc.org/ns/odm/v2.0/ItemData)



```mermaid
 classDiagram
    class ItemData
      ItemData : IsNull
        
          ItemData --|> YesOnly : IsNull
        
      ItemData : ItemOID
        
      ItemData : QueryRef
        
          ItemData --|> Query : QueryRef
        
      ItemData : TransactionType
        
          ItemData --|> TransactionType : TransactionType
        
      ItemData : ValueRef
        
          ItemData --|> Value : ValueRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ItemOID](ItemOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |
| [TransactionType](TransactionType.md) | 0..1 <br/> [TransactionType](TransactionType.md) |  | direct |
| [IsNull](IsNull.md) | 0..1 <br/> [YesOnly](YesOnly.md) |  | direct |
| [ValueRef](ValueRef.md) | 0..* <br/> [Value](Value.md) |  | direct |
| [QueryRef](QueryRef.md) | 0..* <br/> [Query](Query.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemData |
| native | odm:ItemData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemData
in_subset:
- ItemGroupDataGroup
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- ItemOID
- TransactionType
- IsNull
- ValueRef
- QueryRef
slot_usage:
  ItemOID:
    name: ItemOID
    domain_of:
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    - ItemRef
    range: oidref
    required: true
  TransactionType:
    name: TransactionType
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
    required: false
  IsNull:
    name: IsNull
    domain_of:
    - ItemData
    range: YesOnly
    required: false
  ValueRef:
    name: ValueRef
    multivalued: true
    domain_of:
    - ItemData
    - Query
    range: Value
    required: false
    minimum_cardinality: 0
  QueryRef:
    name: QueryRef
    multivalued: true
    domain_of:
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Location
    range: Query
    required: false
    minimum_cardinality: 0
class_uri: odm:ItemData

```
</details>

### Induced

<details>
```yaml
name: ItemData
in_subset:
- ItemGroupDataGroup
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  ItemOID:
    name: ItemOID
    domain_of:
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    - ItemRef
    range: oidref
    required: true
  TransactionType:
    name: TransactionType
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
    required: false
  IsNull:
    name: IsNull
    domain_of:
    - ItemData
    range: YesOnly
    required: false
  ValueRef:
    name: ValueRef
    multivalued: true
    domain_of:
    - ItemData
    - Query
    range: Value
    required: false
    minimum_cardinality: 0
  QueryRef:
    name: QueryRef
    multivalued: true
    domain_of:
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Location
    range: Query
    required: false
    minimum_cardinality: 0
attributes:
  ItemOID:
    name: ItemOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemOID
    owner: ItemData
    domain_of:
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    - ItemRef
    range: oidref
    required: true
  TransactionType:
    name: TransactionType
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: TransactionType
    owner: ItemData
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
    required: false
  IsNull:
    name: IsNull
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: IsNull
    owner: ItemData
    domain_of:
    - ItemData
    range: YesOnly
    required: false
  ValueRef:
    name: ValueRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: ValueRef
    owner: ItemData
    domain_of:
    - ItemData
    - Query
    range: Value
    required: false
    minimum_cardinality: 0
  QueryRef:
    name: QueryRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: QueryRef
    owner: ItemData
    domain_of:
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Location
    range: Query
    required: false
    minimum_cardinality: 0
class_uri: odm:ItemData

```
</details>