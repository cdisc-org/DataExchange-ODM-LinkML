# Class: StudyEventData

_Clinical data for a study event (visit). The model supports repeating study events (e.g., when the same set of information is collected for a series of patient visits)._




URI: [odm:StudyEventData](http://www.cdisc.org/ns/odm/v2.0/StudyEventData)


```mermaid
erDiagram
StudyEventData {
    oidref studyEventOID  
    repeatKey studyEventRepeatKey  
    TransactionType transactionType  
}
Annotation {
    positiveInteger seqNum  
    TransactionType transactionType  
    oid iD  
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
    oid iD  
}
DateTimeStamp {
    datetime content  
}
SignatureRef {
    oidref signatureOID  
}
LocationRef {
    oidref locationOID  
}
UserRef {
    oidref userOID  
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
    oid oID  
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
    oidref itemGroupOID  
    repeatKey itemGroupRepeatKey  
    TransactionType transactionType  
    positiveInteger itemGroupDataSeq  
}
ItemData {
    oidref itemOID  
    TransactionType transactionType  
    YesOnly isNull  
}

StudyEventData ||--}o ItemGroupData : "itemGroupData"
StudyEventData ||--}o Query : "query"
StudyEventData ||--|o AuditRecord : "auditRecord"
StudyEventData ||--|o Signature : "signature"
StudyEventData ||--|o Annotation : "annotation"
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
ItemData ||--}o Value : "value"
ItemData ||--}o Query : "query"
ItemData ||--|o AuditRecord : "auditRecord"
ItemData ||--|o Signature : "signature"
ItemData ||--|o Annotation : "annotation"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyEventOID](studyEventOID.md) | 1..1 <br/> [oidref](oidref.md) | Reference to the StudyEventDef . The StudyEventOID and StudyEventRepeatKey ar... | direct |
| [studyEventRepeatKey](studyEventRepeatKey.md) | 0..1 <br/> [repeatKey](repeatKey.md) | A key used to distinguish between repeats of the same type of study event for... | direct |
| [transactionType](transactionType.md) | 0..1 <br/> [TransactionType](TransactionType.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... | direct |
| [itemGroupData](itemGroupData.md) | 0..* <br/> [ItemGroupData](ItemGroupData.md) | ItemGroupData reference: Clinical data corresponding to an ItemGroupRef defin... | direct |
| [query](query.md) | 0..* <br/> [Query](Query.md) | Query reference: The Query element represents a request for clarification on ... | direct |
| [auditRecord](auditRecord.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... | direct |
| [signature](signature.md) | 0..1 <br/> [Signature](Signature.md) | Signature reference: An electronic signature applies to a collection of clini... | direct |
| [annotation](annotation.md) | 0..1 <br/> [Annotation](Annotation.md) | Annotation reference: A general note about clinical data. If an annotation ha... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SubjectData](SubjectData.md) | [studyEventData](studyEventData.md) | range | [StudyEventData](StudyEventData.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyEventData](https://wiki.cdisc.org/display/PUB/StudyEventData)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyEventData |
| native | odm:StudyEventData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyEventData
description: Clinical data for a study event (visit). The model supports repeating
  study events (e.g., when the same set of information is collected for a series of
  patient visits).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEventData
rank: 1000
slots:
- studyEventOID
- studyEventRepeatKey
- transactionType
- itemGroupData
- query
- auditRecord
- signature
- annotation
slot_usage:
  studyEventOID:
    name: studyEventOID
    description: Reference to the StudyEventDef . The StudyEventOID and StudyEventRepeatKey
      are used together to identify a particular study event. This pair of values
      uniquely identifies a StudyEvent within the containing subject. The StudyEventRepeatKey
      is present if and only if the StudyEventDef is repeating.
    comments:
    - 'Required

      Must match a StudyEventGroupDef/@OID or StudyEventDef/@OID for the MetaDataVersion
      /@OID value that matches the ClinicalData/@MetaDataVersionOID attribute.'
    domain_of:
    - StudyEventRef
    - AbsoluteTimingConstraint
    - StudyEventData
    - KeySet
    range: oidref
    required: true
  studyEventRepeatKey:
    name: studyEventRepeatKey
    description: A key used to distinguish between repeats of the same type of study
      event for a single subject.
    comments:
    - 'Conditional

      If the StudyEventDef/@Repeating attribute has the value "Yes" and there is more
      than one ClinicalData/SubjectData/StudyEventData/@OID element, the StudyEventRepeatKey
      attribute must be provided. Must be unique among the set of ClinicalData/SubjectData/StudyEventData/@OID
      elements. The StudyEventRepeatKey must be present only when the StudyEventDef/@Repeating
      attribute has the value "Yes".'
    domain_of:
    - StudyEventData
    - KeySet
    range: repeatKey
  transactionType:
    name: transactionType
    description: Identifies the transaction type when /ODM/@FileType is Transactional
      and there is no child element.
    comments:
    - 'Conditional Required when contained within an ODM Transactional file and the
      StudyEventData element has no child element content the TransactionType must
      be specified.

      When importing data from an ODM Snapshot file, the TransactionType attribute
      must not affect the processing of any of the StudyEvent child elements.'
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
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
class_uri: odm:StudyEventData

```
</details>

### Induced

<details>
```yaml
name: StudyEventData
description: Clinical data for a study event (visit). The model supports repeating
  study events (e.g., when the same set of information is collected for a series of
  patient visits).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEventData
rank: 1000
slot_usage:
  studyEventOID:
    name: studyEventOID
    description: Reference to the StudyEventDef . The StudyEventOID and StudyEventRepeatKey
      are used together to identify a particular study event. This pair of values
      uniquely identifies a StudyEvent within the containing subject. The StudyEventRepeatKey
      is present if and only if the StudyEventDef is repeating.
    comments:
    - 'Required

      Must match a StudyEventGroupDef/@OID or StudyEventDef/@OID for the MetaDataVersion
      /@OID value that matches the ClinicalData/@MetaDataVersionOID attribute.'
    domain_of:
    - StudyEventRef
    - AbsoluteTimingConstraint
    - StudyEventData
    - KeySet
    range: oidref
    required: true
  studyEventRepeatKey:
    name: studyEventRepeatKey
    description: A key used to distinguish between repeats of the same type of study
      event for a single subject.
    comments:
    - 'Conditional

      If the StudyEventDef/@Repeating attribute has the value "Yes" and there is more
      than one ClinicalData/SubjectData/StudyEventData/@OID element, the StudyEventRepeatKey
      attribute must be provided. Must be unique among the set of ClinicalData/SubjectData/StudyEventData/@OID
      elements. The StudyEventRepeatKey must be present only when the StudyEventDef/@Repeating
      attribute has the value "Yes".'
    domain_of:
    - StudyEventData
    - KeySet
    range: repeatKey
  transactionType:
    name: transactionType
    description: Identifies the transaction type when /ODM/@FileType is Transactional
      and there is no child element.
    comments:
    - 'Conditional Required when contained within an ODM Transactional file and the
      StudyEventData element has no child element content the TransactionType must
      be specified.

      When importing data from an ODM Snapshot file, the TransactionType attribute
      must not affect the processing of any of the StudyEvent child elements.'
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
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
  studyEventOID:
    name: studyEventOID
    description: Reference to the StudyEventDef . The StudyEventOID and StudyEventRepeatKey
      are used together to identify a particular study event. This pair of values
      uniquely identifies a StudyEvent within the containing subject. The StudyEventRepeatKey
      is present if and only if the StudyEventDef is repeating.
    comments:
    - 'Required

      Must match a StudyEventGroupDef/@OID or StudyEventDef/@OID for the MetaDataVersion
      /@OID value that matches the ClinicalData/@MetaDataVersionOID attribute.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyEventOID
    owner: StudyEventData
    domain_of:
    - StudyEventRef
    - AbsoluteTimingConstraint
    - StudyEventData
    - KeySet
    range: oidref
    required: true
  studyEventRepeatKey:
    name: studyEventRepeatKey
    description: A key used to distinguish between repeats of the same type of study
      event for a single subject.
    comments:
    - 'Conditional

      If the StudyEventDef/@Repeating attribute has the value "Yes" and there is more
      than one ClinicalData/SubjectData/StudyEventData/@OID element, the StudyEventRepeatKey
      attribute must be provided. Must be unique among the set of ClinicalData/SubjectData/StudyEventData/@OID
      elements. The StudyEventRepeatKey must be present only when the StudyEventDef/@Repeating
      attribute has the value "Yes".'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyEventRepeatKey
    owner: StudyEventData
    domain_of:
    - StudyEventData
    - KeySet
    range: repeatKey
  transactionType:
    name: transactionType
    description: Identifies the transaction type when /ODM/@FileType is Transactional
      and there is no child element.
    comments:
    - 'Conditional Required when contained within an ODM Transactional file and the
      StudyEventData element has no child element content the TransactionType must
      be specified.

      When importing data from an ODM Snapshot file, the TransactionType attribute
      must not affect the processing of any of the StudyEvent child elements.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: transactionType
    owner: StudyEventData
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  itemGroupData:
    name: itemGroupData
    description: 'ItemGroupData reference: Clinical data corresponding to an ItemGroupRef
      defined in the active MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: itemGroupData
    owner: StudyEventData
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
    identifier: false
    alias: query
    owner: StudyEventData
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
    identifier: false
    alias: auditRecord
    owner: StudyEventData
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
    identifier: false
    alias: signature
    owner: StudyEventData
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
    identifier: false
    alias: annotation
    owner: StudyEventData
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
class_uri: odm:StudyEventData

```
</details>