# Slot: MetaDataVersionOID

URI: [odm:MetaDataVersionOID](http://www.cdisc.org/ns/odm/v2.0/MetaDataVersionOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Include](Include.md) |  |  yes  |
[SourceItem](SourceItem.md) |  |  yes  |
[MetaDataVersionRef](MetaDataVersionRef.md) |  |  yes  |
[ReferenceData](ReferenceData.md) |  |  yes  |
[ClinicalData](ClinicalData.md) |  |  yes  |
[Association](Association.md) |  |  yes  |
[KeySet](KeySet.md) |  |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: MetaDataVersionOID
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: MetaDataVersionOID
domain_of:
- Include
- SourceItem
- MetaDataVersionRef
- ReferenceData
- ClinicalData
- Association
- KeySet
range: oidref

```
</details>