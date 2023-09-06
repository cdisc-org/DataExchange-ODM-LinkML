# Class: StudyEndPoints

_The StudyEndPoints element is a container element for individual StudyEndPoint elements._




URI: [odm:StudyEndPoints](http://www.cdisc.org/ns/odm/v2.0/StudyEndPoints)


```mermaid
erDiagram
StudyEndPoints {

}
StudyEndPoint {
    oid oID  
    nameType name  
    StudyEndPointType type  
    StudyEstimandLevel level  
}
FormalExpression {
    text context  
}
Description {

}

StudyEndPoints ||--}o StudyEndPoint : "studyEndPoint"
StudyEndPoint ||--|o Description : "description"
StudyEndPoint ||--}o FormalExpression : "formalExpression"
FormalExpression ||--|o Code : "code"
FormalExpression ||--|o ExternalCodeLib : "externalCodeLib"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyEndPoint](studyEndPoint.md) | 0..* <br/> [StudyEndPoint](StudyEndPoint.md) | StudyEndPoint reference: A study end point reflects an outcome measure of int... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [studyEndPoints](studyEndPoints.md) | range | [StudyEndPoints](StudyEndPoints.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyEndPoints](https://wiki.cdisc.org/display/PUB/StudyEndPoints)

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
description: The StudyEndPoints element is a container element for individual StudyEndPoint
  elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEndPoints
rank: 1000
slots:
- studyEndPoint
slot_usage:
  studyEndPoint:
    name: studyEndPoint
    multivalued: true
    domain_of:
    - StudyEndPoints
    range: StudyEndPoint
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyEndPoints

```
</details>

### Induced

<details>
```yaml
name: StudyEndPoints
description: The StudyEndPoints element is a container element for individual StudyEndPoint
  elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEndPoints
rank: 1000
slot_usage:
  studyEndPoint:
    name: studyEndPoint
    multivalued: true
    domain_of:
    - StudyEndPoints
    range: StudyEndPoint
    inlined: true
    inlined_as_list: true
attributes:
  studyEndPoint:
    name: studyEndPoint
    description: 'StudyEndPoint reference: A study end point reflects an outcome measure
      of interest that is statistically analyzed to address a particular research
      question for the study. It typically specifies the type of assessments made;
      the timing of those assessments; the assessment tools used; and other details,
      as applicable, such as how multiple assessments within an individual are to
      be combined.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: studyEndPoint
    owner: StudyEndPoints
    domain_of:
    - StudyEndPoints
    range: StudyEndPoint
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyEndPoints

```
</details>