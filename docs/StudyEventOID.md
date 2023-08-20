# Slot: StudyEventOID


_Reference to the StudyEventDef ._



URI: [odm:StudyEventOID](http://www.cdisc.org/ns/odm/v2.0/StudyEventOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventRef](StudyEventRef.md) | This element references a StudyEventDef as it occurs within a specific versio... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit) |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyEventOID
description: Reference to the StudyEventDef .
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: StudyEventOID
domain_of:
- StudyEventRef
- AbsoluteTimingConstraint
- StudyEventData
- KeySet
range: oidref

```
</details>