# Slot: leafID


_References a leaf element that provides a reference to another ODM document. This is necessary when the source ItemOID references an ItemDef contained in a different ODM document._



URI: [odm:leafID](http://www.cdisc.org/ns/odm/v2.0/leafID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata |  yes  |







## Properties

* Range: [Oidref](Oidref.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: leafID
description: References a leaf element that provides a reference to another ODM document.
  This is necessary when the source ItemOID references an ItemDef contained in a different
  ODM document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: true
alias: leafID
domain_of:
- SourceItem
range: oidref
required: true

```
</details>