# Class: ErrorMessage



URI: [odm:ErrorMessage](http://www.cdisc.org/ns/odm/v2.0/ErrorMessage)



```mermaid
 classDiagram
    class ErrorMessage
      ErrorMessage : TranslatedTextRef
        
          ErrorMessage --|> TranslatedText : TranslatedTextRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [TranslatedTextRef](TranslatedTextRef.md) | 1..* <br/> [TranslatedText](TranslatedText.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RangeCheck](RangeCheck.md) | [ErrorMessageRef](ErrorMessageRef.md) | range | [ErrorMessage](ErrorMessage.md) |






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
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- TranslatedTextRef
slot_usage:
  TranslatedTextRef:
    name: TranslatedTextRef
    multivalued: true
    list_elements_unique: true
    domain_of:
    - Description
    - Question
    - ErrorMessage
    - Decode
    - Comment
    range: TranslatedText
    required: true
    minimum_cardinality: 1
class_uri: odm:ErrorMessage

```
</details>

### Induced

<details>
```yaml
name: ErrorMessage
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  TranslatedTextRef:
    name: TranslatedTextRef
    multivalued: true
    list_elements_unique: true
    domain_of:
    - Description
    - Question
    - ErrorMessage
    - Decode
    - Comment
    range: TranslatedText
    required: true
    minimum_cardinality: 1
attributes:
  TranslatedTextRef:
    name: TranslatedTextRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    list_elements_unique: true
    alias: TranslatedTextRef
    owner: ErrorMessage
    domain_of:
    - Description
    - Question
    - ErrorMessage
    - Decode
    - Comment
    range: TranslatedText
    required: true
    minimum_cardinality: 1
class_uri: odm:ErrorMessage

```
</details>