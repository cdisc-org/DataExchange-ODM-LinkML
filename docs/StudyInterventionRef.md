# Class: StudyInterventionRef

_The StudyInterventionRef references an intervention that is taken as the treatment for the estimand._




URI: [odm:StudyInterventionRef](http://www.cdisc.org/ns/odm/v2.0/StudyInterventionRef)


```mermaid
erDiagram
StudyInterventionRef {
    oidref studyInterventionOID  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyInterventionOID](studyInterventionOID.md) | 1..1 <br/> [oidref](oidref.md) | Reference to a StudyIntervention | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEstimand](StudyEstimand.md) | [studyInterventionRef](studyInterventionRef.md) | range | [StudyInterventionRef](StudyInterventionRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyInterventionRef](https://wiki.cdisc.org/display/PUB/StudyInterventionRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyInterventionRef |
| native | odm:StudyInterventionRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyInterventionRef
description: The StudyInterventionRef references an intervention that is taken as
  the treatment for the estimand.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyInterventionRef
rank: 1000
slots:
- studyInterventionOID
slot_usage:
  studyInterventionOID:
    name: studyInterventionOID
    description: Reference to a StudyIntervention
    comments:
    - 'Required

      range: oidref'
    domain_of:
    - StudyInterventionRef
    range: oidref
    required: true
class_uri: odm:StudyInterventionRef

```
</details>

### Induced

<details>
```yaml
name: StudyInterventionRef
description: The StudyInterventionRef references an intervention that is taken as
  the treatment for the estimand.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyInterventionRef
rank: 1000
slot_usage:
  studyInterventionOID:
    name: studyInterventionOID
    description: Reference to a StudyIntervention
    comments:
    - 'Required

      range: oidref'
    domain_of:
    - StudyInterventionRef
    range: oidref
    required: true
attributes:
  studyInterventionOID:
    name: studyInterventionOID
    description: Reference to a StudyIntervention
    comments:
    - 'Required

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyInterventionOID
    owner: StudyInterventionRef
    domain_of:
    - StudyInterventionRef
    range: oidref
    required: true
class_uri: odm:StudyInterventionRef

```
</details>