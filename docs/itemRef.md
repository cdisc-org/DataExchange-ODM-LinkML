# Slot: itemRef


_ItemRef reference: A reference to an ItemDef as it occurs within a specific ItemGroupDef. The list of ItemRefs identifies the types of items that are allowed to occur within this type of item group._



URI: [odm:itemRef](http://www.cdisc.org/ns/odm/v2.0/itemRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ValueListDef](ValueListDef.md) | The following table specifies the XML structure for valuelist metadata. The V... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |







## Properties

* Range: [ItemRef](ItemRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: itemRef
description: 'ItemRef reference: A reference to an ItemDef as it occurs within a specific
  ItemGroupDef. The list of ItemRefs identifies the types of items that are allowed
  to occur within this type of item group.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: itemRef
domain_of:
- ValueListDef
- ItemGroupDef
range: ItemRef

```
</details>