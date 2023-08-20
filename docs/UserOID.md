# Slot: UserOID


_Reference to a User definition._



URI: [odm:UserOID](http://www.cdisc.org/ns/odm/v2.0/UserOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[InvestigatorRef](InvestigatorRef.md) | Provides a reference to the user who created the SubjectData record in the so... |  yes  |
[UserRef](UserRef.md) | Element NameUserRefParent ElementsAuditRecord, SignatureElement XPath(s)/ODM/... |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: UserOID
description: Reference to a User definition.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: UserOID
domain_of:
- InvestigatorRef
- UserRef
range: oidref

```
</details>