# Slot: keySet


_KeySet reference: A KeySet references a single entity (e.g., a study, a subject, a study event). Only those attributes needed to specify the particular entity are required, and all others must be omitted (see Section 2.7, Clinical Data Keys)._



URI: [odm:keySet](http://www.cdisc.org/ns/odm/v2.0/keySet)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Association](Association.md) | An association permits an annotation to be placed on an ordered pair of entit... |  yes  |







## Properties

* Range: [KeySet](KeySet.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: keySet
description: 'KeySet reference: A KeySet references a single entity (e.g., a study,
  a subject, a study event). Only those attributes needed to specify the particular
  entity are required, and all others must be omitted (see Section 2.7, Clinical Data
  Keys).'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: keySet
domain_of:
- Association
range: KeySet

```
</details>