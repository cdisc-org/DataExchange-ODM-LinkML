# Class: Protocol


_The Protocol element lists the kinds of study events that can occur within a specific version of a study. All clinical data must occur within one of these study events._





URI: [odm:Protocol](http://www.cdisc.org/ns/odm/v2.0/Protocol)



```mermaid
 classDiagram
    class Protocol
      Protocol : AliasRef
        
          Protocol --|> Alias : AliasRef
        
      Protocol : DescriptionRef
        
          Protocol --|> Description : DescriptionRef
        
      Protocol : InclusionExclusionCriteriaRef
        
          Protocol --|> InclusionExclusionCriteria : InclusionExclusionCriteriaRef
        
      Protocol : StudyEndPointsRef
        
          Protocol --|> StudyEndPoints : StudyEndPointsRef
        
      Protocol : StudyEstimandsRef
        
          Protocol --|> StudyEstimands : StudyEstimandsRef
        
      Protocol : StudyEventGroupRefRef
        
          Protocol --|> StudyEventGroupRef : StudyEventGroupRefRef
        
      Protocol : StudyIndicationsRef
        
          Protocol --|> StudyIndications : StudyIndicationsRef
        
      Protocol : StudyInterventionsRef
        
          Protocol --|> StudyInterventions : StudyInterventionsRef
        
      Protocol : StudyObjectivesRef
        
          Protocol --|> StudyObjectives : StudyObjectivesRef
        
      Protocol : StudyStructureRef
        
          Protocol --|> StudyStructure : StudyStructureRef
        
      Protocol : StudySummaryRef
        
          Protocol --|> StudySummary : StudySummaryRef
        
      Protocol : StudyTargetPopulationRefRef
        
          Protocol --|> StudyTargetPopulation : StudyTargetPopulationRefRef
        
      Protocol : StudyTimingsRef
        
          Protocol --|> StudyTimings : StudyTimingsRef
        
      Protocol : TrialPhaseRef
        
          Protocol --|> TrialPhase : TrialPhaseRef
        
      Protocol : WorkflowRefRef
        
          Protocol --|> WorkflowRef : WorkflowRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) |  | direct |
| [StudySummaryRef](StudySummaryRef.md) | 0..1 <br/> [StudySummary](StudySummary.md) |  | direct |
| [StudyStructureRef](StudyStructureRef.md) | 0..1 <br/> [StudyStructure](StudyStructure.md) |  | direct |
| [TrialPhaseRef](TrialPhaseRef.md) | 0..1 <br/> [TrialPhase](TrialPhase.md) |  | direct |
| [StudyTimingsRef](StudyTimingsRef.md) | 0..1 <br/> [StudyTimings](StudyTimings.md) |  | direct |
| [StudyIndicationsRef](StudyIndicationsRef.md) | 0..1 <br/> [StudyIndications](StudyIndications.md) |  | direct |
| [StudyInterventionsRef](StudyInterventionsRef.md) | 0..1 <br/> [StudyInterventions](StudyInterventions.md) |  | direct |
| [StudyObjectivesRef](StudyObjectivesRef.md) | 0..1 <br/> [StudyObjectives](StudyObjectives.md) |  | direct |
| [StudyEndPointsRef](StudyEndPointsRef.md) | 0..1 <br/> [StudyEndPoints](StudyEndPoints.md) |  | direct |
| [StudyTargetPopulationRefRef](StudyTargetPopulationRefRef.md) | 0..1 <br/> [StudyTargetPopulation](StudyTargetPopulation.md) |  | direct |
| [StudyEstimandsRef](StudyEstimandsRef.md) | 0..1 <br/> [StudyEstimands](StudyEstimands.md) |  | direct |
| [InclusionExclusionCriteriaRef](InclusionExclusionCriteriaRef.md) | 0..1 <br/> [InclusionExclusionCriteria](InclusionExclusionCriteria.md) |  | direct |
| [StudyEventGroupRefRef](StudyEventGroupRefRef.md) | 0..* <br/> [StudyEventGroupRef](StudyEventGroupRef.md) |  | direct |
| [WorkflowRefRef](WorkflowRefRef.md) | 0..1 <br/> [WorkflowRef](WorkflowRef.md) |  | direct |
| [AliasRef](AliasRef.md) | 0..* <br/> [Alias](Alias.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [ProtocolRef](ProtocolRef.md) | range | [Protocol](Protocol.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Protocol](https://wiki.cdisc.org/display/ODM2/Protocol)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Protocol |
| native | odm:Protocol |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Protocol
description: The Protocol element lists the kinds of study events that can occur within
  a specific version of a study. All clinical data must occur within one of these
  study events.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Protocol
slots:
- DescriptionRef
- StudySummaryRef
- StudyStructureRef
- TrialPhaseRef
- StudyTimingsRef
- StudyIndicationsRef
- StudyInterventionsRef
- StudyObjectivesRef
- StudyEndPointsRef
- StudyTargetPopulationRefRef
- StudyEstimandsRef
- InclusionExclusionCriteriaRef
- StudyEventGroupRefRef
- WorkflowRefRef
- AliasRef
slot_usage:
  DescriptionRef:
    name: DescriptionRef
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
    - ExceptionEvent
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  StudySummaryRef:
    name: StudySummaryRef
    domain_of:
    - Protocol
    range: StudySummary
    maximum_cardinality: 1
  StudyStructureRef:
    name: StudyStructureRef
    domain_of:
    - Protocol
    range: StudyStructure
    maximum_cardinality: 1
  TrialPhaseRef:
    name: TrialPhaseRef
    domain_of:
    - Protocol
    range: TrialPhase
    maximum_cardinality: 1
  StudyTimingsRef:
    name: StudyTimingsRef
    domain_of:
    - Protocol
    range: StudyTimings
    maximum_cardinality: 1
  StudyIndicationsRef:
    name: StudyIndicationsRef
    domain_of:
    - Protocol
    range: StudyIndications
    maximum_cardinality: 1
  StudyInterventionsRef:
    name: StudyInterventionsRef
    domain_of:
    - Protocol
    range: StudyInterventions
    maximum_cardinality: 1
  StudyObjectivesRef:
    name: StudyObjectivesRef
    domain_of:
    - Protocol
    range: StudyObjectives
    maximum_cardinality: 1
  StudyEndPointsRef:
    name: StudyEndPointsRef
    domain_of:
    - Protocol
    range: StudyEndPoints
    maximum_cardinality: 1
  StudyTargetPopulationRefRef:
    name: StudyTargetPopulationRefRef
    domain_of:
    - Protocol
    - StudyEstimand
    range: StudyTargetPopulation
    maximum_cardinality: 1
  StudyEstimandsRef:
    name: StudyEstimandsRef
    domain_of:
    - Protocol
    range: StudyEstimands
    maximum_cardinality: 1
  InclusionExclusionCriteriaRef:
    name: InclusionExclusionCriteriaRef
    domain_of:
    - Protocol
    range: InclusionExclusionCriteria
    maximum_cardinality: 1
  StudyEventGroupRefRef:
    name: StudyEventGroupRefRef
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - Protocol
    - ExceptionEvent
    range: StudyEventGroupRef
    inlined: true
    inlined_as_list: true
  WorkflowRefRef:
    name: WorkflowRefRef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    - ExceptionEvent
    range: WorkflowRef
    maximum_cardinality: 1
  AliasRef:
    name: AliasRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
class_uri: odm:Protocol

```
</details>

### Induced

<details>
```yaml
name: Protocol
description: The Protocol element lists the kinds of study events that can occur within
  a specific version of a study. All clinical data must occur within one of these
  study events.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Protocol
slot_usage:
  DescriptionRef:
    name: DescriptionRef
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
    - ExceptionEvent
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  StudySummaryRef:
    name: StudySummaryRef
    domain_of:
    - Protocol
    range: StudySummary
    maximum_cardinality: 1
  StudyStructureRef:
    name: StudyStructureRef
    domain_of:
    - Protocol
    range: StudyStructure
    maximum_cardinality: 1
  TrialPhaseRef:
    name: TrialPhaseRef
    domain_of:
    - Protocol
    range: TrialPhase
    maximum_cardinality: 1
  StudyTimingsRef:
    name: StudyTimingsRef
    domain_of:
    - Protocol
    range: StudyTimings
    maximum_cardinality: 1
  StudyIndicationsRef:
    name: StudyIndicationsRef
    domain_of:
    - Protocol
    range: StudyIndications
    maximum_cardinality: 1
  StudyInterventionsRef:
    name: StudyInterventionsRef
    domain_of:
    - Protocol
    range: StudyInterventions
    maximum_cardinality: 1
  StudyObjectivesRef:
    name: StudyObjectivesRef
    domain_of:
    - Protocol
    range: StudyObjectives
    maximum_cardinality: 1
  StudyEndPointsRef:
    name: StudyEndPointsRef
    domain_of:
    - Protocol
    range: StudyEndPoints
    maximum_cardinality: 1
  StudyTargetPopulationRefRef:
    name: StudyTargetPopulationRefRef
    domain_of:
    - Protocol
    - StudyEstimand
    range: StudyTargetPopulation
    maximum_cardinality: 1
  StudyEstimandsRef:
    name: StudyEstimandsRef
    domain_of:
    - Protocol
    range: StudyEstimands
    maximum_cardinality: 1
  InclusionExclusionCriteriaRef:
    name: InclusionExclusionCriteriaRef
    domain_of:
    - Protocol
    range: InclusionExclusionCriteria
    maximum_cardinality: 1
  StudyEventGroupRefRef:
    name: StudyEventGroupRefRef
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - Protocol
    - ExceptionEvent
    range: StudyEventGroupRef
    inlined: true
    inlined_as_list: true
  WorkflowRefRef:
    name: WorkflowRefRef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    - ExceptionEvent
    range: WorkflowRef
    maximum_cardinality: 1
  AliasRef:
    name: AliasRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
attributes:
  DescriptionRef:
    name: DescriptionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
    owner: Protocol
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
    - ExceptionEvent
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  StudySummaryRef:
    name: StudySummaryRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudySummaryRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudySummary
    maximum_cardinality: 1
  StudyStructureRef:
    name: StudyStructureRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyStructureRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudyStructure
    maximum_cardinality: 1
  TrialPhaseRef:
    name: TrialPhaseRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: TrialPhaseRef
    owner: Protocol
    domain_of:
    - Protocol
    range: TrialPhase
    maximum_cardinality: 1
  StudyTimingsRef:
    name: StudyTimingsRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyTimingsRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudyTimings
    maximum_cardinality: 1
  StudyIndicationsRef:
    name: StudyIndicationsRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyIndicationsRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudyIndications
    maximum_cardinality: 1
  StudyInterventionsRef:
    name: StudyInterventionsRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyInterventionsRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudyInterventions
    maximum_cardinality: 1
  StudyObjectivesRef:
    name: StudyObjectivesRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyObjectivesRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudyObjectives
    maximum_cardinality: 1
  StudyEndPointsRef:
    name: StudyEndPointsRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyEndPointsRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudyEndPoints
    maximum_cardinality: 1
  StudyTargetPopulationRefRef:
    name: StudyTargetPopulationRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyTargetPopulationRefRef
    owner: Protocol
    domain_of:
    - Protocol
    - StudyEstimand
    range: StudyTargetPopulation
    maximum_cardinality: 1
  StudyEstimandsRef:
    name: StudyEstimandsRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyEstimandsRef
    owner: Protocol
    domain_of:
    - Protocol
    range: StudyEstimands
    maximum_cardinality: 1
  InclusionExclusionCriteriaRef:
    name: InclusionExclusionCriteriaRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: InclusionExclusionCriteriaRef
    owner: Protocol
    domain_of:
    - Protocol
    range: InclusionExclusionCriteria
    maximum_cardinality: 1
  StudyEventGroupRefRef:
    name: StudyEventGroupRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: StudyEventGroupRefRef
    owner: Protocol
    domain_of:
    - StudyEventGroupDef
    - Protocol
    - ExceptionEvent
    range: StudyEventGroupRef
    inlined: true
    inlined_as_list: true
  WorkflowRefRef:
    name: WorkflowRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: WorkflowRefRef
    owner: Protocol
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    - ExceptionEvent
    range: WorkflowRef
    maximum_cardinality: 1
  AliasRef:
    name: AliasRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: AliasRef
    owner: Protocol
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
class_uri: odm:Protocol

```
</details>