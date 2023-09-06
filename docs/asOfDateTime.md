# Slot: asOfDateTime


_The date/time at which the source database was queried in order to create this document._



URI: [odm:asOfDateTime](http://www.cdisc.org/ns/odm/v2.0/asOfDateTime)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents. The ODM element is the top-level (root) eleme... |  yes  |







## Properties

* Range: [datetime](datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: asOfDateTime
description: The date/time at which the source database was queried in order to create
  this document.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: asOfDateTime
domain_of:
- ODMFileMetadata
range: datetime

```
</details>