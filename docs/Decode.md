# Class: Decode


_The displayed value relating to the CodeListItem/@CodedValue. This is often a label corresponding to a short name or alpha-numeric code. The actual Decode text is provided in a TranslatedText element so that it can be provided in different languages on a case report form or tabular data summary._





URI: [odm:Decode](http://www.cdisc.org/ns/odm/v2.0/Decode)



```mermaid
 classDiagram
    class Decode
      Decode : TranslatedTextRef
        
          Decode --|> TranslatedText : TranslatedTextRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [TranslatedTextRef](TranslatedTextRef.md) | 0..* <br/> [TranslatedText](TranslatedText.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CodeListItem](CodeListItem.md) | [DecodeRef](DecodeRef.md) | range | [Decode](Decode.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Decode](https://wiki.cdisc.org/display/ODM2/Decode)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Decode |
| native | odm:Decode |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Decode
description: The displayed value relating to the CodeListItem/@CodedValue. This is
  often a label corresponding to a short name or alpha-numeric code. The actual Decode
  text is provided in a TranslatedText element so that it can be provided in different
  languages on a case report form or tabular data summary.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Decode
slots:
- TranslatedTextRef
slot_usage:
  TranslatedTextRef:
    name: TranslatedTextRef
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
class_uri: odm:Decode

```
</details>

### Induced

<details>
```yaml
name: Decode
description: The displayed value relating to the CodeListItem/@CodedValue. This is
  often a label corresponding to a short name or alpha-numeric code. The actual Decode
  text is provided in a TranslatedText element so that it can be provided in different
  languages on a case report form or tabular data summary.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Decode
slot_usage:
  TranslatedTextRef:
    name: TranslatedTextRef
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
  TranslatedTextRef:
    name: TranslatedTextRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: TranslatedTextRef
    owner: Decode
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
class_uri: odm:Decode

```
</details>