# Slot: StudyEventOID

URI: [odm:StudyEventOID](http://www.cdisc.org/ns/odm/v2.0/StudyEventOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventRef](StudyEventRef.md) |  |  yes  |
[AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) |  |  yes  |
[StudyEventData](StudyEventData.md) |  |  yes  |
[KeySet](KeySet.md) |  |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyEventOID
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