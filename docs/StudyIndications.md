# Class: StudyIndications


_StudyIndications is a container element for individual StudyIndication elements._





URI: [odm:StudyIndications](http://www.cdisc.org/ns/odm/v2.0/StudyIndications)



```mermaid
 classDiagram
    class StudyIndications
      StudyIndications : StudyIndicationRef
        
          StudyIndications --|> StudyIndication : StudyIndicationRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyIndicationRef](StudyIndicationRef.md) | 0..* <br/> [StudyIndication](StudyIndication.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [StudyIndicationsRef](StudyIndicationsRef.md) | range | [StudyIndications](StudyIndications.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/StudyIndications](https://wiki.cdisc.org/display/ODM2/StudyIndications)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyIndications |
| native | odm:StudyIndications |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyIndications
description: StudyIndications is a container element for individual StudyIndication
  elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyIndications
slots:
- StudyIndicationRef
slot_usage:
  StudyIndicationRef:
    name: StudyIndicationRef
    multivalued: true
    domain_of:
    - StudyIndications
    range: StudyIndication
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyIndications

```
</details>

### Induced

<details>
```yaml
name: StudyIndications
description: StudyIndications is a container element for individual StudyIndication
  elements.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyIndications
slot_usage:
  StudyIndicationRef:
    name: StudyIndicationRef
    multivalued: true
    domain_of:
    - StudyIndications
    range: StudyIndication
    inlined: true
    inlined_as_list: true
attributes:
  StudyIndicationRef:
    name: StudyIndicationRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: StudyIndicationRef
    owner: StudyIndications
    domain_of:
    - StudyIndications
    range: StudyIndication
    inlined: true
    inlined_as_list: true
class_uri: odm:StudyIndications

```
</details>