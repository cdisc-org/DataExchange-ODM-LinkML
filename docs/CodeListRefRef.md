# Slot: CodeListRefRef


_CodeListRef reference: A reference to a CodeList definition._



URI: [odm:CodeListRefRef](http://www.cdisc.org/ns/odm/v2.0/CodeListRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |







## Properties

* Range: [CodeListRef](CodeListRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: CodeListRefRef
description: 'CodeListRef reference: A reference to a CodeList definition.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: CodeListRefRef
domain_of:
- MetaDataVersion
- ItemDef
range: CodeListRef

```
</details>