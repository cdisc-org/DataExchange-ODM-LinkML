# Slot: PrefixRef


_Prefix reference: Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhir/datatypes.html#humanname)._



URI: [odm:PrefixRef](http://www.cdisc.org/ns/odm/v2.0/PrefixRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |







## Properties

* Range: [Prefix](Prefix.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: PrefixRef
description: 'Prefix reference: Title or other prefix. Maps to FHIR HumanName.prefix
  (https://www.hl7.org/fhir/datatypes.html#humanname).'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: PrefixRef
domain_of:
- User
range: Prefix

```
</details>