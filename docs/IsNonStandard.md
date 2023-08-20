# Slot: IsNonStandard


_Required for ADaM, SDTM, or SEND if StandardOID is not provided._



URI: [odm:IsNonStandard](http://www.cdisc.org/ns/odm/v2.0/IsNonStandard)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |







## Properties

* Range: [YesOnly](YesOnly.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: IsNonStandard
description: Required for ADaM, SDTM, or SEND if StandardOID is not provided.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: IsNonStandard
domain_of:
- ItemGroupDef
- ItemRef
- CodeList
range: YesOnly

```
</details>