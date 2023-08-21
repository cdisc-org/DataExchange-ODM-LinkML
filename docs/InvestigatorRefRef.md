# Slot: InvestigatorRefRef


_InvestigatorRef reference: Provides a reference to the user who created the SubjectData record in the source system._



URI: [odm:InvestigatorRefRef](http://www.cdisc.org/ns/odm/v2.0/InvestigatorRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SubjectData](SubjectData.md) | Clinical data for a single subject. |  yes  |







## Properties

* Range: [InvestigatorRef](InvestigatorRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: InvestigatorRefRef
description: 'InvestigatorRef reference: Provides a reference to the user who created
  the SubjectData record in the source system.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: InvestigatorRefRef
domain_of:
- SubjectData
range: InvestigatorRef

```
</details>