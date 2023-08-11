# Class: StudyTargetPopulationRef



URI: [odm:StudyTargetPopulationRef](http://www.cdisc.org/ns/odm/v2.0/StudyTargetPopulationRef)



```mermaid
 classDiagram
    class StudyTargetPopulationRef
      StudyTargetPopulationRef : StudyTargetPopulationOID
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyTargetPopulationOID](StudyTargetPopulationOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEstimand](StudyEstimand.md) | [StudyTargetPopulationRefRef](StudyTargetPopulationRefRef.md) | range | [StudyTargetPopulationRef](StudyTargetPopulationRef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/StudyTargetPopulationRef](https://wiki.cdisc.org/display/ODM2/StudyTargetPopulationRef)

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
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyTargetPopulationRef
slots:
- StudyTargetPopulationOID
slot_usage:
  StudyTargetPopulationOID:
    name: StudyTargetPopulationOID
    domain_of:
    - StudyTargetPopulationRef
    range: oidref
    required: true
class_uri: odm:StudyTargetPopulationRef

```
</details>

### Induced

<details>
```yaml
name: StudyTargetPopulationRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyTargetPopulationRef
slot_usage:
  StudyTargetPopulationOID:
    name: StudyTargetPopulationOID
    domain_of:
    - StudyTargetPopulationRef
    range: oidref
    required: true
attributes:
  StudyTargetPopulationOID:
    name: StudyTargetPopulationOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StudyTargetPopulationOID
    owner: StudyTargetPopulationRef
    domain_of:
    - StudyTargetPopulationRef
    range: oidref
    required: true
class_uri: odm:StudyTargetPopulationRef

```
</details>