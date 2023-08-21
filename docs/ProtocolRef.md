# Slot: ProtocolRef


_Protocol reference: The Protocol element lists the kinds of study events that can occur within a specific version of a study. All clinical data must occur within one of these study events._



URI: [odm:ProtocolRef](http://www.cdisc.org/ns/odm/v2.0/ProtocolRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |  yes  |







## Properties

* Range: [Protocol](Protocol.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ProtocolRef
description: 'Protocol reference: The Protocol element lists the kinds of study events
  that can occur within a specific version of a study. All clinical data must occur
  within one of these study events.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ProtocolRef
domain_of:
- MetaDataVersion
range: Protocol

```
</details>