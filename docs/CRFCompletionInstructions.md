# Class: CRFCompletionInstructions


_Instructions for the clinical site on how to enter collected information on the CRF._





URI: [odm:CRFCompletionInstructions](http://www.cdisc.org/ns/odm/v2.0/CRFCompletionInstructions)



```mermaid
 classDiagram
    class CRFCompletionInstructions
      CRFCompletionInstructions : TranslatedTextRef
        
          CRFCompletionInstructions --|> TranslatedText : TranslatedTextRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [TranslatedTextRef](TranslatedTextRef.md) | 0..* <br/> [TranslatedText](TranslatedText.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemDef](ItemDef.md) | [CRFCompletionInstructionsRef](CRFCompletionInstructionsRef.md) | range | [CRFCompletionInstructions](CRFCompletionInstructions.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/CRFCompletionInstructions](https://wiki.cdisc.org/display/ODM2/CRFCompletionInstructions)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:CRFCompletionInstructions |
| native | odm:CRFCompletionInstructions |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CRFCompletionInstructions
description: Instructions for the clinical site on how to enter collected information
  on the CRF.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/CRFCompletionInstructions
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
class_uri: odm:CRFCompletionInstructions

```
</details>

### Induced

<details>
```yaml
name: CRFCompletionInstructions
description: Instructions for the clinical site on how to enter collected information
  on the CRF.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/CRFCompletionInstructions
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
    owner: CRFCompletionInstructions
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
class_uri: odm:CRFCompletionInstructions

```
</details>