# Slot: Source

URI: [odm:Source](http://www.cdisc.org/ns/odm/v2.0/Source)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Origin](Origin.md) |  |  yes  |
[Query](Query.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Source
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Source
domain_of:
- Origin
- Query
range: string
any_of:
- range: OriginSource
- range: QuerySourceType

```
</details>