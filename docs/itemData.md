# Slot: itemData


_ItemData reference: The ItemData element is used for transmission of the clinical data for an item. The model does not support repeating items within a single item group._



URI: [odm:itemData](http://www.cdisc.org/ns/odm/v2.0/itemData)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |







## Properties

* Range: [ItemData](ItemData.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: itemData
description: 'ItemData reference: The ItemData element is used for transmission of
  the clinical data for an item. The model does not support repeating items within
  a single item group.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: itemData
domain_of:
- ItemGroupData
range: ItemData

```
</details>