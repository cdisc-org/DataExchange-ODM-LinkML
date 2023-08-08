# Slot: UserOID

URI: [odm:UserOID](http://www.cdisc.org/ns/odm/v2.0/UserOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[InvestigatorRef](InvestigatorRef.md) |  |  yes  |
[UserRef](UserRef.md) |  |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: UserOID
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: UserOID
domain_of:
- InvestigatorRef
- UserRef
range: oidref

```
</details>