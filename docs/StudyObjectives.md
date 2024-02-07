# Class: StudyObjectives

_The StudyObjectives is a container element for individual StudyObjective elements._




URI: [odm:StudyObjectives](http://www.cdisc.org/ns/odm/v2.0/StudyObjectives)


```mermaid
erDiagram
StudyObjectives {

}
StudyObjective {
    oid OID  
    nameType name  
    StudyObjectiveLevel level  
}
StudyEndPointRef {
    positiveInteger orderNumber  
}
Description {

}

StudyObjectives ||--}o StudyObjective : "studyObjective"
StudyObjective ||--|o Description : "description"
StudyObjective ||--}o StudyEndPointRef : "studyEndPointRef"
StudyEndPointRef ||--|| StudyEndPoint : "studyEndPointOID"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyObjective](studyObjective.md) | 0..* <br/> [StudyObjective](StudyObjective.md) | StudyObjective reference: The reason for performing a study in terms of the s... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [studyObjectives](studyObjectives.md) | range | [StudyObjectives](StudyObjectives.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyObjectives](https://wiki.cdisc.org/display/PUB/StudyObjectives)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyObjectives |
| native | odm:StudyObjectives |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyObjectives
description: The StudyObjectives is a container element for individual StudyObjective
  elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyObjectives
rank: 1000
slots:
- studyObjective
slot_usage:
  studyObjective:
    name: studyObjective
    multivalued: true
    domain_of:
    - StudyObjectives
    range: StudyObjective
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyObjectives

```
</details>

### Induced

<details>
```yaml
name: StudyObjectives
description: The StudyObjectives is a container element for individual StudyObjective
  elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyObjectives
rank: 1000
slot_usage:
  studyObjective:
    name: studyObjective
    multivalued: true
    domain_of:
    - StudyObjectives
    range: StudyObjective
    inlined: true
    inlined_as_list: true
attributes:
  studyObjective:
    name: studyObjective
    description: 'StudyObjective reference: The reason for performing a study in terms
      of the scientific questions to be answered by the analysis of data collected
      during the study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: studyObjective
    owner: StudyObjectives
    domain_of:
    - StudyObjectives
    range: StudyObjective
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyObjectives

```
</details>