# Slot: ID


_Unique identifier for the leaf that is referenced._



URI: [odm:ID](http://www.cdisc.org/ns/odm/v2.0/ID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |  yes  |
[Signature](Signature.md) |  |  yes  |
[Annotation](Annotation.md) |  |  yes  |







## Properties

* Range: [Oid](Oid.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ID
description: Unique identifier for the leaf that is referenced.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ID
domain_of:
- leaf
- Signature
- Annotation
range: oid

```
</details>