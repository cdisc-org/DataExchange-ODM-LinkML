# Class: Value

_The data collected for an item. This data is represented according to DataType attribute of the ItemDef referenced by the ItemOID attribute in the parent ItemData element._




URI: [odm:Value](http://www.cdisc.org/ns/odm/v2.0/Value)


```mermaid
erDiagram
Value {
    positiveInteger seqNum  
    text content  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [seqNum](seqNum.md) | 0..1 <br/> [positiveInteger](positiveInteger.md) | When more than 1 Value element exists this attribute uniquely identifies each... | direct |
| [content](content.md) | 0..1 <br/> [text](text.md) | multi-line text content from between XML tags | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemData](ItemData.md) | [value](value.md) | range | [Value](Value.md) |
| [Query](Query.md) | [value](value.md) | range | [Value](Value.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Value](https://wiki.cdisc.org/display/PUB/Value)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Value |
| native | odm:Value |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Value
description: The data collected for an item. This data is represented according to
  DataType attribute of the ItemDef referenced by the ItemOID attribute in the parent
  ItemData element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Value
rank: 1000
slots:
- seqNum
- content
slot_usage:
  seqNum:
    name: seqNum
    description: When more than 1 Value element exists this attribute uniquely identifies
      each Value and defines the order of a Value in a list of Values.
    comments:
    - 'Conditional Required when the parent ItemData has more than one Value element.

      Must be unique within the ItemData element.'
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
  content:
    name: content
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
    range: text
class_uri: odm:Value

```
</details>

### Induced

<details>
```yaml
name: Value
description: The data collected for an item. This data is represented according to
  DataType attribute of the ItemDef referenced by the ItemOID attribute in the parent
  ItemData element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Value
rank: 1000
slot_usage:
  seqNum:
    name: seqNum
    description: When more than 1 Value element exists this attribute uniquely identifies
      each Value and defines the order of a Value in a list of Values.
    comments:
    - 'Conditional Required when the parent ItemData has more than one Value element.

      Must be unique within the ItemData element.'
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
  content:
    name: content
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
    range: text
attributes:
  seqNum:
    name: seqNum
    description: When more than 1 Value element exists this attribute uniquely identifies
      each Value and defines the order of a Value in a list of Values.
    comments:
    - 'Conditional Required when the parent ItemData has more than one Value element.

      Must be unique within the ItemData element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: seqNum
    owner: Value
    domain_of:
    - Annotation
    - Value
    range: positiveInteger
  content:
    name: content
    description: multi-line text content from between XML tags
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: content
    owner: Value
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
    range: text
    inlined: true
class_uri: odm:Value

```
</details>