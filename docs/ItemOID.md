# Slot: ItemOID

URI: [odm:ItemOID](http://www.cdisc.org/ns/odm/v2.0/ItemOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SourceItem](SourceItem.md) |  |  yes  |
[RangeCheck](RangeCheck.md) |  |  yes  |
[ItemData](ItemData.md) |  |  yes  |
[KeySet](KeySet.md) |  |  yes  |
[ItemRef](ItemRef.md) |  |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemOID
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ItemOID
domain_of:
- SourceItem
- RangeCheck
- ItemData
- KeySet
- ItemRef
range: oidref

```
</details>