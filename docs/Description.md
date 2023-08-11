# Class: Description



URI: [odm:Description](http://www.cdisc.org/ns/odm/v2.0/Description)



```mermaid
 classDiagram
    class Description
      Description : TranslatedTextRef
        
          Description --|> TranslatedText : TranslatedTextRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [TranslatedTextRef](TranslatedTextRef.md) | 1..* <br/> [TranslatedText](TranslatedText.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [MetaDataVersion](MetaDataVersion.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [ValueListDef](ValueListDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyEventGroupRef](StudyEventGroupRef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyEventGroupDef](StudyEventGroupDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyEventDef](StudyEventDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [ItemGroupDef](ItemGroupDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [Origin](Origin.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [ItemDef](ItemDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [CodeList](CodeList.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [CodeListItem](CodeListItem.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [MethodDef](MethodDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [ConditionDef](ConditionDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [CommentDef](CommentDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [Protocol](Protocol.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyStructure](StudyStructure.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [TrialPhase](TrialPhase.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyIndication](StudyIndication.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyIntervention](StudyIntervention.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyObjective](StudyObjective.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyEndPoint](StudyEndPoint.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyTargetPopulation](StudyTargetPopulation.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [StudyEstimand](StudyEstimand.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [IntercurrentEvent](IntercurrentEvent.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [SummaryMeasure](SummaryMeasure.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [Arm](Arm.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [Epoch](Epoch.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [TransitionTimingConstraint](TransitionTimingConstraint.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [RelativeTimingConstraint](RelativeTimingConstraint.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [DurationTimingConstraint](DurationTimingConstraint.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [WorkflowDef](WorkflowDef.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [Criterion](Criterion.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [ExceptionEvent](ExceptionEvent.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [Organization](Organization.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [Location](Location.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |
| [ODMFileMetadata](ODMFileMetadata.md) | [DescriptionRef](DescriptionRef.md) | range | [Description](Description.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Description](https://wiki.cdisc.org/display/ODM2/Description)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Description |
| native | odm:Description |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Description
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Description
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
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
class_uri: odm:Description

```
</details>

### Induced

<details>
```yaml
name: Description
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Description
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
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
attributes:
  TranslatedTextRef:
    name: TranslatedTextRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: TranslatedTextRef
    owner: Description
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
    required: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
class_uri: odm:Description

```
</details>