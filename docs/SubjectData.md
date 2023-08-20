# Class: SubjectData


_Clinical data for a single subject._





URI: [odm:SubjectData](http://www.cdisc.org/ns/odm/v2.0/SubjectData)



```mermaid
 classDiagram
    class SubjectData
      SubjectData : AnnotationRef
        
          SubjectData --|> Annotation : AnnotationRef
        
      SubjectData : AuditRecordRef
        
          SubjectData --|> AuditRecord : AuditRecordRef
        
      SubjectData : InvestigatorRefRef
        
          SubjectData --|> InvestigatorRef : InvestigatorRefRef
        
      SubjectData : QueryRef
        
          SubjectData --|> Query : QueryRef
        
      SubjectData : SignatureRefRef
        
          SubjectData --|> Signature : SignatureRefRef
        
      SubjectData : SiteRefRef
        
          SubjectData --|> SiteRef : SiteRefRef
        
      SubjectData : StudyEventDataRef
        
          SubjectData --|> StudyEventData : StudyEventDataRef
        
      SubjectData : SubjectKey
        
      SubjectData : TransactionTypeRef
        
          SubjectData --|> TransactionType : TransactionTypeRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [SubjectKey](SubjectKey.md) | 1..1 <br/> [SubjectKey](SubjectKey.md) | Unique identifier for the Subject | direct |
| [TransactionTypeRef](TransactionTypeRef.md) | 0..1 <br/> [TransactionType](TransactionType.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... | direct |
| [InvestigatorRefRef](InvestigatorRefRef.md) | 0..1 <br/> [InvestigatorRef](InvestigatorRef.md) |  | direct |
| [SiteRefRef](SiteRefRef.md) | 0..1 <br/> [SiteRef](SiteRef.md) |  | direct |
| [StudyEventDataRef](StudyEventDataRef.md) | 0..* <br/> [StudyEventData](StudyEventData.md) |  | direct |
| [QueryRef](QueryRef.md) | 0..* <br/> [Query](Query.md) |  | direct |
| [AuditRecordRef](AuditRecordRef.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) |  | direct |
| [SignatureRefRef](SignatureRefRef.md) | 0..1 <br/> [Signature](Signature.md) |  | direct |
| [AnnotationRef](AnnotationRef.md) | 0..1 <br/> [Annotation](Annotation.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ClinicalData](ClinicalData.md) | [SubjectDataRef](SubjectDataRef.md) | range | [SubjectData](SubjectData.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/SubjectData](https://wiki.cdisc.org/display/ODM2/SubjectData)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SubjectData |
| native | odm:SubjectData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SubjectData
description: Clinical data for a single subject.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SubjectData
slots:
- SubjectKey
- TransactionTypeRef
- InvestigatorRefRef
- SiteRefRef
- StudyEventDataRef
- QueryRef
- AuditRecordRef
- SignatureRefRef
- AnnotationRef
slot_usage:
  SubjectKey:
    name: SubjectKey
    description: Unique identifier for the Subject.
    comments:
    - 'Required

      range:subjectKey

      For CDISC SDTM regulatory submission, the SubjectKey value should be the SDTM
      SUBJID variable value.'
    domain_of:
    - SubjectData
    - KeySet
    range: subjectKey
    required: true
  TransactionTypeRef:
    name: TransactionTypeRef
    description: Identifies the transaction type when /ODM/@FileType is Transactional
      and there is no child element.
    comments:
    - 'Conditional Required when contained within an ODM Transactional file and the
      SubjectData element has no child element content.

      enum values:(Insert | Update | Remove | Upsert | Context)

      When importing data from an ODM Snapshot file, the TransactionType attribute
      must not affect the processing of the SubjectData element.'
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  InvestigatorRefRef:
    name: InvestigatorRefRef
    domain_of:
    - SubjectData
    range: InvestigatorRef
    maximum_cardinality: 1
  SiteRefRef:
    name: SiteRefRef
    domain_of:
    - SubjectData
    range: SiteRef
    maximum_cardinality: 1
  StudyEventDataRef:
    name: StudyEventDataRef
    multivalued: true
    domain_of:
    - SubjectData
    range: StudyEventData
    inlined: true
    inlined_as_list: true
  QueryRef:
    name: QueryRef
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
class_uri: odm:SubjectData

```
</details>

### Induced

<details>
```yaml
name: SubjectData
description: Clinical data for a single subject.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SubjectData
slot_usage:
  SubjectKey:
    name: SubjectKey
    description: Unique identifier for the Subject.
    comments:
    - 'Required

      range:subjectKey

      For CDISC SDTM regulatory submission, the SubjectKey value should be the SDTM
      SUBJID variable value.'
    domain_of:
    - SubjectData
    - KeySet
    range: subjectKey
    required: true
  TransactionTypeRef:
    name: TransactionTypeRef
    description: Identifies the transaction type when /ODM/@FileType is Transactional
      and there is no child element.
    comments:
    - 'Conditional Required when contained within an ODM Transactional file and the
      SubjectData element has no child element content.

      enum values:(Insert | Update | Remove | Upsert | Context)

      When importing data from an ODM Snapshot file, the TransactionType attribute
      must not affect the processing of the SubjectData element.'
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  InvestigatorRefRef:
    name: InvestigatorRefRef
    domain_of:
    - SubjectData
    range: InvestigatorRef
    maximum_cardinality: 1
  SiteRefRef:
    name: SiteRefRef
    domain_of:
    - SubjectData
    range: SiteRef
    maximum_cardinality: 1
  StudyEventDataRef:
    name: StudyEventDataRef
    multivalued: true
    domain_of:
    - SubjectData
    range: StudyEventData
    inlined: true
    inlined_as_list: true
  QueryRef:
    name: QueryRef
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
  SubjectKey:
    name: SubjectKey
    description: Unique identifier for the Subject.
    comments:
    - 'Required

      range:subjectKey

      For CDISC SDTM regulatory submission, the SubjectKey value should be the SDTM
      SUBJID variable value.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SubjectKey
    owner: SubjectData
    domain_of:
    - SubjectData
    - KeySet
    range: subjectKey
    required: true
  TransactionTypeRef:
    name: TransactionTypeRef
    description: Identifies the transaction type when /ODM/@FileType is Transactional
      and there is no child element.
    comments:
    - 'Conditional Required when contained within an ODM Transactional file and the
      SubjectData element has no child element content.

      enum values:(Insert | Update | Remove | Upsert | Context)

      When importing data from an ODM Snapshot file, the TransactionType attribute
      must not affect the processing of the SubjectData element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: TransactionTypeRef
    owner: SubjectData
    domain_of:
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Annotation
    range: TransactionType
  InvestigatorRefRef:
    name: InvestigatorRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: InvestigatorRefRef
    owner: SubjectData
    domain_of:
    - SubjectData
    range: InvestigatorRef
    maximum_cardinality: 1
  SiteRefRef:
    name: SiteRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SiteRefRef
    owner: SubjectData
    domain_of:
    - SubjectData
    range: SiteRef
    maximum_cardinality: 1
  StudyEventDataRef:
    name: StudyEventDataRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: StudyEventDataRef
    owner: SubjectData
    domain_of:
    - SubjectData
    range: StudyEventData
    inlined: true
    inlined_as_list: true
  QueryRef:
    name: QueryRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: QueryRef
    owner: SubjectData
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
  AuditRecordRef:
    name: AuditRecordRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: AuditRecordRef
    owner: SubjectData
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
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SignatureRefRef
    owner: SubjectData
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
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: AnnotationRef
    owner: SubjectData
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
class_uri: odm:SubjectData

```
</details>