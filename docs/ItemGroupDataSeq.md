# Slot: ItemGroupDataSeq


_Unique sequence # for each ItemGroupData child element (record) in the container element. The ItemGroupDataSeq attribute doesn’t have any other meaning than the sequence in which the items are saved and exchanged for each ItemGroupDef. It is equivalent to the observation # in a dataset._



URI: [odm:ItemGroupDataSeq](http://www.cdisc.org/ns/odm/v2.0/ItemGroupDataSeq)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |







## Properties

* Range: [positiveInteger](positiveInteger.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemGroupDataSeq
description: 'Unique sequence # for each ItemGroupData child element (record) in the
  container element. The ItemGroupDataSeq attribute doesn’t have any other meaning
  than the sequence in which the items are saved and exchanged for each ItemGroupDef.
  It is equivalent to the observation # in a dataset.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ItemGroupDataSeq
domain_of:
- ItemGroupData
range: positiveInteger

```
</details>