# Class: ODMFileMetadata

_Root element for ODM Documents. The ODM element is the top-level (root) element of each ODM document._




URI: [odm:ODM](http://www.cdisc.org/ns/odm/v2.0/ODM)


```mermaid
erDiagram
ODMFileMetadata {
    FileType fileType  
    Granularity granularity  
    Context context  
    oid fileOID  
    datetime creationDateTime  
    oidref priorFileOID  
    datetime asOfDateTime  
    ODMVersion oDMVersion  
    text originator  
    text sourceSystem  
    text sourceSystemVersion  
}
Association {
    oidref studyOID  
    oidref metaDataVersionOID  
}
Annotation {
    positiveInteger seqNum  
    TransactionType transactionType  
    oid iD  
}
KeySet {
    oidref studyOID  
    subjectKeyType subjectKey  
    oidref metaDataVersionOID  
    oidref studyEventOID  
    repeatKey studyEventRepeatKey  
    oidref itemGroupOID  
    repeatKey itemGroupRepeatKey  
    oidref itemOID  
}
ClinicalData {
    oidref studyOID  
    oidref metaDataVersionOID  
}
Signature {
    oid iD  
}
AuditRecord {
    EditPointType editPoint  
    YesOrNo usedMethod  
}
Query {
    oid oID  
    QuerySourceType source  
    text target  
    QueryType type  
    QueryStateType state  
    datetime lastUpdateDatetime  
    nameType name  
}
ItemGroupData {
    oidref itemGroupOID  
    repeatKey itemGroupRepeatKey  
    TransactionType transactionType  
    positiveInteger itemGroupDataSeq  
}
SubjectData {
    subjectKeyType subjectKey  
    TransactionType transactionType  
}
ReferenceData {
    oidref studyOID  
    oidref metaDataVersionOID  
}
AdminData {
    oidref studyOID  
}
SignatureDef {
    oid oID  
    SignMethod methodology  
}
Location {
    oid oID  
    nameType name  
    text role  
    oidref organizationOID  
}
Organization {
    oid oID  
    nameType name  
    text role  
    OrganizationType type  
    oidref locationOID  
    oidref partOfOrganizationOID  
}
User {
    oid oID  
    UserType userType  
    oidref organizationOID  
    oidref locationOID  
}
Study {
    oid oID  
    nameType studyName  
    nameType protocolName  
    nameType versionID  
    nameType versionName  
    nameType status  
}
MetaDataVersion {
    oid oID  
    nameType name  
    oidref commentOID  
}
Description {

}

ODMFileMetadata ||--|o Description : "description"
ODMFileMetadata ||--}o Study : "study"
ODMFileMetadata ||--}o AdminData : "adminData"
ODMFileMetadata ||--}o ReferenceData : "referenceData"
ODMFileMetadata ||--}o ClinicalData : "clinicalData"
ODMFileMetadata ||--}o Association : "association"
Association ||--|o KeySet : "keySet"
Association ||--|o Annotation : "annotation"
Annotation ||--|o Comment : "comment"
Annotation ||--}o Coding : "coding"
Annotation ||--}o Flag : "flag"
ClinicalData ||--}o SubjectData : "subjectData"
ClinicalData ||--}o ItemGroupData : "itemGroupData"
ClinicalData ||--}o Query : "query"
ClinicalData ||--|o AuditRecord : "auditRecord"
ClinicalData ||--|o Signature : "signature"
ClinicalData ||--|o Annotation : "annotation"
Signature ||--|o UserRef : "userRef"
Signature ||--|o LocationRef : "locationRef"
Signature ||--|o SignatureRef : "signatureRef"
Signature ||--|o DateTimeStamp : "dateTimeStamp"
AuditRecord ||--|o UserRef : "userRef"
AuditRecord ||--|o LocationRef : "locationRef"
AuditRecord ||--|o DateTimeStamp : "dateTimeStamp"
AuditRecord ||--|o ReasonForChange : "reasonForChange"
AuditRecord ||--|o SourceID : "sourceID"
Query ||--|o Value : "value"
Query ||--}o AuditRecord : "auditRecord"
ItemGroupData ||--}o Query : "query"
ItemGroupData ||--}o ItemGroupData : "itemGroupData"
ItemGroupData ||--}o ItemData : "itemData"
ItemGroupData ||--|o AuditRecord : "auditRecord"
ItemGroupData ||--|o Signature : "signature"
ItemGroupData ||--|o Annotation : "annotation"
SubjectData ||--|o InvestigatorRef : "investigatorRef"
SubjectData ||--|o SiteRef : "siteRef"
SubjectData ||--}o StudyEventData : "studyEventData"
SubjectData ||--}o Query : "query"
SubjectData ||--|o AuditRecord : "auditRecord"
SubjectData ||--|o Signature : "signature"
SubjectData ||--|o Annotation : "annotation"
ReferenceData ||--}o ItemGroupData : "itemGroupData"
ReferenceData ||--|o AuditRecord : "auditRecord"
ReferenceData ||--|o Signature : "signature"
ReferenceData ||--|o Annotation : "annotation"
AdminData ||--}o User : "user"
AdminData ||--}o Organization : "organization"
AdminData ||--}o Location : "location"
AdminData ||--}o SignatureDef : "signatureDef"
SignatureDef ||--|o Meaning : "meaning"
SignatureDef ||--|o LegalReason : "legalReason"
Location ||--|o Description : "description"
Location ||--}o MetaDataVersionRef : "metaDataVersionRef"
Location ||--}o Address : "address"
Location ||--}o Telecom : "telecom"
Location ||--}o Query : "query"
Organization ||--|o Description : "description"
Organization ||--}o Address : "address"
Organization ||--}o Telecom : "telecom"
User ||--|o UserName : "userName"
User ||--|o Prefix : "prefix"
User ||--|o Suffix : "suffix"
User ||--|o FullName : "fullName"
User ||--|o GivenName : "givenName"
User ||--|o FamilyName : "familyName"
User ||--|o Image : "image"
User ||--}o Address : "address"
User ||--}o Telecom : "telecom"
Study ||--|o Description : "description"
Study ||--}o MetaDataVersion : "metaDataVersion"
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
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [fileType](fileType.md) | 1..1 <br/> [FileType](FileType.md) | Snapshot means that the document contains only the current state of the data ... | direct |
| [granularity](granularity.md) | 0..1 <br/> [Granularity](Granularity.md) | Granularity is intended to give the sender a shorthand way to Describes the s... | direct |
| [context](context.md) | 0..1 <br/> [Context](Context.md) | Indicates the intended usage of the ODM document. Archive - indicates that th... | direct |
| [fileOID](fileOID.md) | 1..1 <br/> [oid](oid.md) | A unique identifier for this file. | direct |
| [creationDateTime](creationDateTime.md) | 1..1 <br/> [datetime](datetime.md) | Time of creation of the file containing the document. | direct |
| [priorFileOID](priorFileOID.md) | 0..1 <br/> [oidref](oidref.md) | Reference to the previous file (if any) in a series. | direct |
| [asOfDateTime](asOfDateTime.md) | 0..1 <br/> [datetime](datetime.md) | The date/time at which the source database was queried in order to create thi... | direct |
| [oDMVersion](oDMVersion.md) | 0..1 <br/> [ODMVersion](ODMVersion.md) | The version of the ODM standard used. | direct |
| [originator](originator.md) | 0..1 <br/> [text](text.md) | The organization that generated the ODM file. | direct |
| [sourceSystem](sourceSystem.md) | 0..1 <br/> [text](text.md) | The computer system or database management system that is the source of the i... | direct |
| [sourceSystemVersion](sourceSystemVersion.md) | 0..1 <br/> [text](text.md) | The version of the "SourceSystem" above. | direct |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [study](study.md) | 0..* <br/> [Study](Study.md) | Study reference: This element collects static structural information about an... | direct |
| [adminData](adminData.md) | 0..* <br/> [AdminData](AdminData.md) | AdminData reference: Administrative information about users, locations, organ... | direct |
| [referenceData](referenceData.md) | 0..* <br/> [ReferenceData](ReferenceData.md) | ReferenceData reference: Reference data provides information on how to interp... | direct |
| [clinicalData](clinicalData.md) | 0..* <br/> [ClinicalData](ClinicalData.md) | ClinicalData reference: Clinical data for 1 or more subjects. | direct |
| [association](association.md) | 0..* <br/> [Association](Association.md) | Association reference: An association permits an annotation to be placed on a... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._








## See Also

* [https://wiki.cdisc.org/display/PUB/ODM](https://wiki.cdisc.org/display/PUB/ODM)

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
description: Root element for ODM Documents. The ODM element is the top-level (root)
  element of each ODM document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ODM
rank: 1000
slots:
- fileType
- granularity
- context
- fileOID
- creationDateTime
- priorFileOID
- asOfDateTime
- oDMVersion
- originator
- sourceSystem
- sourceSystemVersion
- description
- study
- adminData
- referenceData
- clinicalData
- association
slot_usage:
  fileType:
    name: fileType
    description: Snapshot means that the document contains only the current state
      of the data and metadata it describes, and no transactional history. Transactional
      means that the document may contain more than one instance per data point. Query
      means the document contains only ClinicalData/Query elements.
    comments:
    - 'Required

      enum values: ( Snapshot | Transactional | Query)'
    domain_of:
    - ODMFileMetadata
    range: FileType
    required: true
  granularity:
    name: granularity
    description: Granularity is intended to give the sender a shorthand way to Describes
      the scope of information in the document, for certain common types of documents.
      All means the entire study; Metadata means the Study/MetaDataVersion element;
      AdminData and ReferenceData mean the corresponding elements; AllClinicalData
      means all of the ClinicalData collected for the study. SingleSite, means all
      of the Clinical Data for a single study site. SingleSubject means all of the
      Clinical Data for a single Subject.
    comments:
    - 'Optional

      enum values: ( All | Metadata | AdminData | ReferenceData | AllClinicalData
      | SingleSite | SingleSubject )'
    domain_of:
    - ODMFileMetadata
    range: Granularity
  context:
    name: context
    description: Indicates the intended usage of the ODM document. Archive - indicates
      that the file is intended to meet the requirements of an electronic record as
      defined in 21 CFR 11. Submission - indicates that the file is intended to be
      used for regulatory submission. Exchange - indicates that the file was generated
      to be imported into an ODM compliant system.
    comments:
    - 'Optional

      enum values: (Archive| Submission | Exchange)'
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: Context
  fileOID:
    name: fileOID
    description: A unique identifier for this file.
    comments:
    - 'Required

      range: oid'
    domain_of:
    - ODMFileMetadata
    range: oid
    required: true
  creationDateTime:
    name: creationDateTime
    description: Time of creation of the file containing the document.
    comments:
    - 'Required

      range: datetime'
    domain_of:
    - ODMFileMetadata
    range: datetime
    required: true
  priorFileOID:
    name: priorFileOID
    description: Reference to the previous file (if any) in a series.
    comments:
    - 'Optional

      range: oidref'
    domain_of:
    - ODMFileMetadata
    range: oidref
  asOfDateTime:
    name: asOfDateTime
    description: The date/time at which the source database was queried in order to
      create this document.
    comments:
    - 'Optional

      range: datetime'
    domain_of:
    - ODMFileMetadata
    range: datetime
  oDMVersion:
    name: oDMVersion
    description: The version of the ODM standard used.
    comments:
    - 'Required

      enum values: Pattern: 2.0(.(0|([1-9][0-9]*)))?(-([0-9a-zA-Z])+)*'
    domain_of:
    - ODMFileMetadata
    range: ODMVersion
  originator:
    name: originator
    description: The organization that generated the ODM file.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ODMFileMetadata
    range: text
  sourceSystem:
    name: sourceSystem
    description: The computer system or database management system that is the source
      of the information in this file.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ODMFileMetadata
    range: text
  sourceSystemVersion:
    name: sourceSystemVersion
    description: The version of the "SourceSystem" above.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ODMFileMetadata
    range: text
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
  study:
    name: study
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Study
    inlined: true
    inlined_as_list: true
  adminData:
    name: adminData
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: AdminData
    inlined: true
    inlined_as_list: true
  referenceData:
    name: referenceData
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ReferenceData
    inlined: true
    inlined_as_list: true
  clinicalData:
    name: clinicalData
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ClinicalData
    inlined: true
    inlined_as_list: true
  association:
    name: association
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Association
    inlined: true
    inlined_as_list: true
class_uri: odm:ODM
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: ODMFileMetadata
description: Root element for ODM Documents. The ODM element is the top-level (root)
  element of each ODM document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ODM
rank: 1000
slot_usage:
  fileType:
    name: fileType
    description: Snapshot means that the document contains only the current state
      of the data and metadata it describes, and no transactional history. Transactional
      means that the document may contain more than one instance per data point. Query
      means the document contains only ClinicalData/Query elements.
    comments:
    - 'Required

      enum values: ( Snapshot | Transactional | Query)'
    domain_of:
    - ODMFileMetadata
    range: FileType
    required: true
  granularity:
    name: granularity
    description: Granularity is intended to give the sender a shorthand way to Describes
      the scope of information in the document, for certain common types of documents.
      All means the entire study; Metadata means the Study/MetaDataVersion element;
      AdminData and ReferenceData mean the corresponding elements; AllClinicalData
      means all of the ClinicalData collected for the study. SingleSite, means all
      of the Clinical Data for a single study site. SingleSubject means all of the
      Clinical Data for a single Subject.
    comments:
    - 'Optional

      enum values: ( All | Metadata | AdminData | ReferenceData | AllClinicalData
      | SingleSite | SingleSubject )'
    domain_of:
    - ODMFileMetadata
    range: Granularity
  context:
    name: context
    description: Indicates the intended usage of the ODM document. Archive - indicates
      that the file is intended to meet the requirements of an electronic record as
      defined in 21 CFR 11. Submission - indicates that the file is intended to be
      used for regulatory submission. Exchange - indicates that the file was generated
      to be imported into an ODM compliant system.
    comments:
    - 'Optional

      enum values: (Archive| Submission | Exchange)'
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: Context
  fileOID:
    name: fileOID
    description: A unique identifier for this file.
    comments:
    - 'Required

      range: oid'
    domain_of:
    - ODMFileMetadata
    range: oid
    required: true
  creationDateTime:
    name: creationDateTime
    description: Time of creation of the file containing the document.
    comments:
    - 'Required

      range: datetime'
    domain_of:
    - ODMFileMetadata
    range: datetime
    required: true
  priorFileOID:
    name: priorFileOID
    description: Reference to the previous file (if any) in a series.
    comments:
    - 'Optional

      range: oidref'
    domain_of:
    - ODMFileMetadata
    range: oidref
  asOfDateTime:
    name: asOfDateTime
    description: The date/time at which the source database was queried in order to
      create this document.
    comments:
    - 'Optional

      range: datetime'
    domain_of:
    - ODMFileMetadata
    range: datetime
  oDMVersion:
    name: oDMVersion
    description: The version of the ODM standard used.
    comments:
    - 'Required

      enum values: Pattern: 2.0(.(0|([1-9][0-9]*)))?(-([0-9a-zA-Z])+)*'
    domain_of:
    - ODMFileMetadata
    range: ODMVersion
  originator:
    name: originator
    description: The organization that generated the ODM file.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ODMFileMetadata
    range: text
  sourceSystem:
    name: sourceSystem
    description: The computer system or database management system that is the source
      of the information in this file.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ODMFileMetadata
    range: text
  sourceSystemVersion:
    name: sourceSystemVersion
    description: The version of the "SourceSystem" above.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ODMFileMetadata
    range: text
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
  study:
    name: study
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Study
    inlined: true
    inlined_as_list: true
  adminData:
    name: adminData
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: AdminData
    inlined: true
    inlined_as_list: true
  referenceData:
    name: referenceData
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ReferenceData
    inlined: true
    inlined_as_list: true
  clinicalData:
    name: clinicalData
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: ClinicalData
    inlined: true
    inlined_as_list: true
  association:
    name: association
    multivalued: true
    domain_of:
    - ODMFileMetadata
    range: Association
    inlined: true
    inlined_as_list: true
attributes:
  fileType:
    name: fileType
    description: Snapshot means that the document contains only the current state
      of the data and metadata it describes, and no transactional history. Transactional
      means that the document may contain more than one instance per data point. Query
      means the document contains only ClinicalData/Query elements.
    comments:
    - 'Required

      enum values: ( Snapshot | Transactional | Query)'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: fileType
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: FileType
    required: true
  granularity:
    name: granularity
    description: Granularity is intended to give the sender a shorthand way to Describes
      the scope of information in the document, for certain common types of documents.
      All means the entire study; Metadata means the Study/MetaDataVersion element;
      AdminData and ReferenceData mean the corresponding elements; AllClinicalData
      means all of the ClinicalData collected for the study. SingleSite, means all
      of the Clinical Data for a single study site. SingleSubject means all of the
      Clinical Data for a single Subject.
    comments:
    - 'Optional

      enum values: ( All | Metadata | AdminData | ReferenceData | AllClinicalData
      | SingleSite | SingleSubject )'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: granularity
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: Granularity
  context:
    name: context
    description: Indicates the intended usage of the ODM document. Archive - indicates
      that the file is intended to meet the requirements of an electronic record as
      defined in 21 CFR 11. Submission - indicates that the file is intended to be
      used for regulatory submission. Exchange - indicates that the file was generated
      to be imported into an ODM compliant system.
    comments:
    - 'Optional

      enum values: (Archive| Submission | Exchange)'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: context
    owner: ODMFileMetadata
    domain_of:
    - Alias
    - FormalExpression
    - ODMFileMetadata
    range: Context
  fileOID:
    name: fileOID
    description: A unique identifier for this file.
    comments:
    - 'Required

      range: oid'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: fileOID
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: oid
    required: true
  creationDateTime:
    name: creationDateTime
    description: Time of creation of the file containing the document.
    comments:
    - 'Required

      range: datetime'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: creationDateTime
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: datetime
    required: true
  priorFileOID:
    name: priorFileOID
    description: Reference to the previous file (if any) in a series.
    comments:
    - 'Optional

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: priorFileOID
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: oidref
  asOfDateTime:
    name: asOfDateTime
    description: The date/time at which the source database was queried in order to
      create this document.
    comments:
    - 'Optional

      range: datetime'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: asOfDateTime
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: datetime
  oDMVersion:
    name: oDMVersion
    description: The version of the ODM standard used.
    comments:
    - 'Required

      enum values: Pattern: 2.0(.(0|([1-9][0-9]*)))?(-([0-9a-zA-Z])+)*'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: oDMVersion
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: ODMVersion
  originator:
    name: originator
    description: The organization that generated the ODM file.
    comments:
    - 'Optional

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: originator
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: text
  sourceSystem:
    name: sourceSystem
    description: The computer system or database management system that is the source
      of the information in this file.
    comments:
    - 'Optional

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: sourceSystem
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: text
  sourceSystemVersion:
    name: sourceSystemVersion
    description: The version of the "SourceSystem" above.
    comments:
    - 'Optional

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: sourceSystemVersion
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: text
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: description
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
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  study:
    name: study
    description: 'Study reference: This element collects static structural information
      about an individual study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: study
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: Study
    inlined: true
    inlined_as_list: true
  adminData:
    name: adminData
    description: 'AdminData reference: Administrative information about users, locations,
      organizations, and electronic signatures.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: adminData
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: AdminData
    inlined: true
    inlined_as_list: true
  referenceData:
    name: referenceData
    description: 'ReferenceData reference: Reference data provides information on
      how to interpret clinical data. For example, reference data might include lab
      normal ranges. For a study that uses CDISC standards, reference data might include
      SDTM Trial Design datasets.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: referenceData
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: ReferenceData
    inlined: true
    inlined_as_list: true
  clinicalData:
    name: clinicalData
    description: 'ClinicalData reference: Clinical data for 1 or more subjects.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: clinicalData
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: ClinicalData
    inlined: true
    inlined_as_list: true
  association:
    name: association
    description: 'Association reference: An association permits an annotation to be
      placed on an ordered pair of entities rather than on just one. The first and
      second KeySets identify the start and end of the annotated "link.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: association
    owner: ODMFileMetadata
    domain_of:
    - ODMFileMetadata
    range: Association
    inlined: true
    inlined_as_list: true
class_uri: odm:ODM
tree_root: true

```
</details>