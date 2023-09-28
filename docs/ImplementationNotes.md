# Class: ImplementationNotes

_Further information, such as rationale and implementation instructions, on how to implement the CRF data collection fields._




URI: [odm:ImplementationNotes](http://www.cdisc.org/ns/odm/v2.0/ImplementationNotes)


```mermaid
erDiagram
ImplementationNotes {

}
TranslatedText {
    languageType language  
    text type  
    contentType content  
}

ImplementationNotes ||--}o TranslatedText : "translatedText"

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
| [ItemDef](ItemDef.md) | [implementationNotes](implementationNotes.md) | range | [ImplementationNotes](ImplementationNotes.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/ImplementationNotes](https://wiki.cdisc.org/display/PUB/ImplementationNotes)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ImplementationNotes |
| native | odm:ImplementationNotes |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImplementationNotes
description: Further information, such as rationale and implementation instructions,
  on how to implement the CRF data collection fields.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ImplementationNotes
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
class_uri: odm:ImplementationNotes

```
</details>

### Induced

<details>
```yaml
name: ImplementationNotes
description: Further information, such as rationale and implementation instructions,
  on how to implement the CRF data collection fields.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ImplementationNotes
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
    owner: ImplementationNotes
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
class_uri: odm:ImplementationNotes

```
</details>