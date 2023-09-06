# Slot: sourceOID


_References the definition of the source structural element for the transition. The structural element may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, ItemDef, or Branching element._



URI: [odm:sourceOID](http://www.cdisc.org/ns/odm/v2.0/sourceOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Transition](Transition.md) | A Transition defines a link between 2 structural elements in a workflow. When... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: sourceOID
description: References the definition of the source structural element for the transition.
  The structural element may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef,
  ItemDef, or Branching element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: sourceOID
domain_of:
- Transition
range: oidref

```
</details>