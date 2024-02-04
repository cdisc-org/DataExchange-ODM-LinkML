# Class: MetaDataVersion

_The metadata for a study is defined in a series of MetaDataVersion elements. Through this mechanism (multiple MetaDataVersion elements), the model supports the incremental deployment of "mid-stream study changes," and thus can handle a situation where multiple versions of the metadata are being used simultaneously (e.g., due to delays in IRB approval at various sites)._




URI: [odm:MetaDataVersion](http://www.cdisc.org/ns/odm/v2.0/MetaDataVersion)


```mermaid
erDiagram
MetaDataVersion {
    oid OID  
    nameType name  
}
Leaf {
    oid ID  
    uriorcurie href  
}
Title {
    text content  
}
CommentDef {
    oid OID  
}
DocumentRef {
    oid leafID  
}
Description {

}
MethodDef {
    oid OID  
    nameType name  
    MethodType type  
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
Coding {
    text code  
    uriorcurie system  
    text systemName  
    text systemVersion  
    text label  
    uriorcurie href  
    uriorcurie ref  
    text commentOID  
}
CodeListItem {
    valueType codedValue  
    decimal rank  
    YesOnly other  
    positiveInteger orderNumber  
    YesOnly extendedValue  
}
Standard {
    oid OID  
    StandardName name  
    StandardType type  
    StandardPublishingSet publishingSet  
    text version  
    StandardStatus status  
}
ItemDef {
    oid OID  
    nameType name  
    DataType dataType  
    positiveInteger length  
    text displayFormat  
    text variableSet  
}
ValueListRef {

}
CodeListRef {

}
RangeCheck {
    Comparator comparator  
    SoftOrHard softHard  
}
CDISCNotes {

}
ImplementationNotes {

}
CRFCompletionInstructions {

}
Prompt {

}
Question {

}
Definition {

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
ItemRef {
    positiveInteger keySequence  
    YesOnly isNonStandard  
    YesOnly hasNoData  
    YesOnly repeat  
    YesOnly other  
    text role  
    CoreType core  
    text preSpecifiedValue  
    positiveInteger orderNumber  
    YesOrNo mandatory  
}
ItemGroupRef {
    positiveInteger orderNumber  
    YesOrNo mandatory  
}
Origin {
    OriginType type  
    OriginSource source  
}
WorkflowRef {

}
Class {
    ItemGroupClass name  
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
StudyEventRef {
    positiveInteger orderNumber  
    YesOrNo mandatory  
}
StudyEventGroupRef {
    positiveInteger orderNumber  
    YesOrNo mandatory  
}
Epoch {
    oid OID  
    nameType name  
    positiveInteger sequenceNumber  
}
Arm {
    oid OID  
    nameType name  
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
Protocol {

}
InclusionExclusionCriteria {

}
StudyEstimands {

}
StudyTargetPopulation {
    oid OID  
    nameType name  
}
StudyEndPoints {

}
StudyObjectives {

}
StudyInterventions {

}
StudyIndications {

}
StudyTimings {

}
TrialPhase {
    TrialPhaseType value  
}
StudyStructure {

}
StudySummary {

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
Study {
    oid OID  
    nameType studyName  
    nameType protocolName  
    nameType versionID  
    nameType versionName  
    nameType status  
}

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
DocumentRef ||--}o PDFPageRef : "pDFPageRef"
Description ||--}o TranslatedText : "translatedText"
MethodDef ||--|o CommentDef : "commentOID"
MethodDef ||--|o Description : "description"
MethodDef ||--|o MethodSignature : "methodSignature"
MethodDef ||--}o FormalExpression : "formalExpression"
MethodDef ||--}o Alias : "alias"
MethodDef ||--}o DocumentRef : "documentRef"
FormalExpression ||--|o Code : "code"
FormalExpression ||--|o ExternalCodeLib : "externalCodeLib"
MethodSignature ||--}o Parameter : "parameter"
MethodSignature ||--}o ReturnValue : "returnValue"
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
CodeListItem ||--|o CommentDef : "commentOID"
CodeListItem ||--|o Description : "description"
CodeListItem ||--|o Decode : "decode"
CodeListItem ||--}o Coding : "coding"
CodeListItem ||--}o Alias : "alias"
Standard ||--|o CommentDef : "commentOID"
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
ValueListRef ||--|| ValueListDef : "valueListOID"
CodeListRef ||--|| CodeList : "codeListOID"
RangeCheck ||--|o ItemDef : "itemOID"
RangeCheck ||--|o ErrorMessage : "errorMessage"
RangeCheck ||--|o MethodSignature : "methodSignature"
RangeCheck ||--}o FormalExpression : "formalExpression"
RangeCheck ||--}o CheckValue : "checkValue"
CDISCNotes ||--}o TranslatedText : "translatedText"
ImplementationNotes ||--}o TranslatedText : "translatedText"
CRFCompletionInstructions ||--}o TranslatedText : "translatedText"
Prompt ||--}o TranslatedText : "translatedText"
Question ||--}o TranslatedText : "translatedText"
Definition ||--}o TranslatedText : "translatedText"
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
ItemRef ||--|| ItemDef : "itemOID"
ItemRef ||--|o MethodDef : "methodOID"
ItemRef ||--|o ItemDef : "unitsItemOID"
ItemRef ||--|o CodeList : "roleCodeListOID"
ItemRef ||--|o ConditionDef : "collectionExceptionConditionOID"
ItemRef ||--}o Origin : "origin"
ItemRef ||--}o WhereClauseRef : "whereClauseRef"
ItemGroupRef ||--|| ItemGroupDef : "itemGroupOID"
ItemGroupRef ||--|o MethodDef : "methodOID"
ItemGroupRef ||--|o ConditionDef : "collectionExceptionConditionOID"
Origin ||--|o Description : "description"
Origin ||--|o SourceItems : "sourceItems"
Origin ||--}o Coding : "coding"
Origin ||--}o DocumentRef : "documentRef"
WorkflowRef ||--|| WorkflowDef : "workflowOID"
Class ||--}o SubClass : "subClass"
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
StudyEventRef ||--|| StudyEventDef : "studyEventOID"
StudyEventRef ||--|o ConditionDef : "collectionExceptionConditionOID"
StudyEventGroupRef ||--|| StudyEventGroupDef : "studyEventGroupOID"
StudyEventGroupRef ||--|o ConditionDef : "collectionExceptionConditionOID"
StudyEventGroupRef ||--|o Description : "description"
Epoch ||--|o Description : "description"
Arm ||--|o Description : "description"
Arm ||--|o WorkflowRef : "workflowRef"
WorkflowDef ||--|o Description : "description"
WorkflowDef ||--|o WorkflowStart : "workflowStart"
WorkflowDef ||--}o WorkflowEnd : "workflowEnd"
WorkflowDef ||--}o Transition : "transition"
WorkflowDef ||--}o Branching : "branching"
Branching ||--}o TargetTransition : "targetTransition"
Branching ||--}o DefaultTransition : "defaultTransition"
Transition ||--|o ConditionDef : "startConditionOID"
Transition ||--|o ConditionDef : "endConditionOID"
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
InclusionExclusionCriteria ||--|o InclusionCriteria : "inclusionCriteria"
InclusionExclusionCriteria ||--|o ExclusionCriteria : "exclusionCriteria"
StudyEstimands ||--}o StudyEstimand : "studyEstimand"
StudyTargetPopulation ||--|o Description : "description"
StudyTargetPopulation ||--}o Coding : "coding"
StudyTargetPopulation ||--}o FormalExpression : "formalExpression"
StudyEndPoints ||--}o StudyEndPoint : "studyEndPoint"
StudyObjectives ||--}o StudyObjective : "studyObjective"
StudyInterventions ||--}o StudyIntervention : "studyIntervention"
StudyIndications ||--}o StudyIndication : "studyIndication"
StudyTimings ||--}o StudyTiming : "studyTiming"
TrialPhase ||--|o Description : "description"
StudyStructure ||--|o Description : "description"
StudyStructure ||--}o Arm : "arm"
StudyStructure ||--}o Epoch : "epoch"
StudyStructure ||--|o WorkflowRef : "workflowRef"
StudySummary ||--}o StudyParameter : "studyParameter"
WhereClauseDef ||--|o CommentDef : "commentOID"
WhereClauseDef ||--}o RangeCheck : "rangeCheck"
ValueListDef ||--|o Description : "description"
ValueListDef ||--}o ItemRef : "itemRef"
SupplementalDoc ||--}o DocumentRef : "documentRef"
AnnotatedCRF ||--}o DocumentRef : "documentRef"
Standards ||--}o Standard : "standard"
Include ||--|| Study : "studyOID"
Include ||--|| MetaDataVersion : "metaDataVersionOID"
Study ||--|o Description : "description"
Study ||--}o MetaDataVersion : "metaDataVersion"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier. | direct |
| [name](name.md) | 1..1 <br/> [nameType](nameType.md) | MetaDataVersion name. | direct |
| [commentOID](commentOID.md) | 0..1 <br/> [CommentDef](CommentDef.md) | Reference to a CommentDef element. | direct |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [include](include.md) | 0..1 <br/> [Include](Include.md) | Include reference: The Include metadata element allows a reference to a prior... | direct |
| [standards](standards.md) | 0..1 <br/> [Standards](Standards.md) | Standards reference: The Standards element provides a container for the list ... | direct |
| [annotatedCRF](annotatedCRF.md) | 0..1 <br/> [AnnotatedCRF](AnnotatedCRF.md) | AnnotatedCRF reference: An Annotated Case Report Form (CRF) is a Portable Fil... | direct |
| [supplementalDoc](supplementalDoc.md) | 0..1 <br/> [SupplementalDoc](SupplementalDoc.md) | SupplementalDoc reference: Supplemental data definitions | direct |
| [valueListDef](valueListDef.md) | 0..* <br/> [ValueListDef](ValueListDef.md) | ValueListDef reference: The following table specifies the XML structure for v... | direct |
| [whereClauseDef](whereClauseDef.md) | 0..* <br/> [WhereClauseDef](WhereClauseDef.md) | WhereClauseDef reference: The WhereClauseDef element specifies a condition. | direct |
| [protocol](protocol.md) | 0..1 <br/> [Protocol](Protocol.md) | Protocol reference: The Protocol element lists the kinds of study events that... | direct |
| [workflowDef](workflowDef.md) | 0..* <br/> [WorkflowDef](WorkflowDef.md) | WorkflowDef reference: A WorkflowDef defines an automated workflow for a stud... | direct |
| [studyEventGroupDef](studyEventGroupDef.md) | 0..* <br/> [StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef reference: StudyEventGroupDef is a study building block th... | direct |
| [studyEventDef](studyEventDef.md) | 0..* <br/> [StudyEventDef](StudyEventDef.md) | StudyEventDef reference: StudyEventDef represents the definition of an activi... | direct |
| [itemGroupDef](itemGroupDef.md) | 0..* <br/> [ItemGroupDef](ItemGroupDef.md) | ItemGroupDef reference: An ItemGroupDef describes a type of variable or field... | direct |
| [itemDef](itemDef.md) | 0..* <br/> [ItemDef](ItemDef.md) | ItemDef reference: An ItemDef describes a type of item that can occur within ... | direct |
| [codeList](codeList.md) | 0..* <br/> [CodeList](CodeList.md) | CodeList reference: Defines a discrete set of permitted values for an item, o... | direct |
| [conditionDef](conditionDef.md) | 0..* <br/> [ConditionDef](ConditionDef.md) | ConditionDef reference: A ConditionDef defines a boolean condition. | direct |
| [methodDef](methodDef.md) | 0..* <br/> [MethodDef](MethodDef.md) | MethodDef reference: A MethodDef defines how a data value can be obtained fro... | direct |
| [commentDef](commentDef.md) | 0..* <br/> [CommentDef](CommentDef.md) | CommentDef reference: The Comment element allows referencing short comments s... | direct |
| [leaf](leaf.md) | 0..* <br/> [Leaf](Leaf.md) | Leaf reference: Contains the XLink information referenced by DocumentRef or A... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [metaDataVersion](metaDataVersion.md) | range | [MetaDataVersion](MetaDataVersion.md) |
| [Include](Include.md) | [metaDataVersionOID](metaDataVersionOID.md) | range | [MetaDataVersion](MetaDataVersion.md) |
| [SourceItem](SourceItem.md) | [metaDataVersionOID](metaDataVersionOID.md) | range | [MetaDataVersion](MetaDataVersion.md) |
| [MetaDataVersionRef](MetaDataVersionRef.md) | [metaDataVersionOID](metaDataVersionOID.md) | range | [MetaDataVersion](MetaDataVersion.md) |
| [ReferenceData](ReferenceData.md) | [metaDataVersionOID](metaDataVersionOID.md) | range | [MetaDataVersion](MetaDataVersion.md) |
| [ClinicalData](ClinicalData.md) | [metaDataVersionOID](metaDataVersionOID.md) | range | [MetaDataVersion](MetaDataVersion.md) |
| [Association](Association.md) | [metaDataVersionOID](metaDataVersionOID.md) | range | [MetaDataVersion](MetaDataVersion.md) |
| [KeySet](KeySet.md) | [metaDataVersionOID](metaDataVersionOID.md) | range | [MetaDataVersion](MetaDataVersion.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/MetaDataVersion](https://wiki.cdisc.org/display/PUB/MetaDataVersion)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:MetaDataVersion |
| native | odm:MetaDataVersion |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MetaDataVersion
description: The metadata for a study is defined in a series of MetaDataVersion elements.
  Through this mechanism (multiple MetaDataVersion elements), the model supports the
  incremental deployment of "mid-stream study changes," and thus can handle a situation
  where multiple versions of the metadata are being used simultaneously (e.g., due
  to delays in IRB approval at various sites).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/MetaDataVersion
rank: 1000
slots:
- OID
- name
- commentOID
- description
- include
- standards
- annotatedCRF
- supplementalDoc
- valueListDef
- whereClauseDef
- protocol
- workflowDef
- studyEventGroupDef
- studyEventDef
- itemGroupDef
- itemDef
- codeList
- conditionDef
- methodDef
- commentDef
- leaf
slot_usage:
  OID:
    name: OID
    description: Unique identifier.
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
    description: MetaDataVersion name.
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
  commentOID:
    name: commentOID
    description: Reference to a CommentDef element.
    comments:
    - 'Optional

      range: oidref'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: CommentDef
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
  include:
    name: include
    domain_of:
    - MetaDataVersion
    range: Include
    maximum_cardinality: 1
  standards:
    name: standards
    domain_of:
    - MetaDataVersion
    range: Standards
    maximum_cardinality: 1
  annotatedCRF:
    name: annotatedCRF
    domain_of:
    - MetaDataVersion
    range: AnnotatedCRF
    maximum_cardinality: 1
  supplementalDoc:
    name: supplementalDoc
    domain_of:
    - MetaDataVersion
    range: SupplementalDoc
    maximum_cardinality: 1
  valueListDef:
    name: valueListDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ValueListDef
    inlined: true
    inlined_as_list: true
  whereClauseDef:
    name: whereClauseDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WhereClauseDef
    inlined: true
    inlined_as_list: true
  protocol:
    name: protocol
    domain_of:
    - MetaDataVersion
    range: Protocol
    maximum_cardinality: 1
  workflowDef:
    name: workflowDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WorkflowDef
    inlined: true
    inlined_as_list: true
  studyEventGroupDef:
    name: studyEventGroupDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventGroupDef
    inlined: true
    inlined_as_list: true
  studyEventDef:
    name: studyEventDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventDef
    inlined: true
    inlined_as_list: true
  itemGroupDef:
    name: itemGroupDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemGroupDef
    inlined: true
    inlined_as_list: true
  itemDef:
    name: itemDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemDef
    inlined: true
    inlined_as_list: true
  codeList:
    name: codeList
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: CodeList
    inlined: true
    inlined_as_list: true
  conditionDef:
    name: conditionDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ConditionDef
    inlined: true
    inlined_as_list: true
  methodDef:
    name: methodDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: MethodDef
    inlined: true
    inlined_as_list: true
  commentDef:
    name: commentDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: CommentDef
    inlined: true
    inlined_as_list: true
  leaf:
    name: leaf
    multivalued: true
    domain_of:
    - MetaDataVersion
    - ItemGroupDef
    range: Leaf
    inlined: true
    inlined_as_list: true
class_uri: odm:MetaDataVersion

```
</details>

### Induced

<details>
```yaml
name: MetaDataVersion
description: The metadata for a study is defined in a series of MetaDataVersion elements.
  Through this mechanism (multiple MetaDataVersion elements), the model supports the
  incremental deployment of "mid-stream study changes," and thus can handle a situation
  where multiple versions of the metadata are being used simultaneously (e.g., due
  to delays in IRB approval at various sites).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/MetaDataVersion
rank: 1000
slot_usage:
  OID:
    name: OID
    description: Unique identifier.
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
    description: MetaDataVersion name.
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
  commentOID:
    name: commentOID
    description: Reference to a CommentDef element.
    comments:
    - 'Optional

      range: oidref'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: CommentDef
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
  include:
    name: include
    domain_of:
    - MetaDataVersion
    range: Include
    maximum_cardinality: 1
  standards:
    name: standards
    domain_of:
    - MetaDataVersion
    range: Standards
    maximum_cardinality: 1
  annotatedCRF:
    name: annotatedCRF
    domain_of:
    - MetaDataVersion
    range: AnnotatedCRF
    maximum_cardinality: 1
  supplementalDoc:
    name: supplementalDoc
    domain_of:
    - MetaDataVersion
    range: SupplementalDoc
    maximum_cardinality: 1
  valueListDef:
    name: valueListDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ValueListDef
    inlined: true
    inlined_as_list: true
  whereClauseDef:
    name: whereClauseDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WhereClauseDef
    inlined: true
    inlined_as_list: true
  protocol:
    name: protocol
    domain_of:
    - MetaDataVersion
    range: Protocol
    maximum_cardinality: 1
  workflowDef:
    name: workflowDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WorkflowDef
    inlined: true
    inlined_as_list: true
  studyEventGroupDef:
    name: studyEventGroupDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventGroupDef
    inlined: true
    inlined_as_list: true
  studyEventDef:
    name: studyEventDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventDef
    inlined: true
    inlined_as_list: true
  itemGroupDef:
    name: itemGroupDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemGroupDef
    inlined: true
    inlined_as_list: true
  itemDef:
    name: itemDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemDef
    inlined: true
    inlined_as_list: true
  codeList:
    name: codeList
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: CodeList
    inlined: true
    inlined_as_list: true
  conditionDef:
    name: conditionDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ConditionDef
    inlined: true
    inlined_as_list: true
  methodDef:
    name: methodDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: MethodDef
    inlined: true
    inlined_as_list: true
  commentDef:
    name: commentDef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: CommentDef
    inlined: true
    inlined_as_list: true
  leaf:
    name: leaf
    multivalued: true
    domain_of:
    - MetaDataVersion
    - ItemGroupDef
    range: Leaf
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier.
    comments:
    - 'Required

      range: oid'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: MetaDataVersion
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
    description: MetaDataVersion name.
    comments:
    - 'Required

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: name
    owner: MetaDataVersion
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
  commentOID:
    name: commentOID
    description: Reference to a CommentDef element.
    comments:
    - 'Optional

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: commentOID
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: CommentDef
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: description
    owner: MetaDataVersion
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
  include:
    name: include
    description: 'Include reference: The Include metadata element allows a reference
      to a prior metadata version.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: include
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: Include
    maximum_cardinality: 1
  standards:
    name: standards
    description: 'Standards reference: The Standards element provides a container
      for the list of Standard elements referenced in the MetaDataVersion for the
      Study..'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: standards
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: Standards
    maximum_cardinality: 1
  annotatedCRF:
    name: annotatedCRF
    description: 'AnnotatedCRF reference: An Annotated Case Report Form (CRF) is a
      Portable File Format (PDF) document that provides the mapping of data collection
      fields to the variables or discrete variable values contained within the datasets.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: annotatedCRF
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: AnnotatedCRF
    maximum_cardinality: 1
  supplementalDoc:
    name: supplementalDoc
    description: 'SupplementalDoc reference: Supplemental data definitions'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: supplementalDoc
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: SupplementalDoc
    maximum_cardinality: 1
  valueListDef:
    name: valueListDef
    description: 'ValueListDef reference: The following table specifies the XML structure
      for valuelist metadata. The ValueListDef element contains ItemRef elements that
      reference ItemDef elements that provide the value-level metadata details'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: valueListDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ValueListDef
    inlined: true
    inlined_as_list: true
  whereClauseDef:
    name: whereClauseDef
    description: 'WhereClauseDef reference: The WhereClauseDef element specifies a
      condition.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: whereClauseDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: WhereClauseDef
    inlined: true
    inlined_as_list: true
  protocol:
    name: protocol
    description: 'Protocol reference: The Protocol element lists the kinds of study
      events that can occur within a specific version of a study. All clinical data
      must occur within one of these study events.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: protocol
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: Protocol
    maximum_cardinality: 1
  workflowDef:
    name: workflowDef
    description: 'WorkflowDef reference: A WorkflowDef defines an automated workflow
      for a study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: workflowDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: WorkflowDef
    inlined: true
    inlined_as_list: true
  studyEventGroupDef:
    name: studyEventGroupDef
    description: 'StudyEventGroupDef reference: StudyEventGroupDef is a study building
      block that groups a number of smaller building blocks, which can themselves
      be StudyEventGroups or StudyEvents. It thus allows nesting of building blocks.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: studyEventGroupDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: StudyEventGroupDef
    inlined: true
    inlined_as_list: true
  studyEventDef:
    name: studyEventDef
    description: 'StudyEventDef reference: StudyEventDef represents the definition
      of an activity in a study where data is collected. For example, a study event
      may represent a set of item groups that represent data collection instruments
      to be completed for a subject during a visit in a study. The visit occurs as
      part of a study workflow, and the workflow is referenced in the study event.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: studyEventDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: StudyEventDef
    inlined: true
    inlined_as_list: true
  itemGroupDef:
    name: itemGroupDef
    description: 'ItemGroupDef reference: An ItemGroupDef describes a type of variable
      or field grouping that can occur within a study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: itemGroupDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ItemGroupDef
    inlined: true
    inlined_as_list: true
  itemDef:
    name: itemDef
    description: 'ItemDef reference: An ItemDef describes a type of item that can
      occur within a study. Item properties include name, datatype, range, or codelist
      restrictions, and several other properties.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: itemDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ItemDef
    inlined: true
    inlined_as_list: true
  codeList:
    name: codeList
    description: 'CodeList reference: Defines a discrete set of permitted values for
      an item, or provides a reference to a codelist or dictionary maintained by an
      external organization via the Coding element, or a combination of both. Examples
      provided under Coding.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: codeList
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: CodeList
    inlined: true
    inlined_as_list: true
  conditionDef:
    name: conditionDef
    description: 'ConditionDef reference: A ConditionDef defines a boolean condition.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: conditionDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ConditionDef
    inlined: true
    inlined_as_list: true
  methodDef:
    name: methodDef
    description: 'MethodDef reference: A MethodDef defines how a data value can be
      obtained from a collection of other data values.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: methodDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: MethodDef
    inlined: true
    inlined_as_list: true
  commentDef:
    name: commentDef
    description: 'CommentDef reference: The Comment element allows referencing short
      comments self-contained in the XML document or long comments normally included
      in external documents. For comments included in external documents, the reference
      could include specific pages of a document where the comments are included.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: commentDef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: CommentDef
    inlined: true
    inlined_as_list: true
  leaf:
    name: leaf
    description: 'Leaf reference: Contains the XLink information referenced by DocumentRef
      or ArchiveLocationID'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: leaf
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    - ItemGroupDef
    range: Leaf
    inlined: true
    inlined_as_list: true
class_uri: odm:MetaDataVersion

```
</details>