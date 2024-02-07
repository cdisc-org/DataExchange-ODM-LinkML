# Slot: leafID


_Reference to the unique ID of the Leaf element that contains the location of a file containing a document._



URI: [odm:leafID](http://www.cdisc.org/ns/odm/v2.0/leafID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DocumentRef](DocumentRef.md) | Links to a leaf element with the location of the document. |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |







## Properties

* Range: [Leaf](Leaf.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: leafID
description: Reference to the unique ID of the Leaf element that contains the location
  of a file containing a document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: leafID
domain_of:
- DocumentRef
- SourceItem
range: Leaf

```
</details>