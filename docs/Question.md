# Class: Question



URI: [odm:Question](http://www.cdisc.org/ns/odm/v2.0/Question)



```mermaid
 classDiagram
    class Question
      Question : TranslatedTextRef
        
          Question --|> TranslatedText : TranslatedTextRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [TranslatedTextRef](TranslatedTextRef.md) | 1..* <br/> [TranslatedText](TranslatedText.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemDef](ItemDef.md) | [QuestionRef](QuestionRef.md) | range | [Question](Question.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Question |
| native | odm:Question |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Question
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
class_uri: odm:Question

```
</details>

### Induced

<details>
```yaml
name: Question
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
    owner: Question
    domain_of:
    - Description
    - Question
    - ErrorMessage
    - Decode
    - Comment
    range: TranslatedText
    required: true
    minimum_cardinality: 1
class_uri: odm:Question

```
</details>