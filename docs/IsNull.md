# Slot: IsNull


_Flag specifying that an item's value is to be set to null. In the interest of creating non-verbose XML instances, one should not use ItemData elements with IsNull set to "Yes" to indicate uncollected data. The better practice is to transmit only collected data. For use cases where data traceability is important, providing ItemData elements with IsNull="Yes" maybe be useful. It is not necessary to provide an ItemData element with IsNull set to "Yes" in cases where the source system would not create a record._



URI: [odm:IsNull](http://www.cdisc.org/ns/odm/v2.0/IsNull)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |







## Properties

* Range: [YesOnly](YesOnly.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: IsNull
description: Flag specifying that an item's value is to be set to null. In the interest
  of creating non-verbose XML instances, one should not use ItemData elements with
  IsNull set to "Yes" to indicate uncollected data. The better practice is to transmit
  only collected data. For use cases where data traceability is important, providing
  ItemData elements with IsNull="Yes" maybe be useful. It is not necessary to provide
  an ItemData element with IsNull set to "Yes" in cases where the source system would
  not create a record.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: IsNull
domain_of:
- ItemData
range: YesOnly

```
</details>