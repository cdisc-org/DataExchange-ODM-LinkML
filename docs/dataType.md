# Slot: dataType


_The DataType attribute specifies how the corresponding value_

_                    elements are to be interpreted for comparison and storage._



URI: [odm:dataType](http://www.cdisc.org/ns/odm/v2.0/dataType)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[Parameter](Parameter.md) | The Parameter element represents a method parameter used as part of a MethodS... |  yes  |
[ReturnValue](ReturnValue.md) | The ReturnValue element represents a return value used as part of a MethodSig... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: dataType
description: "The DataType attribute specifies how the corresponding value\n     \
  \               elements are to be interpreted for comparison and storage."
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: dataType
domain_of:
- ItemDef
- CodeList
- Parameter
- ReturnValue
range: string
any_of:
- range: DataType
- range: CLDataType

```
</details>