# Slot: DataTypeRef


_The DataType attribute specifies how the corresponding value_

_                    elements are to be interpreted for comparison and storage._



URI: [odm:DataTypeRef](http://www.cdisc.org/ns/odm/v2.0/DataTypeRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemDef](ItemDef.md) |  |  yes  |
[CodeList](CodeList.md) |  |  yes  |
[Parameter](Parameter.md) |  |  yes  |
[ReturnValue](ReturnValue.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: DataTypeRef
description: "The DataType attribute specifies how the corresponding value\n     \
  \               elements are to be interpreted for comparison and storage."
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: DataTypeRef
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