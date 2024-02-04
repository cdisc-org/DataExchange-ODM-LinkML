# Slot: organization


_Organization reference: An organization can reference a parent organization. Users may be associated with an Organization. An Organization may be associated with a Location. A User, Location, or Organization may have an address._



URI: [odm:organization](http://www.cdisc.org/ns/odm/v2.0/organization)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AdminData](AdminData.md) | Administrative information about users, locations, organizations, and electro... |  yes  |







## Properties

* Range: [Organization](Organization.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: organization
description: 'Organization reference: An organization can reference a parent organization.
  Users may be associated with an Organization. An Organization may be associated
  with a Location. A User, Location, or Organization may have an address.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: organization
domain_of:
- AdminData
range: Organization

```
</details>