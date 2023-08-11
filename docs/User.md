# Class: User



URI: [odm:User](http://www.cdisc.org/ns/odm/v2.0/User)



```mermaid
 classDiagram
    class User
      User : AddressRef
        
          User --|> Address : AddressRef
        
      User : FamilyNameRef
        
          User --|> FamilyName : FamilyNameRef
        
      User : FullNameRef
        
          User --|> FullName : FullNameRef
        
      User : GivenNameRef
        
          User --|> GivenName : GivenNameRef
        
      User : ImageRef
        
          User --|> Image : ImageRef
        
      User : LocationOID
        
      User : OID
        
      User : OrganizationOID
        
      User : PrefixRef
        
          User --|> Prefix : PrefixRef
        
      User : SuffixRef
        
          User --|> Suffix : SuffixRef
        
      User : TelecomRef
        
          User --|> Telecom : TelecomRef
        
      User : UserNameRef
        
          User --|> UserName : UserNameRef
        
      User : UserTypeRef
        
          User --|> UserType : UserTypeRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier of the version within the XML document | direct |
| [UserTypeRef](UserTypeRef.md) | 0..1 <br/> [UserType](UserType.md) |  | direct |
| [OrganizationOID](OrganizationOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [LocationOID](LocationOID.md) | 0..1 <br/> [Oidref](Oidref.md) |  | direct |
| [UserNameRef](UserNameRef.md) | 0..1 <br/> [UserName](UserName.md) |  | direct |
| [PrefixRef](PrefixRef.md) | 0..1 <br/> [Prefix](Prefix.md) |  | direct |
| [SuffixRef](SuffixRef.md) | 0..1 <br/> [Suffix](Suffix.md) |  | direct |
| [FullNameRef](FullNameRef.md) | 0..1 <br/> [FullName](FullName.md) |  | direct |
| [GivenNameRef](GivenNameRef.md) | 0..1 <br/> [GivenName](GivenName.md) |  | direct |
| [FamilyNameRef](FamilyNameRef.md) | 0..1 <br/> [FamilyName](FamilyName.md) |  | direct |
| [ImageRef](ImageRef.md) | 0..1 <br/> [Image](Image.md) |  | direct |
| [AddressRef](AddressRef.md) | 0..* <br/> [Address](Address.md) |  | direct |
| [TelecomRef](TelecomRef.md) | 0..* <br/> [Telecom](Telecom.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdminData](AdminData.md) | [UserRefRef](UserRefRef.md) | range | [User](User.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/User](https://wiki.cdisc.org/display/ODM2/User)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:User |
| native | odm:User |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: User
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/User
slots:
- OID
- UserTypeRef
- OrganizationOID
- LocationOID
- UserNameRef
- PrefixRef
- SuffixRef
- FullNameRef
- GivenNameRef
- FamilyNameRef
- ImageRef
- AddressRef
- TelecomRef
slot_usage:
  OID:
    name: OID
    domain_of:
    - Study
    - MetaDataVersion
    - Standard
    - ValueListDef
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - MethodDef
    - ConditionDef
    - CommentDef
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyParameter
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - ExceptionEvent
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  UserTypeRef:
    name: UserTypeRef
    domain_of:
    - User
    range: UserType
  OrganizationOID:
    name: OrganizationOID
    domain_of:
    - User
    - Location
    range: oidref
  LocationOID:
    name: LocationOID
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
  UserNameRef:
    name: UserNameRef
    domain_of:
    - User
    range: UserName
    maximum_cardinality: 1
  PrefixRef:
    name: PrefixRef
    domain_of:
    - User
    range: Prefix
    maximum_cardinality: 1
  SuffixRef:
    name: SuffixRef
    domain_of:
    - User
    range: Suffix
    maximum_cardinality: 1
  FullNameRef:
    name: FullNameRef
    domain_of:
    - User
    range: FullName
    maximum_cardinality: 1
  GivenNameRef:
    name: GivenNameRef
    domain_of:
    - User
    range: GivenName
    maximum_cardinality: 1
  FamilyNameRef:
    name: FamilyNameRef
    domain_of:
    - User
    range: FamilyName
    maximum_cardinality: 1
  ImageRef:
    name: ImageRef
    domain_of:
    - User
    range: Image
    maximum_cardinality: 1
  AddressRef:
    name: AddressRef
    multivalued: true
    domain_of:
    - User
    - Organization
    - Location
    range: Address
    inlined: true
    inlined_as_list: true
  TelecomRef:
    name: TelecomRef
    multivalued: true
    domain_of:
    - User
    - Organization
    - Location
    range: Telecom
    inlined: true
    inlined_as_list: true
class_uri: odm:User

```
</details>

### Induced

<details>
```yaml
name: User
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/User
slot_usage:
  OID:
    name: OID
    domain_of:
    - Study
    - MetaDataVersion
    - Standard
    - ValueListDef
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - MethodDef
    - ConditionDef
    - CommentDef
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyParameter
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - ExceptionEvent
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  UserTypeRef:
    name: UserTypeRef
    domain_of:
    - User
    range: UserType
  OrganizationOID:
    name: OrganizationOID
    domain_of:
    - User
    - Location
    range: oidref
  LocationOID:
    name: LocationOID
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
  UserNameRef:
    name: UserNameRef
    domain_of:
    - User
    range: UserName
    maximum_cardinality: 1
  PrefixRef:
    name: PrefixRef
    domain_of:
    - User
    range: Prefix
    maximum_cardinality: 1
  SuffixRef:
    name: SuffixRef
    domain_of:
    - User
    range: Suffix
    maximum_cardinality: 1
  FullNameRef:
    name: FullNameRef
    domain_of:
    - User
    range: FullName
    maximum_cardinality: 1
  GivenNameRef:
    name: GivenNameRef
    domain_of:
    - User
    range: GivenName
    maximum_cardinality: 1
  FamilyNameRef:
    name: FamilyNameRef
    domain_of:
    - User
    range: FamilyName
    maximum_cardinality: 1
  ImageRef:
    name: ImageRef
    domain_of:
    - User
    range: Image
    maximum_cardinality: 1
  AddressRef:
    name: AddressRef
    multivalued: true
    domain_of:
    - User
    - Organization
    - Location
    range: Address
    inlined: true
    inlined_as_list: true
  TelecomRef:
    name: TelecomRef
    multivalued: true
    domain_of:
    - User
    - Organization
    - Location
    range: Telecom
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier of the version within the XML document.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: User
    domain_of:
    - Study
    - MetaDataVersion
    - Standard
    - ValueListDef
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - MethodDef
    - ConditionDef
    - CommentDef
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyParameter
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - ExceptionEvent
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  UserTypeRef:
    name: UserTypeRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: UserTypeRef
    owner: User
    domain_of:
    - User
    range: UserType
  OrganizationOID:
    name: OrganizationOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: OrganizationOID
    owner: User
    domain_of:
    - User
    - Location
    range: oidref
  LocationOID:
    name: LocationOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: LocationOID
    owner: User
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
  UserNameRef:
    name: UserNameRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: UserNameRef
    owner: User
    domain_of:
    - User
    range: UserName
    maximum_cardinality: 1
  PrefixRef:
    name: PrefixRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: PrefixRef
    owner: User
    domain_of:
    - User
    range: Prefix
    maximum_cardinality: 1
  SuffixRef:
    name: SuffixRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SuffixRef
    owner: User
    domain_of:
    - User
    range: Suffix
    maximum_cardinality: 1
  FullNameRef:
    name: FullNameRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: FullNameRef
    owner: User
    domain_of:
    - User
    range: FullName
    maximum_cardinality: 1
  GivenNameRef:
    name: GivenNameRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: GivenNameRef
    owner: User
    domain_of:
    - User
    range: GivenName
    maximum_cardinality: 1
  FamilyNameRef:
    name: FamilyNameRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: FamilyNameRef
    owner: User
    domain_of:
    - User
    range: FamilyName
    maximum_cardinality: 1
  ImageRef:
    name: ImageRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ImageRef
    owner: User
    domain_of:
    - User
    range: Image
    maximum_cardinality: 1
  AddressRef:
    name: AddressRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: AddressRef
    owner: User
    domain_of:
    - User
    - Organization
    - Location
    range: Address
    inlined: true
    inlined_as_list: true
  TelecomRef:
    name: TelecomRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: TelecomRef
    owner: User
    domain_of:
    - User
    - Organization
    - Location
    range: Telecom
    inlined: true
    inlined_as_list: true
class_uri: odm:User

```
</details>