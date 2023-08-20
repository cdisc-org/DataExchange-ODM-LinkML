# Slot: Source


_I ndicates the party responsible for the data's origin type._



URI: [odm:Source](http://www.cdisc.org/ns/odm/v2.0/Source)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |  yes  |
[Query](Query.md) | The Query element represents a request for clarification on a data item colle... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Source
description: I ndicates the party responsible for the data's origin type.
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