# Slot: MetaDataVersionRefRef

URI: [odm:MetaDataVersionRefRef](http://www.cdisc.org/ns/odm/v2.0/MetaDataVersionRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |







## Properties

* Range: [MetaDataVersionRef](MetaDataVersionRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: MetaDataVersionRefRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: MetaDataVersionRefRef
domain_of:
- Study
- Location
range: MetaDataVersionRef

```
</details>