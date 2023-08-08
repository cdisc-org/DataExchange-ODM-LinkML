# Slot: UserRef

URI: [odm:UserRef](http://www.cdisc.org/ns/odm/v2.0/UserRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AdminData](AdminData.md) |  |  yes  |







## Properties

* Range: [User](User.md)

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AuditRecord](AuditRecord.md) | [UserRefRef](UserRefRef.md) | range | [UserRef](UserRef.md) |
| [Signature](Signature.md) | [UserRefRef](UserRefRef.md) | range | [UserRef](UserRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: UserRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: UserRef
domain_of:
- AdminData
range: User

```
</details>