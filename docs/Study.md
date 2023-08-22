# Class: Study

_This element collects static structural information about an individual study._




URI: [odm:Study](http://www.cdisc.org/ns/odm/v2.0/Study)


```mermaid
erDiagram
Study {
    oid OID  
    name StudyName  
    name ProtocolName  
    name VersionID  
    name VersionName  
    name Status  
}
MetaDataVersion {
    oid OID  
    name Name  
    oidref CommentOID  
}
Leaf {
    oid ID  
    uriorcurie href  
}
CommentDef {
    oid OID  
}
MethodDef {
    oid OID  
    name Name  
    MethodType Type  
    oidref CommentOID  
}
ConditionDef {
    oid OID  
    name Name  
    oidref CommentOID  
}
CodeList {
    oid OID  
    name Name  
    CLDataType DataTypeRef  
    oidref CommentOID  
    oidref StandardOID  
    YesOnly IsNonStandard  
}
ItemDef {
    oid OID  
    name Name  
    DataType DataTypeRef  
    positiveInteger Length  
    text DisplayFormat  
    text VariableSet  
    oidref CommentOID  
}
ItemGroupDef {
    oid OID  
    name Name  
    ItemGroupRepeatingType Repeating  
    positiveInteger RepeatingLimit  
    YesOrNo IsReferenceData  
    text Structure  
    oidref ArchiveLocationID  
    name DatasetName  
    text Domain  
    ItemGroupTypeType Type  
    text Purpose  
    oidref StandardOID  
    YesOnly IsNonStandard  
    YesOnly HasNoData  
    oidref CommentOID  
}
StudyEventDef {
    oid OID  
    name Name  
    YesOrNo Repeating  
    EventType Type  
    text Category  
    oidref CommentOID  
}
StudyEventGroupDef {
    oid OID  
    name Name  
    oidref ArmOID  
    oidref EpochOID  
    oidref CommentOID  
}
WorkflowDef {
    oid OID  
    name Name  
}
Protocol {

}
WhereClauseDef {
    oid OID  
    oidref CommentOID  
}
ValueListDef {
    oid OID  
}
SupplementalDoc {

}
AnnotatedCRF {

}
Standards {

}
Include {
    oidref StudyOID  
    oidref MetaDataVersionOID  
    uriorcurie href  
}
Description {

}

Study ||--|o Description : "DescriptionRef"
Study ||--}o MetaDataVersion : "MetaDataVersionRefRef"
MetaDataVersion ||--|o Description : "DescriptionRef"
MetaDataVersion ||--|o Include : "IncludeRef"
MetaDataVersion ||--|o Standards : "StandardsRef"
MetaDataVersion ||--|o AnnotatedCRF : "AnnotatedCRFRef"
MetaDataVersion ||--|o SupplementalDoc : "SupplementalDocRef"
MetaDataVersion ||--}o ValueListDef : "ValueListDefRef"
MetaDataVersion ||--}o WhereClauseDef : "WhereClauseDefRef"
MetaDataVersion ||--|o Protocol : "ProtocolRef"
MetaDataVersion ||--}o WorkflowDef : "WorkflowDefRef"
MetaDataVersion ||--}o StudyEventGroupDef : "StudyEventGroupDefRef"
MetaDataVersion ||--}o StudyEventDef : "StudyEventDefRef"
MetaDataVersion ||--}o ItemGroupDef : "ItemGroupDefRef"
MetaDataVersion ||--}o ItemDef : "ItemDefRef"
MetaDataVersion ||--}o CodeList : "CodeListRefRef"
MetaDataVersion ||--}o ConditionDef : "ConditionDefRef"
MetaDataVersion ||--}o MethodDef : "MethodDefRef"
MetaDataVersion ||--}o CommentDef : "CommentDefRef"
MetaDataVersion ||--}o Leaf : "LeafRef"
Leaf ||--|o Title : "TitleRef"
CommentDef ||--|o Description : "DescriptionRef"
CommentDef ||--}o DocumentRef : "DocumentRefRef"
MethodDef ||--|o Description : "DescriptionRef"
MethodDef ||--|o MethodSignature : "MethodSignatureRef"
MethodDef ||--}o FormalExpression : "FormalExpressionRef"
MethodDef ||--}o Alias : "AliasRef"
MethodDef ||--}o DocumentRef : "DocumentRefRef"
ConditionDef ||--|o Description : "DescriptionRef"
ConditionDef ||--|o MethodSignature : "MethodSignatureRef"
ConditionDef ||--}o FormalExpression : "FormalExpressionRef"
ConditionDef ||--}o Alias : "AliasRef"
CodeList ||--|o Description : "DescriptionRef"
CodeList ||--}o CodeListItem : "CodeListItemRef"
CodeList ||--}o Coding : "CodingRef"
CodeList ||--}o Alias : "AliasRef"
ItemDef ||--|o Description : "DescriptionRef"
ItemDef ||--|o Definition : "DefinitionRef"
ItemDef ||--|o Question : "QuestionRef"
ItemDef ||--|o Prompt : "PromptRef"
ItemDef ||--|o CRFCompletionInstructions : "CRFCompletionInstructionsRef"
ItemDef ||--|o ImplementationNotes : "ImplementationNotesRef"
ItemDef ||--|o CDISCNotes : "CDISCNotesRef"
ItemDef ||--}o RangeCheck : "RangeCheckRef"
ItemDef ||--|o CodeListRef : "CodeListRefRef"
ItemDef ||--|o ValueListRef : "ValueListRefRef"
ItemDef ||--}o Coding : "CodingRef"
ItemDef ||--}o Alias : "AliasRef"
ItemGroupDef ||--|o Description : "DescriptionRef"
ItemGroupDef ||--|o Class : "ClassRef"
ItemGroupDef ||--}o Coding : "CodingRef"
ItemGroupDef ||--|o WorkflowRef : "WorkflowRefRef"
ItemGroupDef ||--}o Origin : "OriginRef"
ItemGroupDef ||--}o Alias : "AliasRef"
ItemGroupDef ||--|o Leaf : "LeafRef"
ItemGroupDef ||--}o ItemGroupRef : "ItemGroupRefRef"
ItemGroupDef ||--}o ItemRef : "ItemRefRef"
StudyEventDef ||--|o Description : "DescriptionRef"
StudyEventDef ||--}o ItemGroupRef : "ItemGroupRefRef"
StudyEventDef ||--|o WorkflowRef : "WorkflowRefRef"
StudyEventDef ||--}o Coding : "CodingRef"
StudyEventDef ||--}o Alias : "AliasRef"
StudyEventGroupDef ||--|o Description : "DescriptionRef"
StudyEventGroupDef ||--|o WorkflowRef : "WorkflowRefRef"
StudyEventGroupDef ||--}o Coding : "CodingRef"
StudyEventGroupDef ||--}o StudyEventGroupRef : "StudyEventGroupRefRef"
StudyEventGroupDef ||--}o StudyEventRef : "StudyEventRefRef"
WorkflowDef ||--|o Description : "DescriptionRef"
WorkflowDef ||--|o WorkflowStart : "WorkflowStartRef"
WorkflowDef ||--}o WorkflowEnd : "WorkflowEndRef"
WorkflowDef ||--}o Transition : "TransitionRef"
WorkflowDef ||--}o Branching : "BranchingRef"
Protocol ||--|o Description : "DescriptionRef"
Protocol ||--|o StudySummary : "StudySummaryRef"
Protocol ||--|o StudyStructure : "StudyStructureRef"
Protocol ||--|o TrialPhase : "TrialPhaseRef"
Protocol ||--|o StudyTimings : "StudyTimingsRef"
Protocol ||--|o StudyIndications : "StudyIndicationsRef"
Protocol ||--|o StudyInterventions : "StudyInterventionsRef"
Protocol ||--|o StudyObjectives : "StudyObjectivesRef"
Protocol ||--|o StudyEndPoints : "StudyEndPointsRef"
Protocol ||--|o StudyTargetPopulation : "StudyTargetPopulationRefRef"
Protocol ||--|o StudyEstimands : "StudyEstimandsRef"
Protocol ||--|o InclusionExclusionCriteria : "InclusionExclusionCriteriaRef"
Protocol ||--}o StudyEventGroupRef : "StudyEventGroupRefRef"
Protocol ||--|o WorkflowRef : "WorkflowRefRef"
Protocol ||--}o Alias : "AliasRef"
WhereClauseDef ||--}o RangeCheck : "RangeCheckRef"
ValueListDef ||--|o Description : "DescriptionRef"
ValueListDef ||--}o ItemRef : "ItemRefRef"
SupplementalDoc ||--}o DocumentRef : "DocumentRefRef"
AnnotatedCRF ||--}o DocumentRef : "DocumentRefRef"
Standards ||--}o Standard : "StandardRef"
Description ||--}o TranslatedText : "TranslatedTextRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier for the study. | direct |
| [StudyName](StudyName.md) | 1..1 <br/> [name](name.md) | Sponsoring organization's internal name for the study. If no internal name is... | direct |
| [ProtocolName](ProtocolName.md) | 1..1 <br/> [name](name.md) | Protocol identifier or protocol number assigned to the study. It is used by t... | direct |
| [VersionID](VersionID.md) | 0..1 <br/> [name](name.md) | Identifier for the specific version of the study in the source system that th... | direct |
| [VersionName](VersionName.md) | 0..1 <br/> [name](name.md) | Short descriptive label for the version of the study, e.g. "Initial go live" ... | direct |
| [Status](Status.md) | 0..1 <br/> [name](name.md) | Represents the workflow status for the version of the study with content incl... | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [MetaDataVersionRefRef](MetaDataVersionRefRef.md) | 0..* <br/> [MetaDataVersion](MetaDataVersion.md) | MetaDataVersionRef reference: A reference to a MetaDataVersion used at the co... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ODMFileMetadata](ODMFileMetadata.md) | [StudyRef](StudyRef.md) | range | [Study](Study.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Study](https://wiki.cdisc.org/display/ODM2/Study)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Study |
| native | odm:Study |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Study
description: This element collects static structural information about an individual
  study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Study
rank: 1000
slots:
- OID
- StudyName
- ProtocolName
- VersionID
- VersionName
- Status
- DescriptionRef
- MetaDataVersionRefRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the study.
    comments:
    - 'Required

      range: oid'
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
  StudyName:
    name: StudyName
    description: Sponsoring organization's internal name for the study. If no internal
      name is available, the value is expected to be the same value as ProtocolName.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: name
    required: true
  ProtocolName:
    name: ProtocolName
    description: Protocol identifier or protocol number assigned to the study. It
      is used by the regulatory authority or clinical trial registry.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: name
    required: true
  VersionID:
    name: VersionID
    description: Identifier for the specific version of the study in the source system
      that the enclosed Study element metadata refers to.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: name
  VersionName:
    name: VersionName
    description: Short descriptive label for the version of the study, e.g. "Initial
      go live" when VersionID = "<study version ID for Initial go live>". VersionName
      may be provided when a VersionID is provided.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: name
  Status:
    name: Status
    description: Represents the workflow status for the version of the study with
      content included in the enclosed Study element metadata. Status values can be
      different in each system and may have specific meaning within each system, e.g.
      a "Production" version of a study in a particular source system may be non-editable
      and editable in a different source system. If no VersionID is provided, Status
      refers to the status of the Study as a whole.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    - Standard
    range: name
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
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  MetaDataVersionRefRef:
    name: MetaDataVersionRefRef
    multivalued: true
    domain_of:
    - Study
    - Location
    range: MetaDataVersion
    inlined: true
    inlined_as_list: true
class_uri: odm:Study

```
</details>

### Induced

<details>
```yaml
name: Study
description: This element collects static structural information about an individual
  study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Study
rank: 1000
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the study.
    comments:
    - 'Required

      range: oid'
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
  StudyName:
    name: StudyName
    description: Sponsoring organization's internal name for the study. If no internal
      name is available, the value is expected to be the same value as ProtocolName.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: name
    required: true
  ProtocolName:
    name: ProtocolName
    description: Protocol identifier or protocol number assigned to the study. It
      is used by the regulatory authority or clinical trial registry.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: name
    required: true
  VersionID:
    name: VersionID
    description: Identifier for the specific version of the study in the source system
      that the enclosed Study element metadata refers to.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: name
  VersionName:
    name: VersionName
    description: Short descriptive label for the version of the study, e.g. "Initial
      go live" when VersionID = "<study version ID for Initial go live>". VersionName
      may be provided when a VersionID is provided.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: name
  Status:
    name: Status
    description: Represents the workflow status for the version of the study with
      content included in the enclosed Study element metadata. Status values can be
      different in each system and may have specific meaning within each system, e.g.
      a "Production" version of a study in a particular source system may be non-editable
      and editable in a different source system. If no VersionID is provided, Status
      refers to the status of the Study as a whole.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    - Standard
    range: name
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
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  MetaDataVersionRefRef:
    name: MetaDataVersionRefRef
    multivalued: true
    domain_of:
    - Study
    - Location
    range: MetaDataVersion
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier for the study.
    comments:
    - 'Required

      range: oid'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: Study
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
  StudyName:
    name: StudyName
    description: Sponsoring organization's internal name for the study. If no internal
      name is available, the value is expected to be the same value as ProtocolName.
    comments:
    - 'Required

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StudyName
    owner: Study
    domain_of:
    - Study
    range: name
    required: true
  ProtocolName:
    name: ProtocolName
    description: Protocol identifier or protocol number assigned to the study. It
      is used by the regulatory authority or clinical trial registry.
    comments:
    - 'Required

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ProtocolName
    owner: Study
    domain_of:
    - Study
    range: name
    required: true
  VersionID:
    name: VersionID
    description: Identifier for the specific version of the study in the source system
      that the enclosed Study element metadata refers to.
    comments:
    - 'Optional

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: VersionID
    owner: Study
    domain_of:
    - Study
    range: name
  VersionName:
    name: VersionName
    description: Short descriptive label for the version of the study, e.g. "Initial
      go live" when VersionID = "<study version ID for Initial go live>". VersionName
      may be provided when a VersionID is provided.
    comments:
    - 'Optional

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: VersionName
    owner: Study
    domain_of:
    - Study
    range: name
  Status:
    name: Status
    description: Represents the workflow status for the version of the study with
      content included in the enclosed Study element metadata. Status values can be
      different in each system and may have specific meaning within each system, e.g.
      a "Production" version of a study in a particular source system may be non-editable
      and editable in a different source system. If no VersionID is provided, Status
      refers to the status of the Study as a whole.
    comments:
    - 'Optional

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Status
    owner: Study
    domain_of:
    - Study
    - Standard
    range: name
  DescriptionRef:
    name: DescriptionRef
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
    owner: Study
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
  MetaDataVersionRefRef:
    name: MetaDataVersionRefRef
    description: 'MetaDataVersionRef reference: A reference to a MetaDataVersion used
      at the containing Location. The EffectiveDate reflects the possibility that
      the metadata may change over the course of the study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: MetaDataVersionRefRef
    owner: Study
    domain_of:
    - Study
    - Location
    range: MetaDataVersion
    inlined: true
    inlined_as_list: true
class_uri: odm:Study

```
</details>