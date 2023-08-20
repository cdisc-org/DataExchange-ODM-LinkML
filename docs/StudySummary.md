# Class: StudySummary


_The StudyParameter element allows to provide a set of study design parameters such as anticipated number of subjects, minimum and maximum age of the participants, or planned number of arms._





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
| [StudyParameterRef](StudyParameterRef.md) | 0..* <br/> [StudyParameter](StudyParameter.md) |  | direct |





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