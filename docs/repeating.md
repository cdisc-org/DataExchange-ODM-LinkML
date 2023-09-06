# Slot: repeating


_The Repeating flag indicates when this type of study event can occur repeatedly within any given subject. When Repeating is "Yes" multiple instances of StudyEventData for this StudyEventDef may be collected for a study subject._



URI: [odm:repeating](http://www.cdisc.org/ns/odm/v2.0/repeating)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: repeating
description: The Repeating flag indicates when this type of study event can occur
  repeatedly within any given subject. When Repeating is "Yes" multiple instances
  of StudyEventData for this StudyEventDef may be collected for a study subject.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: repeating
domain_of:
- StudyEventDef
- ItemGroupDef
range: string
any_of:
- range: YesOrNo
- range: ItemGroupRepeatingType

```
</details>