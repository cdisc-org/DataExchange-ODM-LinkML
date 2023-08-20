# Class: InclusionCriteria


_The InclusionCriteria is a container element for Criterion elements describing inclusion criteria for subjects in the study. When a list is provided, subjects must meet each of the criteria in the list in order to enroll in the study._





URI: [odm:InclusionCriteria](http://www.cdisc.org/ns/odm/v2.0/InclusionCriteria)



```mermaid
 classDiagram
    class InclusionCriteria
      InclusionCriteria : CriterionRef
        
          InclusionCriteria --|> Criterion : CriterionRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [CriterionRef](CriterionRef.md) | 0..* <br/> [Criterion](Criterion.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [InclusionExclusionCriteria](InclusionExclusionCriteria.md) | [InclusionCriteriaRef](InclusionCriteriaRef.md) | range | [InclusionCriteria](InclusionCriteria.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/InclusionCriteria](https://wiki.cdisc.org/display/ODM2/InclusionCriteria)

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
- https://wiki.cdisc.org/display/ODM2/InclusionCriteria
slots:
- CriterionRef
slot_usage:
  CriterionRef:
    name: CriterionRef
    multivalued: true
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    - EntryCriteria
    - ExitCriteria
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
- https://wiki.cdisc.org/display/ODM2/InclusionCriteria
slot_usage:
  CriterionRef:
    name: CriterionRef
    multivalued: true
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    - EntryCriteria
    - ExitCriteria
    range: Criterion
    inlined: true
    inlined_as_list: true
attributes:
  CriterionRef:
    name: CriterionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: CriterionRef
    owner: InclusionCriteria
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    - EntryCriteria
    - ExitCriteria
    range: Criterion
    inlined: true
    inlined_as_list: true
class_uri: odm:InclusionCriteria

```
</details>