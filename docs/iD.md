# Slot: iD


_Unique identifier for the leaf that is referenced._



URI: [odm:iD](http://www.cdisc.org/ns/odm/v2.0/iD)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data. This indica... |  yes  |
[Annotation](Annotation.md) | A general note about clinical data. If an annotation has both a comment and f... |  yes  |







## Properties

* Range: [oid](oid.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: iD
description: Unique identifier for the leaf that is referenced.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: true
alias: iD
domain_of:
- Leaf
- Signature
- Annotation
range: oid
required: true

```
</details>