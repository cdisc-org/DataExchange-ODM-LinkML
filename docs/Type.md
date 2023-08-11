# Slot: Type


_Type of page for page references indicated in the PageRefs attribute._



URI: [odm:Type](http://www.cdisc.org/ns/odm/v2.0/Type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PDFPageRef](PDFPageRef.md) | This element is the container for CRF page references |  yes  |
[Standard](Standard.md) |  |  yes  |
[StudyEventDef](StudyEventDef.md) |  |  yes  |
[ItemGroupDef](ItemGroupDef.md) |  |  yes  |
[Origin](Origin.md) |  |  yes  |
[Resource](Resource.md) |  |  yes  |
[MethodDef](MethodDef.md) |  |  yes  |
[StudyObjective](StudyObjective.md) |  |  yes  |
[StudyEndPoint](StudyEndPoint.md) |  |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) |  |  yes  |
[RelativeTimingConstraint](RelativeTimingConstraint.md) |  |  yes  |
[Branching](Branching.md) |  |  yes  |
[Organization](Organization.md) |  |  yes  |
[Query](Query.md) |  |  yes  |







## Properties

* Range: [String](String.md)





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
- PDFPageRef
- Standard
- StudyEventDef
- ItemGroupDef
- Origin
- Resource
- MethodDef
- StudyObjective
- StudyEndPoint
- TransitionTimingConstraint
- RelativeTimingConstraint
- Branching
- Organization
- Query
range: string
any_of:
- range: StandardType
- range: PDFPageType
- range: EventType
- range: ItemGroupTypeType
- range: OriginType
- range: text
- range: MethodType
- range: StudyObjectiveLevel
- range: StudyEndPointType
- range: RelativeTimingConstraintType
- range: BranchingType
- range: OrganizationType
- range: QueryType

```
</details>