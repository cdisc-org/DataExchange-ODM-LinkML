# Slot: SourceOID


_References the definition of the source structural element for the transition. The structural element may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, ItemDef, or Branching element._



URI: [odm:SourceOID](http://www.cdisc.org/ns/odm/v2.0/SourceOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Transition](Transition.md) | A Transition defines a link between 2 structural elements in a workflow |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: SourceOID
description: References the definition of the source structural element for the transition.
  The structural element may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef,
  ItemDef, or Branching element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: SourceOID
domain_of:
- Transition
range: oidref

```
</details>