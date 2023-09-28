# Slot: itemGroupRepeatKey


_A key used to distinguish between repeats of the same type of item group._



URI: [odm:itemGroupRepeatKey](http://www.cdisc.org/ns/odm/v2.0/itemGroupRepeatKey)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |  yes  |







## Properties

* Range: [repeatKey](repeatKey.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: itemGroupRepeatKey
description: A key used to distinguish between repeats of the same type of item group.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: itemGroupRepeatKey
domain_of:
- ItemGroupData
- KeySet
range: repeatKey

```
</details>