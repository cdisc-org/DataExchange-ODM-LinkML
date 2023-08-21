# Slot: OrganizationOID


_Reference to an Organization elment._



URI: [odm:OrganizationOID](http://www.cdisc.org/ns/odm/v2.0/OrganizationOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: OrganizationOID
description: Reference to an Organization elment.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: OrganizationOID
domain_of:
- User
- Location
range: oidref

```
</details>