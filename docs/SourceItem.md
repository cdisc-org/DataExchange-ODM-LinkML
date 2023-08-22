# Class: SourceItem

_Provides the information needed to identify the source metadata._




URI: [odm:SourceItem](http://www.cdisc.org/ns/odm/v2.0/SourceItem)


```mermaid
erDiagram
SourceItem {
    oidref ItemOID  
    oidref ItemGroupOID  
    oidref MetaDataVersionOID  
    oidref StudyOID  
    oidref leafID  
    name Name  
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
Resource {
    text Type  
    name Name  
    text Attribute  
    text Label  
}
Selection {
    text Path  
}

SourceItem ||--}o Resource : "ResourceRef"
SourceItem ||--}o Coding : "CodingRef"
Resource ||--}o Selection : "SelectionRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ItemOID](ItemOID.md) | 0..1 <br/> [oidref](oidref.md) | References the ItemDef that provides the variable metadata. | direct |
| [ItemGroupOID](ItemGroupOID.md) | 0..1 <br/> [oidref](oidref.md) | References the ItemGroupDef that provides the ItemGroup or dataset metadata. | direct |
| [MetaDataVersionOID](MetaDataVersionOID.md) | 0..1 <br/> [oidref](oidref.md) | References the MetaDataVersion that provides the metadata when referencing an... | direct |
| [StudyOID](StudyOID.md) | 0..1 <br/> [oidref](oidref.md) | References the Study that provides the metadata when referencing another ODM ... | direct |
| [leafID](leafID.md) | 1..1 <br/> [oidref](oidref.md) | References a leaf element that provides a reference to another ODM document. ... | direct |
| [Name](Name.md) | 0..1 <br/> [name](name.md) | Provides a way to connect an argument to a parameter when SourceItems are inp... | direct |
| [ResourceRef](ResourceRef.md) | 0..* <br/> [Resource](Resource.md) | Resource reference: Describes an external resource used as the source for the... | direct |
| [CodingRef](CodingRef.md) | 0..* <br/> [Coding](Coding.md) | Coding reference: Coding references a symbol from a defined code system. It u... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SourceItems](SourceItems.md) | [SourceItemRef](SourceItemRef.md) | range | [SourceItem](SourceItem.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/SourceItem](https://wiki.cdisc.org/display/ODM2/SourceItem)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SourceItem |
| native | odm:SourceItem |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SourceItem
description: Provides the information needed to identify the source metadata.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SourceItem
rank: 1000
slots:
- ItemOID
- ItemGroupOID
- MetaDataVersionOID
- StudyOID
- leafID
- Name
- ResourceRef
- CodingRef
slot_usage:
  ItemOID:
    name: ItemOID
    description: References the ItemDef that provides the variable metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemDef element. The referenced ItemDef element can
      be in the same ODM document or another ODM document.'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
  ItemGroupOID:
    name: ItemGroupOID
    description: References the ItemGroupDef that provides the ItemGroup or dataset
      metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemGroupDef element. The referenced ItemGroupDef
      element can be in the same ODM document or another ODM document.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: oidref
  MetaDataVersionOID:
    name: MetaDataVersionOID
    description: References the MetaDataVersion that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID of a MetaDataVersion element. The referenced MetaDataVersion
      element can be in the same ODM document or another ODM document. Must be provided
      if the reference is not to an object within the same MetaDataVersion element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
  StudyOID:
    name: StudyOID
    description: References the Study that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an Study element. The referenced Study element can be
      in the same ODM document or another ODM document. Must be provided if the reference
      is not to an object within the same Study element.'
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
  leafID:
    name: leafID
    description: References a leaf element that provides a reference to another ODM
      document. This is necessary when the source ItemOID references an ItemDef contained
      in a different ODM document.
    comments:
    - 'Optional

      range: IDREF

      When referencing another ODM document it is necessary to have values for the
      MetaDataVersionOID and StudyOID attributes.'
    domain_of:
    - SourceItem
    range: oidref
  Name:
    name: Name
    description: Provides a way to connect an argument to a parameter when SourceItems
      are inputs to methods. It allows the name used in the programming code in the
      method description to make it easier to trace the use of the value.
    comments:
    - 'Optional

      range: name'
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
  ResourceRef:
    name: ResourceRef
    multivalued: true
    domain_of:
    - SourceItem
    range: Resource
    inlined: true
    inlined_as_list: true
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
class_uri: odm:SourceItem

```
</details>

### Induced

<details>
```yaml
name: SourceItem
description: Provides the information needed to identify the source metadata.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SourceItem
rank: 1000
slot_usage:
  ItemOID:
    name: ItemOID
    description: References the ItemDef that provides the variable metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemDef element. The referenced ItemDef element can
      be in the same ODM document or another ODM document.'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
  ItemGroupOID:
    name: ItemGroupOID
    description: References the ItemGroupDef that provides the ItemGroup or dataset
      metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemGroupDef element. The referenced ItemGroupDef
      element can be in the same ODM document or another ODM document.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: oidref
  MetaDataVersionOID:
    name: MetaDataVersionOID
    description: References the MetaDataVersion that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID of a MetaDataVersion element. The referenced MetaDataVersion
      element can be in the same ODM document or another ODM document. Must be provided
      if the reference is not to an object within the same MetaDataVersion element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
  StudyOID:
    name: StudyOID
    description: References the Study that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an Study element. The referenced Study element can be
      in the same ODM document or another ODM document. Must be provided if the reference
      is not to an object within the same Study element.'
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
  leafID:
    name: leafID
    description: References a leaf element that provides a reference to another ODM
      document. This is necessary when the source ItemOID references an ItemDef contained
      in a different ODM document.
    comments:
    - 'Optional

      range: IDREF

      When referencing another ODM document it is necessary to have values for the
      MetaDataVersionOID and StudyOID attributes.'
    domain_of:
    - SourceItem
    range: oidref
  Name:
    name: Name
    description: Provides a way to connect an argument to a parameter when SourceItems
      are inputs to methods. It allows the name used in the programming code in the
      method description to make it easier to trace the use of the value.
    comments:
    - 'Optional

      range: name'
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
  ResourceRef:
    name: ResourceRef
    multivalued: true
    domain_of:
    - SourceItem
    range: Resource
    inlined: true
    inlined_as_list: true
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
attributes:
  ItemOID:
    name: ItemOID
    description: References the ItemDef that provides the variable metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemDef element. The referenced ItemDef element can
      be in the same ODM document or another ODM document.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemOID
    owner: SourceItem
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: oidref
  ItemGroupOID:
    name: ItemGroupOID
    description: References the ItemGroupDef that provides the ItemGroup or dataset
      metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemGroupDef element. The referenced ItemGroupDef
      element can be in the same ODM document or another ODM document.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ItemGroupOID
    owner: SourceItem
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: oidref
  MetaDataVersionOID:
    name: MetaDataVersionOID
    description: References the MetaDataVersion that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID of a MetaDataVersion element. The referenced MetaDataVersion
      element can be in the same ODM document or another ODM document. Must be provided
      if the reference is not to an object within the same MetaDataVersion element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: MetaDataVersionOID
    owner: SourceItem
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: oidref
  StudyOID:
    name: StudyOID
    description: References the Study that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an Study element. The referenced Study element can be
      in the same ODM document or another ODM document. Must be provided if the reference
      is not to an object within the same Study element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StudyOID
    owner: SourceItem
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
  leafID:
    name: leafID
    description: References a leaf element that provides a reference to another ODM
      document. This is necessary when the source ItemOID references an ItemDef contained
      in a different ODM document.
    comments:
    - 'Optional

      range: IDREF

      When referencing another ODM document it is necessary to have values for the
      MetaDataVersionOID and StudyOID attributes.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: true
    alias: leafID
    owner: SourceItem
    domain_of:
    - SourceItem
    range: oidref
    required: true
  Name:
    name: Name
    description: Provides a way to connect an argument to a parameter when SourceItems
      are inputs to methods. It allows the name used in the programming code in the
      method description to make it easier to trace the use of the value.
    comments:
    - 'Optional

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Name
    owner: SourceItem
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
  ResourceRef:
    name: ResourceRef
    description: 'Resource reference: Describes an external resource used as the source
      for the parent ItemGroup or Item.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: ResourceRef
    owner: SourceItem
    domain_of:
    - SourceItem
    range: Resource
    inlined: true
    inlined_as_list: true
  CodingRef:
    name: CodingRef
    description: 'Coding reference: Coding references a symbol from a defined code
      system. It uses a code defined in a terminology system to associate semantics
      with a given term, codelist, variable, or group of variables. The presence of
      a Coding element associates a meaning to its parent element. Including multiple
      Coding elements for a given parent indicates synonymous meanings provided by
      different code systems or code system versions.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: CodingRef
    owner: SourceItem
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
class_uri: odm:SourceItem

```
</details>