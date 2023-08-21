# Slot: CodeListOID


_Reference to the CodeList definition that provides the allowable values for ItemData that references the ItemDef._



URI: [odm:CodeListOID](http://www.cdisc.org/ns/odm/v2.0/CodeListOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[CodeListRef](CodeListRef.md) | A reference to a CodeList definition. |  yes  |
[FlagValue](FlagValue.md) | The value of the flag. The meaning of this value is typically dependent on th... |  yes  |
[FlagType](FlagType.md) | The type of flag. This determines the purpose and semantics of the flag. |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: CodeListOID
description: Reference to the CodeList definition that provides the allowable values
  for ItemData that references the ItemDef.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: CodeListOID
domain_of:
- CodeListRef
- FlagValue
- FlagType
range: oidref

```
</details>