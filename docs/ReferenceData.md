# Class: ReferenceData

_Reference data provides information on how to interpret clinical data. For example, reference data might include lab normal ranges. For a study that uses CDISC standards, reference data might include SDTM Trial Design datasets._




URI: [odm:ReferenceData](http://www.cdisc.org/ns/odm/v2.0/ReferenceData)


```mermaid
erDiagram
ReferenceData {
    oidref StudyOID  
    oidref MetaDataVersionOID  
}
Annotation {
    positiveInteger SeqNum  
    TransactionType TransactionTypeRef  
    oid ID  
}
Flag {

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
Comment {
    CommentType SponsorOrSite  
}
Signature {
    oid ID  
}
DateTimeStamp {
    datetime content  
}
SignatureRef {
    oidref SignatureOID  
}
LocationRef {
    oidref LocationOID  
}
UserRef {
    oidref UserOID  
}
AuditRecord {
    EditPointType EditPoint  
    YesOrNo UsedMethod  
}
SourceID {
    text content  
}
ReasonForChange {
    text content  
}
ItemGroupData {
    oidref ItemGroupOID  
    repeatKey ItemGroupRepeatKey  
    TransactionType TransactionTypeRef  
    positiveInteger ItemGroupDataSeq  
}
ItemData {
    oidref ItemOID  
    TransactionType TransactionTypeRef  
    YesOnly IsNull  
}
Query {
    oid OID  
    QuerySourceType Source  
    text Target  
    QueryType Type  
    QueryStateType State  
    datetime LastUpdateDatetime  
    name Name  
}

ReferenceData ||--}o ItemGroupData : "ItemGroupDataRef"
ReferenceData ||--|o AuditRecord : "AuditRecordRef"
ReferenceData ||--|o Signature : "SignatureRefRef"
ReferenceData ||--|o Annotation : "AnnotationRef"
Annotation ||--|o Comment : "CommentRef"
Annotation ||--}o Coding : "CodingRef"
Annotation ||--}o Flag : "FlagRef"
Flag ||--|o FlagValue : "FlagValueRef"
Flag ||--|o FlagType : "FlagTypeRef"
Comment ||--}o TranslatedText : "TranslatedTextRef"
Signature ||--|o UserRef : "UserRefRef"
Signature ||--|o LocationRef : "LocationRefRef"
Signature ||--|o SignatureRef : "SignatureRefRef"
Signature ||--|o DateTimeStamp : "DateTimeStampRef"
AuditRecord ||--|o UserRef : "UserRefRef"
AuditRecord ||--|o LocationRef : "LocationRefRef"
AuditRecord ||--|o DateTimeStamp : "DateTimeStampRef"
AuditRecord ||--|o ReasonForChange : "ReasonForChangeRef"
AuditRecord ||--|o SourceID : "SourceIDRef"
ItemGroupData ||--}o Query : "QueryRef"
ItemGroupData ||--}o ItemGroupData : "ItemGroupDataRef"
ItemGroupData ||--}o ItemData : "ItemDataRef"
ItemGroupData ||--|o AuditRecord : "AuditRecordRef"
ItemGroupData ||--|o Signature : "SignatureRefRef"
ItemGroupData ||--|o Annotation : "AnnotationRef"
ItemData ||--}o Value : "ValueRef"
ItemData ||--}o Query : "QueryRef"
ItemData ||--|o AuditRecord : "AuditRecordRef"
ItemData ||--|o Signature : "SignatureRefRef"
ItemData ||--|o Annotation : "AnnotationRef"
Query ||--|o Value : "ValueRef"
Query ||--}o AuditRecord : "AuditRecordRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyOID](StudyOID.md) | 1..1 <br/> [oidref](oidref.md) | References the Study that defines the metadata for this reference data. | direct |
| [MetaDataVersionOID](MetaDataVersionOID.md) | 1..1 <br/> [oidref](oidref.md) | References the MetaDataVersion (within the above Study) for this reference da... | direct |
| [ItemGroupDataRef](ItemGroupDataRef.md) | 0..* <br/> [ItemGroupData](ItemGroupData.md) | ItemGroupData reference: Clinical data corresponding to an ItemGroupRef defin... | direct |
| [AuditRecordRef](AuditRecordRef.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... | direct |
| [SignatureRefRef](SignatureRefRef.md) | 0..1 <br/> [Signature](Signature.md) | SignatureRef reference: A reference to the signature meaning. | direct |
| [AnnotationRef](AnnotationRef.md) | 0..1 <br/> [Annotation](Annotation.md) | Annotation reference: A general note about clinical data. If an annotation ha... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ODMFileMetadata](ODMFileMetadata.md) | [ReferenceDataRef](ReferenceDataRef.md) | range | [ReferenceData](ReferenceData.md) |






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
- StudyOID
- MetaDataVersionOID
- ItemGroupDataRef
- AuditRecordRef
- SignatureRefRef
- AnnotationRef
slot_usage:
  StudyOID:
    name: StudyOID
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
  MetaDataVersionOID:
    name: MetaDataVersionOID
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
  ItemGroupDataRef:
    name: ItemGroupDataRef
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  AuditRecordRef:
    name: AuditRecordRef
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
  SignatureRefRef:
    name: SignatureRefRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Signature
    range: Signature
    maximum_cardinality: 1
  AnnotationRef:
    name: AnnotationRef
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
  StudyOID:
    name: StudyOID
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
  MetaDataVersionOID:
    name: MetaDataVersionOID
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
  ItemGroupDataRef:
    name: ItemGroupDataRef
    multivalued: true
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  AuditRecordRef:
    name: AuditRecordRef
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
  SignatureRefRef:
    name: SignatureRefRef
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Signature
    range: Signature
    maximum_cardinality: 1
  AnnotationRef:
    name: AnnotationRef
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
  StudyOID:
    name: StudyOID
    description: References the Study that defines the metadata for this reference
      data.
    comments:
    - 'Required

      range: oidref

      Must match the OID of a Study element with a MetaDataVersion OID attribute that
      matches the MetaDataVersionOID.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StudyOID
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
  MetaDataVersionOID:
    name: MetaDataVersionOID
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
    alias: MetaDataVersionOID
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
  ItemGroupDataRef:
    name: ItemGroupDataRef
    description: 'ItemGroupData reference: Clinical data corresponding to an ItemGroupRef
      defined in the active MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemGroupDataRef
    owner: ReferenceData
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  AuditRecordRef:
    name: AuditRecordRef
    description: 'AuditRecord reference: An AuditRecord carries information pertaining
      to the creation, deletion, or modification of clinical data. This information
      includes who performed that action, and where, when, and why that action was
      performed.AuditRecord information describes a change to clinical data, but is
      not itself clinical data. The value of some clinical data can always be changed
      by a subsequent transaction, but history cannot be changed, only added to.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: AuditRecordRef
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
  SignatureRefRef:
    name: SignatureRefRef
    description: 'SignatureRef reference: A reference to the signature meaning.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SignatureRefRef
    owner: ReferenceData
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Signature
    range: Signature
    maximum_cardinality: 1
  AnnotationRef:
    name: AnnotationRef
    description: 'Annotation reference: A general note about clinical data. If an
      annotation has both a comment and flags, the flags should be related to the
      comment.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: AnnotationRef
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