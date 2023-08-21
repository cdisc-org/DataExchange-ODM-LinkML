# Class: EntryCriteria



URI: [odm:EntryCriteria](http://www.cdisc.org/ns/odm/v2.0/EntryCriteria)



```mermaid
 classDiagram
    class EntryCriteria
      EntryCriteria : CriterionRef
        
          EntryCriteria --|> Criterion : CriterionRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [CriterionRef](CriterionRef.md) | 0..* <br/> [Criterion](Criterion.md) | Criterion reference: The Criterion represents either an inclusion or an exclu... | direct |









## See Also

* [https://wiki.cdisc.org/display/ODM2/EntryCriteria](https://wiki.cdisc.org/display/ODM2/EntryCriteria)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:EntryCriteria |
| native | odm:EntryCriteria |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntryCriteria
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/EntryCriteria
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
class_uri: odm:EntryCriteria

```
</details>

### Induced

<details>
```yaml
name: EntryCriteria
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/EntryCriteria
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
    description: 'Criterion reference: The Criterion represents either an inclusion
      or an exclusion criterion, depending on the parent element (i.e., InclusionCriteria,
      ExclusionCriteria).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: CriterionRef
    owner: EntryCriteria
    domain_of:
    - InclusionCriteria
    - ExclusionCriteria
    - EntryCriteria
    - ExitCriteria
    range: Criterion
    inlined: true
    inlined_as_list: true
class_uri: odm:EntryCriteria

```
</details>