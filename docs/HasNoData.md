# Slot: HasNoData


_Used to indicate that an ItemGroupDef has no data. May be used at sponsor's discretion or if required by a regulatory authority_



URI: [odm:HasNoData](http://www.cdisc.org/ns/odm/v2.0/HasNoData)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |







## Properties

* Range: [YesOnly](YesOnly.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: HasNoData
description: Used to indicate that an ItemGroupDef has no data. May be used at sponsor's
  discretion or if required by a regulatory authority
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: HasNoData
domain_of:
- ItemGroupDef
- ItemRef
range: YesOnly

```
</details>