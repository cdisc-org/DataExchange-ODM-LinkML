# Slot: OrderNumber

URI: [odm:OrderNumber](http://www.cdisc.org/ns/odm/v2.0/OrderNumber)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupRef](StudyEventGroupRef.md) |  |  yes  |
[StudyEventRef](StudyEventRef.md) |  |  yes  |
[Parameter](Parameter.md) |  |  yes  |
[ReturnValue](ReturnValue.md) |  |  yes  |
[StudyEndPointRef](StudyEndPointRef.md) |  |  yes  |
[ItemRef](ItemRef.md) |  |  yes  |
[ItemGroupRef](ItemGroupRef.md) |  |  yes  |
[CodeListItem](CodeListItem.md) |  |  yes  |
[EnumeratedItem](EnumeratedItem.md) |  |  yes  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: OrderNumber
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: OrderNumber
domain_of:
- StudyEventGroupRef
- StudyEventRef
- Parameter
- ReturnValue
- StudyEndPointRef
- ItemRef
- ItemGroupRef
- CodeListItem
- EnumeratedItem
range: integer

```
</details>