# Slot: startOID


_Reference to the definition of the structural element that starts the workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef element._



URI: [odm:startOID](http://www.cdisc.org/ns/odm/v2.0/startOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WorkflowStart](WorkflowStart.md) | WorkflowStart references a structural element that begins the automated workf... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: startOID
description: Reference to the definition of the structural element that starts the
  workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef
  element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: startOID
domain_of:
- WorkflowStart
range: string
any_of:
- range: StudyEventGroupDef
- range: StudyEventDef
- range: ItemGroupDef
- range: ItemDef

```
</details>