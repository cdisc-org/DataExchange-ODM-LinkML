# Slot: effectiveDate


_Datetime stamp when this MetaDataVersion was published at this location._



URI: [odm:effectiveDate](http://www.cdisc.org/ns/odm/v2.0/effectiveDate)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetaDataVersionRef](MetaDataVersionRef.md) | A reference to a MetaDataVersion used at the containing Location. The Effecti... |  yes  |







## Properties

* Range: [date](date.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: effectiveDate
description: Datetime stamp when this MetaDataVersion was published at this location.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: effectiveDate
domain_of:
- MetaDataVersionRef
range: date

```
</details>