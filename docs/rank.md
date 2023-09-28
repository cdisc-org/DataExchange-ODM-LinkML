# Slot: rank


_Numeric significance of the CodeListItem relative to others in the CodeList. The Rank attribute may be used where the relative value corresponding to an enumeration cannot or should not be determined by its lexical order. For example, if you have a list of enumerated text values including "Low", "Medium", and "High" and wish to assign these relative numeric values 1, 2, and 3 respectively, you should include a Rank attribute for each CodeListItem defined. Without the applied rank attribute, the normal lexical ordering would be "High", "Low", and "Medium"._



URI: [odm:rank](http://www.cdisc.org/ns/odm/v2.0/rank)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |  yes  |







## Properties

* Range: [decimal](decimal.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: rank
description: Numeric significance of the CodeListItem relative to others in the CodeList.
  The Rank attribute may be used where the relative value corresponding to an enumeration
  cannot or should not be determined by its lexical order. For example, if you have
  a list of enumerated text values including "Low", "Medium", and "High" and wish
  to assign these relative numeric values 1, 2, and 3 respectively, you should include
  a Rank attribute for each CodeListItem defined. Without the applied rank attribute,
  the normal lexical ordering would be "High", "Low", and "Medium".
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: rank
domain_of:
- CodeListItem
range: decimal

```
</details>