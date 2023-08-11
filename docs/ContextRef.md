# Slot: ContextRef

URI: [odm:ContextRef](http://www.cdisc.org/ns/odm/v2.0/ContextRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Alias](Alias.md) |  |  yes  |
[FormalExpression](FormalExpression.md) |  |  yes  |
[ODMFileMetadata](ODMFileMetadata.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ContextRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ContextRef
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