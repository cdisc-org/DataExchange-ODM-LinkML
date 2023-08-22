# Slot: SiteRefRef


_SiteRef reference: Provides a reference to the site that the SubjectData record is associated with in the source system._



URI: [odm:SiteRefRef](http://www.cdisc.org/ns/odm/v2.0/SiteRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SubjectData](SubjectData.md) | Clinical data for a single subject. |  yes  |







## Properties

* Range: [SiteRef](SiteRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: SiteRefRef
description: 'SiteRef reference: Provides a reference to the site that the SubjectData
  record is associated with in the source system.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: SiteRefRef
domain_of:
- SubjectData
range: SiteRef

```
</details>