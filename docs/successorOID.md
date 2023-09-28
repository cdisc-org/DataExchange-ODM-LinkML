# Slot: successorOID


_Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs immediately after the RelativeTimepointTarget._



URI: [odm:successorOID](http://www.cdisc.org/ns/odm/v2.0/successorOID)



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
name: successorOID
description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs
  immediately after the RelativeTimepointTarget.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: successorOID
domain_of:
- RelativeTimingConstraint
range: oidref

```
</details>