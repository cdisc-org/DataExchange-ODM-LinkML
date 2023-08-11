# Class: AdminData



URI: [odm:AdminData](http://www.cdisc.org/ns/odm/v2.0/AdminData)



```mermaid
 classDiagram
    class AdminData
      AdminData : LocationRefRef
        
          AdminData --|> Location : LocationRefRef
        
      AdminData : OrganizationRef
        
          AdminData --|> Organization : OrganizationRef
        
      AdminData : SignatureDefRef
        
          AdminData --|> SignatureDef : SignatureDefRef
        
      AdminData : StudyOID
        
      AdminData : UserRefRef
        
          AdminData --|> User : UserRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyOID](StudyOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [UserRefRef](UserRefRef.md) | 0..* <br/> [User](User.md) |  | direct |
| [OrganizationRef](OrganizationRef.md) | 0..* <br/> [Organization](Organization.md) |  | direct |
| [LocationRefRef](LocationRefRef.md) | 0..* <br/> [Location](Location.md) |  | direct |
| [SignatureDefRef](SignatureDefRef.md) | 0..* <br/> [SignatureDef](SignatureDef.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ODMFileMetadata](ODMFileMetadata.md) | [AdminDataRef](AdminDataRef.md) | range | [AdminData](AdminData.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/AdminData](https://wiki.cdisc.org/display/ODM2/AdminData)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:AdminData |
| native | odm:AdminData |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AdminData
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/AdminData
slots:
- StudyOID
- UserRefRef
- OrganizationRef
- LocationRefRef
- SignatureDefRef
slot_usage:
  StudyOID:
    name: StudyOID
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
  UserRefRef:
    name: UserRefRef
    multivalued: true
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: User
    inlined: true
    inlined_as_list: true
  OrganizationRef:
    name: OrganizationRef
    multivalued: true
    domain_of:
    - AdminData
    range: Organization
    inlined: true
    inlined_as_list: true
  LocationRefRef:
    name: LocationRefRef
    multivalued: true
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: Location
    inlined: true
    inlined_as_list: true
  SignatureDefRef:
    name: SignatureDefRef
    multivalued: true
    domain_of:
    - AdminData
    range: SignatureDef
    inlined: true
    inlined_as_list: true
class_uri: odm:AdminData

```
</details>

### Induced

<details>
```yaml
name: AdminData
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/AdminData
slot_usage:
  StudyOID:
    name: StudyOID
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
  UserRefRef:
    name: UserRefRef
    multivalued: true
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: User
    inlined: true
    inlined_as_list: true
  OrganizationRef:
    name: OrganizationRef
    multivalued: true
    domain_of:
    - AdminData
    range: Organization
    inlined: true
    inlined_as_list: true
  LocationRefRef:
    name: LocationRefRef
    multivalued: true
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: Location
    inlined: true
    inlined_as_list: true
  SignatureDefRef:
    name: SignatureDefRef
    multivalued: true
    domain_of:
    - AdminData
    range: SignatureDef
    inlined: true
    inlined_as_list: true
attributes:
  StudyOID:
    name: StudyOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StudyOID
    owner: AdminData
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
  UserRefRef:
    name: UserRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: UserRefRef
    owner: AdminData
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: User
    inlined: true
    inlined_as_list: true
  OrganizationRef:
    name: OrganizationRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: OrganizationRef
    owner: AdminData
    domain_of:
    - AdminData
    range: Organization
    inlined: true
    inlined_as_list: true
  LocationRefRef:
    name: LocationRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: LocationRefRef
    owner: AdminData
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: Location
    inlined: true
    inlined_as_list: true
  SignatureDefRef:
    name: SignatureDefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: SignatureDefRef
    owner: AdminData
    domain_of:
    - AdminData
    range: SignatureDef
    inlined: true
    inlined_as_list: true
class_uri: odm:AdminData

```
</details>