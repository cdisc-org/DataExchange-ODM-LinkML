# Class: StudySummary



URI: [odm:StudySummary](http://www.cdisc.org/ns/odm/v2.0/StudySummary)



```mermaid
 classDiagram
    class StudySummary
      StudySummary : StudyParameterRef
        
          StudySummary --|> StudyParameter : StudyParameterRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyParameterRef](StudyParameterRef.md) | 1..* <br/> [StudyParameter](StudyParameter.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [StudySummaryRef](StudySummaryRef.md) | range | [StudySummary](StudySummary.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudySummary |
| native | odm:StudySummary |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudySummary
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- StudyParameterRef
slot_usage:
  StudyParameterRef:
    name: StudyParameterRef
    multivalued: true
    domain_of:
    - StudySummary
    range: StudyParameter
    required: true
    minimum_cardinality: 1
class_uri: odm:StudySummary

```
</details>

### Induced

<details>
```yaml
name: StudySummary
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  StudyParameterRef:
    name: StudyParameterRef
    multivalued: true
    domain_of:
    - StudySummary
    range: StudyParameter
    required: true
    minimum_cardinality: 1
attributes:
  StudyParameterRef:
    name: StudyParameterRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: StudyParameterRef
    owner: StudySummary
    domain_of:
    - StudySummary
    range: StudyParameter
    required: true
    minimum_cardinality: 1
class_uri: odm:StudySummary

```
</details>