# Class: RangeCheck



URI: [odm:RangeCheck](http://www.cdisc.org/ns/odm/v2.0/RangeCheck)



```mermaid
 classDiagram
    class RangeCheck
      RangeCheck : CheckValueRef
        
          RangeCheck --|> CheckValue : CheckValueRef
        
      RangeCheck : ComparatorRef
        
          RangeCheck --|> Comparator : ComparatorRef
        
      RangeCheck : ErrorMessageRef
        
          RangeCheck --|> ErrorMessage : ErrorMessageRef
        
      RangeCheck : FormalExpressionRef
        
          RangeCheck --|> FormalExpression : FormalExpressionRef
        
      RangeCheck : ItemOID
        
      RangeCheck : MethodSignatureRef
        
          RangeCheck --|> MethodSignature : MethodSignatureRef
        
      RangeCheck : SoftHard
        
          RangeCheck --|> SoftOrHard : SoftHard
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ComparatorRef](ComparatorRef.md) | 0..1 <br/> [Comparator](Comparator.md) |  | direct |
| [SoftHard](SoftHard.md) | 0..1 <br/> [SoftOrHard](SoftOrHard.md) |  | direct |
| [ItemOID](ItemOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [ErrorMessageRef](ErrorMessageRef.md) | 0..1 <br/> [ErrorMessage](ErrorMessage.md) |  | direct |
| [MethodSignatureRef](MethodSignatureRef.md) | 0..1 <br/> [MethodSignature](MethodSignature.md) |  | direct |
| [FormalExpressionRef](FormalExpressionRef.md) | 0..* <br/> [FormalExpression](FormalExpression.md) |  | direct |
| [CheckValueRef](CheckValueRef.md) | 1..* <br/> [CheckValue](CheckValue.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WhereClauseDef](WhereClauseDef.md) | [RangeCheckRef](RangeCheckRef.md) | range | [RangeCheck](RangeCheck.md) |
| [ItemDef](ItemDef.md) | [RangeCheckRef](RangeCheckRef.md) | range | [RangeCheck](RangeCheck.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/RangeCheck](https://wiki.cdisc.org/display/ODM2/RangeCheck)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:RangeCheck |
| native | odm:RangeCheck |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RangeCheck
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/RangeCheck
slots:
- ComparatorRef
- SoftHard
- ItemOID
- ErrorMessageRef
- MethodSignatureRef
- FormalExpressionRef
- CheckValueRef
slot_usage:
  ComparatorRef:
    name: ComparatorRef
    domain_of:
    - RangeCheck
    range: Comparator
  SoftHard:
    name: SoftHard
    domain_of:
    - RangeCheck
    range: SoftOrHard
  ItemOID:
    name: ItemOID
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
  ErrorMessageRef:
    name: ErrorMessageRef
    domain_of:
    - RangeCheck
    range: ErrorMessage
    maximum_cardinality: 1
  MethodSignatureRef:
    name: MethodSignatureRef
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    range: MethodSignature
    maximum_cardinality: 1
  FormalExpressionRef:
    name: FormalExpressionRef
    multivalued: true
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    - StudyEndPoint
    - StudyTargetPopulation
    range: FormalExpression
    inlined: true
    inlined_as_list: true
  CheckValueRef:
    name: CheckValueRef
    multivalued: true
    domain_of:
    - RangeCheck
    range: CheckValue
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
class_uri: odm:RangeCheck

```
</details>

### Induced

<details>
```yaml
name: RangeCheck
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/RangeCheck
slot_usage:
  ComparatorRef:
    name: ComparatorRef
    domain_of:
    - RangeCheck
    range: Comparator
  SoftHard:
    name: SoftHard
    domain_of:
    - RangeCheck
    range: SoftOrHard
  ItemOID:
    name: ItemOID
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
  ErrorMessageRef:
    name: ErrorMessageRef
    domain_of:
    - RangeCheck
    range: ErrorMessage
    maximum_cardinality: 1
  MethodSignatureRef:
    name: MethodSignatureRef
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    range: MethodSignature
    maximum_cardinality: 1
  FormalExpressionRef:
    name: FormalExpressionRef
    multivalued: true
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    - StudyEndPoint
    - StudyTargetPopulation
    range: FormalExpression
    inlined: true
    inlined_as_list: true
  CheckValueRef:
    name: CheckValueRef
    multivalued: true
    domain_of:
    - RangeCheck
    range: CheckValue
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
attributes:
  ComparatorRef:
    name: ComparatorRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ComparatorRef
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: Comparator
  SoftHard:
    name: SoftHard
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SoftHard
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: SoftOrHard
  ItemOID:
    name: ItemOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemOID
    owner: RangeCheck
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
  ErrorMessageRef:
    name: ErrorMessageRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ErrorMessageRef
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: ErrorMessage
    maximum_cardinality: 1
  MethodSignatureRef:
    name: MethodSignatureRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: MethodSignatureRef
    owner: RangeCheck
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    range: MethodSignature
    maximum_cardinality: 1
  FormalExpressionRef:
    name: FormalExpressionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: FormalExpressionRef
    owner: RangeCheck
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    - StudyEndPoint
    - StudyTargetPopulation
    range: FormalExpression
    inlined: true
    inlined_as_list: true
  CheckValueRef:
    name: CheckValueRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: CheckValueRef
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: CheckValue
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
class_uri: odm:RangeCheck

```
</details>