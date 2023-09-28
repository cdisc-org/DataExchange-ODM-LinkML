# Class: ItemData

_The ItemData element is used for transmission of the clinical data for an item. The model does not support repeating items within a single item group._




URI: [odm:ItemData](http://www.cdisc.org/ns/odm/v2.0/ItemData)


```mermaid
erDiagram
ItemData {
    oidref itemOID  
    TransactionType transactionType  
    YesOnly isNull  
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

ItemData ||--}o Value : "value"
ItemData ||--}o Query : "query"
ItemData ||--|o AuditRecord : "auditRecord"
ItemData ||--|o Signature : "signature"
ItemData ||--|o Annotation : "annotation"
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

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [itemOID](itemOID.md) | 1..1 <br/> [oidref](oidref.md) | Reference to an ItemDef in the MetaDataVersion identified in the ClinicalData... | direct |
| [transactionType](transactionType.md) | 0..1 <br/> [TransactionType](TransactionType.md) | Records the TransactionType for this ItemData instance in the source system. | direct |
| [isNull](isNull.md) | 0..1 <br/> [YesOnly](YesOnly.md) | Flag specifying that an item's value is to be set to null. In the interest of... | direct |
| [value](value.md) | 0..* <br/> [Value](Value.md) | Human-readable designation of the trial phase. | direct |
| [query](query.md) | 0..* <br/> [Query](Query.md) | Query reference: The Query element represents a request for clarification on ... | direct |
| [auditRecord](auditRecord.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... | direct |
| [signature](signature.md) | 0..1 <br/> [Signature](Signature.md) | Signature reference: An electronic signature applies to a collection of clini... | direct |
| [annotation](annotation.md) | 0..1 <br/> [Annotation](Annotation.md) | Annotation reference: A general note about clinical data. If an annotation ha... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemGroupData](ItemGroupData.md) | [itemData](itemData.md) | range | [ItemData](ItemData.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/ItemData](https://wiki.cdisc.org/display/PUB/ItemData)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemData |
| native | odm:ItemData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemData
description: The ItemData element is used for transmission of the clinical data for
  an item. The model does not support repeating items within a single item group.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ItemData
rank: 1000
slots:
- itemOID
- transactionType
- isNull
- value
- query
- auditRecord
- signature
- annotation
slot_usage:
  itemOID:
    name: itemOID
    description: Reference to an ItemDef in the MetaDataVersion identified in the
      ClinicalData element. The referenced ItemDef defines the DataType of this item.
      The ItemOID attribute is used to identify a particular item definition. This
      value uniquely identifies an Item within the containing ItemGroup.
    comments:
    - Required
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
    required: true
  transactionType:
    name: transactionType
    description: Records the TransactionType for this ItemData instance in the source
      system.
    comments:
    - Conditional Required on the ItemData element, or one of its ancestor elements,
      when ODM/@FileType has the value "Transactional".
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  isNull:
    name: isNull
    description: Flag specifying that an item's value is to be set to null. In the
      interest of creating non-verbose XML instances, one should not use ItemData
      elements with IsNull set to "Yes" to indicate uncollected data. The better practice
      is to transmit only collected data. For use cases where data traceability is
      important, providing ItemData elements with IsNull="Yes" maybe be useful. It
      is not necessary to provide an ItemData element with IsNull set to "Yes" in
      cases where the source system would not create a record.
    comments:
    - Conditional If the child element ItemData/Value is present, the IsNull attribute
      must not be set. If IsNull is set, the child element ItemData/Value must not
      be present.
    domain_of:
    - ItemData
    range: YesOnly
  value:
    name: value
    multivalued: true
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: Value
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
class_uri: odm:ItemData

```
</details>

### Induced

<details>
```yaml
name: ItemData
description: The ItemData element is used for transmission of the clinical data for
  an item. The model does not support repeating items within a single item group.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ItemData
rank: 1000
slot_usage:
  itemOID:
    name: itemOID
    description: Reference to an ItemDef in the MetaDataVersion identified in the
      ClinicalData element. The referenced ItemDef defines the DataType of this item.
      The ItemOID attribute is used to identify a particular item definition. This
      value uniquely identifies an Item within the containing ItemGroup.
    comments:
    - Required
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
    required: true
  transactionType:
    name: transactionType
    description: Records the TransactionType for this ItemData instance in the source
      system.
    comments:
    - Conditional Required on the ItemData element, or one of its ancestor elements,
      when ODM/@FileType has the value "Transactional".
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  isNull:
    name: isNull
    description: Flag specifying that an item's value is to be set to null. In the
      interest of creating non-verbose XML instances, one should not use ItemData
      elements with IsNull set to "Yes" to indicate uncollected data. The better practice
      is to transmit only collected data. For use cases where data traceability is
      important, providing ItemData elements with IsNull="Yes" maybe be useful. It
      is not necessary to provide an ItemData element with IsNull set to "Yes" in
      cases where the source system would not create a record.
    comments:
    - Conditional If the child element ItemData/Value is present, the IsNull attribute
      must not be set. If IsNull is set, the child element ItemData/Value must not
      be present.
    domain_of:
    - ItemData
    range: YesOnly
  value:
    name: value
    multivalued: true
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: Value
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
  itemOID:
    name: itemOID
    description: Reference to an ItemDef in the MetaDataVersion identified in the
      ClinicalData element. The referenced ItemDef defines the DataType of this item.
      The ItemOID attribute is used to identify a particular item definition. This
      value uniquely identifies an Item within the containing ItemGroup.
    comments:
    - Required
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemOID
    owner: ItemData
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
    required: true
  transactionType:
    name: transactionType
    description: Records the TransactionType for this ItemData instance in the source
      system.
    comments:
    - Conditional Required on the ItemData element, or one of its ancestor elements,
      when ODM/@FileType has the value "Transactional".
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: transactionType
    owner: ItemData
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  isNull:
    name: isNull
    description: Flag specifying that an item's value is to be set to null. In the
      interest of creating non-verbose XML instances, one should not use ItemData
      elements with IsNull set to "Yes" to indicate uncollected data. The better practice
      is to transmit only collected data. For use cases where data traceability is
      important, providing ItemData elements with IsNull="Yes" maybe be useful. It
      is not necessary to provide an ItemData element with IsNull set to "Yes" in
      cases where the source system would not create a record.
    comments:
    - Conditional If the child element ItemData/Value is present, the IsNull attribute
      must not be set. If IsNull is set, the child element ItemData/Value must not
      be present.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: isNull
    owner: ItemData
    domain_of:
    - ItemData
    range: YesOnly
  value:
    name: value
    description: Human-readable designation of the trial phase.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: value
    owner: ItemData
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: Value
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
    owner: ItemData
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
    owner: ItemData
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
    owner: ItemData
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
    owner: ItemData
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
class_uri: odm:ItemData

```
</details>