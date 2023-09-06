# Class: Origin

_Origin defines the source metadata, where applicable, for ODM ItemRefs or ItemGroupRefs. Origin as a child element replaces the Origin attribute in ODM v1.3 that exists for the ItemDef and ItemGroupDef elements.The Origin element is based on the def:Origin element in Define-XML v2.1 with the Trace-XML v1.0 extension._




URI: [odm:Origin](http://www.cdisc.org/ns/odm/v2.0/Origin)


```mermaid
erDiagram
Origin {
    OriginType type  
    OriginSource source  
}
DocumentRef {
    oid leafID  
}
PDFPageRef {
    text pageRefs  
    positiveInteger firstPage  
    positiveInteger lastPage  
    PDFPageType type  
    text title  
}
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
SourceItems {

}
SourceItem {
    oidref itemOID  
    oidref itemGroupOID  
    oidref metaDataVersionOID  
    oidref studyOID  
    oidref leafID  
    nameType name  
}
Description {

}
TranslatedText {
    languageType language  
    text type  
    contentType content  
}

Origin ||--|o Description : "description"
Origin ||--|o SourceItems : "sourceItems"
Origin ||--}o Coding : "coding"
Origin ||--}o DocumentRef : "documentRef"
DocumentRef ||--}o PDFPageRef : "pDFPageRef"
SourceItems ||--}o SourceItem : "sourceItem"
SourceItems ||--}o Coding : "coding"
SourceItem ||--}o Resource : "resource"
SourceItem ||--}o Coding : "coding"
Description ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1..1 <br/> [OriginType](OriginType.md) | Identifies how the clinical data values were obtained. | direct |
| [source](source.md) | 0..1 <br/> [OriginSource](OriginSource.md) | Indicates the party responsible for the data's origin type. | direct |
| [description](description.md) | 0..1 <br/> [Description](Description.md) | Description reference: A free-text description of the containing metadata com... | direct |
| [sourceItems](sourceItems.md) | 0..1 <br/> [SourceItems](SourceItems.md) | SourceItems reference: Identifies source items as needed to support automated... | direct |
| [coding](coding.md) | 0..* <br/> [Coding](Coding.md) | Coding reference: Coding references a symbol from a defined code system. It u... | direct |
| [documentRef](documentRef.md) | 0..* <br/> [DocumentRef](DocumentRef.md) | The DocumentRef element is a container for page references in a PDF file. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemGroupDef](ItemGroupDef.md) | [origin](origin.md) | range | [Origin](Origin.md) |
| [ItemRef](ItemRef.md) | [origin](origin.md) | range | [Origin](Origin.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Origin](https://wiki.cdisc.org/display/PUB/Origin)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Origin |
| native | odm:Origin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Origin
description: Origin defines the source metadata, where applicable, for ODM ItemRefs
  or ItemGroupRefs. Origin as a child element replaces the Origin attribute in ODM
  v1.3 that exists for the ItemDef and ItemGroupDef elements.The Origin element is
  based on the def:Origin element in Define-XML v2.1 with the Trace-XML v1.0 extension.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Origin
rank: 1000
slots:
- type
- source
- description
- sourceItems
- coding
- documentRef
slot_usage:
  type:
    name: type
    description: Identifies how the clinical data values were obtained.
    comments:
    - 'Required

      range: text

      The list of allowable Origin/@Type attribute values is provided as non-extensible
      codelists in the CDISC Controlled Terminology, Define-XML package. * Users are
      encouraged to refer to the most recent version of the CDISC Controlled Terminology
      ( https://www.cdisc.org/standards/terminology/controlled-terminology ).'
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: OriginType
    required: true
  source:
    name: source
    description: Indicates the party responsible for the data's origin type.
    comments:
    - 'Optional

      range: text

      The list of allowable Origin/@Source attribute values is provided in the CDISC
      Controlled Terminology, Define-XML package. * Users are encouraged to refer
      to the most recent version of the CDISC Controlled Terminology ( https://www.cdisc.org/standards/terminology/controlled-terminology
      ).'
    domain_of:
    - Origin
    - Query
    range: OriginSource
  description:
    name: description
    domain_of:
    - Study
    - MetaDataVersion
    - ValueListDef
    - StudyEventGroupRef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - CommentDef
    - Protocol
    - StudyStructure
    - TrialPhase
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - IntercurrentEvent
    - SummaryMeasure
    - Arm
    - Epoch
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Criterion
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  sourceItems:
    name: sourceItems
    domain_of:
    - Origin
    range: SourceItems
    maximum_cardinality: 1
  coding:
    name: coding
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
  documentRef:
    name: documentRef
    multivalued: true
    domain_of:
    - AnnotatedCRF
    - SupplementalDoc
    - Origin
    - MethodDef
    - CommentDef
    range: DocumentRef
    inlined: true
    inlined_as_list: true
class_uri: odm:Origin

```
</details>

### Induced

<details>
```yaml
name: Origin
description: Origin defines the source metadata, where applicable, for ODM ItemRefs
  or ItemGroupRefs. Origin as a child element replaces the Origin attribute in ODM
  v1.3 that exists for the ItemDef and ItemGroupDef elements.The Origin element is
  based on the def:Origin element in Define-XML v2.1 with the Trace-XML v1.0 extension.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Origin
rank: 1000
slot_usage:
  type:
    name: type
    description: Identifies how the clinical data values were obtained.
    comments:
    - 'Required

      range: text

      The list of allowable Origin/@Type attribute values is provided as non-extensible
      codelists in the CDISC Controlled Terminology, Define-XML package. * Users are
      encouraged to refer to the most recent version of the CDISC Controlled Terminology
      ( https://www.cdisc.org/standards/terminology/controlled-terminology ).'
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: OriginType
    required: true
  source:
    name: source
    description: Indicates the party responsible for the data's origin type.
    comments:
    - 'Optional

      range: text

      The list of allowable Origin/@Source attribute values is provided in the CDISC
      Controlled Terminology, Define-XML package. * Users are encouraged to refer
      to the most recent version of the CDISC Controlled Terminology ( https://www.cdisc.org/standards/terminology/controlled-terminology
      ).'
    domain_of:
    - Origin
    - Query
    range: OriginSource
  description:
    name: description
    domain_of:
    - Study
    - MetaDataVersion
    - ValueListDef
    - StudyEventGroupRef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - CommentDef
    - Protocol
    - StudyStructure
    - TrialPhase
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - IntercurrentEvent
    - SummaryMeasure
    - Arm
    - Epoch
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Criterion
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  sourceItems:
    name: sourceItems
    domain_of:
    - Origin
    range: SourceItems
    maximum_cardinality: 1
  coding:
    name: coding
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
  documentRef:
    name: documentRef
    multivalued: true
    domain_of:
    - AnnotatedCRF
    - SupplementalDoc
    - Origin
    - MethodDef
    - CommentDef
    range: DocumentRef
    inlined: true
    inlined_as_list: true
attributes:
  type:
    name: type
    description: Identifies how the clinical data values were obtained.
    comments:
    - 'Required

      range: text

      The list of allowable Origin/@Type attribute values is provided as non-extensible
      codelists in the CDISC Controlled Terminology, Define-XML package. * Users are
      encouraged to refer to the most recent version of the CDISC Controlled Terminology
      ( https://www.cdisc.org/standards/terminology/controlled-terminology ).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: type
    owner: Origin
    domain_of:
    - TranslatedText
    - PDFPageRef
    - Standard
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - Resource
    - MethodDef
    - StudyEndPoint
    - TransitionTimingConstraint
    - RelativeTimingConstraint
    - Branching
    - Organization
    - Query
    range: OriginType
    required: true
  source:
    name: source
    description: Indicates the party responsible for the data's origin type.
    comments:
    - 'Optional

      range: text

      The list of allowable Origin/@Source attribute values is provided in the CDISC
      Controlled Terminology, Define-XML package. * Users are encouraged to refer
      to the most recent version of the CDISC Controlled Terminology ( https://www.cdisc.org/standards/terminology/controlled-terminology
      ).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: source
    owner: Origin
    domain_of:
    - Origin
    - Query
    range: OriginSource
  description:
    name: description
    description: 'Description reference: A free-text description of the containing
      metadata component, unless restricted by Business Rules.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: description
    owner: Origin
    domain_of:
    - Study
    - MetaDataVersion
    - ValueListDef
    - StudyEventGroupRef
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - ItemDef
    - CodeList
    - CodeListItem
    - MethodDef
    - ConditionDef
    - CommentDef
    - Protocol
    - StudyStructure
    - TrialPhase
    - StudyIndication
    - StudyIntervention
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - IntercurrentEvent
    - SummaryMeasure
    - Arm
    - Epoch
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Criterion
    - Organization
    - Location
    - ODMFileMetadata
    range: Description
    maximum_cardinality: 1
  sourceItems:
    name: sourceItems
    description: 'SourceItems reference: Identifies source items as needed to support
      automated data capture and end-to-end traceability.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: sourceItems
    owner: Origin
    domain_of:
    - Origin
    range: SourceItems
    maximum_cardinality: 1
  coding:
    name: coding
    description: 'Coding reference: Coding references a symbol from a defined code
      system. It uses a code defined in a terminology system to associate semantics
      with a given term, codelist, variable, or group of variables. The presence of
      a Coding element associates a meaning to its parent element. Including multiple
      Coding elements for a given parent indicates synonymous meanings provided by
      different code systems or code system versions.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: coding
    owner: Origin
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
  documentRef:
    name: documentRef
    description: The DocumentRef element is a container for page references in a PDF
      file.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    identifier: false
    alias: documentRef
    owner: Origin
    domain_of:
    - AnnotatedCRF
    - SupplementalDoc
    - Origin
    - MethodDef
    - CommentDef
    range: DocumentRef
    inlined: true
    inlined_as_list: true
class_uri: odm:Origin

```
</details>