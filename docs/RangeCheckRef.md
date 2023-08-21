# Slot: RangeCheckRef


_RangeCheck reference: A RangeCheck defines a constraint on the value of the enclosing item. It represents an expression that evaluates to True when the ItemData value is valid or False when the ItemData value is invalid. The expression is specified using either Comparator and CheckValue or using FormalExpressions._



URI: [odm:RangeCheckRef](http://www.cdisc.org/ns/odm/v2.0/RangeCheckRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClauseDef](WhereClauseDef.md) | The WhereClauseDef element specifies a condition. |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |







## Properties

* Range: [RangeCheck](RangeCheck.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: RangeCheckRef
description: 'RangeCheck reference: A RangeCheck defines a constraint on the value
  of the enclosing item. It represents an expression that evaluates to True when the
  ItemData value is valid or False when the ItemData value is invalid. The expression
  is specified using either Comparator and CheckValue or using FormalExpressions.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: RangeCheckRef
domain_of:
- WhereClauseDef
- ItemDef
range: RangeCheck

```
</details>