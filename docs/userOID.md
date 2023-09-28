# Slot: userOID


_Reference to a User definition._



URI: [odm:userOID](http://www.cdisc.org/ns/odm/v2.0/userOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[InvestigatorRef](InvestigatorRef.md) | Provides a reference to the user who created the SubjectData record in the so... |  yes  |
[UserRef](UserRef.md) | A reference to information about a specific user of a clinical data collectio... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: userOID
description: Reference to a User definition.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: userOID
domain_of:
- InvestigatorRef
- UserRef
range: oidref

```
</details>