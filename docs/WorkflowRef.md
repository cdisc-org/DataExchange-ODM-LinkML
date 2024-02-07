# Class: WorkflowRef

_The WorkflowRef references a workflow definition_




URI: [odm:WorkflowRef](http://www.cdisc.org/ns/odm/v2.0/WorkflowRef)


```mermaid
erDiagram
WorkflowRef {

}
WorkflowDef {
    oid OID  
    nameType name  
}
Branching {
    oid OID  
    nameType name  
    BranchingType type  
}
Transition {
    oid OID  
    nameType name  
    string sourceOID  
    string targetOID  
}
WorkflowEnd {
    string endOID  
    text content  
}
WorkflowStart {
    string startOID  
}
Description {

}

WorkflowRef ||--|| WorkflowDef : "workflowOID"
WorkflowDef ||--|o Description : "description"
WorkflowDef ||--|o WorkflowStart : "workflowStart"
WorkflowDef ||--}o WorkflowEnd : "workflowEnd"
WorkflowDef ||--}o Transition : "transition"
WorkflowDef ||--}o Branching : "branching"
Branching ||--}o TargetTransition : "targetTransition"
Branching ||--}o DefaultTransition : "defaultTransition"
Transition ||--|o ConditionDef : "startConditionOID"
Transition ||--|o ConditionDef : "endConditionOID"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [workflowOID](workflowOID.md) | 1..1 <br/> [WorkflowDef](WorkflowDef.md) | Reference to a WorkflowDef | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEventGroupDef](StudyEventGroupDef.md) | [workflowRef](workflowRef.md) | range | [WorkflowRef](WorkflowRef.md) |
| [StudyEventDef](StudyEventDef.md) | [workflowRef](workflowRef.md) | range | [WorkflowRef](WorkflowRef.md) |
| [ItemGroupDef](ItemGroupDef.md) | [workflowRef](workflowRef.md) | range | [WorkflowRef](WorkflowRef.md) |
| [Protocol](Protocol.md) | [workflowRef](workflowRef.md) | range | [WorkflowRef](WorkflowRef.md) |
| [StudyStructure](StudyStructure.md) | [workflowRef](workflowRef.md) | range | [WorkflowRef](WorkflowRef.md) |
| [Arm](Arm.md) | [workflowRef](workflowRef.md) | range | [WorkflowRef](WorkflowRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/WorkflowRef](https://wiki.cdisc.org/display/PUB/WorkflowRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:WorkflowRef |
| native | odm:WorkflowRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkflowRef
description: The WorkflowRef references a workflow definition
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/WorkflowRef
rank: 1000
slots:
- workflowOID
slot_usage:
  workflowOID:
    name: workflowOID
    description: Reference to a WorkflowDef
    comments:
    - 'Required

      range: oidref

      Must match the OID of a WorkflowDef child element of this MetaDataVersion.'
    domain_of:
    - WorkflowRef
    range: WorkflowDef
    required: true
class_uri: odm:WorkflowRef

```
</details>

### Induced

<details>
```yaml
name: WorkflowRef
description: The WorkflowRef references a workflow definition
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/WorkflowRef
rank: 1000
slot_usage:
  workflowOID:
    name: workflowOID
    description: Reference to a WorkflowDef
    comments:
    - 'Required

      range: oidref

      Must match the OID of a WorkflowDef child element of this MetaDataVersion.'
    domain_of:
    - WorkflowRef
    range: WorkflowDef
    required: true
attributes:
  workflowOID:
    name: workflowOID
    description: Reference to a WorkflowDef
    comments:
    - 'Required

      range: oidref

      Must match the OID of a WorkflowDef child element of this MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: workflowOID
    owner: WorkflowRef
    domain_of:
    - WorkflowRef
    range: WorkflowDef
    required: true
class_uri: odm:WorkflowRef

```
</details>