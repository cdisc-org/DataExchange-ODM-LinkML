# Class: StudyInterventions

_The StudyInterventions element is a container element for individual StudyIntervention elements._




URI: [odm:StudyInterventions](http://www.cdisc.org/ns/odm/v2.0/StudyInterventions)


```mermaid
erDiagram
StudyInterventions {

}
StudyIntervention {
    oid OID  
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
Description {

}

StudyInterventions ||--}o StudyIntervention : "StudyInterventionRefRef"
StudyIntervention ||--|o Description : "DescriptionRef"
StudyIntervention ||--}o Coding : "CodingRef"
Description ||--}o TranslatedText : "TranslatedTextRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyInterventionRefRef](StudyInterventionRefRef.md) | 0..* <br/> [StudyIntervention](StudyIntervention.md) | StudyInterventionRef reference: The StudyInterventionRef references an interv... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [StudyInterventionsRef](StudyInterventionsRef.md) | range | [StudyInterventions](StudyInterventions.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/StudyInterventions](https://wiki.cdisc.org/display/ODM2/StudyInterventions)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyInterventions |
| native | odm:StudyInterventions |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyInterventions
description: The StudyInterventions element is a container element for individual
  StudyIntervention elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyInterventions
rank: 1000
slots:
- StudyInterventionRefRef
slot_usage:
  StudyInterventionRefRef:
    name: StudyInterventionRefRef
    multivalued: true
    domain_of:
    - StudyInterventions
    - StudyEstimand
    range: StudyIntervention
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyInterventions

```
</details>

### Induced

<details>
```yaml
name: StudyInterventions
description: The StudyInterventions element is a container element for individual
  StudyIntervention elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyInterventions
rank: 1000
slot_usage:
  StudyInterventionRefRef:
    name: StudyInterventionRefRef
    multivalued: true
    domain_of:
    - StudyInterventions
    - StudyEstimand
    range: StudyIntervention
    inlined: true
    inlined_as_list: true
attributes:
  StudyInterventionRefRef:
    name: StudyInterventionRefRef
    description: 'StudyInterventionRef reference: The StudyInterventionRef references
      an intervention that is taken as the treatment for the estimand.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: StudyInterventionRefRef
    owner: StudyInterventions
    domain_of:
    - StudyInterventions
    - StudyEstimand
    range: StudyIntervention
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyInterventions

```
</details>