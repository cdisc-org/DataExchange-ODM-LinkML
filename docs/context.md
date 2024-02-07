# Slot: context


_Identifies applicable domain or scope of the mapping._



URI: [odm:context](http://www.cdisc.org/ns/odm/v2.0/context)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Alias](Alias.md) | An Alias provides an additional name for an element. The Context attribute sp... |  yes  |
[FormalExpression](FormalExpression.md) | A FormalExpression used within a ConditionDef or a RangeCheck must evaluate t... |  yes  |
[ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents. The ODM element is the top-level (root) eleme... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: context
description: Identifies applicable domain or scope of the mapping.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: context
domain_of:
- Alias
- FormalExpression
- ODMFileMetadata
range: string
any_of:
- range: text
- range: Context

```
</details>