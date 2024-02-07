# Class: StudyEstimand

_A precise description of the treatment effect reflecting the clinical question posed by a given clinical trial objective. It summarises at a population level what the outcomes would be in the same patients under different treatment conditions being compared._




URI: [odm:StudyEstimand](http://www.cdisc.org/ns/odm/v2.0/StudyEstimand)


```mermaid
erDiagram
StudyEstimand {
    oid OID  
    nameType name  
    StudyEstimandLevel level  
}
SummaryMeasure {

}
Description {

}
IntercurrentEvent {

}
StudyEndPointRef {
    positiveInteger orderNumber  
}
StudyEndPoint {
    oid OID  
    nameType name  
    StudyEndPointType type  
    StudyEstimandLevel level  
}
StudyInterventionRef {

}
StudyIntervention {
    oid OID  
}
StudyTargetPopulationRef {

}
StudyTargetPopulation {
    oid OID  
    nameType name  
}

StudyEstimand ||--|o Description : "description"
StudyEstimand ||--|o StudyTargetPopulationRef : "studyTargetPopulationRef"
StudyEstimand ||--|o StudyInterventionRef : "studyInterventionRef"
StudyEstimand ||--|o StudyEndPointRef : "studyEndPointRef"
StudyEstimand ||--}o IntercurrentEvent : "intercurrentEvent"
StudyEstimand ||--|o SummaryMeasure : "summaryMeasure"
SummaryMeasure ||--|o Description : "description"
Description ||--}o TranslatedText : "translatedText"
IntercurrentEvent ||--|o Description : "description"
StudyEndPointRef ||--|| StudyEndPoint : "studyEndPointOID"
StudyEndPoint ||--|o Description : "description"
StudyEndPoint ||--}o FormalExpression : "formalExpression"
StudyInterventionRef ||--|| StudyIntervention : "studyInterventionOID"
StudyIntervention ||--|o Description : "description"
StudyIntervention ||--}o Coding : "coding"
StudyTargetPopulationRef ||--|| StudyTargetPopulation : "studyTargetPopulationOID"
StudyTargetPopulation ||--|o Description : "description"
StudyTargetPopulation ||--}o Coding : "coding"
StudyTargetPopulation ||--}o FormalExpression : "formalExpression"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier for the StudyEstimand element. | direct |
| [name](name.md) | 1..1 <br/> [nameType](nameType.md) | Human readable name for the Study Estimand. | direct |
| [level](level.md) | 0..1 <br/> [StudyEstimandLevel](StudyEstimandLevel.md) | Defined Level for the Study Estimand | direct |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [studyTargetPopulationRef](studyTargetPopulationRef.md) | 0..1 <br/> [StudyTargetPopulationRef](StudyTargetPopulationRef.md) | StudyTargetPopulationRef reference: The StudyTargetPopulationRef references a... | direct |
| [studyInterventionRef](studyInterventionRef.md) | 0..1 <br/> [StudyInterventionRef](StudyInterventionRef.md) | StudyInterventionRef reference: The StudyInterventionRef references an interv... | direct |
| [studyEndPointRef](studyEndPointRef.md) | 0..1 <br/> [StudyEndPointRef](StudyEndPointRef.md) | StudyEndPointRef reference: A reference to a StudyEndPoint as it occurs withi... | direct |
| [intercurrentEvent](intercurrentEvent.md) | 0..* <br/> [IntercurrentEvent](IntercurrentEvent.md) | IntercurrentEvent reference: The IntercurrentEvent element describes an inter... | direct |
| [summaryMeasure](summaryMeasure.md) | 0..1 <br/> [SummaryMeasure](SummaryMeasure.md) | SummaryMeasure reference: The SummaryMeasure element describes a summary meas... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEstimands](StudyEstimands.md) | [studyEstimand](studyEstimand.md) | range | [StudyEstimand](StudyEstimand.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyEstimand](https://wiki.cdisc.org/display/PUB/StudyEstimand)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyEstimand |
| native | odm:StudyEstimand |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyEstimand
description: A precise description of the treatment effect reflecting the clinical
  question posed by a given clinical trial objective. It summarises at a population
  level what the outcomes would be in the same patients under different treatment
  conditions being compared.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEstimand
rank: 1000
slots:
- OID
- name
- level
- description
- studyTargetPopulationRef
- studyInterventionRef
- studyEndPointRef
- intercurrentEvent
- summaryMeasure
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the StudyEstimand element.
    comments:
    - 'Required

      range: oid'
    identifier: true
    domain_of:
    - Study
    - MetaDataVersion
    - Standard
    - ValueListDef
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - MethodDef
    - ConditionDef
    - CommentDef
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyParameter
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  name:
    name: name
    description: Human readable name for the Study Estimand.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: nameType
    required: true
  level:
    name: level
    description: Defined Level for the Study Estimand
    comments:
    - 'Optional

      enum values: ( Primary | Secondary | Exploratory )'
    domain_of:
    - StudyObjective
    - StudyEndPoint
    - StudyEstimand
    range: StudyEstimandLevel
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
  studyTargetPopulationRef:
    name: studyTargetPopulationRef
    domain_of:
    - StudyEstimand
    range: StudyTargetPopulationRef
    maximum_cardinality: 1
  studyInterventionRef:
    name: studyInterventionRef
    domain_of:
    - StudyEstimand
    range: StudyInterventionRef
    maximum_cardinality: 1
  studyEndPointRef:
    name: studyEndPointRef
    domain_of:
    - StudyObjective
    - StudyEstimand
    range: StudyEndPointRef
    maximum_cardinality: 1
  intercurrentEvent:
    name: intercurrentEvent
    multivalued: true
    domain_of:
    - StudyEstimand
    range: IntercurrentEvent
    inlined: true
    inlined_as_list: true
  summaryMeasure:
    name: summaryMeasure
    domain_of:
    - StudyEstimand
    range: SummaryMeasure
    maximum_cardinality: 1
class_uri: odm:StudyEstimand

```
</details>

### Induced

<details>
```yaml
name: StudyEstimand
description: A precise description of the treatment effect reflecting the clinical
  question posed by a given clinical trial objective. It summarises at a population
  level what the outcomes would be in the same patients under different treatment
  conditions being compared.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEstimand
rank: 1000
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the StudyEstimand element.
    comments:
    - 'Required

      range: oid'
    identifier: true
    domain_of:
    - Study
    - MetaDataVersion
    - Standard
    - ValueListDef
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - MethodDef
    - ConditionDef
    - CommentDef
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyParameter
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  name:
    name: name
    description: Human readable name for the Study Estimand.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: nameType
    required: true
  level:
    name: level
    description: Defined Level for the Study Estimand
    comments:
    - 'Optional

      enum values: ( Primary | Secondary | Exploratory )'
    domain_of:
    - StudyObjective
    - StudyEndPoint
    - StudyEstimand
    range: StudyEstimandLevel
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
  studyTargetPopulationRef:
    name: studyTargetPopulationRef
    domain_of:
    - StudyEstimand
    range: StudyTargetPopulationRef
    maximum_cardinality: 1
  studyInterventionRef:
    name: studyInterventionRef
    domain_of:
    - StudyEstimand
    range: StudyInterventionRef
    maximum_cardinality: 1
  studyEndPointRef:
    name: studyEndPointRef
    domain_of:
    - StudyObjective
    - StudyEstimand
    range: StudyEndPointRef
    maximum_cardinality: 1
  intercurrentEvent:
    name: intercurrentEvent
    multivalued: true
    domain_of:
    - StudyEstimand
    range: IntercurrentEvent
    inlined: true
    inlined_as_list: true
  summaryMeasure:
    name: summaryMeasure
    domain_of:
    - StudyEstimand
    range: SummaryMeasure
    maximum_cardinality: 1
attributes:
  OID:
    name: OID
    description: Unique identifier for the StudyEstimand element.
    comments:
    - 'Required

      range: oid'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: StudyEstimand
    domain_of:
    - Study
    - MetaDataVersion
    - Standard
    - ValueListDef
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - MethodDef
    - ConditionDef
    - CommentDef
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyParameter
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  name:
    name: name
    description: Human readable name for the Study Estimand.
    comments:
    - 'Required

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: name
    owner: StudyEstimand
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: nameType
    required: true
  level:
    name: level
    description: Defined Level for the Study Estimand
    comments:
    - 'Optional

      enum values: ( Primary | Secondary | Exploratory )'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: level
    owner: StudyEstimand
    domain_of:
    - StudyObjective
    - StudyEndPoint
    - StudyEstimand
    range: StudyEstimandLevel
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: description
    owner: StudyEstimand
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
  studyTargetPopulationRef:
    name: studyTargetPopulationRef
    description: 'StudyTargetPopulationRef reference: The StudyTargetPopulationRef
      references a StudyTargetPopulation to which the estimand applies.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyTargetPopulationRef
    owner: StudyEstimand
    domain_of:
    - StudyEstimand
    range: StudyTargetPopulationRef
    maximum_cardinality: 1
  studyInterventionRef:
    name: studyInterventionRef
    description: 'StudyInterventionRef reference: The StudyInterventionRef references
      an intervention that is taken as the treatment for the estimand.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyInterventionRef
    owner: StudyEstimand
    domain_of:
    - StudyEstimand
    range: StudyInterventionRef
    maximum_cardinality: 1
  studyEndPointRef:
    name: studyEndPointRef
    description: 'StudyEndPointRef reference: A reference to a StudyEndPoint as it
      occurs within a specific StudyObjective.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyEndPointRef
    owner: StudyEstimand
    domain_of:
    - StudyObjective
    - StudyEstimand
    range: StudyEndPointRef
    maximum_cardinality: 1
  intercurrentEvent:
    name: intercurrentEvent
    description: 'IntercurrentEvent reference: The IntercurrentEvent element describes
      an intercurrent event for an estimand (e.g., treatment discontinuation).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: intercurrentEvent
    owner: StudyEstimand
    domain_of:
    - StudyEstimand
    range: IntercurrentEvent
    inlined: true
    inlined_as_list: true
  summaryMeasure:
    name: summaryMeasure
    description: 'SummaryMeasure reference: The SummaryMeasure element describes a
      summary measure for an estimand (e.g., proportion of patients with an improvement).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: summaryMeasure
    owner: StudyEstimand
    domain_of:
    - StudyEstimand
    range: SummaryMeasure
    maximum_cardinality: 1
class_uri: odm:StudyEstimand

```
</details>