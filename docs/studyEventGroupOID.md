# Slot: studyEventGroupOID


_Reference to the StudyEventGroupDef ._



URI: [odm:studyEventGroupOID](http://www.cdisc.org/ns/odm/v2.0/studyEventGroupOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific v... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: studyEventGroupOID
description: Reference to the StudyEventGroupDef .
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: studyEventGroupOID
domain_of:
- StudyEventGroupRef
- AbsoluteTimingConstraint
range: oidref

```
</details>