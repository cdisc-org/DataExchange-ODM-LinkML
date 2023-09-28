# Slot: leafID


_Unique identifier for the Leaf element with the document location._



URI: [odm:leafID](http://www.cdisc.org/ns/odm/v2.0/leafID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DocumentRef](DocumentRef.md) | Links to a leaf element with the location of the document. |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |







## Properties

* Range: [oid](oid.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: leafID
description: Unique identifier for the Leaf element with the document location.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: leafID
domain_of:
- DocumentRef
- SourceItem
range: oid

```
</details>