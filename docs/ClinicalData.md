# Class: ClinicalData

_Clinical data for 1 or more subjects._




URI: [odm:ClinicalData](http://www.cdisc.org/ns/odm/v2.0/ClinicalData)


```mermaid
erDiagram
ClinicalData {

}
Annotation {
    positiveInteger seqNum  
    TransactionType transactionType  
    oid ID  
}
Flag {

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
Comment {
    CommentType sponsorOrSite  
}
Signature {
    oid ID  
}
DateTimeStamp {
    datetime content  
}
SignatureRef {

}
LocationRef {

}
UserRef {

}
AuditRecord {
    EditPointType editPoint  
    YesOrNo usedMethod  
}
SourceID {
    text content  
}
ReasonForChange {
    text content  
}
Query {
    oid OID  
    QuerySourceType source  
    text target  
    QueryType type  
    QueryStateType state  
    datetime lastUpdateDatetime  
    nameType name  
}
Value {
    positiveInteger seqNum  
    text content  
}
ItemGroupData {
    repeatKey itemGroupRepeatKey  
    TransactionType transactionType  
    positiveInteger itemGroupDataSeq  
}
ItemData {
    TransactionType transactionType  
    YesOnly isNull  
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
SubjectData {
    subjectKeyType subjectKey  
    TransactionType transactionType  
}
StudyEventData {
    repeatKey studyEventRepeatKey  
    TransactionType transactionType  
}
SiteRef {

}
InvestigatorRef {

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
Study {
    oid OID  
    nameType studyName  
    nameType protocolName  
    nameType versionID  
    nameType versionName  
    nameType status  
}

ClinicalData ||--|| Study : "studyOID"
ClinicalData ||--|| MetaDataVersion : "metaDataVersionOID"
ClinicalData ||--}o SubjectData : "subjectData"
ClinicalData ||--}o ItemGroupData : "itemGroupData"
ClinicalData ||--}o Query : "query"
ClinicalData ||--|o AuditRecord : "auditRecord"
ClinicalData ||--|o Signature : "signature"
ClinicalData ||--|o Annotation : "annotation"
Annotation ||--|o Comment : "comment"
Annotation ||--}o Coding : "coding"
Annotation ||--}o Flag : "flag"
Flag ||--|o FlagValue : "flagValue"
Flag ||--|o FlagType : "flagType"
Comment ||--}o TranslatedText : "translatedText"
Signature ||--|o UserRef : "userRef"
Signature ||--|o LocationRef : "locationRef"
Signature ||--|o SignatureRef : "signatureRef"
Signature ||--|o DateTimeStamp : "dateTimeStamp"
SignatureRef ||--|| SignatureDef : "signatureOID"
LocationRef ||--|| Location : "locationOID"
UserRef ||--|| User : "userOID"
AuditRecord ||--|o UserRef : "userRef"
AuditRecord ||--|o LocationRef : "locationRef"
AuditRecord ||--|o DateTimeStamp : "dateTimeStamp"
AuditRecord ||--|o ReasonForChange : "reasonForChange"
AuditRecord ||--|o SourceID : "sourceID"
Query ||--|o Value : "value"
Query ||--}o AuditRecord : "auditRecord"
ItemGroupData ||--|| ItemGroupDef : "itemGroupOID"
ItemGroupData ||--}o Query : "query"
ItemGroupData ||--}o ItemGroupData : "itemGroupData"
ItemGroupData ||--}o ItemData : "itemData"
ItemGroupData ||--|o AuditRecord : "auditRecord"
ItemGroupData ||--|o Signature : "signature"
ItemGroupData ||--|o Annotation : "annotation"
ItemData ||--|| ItemDef : "itemOID"
ItemData ||--}o Value : "value"
ItemData ||--}o Query : "query"
ItemData ||--|o AuditRecord : "auditRecord"
ItemData ||--|o Signature : "signature"
ItemData ||--|o Annotation : "annotation"
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
SubjectData ||--|o InvestigatorRef : "investigatorRef"
SubjectData ||--|o SiteRef : "siteRef"
SubjectData ||--}o StudyEventData : "studyEventData"
SubjectData ||--}o Query : "query"
SubjectData ||--|o AuditRecord : "auditRecord"
SubjectData ||--|o Signature : "signature"
SubjectData ||--|o Annotation : "annotation"
StudyEventData ||--|| StudyEventDef : "studyEventOID"
StudyEventData ||--}o ItemGroupData : "itemGroupData"
StudyEventData ||--}o Query : "query"
StudyEventData ||--|o AuditRecord : "auditRecord"
StudyEventData ||--|o Signature : "signature"
StudyEventData ||--|o Annotation : "annotation"
SiteRef ||--|| Location : "locationOID"
InvestigatorRef ||--|| User : "userOID"
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
Study ||--|o Description : "description"
Study ||--}o MetaDataVersion : "metaDataVersion"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyOID](studyOID.md) | 1..1 <br/> [Study](Study.md) | References the Study that uses the data nested within this element. | direct |
| [metaDataVersionOID](metaDataVersionOID.md) | 1..1 <br/> [MetaDataVersion](MetaDataVersion.md) | References the MetaDataVersion (within the above Study) that governs the data... | direct |
| [subjectData](subjectData.md) | 0..* <br/> [SubjectData](SubjectData.md) | SubjectData reference: Clinical data for a single subject. | direct |
| [itemGroupData](itemGroupData.md) | 0..* <br/> [ItemGroupData](ItemGroupData.md) | ItemGroupData reference: Clinical data corresponding to an ItemGroupRef defin... | direct |
| [query](query.md) | 0..* <br/> [Query](Query.md) | Query reference: The Query element represents a request for clarification on ... | direct |
| [auditRecord](auditRecord.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... | direct |
| [signature](signature.md) | 0..1 <br/> [Signature](Signature.md) | Signature reference: An electronic signature applies to a collection of clini... | direct |
| [annotation](annotation.md) | 0..1 <br/> [Annotation](Annotation.md) | Annotation reference: A general note about clinical data. If an annotation ha... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ODMFileMetadata](ODMFileMetadata.md) | [clinicalData](clinicalData.md) | range | [ClinicalData](ClinicalData.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/ClinicalData](https://wiki.cdisc.org/display/PUB/ClinicalData)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ClinicalData |
| native | odm:ClinicalData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ClinicalData
description: Clinical data for 1 or more subjects.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ClinicalData
rank: 1000
slots:
- studyOID
- metaDataVersionOID
- subjectData
- itemGroupData
- query
- auditRecord
- signature
- annotation
slot_usage:
  studyOID:
    name: studyOID
    description: References the Study that uses the data nested within this element.
    comments:
    - 'Required

      range: oidref

      Must match a Study/@OID value.'
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
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion (within the above Study) that governs
      the data nested within this element. The StudyOID and MetaDataVersionOID attributes
      select a particular metadata version. All metadata references (OIDs) occurring
      within this ClinicalData element refer to definitions within the selected metadata
      version.
    comments:
    - 'Required

      range: oidref

      Must match a MetaDataVersions/@OID value contained in the Study element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
    required: true
  subjectData:
    name: subjectData
    multivalued: true
    domain_of:
    - ClinicalData
    range: SubjectData
    inlined: true
    inlined_as_list: true
  itemGroupData:
    name: itemGroupData
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  query:
    name: query
    multivalued: true
    domain_of:
    - Location
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Query
    inlined: true
    inlined_as_list: true
  auditRecord:
    name: auditRecord
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    maximum_cardinality: 1
  signature:
    name: signature
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Signature
    maximum_cardinality: 1
  annotation:
    name: annotation
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Association
    range: Annotation
    maximum_cardinality: 1
class_uri: odm:ClinicalData

```
</details>

### Induced

<details>
```yaml
name: ClinicalData
description: Clinical data for 1 or more subjects.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ClinicalData
rank: 1000
slot_usage:
  studyOID:
    name: studyOID
    description: References the Study that uses the data nested within this element.
    comments:
    - 'Required

      range: oidref

      Must match a Study/@OID value.'
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
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion (within the above Study) that governs
      the data nested within this element. The StudyOID and MetaDataVersionOID attributes
      select a particular metadata version. All metadata references (OIDs) occurring
      within this ClinicalData element refer to definitions within the selected metadata
      version.
    comments:
    - 'Required

      range: oidref

      Must match a MetaDataVersions/@OID value contained in the Study element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
    required: true
  subjectData:
    name: subjectData
    multivalued: true
    domain_of:
    - ClinicalData
    range: SubjectData
    inlined: true
    inlined_as_list: true
  itemGroupData:
    name: itemGroupData
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  query:
    name: query
    multivalued: true
    domain_of:
    - Location
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Query
    inlined: true
    inlined_as_list: true
  auditRecord:
    name: auditRecord
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    maximum_cardinality: 1
  signature:
    name: signature
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Signature
    maximum_cardinality: 1
  annotation:
    name: annotation
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Association
    range: Annotation
    maximum_cardinality: 1
attributes:
  studyOID:
    name: studyOID
    description: References the Study that uses the data nested within this element.
    comments:
    - 'Required

      range: oidref

      Must match a Study/@OID value.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyOID
    owner: ClinicalData
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
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion (within the above Study) that governs
      the data nested within this element. The StudyOID and MetaDataVersionOID attributes
      select a particular metadata version. All metadata references (OIDs) occurring
      within this ClinicalData element refer to definitions within the selected metadata
      version.
    comments:
    - 'Required

      range: oidref

      Must match a MetaDataVersions/@OID value contained in the Study element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: metaDataVersionOID
    owner: ClinicalData
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
    required: true
  subjectData:
    name: subjectData
    description: 'SubjectData reference: Clinical data for a single subject.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: subjectData
    owner: ClinicalData
    domain_of:
    - ClinicalData
    range: SubjectData
    inlined: true
    inlined_as_list: true
  itemGroupData:
    name: itemGroupData
    description: 'ItemGroupData reference: Clinical data corresponding to an ItemGroupRef
      defined in the active MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: itemGroupData
    owner: ClinicalData
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  query:
    name: query
    description: 'Query reference: The Query element represents a request for clarification
      on a data item collected for a clinical trial, specifically a request from a
      sponsor or sponsor’s representative to an investigator to resolve an error or
      inconsistency discovered during data review. Queries can be created manually
      by individuals such as site monitors or data managers or automatically by systems.
      The full text of the Query exists in the Value child element. The optional Name
      attribute provide the means to provide a short identifier that can be included
      in listing or user interfaces.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: query
    owner: ClinicalData
    domain_of:
    - Location
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Query
    inlined: true
    inlined_as_list: true
  auditRecord:
    name: auditRecord
    description: 'AuditRecord reference: An AuditRecord carries information pertaining
      to the creation, deletion, or modification of clinical data. This information
      includes who performed that action, and where, when, and why that action was
      performed.AuditRecord information describes a change to clinical data, but is
      not itself clinical data. The value of some clinical data can always be changed
      by a subsequent transaction, but history cannot be changed, only added to.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: auditRecord
    owner: ClinicalData
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Query
    range: AuditRecord
    maximum_cardinality: 1
  signature:
    name: signature
    description: 'Signature reference: An electronic signature applies to a collection
      of clinical data. This indicates that some user accepts legal responsibility
      for that data. See 21 CFR Part 11. The signature identifies the person signing,
      the location of signing, the signature meaning (via the referenced SignatureDef),
      the date and time of signing, and (in the case of a digital signature) an encrypted
      hash of the included data.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: signature
    owner: ClinicalData
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    range: Signature
    maximum_cardinality: 1
  annotation:
    name: annotation
    description: 'Annotation reference: A general note about clinical data. If an
      annotation has both a comment and flags, the flags should be related to the
      comment.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: annotation
    owner: ClinicalData
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Association
    range: Annotation
    maximum_cardinality: 1
class_uri: odm:ClinicalData

```
</details>