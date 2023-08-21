# Slot: StudyName


_Sponsoring organization's internal name for the study. If no internal name is available, the value is expected to be the same value as ProtocolName._



URI: [odm:StudyName](http://www.cdisc.org/ns/odm/v2.0/StudyName)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study... |  yes  |







## Properties

* Range: [name](name.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StudyName
description: Sponsoring organization's internal name for the study. If no internal
  name is available, the value is expected to be the same value as ProtocolName.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: StudyName
domain_of:
- Study
range: name

```
</details>