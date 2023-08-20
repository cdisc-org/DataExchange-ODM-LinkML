# Slot: AddressRef

URI: [odm:AddressRef](http://www.cdisc.org/ns/odm/v2.0/AddressRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |







## Properties

* Range: [Address](Address.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: AddressRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: AddressRef
domain_of:
- User
- Organization
- Location
range: Address

```
</details>