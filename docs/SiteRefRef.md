# Slot: SiteRefRef


_SiteRef reference: lement NameSiteRefParent ElementsSubjectDataElement XPath(s)/ODM/ClinicalData/SubjectData/SiteRefElement Textual ValueNoneAttributesLocationOIDChild ElementsNoneUsage/Business RulesBusiness Rule(s):Must be provided when the /ODM/FileType is Transactional._



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
description: 'SiteRef reference: lement NameSiteRefParent ElementsSubjectDataElement
  XPath(s)/ODM/ClinicalData/SubjectData/SiteRefElement Textual ValueNoneAttributesLocationOIDChild
  ElementsNoneUsage/Business RulesBusiness Rule(s):Must be provided when the /ODM/FileType
  is Transactional.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: SiteRefRef
domain_of:
- SubjectData
range: SiteRef

```
</details>