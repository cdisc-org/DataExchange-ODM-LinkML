# Slot: softHard


_Type of range check. Soft indicates that a warning occurs when the RangeCheck fails. Hard indicates that an error occurs when the RangeCheck fails._



URI: [odm:softHard](http://www.cdisc.org/ns/odm/v2.0/softHard)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item. It repr... |  yes  |







## Properties

* Range: [SoftOrHard](SoftOrHard.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: softHard
description: Type of range check. Soft indicates that a warning occurs when the RangeCheck
  fails. Hard indicates that an error occurs when the RangeCheck fails.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: softHard
domain_of:
- RangeCheck
range: SoftOrHard

```
</details>