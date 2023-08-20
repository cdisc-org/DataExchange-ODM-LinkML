# Class: StudyEstimand


_Element NameStudyEstimandParent ElementsStudyEstimandsElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimandElement Textual ValueNoneAttributesOID, NameChild Elements(Description?, StudyTargetPopulationRef?, StudyInterventionRef?, StudyEndpointRef?, IntercurrentEvent*, SummaryMeasure?)Usage/Business Rules_





URI: [odm:StudyEstimand](http://www.cdisc.org/ns/odm/v2.0/StudyEstimand)



```mermaid
 classDiagram
    class StudyEstimand
      StudyEstimand : DescriptionRef
        
          StudyEstimand --|> Description : DescriptionRef
        
      StudyEstimand : IntercurrentEventRef
        
          StudyEstimand --|> IntercurrentEvent : IntercurrentEventRef
        
      StudyEstimand : Level
        
          StudyEstimand --|> StudyEstimandLevel : Level
        
      StudyEstimand : Name
        
      StudyEstimand : OID
        
      StudyEstimand : StudyEndPointRefRef
        
          StudyEstimand --|> StudyEndPointRef : StudyEndPointRefRef
        
      StudyEstimand : StudyInterventionRefRef
        
          StudyEstimand --|> StudyInterventionRef : StudyInterventionRefRef
        
      StudyEstimand : StudyTargetPopulationRefRef
        
          StudyEstimand --|> StudyTargetPopulationRef : StudyTargetPopulationRefRef
        
      StudyEstimand : SummaryMeasureRef
        
          StudyEstimand --|> SummaryMeasure : SummaryMeasureRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier for the StudyEstimand element | direct |
| [Name](Name.md) | 1..1 <br/> [Name](Name.md) | Human readable name for the Study Estimand | direct |
| [Level](Level.md) | 0..1 <br/> [StudyEstimandLevel](StudyEstimandLevel.md) | Defined Level for the Study Estimand | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) |  | direct |
| [StudyTargetPopulationRefRef](StudyTargetPopulationRefRef.md) | 0..1 <br/> [StudyTargetPopulationRef](StudyTargetPopulationRef.md) |  | direct |
| [StudyInterventionRefRef](StudyInterventionRefRef.md) | 0..1 <br/> [StudyInterventionRef](StudyInterventionRef.md) |  | direct |
| [StudyEndPointRefRef](StudyEndPointRefRef.md) | 0..1 <br/> [StudyEndPointRef](StudyEndPointRef.md) |  | direct |
| [IntercurrentEventRef](IntercurrentEventRef.md) | 0..* <br/> [IntercurrentEvent](IntercurrentEvent.md) |  | direct |
| [SummaryMeasureRef](SummaryMeasureRef.md) | 0..1 <br/> [SummaryMeasure](SummaryMeasure.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEstimands](StudyEstimands.md) | [StudyEstimandRef](StudyEstimandRef.md) | range | [StudyEstimand](StudyEstimand.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/StudyEstimand](https://wiki.cdisc.org/display/ODM2/StudyEstimand)

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
description: Element NameStudyEstimandParent ElementsStudyEstimandsElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimandElement
  Textual ValueNoneAttributesOID, NameChild Elements(Description?, StudyTargetPopulationRef?,
  StudyInterventionRef?, StudyEndpointRef?, IntercurrentEvent*, SummaryMeasure?)Usage/Business
  Rules
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyEstimand
slots:
- OID
- Name
- Level
- DescriptionRef
- StudyTargetPopulationRefRef
- StudyInterventionRefRef
- StudyEndPointRefRef
- IntercurrentEventRef
- SummaryMeasureRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the StudyEstimand element.
    comments:
    - 'Required

      range:oid'
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
    - ExceptionEvent
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  Name:
    name: Name
    description: Human readable name for the Study Estimand.
    comments:
    - 'Required

      range:name'
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
    - ExceptionEvent
    - Organization
    - Location
    - Query
    range: name
    required: true
  Level:
    name: Level
    description: Defined Level for the Study Estimand
    comments:
    - 'Optional

      enum values:( Primary | Secondary | Exploratory )'
    domain_of:
    - StudyObjective
    - StudyEndPoint
    - StudyEstimand
    range: StudyEstimandLevel
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
  StudyTargetPopulationRefRef:
    name: StudyTargetPopulationRefRef
    domain_of:
    - Protocol
    - StudyEstimand
    range: StudyTargetPopulationRef
    maximum_cardinality: 1
  StudyInterventionRefRef:
    name: StudyInterventionRefRef
    domain_of:
    - StudyInterventions
    - StudyEstimand
    range: StudyInterventionRef
    maximum_cardinality: 1
  StudyEndPointRefRef:
    name: StudyEndPointRefRef
    domain_of:
    - StudyObjective
    - StudyEndPoints
    - StudyEstimand
    range: StudyEndPointRef
    maximum_cardinality: 1
  IntercurrentEventRef:
    name: IntercurrentEventRef
    multivalued: true
    domain_of:
    - StudyEstimand
    range: IntercurrentEvent
    inlined: true
    inlined_as_list: true
  SummaryMeasureRef:
    name: SummaryMeasureRef
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
description: Element NameStudyEstimandParent ElementsStudyEstimandsElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimandElement
  Textual ValueNoneAttributesOID, NameChild Elements(Description?, StudyTargetPopulationRef?,
  StudyInterventionRef?, StudyEndpointRef?, IntercurrentEvent*, SummaryMeasure?)Usage/Business
  Rules
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyEstimand
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the StudyEstimand element.
    comments:
    - 'Required

      range:oid'
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
    - ExceptionEvent
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  Name:
    name: Name
    description: Human readable name for the Study Estimand.
    comments:
    - 'Required

      range:name'
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
    - ExceptionEvent
    - Organization
    - Location
    - Query
    range: name
    required: true
  Level:
    name: Level
    description: Defined Level for the Study Estimand
    comments:
    - 'Optional

      enum values:( Primary | Secondary | Exploratory )'
    domain_of:
    - StudyObjective
    - StudyEndPoint
    - StudyEstimand
    range: StudyEstimandLevel
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
  StudyTargetPopulationRefRef:
    name: StudyTargetPopulationRefRef
    domain_of:
    - Protocol
    - StudyEstimand
    range: StudyTargetPopulationRef
    maximum_cardinality: 1
  StudyInterventionRefRef:
    name: StudyInterventionRefRef
    domain_of:
    - StudyInterventions
    - StudyEstimand
    range: StudyInterventionRef
    maximum_cardinality: 1
  StudyEndPointRefRef:
    name: StudyEndPointRefRef
    domain_of:
    - StudyObjective
    - StudyEndPoints
    - StudyEstimand
    range: StudyEndPointRef
    maximum_cardinality: 1
  IntercurrentEventRef:
    name: IntercurrentEventRef
    multivalued: true
    domain_of:
    - StudyEstimand
    range: IntercurrentEvent
    inlined: true
    inlined_as_list: true
  SummaryMeasureRef:
    name: SummaryMeasureRef
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

      range:oid'
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
    - ExceptionEvent
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  Name:
    name: Name
    description: Human readable name for the Study Estimand.
    comments:
    - 'Required

      range:name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
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
    - ExceptionEvent
    - Organization
    - Location
    - Query
    range: name
    required: true
  Level:
    name: Level
    description: Defined Level for the Study Estimand
    comments:
    - 'Optional

      enum values:( Primary | Secondary | Exploratory )'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Level
    owner: StudyEstimand
    domain_of:
    - StudyObjective
    - StudyEndPoint
    - StudyEstimand
    range: StudyEstimandLevel
  DescriptionRef:
    name: DescriptionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
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
    - ExceptionEvent
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  StudyTargetPopulationRefRef:
    name: StudyTargetPopulationRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyTargetPopulationRefRef
    owner: StudyEstimand
    domain_of:
    - Protocol
    - StudyEstimand
    range: StudyTargetPopulationRef
    maximum_cardinality: 1
  StudyInterventionRefRef:
    name: StudyInterventionRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyInterventionRefRef
    owner: StudyEstimand
    domain_of:
    - StudyInterventions
    - StudyEstimand
    range: StudyInterventionRef
    maximum_cardinality: 1
  StudyEndPointRefRef:
    name: StudyEndPointRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StudyEndPointRefRef
    owner: StudyEstimand
    domain_of:
    - StudyObjective
    - StudyEndPoints
    - StudyEstimand
    range: StudyEndPointRef
    maximum_cardinality: 1
  IntercurrentEventRef:
    name: IntercurrentEventRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: IntercurrentEventRef
    owner: StudyEstimand
    domain_of:
    - StudyEstimand
    range: IntercurrentEvent
    inlined: true
    inlined_as_list: true
  SummaryMeasureRef:
    name: SummaryMeasureRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SummaryMeasureRef
    owner: StudyEstimand
    domain_of:
    - StudyEstimand
    range: SummaryMeasure
    maximum_cardinality: 1
class_uri: odm:StudyEstimand

```
</details>