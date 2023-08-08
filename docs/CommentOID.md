# Slot: CommentOID


_The Comment identifier that this value refers to. Needed when the WhereClause references Items across different domains._

_                The Comment would define any join assumptions._



URI: [odm:CommentOID](http://www.cdisc.org/ns/odm/v2.0/CommentOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WhereClauseDef](WhereClauseDef.md) |  |  yes  |
[StudyEventGroupDef](StudyEventGroupDef.md) |  |  yes  |
[Coding](Coding.md) |  |  yes  |
[MetaDataVersion](MetaDataVersion.md) |  |  yes  |
[StudyEventDef](StudyEventDef.md) |  |  yes  |
[ItemGroupDef](ItemGroupDef.md) |  |  yes  |
[ItemDef](ItemDef.md) |  |  yes  |
[CodeList](CodeList.md) |  |  yes  |
[ConditionDef](ConditionDef.md) |  |  yes  |
[MethodDef](MethodDef.md) |  |  yes  |
[Standard](Standard.md) |  |  yes  |
[CodeListItem](CodeListItem.md) |  |  yes  |
[EnumeratedItem](EnumeratedItem.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: CommentOID
description: "The Comment identifier that this value refers to. Needed when the WhereClause\
  \ references Items across different domains.\n                The Comment would\
  \ define any join assumptions."
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: CommentOID
domain_of:
- WhereClauseDef
- StudyEventGroupDef
- Coding
- MetaDataVersion
- StudyEventDef
- ItemGroupDef
- ItemDef
- CodeList
- ConditionDef
- MethodDef
- Standard
- CodeListItem
- EnumeratedItem
range: string
any_of:
- range: oidref
- range: text

```
</details>