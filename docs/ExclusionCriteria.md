# Class: ExclusionCriteria

_The ExclusionCriteria is a container element for Criterion elements describing exclusion criteria for subjects in the study. When a list is provided, not meeting any of the criteria in the list may lead to exclusion of enrollment in the study._




URI: [odm:ExclusionCriteria](http://www.cdisc.org/ns/odm/v2.0/ExclusionCriteria)


```mermaid
erDiagram
ExclusionCriteria {

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

ExclusionCriteria ||--}o Criterion : "criterion"
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
| [InclusionExclusionCriteria](InclusionExclusionCriteria.md) | [exclusionCriteria](exclusionCriteria.md) | range | [ExclusionCriteria](ExclusionCriteria.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/ExclusionCriteria](https://wiki.cdisc.org/display/PUB/ExclusionCriteria)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ExclusionCriteria |
| native | odm:ExclusionCriteria |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExclusionCriteria
description: The ExclusionCriteria is a container element for Criterion elements describing
  exclusion criteria for subjects in the study. When a list is provided, not meeting
  any of the criteria in the list may lead to exclusion of enrollment in the study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ExclusionCriteria
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
class_uri: odm:ExclusionCriteria

```
</details>

### Induced

<details>
```yaml
name: ExclusionCriteria
description: The ExclusionCriteria is a container element for Criterion elements describing
  exclusion criteria for subjects in the study. When a list is provided, not meeting
  any of the criteria in the list may lead to exclusion of enrollment in the study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ExclusionCriteria
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
    owner: ExclusionCriteria
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    range: Criterion
    inlined: true
    inlined_as_list: true
class_uri: odm:ExclusionCriteria

```
</details>