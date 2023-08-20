# Slot: VersionName


_Short descriptive label for the version of the study, e.g. "Initial go live" when VersionID = "<study version ID for Initial go live>". VersionName may be provided when a VersionID is provided._



URI: [odm:VersionName](http://www.cdisc.org/ns/odm/v2.0/VersionName)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | This element collects static structural information about an individual study |  yes  |







## Properties

* Range: [Name](Name.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: VersionName
description: Short descriptive label for the version of the study, e.g. "Initial go
  live" when VersionID = "<study version ID for Initial go live>". VersionName may
  be provided when a VersionID is provided.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: VersionName
domain_of:
- Study
range: name

```
</details>