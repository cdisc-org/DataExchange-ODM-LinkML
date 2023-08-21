# Slot: StudyEventOID


_Reference to the StudyEventDef ._



URI: [odm:StudyEventOID](http://www.cdisc.org/ns/odm/v2.0/StudyEventOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventRef](StudyEventRef.md) | This element references a StudyEventDef as it occurs within a specific versio... |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit). The model supports repeating study e... |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |  yes  |







## Properties

* Range: [oidref](oidref.md)





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