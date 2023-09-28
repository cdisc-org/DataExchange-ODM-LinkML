# Class: InclusionCriteria

_The InclusionCriteria is a container element for Criterion elements describing inclusion criteria for subjects in the study. When a list is provided, subjects must meet each of the criteria in the list in order to enroll in the study._




URI: [odm:InclusionCriteria](http://www.cdisc.org/ns/odm/v2.0/InclusionCriteria)


```mermaid
erDiagram
InclusionCriteria {

}
Criterion {
    oid oID  
    nameType name  
    oidref conditionOID  
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

InclusionCriteria ||--}o Criterion : "criterion"
Criterion ||--|o Description : "description"
Criterion ||--}o Coding : "coding"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [criterion](criterion.md) | 0..* <br/> [Criterion](Criterion.md) | Criterion reference: The Criterion represents either an inclusion or an exclu... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [InclusionExclusionCriteria](InclusionExclusionCriteria.md) | [inclusionCriteria](inclusionCriteria.md) | range | [InclusionCriteria](InclusionCriteria.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/InclusionCriteria](https://wiki.cdisc.org/display/PUB/InclusionCriteria)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:InclusionCriteria |
| native | odm:InclusionCriteria |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InclusionCriteria
description: The InclusionCriteria is a container element for Criterion elements describing
  inclusion criteria for subjects in the study. When a list is provided, subjects
  must meet each of the criteria in the list in order to enroll in the study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/InclusionCriteria
rank: 1000
slots:
- criterion
slot_usage:
  criterion:
    name: criterion
    multivalued: true
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    range: Criterion
    inlined: true
    inlined_as_list: true
class_uri: odm:InclusionCriteria

```
</details>

### Induced

<details>
```yaml
name: InclusionCriteria
description: The InclusionCriteria is a container element for Criterion elements describing
  inclusion criteria for subjects in the study. When a list is provided, subjects
  must meet each of the criteria in the list in order to enroll in the study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/InclusionCriteria
rank: 1000
slot_usage:
  criterion:
    name: criterion
    multivalued: true
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    range: Criterion
    inlined: true
    inlined_as_list: true
attributes:
  criterion:
    name: criterion
    description: 'Criterion reference: The Criterion represents either an inclusion
      or an exclusion criterion, depending on the parent element (i.e., InclusionCriteria,
      ExclusionCriteria).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: criterion
    owner: InclusionCriteria
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    range: Criterion
    inlined: true
    inlined_as_list: true
class_uri: odm:InclusionCriteria

```
</details>