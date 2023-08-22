# Class: FullName


_The user's full formal name. May be a combination of Prefix, GivenName, FamilyName & Suffix. Intended to be used for display._





URI: [odm:FullName](http://www.cdisc.org/ns/odm/v2.0/FullName)



```mermaid
 classDiagram
    class FullName
      FullName : _content
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [_content](_content.md) | 0..1 <br/> [_contentType](_contentType.md) | multi-line text content from between XML tags | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [User](User.md) | [FullNameRef](FullNameRef.md) | range | [FullName](FullName.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/FullName](https://wiki.cdisc.org/display/ODM2/FullName)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:FullName |
| native | odm:FullName |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FullName
description: The user's full formal name. May be a combination of Prefix, GivenName,
  FamilyName & Suffix. Intended to be used for display.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/FullName
slots:
- _content
slot_usage:
  range:
    name: range
    id_prefixes:
    - text
class_uri: odm:FullName

```
</details>

### Induced

<details>
```yaml
name: FullName
description: The user's full formal name. May be a combination of Prefix, GivenName,
  FamilyName & Suffix. Intended to be used for display.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/FullName
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
  owner: FullName
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
class_uri: odm:FullName

```
</details>