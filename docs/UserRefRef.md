# Slot: UserRefRef

URI: [odm:UserRefRef](http://www.cdisc.org/ns/odm/v2.0/UserRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AdminData](AdminData.md) | Administrative information about users, locations, organizations, and electro... |  yes  |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data |  yes  |







## Properties

* Range: [UserRef](UserRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: UserRefRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: UserRefRef
domain_of:
- AdminData
- AuditRecord
- Signature
range: UserRef

```
</details>