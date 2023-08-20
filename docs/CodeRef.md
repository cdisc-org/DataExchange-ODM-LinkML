# Slot: CodeRef


_A string pattern that identifies a concept as defined by the code system._



URI: [odm:CodeRef](http://www.cdisc.org/ns/odm/v2.0/CodeRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FormalExpression](FormalExpression.md) | A FormalExpression used within a ConditionDef or a RangeCheck must evaluate t... |  yes  |
[Coding](Coding.md) | Coding references a symbol from a defined code system |  yes  |







## Properties

* Range: [Code](Code.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: CodeRef
description: A string pattern that identifies a concept as defined by the code system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: CodeRef
domain_of:
- FormalExpression
- Coding
range: Code

```
</details>