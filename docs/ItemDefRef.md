# Slot: ItemDefRef


_ItemDef reference: An ItemDef describes a type of item that can occur within a study. Item properties include name, datatype, range, or codelist restrictions, and several other properties._



URI: [odm:ItemDefRef](http://www.cdisc.org/ns/odm/v2.0/ItemDefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |







## Properties

* Range: [ItemDef](ItemDef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemDefRef
description: 'ItemDef reference: An ItemDef describes a type of item that can occur
  within a study. Item properties include name, datatype, range, or codelist restrictions,
  and several other properties.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ItemDefRef
domain_of:
- MetaDataVersion
range: ItemDef

```
</details>