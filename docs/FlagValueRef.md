# Slot: FlagValueRef


_FlagValue reference: The value of the flag. The meaning of this value is typically dependent on the associated FlagType. The actual value must be a member of the referenced CodeList_



URI: [odm:FlagValueRef](http://www.cdisc.org/ns/odm/v2.0/FlagValueRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Flag](Flag.md) | A machine-processable annotation. |  yes  |







## Properties

* Range: [FlagValue](FlagValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: FlagValueRef
description: 'FlagValue reference: The value of the flag. The meaning of this value
  is typically dependent on the associated FlagType. The actual value must be a member
  of the referenced CodeList'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: FlagValueRef
domain_of:
- Flag
range: FlagValue

```
</details>