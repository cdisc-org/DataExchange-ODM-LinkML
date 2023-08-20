# Slot: AsOfDateTime


_The date/time at which the source database was queried in order to create this document._



URI: [odm:AsOfDateTime](http://www.cdisc.org/ns/odm/v2.0/AsOfDateTime)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents |  yes  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: AsOfDateTime
description: The date/time at which the source database was queried in order to create
  this document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: AsOfDateTime
domain_of:
- ODMFileMetadata
range: datetime

```
</details>