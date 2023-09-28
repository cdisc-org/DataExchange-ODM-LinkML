# Slot: domain


_Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup data. The domain applies to the object itself rather then providing a mapping to a different object._



URI: [odm:domain](http://www.cdisc.org/ns/odm/v2.0/domain)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |







## Properties

* Range: [text](text.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: domain
description: Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup data.
  The domain applies to the object itself rather then providing a mapping to a different
  object.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: domain
domain_of:
- ItemGroupDef
range: text

```
</details>