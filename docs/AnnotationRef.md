# Slot: AnnotationRef

URI: [odm:AnnotationRef](http://www.cdisc.org/ns/odm/v2.0/AnnotationRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects |  yes  |
[SubjectData](SubjectData.md) | Clinical data for a single subject |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit) |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |
[Association](Association.md) | An association permits an annotation to be placed on an ordered pair of entit... |  yes  |







## Properties

* Range: [Annotation](Annotation.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: AnnotationRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: AnnotationRef
domain_of:
- ReferenceData
- ClinicalData
- SubjectData
- StudyEventData
- ItemGroupData
- ItemData
- Association
range: Annotation

```
</details>