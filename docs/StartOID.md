# Slot: StartOID


_Reference to the definition of the structural element that starts the workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef element._



URI: [odm:StartOID](http://www.cdisc.org/ns/odm/v2.0/StartOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WorkflowStart](WorkflowStart.md) | WorkflowStart references a structural element that begins the automated workf... |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StartOID
description: Reference to the definition of the structural element that starts the
  workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef
  element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: StartOID
domain_of:
- WorkflowStart
range: oidref

```
</details>