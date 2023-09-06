# Slot: partOfOrganizationOID


_Reference to a parent organization._



URI: [odm:partOfOrganizationOID](http://www.cdisc.org/ns/odm/v2.0/partOfOrganizationOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: partOfOrganizationOID
description: Reference to a parent organization.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: partOfOrganizationOID
domain_of:
- Organization
range: oidref

```
</details>