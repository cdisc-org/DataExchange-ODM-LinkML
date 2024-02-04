# Class: KeySet

_A KeySet references a single entity (e.g., a study, a subject, a study event). Only those attributes needed to specify the particular entity are required, and all others must be omitted (see Section 2.7, Clinical Data Keys)._




URI: [odm:KeySet](http://www.cdisc.org/ns/odm/v2.0/KeySet)


```mermaid
erDiagram
KeySet {
    subjectKeyType subjectKey  
    repeatKey studyEventRepeatKey  
    repeatKey itemGroupRepeatKey  
}
ItemDef {
    oid OID  
    nameType name  
    DataType dataType  
    positiveInteger length  
    text displayFormat  
    text variableSet  
}
Alias {
    text context  
    text name  
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
Description {

}
CommentDef {
    oid OID  
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
Leaf {
    oid ID  
    uriorcurie href  
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
Standard {
    oid OID  
    StandardName name  
    StandardType type  
    StandardPublishingSet publishingSet  
    text version  
    StandardStatus status  
}
StudyEventDef {
    oid OID  
    nameType name  
    YesOrNo repeating  
    EventType type  
    text category  
}
MetaDataVersion {
    oid OID  
    nameType name  
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
Study {
    oid OID  
    nameType studyName  
    nameType protocolName  
    nameType versionID  
    nameType versionName  
    nameType status  
}

KeySet ||--|| Study : "studyOID"
KeySet ||--|o MetaDataVersion : "metaDataVersionOID"
KeySet ||--|o StudyEventDef : "studyEventOID"
KeySet ||--|o ItemGroupDef : "itemGroupOID"
KeySet ||--|o ItemDef : "itemOID"
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
Description ||--}o TranslatedText : "translatedText"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"
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
Leaf ||--|o Title : "title"
Origin ||--|o Description : "description"
Origin ||--|o SourceItems : "sourceItems"
Origin ||--}o Coding : "coding"
Origin ||--}o DocumentRef : "documentRef"
WorkflowRef ||--|| WorkflowDef : "workflowOID"
Class ||--}o SubClass : "subClass"
Standard ||--|o CommentDef : "commentOID"
StudyEventDef ||--|o CommentDef : "commentOID"
StudyEventDef ||--|o Description : "description"
StudyEventDef ||--}o ItemGroupRef : "itemGroupRef"
StudyEventDef ||--|o WorkflowRef : "workflowRef"
StudyEventDef ||--}o Coding : "coding"
StudyEventDef ||--}o Alias : "alias"
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
Study ||--|o Description : "description"
Study ||--}o MetaDataVersion : "metaDataVersion"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyOID](studyOID.md) | 1..1 <br/> [Study](Study.md) | References the StudyOID in an ODM/ClinicalData element. | direct |
| [subjectKey](subjectKey.md) | 0..1 <br/> [subjectKeyType](subjectKeyType.md) | Reference to a SubjectKey attribute value for a SubjectData child element of ... | direct |
| [metaDataVersionOID](metaDataVersionOID.md) | 0..1 <br/> [MetaDataVersion](MetaDataVersion.md) | Reference to a MetaDataVersionOID attribute value for this ClinicalData eleme... | direct |
| [studyEventOID](studyEventOID.md) | 0..1 <br/> [StudyEventDef](StudyEventDef.md) | Reference to a StudyEventOID attribute value for a StudyEventData child eleme... | direct |
| [studyEventRepeatKey](studyEventRepeatKey.md) | 0..1 <br/> [repeatKey](repeatKey.md) | Reference to a StudyEventRepeatKey attribute value for a StudyEventData child... | direct |
| [itemGroupOID](itemGroupOID.md) | 0..1 <br/> [ItemGroupDef](ItemGroupDef.md) | Reference to an ItemGroupOID attribute value for an ItemGroupData child eleme... | direct |
| [itemGroupRepeatKey](itemGroupRepeatKey.md) | 0..1 <br/> [repeatKey](repeatKey.md) | Reference to an ItemGroupRepeatKey attribute value for an ItemGroupData child... | direct |
| [itemOID](itemOID.md) | 0..1 <br/> [ItemDef](ItemDef.md) | Reference to an ItemOID attribute for an ItemData child element of this Clini... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Association](Association.md) | [keySet](keySet.md) | range | [KeySet](KeySet.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/KeySet](https://wiki.cdisc.org/display/PUB/KeySet)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:KeySet |
| native | odm:KeySet |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KeySet
description: A KeySet references a single entity (e.g., a study, a subject, a study
  event). Only those attributes needed to specify the particular entity are required,
  and all others must be omitted (see Section 2.7, Clinical Data Keys).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/KeySet
rank: 1000
slots:
- studyOID
- subjectKey
- metaDataVersionOID
- studyEventOID
- studyEventRepeatKey
- itemGroupOID
- itemGroupRepeatKey
- itemOID
slot_usage:
  studyOID:
    name: studyOID
    description: References the StudyOID in an ODM/ClinicalData element.
    comments:
    - Matches the Association/@StudyOID.
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: Study
    required: true
  subjectKey:
    name: subjectKey
    description: Reference to a SubjectKey attribute value for a SubjectData child
      element of this ClinicalData element.
    comments:
    - 'Optional

      Matches the SubjectKey attribute for a ClinicalData/SubjectData element.'
    domain_of:
    - SubjectData
    - KeySet
    range: subjectKeyType
  metaDataVersionOID:
    name: metaDataVersionOID
    description: Reference to a MetaDataVersionOID attribute value for this ClinicalData
      element.
    comments:
    - 'Optional

      Matches the MetaDataVersionOID attribute for this ClinicalData element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
  studyEventOID:
    name: studyEventOID
    description: Reference to a StudyEventOID attribute value for a StudyEventData
      child element of this ClinicalData/SubjectData element.
    comments:
    - 'Optional

      Matches the StudyEventOID attribute for a StudyEventData child element of this
      ClinicalData/SubjectData element.'
    domain_of:
    - StudyEventRef
    - AbsoluteTimingConstraint
    - StudyEventData
    - KeySet
    range: StudyEventDef
  studyEventRepeatKey:
    name: studyEventRepeatKey
    description: Reference to a StudyEventRepeatKey attribute value for a StudyEventData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - 'Optional

      Matches the StudyEventRepeatKey attribute for this ClinicalData/SubjectData/StudyEventData
      element.'
    domain_of:
    - StudyEventData
    - KeySet
    range: repeatKey
  itemGroupOID:
    name: itemGroupOID
    description: Reference to an ItemGroupOID attribute value for an ItemGroupData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - 'Optional

      Matches the ItemGroupOID attribute for an ItemGroupData child of this ClinicalData/SubjectData/StudyEventData.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
  itemGroupRepeatKey:
    name: itemGroupRepeatKey
    description: Reference to an ItemGroupRepeatKey attribute value for an ItemGroupData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - '(Optional

      Matches the ItemGroupRepeatKey value for this ClinicalData/SubjectData/StudyEventData/ItemGroupData
      element.'
    domain_of:
    - ItemGroupData
    - KeySet
    range: repeatKey
  itemOID:
    name: itemOID
    description: Reference to an ItemOID attribute for an ItemData child element of
      this ClinicalData/SubjectData/StudyEventData/ItemGroupData element.
    comments:
    - 'Optional

      Matches the ItemOID for an ItemData child of this ClinicalData/SubjectData/StudyEventData/ItemGroupData
      element.'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
class_uri: odm:KeySet

```
</details>

### Induced

<details>
```yaml
name: KeySet
description: A KeySet references a single entity (e.g., a study, a subject, a study
  event). Only those attributes needed to specify the particular entity are required,
  and all others must be omitted (see Section 2.7, Clinical Data Keys).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/KeySet
rank: 1000
slot_usage:
  studyOID:
    name: studyOID
    description: References the StudyOID in an ODM/ClinicalData element.
    comments:
    - Matches the Association/@StudyOID.
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: Study
    required: true
  subjectKey:
    name: subjectKey
    description: Reference to a SubjectKey attribute value for a SubjectData child
      element of this ClinicalData element.
    comments:
    - 'Optional

      Matches the SubjectKey attribute for a ClinicalData/SubjectData element.'
    domain_of:
    - SubjectData
    - KeySet
    range: subjectKeyType
  metaDataVersionOID:
    name: metaDataVersionOID
    description: Reference to a MetaDataVersionOID attribute value for this ClinicalData
      element.
    comments:
    - 'Optional

      Matches the MetaDataVersionOID attribute for this ClinicalData element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
  studyEventOID:
    name: studyEventOID
    description: Reference to a StudyEventOID attribute value for a StudyEventData
      child element of this ClinicalData/SubjectData element.
    comments:
    - 'Optional

      Matches the StudyEventOID attribute for a StudyEventData child element of this
      ClinicalData/SubjectData element.'
    domain_of:
    - StudyEventRef
    - AbsoluteTimingConstraint
    - StudyEventData
    - KeySet
    range: StudyEventDef
  studyEventRepeatKey:
    name: studyEventRepeatKey
    description: Reference to a StudyEventRepeatKey attribute value for a StudyEventData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - 'Optional

      Matches the StudyEventRepeatKey attribute for this ClinicalData/SubjectData/StudyEventData
      element.'
    domain_of:
    - StudyEventData
    - KeySet
    range: repeatKey
  itemGroupOID:
    name: itemGroupOID
    description: Reference to an ItemGroupOID attribute value for an ItemGroupData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - 'Optional

      Matches the ItemGroupOID attribute for an ItemGroupData child of this ClinicalData/SubjectData/StudyEventData.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
  itemGroupRepeatKey:
    name: itemGroupRepeatKey
    description: Reference to an ItemGroupRepeatKey attribute value for an ItemGroupData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - '(Optional

      Matches the ItemGroupRepeatKey value for this ClinicalData/SubjectData/StudyEventData/ItemGroupData
      element.'
    domain_of:
    - ItemGroupData
    - KeySet
    range: repeatKey
  itemOID:
    name: itemOID
    description: Reference to an ItemOID attribute for an ItemData child element of
      this ClinicalData/SubjectData/StudyEventData/ItemGroupData element.
    comments:
    - 'Optional

      Matches the ItemOID for an ItemData child of this ClinicalData/SubjectData/StudyEventData/ItemGroupData
      element.'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
attributes:
  studyOID:
    name: studyOID
    description: References the StudyOID in an ODM/ClinicalData element.
    comments:
    - Matches the Association/@StudyOID.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyOID
    owner: KeySet
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: Study
    required: true
  subjectKey:
    name: subjectKey
    description: Reference to a SubjectKey attribute value for a SubjectData child
      element of this ClinicalData element.
    comments:
    - 'Optional

      Matches the SubjectKey attribute for a ClinicalData/SubjectData element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: subjectKey
    owner: KeySet
    domain_of:
    - SubjectData
    - KeySet
    range: subjectKeyType
  metaDataVersionOID:
    name: metaDataVersionOID
    description: Reference to a MetaDataVersionOID attribute value for this ClinicalData
      element.
    comments:
    - 'Optional

      Matches the MetaDataVersionOID attribute for this ClinicalData element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: metaDataVersionOID
    owner: KeySet
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
  studyEventOID:
    name: studyEventOID
    description: Reference to a StudyEventOID attribute value for a StudyEventData
      child element of this ClinicalData/SubjectData element.
    comments:
    - 'Optional

      Matches the StudyEventOID attribute for a StudyEventData child element of this
      ClinicalData/SubjectData element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyEventOID
    owner: KeySet
    domain_of:
    - StudyEventRef
    - AbsoluteTimingConstraint
    - StudyEventData
    - KeySet
    range: StudyEventDef
  studyEventRepeatKey:
    name: studyEventRepeatKey
    description: Reference to a StudyEventRepeatKey attribute value for a StudyEventData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - 'Optional

      Matches the StudyEventRepeatKey attribute for this ClinicalData/SubjectData/StudyEventData
      element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyEventRepeatKey
    owner: KeySet
    domain_of:
    - StudyEventData
    - KeySet
    range: repeatKey
  itemGroupOID:
    name: itemGroupOID
    description: Reference to an ItemGroupOID attribute value for an ItemGroupData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - 'Optional

      Matches the ItemGroupOID attribute for an ItemGroupData child of this ClinicalData/SubjectData/StudyEventData.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemGroupOID
    owner: KeySet
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
  itemGroupRepeatKey:
    name: itemGroupRepeatKey
    description: Reference to an ItemGroupRepeatKey attribute value for an ItemGroupData
      child element of this ClinicalData/SubjectData/StudyEventData element.
    comments:
    - '(Optional

      Matches the ItemGroupRepeatKey value for this ClinicalData/SubjectData/StudyEventData/ItemGroupData
      element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemGroupRepeatKey
    owner: KeySet
    domain_of:
    - ItemGroupData
    - KeySet
    range: repeatKey
  itemOID:
    name: itemOID
    description: Reference to an ItemOID attribute for an ItemData child element of
      this ClinicalData/SubjectData/StudyEventData/ItemGroupData element.
    comments:
    - 'Optional

      Matches the ItemOID for an ItemData child of this ClinicalData/SubjectData/StudyEventData/ItemGroupData
      element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemOID
    owner: KeySet
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
class_uri: odm:KeySet

```
</details>