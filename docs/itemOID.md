# Slot: itemOID


_Reference to the ItemDef ._



URI: [odm:itemOID](http://www.cdisc.org/ns/odm/v2.0/itemOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |
[RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item. It repr... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: itemOID
description: Reference to the ItemDef .
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: itemOID
domain_of:
- ItemRef
- SourceItem
- RangeCheck
- ItemData
- KeySet
range: oidref

```
</details>