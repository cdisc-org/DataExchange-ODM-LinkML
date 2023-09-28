# Class: SourceItems

_Identifies source items as needed to support automated data capture and end-to-end traceability._




URI: [odm:SourceItems](http://www.cdisc.org/ns/odm/v2.0/SourceItems)


```mermaid
erDiagram
SourceItems {

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
SourceItem {
    oidref itemOID  
    oidref itemGroupOID  
    oidref metaDataVersionOID  
    oidref studyOID  
    oidref leafID  
    nameType name  
}
Resource {
    text type  
    nameType name  
    text attribute  
    text label  
}

SourceItems ||--}o SourceItem : "sourceItem"
SourceItems ||--}o Coding : "coding"
SourceItem ||--}o Resource : "resource"
SourceItem ||--}o Coding : "coding"
Resource ||--}o Selection : "selection"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sourceItem](sourceItem.md) | 0..* <br/> [SourceItem](SourceItem.md) | SourceItem reference: Provides the information needed to identify the source ... | direct |
| [coding](coding.md) | 0..* <br/> [Coding](Coding.md) | Coding reference: Coding references a symbol from a defined code system. It u... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Origin](Origin.md) | [sourceItems](sourceItems.md) | range | [SourceItems](SourceItems.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/SourceItems](https://wiki.cdisc.org/display/PUB/SourceItems)

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
description: Identifies source items as needed to support automated data capture and
  end-to-end traceability.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SourceItems
rank: 1000
slots:
- sourceItem
- coding
slot_usage:
  sourceItem:
    name: sourceItem
    multivalued: true
    domain_of:
    - SourceItems
    range: SourceItem
    inlined: true
    inlined_as_list: true
  coding:
    name: coding
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
description: Identifies source items as needed to support automated data capture and
  end-to-end traceability.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SourceItems
rank: 1000
slot_usage:
  sourceItem:
    name: sourceItem
    multivalued: true
    domain_of:
    - SourceItems
    range: SourceItem
    inlined: true
    inlined_as_list: true
  coding:
    name: coding
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
  sourceItem:
    name: sourceItem
    description: 'SourceItem reference: Provides the information needed to identify
      the source metadata.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: sourceItem
    owner: SourceItems
    domain_of:
    - SourceItems
    range: SourceItem
    inlined: true
    inlined_as_list: true
  coding:
    name: coding
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
    alias: coding
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