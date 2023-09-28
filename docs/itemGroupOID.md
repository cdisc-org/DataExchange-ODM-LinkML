# Slot: itemGroupOID


_Reference to the ItemGroupDef ._



URI: [odm:itemGroupOID](http://www.cdisc.org/ns/odm/v2.0/itemGroupOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyE... |  yes  |
[SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: itemGroupOID
description: Reference to the ItemGroupDef .
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: itemGroupOID
domain_of:
- ItemGroupRef
- SourceItem
- ItemGroupData
- KeySet
range: oidref

```
</details>