# Slot: ReturnValueRef


_ReturnValue reference: The ReturnValue element represents a return value used as part of a MethodSignature in MethodDef, ConditionDef, or RangeCheck. A return value identifies values passed from the Method to the calling element. A ReturnValue may be computed by a FormalExpression._



URI: [odm:ReturnValueRef](http://www.cdisc.org/ns/odm/v2.0/ReturnValueRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MethodSignature](MethodSignature.md) | A MethodSignature defines the parameters and return values for a method. The ... |  yes  |







## Properties

* Range: [ReturnValue](ReturnValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ReturnValueRef
description: 'ReturnValue reference: The ReturnValue element represents a return value
  used as part of a MethodSignature in MethodDef, ConditionDef, or RangeCheck. A return
  value identifies values passed from the Method to the calling element. A ReturnValue
  may be computed by a FormalExpression.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ReturnValueRef
domain_of:
- MethodSignature
range: ReturnValue

```
</details>