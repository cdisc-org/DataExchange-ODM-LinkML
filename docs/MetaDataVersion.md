# Class: MetaDataVersion

_The metadata for a study is defined in a series of MetaDataVersion elements. Through this mechanism (multiple MetaDataVersion elements), the model supports the incremental deployment of "mid-stream study changes," and thus can handle a situation where multiple versions of the metadata are being used simultaneously (e.g., due to delays in IRB approval at various sites)._




URI: [odm:MetaDataVersion](http://www.cdisc.org/ns/odm/v2.0/MetaDataVersion)


```mermaid
erDiagram
MetaDataVersion {
    oid OID  
    name Name  
    oidref CommentOID  
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
    oid LeafID  
}
Description {

}
MethodDef {
    oid OID  
    name Name  
    MethodType Type  
    oidref CommentOID  
}
Alias {
    text ContextRef  
    text Name  
}
FormalExpression {
    text ContextRef  
}
MethodSignature {

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
Coding {
    text CodeRef  
    uriorcurie System  
    text SystemName  
    text SystemVersion  
    text Label  
    uriorcurie href  
    uriorcurie ref  
    text CommentOID  
}
CodeListItem {
    value CodedValue  
    decimal Rank  
    YesOnly Other  
    positiveInteger OrderNumber  
    YesOnly ExtendedValue  
    oidref CommentOID  
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
ValueListRef {
    oidref ValueListOID  
}
CodeListRef {
    oidref CodeListOID  
}
RangeCheck {
    Comparator ComparatorRef  
    SoftOrHard SoftHard  
    oidref ItemOID  
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
ItemRef {
    oidref ItemOID  
    positiveInteger KeySequence  
    YesOnly IsNonStandard  
    YesOnly HasNoData  
    oidref MethodOID  
    oidref UnitsItemOID  
    YesOnly Repeat  
    YesOnly Other  
    text Role  
    oidref RoleCodeListOID  
    CoreType Core  
    text PreSpecifiedValue  
    positiveInteger OrderNumber  
    YesOrNo Mandatory  
    oidref CollectionExceptionConditionOID  
}
ItemGroupRef {
    oidref ItemGroupOID  
    oidref MethodOID  
    positiveInteger OrderNumber  
    YesOrNo Mandatory  
    oidref CollectionExceptionConditionOID  
}
Origin {
    OriginType Type  
    OriginSource Source  
}
WorkflowRef {
    oidref WorkflowOID  
}
Class {
    ItemGroupClass Name  
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
StudyEventRef {
    oidref StudyEventOID  
    positiveInteger OrderNumber  
    YesOrNo Mandatory  
    oidref CollectionExceptionConditionOID  
}
StudyEventGroupRef {
    oidref StudyEventGroupOID  
    positiveInteger OrderNumber  
    YesOrNo Mandatory  
    oidref CollectionExceptionConditionOID  
}
WorkflowDef {
    oid OID  
    name Name  
}
Branching {
    oid OID  
    name Name  
    BranchingType Type  
}
Transition {
    oid OID  
    name Name  
    oidref SourceOID  
    oidref TargetOID  
    oidref StartConditionOID  
    oidref EndConditionOID  
}
WorkflowEnd {
    oidref EndOID  
    text content  
}
WorkflowStart {
    oidref StartOID  
}
Protocol {

}
InclusionExclusionCriteria {

}
StudyEstimands {

}
StudyTargetPopulation {
    oid OID  
    name Name  
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
    TrialPhaseType ValueRef  
}
StudyStructure {

}
StudySummary {

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
Standard {
    oid OID  
    StandardName Name  
    StandardType Type  
    StandardPublishingSet PublishingSet  
    text Version  
    StandardStatus Status  
    oidref CommentOID  
}
Include {
    oidref StudyOID  
    oidref MetaDataVersionOID  
    uriorcurie href  
}

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
DocumentRef ||--}o PDFPageRef : "PDFPageRefRef"
Description ||--}o TranslatedText : "TranslatedTextRef"
MethodDef ||--|o Description : "DescriptionRef"
MethodDef ||--|o MethodSignature : "MethodSignatureRef"
MethodDef ||--}o FormalExpression : "FormalExpressionRef"
MethodDef ||--}o Alias : "AliasRef"
MethodDef ||--}o DocumentRef : "DocumentRefRef"
FormalExpression ||--|o Code : "CodeRef"
FormalExpression ||--|o ExternalCodeLib : "ExternalCodeLibRef"
MethodSignature ||--}o Parameter : "ParameterRef"
MethodSignature ||--}o ReturnValue : "ReturnValueRef"
ConditionDef ||--|o Description : "DescriptionRef"
ConditionDef ||--|o MethodSignature : "MethodSignatureRef"
ConditionDef ||--}o FormalExpression : "FormalExpressionRef"
ConditionDef ||--}o Alias : "AliasRef"
CodeList ||--|o Description : "DescriptionRef"
CodeList ||--}o CodeListItem : "CodeListItemRef"
CodeList ||--}o Coding : "CodingRef"
CodeList ||--}o Alias : "AliasRef"
CodeListItem ||--|o Description : "DescriptionRef"
CodeListItem ||--|o Decode : "DecodeRef"
CodeListItem ||--}o Coding : "CodingRef"
CodeListItem ||--}o Alias : "AliasRef"
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
RangeCheck ||--|o ErrorMessage : "ErrorMessageRef"
RangeCheck ||--|o MethodSignature : "MethodSignatureRef"
RangeCheck ||--}o FormalExpression : "FormalExpressionRef"
RangeCheck ||--}o CheckValue : "CheckValueRef"
CDISCNotes ||--}o TranslatedText : "TranslatedTextRef"
ImplementationNotes ||--}o TranslatedText : "TranslatedTextRef"
CRFCompletionInstructions ||--}o TranslatedText : "TranslatedTextRef"
Prompt ||--}o TranslatedText : "TranslatedTextRef"
Question ||--}o TranslatedText : "TranslatedTextRef"
Definition ||--}o TranslatedText : "TranslatedTextRef"
ItemGroupDef ||--|o Description : "DescriptionRef"
ItemGroupDef ||--|o Class : "ClassRef"
ItemGroupDef ||--}o Coding : "CodingRef"
ItemGroupDef ||--|o WorkflowRef : "WorkflowRefRef"
ItemGroupDef ||--}o Origin : "OriginRef"
ItemGroupDef ||--}o Alias : "AliasRef"
ItemGroupDef ||--|o Leaf : "LeafRef"
ItemGroupDef ||--}o ItemGroupRef : "ItemGroupRefRef"
ItemGroupDef ||--}o ItemRef : "ItemRefRef"
ItemRef ||--}o Origin : "OriginRef"
ItemRef ||--}o WhereClauseRef : "WhereClauseRefRef"
Origin ||--|o Description : "DescriptionRef"
Origin ||--|o SourceItems : "SourceItemsRef"
Origin ||--}o Coding : "CodingRef"
Origin ||--}o DocumentRef : "DocumentRefRef"
Class ||--}o SubClass : "SubClassRef"
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
StudyEventGroupRef ||--|o Description : "DescriptionRef"
WorkflowDef ||--|o Description : "DescriptionRef"
WorkflowDef ||--|o WorkflowStart : "WorkflowStartRef"
WorkflowDef ||--}o WorkflowEnd : "WorkflowEndRef"
WorkflowDef ||--}o Transition : "TransitionRef"
WorkflowDef ||--}o Branching : "BranchingRef"
Branching ||--}o TargetTransition : "TargetTransitionRef"
Branching ||--}o DefaultTransition : "DefaultTransitionRef"
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
InclusionExclusionCriteria ||--|o InclusionCriteria : "InclusionCriteriaRef"
InclusionExclusionCriteria ||--|o ExclusionCriteria : "ExclusionCriteriaRef"
StudyEstimands ||--}o StudyEstimand : "StudyEstimandRef"
StudyTargetPopulation ||--|o Description : "DescriptionRef"
StudyTargetPopulation ||--}o Coding : "CodingRef"
StudyTargetPopulation ||--}o FormalExpression : "FormalExpressionRef"
StudyEndPoints ||--}o StudyEndPoint : "StudyEndPointRefRef"
StudyObjectives ||--}o StudyObjective : "StudyObjectiveRef"
StudyInterventions ||--}o StudyIntervention : "StudyInterventionRefRef"
StudyIndications ||--}o StudyIndication : "StudyIndicationRef"
StudyTimings ||--}o StudyTiming : "StudyTimingRef"
TrialPhase ||--|o Description : "DescriptionRef"
StudyStructure ||--|o Description : "DescriptionRef"
StudyStructure ||--}o Arm : "ArmRef"
StudyStructure ||--}o Epoch : "EpochRef"
StudyStructure ||--|o WorkflowRef : "WorkflowRefRef"
StudySummary ||--}o StudyParameter : "StudyParameterRef"
WhereClauseDef ||--}o RangeCheck : "RangeCheckRef"
ValueListDef ||--|o Description : "DescriptionRef"
ValueListDef ||--}o ItemRef : "ItemRefRef"
SupplementalDoc ||--}o DocumentRef : "DocumentRefRef"
AnnotatedCRF ||--}o DocumentRef : "DocumentRefRef"
Standards ||--}o Standard : "StandardRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier. | direct |
| [Name](Name.md) | 1..1 <br/> [name](name.md) | MetaDataVersion name. | direct |
| [CommentOID](CommentOID.md) | 0..1 <br/> [oidref](oidref.md) | Reference to a CommentDef element. | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [IncludeRef](IncludeRef.md) | 0..1 <br/> [Include](Include.md) | Include reference: The Include metadata element allows a reference to a prior... | direct |
| [StandardsRef](StandardsRef.md) | 0..1 <br/> [Standards](Standards.md) | Standards reference: The Standards element provides a container for the list ... | direct |
| [AnnotatedCRFRef](AnnotatedCRFRef.md) | 0..1 <br/> [AnnotatedCRF](AnnotatedCRF.md) | AnnotatedCRF reference: An Annotated Case Report Form (CRF) is a Portable Fil... | direct |
| [SupplementalDocRef](SupplementalDocRef.md) | 0..1 <br/> [SupplementalDoc](SupplementalDoc.md) | SupplementalDoc reference: Supplemental data definitions | direct |
| [ValueListDefRef](ValueListDefRef.md) | 0..* <br/> [ValueListDef](ValueListDef.md) | ValueListDef reference: The following table specifies the XML structure for v... | direct |
| [WhereClauseDefRef](WhereClauseDefRef.md) | 0..* <br/> [WhereClauseDef](WhereClauseDef.md) | WhereClauseDef reference: The WhereClauseDef element specifies a condition. | direct |
| [ProtocolRef](ProtocolRef.md) | 0..1 <br/> [Protocol](Protocol.md) | Protocol reference: The Protocol element lists the kinds of study events that... | direct |
| [WorkflowDefRef](WorkflowDefRef.md) | 0..* <br/> [WorkflowDef](WorkflowDef.md) | WorkflowDef reference: A WorkflowDef defines an automated workflow for a stud... | direct |
| [StudyEventGroupDefRef](StudyEventGroupDefRef.md) | 0..* <br/> [StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef reference: StudyEventGroupDef is a study building block th... | direct |
| [StudyEventDefRef](StudyEventDefRef.md) | 0..* <br/> [StudyEventDef](StudyEventDef.md) | StudyEventDef reference: StudyEventDef represents the definition of an activi... | direct |
| [ItemGroupDefRef](ItemGroupDefRef.md) | 0..* <br/> [ItemGroupDef](ItemGroupDef.md) | ItemGroupDef reference: An ItemGroupDef describes a type of variable or field... | direct |
| [ItemDefRef](ItemDefRef.md) | 0..* <br/> [ItemDef](ItemDef.md) | ItemDef reference: An ItemDef describes a type of item that can occur within ... | direct |
| [CodeListRefRef](CodeListRefRef.md) | 0..* <br/> [CodeList](CodeList.md) | CodeListRef reference: A reference to a CodeList definition. | direct |
| [ConditionDefRef](ConditionDefRef.md) | 0..* <br/> [ConditionDef](ConditionDef.md) | ConditionDef reference: A ConditionDef defines a boolean condition. | direct |
| [MethodDefRef](MethodDefRef.md) | 0..* <br/> [MethodDef](MethodDef.md) | MethodDef reference: A MethodDef defines how a data value can be obtained fro... | direct |
| [CommentDefRef](CommentDefRef.md) | 0..* <br/> [CommentDef](CommentDef.md) | CommentDef reference: The Comment element allows referencing short comments s... | direct |
| [LeafRef](LeafRef.md) | 0..* <br/> [Leaf](Leaf.md) | Leaf reference: Contains the XLink information referenced by DocumentRef or A... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [MetaDataVersionRefRef](MetaDataVersionRefRef.md) | range | [MetaDataVersion](MetaDataVersion.md) |






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
- Name
- CommentOID
- DescriptionRef
- IncludeRef
- StandardsRef
- AnnotatedCRFRef
- SupplementalDocRef
- ValueListDefRef
- WhereClauseDefRef
- ProtocolRef
- WorkflowDefRef
- StudyEventGroupDefRef
- StudyEventDefRef
- ItemGroupDefRef
- ItemDefRef
- CodeListRefRef
- ConditionDefRef
- MethodDefRef
- CommentDefRef
- LeafRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier.
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
  Name:
    name: Name
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
    range: name
    required: true
  CommentOID:
    name: CommentOID
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
    range: oidref
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
  IncludeRef:
    name: IncludeRef
    domain_of:
    - MetaDataVersion
    range: Include
    maximum_cardinality: 1
  StandardsRef:
    name: StandardsRef
    domain_of:
    - MetaDataVersion
    range: Standards
    maximum_cardinality: 1
  AnnotatedCRFRef:
    name: AnnotatedCRFRef
    domain_of:
    - MetaDataVersion
    range: AnnotatedCRF
    maximum_cardinality: 1
  SupplementalDocRef:
    name: SupplementalDocRef
    domain_of:
    - MetaDataVersion
    range: SupplementalDoc
    maximum_cardinality: 1
  ValueListDefRef:
    name: ValueListDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ValueListDef
    inlined: true
    inlined_as_list: true
  WhereClauseDefRef:
    name: WhereClauseDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WhereClauseDef
    inlined: true
    inlined_as_list: true
  ProtocolRef:
    name: ProtocolRef
    domain_of:
    - MetaDataVersion
    range: Protocol
    maximum_cardinality: 1
  WorkflowDefRef:
    name: WorkflowDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WorkflowDef
    inlined: true
    inlined_as_list: true
  StudyEventGroupDefRef:
    name: StudyEventGroupDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventGroupDef
    inlined: true
    inlined_as_list: true
  StudyEventDefRef:
    name: StudyEventDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventDef
    inlined: true
    inlined_as_list: true
  ItemGroupDefRef:
    name: ItemGroupDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemGroupDef
    inlined: true
    inlined_as_list: true
  ItemDefRef:
    name: ItemDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemDef
    inlined: true
    inlined_as_list: true
  CodeListRefRef:
    name: CodeListRefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    - ItemDef
    range: CodeList
    inlined: true
    inlined_as_list: true
  ConditionDefRef:
    name: ConditionDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ConditionDef
    inlined: true
    inlined_as_list: true
  MethodDefRef:
    name: MethodDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: MethodDef
    inlined: true
    inlined_as_list: true
  CommentDefRef:
    name: CommentDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: CommentDef
    inlined: true
    inlined_as_list: true
  LeafRef:
    name: LeafRef
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
  Name:
    name: Name
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
    range: name
    required: true
  CommentOID:
    name: CommentOID
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
    range: oidref
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
  IncludeRef:
    name: IncludeRef
    domain_of:
    - MetaDataVersion
    range: Include
    maximum_cardinality: 1
  StandardsRef:
    name: StandardsRef
    domain_of:
    - MetaDataVersion
    range: Standards
    maximum_cardinality: 1
  AnnotatedCRFRef:
    name: AnnotatedCRFRef
    domain_of:
    - MetaDataVersion
    range: AnnotatedCRF
    maximum_cardinality: 1
  SupplementalDocRef:
    name: SupplementalDocRef
    domain_of:
    - MetaDataVersion
    range: SupplementalDoc
    maximum_cardinality: 1
  ValueListDefRef:
    name: ValueListDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ValueListDef
    inlined: true
    inlined_as_list: true
  WhereClauseDefRef:
    name: WhereClauseDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WhereClauseDef
    inlined: true
    inlined_as_list: true
  ProtocolRef:
    name: ProtocolRef
    domain_of:
    - MetaDataVersion
    range: Protocol
    maximum_cardinality: 1
  WorkflowDefRef:
    name: WorkflowDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: WorkflowDef
    inlined: true
    inlined_as_list: true
  StudyEventGroupDefRef:
    name: StudyEventGroupDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventGroupDef
    inlined: true
    inlined_as_list: true
  StudyEventDefRef:
    name: StudyEventDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: StudyEventDef
    inlined: true
    inlined_as_list: true
  ItemGroupDefRef:
    name: ItemGroupDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemGroupDef
    inlined: true
    inlined_as_list: true
  ItemDefRef:
    name: ItemDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ItemDef
    inlined: true
    inlined_as_list: true
  CodeListRefRef:
    name: CodeListRefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    - ItemDef
    range: CodeList
    inlined: true
    inlined_as_list: true
  ConditionDefRef:
    name: ConditionDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: ConditionDef
    inlined: true
    inlined_as_list: true
  MethodDefRef:
    name: MethodDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: MethodDef
    inlined: true
    inlined_as_list: true
  CommentDefRef:
    name: CommentDefRef
    multivalued: true
    domain_of:
    - MetaDataVersion
    range: CommentDef
    inlined: true
    inlined_as_list: true
  LeafRef:
    name: LeafRef
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
  Name:
    name: Name
    description: MetaDataVersion name.
    comments:
    - 'Required

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
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
    range: name
    required: true
  CommentOID:
    name: CommentOID
    description: Reference to a CommentDef element.
    comments:
    - 'Optional

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CommentOID
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
    range: oidref
  DescriptionRef:
    name: DescriptionRef
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
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
  IncludeRef:
    name: IncludeRef
    description: 'Include reference: The Include metadata element allows a reference
      to a prior metadata version.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: IncludeRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: Include
    maximum_cardinality: 1
  StandardsRef:
    name: StandardsRef
    description: 'Standards reference: The Standards element provides a container
      for the list of Standard elements referenced in the MetaDataVersion for the
      Study..'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StandardsRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: Standards
    maximum_cardinality: 1
  AnnotatedCRFRef:
    name: AnnotatedCRFRef
    description: 'AnnotatedCRF reference: An Annotated Case Report Form (CRF) is a
      Portable File Format (PDF) document that provides the mapping of data collection
      fields to the variables or discrete variable values contained within the datasets.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: AnnotatedCRFRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: AnnotatedCRF
    maximum_cardinality: 1
  SupplementalDocRef:
    name: SupplementalDocRef
    description: 'SupplementalDoc reference: Supplemental data definitions'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SupplementalDocRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: SupplementalDoc
    maximum_cardinality: 1
  ValueListDefRef:
    name: ValueListDefRef
    description: 'ValueListDef reference: The following table specifies the XML structure
      for valuelist metadata. The ValueListDef element contains ItemRef elements that
      reference ItemDef elements that provide the value-level metadata details'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ValueListDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ValueListDef
    inlined: true
    inlined_as_list: true
  WhereClauseDefRef:
    name: WhereClauseDefRef
    description: 'WhereClauseDef reference: The WhereClauseDef element specifies a
      condition.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: WhereClauseDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: WhereClauseDef
    inlined: true
    inlined_as_list: true
  ProtocolRef:
    name: ProtocolRef
    description: 'Protocol reference: The Protocol element lists the kinds of study
      events that can occur within a specific version of a study. All clinical data
      must occur within one of these study events.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: ProtocolRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: Protocol
    maximum_cardinality: 1
  WorkflowDefRef:
    name: WorkflowDefRef
    description: 'WorkflowDef reference: A WorkflowDef defines an automated workflow
      for a study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: WorkflowDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: WorkflowDef
    inlined: true
    inlined_as_list: true
  StudyEventGroupDefRef:
    name: StudyEventGroupDefRef
    description: 'StudyEventGroupDef reference: StudyEventGroupDef is a study building
      block that groups a number of smaller building blocks, which can themselves
      be StudyEventGroups or StudyEvents. It thus allows nesting of building blocks.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: StudyEventGroupDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: StudyEventGroupDef
    inlined: true
    inlined_as_list: true
  StudyEventDefRef:
    name: StudyEventDefRef
    description: 'StudyEventDef reference: StudyEventDef represents the definition
      of an activity in a study where data is collected. For example, a study event
      may represent a set of item groups that represent data collection instruments
      to be completed for a subject during a visit in a study. The visit occurs as
      part of a study workflow, and the workflow is referenced in the study event.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: StudyEventDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: StudyEventDef
    inlined: true
    inlined_as_list: true
  ItemGroupDefRef:
    name: ItemGroupDefRef
    description: 'ItemGroupDef reference: An ItemGroupDef describes a type of variable
      or field grouping that can occur within a study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemGroupDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ItemGroupDef
    inlined: true
    inlined_as_list: true
  ItemDefRef:
    name: ItemDefRef
    description: 'ItemDef reference: An ItemDef describes a type of item that can
      occur within a study. Item properties include name, datatype, range, or codelist
      restrictions, and several other properties.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ItemDef
    inlined: true
    inlined_as_list: true
  CodeListRefRef:
    name: CodeListRefRef
    description: 'CodeListRef reference: A reference to a CodeList definition.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: CodeListRefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    - ItemDef
    range: CodeList
    inlined: true
    inlined_as_list: true
  ConditionDefRef:
    name: ConditionDefRef
    description: 'ConditionDef reference: A ConditionDef defines a boolean condition.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ConditionDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: ConditionDef
    inlined: true
    inlined_as_list: true
  MethodDefRef:
    name: MethodDefRef
    description: 'MethodDef reference: A MethodDef defines how a data value can be
      obtained from a collection of other data values.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: MethodDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: MethodDef
    inlined: true
    inlined_as_list: true
  CommentDefRef:
    name: CommentDefRef
    description: 'CommentDef reference: The Comment element allows referencing short
      comments self-contained in the XML document or long comments normally included
      in external documents. For comments included in external documents, the reference
      could include specific pages of a document where the comments are included.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: CommentDefRef
    owner: MetaDataVersion
    domain_of:
    - MetaDataVersion
    range: CommentDef
    inlined: true
    inlined_as_list: true
  LeafRef:
    name: LeafRef
    description: 'Leaf reference: Contains the XLink information referenced by DocumentRef
      or ArchiveLocationID'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: LeafRef
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