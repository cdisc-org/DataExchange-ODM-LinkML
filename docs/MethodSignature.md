# Class: MethodSignature



URI: [odm:MethodSignature](http://www.cdisc.org/ns/odm/v2.0/MethodSignature)



```mermaid
 classDiagram
    class MethodSignature
      MethodSignature : ParameterRef
        
          MethodSignature --|> Parameter : ParameterRef
        
      MethodSignature : ReturnValueRef
        
          MethodSignature --|> ReturnValue : ReturnValueRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ParameterRef](ParameterRef.md) | 0..* <br/> [Parameter](Parameter.md) |  | direct |
| [ReturnValueRef](ReturnValueRef.md) | 0..* <br/> [ReturnValue](ReturnValue.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ConditionDef](ConditionDef.md) | [MethodSignatureRef](MethodSignatureRef.md) | range | [MethodSignature](MethodSignature.md) |
| [MethodDef](MethodDef.md) | [MethodSignatureRef](MethodSignatureRef.md) | range | [MethodSignature](MethodSignature.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:MethodSignature |
| native | odm:MethodSignature |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MethodSignature
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- ParameterRef
- ReturnValueRef
slot_usage:
  ParameterRef:
    name: ParameterRef
    multivalued: true
    domain_of:
    - MethodSignature
    range: Parameter
    required: false
    minimum_cardinality: 0
  ReturnValueRef:
    name: ReturnValueRef
    multivalued: true
    domain_of:
    - MethodSignature
    range: ReturnValue
    required: false
    minimum_cardinality: 0
class_uri: odm:MethodSignature

```
</details>

### Induced

<details>
```yaml
name: MethodSignature
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  ParameterRef:
    name: ParameterRef
    multivalued: true
    domain_of:
    - MethodSignature
    range: Parameter
    required: false
    minimum_cardinality: 0
  ReturnValueRef:
    name: ReturnValueRef
    multivalued: true
    domain_of:
    - MethodSignature
    range: ReturnValue
    required: false
    minimum_cardinality: 0
attributes:
  ParameterRef:
    name: ParameterRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: ParameterRef
    owner: MethodSignature
    domain_of:
    - MethodSignature
    range: Parameter
    required: false
    minimum_cardinality: 0
  ReturnValueRef:
    name: ReturnValueRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: ReturnValueRef
    owner: MethodSignature
    domain_of:
    - MethodSignature
    range: ReturnValue
    required: false
    minimum_cardinality: 0
class_uri: odm:MethodSignature

```
</details>