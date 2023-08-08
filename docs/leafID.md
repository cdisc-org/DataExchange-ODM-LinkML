# Slot: leafID


_Unique identifier for the leaf element with the document location._



URI: [odm:leafID](http://www.cdisc.org/ns/odm/v2.0/leafID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SourceItem](SourceItem.md) |  |  yes  |
[DocumentRef](DocumentRef.md) | Links to a leaf element with the location of the document |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: leafID
description: Unique identifier for the leaf element with the document location.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: leafID
domain_of:
- SourceItem
- DocumentRef
range: string
any_of:
- range: oid
- range: oidref

```
</details>