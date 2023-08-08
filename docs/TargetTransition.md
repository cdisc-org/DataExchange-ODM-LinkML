# Class: TargetTransition



URI: [odm:TargetTransition](http://www.cdisc.org/ns/odm/v2.0/TargetTransition)



```mermaid
 classDiagram
    class TargetTransition
      TargetTransition : ConditionOID
        
      TargetTransition : TargetTransitionOID
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [TargetTransitionOID](TargetTransitionOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |
| [ConditionOID](ConditionOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Branching](Branching.md) | [TargetTransitionRef](TargetTransitionRef.md) | range | [TargetTransition](TargetTransition.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:TargetTransition |
| native | odm:TargetTransition |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TargetTransition
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- TargetTransitionOID
- ConditionOID
slot_usage:
  TargetTransitionOID:
    name: TargetTransitionOID
    domain_of:
    - TargetTransition
    - DefaultTransition
    range: oidref
    required: true
  ConditionOID:
    name: ConditionOID
    domain_of:
    - TargetTransition
    - Criterion
    - ExceptionEvent
    range: oidref
    required: false
class_uri: odm:TargetTransition

```
</details>

### Induced

<details>
```yaml
name: TargetTransition
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  TargetTransitionOID:
    name: TargetTransitionOID
    domain_of:
    - TargetTransition
    - DefaultTransition
    range: oidref
    required: true
  ConditionOID:
    name: ConditionOID
    domain_of:
    - TargetTransition
    - Criterion
    - ExceptionEvent
    range: oidref
    required: false
attributes:
  TargetTransitionOID:
    name: TargetTransitionOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: TargetTransitionOID
    owner: TargetTransition
    domain_of:
    - TargetTransition
    - DefaultTransition
    range: oidref
    required: true
  ConditionOID:
    name: ConditionOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ConditionOID
    owner: TargetTransition
    domain_of:
    - TargetTransition
    - Criterion
    - ExceptionEvent
    range: oidref
    required: false
class_uri: odm:TargetTransition

```
</details>