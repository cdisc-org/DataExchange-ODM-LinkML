# Slot: userRef


_UserRef reference: A reference to information about a specific user of a clinical data collection or data management system._



URI: [odm:userRef](http://www.cdisc.org/ns/odm/v2.0/userRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data. This indica... |  yes  |







## Properties

* Range: [UserRef](UserRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: userRef
description: 'UserRef reference: A reference to information about a specific user
  of a clinical data collection or data management system.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: userRef
domain_of:
- AuditRecord
- Signature
range: UserRef

```
</details>