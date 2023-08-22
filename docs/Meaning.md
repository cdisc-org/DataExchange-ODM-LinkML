# Class: Meaning


_A short name or description for this signature. It should reflect the context of the signature and/or the text that appears when the signature is applied in the user interface._





URI: [odm:Meaning](http://www.cdisc.org/ns/odm/v2.0/Meaning)



```mermaid
 classDiagram
    class Meaning
      Meaning : _content
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [_content](_content.md) | 0..1 <br/> [_contentType](_contentType.md) | multi-line text content from between XML tags | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SignatureDef](SignatureDef.md) | [MeaningRef](MeaningRef.md) | range | [Meaning](Meaning.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Meaning](https://wiki.cdisc.org/display/ODM2/Meaning)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Meaning |
| native | odm:Meaning |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Meaning
description: A short name or description for this signature. It should reflect the
  context of the signature and/or the text that appears when the signature is applied
  in the user interface.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Meaning
slots:
- _content
slot_usage:
  range:
    name: range
    id_prefixes:
    - text
class_uri: odm:Meaning

```
</details>

### Induced

<details>
```yaml
name: Meaning
description: A short name or description for this signature. It should reflect the
  context of the signature and/or the text that appears when the signature is applied
  in the user interface.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Meaning
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
  owner: Meaning
  domain_of:
  - TranslatedText
  - Title
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
class_uri: odm:Meaning

```
</details>