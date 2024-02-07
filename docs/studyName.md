# Slot: studyName


_Sponsoring organization's internal name for the study. If no internal name is available, the value is expected to be the same value as ProtocolName._



URI: [odm:studyName](http://www.cdisc.org/ns/odm/v2.0/studyName)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study... |  yes  |







## Properties

* Range: [nameType](nameType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: studyName
description: Sponsoring organization's internal name for the study. If no internal
  name is available, the value is expected to be the same value as ProtocolName.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: studyName
domain_of:
- Study
range: nameType

```
</details>