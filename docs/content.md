# Slot: content


_multi-line text content from between XML tags_



URI: [odm:content](http://www.cdisc.org/ns/odm/v2.0/content)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TranslatedText](TranslatedText.md) | Human-readable text that is appropriate for a particular language. Translated... |  yes  |
[Title](Title.md) | Text with the label for the document or dataset. |  yes  |
[CheckValue](CheckValue.md) | A comparison value used in a range check. |  yes  |
[Code](Code.md) | Contains the source code that represents a FormalExpression in a given Contex... |  yes  |
[WorkflowEnd](WorkflowEnd.md) | A WorkflowEnd references a structural element with which the workflows ends. |  yes  |
[UserName](UserName.md) | The user's login identification in the sender's system. |  yes  |
[Prefix](Prefix.md) | Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhi... |  yes  |
[Suffix](Suffix.md) | This element may include credentials, or suffixes (e.g., Jr., III). |  yes  |
[FullName](FullName.md) | The user's full formal name. May be a combination of Prefix, GivenName, Famil... |  yes  |
[GivenName](GivenName.md) | The user's initial given name or all given names. |  yes  |
[FamilyName](FamilyName.md) | The user's surname (family name). |  yes  |
[StreetName](StreetName.md) | The street name part of a user's postal address. |  yes  |
[HouseNumber](HouseNumber.md) | The house number part of a user's postal address. |  yes  |
[City](City.md) | The city name part of a user's postal address. |  yes  |
[StateProv](StateProv.md) | The state or province name part of a user's postal address. |  yes  |
[Country](Country.md) | The country name part of a user's postal address. For CDISC SDTM or trial reg... |  yes  |
[PostalCode](PostalCode.md) | The postal code part of a user's postal address. |  yes  |
[OtherText](OtherText.md) | Any other text needed as part of a user's postal address. |  yes  |
[Meaning](Meaning.md) | A short name or description for this signature. It should reflect the context... |  yes  |
[LegalReason](LegalReason.md) | The responsibility statement associated with a signature (e.g., "The signer a... |  yes  |
[DateTimeStamp](DateTimeStamp.md) | Date and time when an action was performed. |  yes  |
[ReasonForChange](ReasonForChange.md) | A user-supplied reason for a data change. |  yes  |
[SourceID](SourceID.md) | Information that identifies the source of the data within an originating syst... |  yes  |
[FlagValue](FlagValue.md) | The value of the flag. The meaning of this value is typically dependent on th... |  yes  |
[FlagType](FlagType.md) | The type of flag. This determines the purpose and semantics of the flag. |  yes  |
[Value](Value.md) | The data collected for an item. This data is represented according to DataTyp... |  yes  |







## Properties

* Range: [contentType](contentType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: content
description: multi-line text content from between XML tags
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: content
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
range: contentType
inlined: true

```
</details>