# Slot: LocationRefRef

URI: [odm:LocationRefRef](http://www.cdisc.org/ns/odm/v2.0/LocationRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AdminData](AdminData.md) | Administrative information about users, locations, organizations, and electro... |  yes  |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data |  yes  |







## Properties

* Range: [LocationRef](LocationRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: LocationRefRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: LocationRefRef
domain_of:
- AdminData
- AuditRecord
- Signature
range: LocationRef

```
</details>