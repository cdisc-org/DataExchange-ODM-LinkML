# Slot: EndOID


_Reference to the definition of the structural element that ends the workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef element._



URI: [odm:EndOID](http://www.cdisc.org/ns/odm/v2.0/EndOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WorkflowEnd](WorkflowEnd.md) | A WorkflowEnd references a structural element with which the workflows ends |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: EndOID
description: Reference to the definition of the structural element that ends the workflow.
  It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: EndOID
domain_of:
- WorkflowEnd
range: oidref

```
</details>