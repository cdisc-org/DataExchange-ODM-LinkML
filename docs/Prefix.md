# Class: Prefix


_Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhir/datatypes.html#humanname)._





URI: [odm:Prefix](http://www.cdisc.org/ns/odm/v2.0/Prefix)



```mermaid
 classDiagram
    class Prefix
      Prefix : _content
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [_content](_content.md) | 0..1 <br/> [ContentType](ContentType.md) | multi-line text content from between XML tags | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [User](User.md) | [PrefixRef](PrefixRef.md) | range | [Prefix](Prefix.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Prefix](https://wiki.cdisc.org/display/ODM2/Prefix)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Prefix |
| native | odm:Prefix |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Prefix
description: Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhir/datatypes.html#humanname).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Prefix
slots:
- _content
slot_usage:
  range:
    name: range
    id_prefixes:
    - text
class_uri: odm:Prefix

```
</details>

### Induced

<details>
```yaml
name: Prefix
description: Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhir/datatypes.html#humanname).
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Prefix
slot_usage:
  range:
    name: range
    id_prefixes:
    - text
attributes:
  name: _content
  description: multi-line text content from between XML tags
  from_schema: http://www.cdisc.org/ns/odm/v2.0
  rank: 1000
  alias: _content
  owner: Prefix
  domain_of:
  - TranslatedText
  - CheckValue
  - Code
  - WorkflowEnd
  - UserName
  - Prefix
  - Suffix
  - FullName
  - GivenName
  - FamilyName
  - StreetName
  - HouseNumber
  - City
  - StateProv
  - Country
  - PostalCode
  - OtherText
  - Meaning
  - LegalReason
  - DateTimeStamp
  - ReasonForChange
  - SourceID
  - FlagValue
  - FlagType
  - Value
  range: _contentType
  inlined: true
class_uri: odm:Prefix

```
</details>