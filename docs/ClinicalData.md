# Class: ClinicalData


_Clinical data for 1 or more subjects._





URI: [odm:ClinicalData](http://www.cdisc.org/ns/odm/v2.0/ClinicalData)



```mermaid
 classDiagram
    class ClinicalData
      ClinicalData : AnnotationRef
        
          ClinicalData --|> Annotation : AnnotationRef
        
      ClinicalData : AuditRecordRef
        
          ClinicalData --|> AuditRecord : AuditRecordRef
        
      ClinicalData : ItemGroupDataRef
        
          ClinicalData --|> ItemGroupData : ItemGroupDataRef
        
      ClinicalData : MetaDataVersionOID
        
      ClinicalData : QueryRef
        
          ClinicalData --|> Query : QueryRef
        
      ClinicalData : SignatureRefRef
        
          ClinicalData --|> Signature : SignatureRefRef
        
      ClinicalData : StudyOID
        
      ClinicalData : SubjectDataRef
        
          ClinicalData --|> SubjectData : SubjectDataRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyOID](StudyOID.md) | 1..1 <br/> [oidref](oidref.md) | References the Study that uses the data nested within this element. | direct |
| [MetaDataVersionOID](MetaDataVersionOID.md) | 1..1 <br/> [oidref](oidref.md) | References the MetaDataVersion (within the above Study) that governs the data... | direct |
| [SubjectDataRef](SubjectDataRef.md) | 0..* <br/> [SubjectData](SubjectData.md) | SubjectData reference: Clinical data for a single subject. | direct |
| [ItemGroupDataRef](ItemGroupDataRef.md) | 0..* <br/> [ItemGroupData](ItemGroupData.md) | ItemGroupData reference: Clinical data corresponding to an ItemGroupRef defin... | direct |
| [QueryRef](QueryRef.md) | 0..* <br/> [Query](Query.md) | Query reference: The Query element represents a request for clarification on ... | direct |
| [AuditRecordRef](AuditRecordRef.md) | 0..1 <br/> [AuditRecord](AuditRecord.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... | direct |
| [SignatureRefRef](SignatureRefRef.md) | 0..1 <br/> [Signature](Signature.md) | SignatureRef reference: None | direct |
| [AnnotationRef](AnnotationRef.md) | 0..1 <br/> [Annotation](Annotation.md) | Annotation reference: A general note about clinical data. If an annotation ha... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ODMFileMetadata](ODMFileMetadata.md) | [ClinicalDataRef](ClinicalDataRef.md) | range | [ClinicalData](ClinicalData.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/ClinicalData](https://wiki.cdisc.org/display/ODM2/ClinicalData)

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
- https://wiki.cdisc.org/display/ODM2/ClinicalData
slots:
- StudyOID
- MetaDataVersionOID
- SubjectDataRef
- ItemGroupDataRef
- QueryRef
- AuditRecordRef
- SignatureRefRef
- AnnotationRef
slot_usage:
  StudyOID:
    name: StudyOID
    description: References the Study that uses the data nested within this element.
    comments:
    - 'Required

      range:oidref

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
    range: oidref
    required: true
  MetaDataVersionOID:
    name: MetaDataVersionOID
    description: References the MetaDataVersion (within the above Study) that governs
      the data nested within this element. The StudyOID and MetaDataVersionOID attributes
      select a particular metadata version. All metadata references (OIDs) occurring
      within this ClinicalData element refer to definitions within the selected metadata
      version.
    comments:
    - 'Required

      range:oidref

      Must match a MetaDataVersions/@OID value contained in the Study element.'
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
  SubjectDataRef:
    name: SubjectDataRef
    multivalued: true
    domain_of:
    - ClinicalData
    range: SubjectData
    inlined: true
    inlined_as_list: true
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
- https://wiki.cdisc.org/display/ODM2/ClinicalData
slot_usage:
  StudyOID:
    name: StudyOID
    description: References the Study that uses the data nested within this element.
    comments:
    - 'Required

      range:oidref

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
    range: oidref
    required: true
  MetaDataVersionOID:
    name: MetaDataVersionOID
    description: References the MetaDataVersion (within the above Study) that governs
      the data nested within this element. The StudyOID and MetaDataVersionOID attributes
      select a particular metadata version. All metadata references (OIDs) occurring
      within this ClinicalData element refer to definitions within the selected metadata
      version.
    comments:
    - 'Required

      range:oidref

      Must match a MetaDataVersions/@OID value contained in the Study element.'
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
  SubjectDataRef:
    name: SubjectDataRef
    multivalued: true
    domain_of:
    - ClinicalData
    range: SubjectData
    inlined: true
    inlined_as_list: true
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
  StudyOID:
    name: StudyOID
    description: References the Study that uses the data nested within this element.
    comments:
    - 'Required

      range:oidref

      Must match a Study/@OID value.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StudyOID
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
    range: oidref
    required: true
  MetaDataVersionOID:
    name: MetaDataVersionOID
    description: References the MetaDataVersion (within the above Study) that governs
      the data nested within this element. The StudyOID and MetaDataVersionOID attributes
      select a particular metadata version. All metadata references (OIDs) occurring
      within this ClinicalData element refer to definitions within the selected metadata
      version.
    comments:
    - 'Required

      range:oidref

      Must match a MetaDataVersions/@OID value contained in the Study element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: MetaDataVersionOID
    owner: ClinicalData
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
  SubjectDataRef:
    name: SubjectDataRef
    description: 'SubjectData reference: Clinical data for a single subject.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: SubjectDataRef
    owner: ClinicalData
    domain_of:
    - ClinicalData
    range: SubjectData
    inlined: true
    inlined_as_list: true
  ItemGroupDataRef:
    name: ItemGroupDataRef
    description: 'ItemGroupData reference: Clinical data corresponding to an ItemGroupRef
      defined in the active MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemGroupDataRef
    owner: ClinicalData
    domain_of:
    - ReferenceData
    - ClinicalData
    - StudyEventData
    - ItemGroupData
    range: ItemGroupData
    inlined: true
    inlined_as_list: true
  QueryRef:
    name: QueryRef
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
    alias: QueryRef
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
  SignatureRefRef:
    name: SignatureRefRef
    description: 'SignatureRef reference: None'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SignatureRefRef
    owner: ClinicalData
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