# Slot: Status


_Status of Standard._



URI: [odm:Status](http://www.cdisc.org/ns/odm/v2.0/Status)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study... |  yes  |
[Standard](Standard.md) | The Standard element describes each standard used within the MetaDataVersion ... |  yes  |







## Properties

* Range: [string](string.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Status
description: Status of Standard.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Status
domain_of:
- Study
- Standard
range: string
any_of:
- range: name
- range: StandardStatus

```
</details>