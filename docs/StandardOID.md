# Slot: StandardOID


_Reference to a Standard element._



URI: [odm:StandardOID](http://www.cdisc.org/ns/odm/v2.0/StandardOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StandardOID
description: Reference to a Standard element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: StandardOID
domain_of:
- ItemGroupDef
- CodeList
range: oidref

```
</details>