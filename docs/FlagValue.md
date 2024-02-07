# Class: FlagValue

_The value of the flag. The meaning of this value is typically dependent on the associated FlagType. The actual value must be a member of the referenced CodeList_




URI: [odm:FlagValue](http://www.cdisc.org/ns/odm/v2.0/FlagValue)


```mermaid
erDiagram
FlagValue {
    nameType content  
}
CodeList {
    oid OID  
    nameType name  
    CLDataType dataType  
    YesOnly isNonStandard  
}
Alias {
    text context  
    text name  
}
Coding {
    text code  
    uriorcurie system  
    text systemName  
    text systemVersion  
    text label  
    uriorcurie href  
    uriorcurie ref  
    text commentOID  
}
CodeListItem {
    valueType codedValue  
    decimal rank  
    YesOnly other  
    positiveInteger orderNumber  
    YesOnly extendedValue  
}
Description {

}
Standard {
    oid OID  
    StandardName name  
    StandardType type  
    StandardPublishingSet publishingSet  
    text version  
    StandardStatus status  
}
CommentDef {
    oid OID  
}

FlagValue ||--|| CodeList : "codeListOID"
CodeList ||--|o CommentDef : "commentOID"
CodeList ||--|o Standard : "standardOID"
CodeList ||--|o Description : "description"
CodeList ||--}o CodeListItem : "codeListItem"
CodeList ||--}o Coding : "coding"
CodeList ||--}o Alias : "alias"
CodeListItem ||--|o CommentDef : "commentOID"
CodeListItem ||--|o Description : "description"
CodeListItem ||--|o Decode : "decode"
CodeListItem ||--}o Coding : "coding"
CodeListItem ||--}o Alias : "alias"
Description ||--}o TranslatedText : "translatedText"
Standard ||--|o CommentDef : "commentOID"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [codeListOID](codeListOID.md) | 1..1 <br/> [CodeList](CodeList.md) | Reference to the CodeList definition. | direct |
| [content](content.md) | 0..1 <br/> [nameType](nameType.md) | multi-line text content from between XML tags | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Flag](Flag.md) | [flagValue](flagValue.md) | range | [FlagValue](FlagValue.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/FlagValue](https://wiki.cdisc.org/display/PUB/FlagValue)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:FlagValue |
| native | odm:FlagValue |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FlagValue
description: The value of the flag. The meaning of this value is typically dependent
  on the associated FlagType. The actual value must be a member of the referenced
  CodeList
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/FlagValue
rank: 1000
slots:
- codeListOID
- content
slot_usage:
  codeListOID:
    name: codeListOID
    description: Reference to the CodeList definition.
    comments:
    - 'Required

      range: oidref

      The valid values for a FlagValue are provided by the study sponsor. Must match
      the OID for a CodeList element in the Study/MetaDataVersion.'
    domain_of:
    - CodeListRef
    - FlagValue
    - FlagType
    range: CodeList
    required: true
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
    range: nameType
class_uri: odm:FlagValue

```
</details>

### Induced

<details>
```yaml
name: FlagValue
description: The value of the flag. The meaning of this value is typically dependent
  on the associated FlagType. The actual value must be a member of the referenced
  CodeList
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/FlagValue
rank: 1000
slot_usage:
  codeListOID:
    name: codeListOID
    description: Reference to the CodeList definition.
    comments:
    - 'Required

      range: oidref

      The valid values for a FlagValue are provided by the study sponsor. Must match
      the OID for a CodeList element in the Study/MetaDataVersion.'
    domain_of:
    - CodeListRef
    - FlagValue
    - FlagType
    range: CodeList
    required: true
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
    range: nameType
attributes:
  codeListOID:
    name: codeListOID
    description: Reference to the CodeList definition.
    comments:
    - 'Required

      range: oidref

      The valid values for a FlagValue are provided by the study sponsor. Must match
      the OID for a CodeList element in the Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: codeListOID
    owner: FlagValue
    domain_of:
    - CodeListRef
    - FlagValue
    - FlagType
    range: CodeList
    required: true
  content:
    name: content
    description: multi-line text content from between XML tags
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: content
    owner: FlagValue
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
    range: nameType
    inlined: true
class_uri: odm:FlagValue

```
</details>