# Class: StudyTargetPopulationRef

_The StudyTargetPopulationRef references a StudyTargetPopulation to which the estimand applies._




URI: [odm:StudyTargetPopulationRef](http://www.cdisc.org/ns/odm/v2.0/StudyTargetPopulationRef)


```mermaid
erDiagram
StudyTargetPopulationRef {

}
StudyTargetPopulation {
    oid OID  
    nameType name  
}
FormalExpression {
    text context  
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
Description {

}

StudyTargetPopulationRef ||--|| StudyTargetPopulation : "studyTargetPopulationOID"
StudyTargetPopulation ||--|o Description : "description"
StudyTargetPopulation ||--}o Coding : "coding"
StudyTargetPopulation ||--}o FormalExpression : "formalExpression"
FormalExpression ||--|o Code : "code"
FormalExpression ||--|o ExternalCodeLib : "externalCodeLib"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyTargetPopulationOID](studyTargetPopulationOID.md) | 1..1 <br/> [StudyTargetPopulation](StudyTargetPopulation.md) | StudyTargetPopulation reference: The StudyTargetPopulation describes the popu... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEstimand](StudyEstimand.md) | [studyTargetPopulationRef](studyTargetPopulationRef.md) | range | [StudyTargetPopulationRef](StudyTargetPopulationRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyTargetPopulationRef](https://wiki.cdisc.org/display/PUB/StudyTargetPopulationRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyTargetPopulationRef |
| native | odm:StudyTargetPopulationRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyTargetPopulationRef
description: The StudyTargetPopulationRef references a StudyTargetPopulation to which
  the estimand applies.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyTargetPopulationRef
rank: 1000
slots:
- studyTargetPopulationOID
slot_usage:
  studyTargetPopulationOID:
    name: studyTargetPopulationOID
    domain_of:
    - StudyTargetPopulationRef
    range: StudyTargetPopulation
    required: true
class_uri: odm:StudyTargetPopulationRef

```
</details>

### Induced

<details>
```yaml
name: StudyTargetPopulationRef
description: The StudyTargetPopulationRef references a StudyTargetPopulation to which
  the estimand applies.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyTargetPopulationRef
rank: 1000
slot_usage:
  studyTargetPopulationOID:
    name: studyTargetPopulationOID
    domain_of:
    - StudyTargetPopulationRef
    range: StudyTargetPopulation
    required: true
attributes:
  studyTargetPopulationOID:
    name: studyTargetPopulationOID
    description: 'StudyTargetPopulation reference: The StudyTargetPopulation describes
      the population targeted for the clinical study.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyTargetPopulationOID
    owner: StudyTargetPopulationRef
    domain_of:
    - StudyTargetPopulationRef
    range: StudyTargetPopulation
    required: true
class_uri: odm:StudyTargetPopulationRef

```
</details>