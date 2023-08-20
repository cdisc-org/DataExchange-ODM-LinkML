# Slot: Other


_Flag to indicate that the Item represents "other" content added to an ItemGroup._



URI: [odm:Other](http://www.cdisc.org/ns/odm/v2.0/Other)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist |  yes  |







## Properties

* Range: [YesOnly](YesOnly.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Other
description: Flag to indicate that the Item represents "other" content added to an
  ItemGroup.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Other
domain_of:
- ItemRef
- CodeListItem
range: YesOnly

```
</details>