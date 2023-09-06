# Class: StudyStructure

_The StudyStructure element describes the general structure of a clinical study with arms, epochs, and workflows._




URI: [odm:StudyStructure](http://www.cdisc.org/ns/odm/v2.0/StudyStructure)


```mermaid
erDiagram
StudyStructure {

}
WorkflowRef {
    oidref workflowOID  
}
Epoch {
    oid oID  
    nameType name  
    positiveInteger sequenceNumber  
}
Description {

}
Arm {
    oid oID  
    nameType name  
}

StudyStructure ||--|o Description : "description"
StudyStructure ||--}o Arm : "arm"
StudyStructure ||--}o Epoch : "epoch"
StudyStructure ||--|o WorkflowRef : "workflowRef"
Epoch ||--|o Description : "description"
Description ||--}o TranslatedText : "translatedText"
Arm ||--|o Description : "description"
Arm ||--|o WorkflowRef : "workflowRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [arm](arm.md) | 0..* <br/> [Arm](Arm.md) | Arm reference: An Arm element provides the declaration of a study arm. Arms d... | direct |
| [epoch](epoch.md) | 0..* <br/> [Epoch](Epoch.md) | Epoch reference: The planned period of subjects' participation in the trial i... | direct |
| [workflowRef](workflowRef.md) | 0..1 <br/> [WorkflowRef](WorkflowRef.md) | WorkflowRef reference: The WorkflowRef references a workflow definition | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [studyStructure](studyStructure.md) | range | [StudyStructure](StudyStructure.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyStructure](https://wiki.cdisc.org/display/PUB/StudyStructure)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyStructure |
| native | odm:StudyStructure |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyStructure
description: The StudyStructure element describes the general structure of a clinical
  study with arms, epochs, and workflows.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyStructure
rank: 1000
slots:
- description
- arm
- epoch
- workflowRef
slot_usage:
  description:
    name: description
    domain_of:
    - Study
    - MetaDataVersion
    - ValueListDef
    - StudyEventGroupRef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - CommentDef
    - Protocol
    - StudyStructure
    - TrialPhase
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - IntercurrentEvent
    - SummaryMeasure
    - Arm
    - Epoch
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Criterion
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  arm:
    name: arm
    multivalued: true
    domain_of:
    - StudyStructure
    range: Arm
    inlined: true
    inlined_as_list: true
  epoch:
    name: epoch
    multivalued: true
    domain_of:
    - StudyStructure
    range: Epoch
    inlined: true
    inlined_as_list: true
  workflowRef:
    name: workflowRef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    range: WorkflowRef
    maximum_cardinality: 1
class_uri: odm:StudyStructure

```
</details>

### Induced

<details>
```yaml
name: StudyStructure
description: The StudyStructure element describes the general structure of a clinical
  study with arms, epochs, and workflows.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyStructure
rank: 1000
slot_usage:
  description:
    name: description
    domain_of:
    - Study
    - MetaDataVersion
    - ValueListDef
    - StudyEventGroupRef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - CommentDef
    - Protocol
    - StudyStructure
    - TrialPhase
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - IntercurrentEvent
    - SummaryMeasure
    - Arm
    - Epoch
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Criterion
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  arm:
    name: arm
    multivalued: true
    domain_of:
    - StudyStructure
    range: Arm
    inlined: true
    inlined_as_list: true
  epoch:
    name: epoch
    multivalued: true
    domain_of:
    - StudyStructure
    range: Epoch
    inlined: true
    inlined_as_list: true
  workflowRef:
    name: workflowRef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    range: WorkflowRef
    maximum_cardinality: 1
attributes:
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: description
    owner: StudyStructure
    domain_of:
    - Study
    - MetaDataVersion
    - ValueListDef
    - StudyEventGroupRef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - CommentDef
    - Protocol
    - StudyStructure
    - TrialPhase
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - IntercurrentEvent
    - SummaryMeasure
    - Arm
    - Epoch
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Criterion
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  arm:
    name: arm
    description: 'Arm reference: An Arm element provides the declaration of a study
      arm. Arms do not have any ordering relative to one another.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: arm
    owner: StudyStructure
    domain_of:
    - StudyStructure
    range: Arm
    inlined: true
    inlined_as_list: true
  epoch:
    name: epoch
    description: 'Epoch reference: The planned period of subjects'' participation
      in the trial is divided into sequential epochs. Each epoch is a period of time
      that serves a purpose in the trial as a whole. Epochs cannot overlap. The sequence
      of the epoch in the study is provided by the SequenceNumber attribute, the first
      epoch in the study being assigned the sequence number 1. Sequence numbers are
      subsequent.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: epoch
    owner: StudyStructure
    domain_of:
    - StudyStructure
    range: Epoch
    inlined: true
    inlined_as_list: true
  workflowRef:
    name: workflowRef
    description: 'WorkflowRef reference: The WorkflowRef references a workflow definition'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: workflowRef
    owner: StudyStructure
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    range: WorkflowRef
    maximum_cardinality: 1
class_uri: odm:StudyStructure

```
</details>