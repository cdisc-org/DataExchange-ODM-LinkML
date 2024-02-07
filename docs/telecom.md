# Slot: telecom


_Telecom reference: The telecommunication contacts points of a user, a location, or an organization. The Type attribute designates the type of contact._



URI: [odm:telecom](http://www.cdisc.org/ns/odm/v2.0/telecom)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |







## Properties

* Range: [Telecom](Telecom.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: telecom
description: 'Telecom reference: The telecommunication contacts points of a user,
  a location, or an organization. The Type attribute designates the type of contact.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: telecom
domain_of:
- User
- Organization
- Location
range: Telecom

```
</details>