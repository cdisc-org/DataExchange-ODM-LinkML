# Slot: origin


_Origin reference: Origin defines the source metadata, where applicable, for ODM ItemRefs or ItemGroupRefs. Origin as a child element replaces the Origin attribute in ODM v1.3 that exists for the ItemDef and ItemGroupDef elements.The Origin element is based on the def:Origin element in Define-XML v2.1 with the Trace-XML v1.0 extension._



URI: [odm:origin](http://www.cdisc.org/ns/odm/v2.0/origin)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |







## Properties

* Range: [Origin](Origin.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: origin
description: 'Origin reference: Origin defines the source metadata, where applicable,
  for ODM ItemRefs or ItemGroupRefs. Origin as a child element replaces the Origin
  attribute in ODM v1.3 that exists for the ItemDef and ItemGroupDef elements.The
  Origin element is based on the def:Origin element in Define-XML v2.1 with the Trace-XML
  v1.0 extension.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: origin
domain_of:
- ItemGroupDef
- ItemRef
range: Origin

```
</details>