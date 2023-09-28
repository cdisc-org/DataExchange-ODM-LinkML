# Class: ErrorMessage

_Error message provided to user when the range check fails._




URI: [odm:ErrorMessage](http://www.cdisc.org/ns/odm/v2.0/ErrorMessage)


```mermaid
erDiagram
ErrorMessage {

}
TranslatedText {
    languageType language  
    text type  
    contentType content  
}

ErrorMessage ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [translatedText](translatedText.md) | 0..* <br/> [TranslatedText](TranslatedText.md) | TranslatedText reference: Human-readable text that is appropriate for a parti... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RangeCheck](RangeCheck.md) | [errorMessage](errorMessage.md) | range | [ErrorMessage](ErrorMessage.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/ErrorMessage](https://wiki.cdisc.org/display/PUB/ErrorMessage)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ErrorMessage |
| native | odm:ErrorMessage |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ErrorMessage
description: Error message provided to user when the range check fails.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ErrorMessage
rank: 1000
slots:
- translatedText
slot_usage:
  translatedText:
    name: translatedText
    multivalued: true
    domain_of:
    - Description
    - Question
    - Definition
    - Prompt
    - CRFCompletionInstructions
    - ImplementationNotes
    - CDISCNotes
    - ErrorMessage
    - Decode
    - Comment
    range: TranslatedText
    inlined: true
    inlined_as_list: true
class_uri: odm:ErrorMessage

```
</details>

### Induced

<details>
```yaml
name: ErrorMessage
description: Error message provided to user when the range check fails.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ErrorMessage
rank: 1000
slot_usage:
  translatedText:
    name: translatedText
    multivalued: true
    domain_of:
    - Description
    - Question
    - Definition
    - Prompt
    - CRFCompletionInstructions
    - ImplementationNotes
    - CDISCNotes
    - ErrorMessage
    - Decode
    - Comment
    range: TranslatedText
    inlined: true
    inlined_as_list: true
attributes:
  translatedText:
    name: translatedText
    description: 'TranslatedText reference: Human-readable text that is appropriate
      for a particular language. TranslatedText elements typically occur in a series,
      presenting a set of alternative textual renditions for different languages and
      types.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: translatedText
    owner: ErrorMessage
    domain_of:
    - Description
    - Question
    - Definition
    - Prompt
    - CRFCompletionInstructions
    - ImplementationNotes
    - CDISCNotes
    - ErrorMessage
    - Decode
    - Comment
    range: TranslatedText
    inlined: true
    inlined_as_list: true
class_uri: odm:ErrorMessage

```
</details>