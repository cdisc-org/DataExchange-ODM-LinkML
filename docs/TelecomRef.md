# Slot: TelecomRef

URI: [odm:TelecomRef](http://www.cdisc.org/ns/odm/v2.0/TelecomRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization |  yes  |
[Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |  yes  |







## Properties

* Range: [Telecom](Telecom.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TelecomRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: TelecomRef
domain_of:
- User
- Organization
- Location
range: Telecom

```
</details>