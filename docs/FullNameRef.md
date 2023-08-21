# Slot: FullNameRef


_FullName reference: The user's full formal name. May be a combination of Prefix, GivenName, FamilyName & Suffix. Intended to be used for display._



URI: [odm:FullNameRef](http://www.cdisc.org/ns/odm/v2.0/FullNameRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |







## Properties

* Range: [FullName](FullName.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: FullNameRef
description: 'FullName reference: The user''s full formal name. May be a combination
  of Prefix, GivenName, FamilyName & Suffix. Intended to be used for display.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: FullNameRef
domain_of:
- User
range: FullName

```
</details>