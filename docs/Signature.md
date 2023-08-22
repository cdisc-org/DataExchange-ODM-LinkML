# Class: Signature


_An electronic signature applies to a collection of clinical data. This indicates that some user accepts legal responsibility for that data. See 21 CFR Part 11. The signature identifies the person signing, the location of signing, the signature meaning (via the referenced SignatureDef), the date and time of signing, and (in the case of a digital signature) an encrypted hash of the included data._





URI: [odm:Signature](http://www.cdisc.org/ns/odm/v2.0/Signature)



```mermaid
 classDiagram
    class Signature
      Signature : DateTimeStampRef
        
          Signature --|> DateTimeStamp : DateTimeStampRef
        
      Signature : ID
        
      Signature : LocationRefRef
        
          Signature --|> LocationRef : LocationRefRef
        
      Signature : SignatureRefRef
        
          Signature --|> SignatureRef : SignatureRefRef
        
      Signature : UserRefRef
        
          Signature --|> UserRef : UserRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ID](ID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier for the leaf that is referenced. | direct |
| [UserRefRef](UserRefRef.md) | 0..1 <br/> [UserRef](UserRef.md) | UserRef reference: A reference to information about a specific user of a clin... | direct |
| [LocationRefRef](LocationRefRef.md) | 0..1 <br/> [LocationRef](LocationRef.md) | LocationRef reference: A reference to the user's physical location. | direct |
| [SignatureRefRef](SignatureRefRef.md) | 0..1 <br/> [SignatureRef](SignatureRef.md) | SignatureRef reference: A reference to the signature meaning. | direct |
| [DateTimeStampRef](DateTimeStampRef.md) | 0..1 <br/> [DateTimeStamp](DateTimeStamp.md) | DateTimeStamp reference: Date and time when an action was performed. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReferenceData](ReferenceData.md) | [SignatureRefRef](SignatureRefRef.md) | range | [Signature](Signature.md) |
| [ClinicalData](ClinicalData.md) | [SignatureRefRef](SignatureRefRef.md) | range | [Signature](Signature.md) |
| [SubjectData](SubjectData.md) | [SignatureRefRef](SignatureRefRef.md) | range | [Signature](Signature.md) |
| [StudyEventData](StudyEventData.md) | [SignatureRefRef](SignatureRefRef.md) | range | [Signature](Signature.md) |
| [ItemGroupData](ItemGroupData.md) | [SignatureRefRef](SignatureRefRef.md) | range | [Signature](Signature.md) |
| [ItemData](ItemData.md) | [SignatureRefRef](SignatureRefRef.md) | range | [Signature](Signature.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Signature](https://wiki.cdisc.org/display/ODM2/Signature)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Signature |
| native | odm:Signature |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Signature
description: An electronic signature applies to a collection of clinical data. This
  indicates that some user accepts legal responsibility for that data. See 21 CFR
  Part 11. The signature identifies the person signing, the location of signing, the
  signature meaning (via the referenced SignatureDef), the date and time of signing,
  and (in the case of a digital signature) an encrypted hash of the included data.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Signature
slots:
- ID
- UserRefRef
- LocationRefRef
- SignatureRefRef
- DateTimeStampRef
slot_usage:
  ID:
    name: ID
    domain_of:
    - Leaf
    - Signature
    - Annotation
    range: oid
  UserRefRef:
    name: UserRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: UserRef
    maximum_cardinality: 1
  LocationRefRef:
    name: LocationRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: LocationRef
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
    range: SignatureRef
    maximum_cardinality: 1
  DateTimeStampRef:
    name: DateTimeStampRef
    domain_of:
    - AuditRecord
    - Signature
    range: DateTimeStamp
    maximum_cardinality: 1
class_uri: odm:Signature

```
</details>

### Induced

<details>
```yaml
name: Signature
description: An electronic signature applies to a collection of clinical data. This
  indicates that some user accepts legal responsibility for that data. See 21 CFR
  Part 11. The signature identifies the person signing, the location of signing, the
  signature meaning (via the referenced SignatureDef), the date and time of signing,
  and (in the case of a digital signature) an encrypted hash of the included data.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Signature
slot_usage:
  ID:
    name: ID
    domain_of:
    - Leaf
    - Signature
    - Annotation
    range: oid
  UserRefRef:
    name: UserRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: UserRef
    maximum_cardinality: 1
  LocationRefRef:
    name: LocationRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: LocationRef
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
    range: SignatureRef
    maximum_cardinality: 1
  DateTimeStampRef:
    name: DateTimeStampRef
    domain_of:
    - AuditRecord
    - Signature
    range: DateTimeStamp
    maximum_cardinality: 1
attributes:
  ID:
    name: ID
    description: Unique identifier for the leaf that is referenced.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: ID
    owner: Signature
    domain_of:
    - Leaf
    - Signature
    - Annotation
    range: oid
    required: true
  UserRefRef:
    name: UserRefRef
    description: 'UserRef reference: A reference to information about a specific user
      of a clinical data collection or data management system.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: UserRefRef
    owner: Signature
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: UserRef
    maximum_cardinality: 1
  LocationRefRef:
    name: LocationRefRef
    description: 'LocationRef reference: A reference to the user''s physical location.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: LocationRefRef
    owner: Signature
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: LocationRef
    maximum_cardinality: 1
  SignatureRefRef:
    name: SignatureRefRef
    description: 'SignatureRef reference: A reference to the signature meaning.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SignatureRefRef
    owner: Signature
    domain_of:
    - ReferenceData
    - ClinicalData
    - SubjectData
    - StudyEventData
    - ItemGroupData
    - ItemData
    - Signature
    range: SignatureRef
    maximum_cardinality: 1
  DateTimeStampRef:
    name: DateTimeStampRef
    description: 'DateTimeStamp reference: Date and time when an action was performed.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DateTimeStampRef
    owner: Signature
    domain_of:
    - AuditRecord
    - Signature
    range: DateTimeStamp
    maximum_cardinality: 1
class_uri: odm:Signature

```
</details>