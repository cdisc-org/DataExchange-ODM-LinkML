# Class: TargetTransition

_TargetTransition provides a reference to a Transition element that is the target of a branching._




URI: [odm:TargetTransition](http://www.cdisc.org/ns/odm/v2.0/TargetTransition)


```mermaid
erDiagram
TargetTransition {

}
ConditionDef {
    oid OID  
    nameType name  
}
Alias {
    text context  
    text name  
}
FormalExpression {
    text context  
}
MethodSignature {

}
Description {

}
CommentDef {
    oid OID  
}
Transition {
    oid OID  
    nameType name  
    string sourceOID  
    string targetOID  
}

TargetTransition ||--|| Transition : "targetTransitionOID"
TargetTransition ||--|o ConditionDef : "conditionOID"
ConditionDef ||--|o CommentDef : "commentOID"
ConditionDef ||--|o Description : "description"
ConditionDef ||--|o MethodSignature : "methodSignature"
ConditionDef ||--}o FormalExpression : "formalExpression"
ConditionDef ||--}o Alias : "alias"
FormalExpression ||--|o Code : "code"
FormalExpression ||--|o ExternalCodeLib : "externalCodeLib"
MethodSignature ||--}o Parameter : "parameter"
MethodSignature ||--}o ReturnValue : "returnValue"
Description ||--}o TranslatedText : "translatedText"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"
Transition ||--|o ConditionDef : "startConditionOID"
Transition ||--|o ConditionDef : "endConditionOID"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [targetTransitionOID](targetTransitionOID.md) | 1..1 <br/> [Transition](Transition.md) | Reference to the Transition that is one of the targets of the branching. | direct |
| [conditionOID](conditionOID.md) | 0..1 <br/> [ConditionDef](ConditionDef.md) | Reference to a ConditionDef defining the condition under which the transition... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Branching](Branching.md) | [targetTransition](targetTransition.md) | range | [TargetTransition](TargetTransition.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/TargetTransition](https://wiki.cdisc.org/display/PUB/TargetTransition)

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
description: TargetTransition provides a reference to a Transition element that is
  the target of a branching.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/TargetTransition
rank: 1000
slots:
- targetTransitionOID
- conditionOID
slot_usage:
  targetTransitionOID:
    name: targetTransitionOID
    description: Reference to the Transition that is one of the targets of the branching.
    comments:
    - 'Required

      range: oidref

      The TargetTransitionOID attibute must match the OID attribute of a Transition
      element in the Study/MetaDataVersion.'
    domain_of:
    - TargetTransition
    - DefaultTransition
    range: Transition
    required: true
  conditionOID:
    name: conditionOID
    description: Reference to a ConditionDef defining the condition under which the
      transition must be executed. The ConditionOID references a ConditionDef element
      defining a condition that needs to be evaluated at the time of entering the
      branching state. When the condition evaluates to true, the branch is entered.
    comments:
    - 'Required

      range: oidref

      The ConditionOID must match the OID attribute of a ConditionDef element in the
      Study/MetaDataVersion.'
    domain_of:
    - TargetTransition
    - Criterion
    range: ConditionDef
class_uri: odm:TargetTransition

```
</details>

### Induced

<details>
```yaml
name: TargetTransition
description: TargetTransition provides a reference to a Transition element that is
  the target of a branching.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/TargetTransition
rank: 1000
slot_usage:
  targetTransitionOID:
    name: targetTransitionOID
    description: Reference to the Transition that is one of the targets of the branching.
    comments:
    - 'Required

      range: oidref

      The TargetTransitionOID attibute must match the OID attribute of a Transition
      element in the Study/MetaDataVersion.'
    domain_of:
    - TargetTransition
    - DefaultTransition
    range: Transition
    required: true
  conditionOID:
    name: conditionOID
    description: Reference to a ConditionDef defining the condition under which the
      transition must be executed. The ConditionOID references a ConditionDef element
      defining a condition that needs to be evaluated at the time of entering the
      branching state. When the condition evaluates to true, the branch is entered.
    comments:
    - 'Required

      range: oidref

      The ConditionOID must match the OID attribute of a ConditionDef element in the
      Study/MetaDataVersion.'
    domain_of:
    - TargetTransition
    - Criterion
    range: ConditionDef
attributes:
  targetTransitionOID:
    name: targetTransitionOID
    description: Reference to the Transition that is one of the targets of the branching.
    comments:
    - 'Required

      range: oidref

      The TargetTransitionOID attibute must match the OID attribute of a Transition
      element in the Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: targetTransitionOID
    owner: TargetTransition
    domain_of:
    - TargetTransition
    - DefaultTransition
    range: Transition
    required: true
  conditionOID:
    name: conditionOID
    description: Reference to a ConditionDef defining the condition under which the
      transition must be executed. The ConditionOID references a ConditionDef element
      defining a condition that needs to be evaluated at the time of entering the
      branching state. When the condition evaluates to true, the branch is entered.
    comments:
    - 'Required

      range: oidref

      The ConditionOID must match the OID attribute of a ConditionDef element in the
      Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: conditionOID
    owner: TargetTransition
    domain_of:
    - TargetTransition
    - Criterion
    range: ConditionDef
class_uri: odm:TargetTransition

```
</details>