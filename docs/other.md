# Slot: other


_Flag to indicate that the Item represents "other" content added to an ItemGroup._



URI: [odm:other](http://www.cdisc.org/ns/odm/v2.0/other)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |  yes  |







## Properties

* Range: [YesOnly](YesOnly.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: other
description: Flag to indicate that the Item represents "other" content added to an
  ItemGroup.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: other
domain_of:
- ItemRef
- CodeListItem
range: YesOnly

```
</details>