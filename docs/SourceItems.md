# Class: SourceItems



URI: [odm:SourceItems](http://www.cdisc.org/ns/odm/v2.0/SourceItems)



```mermaid
 classDiagram
    class SourceItems
      SourceItems : CodingRef
        
          SourceItems --|> Coding : CodingRef
        
      SourceItems : SourceItemRef
        
          SourceItems --|> SourceItem : SourceItemRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [SourceItemRef](SourceItemRef.md) | 1..* <br/> [SourceItem](SourceItem.md) |  | direct |
| [CodingRef](CodingRef.md) | 0..* <br/> [Coding](Coding.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Origin](Origin.md) | [SourceItemsRef](SourceItemsRef.md) | range | [SourceItems](SourceItems.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/SourceItems](https://wiki.cdisc.org/display/ODM2/SourceItems)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SourceItems |
| native | odm:SourceItems |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SourceItems
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SourceItems
slots:
- SourceItemRef
- CodingRef
slot_usage:
  SourceItemRef:
    name: SourceItemRef
    multivalued: true
    domain_of:
    - SourceItems
    range: SourceItem
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
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
class_uri: odm:SourceItems

```
</details>

### Induced

<details>
```yaml
name: SourceItems
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SourceItems
slot_usage:
  SourceItemRef:
    name: SourceItemRef
    multivalued: true
    domain_of:
    - SourceItems
    range: SourceItem
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
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
  SourceItemRef:
    name: SourceItemRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: SourceItemRef
    owner: SourceItems
    domain_of:
    - SourceItems
    range: SourceItem
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
  CodingRef:
    name: CodingRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: CodingRef
    owner: SourceItems
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
class_uri: odm:SourceItems

```
</details>