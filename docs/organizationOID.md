# Slot: organizationOID


_Reference to an Organization elment._



URI: [odm:organizationOID](http://www.cdisc.org/ns/odm/v2.0/organizationOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |







## Properties

* Range: [Organization](Organization.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: organizationOID
description: Reference to an Organization elment.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: organizationOID
domain_of:
- User
- Location
range: Organization

```
</details>