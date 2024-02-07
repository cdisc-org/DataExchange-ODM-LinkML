# Class: Study

_This element collects static structural information about an individual study._




URI: [odm:Study](http://www.cdisc.org/ns/odm/v2.0/Study)


```mermaid
erDiagram
Study {
    oid OID  
    nameType studyName  
    nameType protocolName  
    nameType versionID  
    nameType versionName  
    nameType status  
}
MetaDataVersion {
    oid OID  
    nameType name  
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
    nameType name  
    MethodType type  
}
ConditionDef {
    oid OID  
    nameType name  
}
CodeList {
    oid OID  
    nameType name  
    CLDataType dataType  
    YesOnly isNonStandard  
}
ItemDef {
    oid OID  
    nameType name  
    DataType dataType  
    positiveInteger length  
    text displayFormat  
    text variableSet  
}
ItemGroupDef {
    oid OID  
    nameType name  
    ItemGroupRepeatingType repeating  
    positiveInteger repeatingLimit  
    YesOrNo isReferenceData  
    text structure  
    nameType datasetName  
    text domain  
    ItemGroupTypeType type  
    text purpose  
    YesOnly isNonStandard  
    YesOnly hasNoData  
}
StudyEventDef {
    oid OID  
    nameType name  
    YesOrNo repeating  
    EventType type  
    text category  
}
StudyEventGroupDef {
    oid OID  
    nameType name  
}
WorkflowDef {
    oid OID  
    nameType name  
}
Protocol {

}
WhereClauseDef {
    oid OID  
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
    uriorcurie href  
}
Description {

}

Study ||--|o Description : "description"
Study ||--}o MetaDataVersion : "metaDataVersion"
MetaDataVersion ||--|o CommentDef : "commentOID"
MetaDataVersion ||--|o Description : "description"
MetaDataVersion ||--|o Include : "include"
MetaDataVersion ||--|o Standards : "standards"
MetaDataVersion ||--|o AnnotatedCRF : "annotatedCRF"
MetaDataVersion ||--|o SupplementalDoc : "supplementalDoc"
MetaDataVersion ||--}o ValueListDef : "valueListDef"
MetaDataVersion ||--}o WhereClauseDef : "whereClauseDef"
MetaDataVersion ||--|o Protocol : "protocol"
MetaDataVersion ||--}o WorkflowDef : "workflowDef"
MetaDataVersion ||--}o StudyEventGroupDef : "studyEventGroupDef"
MetaDataVersion ||--}o StudyEventDef : "studyEventDef"
MetaDataVersion ||--}o ItemGroupDef : "itemGroupDef"
MetaDataVersion ||--}o ItemDef : "itemDef"
MetaDataVersion ||--}o CodeList : "codeList"
MetaDataVersion ||--}o ConditionDef : "conditionDef"
MetaDataVersion ||--}o MethodDef : "methodDef"
MetaDataVersion ||--}o CommentDef : "commentDef"
MetaDataVersion ||--}o Leaf : "leaf"
Leaf ||--|o Title : "title"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"
MethodDef ||--|o CommentDef : "commentOID"
MethodDef ||--|o Description : "description"
MethodDef ||--|o MethodSignature : "methodSignature"
MethodDef ||--}o FormalExpression : "formalExpression"
MethodDef ||--}o Alias : "alias"
MethodDef ||--}o DocumentRef : "documentRef"
ConditionDef ||--|o CommentDef : "commentOID"
ConditionDef ||--|o Description : "description"
ConditionDef ||--|o MethodSignature : "methodSignature"
ConditionDef ||--}o FormalExpression : "formalExpression"
ConditionDef ||--}o Alias : "alias"
CodeList ||--|o CommentDef : "commentOID"
CodeList ||--|o Standard : "standardOID"
CodeList ||--|o Description : "description"
CodeList ||--}o CodeListItem : "codeListItem"
CodeList ||--}o Coding : "coding"
CodeList ||--}o Alias : "alias"
ItemDef ||--|o CommentDef : "commentOID"
ItemDef ||--|o Description : "description"
ItemDef ||--|o Definition : "definition"
ItemDef ||--|o Question : "question"
ItemDef ||--|o Prompt : "prompt"
ItemDef ||--|o CRFCompletionInstructions : "cRFCompletionInstructions"
ItemDef ||--|o ImplementationNotes : "implementationNotes"
ItemDef ||--|o CDISCNotes : "cDISCNotes"
ItemDef ||--}o RangeCheck : "rangeCheck"
ItemDef ||--|o CodeListRef : "codeListRef"
ItemDef ||--|o ValueListRef : "valueListRef"
ItemDef ||--}o Coding : "coding"
ItemDef ||--}o Alias : "alias"
ItemGroupDef ||--|o Leaf : "archiveLocationID"
ItemGroupDef ||--|o Standard : "standardOID"
ItemGroupDef ||--|o CommentDef : "commentOID"
ItemGroupDef ||--|o Description : "description"
ItemGroupDef ||--|o Class : "itemGroupClass"
ItemGroupDef ||--}o Coding : "coding"
ItemGroupDef ||--|o WorkflowRef : "workflowRef"
ItemGroupDef ||--}o Origin : "origin"
ItemGroupDef ||--}o Alias : "alias"
ItemGroupDef ||--|o Leaf : "leaf"
ItemGroupDef ||--}o ItemGroupRef : "itemGroupRef"
ItemGroupDef ||--}o ItemRef : "itemRef"
StudyEventDef ||--|o CommentDef : "commentOID"
StudyEventDef ||--|o Description : "description"
StudyEventDef ||--}o ItemGroupRef : "itemGroupRef"
StudyEventDef ||--|o WorkflowRef : "workflowRef"
StudyEventDef ||--}o Coding : "coding"
StudyEventDef ||--}o Alias : "alias"
StudyEventGroupDef ||--|o Arm : "armOID"
StudyEventGroupDef ||--|o Epoch : "epochOID"
StudyEventGroupDef ||--|o CommentDef : "commentOID"
StudyEventGroupDef ||--|o Description : "description"
StudyEventGroupDef ||--|o WorkflowRef : "workflowRef"
StudyEventGroupDef ||--}o Coding : "coding"
StudyEventGroupDef ||--}o StudyEventGroupRef : "studyEventGroupRef"
StudyEventGroupDef ||--}o StudyEventRef : "studyEventRef"
WorkflowDef ||--|o Description : "description"
WorkflowDef ||--|o WorkflowStart : "workflowStart"
WorkflowDef ||--}o WorkflowEnd : "workflowEnd"
WorkflowDef ||--}o Transition : "transition"
WorkflowDef ||--}o Branching : "branching"
Protocol ||--|o Description : "description"
Protocol ||--|o StudySummary : "studySummary"
Protocol ||--|o StudyStructure : "studyStructure"
Protocol ||--|o TrialPhase : "trialPhase"
Protocol ||--|o StudyTimings : "studyTimings"
Protocol ||--|o StudyIndications : "studyIndications"
Protocol ||--|o StudyInterventions : "studyInterventions"
Protocol ||--|o StudyObjectives : "studyObjectives"
Protocol ||--|o StudyEndPoints : "studyEndPoints"
Protocol ||--|o StudyTargetPopulation : "studyTargetPopulation"
Protocol ||--|o StudyEstimands : "studyEstimands"
Protocol ||--|o InclusionExclusionCriteria : "inclusionExclusionCriteria"
Protocol ||--}o StudyEventGroupRef : "studyEventGroupRef"
Protocol ||--|o WorkflowRef : "workflowRef"
Protocol ||--}o Alias : "alias"
WhereClauseDef ||--|o CommentDef : "commentOID"
WhereClauseDef ||--}o RangeCheck : "rangeCheck"
ValueListDef ||--|o Description : "description"
ValueListDef ||--}o ItemRef : "itemRef"
SupplementalDoc ||--}o DocumentRef : "documentRef"
AnnotatedCRF ||--}o DocumentRef : "documentRef"
Standards ||--}o Standard : "standard"
Include ||--|| Study : "studyOID"
Include ||--|| MetaDataVersion : "metaDataVersionOID"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier for the study. | direct |
| [studyName](studyName.md) | 1..1 <br/> [nameType](nameType.md) | Sponsoring organization's internal name for the study. If no internal name is... | direct |
| [protocolName](protocolName.md) | 1..1 <br/> [nameType](nameType.md) | Protocol identifier or protocol number assigned to the study. It is used by t... | direct |
| [versionID](versionID.md) | 0..1 <br/> [nameType](nameType.md) | Identifier for the specific version of the study in the source system that th... | direct |
| [versionName](versionName.md) | 0..1 <br/> [nameType](nameType.md) | Short descriptive label for the version of the study, e.g. "Initial go live" ... | direct |
| [status](status.md) | 0..1 <br/> [nameType](nameType.md) | Represents the workflow status for the version of the study with content incl... | direct |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [metaDataVersion](metaDataVersion.md) | 0..* <br/> [MetaDataVersion](MetaDataVersion.md) | MetaDataVersion reference: The metadata for a study is defined in a series of... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Include](Include.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [SourceItem](SourceItem.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [AdminData](AdminData.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [MetaDataVersionRef](MetaDataVersionRef.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [ReferenceData](ReferenceData.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [ClinicalData](ClinicalData.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [Association](Association.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [KeySet](KeySet.md) | [studyOID](studyOID.md) | range | [Study](Study.md) |
| [ODMFileMetadata](ODMFileMetadata.md) | [study](study.md) | range | [Study](Study.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Study](https://wiki.cdisc.org/display/PUB/Study)

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
- https://wiki.cdisc.org/display/PUB/Study
rank: 1000
slots:
- OID
- studyName
- protocolName
- versionID
- versionName
- status
- description
- metaDataVersion
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the study.
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
  studyName:
    name: studyName
    description: Sponsoring organization's internal name for the study. If no internal
      name is available, the value is expected to be the same value as ProtocolName.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: nameType
    required: true
  protocolName:
    name: protocolName
    description: Protocol identifier or protocol number assigned to the study. It
      is used by the regulatory authority or clinical trial registry.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: nameType
    required: true
  versionID:
    name: versionID
    description: Identifier for the specific version of the study in the source system
      that the enclosed Study element metadata refers to.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: nameType
  versionName:
    name: versionName
    description: Short descriptive label for the version of the study, e.g. "Initial
      go live" when VersionID = "<study version ID for Initial go live>". VersionName
      may be provided when a VersionID is provided.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: nameType
  status:
    name: status
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
    range: nameType
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
  metaDataVersion:
    name: metaDataVersion
    multivalued: true
    domain_of:
    - Study
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
- https://wiki.cdisc.org/display/PUB/Study
rank: 1000
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the study.
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
  studyName:
    name: studyName
    description: Sponsoring organization's internal name for the study. If no internal
      name is available, the value is expected to be the same value as ProtocolName.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: nameType
    required: true
  protocolName:
    name: protocolName
    description: Protocol identifier or protocol number assigned to the study. It
      is used by the regulatory authority or clinical trial registry.
    comments:
    - 'Required

      range: name'
    domain_of:
    - Study
    range: nameType
    required: true
  versionID:
    name: versionID
    description: Identifier for the specific version of the study in the source system
      that the enclosed Study element metadata refers to.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: nameType
  versionName:
    name: versionName
    description: Short descriptive label for the version of the study, e.g. "Initial
      go live" when VersionID = "<study version ID for Initial go live>". VersionName
      may be provided when a VersionID is provided.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Study
    range: nameType
  status:
    name: status
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
    range: nameType
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
  metaDataVersion:
    name: metaDataVersion
    multivalued: true
    domain_of:
    - Study
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
  studyName:
    name: studyName
    description: Sponsoring organization's internal name for the study. If no internal
      name is available, the value is expected to be the same value as ProtocolName.
    comments:
    - 'Required

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyName
    owner: Study
    domain_of:
    - Study
    range: nameType
    required: true
  protocolName:
    name: protocolName
    description: Protocol identifier or protocol number assigned to the study. It
      is used by the regulatory authority or clinical trial registry.
    comments:
    - 'Required

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: protocolName
    owner: Study
    domain_of:
    - Study
    range: nameType
    required: true
  versionID:
    name: versionID
    description: Identifier for the specific version of the study in the source system
      that the enclosed Study element metadata refers to.
    comments:
    - 'Optional

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: versionID
    owner: Study
    domain_of:
    - Study
    range: nameType
  versionName:
    name: versionName
    description: Short descriptive label for the version of the study, e.g. "Initial
      go live" when VersionID = "<study version ID for Initial go live>". VersionName
      may be provided when a VersionID is provided.
    comments:
    - 'Optional

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: versionName
    owner: Study
    domain_of:
    - Study
    range: nameType
  status:
    name: status
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
    alias: status
    owner: Study
    domain_of:
    - Study
    - Standard
    range: nameType
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: description
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
  metaDataVersion:
    name: metaDataVersion
    description: 'MetaDataVersion reference: The metadata for a study is defined in
      a series of MetaDataVersion elements. Through this mechanism (multiple MetaDataVersion
      elements), the model supports the incremental deployment of "mid-stream study
      changes," and thus can handle a situation where multiple versions of the metadata
      are being used simultaneously (e.g., due to delays in IRB approval at various
      sites).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: metaDataVersion
    owner: Study
    domain_of:
    - Study
    range: MetaDataVersion
    inlined: true
    inlined_as_list: true
class_uri: odm:Study

```
</details>