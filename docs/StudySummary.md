# Class: StudySummary

_The StudyParameter element allows to provide a set of study design parameters such as anticipated number of subjects, minimum and maximum age of the participants, or planned number of arms._




URI: [odm:StudySummary](http://www.cdisc.org/ns/odm/v2.0/StudySummary)


```mermaid
erDiagram
StudySummary {

}
StudyParameter {
    oid OID  
    name Term  
    name ShortName  
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
ParameterValue {
    text ValueRef  
}

StudySummary ||--}o StudyParameter : "StudyParameterRef"
StudyParameter ||--|o ParameterValue : "ParameterValueRef"
StudyParameter ||--}o Coding : "CodingRef"
ParameterValue ||--}o Coding : "CodingRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyParameterRef](StudyParameterRef.md) | 0..* <br/> [StudyParameter](StudyParameter.md) | StudyParameter reference: A StudyParameter defines a study design parameter f... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [StudySummaryRef](StudySummaryRef.md) | range | [StudySummary](StudySummary.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/StudySummary](https://wiki.cdisc.org/display/ODM2/StudySummary)

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
- https://wiki.cdisc.org/display/ODM2/StudySummary
rank: 1000
slots:
- StudyParameterRef
slot_usage:
  StudyParameterRef:
    name: StudyParameterRef
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
- https://wiki.cdisc.org/display/ODM2/StudySummary
rank: 1000
slot_usage:
  StudyParameterRef:
    name: StudyParameterRef
    multivalued: true
    domain_of:
    - StudySummary
    range: StudyParameter
    inlined: true
    inlined_as_list: true
attributes:
  StudyParameterRef:
    name: StudyParameterRef
    description: 'StudyParameter reference: A StudyParameter defines a study design
      parameter for which the value or values are delivered in the ParameterValue
      child element or elements.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: StudyParameterRef
    owner: StudySummary
    domain_of:
    - StudySummary
    range: StudyParameter
    inlined: true
    inlined_as_list: true
class_uri: odm:StudySummary

```
</details>