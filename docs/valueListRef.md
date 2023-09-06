# Slot: valueListRef


_ValueListRef reference: The ValueListRef element is the OID of the ValueListDef that contains the valuelist definition associated with the variable. If value-level metadata is required for a variable, a ValueListRef element should be provided as a child element on the ItemDef for the variable definition._



URI: [odm:valueListRef](http://www.cdisc.org/ns/odm/v2.0/valueListRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |







## Properties

* Range: [ValueListRef](ValueListRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: valueListRef
description: 'ValueListRef reference: The ValueListRef element is the OID of the ValueListDef
  that contains the valuelist definition associated with the variable. If value-level
  metadata is required for a variable, a ValueListRef element should be provided as
  a child element on the ItemDef for the variable definition.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: valueListRef
domain_of:
- ItemDef
range: ValueListRef

```
</details>