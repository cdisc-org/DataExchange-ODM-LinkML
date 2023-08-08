# Class: ItemGroupRef



URI: [odm:ItemGroupRef](http://www.cdisc.org/ns/odm/v2.0/ItemGroupRef)



```mermaid
 classDiagram
    class ItemGroupRef
      ItemGroupRef : CollectionExceptionConditionOID
        
      ItemGroupRef : ItemGroupOID
        
      ItemGroupRef : Mandatory
        
          ItemGroupRef --|> YesOrNo : Mandatory
        
      ItemGroupRef : MethodOID
        
      ItemGroupRef : OrderNumber
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ItemGroupOID](ItemGroupOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |
| [MethodOID](MethodOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [OrderNumber](OrderNumber.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [Mandatory](Mandatory.md) | 1..1 <br/> [YesOrNo](YesOrNo.md) |  | direct |
| [CollectionExceptionConditionOID](CollectionExceptionConditionOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEventDef](StudyEventDef.md) | [ItemGroupRefRef](ItemGroupRefRef.md) | range | [ItemGroupRef](ItemGroupRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemGroupRef |
| native | odm:ItemGroupRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemGroupRef
in_subset:
- ItemGroupDefGroup
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- ItemGroupOID
- MethodOID
- OrderNumber
- Mandatory
- CollectionExceptionConditionOID
slot_usage:
  ItemGroupOID:
    name: ItemGroupOID
    domain_of:
    - SourceItem
    - ItemGroupData
    - KeySet
    - ItemGroupRef
    range: oidref
    required: true
  MethodOID:
    name: MethodOID
    domain_of:
    - TransitionTimingConstraint
    - ItemRef
    - ItemGroupRef
    range: oidref
    required: false
  OrderNumber:
    name: OrderNumber
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - Parameter
    - ReturnValue
    - StudyEndPointRef
    - ItemRef
    - ItemGroupRef
    - CodeListItem
    - EnumeratedItem
    range: integer
    required: false
  Mandatory:
    name: Mandatory
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemRef
    - ItemGroupRef
    range: YesOrNo
    required: true
  CollectionExceptionConditionOID:
    name: CollectionExceptionConditionOID
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemRef
    - ItemGroupRef
    range: oidref
    required: false
class_uri: odm:ItemGroupRef
unique_keys:
  UC-SED-2:
    unique_key_name: UC-SED-2
    unique_key_slots:
    - OrderNumber

```
</details>

### Induced

<details>
```yaml
name: ItemGroupRef
in_subset:
- ItemGroupDefGroup
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  ItemGroupOID:
    name: ItemGroupOID
    domain_of:
    - SourceItem
    - ItemGroupData
    - KeySet
    - ItemGroupRef
    range: oidref
    required: true
  MethodOID:
    name: MethodOID
    domain_of:
    - TransitionTimingConstraint
    - ItemRef
    - ItemGroupRef
    range: oidref
    required: false
  OrderNumber:
    name: OrderNumber
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - Parameter
    - ReturnValue
    - StudyEndPointRef
    - ItemRef
    - ItemGroupRef
    - CodeListItem
    - EnumeratedItem
    range: integer
    required: false
  Mandatory:
    name: Mandatory
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemRef
    - ItemGroupRef
    range: YesOrNo
    required: true
  CollectionExceptionConditionOID:
    name: CollectionExceptionConditionOID
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemRef
    - ItemGroupRef
    range: oidref
    required: false
attributes:
  ItemGroupOID:
    name: ItemGroupOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemGroupOID
    owner: ItemGroupRef
    domain_of:
    - SourceItem
    - ItemGroupData
    - KeySet
    - ItemGroupRef
    range: oidref
    required: true
  MethodOID:
    name: MethodOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: MethodOID
    owner: ItemGroupRef
    domain_of:
    - TransitionTimingConstraint
    - ItemRef
    - ItemGroupRef
    range: oidref
    required: false
  OrderNumber:
    name: OrderNumber
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: OrderNumber
    owner: ItemGroupRef
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - Parameter
    - ReturnValue
    - StudyEndPointRef
    - ItemRef
    - ItemGroupRef
    - CodeListItem
    - EnumeratedItem
    range: integer
    required: false
  Mandatory:
    name: Mandatory
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Mandatory
    owner: ItemGroupRef
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemRef
    - ItemGroupRef
    range: YesOrNo
    required: true
  CollectionExceptionConditionOID:
    name: CollectionExceptionConditionOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CollectionExceptionConditionOID
    owner: ItemGroupRef
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemRef
    - ItemGroupRef
    range: oidref
    required: false
class_uri: odm:ItemGroupRef
unique_keys:
  UC-SED-2:
    unique_key_name: UC-SED-2
    unique_key_slots:
    - OrderNumber

```
</details>