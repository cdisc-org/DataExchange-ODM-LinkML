# Slot: PredecessorOID


_Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that occurs immediately before the RelativeTimepointTarget._



URI: [odm:PredecessorOID](http://www.cdisc.org/ns/odm/v2.0/PredecessorOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: PredecessorOID
description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that occurs
  immediately before the RelativeTimepointTarget.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: PredecessorOID
domain_of:
- RelativeTimingConstraint
range: oidref

```
</details>