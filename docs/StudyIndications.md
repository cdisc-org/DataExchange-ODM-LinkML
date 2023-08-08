# Class: StudyIndications



URI: [odm:StudyIndications](http://www.cdisc.org/ns/odm/v2.0/StudyIndications)



```mermaid
 classDiagram
    class StudyIndications
      StudyIndications : StudyIndicationRef
        
          StudyIndications --|> StudyIndication : StudyIndicationRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyIndicationRef](StudyIndicationRef.md) | 1..* <br/> [StudyIndication](StudyIndication.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [StudyIndicationsRef](StudyIndicationsRef.md) | range | [StudyIndications](StudyIndications.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyIndications |
| native | odm:StudyIndications |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyIndications
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- StudyIndicationRef
slot_usage:
  StudyIndicationRef:
    name: StudyIndicationRef
    multivalued: true
    domain_of:
    - StudyIndications
    range: StudyIndication
    required: true
    minimum_cardinality: 1
class_uri: odm:StudyIndications

```
</details>

### Induced

<details>
```yaml
name: StudyIndications
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  StudyIndicationRef:
    name: StudyIndicationRef
    multivalued: true
    domain_of:
    - StudyIndications
    range: StudyIndication
    required: true
    minimum_cardinality: 1
attributes:
  StudyIndicationRef:
    name: StudyIndicationRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: StudyIndicationRef
    owner: StudyIndications
    domain_of:
    - StudyIndications
    range: StudyIndication
    required: true
    minimum_cardinality: 1
class_uri: odm:StudyIndications

```
</details>