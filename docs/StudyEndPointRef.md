# Slot: StudyEndPointRef

URI: [odm:StudyEndPointRef](http://www.cdisc.org/ns/odm/v2.0/StudyEndPointRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEndPoints](StudyEndPoints.md) |  |  yes  |







## Properties

* Range: [StudyEndPoint](StudyEndPoint.md)

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyObjective](StudyObjective.md) | [StudyEndPointRefRef](StudyEndPointRefRef.md) | range | [StudyEndPointRef](StudyEndPointRef.md) |
| [StudyEstimand](StudyEstimand.md) | [StudyEndPointRefRef](StudyEndPointRefRef.md) | range | [StudyEndPointRef](StudyEndPointRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyEndPointRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: StudyEndPointRef
domain_of:
- StudyEndPoints
range: StudyEndPoint

```
</details>