# Slot: ErrorMessageRef


_ErrorMessage reference: Error message provided to user when the range check fails._



URI: [odm:ErrorMessageRef](http://www.cdisc.org/ns/odm/v2.0/ErrorMessageRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item. It repr... |  yes  |







## Properties

* Range: [ErrorMessage](ErrorMessage.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ErrorMessageRef
description: 'ErrorMessage reference: Error message provided to user when the range
  check fails.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ErrorMessageRef
domain_of:
- RangeCheck
range: ErrorMessage

```
</details>