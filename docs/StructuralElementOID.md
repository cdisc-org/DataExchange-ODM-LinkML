# Slot: StructuralElementOID


_OID of a structural element such as a Study, Epoch, StudyEventGroup, StudyEvent, ItemGroup, Item_



URI: [odm:StructuralElementOID](http://www.cdisc.org/ns/odm/v2.0/StructuralElementOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DurationTimingConstraint](DurationTimingConstraint.md) | The DurationTimingConstraint constrains the duration of an activity represent... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StructuralElementOID
description: OID of a structural element such as a Study, Epoch, StudyEventGroup,
  StudyEvent, ItemGroup, Item
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: StructuralElementOID
domain_of:
- DurationTimingConstraint
range: oidref

```
</details>