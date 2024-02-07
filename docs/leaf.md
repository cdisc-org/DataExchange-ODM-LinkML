# Slot: leaf


_Leaf reference: Contains the XLink information referenced by DocumentRef or ArchiveLocationID_



URI: [odm:leaf](http://www.cdisc.org/ns/odm/v2.0/leaf)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |







## Properties

* Range: [Leaf](Leaf.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: leaf
description: 'Leaf reference: Contains the XLink information referenced by DocumentRef
  or ArchiveLocationID'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: leaf
domain_of:
- MetaDataVersion
- ItemGroupDef
range: Leaf

```
</details>