# Slot: endOID


_Reference to the definition of the structural element that ends the workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef element._



URI: [odm:endOID](http://www.cdisc.org/ns/odm/v2.0/endOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WorkflowEnd](WorkflowEnd.md) | A WorkflowEnd references a structural element with which the workflows ends. |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: endOID
description: Reference to the definition of the structural element that ends the workflow.
  It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: endOID
domain_of:
- WorkflowEnd
range: oidref

```
</details>