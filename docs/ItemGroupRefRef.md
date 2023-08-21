# Slot: ItemGroupRefRef


_ItemGroupRef reference: ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyEventDef or ItemGroupDef. The list of ItemGroupRefs identifies the types of item groups that are allowed to occur within this type of studyevent or (nested) item group. The ItemGroupRefs within a single StudyEventDef or ItemGroupDef must not have duplicate ItemGroupOID or OrderNumber attribute values._



URI: [odm:ItemGroupRefRef](http://www.cdisc.org/ns/odm/v2.0/ItemGroupRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |







## Properties

* Range: [ItemGroupRef](ItemGroupRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemGroupRefRef
description: 'ItemGroupRef reference: ItemGroupRef references an ItemGroupDef as it
  occurs within a specific StudyEventDef or ItemGroupDef. The list of ItemGroupRefs
  identifies the types of item groups that are allowed to occur within this type of
  studyevent or (nested) item group. The ItemGroupRefs within a single StudyEventDef
  or ItemGroupDef must not have duplicate ItemGroupOID or OrderNumber attribute values.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ItemGroupRefRef
domain_of:
- StudyEventDef
- ItemGroupDef
range: ItemGroupRef

```
</details>