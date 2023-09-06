# Slot: definition


_A free-text definition of the parameter_



URI: [odm:definition](http://www.cdisc.org/ns/odm/v2.0/definition)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[Parameter](Parameter.md) | The Parameter element represents a method parameter used as part of a MethodS... |  yes  |
[ReturnValue](ReturnValue.md) | The ReturnValue element represents a return value used as part of a MethodSig... |  yes  |







## Properties

* Range: [Definition](Definition.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: definition
description: A free-text definition of the parameter
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: definition
domain_of:
- ItemDef
- Parameter
- ReturnValue
range: Definition

```
</details>