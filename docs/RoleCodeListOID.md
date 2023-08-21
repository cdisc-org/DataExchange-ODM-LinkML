# Slot: RoleCodeListOID


_Reference to a CodeList that defines the allowable values of Role for the Study._



URI: [odm:RoleCodeListOID](http://www.cdisc.org/ns/odm/v2.0/RoleCodeListOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: RoleCodeListOID
description: Reference to a CodeList that defines the allowable values of Role for
  the Study.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: RoleCodeListOID
domain_of:
- ItemRef
range: oidref

```
</details>