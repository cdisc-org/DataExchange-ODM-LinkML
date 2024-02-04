# Slot: metaDataVersion


_MetaDataVersion reference: The metadata for a study is defined in a series of MetaDataVersion elements. Through this mechanism (multiple MetaDataVersion elements), the model supports the incremental deployment of "mid-stream study changes," and thus can handle a situation where multiple versions of the metadata are being used simultaneously (e.g., due to delays in IRB approval at various sites)._



URI: [odm:metaDataVersion](http://www.cdisc.org/ns/odm/v2.0/metaDataVersion)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study... |  yes  |







## Properties

* Range: [MetaDataVersion](MetaDataVersion.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: metaDataVersion
description: 'MetaDataVersion reference: The metadata for a study is defined in a
  series of MetaDataVersion elements. Through this mechanism (multiple MetaDataVersion
  elements), the model supports the incremental deployment of "mid-stream study changes,"
  and thus can handle a situation where multiple versions of the metadata are being
  used simultaneously (e.g., due to delays in IRB approval at various sites).'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: metaDataVersion
domain_of:
- Study
range: MetaDataVersion

```
</details>