# Slot: alias


_Alias reference: An Alias provides an additional name for an element. The Context attribute specifies the application domain in which this additional name is relevant._



URI: [odm:alias](http://www.cdisc.org/ns/odm/v2.0/alias)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |  yes  |
[Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |  yes  |







## Properties

* Range: [Alias](Alias.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: alias
description: 'Alias reference: An Alias provides an additional name for an element.
  The Context attribute specifies the application domain in which this additional
  name is relevant.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: alias
domain_of:
- StudyEventDef
- ItemGroupDef
- ItemDef
- CodeList
- CodeListItem
- MethodDef
- ConditionDef
- Protocol
range: Alias

```
</details>