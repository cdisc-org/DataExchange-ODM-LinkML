# Class: ItemRef



URI: [odm:ItemRef](http://www.cdisc.org/ns/odm/v2.0/ItemRef)



```mermaid
 classDiagram
    class ItemRef
      ItemRef : CollectionExceptionConditionOID
        
      ItemRef : Core
        
      ItemRef : HasNoData
        
          ItemRef --|> YesOnly : HasNoData
        
      ItemRef : IsNonStandard
        
          ItemRef --|> YesOnly : IsNonStandard
        
      ItemRef : ItemOID
        
      ItemRef : KeySequence
        
      ItemRef : Mandatory
        
          ItemRef --|> YesOrNo : Mandatory
        
      ItemRef : MethodOID
        
      ItemRef : OrderNumber
        
      ItemRef : OriginRef
        
          ItemRef --|> Origin : OriginRef
        
      ItemRef : Other
        
          ItemRef --|> YesOnly : Other
        
      ItemRef : PreSpecifiedValue
        
      ItemRef : Repeat
        
          ItemRef --|> YesOnly : Repeat
        
      ItemRef : Role
        
      ItemRef : RoleCodeListOID
        
      ItemRef : UnitsItemOID
        
      ItemRef : WhereClauseRefRef
        
          ItemRef --|> WhereClauseRef : WhereClauseRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ItemOID](ItemOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |
| [KeySequence](KeySequence.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) |  | direct |
| [IsNonStandard](IsNonStandard.md) | 0..1 <br/> [YesOnly](YesOnly.md) |  | direct |
| [HasNoData](HasNoData.md) | 0..1 <br/> [YesOnly](YesOnly.md) |  | direct |
| [MethodOID](MethodOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [UnitsItemOID](UnitsItemOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [Repeat](Repeat.md) | 0..1 <br/> [YesOnly](YesOnly.md) |  | direct |
| [Other](Other.md) | 0..1 <br/> [YesOnly](YesOnly.md) |  | direct |
| [Role](Role.md) | 0..1 <br/> [Text](Text.md) |  | direct |
| [RoleCodeListOID](RoleCodeListOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [Core](Core.md) | 0..1 <br/> [CoreType](CoreType.md) |  | direct |
| [PreSpecifiedValue](PreSpecifiedValue.md) | 0..1 <br/> [Text](Text.md) |  | direct |
| [OrderNumber](OrderNumber.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) |  | direct |
| [Mandatory](Mandatory.md) | 1..1 <br/> [YesOrNo](YesOrNo.md) |  | direct |
| [CollectionExceptionConditionOID](CollectionExceptionConditionOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [OriginRef](OriginRef.md) | 0..* <br/> [Origin](Origin.md) |  | direct |
| [WhereClauseRefRef](WhereClauseRefRef.md) | 0..* <br/> [WhereClauseRef](WhereClauseRef.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ValueListDef](ValueListDef.md) | [ItemRefRef](ItemRefRef.md) | range | [ItemRef](ItemRef.md) |
| [ItemGroupDef](ItemGroupDef.md) | [ItemRefRef](ItemRefRef.md) | range | [ItemRef](ItemRef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/ItemRef](https://wiki.cdisc.org/display/ODM2/ItemRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemRef |
| native | odm:ItemRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemRef
slots:
- ItemOID
- KeySequence
- IsNonStandard
- HasNoData
- MethodOID
- UnitsItemOID
- Repeat
- Other
- Role
- RoleCodeListOID
- Core
- PreSpecifiedValue
- OrderNumber
- Mandatory
- CollectionExceptionConditionOID
- OriginRef
- WhereClauseRefRef
slot_usage:
  ItemOID:
    name: ItemOID
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
    required: true
  KeySequence:
    name: KeySequence
    domain_of:
    - ItemRef
    range: positiveInteger
  IsNonStandard:
    name: IsNonStandard
    domain_of:
    - ItemGroupDef
    - ItemRef
    - CodeList
    range: YesOnly
  HasNoData:
    name: HasNoData
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: YesOnly
  MethodOID:
    name: MethodOID
    domain_of:
    - ItemGroupRef
    - ItemRef
    - TransitionTimingConstraint
    range: oidref
  UnitsItemOID:
    name: UnitsItemOID
    domain_of:
    - ItemRef
    range: oidref
  Repeat:
    name: Repeat
    domain_of:
    - ItemRef
    range: YesOnly
  Other:
    name: Other
    domain_of:
    - ItemRef
    - CodeListItem
    range: YesOnly
  Role:
    name: Role
    domain_of:
    - ItemRef
    - Organization
    - Location
    range: text
  RoleCodeListOID:
    name: RoleCodeListOID
    domain_of:
    - ItemRef
    range: oidref
  Core:
    name: Core
    domain_of:
    - ItemRef
    range: CoreType
  PreSpecifiedValue:
    name: PreSpecifiedValue
    domain_of:
    - ItemRef
    range: text
  OrderNumber:
    name: OrderNumber
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
  Mandatory:
    name: Mandatory
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: YesOrNo
    required: true
  CollectionExceptionConditionOID:
    name: CollectionExceptionConditionOID
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: oidref
  OriginRef:
    name: OriginRef
    multivalued: true
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: Origin
    inlined: true
    inlined_as_list: true
  WhereClauseRefRef:
    name: WhereClauseRefRef
    multivalued: true
    domain_of:
    - ItemRef
    range: WhereClauseRef
    inlined: true
    inlined_as_list: true
class_uri: odm:ItemRef

```
</details>

### Induced

<details>
```yaml
name: ItemRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemRef
slot_usage:
  ItemOID:
    name: ItemOID
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
    required: true
  KeySequence:
    name: KeySequence
    domain_of:
    - ItemRef
    range: positiveInteger
  IsNonStandard:
    name: IsNonStandard
    domain_of:
    - ItemGroupDef
    - ItemRef
    - CodeList
    range: YesOnly
  HasNoData:
    name: HasNoData
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: YesOnly
  MethodOID:
    name: MethodOID
    domain_of:
    - ItemGroupRef
    - ItemRef
    - TransitionTimingConstraint
    range: oidref
  UnitsItemOID:
    name: UnitsItemOID
    domain_of:
    - ItemRef
    range: oidref
  Repeat:
    name: Repeat
    domain_of:
    - ItemRef
    range: YesOnly
  Other:
    name: Other
    domain_of:
    - ItemRef
    - CodeListItem
    range: YesOnly
  Role:
    name: Role
    domain_of:
    - ItemRef
    - Organization
    - Location
    range: text
  RoleCodeListOID:
    name: RoleCodeListOID
    domain_of:
    - ItemRef
    range: oidref
  Core:
    name: Core
    domain_of:
    - ItemRef
    range: CoreType
  PreSpecifiedValue:
    name: PreSpecifiedValue
    domain_of:
    - ItemRef
    range: text
  OrderNumber:
    name: OrderNumber
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
  Mandatory:
    name: Mandatory
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: YesOrNo
    required: true
  CollectionExceptionConditionOID:
    name: CollectionExceptionConditionOID
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: oidref
  OriginRef:
    name: OriginRef
    multivalued: true
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: Origin
    inlined: true
    inlined_as_list: true
  WhereClauseRefRef:
    name: WhereClauseRefRef
    multivalued: true
    domain_of:
    - ItemRef
    range: WhereClauseRef
    inlined: true
    inlined_as_list: true
attributes:
  ItemOID:
    name: ItemOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemOID
    owner: ItemRef
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
    required: true
  KeySequence:
    name: KeySequence
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: KeySequence
    owner: ItemRef
    domain_of:
    - ItemRef
    range: positiveInteger
  IsNonStandard:
    name: IsNonStandard
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: IsNonStandard
    owner: ItemRef
    domain_of:
    - ItemGroupDef
    - ItemRef
    - CodeList
    range: YesOnly
  HasNoData:
    name: HasNoData
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: HasNoData
    owner: ItemRef
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: YesOnly
  MethodOID:
    name: MethodOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: MethodOID
    owner: ItemRef
    domain_of:
    - ItemGroupRef
    - ItemRef
    - TransitionTimingConstraint
    range: oidref
  UnitsItemOID:
    name: UnitsItemOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: UnitsItemOID
    owner: ItemRef
    domain_of:
    - ItemRef
    range: oidref
  Repeat:
    name: Repeat
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Repeat
    owner: ItemRef
    domain_of:
    - ItemRef
    range: YesOnly
  Other:
    name: Other
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Other
    owner: ItemRef
    domain_of:
    - ItemRef
    - CodeListItem
    range: YesOnly
  Role:
    name: Role
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Role
    owner: ItemRef
    domain_of:
    - ItemRef
    - Organization
    - Location
    range: text
  RoleCodeListOID:
    name: RoleCodeListOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: RoleCodeListOID
    owner: ItemRef
    domain_of:
    - ItemRef
    range: oidref
  Core:
    name: Core
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Core
    owner: ItemRef
    domain_of:
    - ItemRef
    range: CoreType
  PreSpecifiedValue:
    name: PreSpecifiedValue
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: PreSpecifiedValue
    owner: ItemRef
    domain_of:
    - ItemRef
    range: text
  OrderNumber:
    name: OrderNumber
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: OrderNumber
    owner: ItemRef
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
  Mandatory:
    name: Mandatory
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Mandatory
    owner: ItemRef
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: YesOrNo
    required: true
  CollectionExceptionConditionOID:
    name: CollectionExceptionConditionOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CollectionExceptionConditionOID
    owner: ItemRef
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: oidref
  OriginRef:
    name: OriginRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: OriginRef
    owner: ItemRef
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: Origin
    inlined: true
    inlined_as_list: true
  WhereClauseRefRef:
    name: WhereClauseRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: WhereClauseRefRef
    owner: ItemRef
    domain_of:
    - ItemRef
    range: WhereClauseRef
    inlined: true
    inlined_as_list: true
class_uri: odm:ItemRef

```
</details>