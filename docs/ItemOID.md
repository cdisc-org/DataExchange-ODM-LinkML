# Slot: ItemOID


_Reference to the ItemDef ._



URI: [odm:ItemOID](http://www.cdisc.org/ns/odm/v2.0/ItemOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata |  yes  |
[RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemOID
description: Reference to the ItemDef .
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ItemOID
domain_of:
- ItemRef
- SourceItem
- RangeCheck
- ItemData
- KeySet
range: oidref

```
</details>