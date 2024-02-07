# Slot: targetOID


_References the definition of the target structural element for the transition. The structural element may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, ItemDef, or Branching element. The latter will be used when there is a branching definition necessary as a result of the transition._



URI: [odm:targetOID](http://www.cdisc.org/ns/odm/v2.0/targetOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Transition](Transition.md) | A Transition defines a link between 2 structural elements in a workflow. When... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: targetOID
description: References the definition of the target structural element for the transition.
  The structural element may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef,
  ItemDef, or Branching element. The latter will be used when there is a branching
  definition necessary as a result of the transition.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: targetOID
domain_of:
- Transition
range: string
any_of:
- range: StudyEventGroupDef
- range: StudyEventDef
- range: ItemGroupDef
- range: ItemDef
- range: Branching

```
</details>