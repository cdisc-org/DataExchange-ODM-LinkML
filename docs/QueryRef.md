# Slot: QueryRef


_Query reference: The Query element represents a request for clarification on a data item collected for a clinical trial, specifically a request from a sponsor or sponsor’s representative to an investigator to resolve an error or inconsistency discovered during data review. Queries can be created manually by individuals such as site monitors or data managers or automatically by systems. The full text of the Query exists in the Value child element. The optional Name attribute provide the means to provide a short identifier that can be included in listing or user interfaces._



URI: [odm:QueryRef](http://www.cdisc.org/ns/odm/v2.0/QueryRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects. |  yes  |
[SubjectData](SubjectData.md) | Clinical data for a single subject. |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit). The model supports repeating study e... |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |







## Properties

* Range: [Query](Query.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: QueryRef
description: 'Query reference: The Query element represents a request for clarification
  on a data item collected for a clinical trial, specifically a request from a sponsor
  or sponsor’s representative to an investigator to resolve an error or inconsistency
  discovered during data review. Queries can be created manually by individuals such
  as site monitors or data managers or automatically by systems. The full text of
  the Query exists in the Value child element. The optional Name attribute provide
  the means to provide a short identifier that can be included in listing or user
  interfaces.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: QueryRef
domain_of:
- Location
- ClinicalData
- SubjectData
- StudyEventData
- ItemGroupData
- ItemData
range: Query

```
</details>