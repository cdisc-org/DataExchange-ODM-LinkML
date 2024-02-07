# Slot: predecessorOID


_Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that occurs immediately before the RelativeTimepointTarget._



URI: [odm:predecessorOID](http://www.cdisc.org/ns/odm/v2.0/predecessorOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: predecessorOID
description: Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that occurs
  immediately before the RelativeTimepointTarget.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: predecessorOID
domain_of:
- RelativeTimingConstraint
range: string
any_of:
- range: StudyEventGroupDef
- range: StudyEventDef
- range: ItemGroupDef
- range: ItemDef

```
</details>