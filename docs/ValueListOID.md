# Slot: ValueListOID


_Reference to the unique ID of a ValueListDef element that provides value-level metadata._



URI: [odm:ValueListOID](http://www.cdisc.org/ns/odm/v2.0/ValueListOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ValueListRef](ValueListRef.md) | The ValueListRef element is the OID of the ValueListDef that contains the val... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ValueListOID
description: Reference to the unique ID of a ValueListDef element that provides value-level
  metadata.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ValueListOID
domain_of:
- ValueListRef
range: oidref

```
</details>