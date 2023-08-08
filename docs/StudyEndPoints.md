# Class: StudyEndPoints



URI: [odm:StudyEndPoints](http://www.cdisc.org/ns/odm/v2.0/StudyEndPoints)



```mermaid
 classDiagram
    class StudyEndPoints
      StudyEndPoints : StudyEndPointRef
        
          StudyEndPoints --|> StudyEndPoint : StudyEndPointRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyEndPointRef](StudyEndPointRef.md) | 1..* <br/> [StudyEndPoint](StudyEndPoint.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [StudyEndPointsRef](StudyEndPointsRef.md) | range | [StudyEndPoints](StudyEndPoints.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyEndPoints |
| native | odm:StudyEndPoints |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyEndPoints
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- StudyEndPointRef
slot_usage:
  StudyEndPointRef:
    name: StudyEndPointRef
    multivalued: true
    domain_of:
    - StudyEndPoints
    range: StudyEndPoint
    required: true
    minimum_cardinality: 1
class_uri: odm:StudyEndPoints

```
</details>

### Induced

<details>
```yaml
name: StudyEndPoints
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  StudyEndPointRef:
    name: StudyEndPointRef
    multivalued: true
    domain_of:
    - StudyEndPoints
    range: StudyEndPoint
    required: true
    minimum_cardinality: 1
attributes:
  StudyEndPointRef:
    name: StudyEndPointRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: StudyEndPointRef
    owner: StudyEndPoints
    domain_of:
    - StudyEndPoints
    range: StudyEndPoint
    required: true
    minimum_cardinality: 1
class_uri: odm:StudyEndPoints

```
</details>