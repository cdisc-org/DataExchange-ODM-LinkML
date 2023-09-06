# Slot: mandatory


_Indicator of whether this StudyEventGroup must appear in the study clinical data for each subject per the study protocol._



URI: [odm:mandatory](http://www.cdisc.org/ns/odm/v2.0/mandatory)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific v... |  yes  |
[StudyEventRef](StudyEventRef.md) | This element references a StudyEventDef as it occurs within a specific versio... |  yes  |
[ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyE... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |







## Properties

* Range: [YesOrNo](YesOrNo.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: mandatory
description: Indicator of whether this StudyEventGroup must appear in the study clinical
  data for each subject per the study protocol.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: mandatory
domain_of:
- StudyEventGroupRef
- StudyEventRef
- ItemGroupRef
- ItemRef
range: YesOrNo

```
</details>