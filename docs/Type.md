# Slot: Type


_Type of page for page references indicated in the PageRefs attribute._



URI: [odm:Type](http://www.cdisc.org/ns/odm/v2.0/Type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TranslatedText](TranslatedText.md) | Human-readable text that is appropriate for a particular language. Translated... |  yes  |
[PDFPageRef](PDFPageRef.md) | This element is the container for CRF page references. |  yes  |
[Standard](Standard.md) | The Standard element describes each standard used within the MetaDataVersion ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |  yes  |
[Resource](Resource.md) | Describes an external resource used as the source for the parent ItemGroup or... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |
[RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |  yes  |
[Branching](Branching.md) | This element describes the branching in a workflow from a source (start) stru... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |
[Query](Query.md) | The Query element represents a request for clarification on a data item colle... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Type
description: Type of page for page references indicated in the PageRefs attribute.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Type
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
range: string
any_of:
- range: text
- range: StandardType
- range: PDFPageType
- range: EventType
- range: ItemGroupTypeType
- range: OriginType
- range: MethodType
- range: StudyEndPointType
- range: RelativeTimingConstraintType
- range: BranchingType
- range: OrganizationType
- range: QueryType

```
</details>