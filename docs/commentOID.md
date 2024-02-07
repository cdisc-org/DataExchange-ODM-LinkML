# Slot: commentOID


_The Comment identifier that this value refers to. Needed when the WhereClause references Items across different domains._

_                The Comment would define any join assumptions._



URI: [odm:commentOID](http://www.cdisc.org/ns/odm/v2.0/commentOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |
[Standard](Standard.md) | The Standard element describes each standard used within the MetaDataVersion ... |  yes  |
[WhereClauseDef](WhereClauseDef.md) | The WhereClauseDef element specifies a condition. |  yes  |
[StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |  yes  |
[StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |  yes  |
[ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |
[CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |  yes  |
[Coding](Coding.md) | Coding references a symbol from a defined code system. It uses a code defined... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: commentOID
description: "The Comment identifier that this value refers to. Needed when the WhereClause\
  \ references Items across different domains.\n                The Comment would\
  \ define any join assumptions."
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: commentOID
domain_of:
- MetaDataVersion
- Standard
- WhereClauseDef
- StudyEventGroupDef
- StudyEventDef
- ItemGroupDef
- ItemDef
- CodeList
- CodeListItem
- MethodDef
- ConditionDef
- Coding
range: string
any_of:
- range: text
- range: CommentDef

```
</details>