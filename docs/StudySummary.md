# Class: StudySummary

_The StudyParameter element allows to provide a set of study design parameters such as anticipated number of subjects, minimum and maximum age of the participants, or planned number of arms._




URI: [odm:StudySummary](http://www.cdisc.org/ns/odm/v2.0/StudySummary)


```mermaid
erDiagram
StudySummary {

}
StudyParameter {
    oid OID  
    nameType term  
    nameType shortName  
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
ParameterValue {
    text value  
}

StudySummary ||--}o StudyParameter : "studyParameter"
StudyParameter ||--|o ParameterValue : "parameterValue"
StudyParameter ||--}o Coding : "coding"
ParameterValue ||--}o Coding : "coding"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyParameter](studyParameter.md) | 0..* <br/> [StudyParameter](StudyParameter.md) | StudyParameter reference: A StudyParameter defines a study design parameter f... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [studySummary](studySummary.md) | range | [StudySummary](StudySummary.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudySummary](https://wiki.cdisc.org/display/PUB/StudySummary)

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
description: The StudyParameter element allows to provide a set of study design parameters
  such as anticipated number of subjects, minimum and maximum age of the participants,
  or planned number of arms.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudySummary
rank: 1000
slots:
- studyParameter
slot_usage:
  studyParameter:
    name: studyParameter
    multivalued: true
    domain_of:
    - StudySummary
    range: StudyParameter
    inlined: true
    inlined_as_list: true
class_uri: odm:StudySummary

```
</details>

### Induced

<details>
```yaml
name: StudySummary
description: The StudyParameter element allows to provide a set of study design parameters
  such as anticipated number of subjects, minimum and maximum age of the participants,
  or planned number of arms.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudySummary
rank: 1000
slot_usage:
  studyParameter:
    name: studyParameter
    multivalued: true
    domain_of:
    - StudySummary
    range: StudyParameter
    inlined: true
    inlined_as_list: true
attributes:
  studyParameter:
    name: studyParameter
    description: 'StudyParameter reference: A StudyParameter defines a study design
      parameter for which the value or values are delivered in the ParameterValue
      child element or elements.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: studyParameter
    owner: StudySummary
    domain_of:
    - StudySummary
    range: StudyParameter
    inlined: true
    inlined_as_list: true
class_uri: odm:StudySummary

```
</details>