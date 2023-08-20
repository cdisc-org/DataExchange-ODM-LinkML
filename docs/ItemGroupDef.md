# Class: ItemGroupDef


_An ItemGroupDef describes a type of variable or field grouping that can occur within a study._





URI: [odm:ItemGroupDef](http://www.cdisc.org/ns/odm/v2.0/ItemGroupDef)



```mermaid
 classDiagram
    class ItemGroupDef
      ItemGroupDef : AliasRef
        
          ItemGroupDef --|> Alias : AliasRef
        
      ItemGroupDef : ArchiveLocationID
        
      ItemGroupDef : ClassRef
        
          ItemGroupDef --|> Class : ClassRef
        
      ItemGroupDef : CodingRef
        
          ItemGroupDef --|> Coding : CodingRef
        
      ItemGroupDef : CommentOID
        
      ItemGroupDef : DatasetName
        
      ItemGroupDef : DescriptionRef
        
          ItemGroupDef --|> Description : DescriptionRef
        
      ItemGroupDef : Domain
        
      ItemGroupDef : HasNoData
        
          ItemGroupDef --|> YesOnly : HasNoData
        
      ItemGroupDef : IsNonStandard
        
          ItemGroupDef --|> YesOnly : IsNonStandard
        
      ItemGroupDef : IsReferenceData
        
          ItemGroupDef --|> YesOrNo : IsReferenceData
        
      ItemGroupDef : ItemGroupRefRef
        
          ItemGroupDef --|> ItemGroupRef : ItemGroupRefRef
        
      ItemGroupDef : ItemRefRef
        
          ItemGroupDef --|> ItemRef : ItemRefRef
        
      ItemGroupDef : LeafRef
        
          ItemGroupDef --|> Leaf : LeafRef
        
      ItemGroupDef : Name
        
      ItemGroupDef : OID
        
      ItemGroupDef : OriginRef
        
          ItemGroupDef --|> Origin : OriginRef
        
      ItemGroupDef : Purpose
        
      ItemGroupDef : Repeating
        
          ItemGroupDef --|> ItemGroupRepeatingType : Repeating
        
      ItemGroupDef : RepeatingLimit
        
      ItemGroupDef : StandardOID
        
      ItemGroupDef : Structure
        
      ItemGroupDef : Type
        
      ItemGroupDef : WorkflowRefRef
        
          ItemGroupDef --|> WorkflowRef : WorkflowRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [OID](OID.md) | 1..1 <br/> [Oid](Oid.md) | Unique identifier for the ItemGroupDef element | direct |
| [Name](Name.md) | 1..1 <br/> [Name](Name.md) | Human readable name for the ItemGroupDef | direct |
| [Repeating](Repeating.md) | 1..1 <br/> [ItemGroupRepeatingType](ItemGroupRepeatingType.md) | The Repeating attribute indicates that the ItemGroup may occur repeatedly wit... | direct |
| [RepeatingLimit](RepeatingLimit.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) | Maximum number of repeats | direct |
| [IsReferenceData](IsReferenceData.md) | 0..1 <br/> [YesOrNo](YesOrNo.md) | Specifies whether this ItemGroupDef is used for non-subject data | direct |
| [Structure](Structure.md) | 0..1 <br/> [Text](Text.md) | Description of the level of detail represented by individual records in the I... | direct |
| [ArchiveLocationID](ArchiveLocationID.md) | 0..1 <br/> [Oidref](Oidref.md) | Reference to the unique ID of a leaf element that provides the actual locatio... | direct |
| [DatasetName](DatasetName.md) | 0..1 <br/> [Name](Name.md) | Name of a file containing the ItemGroupData for this ItemGroupDef | direct |
| [Domain](Domain.md) | 0..1 <br/> [Text](Text.md) | Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup data | direct |
| [Type](Type.md) | 1..1 <br/> [ItemGroupTypeType](ItemGroupTypeType.md) | identifies the type of data structure the ItemGroup represents | direct |
| [Purpose](Purpose.md) | 0..1 <br/> [Text](Text.md) | Purpose of the ItemGroup | direct |
| [StandardOID](StandardOID.md) | 0..1 <br/> [Oidref](Oidref.md) | Reference to a Standard element | direct |
| [IsNonStandard](IsNonStandard.md) | 0..1 <br/> [YesOnly](YesOnly.md) | Required for ADaM, SDTM, or SEND if StandardOID is not provided | direct |
| [HasNoData](HasNoData.md) | 0..1 <br/> [YesOnly](YesOnly.md) | Used to indicate that an ItemGroupDef has no data | direct |
| [CommentOID](CommentOID.md) | 0..1 <br/> [Oidref](Oidref.md) | Reference to a CommentDef with sponsor provided information related to this I... | direct |
| [DescriptionRef](DescriptionRef.md) | 0..1 <br/> [Description](Description.md) |  | direct |
| [ClassRef](ClassRef.md) | 0..1 <br/> [Class](Class.md) |  | direct |
| [CodingRef](CodingRef.md) | 0..* <br/> [Coding](Coding.md) |  | direct |
| [WorkflowRefRef](WorkflowRefRef.md) | 0..1 <br/> [WorkflowRef](WorkflowRef.md) |  | direct |
| [OriginRef](OriginRef.md) | 0..* <br/> [Origin](Origin.md) |  | direct |
| [AliasRef](AliasRef.md) | 0..* <br/> [Alias](Alias.md) |  | direct |
| [LeafRef](LeafRef.md) | 0..1 <br/> [Leaf](Leaf.md) |  | direct |
| [ItemGroupRefRef](ItemGroupRefRef.md) | 0..* <br/> [ItemGroupRef](ItemGroupRef.md) |  | direct |
| [ItemRefRef](ItemRefRef.md) | 0..* <br/> [ItemRef](ItemRef.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [ItemGroupDefRef](ItemGroupDefRef.md) | range | [ItemGroupDef](ItemGroupDef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/ItemGroupDef](https://wiki.cdisc.org/display/ODM2/ItemGroupDef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemGroupDef |
| native | odm:ItemGroupDef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemGroupDef
description: An ItemGroupDef describes a type of variable or field grouping that can
  occur within a study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemGroupDef
slots:
- OID
- Name
- Repeating
- RepeatingLimit
- IsReferenceData
- Structure
- ArchiveLocationID
- DatasetName
- Domain
- Type
- Purpose
- StandardOID
- IsNonStandard
- HasNoData
- CommentOID
- DescriptionRef
- ClassRef
- CodingRef
- WorkflowRefRef
- OriginRef
- AliasRef
- LeafRef
- ItemGroupRefRef
- ItemRefRef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the ItemGroupDef element.
    comments:
    - 'Required

      range:oid

      The OID attribute value must be unique within the Study/MetaDataVersion.'
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
  Name:
    name: Name
    description: Human readable name for the ItemGroupDef.
    comments:
    - 'Required

      range:name

      The Name attribute must be unique within set of ItemGroupDef elements within
      a Study/MetadataVersion.'
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
    - ExceptionEvent
    - Organization
    - Location
    - Query
    range: name
    required: true
  Repeating:
    name: Repeating
    description: 'The Repeating attribute indicates that the ItemGroup may occur repeatedly
      within the containing element . Simple - the ItemGroup repeats within the containing
      element and is not bound in any way. Note: It is equivalent to the ODM v1.3.2
      case where Repeating="Yes". Dynamic - ItemGroupData repeats based on values
      in a codelist. There may be multiple occurrences for some codelist items. Static
      - ItemGroupData repeats based on values in a codelist. Only one occurrence may
      happen for each codelist item.'
    comments:
    - 'Required

      enum values:(No | Simple | Dynamic | Static)

      For cases where Repeating is set to Dynamic or Static, one ItemRef within the
      ItemGroup must include the Repeat="Yes" attribute to indicate that that specific
      ItemRef references the codelist that establishes the Repeating behavior. If
      IsReferenceData is "Yes", the ItemGroup can occur only within a ReferenceData
      element. If IsReferenceData is "No", the ItemGroup can occur only within a ClinicalData
      element.'
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    range: ItemGroupRepeatingType
    required: true
  RepeatingLimit:
    name: RepeatingLimit
    description: Maximum number of repeats.
    comments:
    - 'Optional

      range:positiveInteger

      RepeatingLimit can only be used when Repeating="Simple".'
    domain_of:
    - ItemGroupDef
    range: positiveInteger
  IsReferenceData:
    name: IsReferenceData
    description: Specifies whether this ItemGroupDef is used for non-subject data.
    comments:
    - 'Optional

      enum values:(Yes | No)

      Data content for ItemGroupDef elements where the IsReferenceData attribute is
      "Yes" is under the /ODM/ReferenceData element.'
    domain_of:
    - ItemGroupDef
    range: YesOrNo
  Structure:
    name: Structure
    description: Description of the level of detail represented by individual records
      in the ItemGroup
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemGroupDef
    range: text
  ArchiveLocationID:
    name: ArchiveLocationID
    description: Reference to the unique ID of a leaf element that provides the actual
      location and file name of the data file.
    comments:
    - 'Optional

      range:oidref

      If provided, the value must match the leaf ID attribute of the leaf child element.'
    domain_of:
    - ItemGroupDef
    range: oidref
  DatasetName:
    name: DatasetName
    description: Name of a file containing the ItemGroupData for this ItemGroupDef.
      The name applies to the object itself rather then providing a mapping to a different
      object.
    comments:
    - 'Optional

      range:name

      Could have constraints on individual ODM extensions, such as Define-XML or associated
      CDISC Metadata Guidelines. For example, DatasetName could be defined as sasName
      (see Section 2.14, Data Formats ) in Define-XML or associated CDISC Metadata
      Guidelines.'
    domain_of:
    - ItemGroupDef
    range: name
  Domain:
    name: Domain
    description: Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup
      data. The domain applies to the object itself rather then providing a mapping
      to a different object.
    comments:
    - 'Optional

      range:text

      Usage requirements are based on the applicable CDISC Standard. Could have constraints
      on individual ODM extensions, such as Define-XML or associated CDISC Metadata
      Guidelines.'
    domain_of:
    - ItemGroupDef
    range: text
  Type:
    name: Type
    description: identifies the type of data structure the ItemGroup represents. Form
      - a CRF for data collection. Note, ItemGroupDef Type="Form" replaces the ODM
      v1.x FormDef element. Section - a section within a CRF. Dataset - tabulation,
      analysis or operational datasets. Concept - defines a biomedical concept.
    comments:
    - 'Required

      enum values:(Form | Section | Dataset | Concept)

      Type is an extensible attribute. Type="Section" can only be used when the ItemGroup
      has a top-level ancestor ItemGroup that has Type="Form".'
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
    range: ItemGroupTypeType
    required: true
  Purpose:
    name: Purpose
    description: 'Purpose of the ItemGroup. '
    comments:
    - 'Optional

      range:text

      Usage requirements are based on the applicable CDISC Standard. Could have constraints
      on individual ODM extensions, such as Define-XML or associated CDISC Metadata
      Guidelines.'
    domain_of:
    - ItemGroupDef
    range: text
  StandardOID:
    name: StandardOID
    description: Reference to a Standard element.
    comments:
    - 'Optional

      range:oidref

      Must match the OID attribute of a Standard element within this Study/MetaDataVersion/Standards.'
    domain_of:
    - ItemGroupDef
    - CodeList
    range: oidref
  IsNonStandard:
    name: IsNonStandard
    description: Required for ADaM, SDTM, or SEND if StandardOID is not provided.
    comments:
    - 'Conditional

      range:Yes

      Must not be provided when StandardOID is provided.'
    domain_of:
    - ItemGroupDef
    - ItemRef
    - CodeList
    range: YesOnly
  HasNoData:
    name: HasNoData
    description: Used to indicate that an ItemGroupDef has no data. May be used at
      sponsor's discretion or if required by a regulatory authority
    comments:
    - 'Optional

      range:Yes

      A comment must be included to explain why no data are present for datasets that
      were planned for use in the study.'
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: YesOnly
  CommentOID:
    name: CommentOID
    description: Reference to a CommentDef with sponsor provided information related
      to this ItemGroupDef. It allows annotations to the ItemGroup.
    comments:
    - 'Optional

      range:oidref

      Must match the OID attribute of a CommentDef element within this Study/MetaDataVersion.'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
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
    - ExceptionEvent
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  ClassRef:
    name: ClassRef
    domain_of:
    - ItemGroupDef
    range: Class
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
  WorkflowRefRef:
    name: WorkflowRefRef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    - ExceptionEvent
    range: WorkflowRef
    maximum_cardinality: 1
  OriginRef:
    name: OriginRef
    multivalued: true
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: Origin
    inlined: true
    inlined_as_list: true
  AliasRef:
    name: AliasRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
  LeafRef:
    name: LeafRef
    domain_of:
    - MetaDataVersion
    - ItemGroupDef
    range: Leaf
    maximum_cardinality: 1
  ItemGroupRefRef:
    name: ItemGroupRefRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    range: ItemGroupRef
    inlined: true
    inlined_as_list: true
  ItemRefRef:
    name: ItemRefRef
    multivalued: true
    domain_of:
    - ValueListDef
    - ItemGroupDef
    range: ItemRef
    inlined: true
    inlined_as_list: true
class_uri: odm:ItemGroupDef

```
</details>

### Induced

<details>
```yaml
name: ItemGroupDef
description: An ItemGroupDef describes a type of variable or field grouping that can
  occur within a study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/ItemGroupDef
slot_usage:
  OID:
    name: OID
    description: Unique identifier for the ItemGroupDef element.
    comments:
    - 'Required

      range:oid

      The OID attribute value must be unique within the Study/MetaDataVersion.'
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
  Name:
    name: Name
    description: Human readable name for the ItemGroupDef.
    comments:
    - 'Required

      range:name

      The Name attribute must be unique within set of ItemGroupDef elements within
      a Study/MetadataVersion.'
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
    - ExceptionEvent
    - Organization
    - Location
    - Query
    range: name
    required: true
  Repeating:
    name: Repeating
    description: 'The Repeating attribute indicates that the ItemGroup may occur repeatedly
      within the containing element . Simple - the ItemGroup repeats within the containing
      element and is not bound in any way. Note: It is equivalent to the ODM v1.3.2
      case where Repeating="Yes". Dynamic - ItemGroupData repeats based on values
      in a codelist. There may be multiple occurrences for some codelist items. Static
      - ItemGroupData repeats based on values in a codelist. Only one occurrence may
      happen for each codelist item.'
    comments:
    - 'Required

      enum values:(No | Simple | Dynamic | Static)

      For cases where Repeating is set to Dynamic or Static, one ItemRef within the
      ItemGroup must include the Repeat="Yes" attribute to indicate that that specific
      ItemRef references the codelist that establishes the Repeating behavior. If
      IsReferenceData is "Yes", the ItemGroup can occur only within a ReferenceData
      element. If IsReferenceData is "No", the ItemGroup can occur only within a ClinicalData
      element.'
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    range: ItemGroupRepeatingType
    required: true
  RepeatingLimit:
    name: RepeatingLimit
    description: Maximum number of repeats.
    comments:
    - 'Optional

      range:positiveInteger

      RepeatingLimit can only be used when Repeating="Simple".'
    domain_of:
    - ItemGroupDef
    range: positiveInteger
  IsReferenceData:
    name: IsReferenceData
    description: Specifies whether this ItemGroupDef is used for non-subject data.
    comments:
    - 'Optional

      enum values:(Yes | No)

      Data content for ItemGroupDef elements where the IsReferenceData attribute is
      "Yes" is under the /ODM/ReferenceData element.'
    domain_of:
    - ItemGroupDef
    range: YesOrNo
  Structure:
    name: Structure
    description: Description of the level of detail represented by individual records
      in the ItemGroup
    comments:
    - 'Optional

      range:text'
    domain_of:
    - ItemGroupDef
    range: text
  ArchiveLocationID:
    name: ArchiveLocationID
    description: Reference to the unique ID of a leaf element that provides the actual
      location and file name of the data file.
    comments:
    - 'Optional

      range:oidref

      If provided, the value must match the leaf ID attribute of the leaf child element.'
    domain_of:
    - ItemGroupDef
    range: oidref
  DatasetName:
    name: DatasetName
    description: Name of a file containing the ItemGroupData for this ItemGroupDef.
      The name applies to the object itself rather then providing a mapping to a different
      object.
    comments:
    - 'Optional

      range:name

      Could have constraints on individual ODM extensions, such as Define-XML or associated
      CDISC Metadata Guidelines. For example, DatasetName could be defined as sasName
      (see Section 2.14, Data Formats ) in Define-XML or associated CDISC Metadata
      Guidelines.'
    domain_of:
    - ItemGroupDef
    range: name
  Domain:
    name: Domain
    description: Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup
      data. The domain applies to the object itself rather then providing a mapping
      to a different object.
    comments:
    - 'Optional

      range:text

      Usage requirements are based on the applicable CDISC Standard. Could have constraints
      on individual ODM extensions, such as Define-XML or associated CDISC Metadata
      Guidelines.'
    domain_of:
    - ItemGroupDef
    range: text
  Type:
    name: Type
    description: identifies the type of data structure the ItemGroup represents. Form
      - a CRF for data collection. Note, ItemGroupDef Type="Form" replaces the ODM
      v1.x FormDef element. Section - a section within a CRF. Dataset - tabulation,
      analysis or operational datasets. Concept - defines a biomedical concept.
    comments:
    - 'Required

      enum values:(Form | Section | Dataset | Concept)

      Type is an extensible attribute. Type="Section" can only be used when the ItemGroup
      has a top-level ancestor ItemGroup that has Type="Form".'
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
    range: ItemGroupTypeType
    required: true
  Purpose:
    name: Purpose
    description: 'Purpose of the ItemGroup. '
    comments:
    - 'Optional

      range:text

      Usage requirements are based on the applicable CDISC Standard. Could have constraints
      on individual ODM extensions, such as Define-XML or associated CDISC Metadata
      Guidelines.'
    domain_of:
    - ItemGroupDef
    range: text
  StandardOID:
    name: StandardOID
    description: Reference to a Standard element.
    comments:
    - 'Optional

      range:oidref

      Must match the OID attribute of a Standard element within this Study/MetaDataVersion/Standards.'
    domain_of:
    - ItemGroupDef
    - CodeList
    range: oidref
  IsNonStandard:
    name: IsNonStandard
    description: Required for ADaM, SDTM, or SEND if StandardOID is not provided.
    comments:
    - 'Conditional

      range:Yes

      Must not be provided when StandardOID is provided.'
    domain_of:
    - ItemGroupDef
    - ItemRef
    - CodeList
    range: YesOnly
  HasNoData:
    name: HasNoData
    description: Used to indicate that an ItemGroupDef has no data. May be used at
      sponsor's discretion or if required by a regulatory authority
    comments:
    - 'Optional

      range:Yes

      A comment must be included to explain why no data are present for datasets that
      were planned for use in the study.'
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: YesOnly
  CommentOID:
    name: CommentOID
    description: Reference to a CommentDef with sponsor provided information related
      to this ItemGroupDef. It allows annotations to the ItemGroup.
    comments:
    - 'Optional

      range:oidref

      Must match the OID attribute of a CommentDef element within this Study/MetaDataVersion.'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
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
    - ExceptionEvent
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  ClassRef:
    name: ClassRef
    domain_of:
    - ItemGroupDef
    range: Class
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
  WorkflowRefRef:
    name: WorkflowRefRef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    - ExceptionEvent
    range: WorkflowRef
    maximum_cardinality: 1
  OriginRef:
    name: OriginRef
    multivalued: true
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: Origin
    inlined: true
    inlined_as_list: true
  AliasRef:
    name: AliasRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
  LeafRef:
    name: LeafRef
    domain_of:
    - MetaDataVersion
    - ItemGroupDef
    range: Leaf
    maximum_cardinality: 1
  ItemGroupRefRef:
    name: ItemGroupRefRef
    multivalued: true
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    range: ItemGroupRef
    inlined: true
    inlined_as_list: true
  ItemRefRef:
    name: ItemRefRef
    multivalued: true
    domain_of:
    - ValueListDef
    - ItemGroupDef
    range: ItemRef
    inlined: true
    inlined_as_list: true
attributes:
  OID:
    name: OID
    description: Unique identifier for the ItemGroupDef element.
    comments:
    - 'Required

      range:oid

      The OID attribute value must be unique within the Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: OID
    owner: ItemGroupDef
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
  Name:
    name: Name
    description: Human readable name for the ItemGroupDef.
    comments:
    - 'Required

      range:name

      The Name attribute must be unique within set of ItemGroupDef elements within
      a Study/MetadataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: ItemGroupDef
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
    - ExceptionEvent
    - Organization
    - Location
    - Query
    range: name
    required: true
  Repeating:
    name: Repeating
    description: 'The Repeating attribute indicates that the ItemGroup may occur repeatedly
      within the containing element . Simple - the ItemGroup repeats within the containing
      element and is not bound in any way. Note: It is equivalent to the ODM v1.3.2
      case where Repeating="Yes". Dynamic - ItemGroupData repeats based on values
      in a codelist. There may be multiple occurrences for some codelist items. Static
      - ItemGroupData repeats based on values in a codelist. Only one occurrence may
      happen for each codelist item.'
    comments:
    - 'Required

      enum values:(No | Simple | Dynamic | Static)

      For cases where Repeating is set to Dynamic or Static, one ItemRef within the
      ItemGroup must include the Repeat="Yes" attribute to indicate that that specific
      ItemRef references the codelist that establishes the Repeating behavior. If
      IsReferenceData is "Yes", the ItemGroup can occur only within a ReferenceData
      element. If IsReferenceData is "No", the ItemGroup can occur only within a ClinicalData
      element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Repeating
    owner: ItemGroupDef
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    range: ItemGroupRepeatingType
    required: true
  RepeatingLimit:
    name: RepeatingLimit
    description: Maximum number of repeats.
    comments:
    - 'Optional

      range:positiveInteger

      RepeatingLimit can only be used when Repeating="Simple".'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: RepeatingLimit
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: positiveInteger
  IsReferenceData:
    name: IsReferenceData
    description: Specifies whether this ItemGroupDef is used for non-subject data.
    comments:
    - 'Optional

      enum values:(Yes | No)

      Data content for ItemGroupDef elements where the IsReferenceData attribute is
      "Yes" is under the /ODM/ReferenceData element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: IsReferenceData
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: YesOrNo
  Structure:
    name: Structure
    description: Description of the level of detail represented by individual records
      in the ItemGroup
    comments:
    - 'Optional

      range:text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Structure
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: text
  ArchiveLocationID:
    name: ArchiveLocationID
    description: Reference to the unique ID of a leaf element that provides the actual
      location and file name of the data file.
    comments:
    - 'Optional

      range:oidref

      If provided, the value must match the leaf ID attribute of the leaf child element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ArchiveLocationID
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: oidref
  DatasetName:
    name: DatasetName
    description: Name of a file containing the ItemGroupData for this ItemGroupDef.
      The name applies to the object itself rather then providing a mapping to a different
      object.
    comments:
    - 'Optional

      range:name

      Could have constraints on individual ODM extensions, such as Define-XML or associated
      CDISC Metadata Guidelines. For example, DatasetName could be defined as sasName
      (see Section 2.14, Data Formats ) in Define-XML or associated CDISC Metadata
      Guidelines.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: DatasetName
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: name
  Domain:
    name: Domain
    description: Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup
      data. The domain applies to the object itself rather then providing a mapping
      to a different object.
    comments:
    - 'Optional

      range:text

      Usage requirements are based on the applicable CDISC Standard. Could have constraints
      on individual ODM extensions, such as Define-XML or associated CDISC Metadata
      Guidelines.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Domain
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: text
  Type:
    name: Type
    description: identifies the type of data structure the ItemGroup represents. Form
      - a CRF for data collection. Note, ItemGroupDef Type="Form" replaces the ODM
      v1.x FormDef element. Section - a section within a CRF. Dataset - tabulation,
      analysis or operational datasets. Concept - defines a biomedical concept.
    comments:
    - 'Required

      enum values:(Form | Section | Dataset | Concept)

      Type is an extensible attribute. Type="Section" can only be used when the ItemGroup
      has a top-level ancestor ItemGroup that has Type="Form".'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Type
    owner: ItemGroupDef
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
    range: ItemGroupTypeType
    required: true
  Purpose:
    name: Purpose
    description: 'Purpose of the ItemGroup. '
    comments:
    - 'Optional

      range:text

      Usage requirements are based on the applicable CDISC Standard. Could have constraints
      on individual ODM extensions, such as Define-XML or associated CDISC Metadata
      Guidelines.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Purpose
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: text
  StandardOID:
    name: StandardOID
    description: Reference to a Standard element.
    comments:
    - 'Optional

      range:oidref

      Must match the OID attribute of a Standard element within this Study/MetaDataVersion/Standards.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StandardOID
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    - CodeList
    range: oidref
  IsNonStandard:
    name: IsNonStandard
    description: Required for ADaM, SDTM, or SEND if StandardOID is not provided.
    comments:
    - 'Conditional

      range:Yes

      Must not be provided when StandardOID is provided.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: IsNonStandard
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    - ItemRef
    - CodeList
    range: YesOnly
  HasNoData:
    name: HasNoData
    description: Used to indicate that an ItemGroupDef has no data. May be used at
      sponsor's discretion or if required by a regulatory authority
    comments:
    - 'Optional

      range:Yes

      A comment must be included to explain why no data are present for datasets that
      were planned for use in the study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: HasNoData
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: YesOnly
  CommentOID:
    name: CommentOID
    description: Reference to a CommentDef with sponsor provided information related
      to this ItemGroupDef. It allows annotations to the ItemGroup.
    comments:
    - 'Optional

      range:oidref

      Must match the OID attribute of a CommentDef element within this Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CommentOID
    owner: ItemGroupDef
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: oidref
  DescriptionRef:
    name: DescriptionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DescriptionRef
    owner: ItemGroupDef
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
    - ExceptionEvent
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  ClassRef:
    name: ClassRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: ClassRef
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    range: Class
    maximum_cardinality: 1
  CodingRef:
    name: CodingRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: CodingRef
    owner: ItemGroupDef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
  WorkflowRefRef:
    name: WorkflowRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: WorkflowRefRef
    owner: ItemGroupDef
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Protocol
    - StudyStructure
    - Arm
    - ExceptionEvent
    range: WorkflowRef
    maximum_cardinality: 1
  OriginRef:
    name: OriginRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: OriginRef
    owner: ItemGroupDef
    domain_of:
    - ItemGroupDef
    - ItemRef
    range: Origin
    inlined: true
    inlined_as_list: true
  AliasRef:
    name: AliasRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: AliasRef
    owner: ItemGroupDef
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Protocol
    range: Alias
    inlined: true
    inlined_as_list: true
  LeafRef:
    name: LeafRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: LeafRef
    owner: ItemGroupDef
    domain_of:
    - MetaDataVersion
    - ItemGroupDef
    range: Leaf
    maximum_cardinality: 1
  ItemGroupRefRef:
    name: ItemGroupRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemGroupRefRef
    owner: ItemGroupDef
    domain_of:
    - StudyEventDef
    - ItemGroupDef
    range: ItemGroupRef
    inlined: true
    inlined_as_list: true
  ItemRefRef:
    name: ItemRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ItemRefRef
    owner: ItemGroupDef
    domain_of:
    - ValueListDef
    - ItemGroupDef
    range: ItemRef
    inlined: true
    inlined_as_list: true
class_uri: odm:ItemGroupDef

```
</details>