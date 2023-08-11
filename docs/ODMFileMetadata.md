# Class: ODMFileMetadata



URI: [odm:ODM](http://www.cdisc.org/ns/odm/v2.0/ODM)



```mermaid
 classDiagram
    class ODMFileMetadata
      ODMFileMetadata : AdminDataRef
        
          ODMFileMetadata --|> AdminData : AdminDataRef
        
      ODMFileMetadata : AsOfDateTime
        
      ODMFileMetadata : AssociationRef
        
          ODMFileMetadata --|> Association : AssociationRef
        
      ODMFileMetadata : ClinicalDataRef
        
          ODMFileMetadata --|> ClinicalData : ClinicalDataRef
        
      ODMFileMetadata : ContextRef
        
          ODMFileMetadata --|> Context : ContextRef
        
      ODMFileMetadata : CreationDateTime
        
      ODMFileMetadata : DescriptionRef
        
          ODMFileMetadata --|> Description : DescriptionRef
        
      ODMFileMetadata : FileOID
        
      ODMFileMetadata : FileTypeRef
        
          ODMFileMetadata --|> FileType : FileTypeRef
        
      ODMFileMetadata : GranularityRef
        
          ODMFileMetadata --|> Granularity : GranularityRef
        
      ODMFileMetadata : ODMVersionRef
        
      ODMFileMetadata : Originator
        
      ODMFileMetadata : PriorFileOID
        
      ODMFileMetadata : ReferenceDataRef
        
          ODMFileMetadata --|> ReferenceData : ReferenceDataRef
        
      ODMFileMetadata : SourceSystem
        
      ODMFileMetadata : SourceSystemVersion
        
      ODMFileMetadata : StudyRef
        
          ODMFileMetadata --|> Study : StudyRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [FileTypeRef](FileTypeRef.md) | 1..1 <br/> [FileType](FileType.md) |  | direct |
| [GranularityRef](GranularityRef.md) | 0..1 <br/> [Granularity](Granularity.md) |  | direct |
| [ContextRef](ContextRef.md) | 0..1 <br/> [Context](Context.md) |  | direct |
| [FileOID](FileOID.md) | 1..1 <br/> [Oid](Oid.md) |  | direct |
| [CreationDateTime](CreationDateTime.md) | 1..1 <br/> [Datetime](Datetime.md) |  | direct |
| [PriorFileOID](PriorFileOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [AsOfDateTime](AsOfDateTime.md) | 0..1 <br/> [Datetime](Datetime.md) |  | direct |
| [ODMVersionRef](ODMVersionRef.md) | 0..1 <br/> [ODMVersion](ODMVersion.md) |  | direct |
| [Originator](Originator.md) | 0..1 <br/> [Text](Text.md) |  | direct |
| [SourceSystem](SourceSystem.md) | 0..1 <br/> [Text](Text.md) |  | direct |
| [SourceSystemVersion](SourceSystemVersion.md) | 0..1 <br/> [Text](Text.md) |  | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) |  | direct |
| [StudyRef](StudyRef.md) | 0..* <br/> [Study](Study.md) |  | direct |
| [AdminDataRef](AdminDataRef.md) | 0..* <br/> [AdminData](AdminData.md) |  | direct |
| [ReferenceDataRef](ReferenceDataRef.md) | 0..* <br/> [ReferenceData](ReferenceData.md) |  | direct |
| [ClinicalDataRef](ClinicalDataRef.md) | 0..* <br/> [ClinicalData](ClinicalData.md) |  | direct |
| [AssociationRef](AssociationRef.md) | 0..* <br/> [Association](Association.md) |  | direct |









## See Also

* [https://wiki.cdisc.org/display/ODM2/ODM](https://wiki.cdisc.org/display/ODM2/ODM)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ODM |
| native | odm:ODMFileMetadata |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ODMFileMetadata
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ODM
slots:
- FileTypeRef
- GranularityRef
- ContextRef
- FileOID
- CreationDateTime
- PriorFileOID
- AsOfDateTime
- ODMVersionRef
- Originator
- SourceSystem
- SourceSystemVersion
- DescriptionRef
- StudyRef
- AdminDataRef
- ReferenceDataRef
- ClinicalDataRef
- AssociationRef
slot_usage:
  FileTypeRef:
    name: FileTypeRef
    domain_of:
    - ODMFileMetadata
    range: FileType
    required: true
  GranularityRef:
    name: GranularityRef
    domain_of:
    - ODMFileMetadata
    range: Granularity
  ContextRef:
    name: ContextRef
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: Context
  FileOID:
    name: FileOID
    domain_of:
    - ODMFileMetadata
    range: oid
    required: true
  CreationDateTime:
    name: CreationDateTime
    domain_of:
    - ODMFileMetadata
    range: datetime
    required: true
  PriorFileOID:
    name: PriorFileOID
    domain_of:
    - ODMFileMetadata
    range: oidref
  AsOfDateTime:
    name: AsOfDateTime
    domain_of:
    - ODMFileMetadata
    range: datetime
  ODMVersionRef:
    name: ODMVersionRef
    domain_of:
    - ODMFileMetadata
    range: ODMVersion
  Originator:
    name: Originator
    domain_of:
    - ODMFileMetadata
    range: text
  SourceSystem:
    name: SourceSystem
    domain_of:
    - ODMFileMetadata
    range: text
  SourceSystemVersion:
    name: SourceSystemVersion
    domain_of:
    - ODMFileMetadata
    range: text
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
  StudyRef:
    name: StudyRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Study
    inlined: true
    inlined_as_list: true
  AdminDataRef:
    name: AdminDataRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: AdminData
    inlined: true
    inlined_as_list: true
  ReferenceDataRef:
    name: ReferenceDataRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ReferenceData
    inlined: true
    inlined_as_list: true
  ClinicalDataRef:
    name: ClinicalDataRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ClinicalData
    inlined: true
    inlined_as_list: true
  AssociationRef:
    name: AssociationRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Association
    inlined: true
    inlined_as_list: true
class_uri: odm:ODM

```
</details>

### Induced

<details>
```yaml
name: ODMFileMetadata
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ODM
slot_usage:
  FileTypeRef:
    name: FileTypeRef
    domain_of:
    - ODMFileMetadata
    range: FileType
    required: true
  GranularityRef:
    name: GranularityRef
    domain_of:
    - ODMFileMetadata
    range: Granularity
  ContextRef:
    name: ContextRef
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: Context
  FileOID:
    name: FileOID
    domain_of:
    - ODMFileMetadata
    range: oid
    required: true
  CreationDateTime:
    name: CreationDateTime
    domain_of:
    - ODMFileMetadata
    range: datetime
    required: true
  PriorFileOID:
    name: PriorFileOID
    domain_of:
    - ODMFileMetadata
    range: oidref
  AsOfDateTime:
    name: AsOfDateTime
    domain_of:
    - ODMFileMetadata
    range: datetime
  ODMVersionRef:
    name: ODMVersionRef
    domain_of:
    - ODMFileMetadata
    range: ODMVersion
  Originator:
    name: Originator
    domain_of:
    - ODMFileMetadata
    range: text
  SourceSystem:
    name: SourceSystem
    domain_of:
    - ODMFileMetadata
    range: text
  SourceSystemVersion:
    name: SourceSystemVersion
    domain_of:
    - ODMFileMetadata
    range: text
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
  StudyRef:
    name: StudyRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Study
    inlined: true
    inlined_as_list: true
  AdminDataRef:
    name: AdminDataRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: AdminData
    inlined: true
    inlined_as_list: true
  ReferenceDataRef:
    name: ReferenceDataRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ReferenceData
    inlined: true
    inlined_as_list: true
  ClinicalDataRef:
    name: ClinicalDataRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ClinicalData
    inlined: true
    inlined_as_list: true
  AssociationRef:
    name: AssociationRef
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Association
    inlined: true
    inlined_as_list: true
attributes:
  FileTypeRef:
    name: FileTypeRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: FileTypeRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: FileType
    required: true
  GranularityRef:
    name: GranularityRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: GranularityRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: Granularity
  ContextRef:
    name: ContextRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ContextRef
    owner: ODMFileMetadata
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: Context
  FileOID:
    name: FileOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: FileOID
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: oid
    required: true
  CreationDateTime:
    name: CreationDateTime
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CreationDateTime
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: datetime
    required: true
  PriorFileOID:
    name: PriorFileOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: PriorFileOID
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: oidref
  AsOfDateTime:
    name: AsOfDateTime
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: AsOfDateTime
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: datetime
  ODMVersionRef:
    name: ODMVersionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ODMVersionRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: ODMVersion
  Originator:
    name: Originator
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Originator
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: text
  SourceSystem:
    name: SourceSystem
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SourceSystem
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: text
  SourceSystemVersion:
    name: SourceSystemVersion
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SourceSystemVersion
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: text
  DescriptionRef:
    name: DescriptionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: DescriptionRef
    owner: ODMFileMetadata
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
  StudyRef:
    name: StudyRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: StudyRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: Study
    inlined: true
    inlined_as_list: true
  AdminDataRef:
    name: AdminDataRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: AdminDataRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: AdminData
    inlined: true
    inlined_as_list: true
  ReferenceDataRef:
    name: ReferenceDataRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: ReferenceDataRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: ReferenceData
    inlined: true
    inlined_as_list: true
  ClinicalDataRef:
    name: ClinicalDataRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: ClinicalDataRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: ClinicalData
    inlined: true
    inlined_as_list: true
  AssociationRef:
    name: AssociationRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: AssociationRef
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: Association
    inlined: true
    inlined_as_list: true
class_uri: odm:ODM

```
</details>