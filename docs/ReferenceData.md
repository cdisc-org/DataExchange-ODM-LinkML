# Class: ReferenceData

_Reference data provides information on how to interpret clinical data. For example, reference data might include lab normal ranges. For a study that uses CDISC standards, reference data might include SDTM Trial Design datasets._




URI: [odm:ReferenceData](http://www.cdisc.org/ns/odm/v2.0/ReferenceData)


```mermaid
erDiagram
ReferenceData {
    oidref studyOID  
    oidref metaDataVersionOID  
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
Query {
    oid oID  
    QuerySourceType source  
    text target  
    QueryType type  
    QueryStateType state  
    datetime lastUpdateDatetime  
    nameType name  
}

ReferenceData ||--}o ItemGroupData : "itemGroupData"
ReferenceData ||--|o AuditRecord : "auditRecord"
ReferenceData ||--|o Signature : "signature"
ReferenceData ||--|o Annotation : "annotation"
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
Query ||--|o Value : "value"
Query ||--}o AuditRecord : "auditRecord"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyOID](studyOID.md) | 1..1 <br/> [oidref](oidref.md) | References the Study that defines the metadata for this reference data. | direct |
| [metaDataVersionOID](metaDataVersionOID.md) | 1..1 <br/> [oidref](oidref.md) | References the MetaDataVersion (within the above Study) for this reference da... | direct |
| [itemGroupData](itemGroupData.md) | 0..* <br/> [ItemGroupData](ItemGroupData.md) | ItemGroupData reference: Clinical data corresponding to an ItemGroupRef defin... | direct |
| [auditRecord](auditRecord.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... | direct |
| [signature](signature.md) | 0..1 <br/> [Signature](Signature.md) | Signature reference: An electronic signature applies to a collection of clini... | direct |
| [annotation](annotation.md) | 0..1 <br/> [Annotation](Annotation.md) | Annotation reference: A general note about clinical data. If an annotation ha... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ODMFileMetadata](ODMFileMetadata.md) | [referenceData](referenceData.md) | range | [ReferenceData](ReferenceData.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/ReferenceData](https://wiki.cdisc.org/display/PUB/ReferenceData)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ReferenceData |
| native | odm:ReferenceData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferenceData
description: Reference data provides information on how to interpret clinical data.
  For example, reference data might include lab normal ranges. For a study that uses
  CDISC standards, reference data might include SDTM Trial Design datasets.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ReferenceData
rank: 1000
slots:
- studyOID
- metaDataVersionOID
- itemGroupData
- auditRecord
- signature
- annotation
slot_usage:
  studyOID:
    name: studyOID
    description: References the Study that defines the metadata for this reference
      data.
    comments:
    - 'Required

      range: oidref

      Must match the OID of a Study element with a MetaDataVersion OID attribute that
      matches the MetaDataVersionOID.'
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
    required: true
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion (within the above Study) for this
      reference data. All metadata references (OIDs) occurring within this ReferenceData
      element refer to definitions within the selected metadata version. Signature
      elements nested within ReferenceData have no meaning, and should be ignored.
      The TransactionType attribute behaves the same within ReferenceData as it does
      within ClinicalData.
    comments:
    - 'Required

      range: oidref

      Must match the OID of a MetaDataVersion within a Study element with an OID attribute
      that matches the StudyOID.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
    required: true
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
class_uri: odm:ReferenceData

```
</details>

### Induced

<details>
```yaml
name: ReferenceData
description: Reference data provides information on how to interpret clinical data.
  For example, reference data might include lab normal ranges. For a study that uses
  CDISC standards, reference data might include SDTM Trial Design datasets.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ReferenceData
rank: 1000
slot_usage:
  studyOID:
    name: studyOID
    description: References the Study that defines the metadata for this reference
      data.
    comments:
    - 'Required

      range: oidref

      Must match the OID of a Study element with a MetaDataVersion OID attribute that
      matches the MetaDataVersionOID.'
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
    required: true
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion (within the above Study) for this
      reference data. All metadata references (OIDs) occurring within this ReferenceData
      element refer to definitions within the selected metadata version. Signature
      elements nested within ReferenceData have no meaning, and should be ignored.
      The TransactionType attribute behaves the same within ReferenceData as it does
      within ClinicalData.
    comments:
    - 'Required

      range: oidref

      Must match the OID of a MetaDataVersion within a Study element with an OID attribute
      that matches the StudyOID.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
    required: true
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
    description: References the Study that defines the metadata for this reference
      data.
    comments:
    - 'Required

      range: oidref

      Must match the OID of a Study element with a MetaDataVersion OID attribute that
      matches the MetaDataVersionOID.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyOID
    owner: ReferenceData
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
    required: true
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion (within the above Study) for this
      reference data. All metadata references (OIDs) occurring within this ReferenceData
      element refer to definitions within the selected metadata version. Signature
      elements nested within ReferenceData have no meaning, and should be ignored.
      The TransactionType attribute behaves the same within ReferenceData as it does
      within ClinicalData.
    comments:
    - 'Required

      range: oidref

      Must match the OID of a MetaDataVersion within a Study element with an OID attribute
      that matches the StudyOID.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: metaDataVersionOID
    owner: ReferenceData
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
    required: true
  itemGroupData:
    name: itemGroupData
    description: 'ItemGroupData reference: Clinical data corresponding to an ItemGroupRef
      defined in the active MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: itemGroupData
    owner: ReferenceData
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
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
    owner: ReferenceData
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
    owner: ReferenceData
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
    owner: ReferenceData
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
class_uri: odm:ReferenceData

```
</details>