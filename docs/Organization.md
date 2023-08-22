# Class: Organization


_An organization can reference a parent organization. Users may be associated with an Organization. An Organization may be associated with a Location. A User, Location, or Organization may have an address._





URI: [odm:Organization](http://www.cdisc.org/ns/odm/v2.0/Organization)



```mermaid
 classDiagram
    class Organization
      Organization : AddressRef
        
          Organization --|> Address : AddressRef
        
      Organization : DescriptionRef
        
          Organization --|> Description : DescriptionRef
        
      Organization : LocationOID
        
      Organization : Name
        
      Organization : OID
        
      Organization : PartOfOrganizationOID
        
      Organization : Role
        
      Organization : TelecomRef
        
          Organization --|> Telecom : TelecomRef
        
      Organization : Type
        
          Organization --|> OrganizationType : Type
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [oid](oid.md) | Unique identifier for the organization. | direct |
| [Name](Name.md) | 1..1 <br/> [name](name.md) | Formal, human readable name of the organization. | direct |
| [Role](Role.md) | 0..1 <br/> [text](text.md) | Role of the organization in the current study. | direct |
| [Type](Type.md) | 1..1 <br/> [OrganizationType](OrganizationType.md) | Categorization of organizations associated with clinical studies. | direct |
| [LocationOID](LocationOID.md) | 0..1 <br/> [oidref](oidref.md) | Reference to a location where data is collected and/or study subjects are tre... | direct |
| [PartOfOrganizationOID](PartOfOrganizationOID.md) | 0..1 <br/> [oidref](oidref.md) | Reference to a parent organization. | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [AddressRef](AddressRef.md) | 0..* <br/> [Address](Address.md) | Address reference: The postal address for a user, location, or organization. | direct |
| [TelecomRef](TelecomRef.md) | 0..* <br/> [Telecom](Telecom.md) | Telecom reference: The telecommunication contacts points of a user, a locatio... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AdminData](AdminData.md) | [OrganizationRef](OrganizationRef.md) | range | [Organization](Organization.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Organization](https://wiki.cdisc.org/display/ODM2/Organization)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Organization |
| native | odm:Organization |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organization
description: An organization can reference a parent organization. Users may be associated
  with an Organization. An Organization may be associated with a Location. A User,
  Location, or Organization may have an address.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Organization
slots:
- OID
- Name
- Role
- Type
- LocationOID
- PartOfOrganizationOID
- DescriptionRef
- AddressRef
- TelecomRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the organization.
    comments:
    - 'Required

      range: oid

      Must be unique within the Organization elements for a study.'
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
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  Name:
    name: Name
    description: Formal, human readable name of the organization.
    comments:
    - 'Required

      range: name

      Must be unique within the set of Organization elements for a study.'
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: name
    required: true
  Role:
    name: Role
    description: Role of the organization in the current study.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ItemRef
    - Organization
    - Location
    range: text
  Type:
    name: Type
    description: Categorization of organizations associated with clinical studies.
    comments:
    - 'Required

      enum values: (Sponsor | Site | CRO | Lab | Other | TechnologyProvider)

      An ODM extension is required if additional Type values are needed.'
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: OrganizationType
    required: true
  LocationOID:
    name: LocationOID
    description: Reference to a location where data is collected and/or study subjects
      are treated.
    comments:
    - 'Optional

      range: oidref

      Must match the OID attribute for a Location element for the study.'
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
  PartOfOrganizationOID:
    name: PartOfOrganizationOID
    description: Reference to a parent organization.
    comments:
    - 'Optional

      range: oidref

      Must match the OID Organization within the study.'
    domain_of:
    - Organization
    range: oidref
  DescriptionRef:
    name: DescriptionRef
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
class_uri: odm:Organization

```
</details>

### Induced

<details>
```yaml
name: Organization
description: An organization can reference a parent organization. Users may be associated
  with an Organization. An Organization may be associated with a Location. A User,
  Location, or Organization may have an address.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Organization
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the organization.
    comments:
    - 'Required

      range: oid

      Must be unique within the Organization elements for a study.'
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
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  Name:
    name: Name
    description: Formal, human readable name of the organization.
    comments:
    - 'Required

      range: name

      Must be unique within the set of Organization elements for a study.'
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: name
    required: true
  Role:
    name: Role
    description: Role of the organization in the current study.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - ItemRef
    - Organization
    - Location
    range: text
  Type:
    name: Type
    description: Categorization of organizations associated with clinical studies.
    comments:
    - 'Required

      enum values: (Sponsor | Site | CRO | Lab | Other | TechnologyProvider)

      An ODM extension is required if additional Type values are needed.'
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: OrganizationType
    required: true
  LocationOID:
    name: LocationOID
    description: Reference to a location where data is collected and/or study subjects
      are treated.
    comments:
    - 'Optional

      range: oidref

      Must match the OID attribute for a Location element for the study.'
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
  PartOfOrganizationOID:
    name: PartOfOrganizationOID
    description: Reference to a parent organization.
    comments:
    - 'Optional

      range: oidref

      Must match the OID Organization within the study.'
    domain_of:
    - Organization
    range: oidref
  DescriptionRef:
    name: DescriptionRef
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
    description: Unique identifier for the organization.
    comments:
    - 'Required

      range: oid

      Must be unique within the Organization elements for a study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: Organization
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
    - User
    - Organization
    - Location
    - SignatureDef
    - Query
    range: oid
    required: true
  Name:
    name: Name
    description: Formal, human readable name of the organization.
    comments:
    - 'Required

      range: name

      Must be unique within the set of Organization elements for a study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: Organization
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: name
    required: true
  Role:
    name: Role
    description: Role of the organization in the current study.
    comments:
    - 'Optional

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Role
    owner: Organization
    domain_of:
    - ItemRef
    - Organization
    - Location
    range: text
  Type:
    name: Type
    description: Categorization of organizations associated with clinical studies.
    comments:
    - 'Required

      enum values: (Sponsor | Site | CRO | Lab | Other | TechnologyProvider)

      An ODM extension is required if additional Type values are needed.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Type
    owner: Organization
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: OrganizationType
    required: true
  LocationOID:
    name: LocationOID
    description: Reference to a location where data is collected and/or study subjects
      are treated.
    comments:
    - 'Optional

      range: oidref

      Must match the OID attribute for a Location element for the study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: LocationOID
    owner: Organization
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
  PartOfOrganizationOID:
    name: PartOfOrganizationOID
    description: Reference to a parent organization.
    comments:
    - 'Optional

      range: oidref

      Must match the OID Organization within the study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: PartOfOrganizationOID
    owner: Organization
    domain_of:
    - Organization
    range: oidref
  DescriptionRef:
    name: DescriptionRef
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
    owner: Organization
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
  AddressRef:
    name: AddressRef
    description: 'Address reference: The postal address for a user, location, or organization.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: AddressRef
    owner: Organization
    domain_of:
    - User
    - Organization
    - Location
    range: Address
    inlined: true
    inlined_as_list: true
  TelecomRef:
    name: TelecomRef
    description: 'Telecom reference: The telecommunication contacts points of a user,
      a location, or an organization. The Type attribute designates the type of contact.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: TelecomRef
    owner: Organization
    domain_of:
    - User
    - Organization
    - Location
    range: Telecom
    inlined: true
    inlined_as_list: true
class_uri: odm:Organization

```
</details>