# Class: StudyInterventions


_The StudyInterventions element is a container element for individual StudyIntervention elements.Element NameStudyInterventionsParent Element(s)ProtocolElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyInterventionsElement Text ValueNoneAttributesNoneChild Elements(StudyIntervention+)Usage/Business Rules_





URI: [odm:StudyInterventions](http://www.cdisc.org/ns/odm/v2.0/StudyInterventions)



```mermaid
 classDiagram
    class StudyInterventions
      StudyInterventions : StudyInterventionRefRef
        
          StudyInterventions --|> StudyIntervention : StudyInterventionRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyInterventionRefRef](StudyInterventionRefRef.md) | 0..* <br/> [StudyIntervention](StudyIntervention.md) |  | direct |





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
  StudyIntervention elements.Element NameStudyInterventionsParent Element(s)ProtocolElement
  XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyInterventionsElement Text ValueNoneAttributesNoneChild
  Elements(StudyIntervention+)Usage/Business Rules
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyInterventions
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
  StudyIntervention elements.Element NameStudyInterventionsParent Element(s)ProtocolElement
  XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyInterventionsElement Text ValueNoneAttributesNoneChild
  Elements(StudyIntervention+)Usage/Business Rules
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/StudyInterventions
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