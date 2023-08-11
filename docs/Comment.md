# Class: Comment



URI: [odm:Comment](http://www.cdisc.org/ns/odm/v2.0/Comment)



```mermaid
 classDiagram
    class Comment
      Comment : SponsorOrSite
        
          Comment --|> CommentType : SponsorOrSite
        
      Comment : TranslatedTextRef
        
          Comment --|> TranslatedText : TranslatedTextRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [SponsorOrSite](SponsorOrSite.md) | 0..1 <br/> [CommentType](CommentType.md) |  | direct |
| [TranslatedTextRef](TranslatedTextRef.md) | 1..* <br/> [TranslatedText](TranslatedText.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Annotation](Annotation.md) | [CommentRef](CommentRef.md) | range | [Comment](Comment.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Comment](https://wiki.cdisc.org/display/ODM2/Comment)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Comment |
| native | odm:Comment |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Comment
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Comment
slots:
- SponsorOrSite
- TranslatedTextRef
slot_usage:
  SponsorOrSite:
    name: SponsorOrSite
    domain_of:
    - Comment
    range: CommentType
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
class_uri: odm:Comment

```
</details>

### Induced

<details>
```yaml
name: Comment
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Comment
slot_usage:
  SponsorOrSite:
    name: SponsorOrSite
    domain_of:
    - Comment
    range: CommentType
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
  SponsorOrSite:
    name: SponsorOrSite
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SponsorOrSite
    owner: Comment
    domain_of:
    - Comment
    range: CommentType
  TranslatedTextRef:
    name: TranslatedTextRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: TranslatedTextRef
    owner: Comment
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
class_uri: odm:Comment

```
</details>