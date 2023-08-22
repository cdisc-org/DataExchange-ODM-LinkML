# Class: DateTimeStamp


_Date and time when an action was performed._





URI: [odm:DateTimeStamp](http://www.cdisc.org/ns/odm/v2.0/DateTimeStamp)



```mermaid
 classDiagram
    class DateTimeStamp
      DateTimeStamp : _content
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [_content](_content.md) | 0..1 <br/> [_contentType](_contentType.md) | multi-line text content from between XML tags | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AuditRecord](AuditRecord.md) | [DateTimeStampRef](DateTimeStampRef.md) | range | [DateTimeStamp](DateTimeStamp.md) |
| [Signature](Signature.md) | [DateTimeStampRef](DateTimeStampRef.md) | range | [DateTimeStamp](DateTimeStamp.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/DateTimeStamp](https://wiki.cdisc.org/display/ODM2/DateTimeStamp)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:DateTimeStamp |
| native | odm:DateTimeStamp |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DateTimeStamp
description: Date and time when an action was performed.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/DateTimeStamp
slots:
- _content
slot_usage:
  range:
    name: range
    id_prefixes:
    - datetime
class_uri: odm:DateTimeStamp

```
</details>

### Induced

<details>
```yaml
name: DateTimeStamp
description: Date and time when an action was performed.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/DateTimeStamp
slot_usage:
  range:
    name: range
    id_prefixes:
    - datetime
attributes:
  name: _content
  description: multi-line text content from between XML tags
  from_schema: http://www.cdisc.org/ns/odm/v2.0
  rank: 1000
  alias: _content
  owner: DateTimeStamp
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
class_uri: odm:DateTimeStamp

```
</details>