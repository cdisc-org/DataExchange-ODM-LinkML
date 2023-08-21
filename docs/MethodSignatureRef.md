# Slot: MethodSignatureRef


_MethodSignature reference: A MethodSignature defines the parameters and return values for a method. The MethodSignature improves traceability while enhancing the ability for automation engines to execute a MethodDef's FormalExpression. Most Methods use one or more input parameters and return one or more values._



URI: [odm:MethodSignatureRef](http://www.cdisc.org/ns/odm/v2.0/MethodSignatureRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item. It repr... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |  yes  |







## Properties

* Range: [MethodSignature](MethodSignature.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: MethodSignatureRef
description: 'MethodSignature reference: A MethodSignature defines the parameters
  and return values for a method. The MethodSignature improves traceability while
  enhancing the ability for automation engines to execute a MethodDef''s FormalExpression.
  Most Methods use one or more input parameters and return one or more values.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: MethodSignatureRef
domain_of:
- RangeCheck
- MethodDef
- ConditionDef
range: MethodSignature

```
</details>