# Class: Coding

_Coding references a symbol from a defined code system. It uses a code defined in a terminology system to associate semantics with a given term, codelist, variable, or group of variables. The presence of a Coding element associates a meaning to its parent element. Including multiple Coding elements for a given parent indicates synonymous meanings provided by different code systems or code system versions._




URI: [odm:Coding](http://www.cdisc.org/ns/odm/v2.0/Coding)


```mermaid
erDiagram
Coding {
    text code  
    uriorcurie system  
    text systemName  
    text systemVersion  
    text label  
    uriorcurie href  
    uriorcurie ref  
    text commentOID  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [code](code.md) | 0..1 <br/> [text](text.md) | A string pattern that identifies a concept as defined by the code system. | direct |
| [system](system.md) | 1..1 <br/> [uriorcurie](uriorcurie.md) | Identifies the code system that defines the code. If the code is taken from a... | direct |
| [systemName](systemName.md) | 0..1 <br/> [text](text.md) | Human readable name for the code system. | direct |
| [systemVersion](systemVersion.md) | 0..1 <br/> [text](text.md) | Identifies the version of the code system | direct |
| [label](label.md) | 0..1 <br/> [text](text.md) | Used to link the value to a named MethodDef parameter. | direct |
| [href](href.md) | 0..1 <br/> [uriorcurie](uriorcurie.md) | URI reference to the Code definition. | direct |
| [ref](ref.md) | 0..1 <br/> [uriorcurie](uriorcurie.md) | Reference to a local instance of the code system. | direct |
| [commentOID](commentOID.md) | 0..1 <br/> [text](text.md) | Reference to a CommentDef that provides the rationale for the use of the Conc... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEventGroupDef](StudyEventGroupDef.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [StudyEventDef](StudyEventDef.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [ItemGroupDef](ItemGroupDef.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [Origin](Origin.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [SourceItems](SourceItems.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [SourceItem](SourceItem.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [ItemDef](ItemDef.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [CodeList](CodeList.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [CodeListItem](CodeListItem.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [StudyIndication](StudyIndication.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [StudyIntervention](StudyIntervention.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [StudyTargetPopulation](StudyTargetPopulation.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [StudyParameter](StudyParameter.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [ParameterValue](ParameterValue.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [Criterion](Criterion.md) | [coding](coding.md) | range | [Coding](Coding.md) |
| [Annotation](Annotation.md) | [coding](coding.md) | range | [Coding](Coding.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Coding](https://wiki.cdisc.org/display/PUB/Coding)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Coding |
| native | odm:Coding |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Coding
description: Coding references a symbol from a defined code system. It uses a code
  defined in a terminology system to associate semantics with a given term, codelist,
  variable, or group of variables. The presence of a Coding element associates a meaning
  to its parent element. Including multiple Coding elements for a given parent indicates
  synonymous meanings provided by different code systems or code system versions.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Coding
rank: 1000
slots:
- code
- system
- systemName
- systemVersion
- label
- href
- ref
- commentOID
slot_usage:
  code:
    name: code
    description: A string pattern that identifies a concept as defined by the code
      system.
    comments:
    - 'Optional

      range: text

      When not provided, all codes in the code system are allowed. For example, when
      referencing the complete set of codes from the MedDRA code system.'
    domain_of:
    - FormalExpression
    - Coding
    range: text
  system:
    name: system
    description: Identifies the code system that defines the code. If the code is
      taken from a code system resource then the URL for the code system should be
      used.
    comments:
    - 'Required

      range: URI'
    domain_of:
    - Coding
    range: uriorcurie
    required: true
  systemName:
    name: systemName
    description: Human readable name for the code system.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - Coding
    range: text
  systemVersion:
    name: systemVersion
    description: Identifies the version of the code system
    comments:
    - 'Optional

      range: text'
    domain_of:
    - Coding
    range: text
  label:
    name: label
    description: Used to link the value to a named MethodDef parameter.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - Resource
    - Coding
    range: text
  href:
    name: href
    description: URI reference to the Code definition.
    comments:
    - 'Optional

      range: URI'
    domain_of:
    - Leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: uriorcurie
  ref:
    name: ref
    description: Reference to a local instance of the code system.
    comments:
    - 'Optional

      range: URI'
    domain_of:
    - ExternalCodeLib
    - Coding
    range: uriorcurie
  commentOID:
    name: commentOID
    description: Reference to a CommentDef that provides the rationale for the use
      of the Concept.
    comments:
    - 'Optional

      range: oidref

      Must match the OID attribute of a CommentDef element within in this Study/MetaDataVersion.'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: text
class_uri: odm:Coding

```
</details>

### Induced

<details>
```yaml
name: Coding
description: Coding references a symbol from a defined code system. It uses a code
  defined in a terminology system to associate semantics with a given term, codelist,
  variable, or group of variables. The presence of a Coding element associates a meaning
  to its parent element. Including multiple Coding elements for a given parent indicates
  synonymous meanings provided by different code systems or code system versions.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Coding
rank: 1000
slot_usage:
  code:
    name: code
    description: A string pattern that identifies a concept as defined by the code
      system.
    comments:
    - 'Optional

      range: text

      When not provided, all codes in the code system are allowed. For example, when
      referencing the complete set of codes from the MedDRA code system.'
    domain_of:
    - FormalExpression
    - Coding
    range: text
  system:
    name: system
    description: Identifies the code system that defines the code. If the code is
      taken from a code system resource then the URL for the code system should be
      used.
    comments:
    - 'Required

      range: URI'
    domain_of:
    - Coding
    range: uriorcurie
    required: true
  systemName:
    name: systemName
    description: Human readable name for the code system.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - Coding
    range: text
  systemVersion:
    name: systemVersion
    description: Identifies the version of the code system
    comments:
    - 'Optional

      range: text'
    domain_of:
    - Coding
    range: text
  label:
    name: label
    description: Used to link the value to a named MethodDef parameter.
    comments:
    - 'Optional

      range: text'
    domain_of:
    - Resource
    - Coding
    range: text
  href:
    name: href
    description: URI reference to the Code definition.
    comments:
    - 'Optional

      range: URI'
    domain_of:
    - Leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: uriorcurie
  ref:
    name: ref
    description: Reference to a local instance of the code system.
    comments:
    - 'Optional

      range: URI'
    domain_of:
    - ExternalCodeLib
    - Coding
    range: uriorcurie
  commentOID:
    name: commentOID
    description: Reference to a CommentDef that provides the rationale for the use
      of the Concept.
    comments:
    - 'Optional

      range: oidref

      Must match the OID attribute of a CommentDef element within in this Study/MetaDataVersion.'
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: text
attributes:
  code:
    name: code
    description: A string pattern that identifies a concept as defined by the code
      system.
    comments:
    - 'Optional

      range: text

      When not provided, all codes in the code system are allowed. For example, when
      referencing the complete set of codes from the MedDRA code system.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: code
    owner: Coding
    domain_of:
    - FormalExpression
    - Coding
    range: text
  system:
    name: system
    description: Identifies the code system that defines the code. If the code is
      taken from a code system resource then the URL for the code system should be
      used.
    comments:
    - 'Required

      range: URI'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: system
    owner: Coding
    domain_of:
    - Coding
    range: uriorcurie
    required: true
  systemName:
    name: systemName
    description: Human readable name for the code system.
    comments:
    - 'Optional

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: systemName
    owner: Coding
    domain_of:
    - Coding
    range: text
  systemVersion:
    name: systemVersion
    description: Identifies the version of the code system
    comments:
    - 'Optional

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: systemVersion
    owner: Coding
    domain_of:
    - Coding
    range: text
  label:
    name: label
    description: Used to link the value to a named MethodDef parameter.
    comments:
    - 'Optional

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: label
    owner: Coding
    domain_of:
    - Resource
    - Coding
    range: text
  href:
    name: href
    description: URI reference to the Code definition.
    comments:
    - 'Optional

      range: URI'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: href
    owner: Coding
    domain_of:
    - Leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: uriorcurie
  ref:
    name: ref
    description: Reference to a local instance of the code system.
    comments:
    - 'Optional

      range: URI'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ref
    owner: Coding
    domain_of:
    - ExternalCodeLib
    - Coding
    range: uriorcurie
  commentOID:
    name: commentOID
    description: Reference to a CommentDef that provides the rationale for the use
      of the Concept.
    comments:
    - 'Optional

      range: oidref

      Must match the OID attribute of a CommentDef element within in this Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: commentOID
    owner: Coding
    domain_of:
    - MetaDataVersion
    - Standard
    - WhereClauseDef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - Coding
    range: text
class_uri: odm:Coding

```
</details>