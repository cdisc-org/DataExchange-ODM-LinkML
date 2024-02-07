# Slot: role


_The Role for the referenced ItemDef. The Role attribute provides a single role name describing the use of this data item. If the Role is defined by a standard terminology, RoleCodeListOID may be used to reference a CodeList that defines the full set roles from which the Role attribute value is to be taken._



URI: [odm:role](http://www.cdisc.org/ns/odm/v2.0/role)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |







## Properties

* Range: [text](text.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: role
description: The Role for the referenced ItemDef. The Role attribute provides a single
  role name describing the use of this data item. If the Role is defined by a standard
  terminology, RoleCodeListOID may be used to reference a CodeList that defines the
  full set roles from which the Role attribute value is to be taken.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: role
domain_of:
- ItemRef
- Organization
- Location
range: text

```
</details>