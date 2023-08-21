# Slot: TranslatedTextRef


_TranslatedText reference: Human-readable text that is appropriate for a particular language. TranslatedText elements typically occur in a series, presenting a set of alternative textual renditions for different languages and types._



URI: [odm:TranslatedTextRef](http://www.cdisc.org/ns/odm/v2.0/TranslatedTextRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Description](Description.md) | A free-text description of the containing metadata component, unless restrict... |  yes  |
[Question](Question.md) | A label shown to a human user when prompted to provide data for an item on pa... |  yes  |
[Definition](Definition.md) | Definition of the item. |  yes  |
[Prompt](Prompt.md) | A prompt text shown to a human user when prompted to provide data for an item... |  yes  |
[CRFCompletionInstructions](CRFCompletionInstructions.md) | Instructions for the clinical site on how to enter collected information on t... |  yes  |
[ImplementationNotes](ImplementationNotes.md) | Further information, such as rationale and implementation instructions, on ho... |  yes  |
[CDISCNotes](CDISCNotes.md) | Explanatory text for the variable. |  yes  |
[ErrorMessage](ErrorMessage.md) | Error message provided to user when the range check fails. |  yes  |
[Decode](Decode.md) | The displayed value relating to the CodeListItem/@CodedValue. This is often a... |  yes  |
[Comment](Comment.md) | A free-text (uninterpreted) comment about clinical data. The comment may have... |  yes  |







## Properties

* Range: [TranslatedText](TranslatedText.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TranslatedTextRef
description: 'TranslatedText reference: Human-readable text that is appropriate for
  a particular language. TranslatedText elements typically occur in a series, presenting
  a set of alternative textual renditions for different languages and types.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: TranslatedTextRef
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

```
</details>