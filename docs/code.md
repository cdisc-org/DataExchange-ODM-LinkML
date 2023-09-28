# Slot: code


_A string pattern that identifies a concept as defined by the code system._



URI: [odm:code](http://www.cdisc.org/ns/odm/v2.0/code)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FormalExpression](FormalExpression.md) | A FormalExpression used within a ConditionDef or a RangeCheck must evaluate t... |  yes  |
[Coding](Coding.md) | Coding references a symbol from a defined code system. It uses a code defined... |  yes  |







## Properties

* Range: [Code](Code.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: code
description: A string pattern that identifies a concept as defined by the code system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: code
domain_of:
- FormalExpression
- Coding
range: Code

```
</details>