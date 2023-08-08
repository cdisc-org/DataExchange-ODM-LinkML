# Slot: MetaDataVersionRef

URI: [odm:MetaDataVersionRef](http://www.cdisc.org/ns/odm/v2.0/MetaDataVersionRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) |  |  yes  |







## Properties

* Range: [MetaDataVersion](MetaDataVersion.md)

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Location](Location.md) | [MetaDataVersionRefRef](MetaDataVersionRefRef.md) | range | [MetaDataVersionRef](MetaDataVersionRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: MetaDataVersionRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
list_elements_unique: true
alias: MetaDataVersionRef
domain_of:
- Study
range: MetaDataVersion

```
</details>