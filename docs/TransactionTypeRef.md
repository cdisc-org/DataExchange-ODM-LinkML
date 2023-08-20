# Slot: TransactionTypeRef


_Identifies the transaction type when /ODM/@FileType is Transactional and there is no child element._



URI: [odm:TransactionTypeRef](http://www.cdisc.org/ns/odm/v2.0/TransactionTypeRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SubjectData](SubjectData.md) | Clinical data for a single subject |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit) |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |
[Annotation](Annotation.md) | A general note about clinical data |  yes  |







## Properties

* Range: [TransactionType](TransactionType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TransactionTypeRef
description: Identifies the transaction type when /ODM/@FileType is Transactional
  and there is no child element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: TransactionTypeRef
domain_of:
- SubjectData
- StudyEventData
- ItemGroupData
- ItemData
- Annotation
range: TransactionType

```
</details>