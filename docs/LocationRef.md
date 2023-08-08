# Slot: LocationRef

URI: [odm:LocationRef](http://www.cdisc.org/ns/odm/v2.0/LocationRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AdminData](AdminData.md) |  |  yes  |







## Properties

* Range: [Location](Location.md)

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AuditRecord](AuditRecord.md) | [LocationRefRef](LocationRefRef.md) | range | [LocationRef](LocationRef.md) |
| [Signature](Signature.md) | [LocationRefRef](LocationRefRef.md) | range | [LocationRef](LocationRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: LocationRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: LocationRef
domain_of:
- AdminData
range: Location

```
</details>