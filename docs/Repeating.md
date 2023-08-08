# Slot: Repeating

URI: [odm:Repeating](http://www.cdisc.org/ns/odm/v2.0/Repeating)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventDef](StudyEventDef.md) |  |  yes  |
[ItemGroupDef](ItemGroupDef.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Repeating
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Repeating
domain_of:
- StudyEventDef
- ItemGroupDef
range: string
any_of:
- range: YesOrNo
- range: ItemGroupRepeatingType

```
</details>