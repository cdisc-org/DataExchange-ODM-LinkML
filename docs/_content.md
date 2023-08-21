# Slot: _content


_multi-line text content from between XML tags_



URI: [odm:_content](http://www.cdisc.org/ns/odm/v2.0/_content)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TranslatedText](TranslatedText.md) | Human-readable text that is appropriate for a particular language. Translated... |  yes  |
[CheckValue](CheckValue.md) | A comparison value used in a range check. |  no  |
[Code](Code.md) | Contains the source code that represents a FormalExpression in a given Contex... |  no  |
[WorkflowEnd](WorkflowEnd.md) | A WorkflowEnd references a structural element with which the workflows ends. |  yes  |
[UserName](UserName.md) | The user's login identification in the sender's system. |  no  |
[Prefix](Prefix.md) | Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhi... |  no  |
[Suffix](Suffix.md) | This element may include credentials, or suffixes (e.g., Jr., III). |  no  |
[FullName](FullName.md) | The user's full formal name. May be a combination of Prefix, GivenName, Famil... |  no  |
[GivenName](GivenName.md) | The user's initial given name or all given names. |  no  |
[FamilyName](FamilyName.md) | The user's surname (family name). |  no  |
[StreetName](StreetName.md) | The street name part of a user's postal address. |  no  |
[HouseNumber](HouseNumber.md) | The house number part of a user's postal address. |  no  |
[City](City.md) | The city name part of a user's postal address. |  no  |
[StateProv](StateProv.md) | The state or province name part of a user's postal address. |  no  |
[Country](Country.md) | The country name part of a user's postal address. For CDISC SDTM or trial reg... |  no  |
[PostalCode](PostalCode.md) | The postal code part of a user's postal address. |  no  |
[OtherText](OtherText.md) | Any other text needed as part of a user's postal address. |  no  |
[Meaning](Meaning.md) | A short name or description for this signature. It should reflect the context... |  no  |
[LegalReason](LegalReason.md) | The responsibility statement associated with a signature (e.g., "The signer a... |  no  |
[DateTimeStamp](DateTimeStamp.md) |  |  no  |
[ReasonForChange](ReasonForChange.md) | A user-supplied reason for a data change. |  no  |
[SourceID](SourceID.md) | Information that identifies the source of the data within an originating syst... |  no  |
[FlagValue](FlagValue.md) | The value of the flag. The meaning of this value is typically dependent on th... |  yes  |
[FlagType](FlagType.md) | The type of flag. This determines the purpose and semantics of the flag. |  yes  |
[Value](Value.md) | The data collected for an item. This data is represented according to DataTyp... |  yes  |







## Properties

* Range: [_contentType](_contentType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: _content
description: multi-line text content from between XML tags
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: _content
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

```
</details>