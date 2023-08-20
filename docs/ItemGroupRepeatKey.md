# Slot: ItemGroupRepeatKey


_A key used to distinguish between repeats of the same type of item group._



URI: [odm:ItemGroupRepeatKey](http://www.cdisc.org/ns/odm/v2.0/ItemGroupRepeatKey)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e |  yes  |







## Properties

* Range: [RepeatKey](RepeatKey.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemGroupRepeatKey
description: A key used to distinguish between repeats of the same type of item group.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ItemGroupRepeatKey
domain_of:
- ItemGroupData
- KeySet
range: repeatKey

```
</details>