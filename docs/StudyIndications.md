# Class: StudyIndications

_StudyIndications is a container element for individual StudyIndication elements._




URI: [odm:StudyIndications](http://www.cdisc.org/ns/odm/v2.0/StudyIndications)


```mermaid
erDiagram
StudyIndications {

}
StudyIndication {
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

StudyIndications ||--}o StudyIndication : "StudyIndicationRef"
StudyIndication ||--|o Description : "DescriptionRef"
StudyIndication ||--}o Coding : "CodingRef"
Description ||--}o TranslatedText : "TranslatedTextRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StudyIndicationRef](StudyIndicationRef.md) | 0..* <br/> [StudyIndication](StudyIndication.md) | StudyIndication reference: This element describes a study indication (e.g., c... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




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
rank: 1000
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
rank: 1000
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
    description: 'StudyIndication reference: This element describes a study indication
      (e.g., condition, disease) for the clinical study. The human-readable description
      is provided in the Description element. The Coding element can be used to provide
      a machine-readable code for the indication (e.g., SNOMED-CT code 26929004 for
      "Alzheimer''s disease").'
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