# Slot: ValueListDefRef


_ValueListDef reference: The following table specifies the XML structure for valuelist metadata. The ValueListDef element contains ItemRef elements that reference ItemDef elements that provide the value-level metadata details_



URI: [odm:ValueListDefRef](http://www.cdisc.org/ns/odm/v2.0/ValueListDefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |







## Properties

* Range: [ValueListDef](ValueListDef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ValueListDefRef
description: 'ValueListDef reference: The following table specifies the XML structure
  for valuelist metadata. The ValueListDef element contains ItemRef elements that
  reference ItemDef elements that provide the value-level metadata details'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ValueListDefRef
domain_of:
- MetaDataVersion
range: ValueListDef

```
</details>