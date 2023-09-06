# Slot: locationOID


_Reference to a Location element._



URI: [odm:locationOID](http://www.cdisc.org/ns/odm/v2.0/locationOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |  yes  |
[SiteRef](SiteRef.md) | Provides a reference to the site that the SubjectData record is associated wi... |  yes  |
[LocationRef](LocationRef.md) | A reference to the user's physical location. |  yes  |







## Properties

* Range: [oidref](oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: locationOID
description: Reference to a Location element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: locationOID
domain_of:
- User
- Organization
- SiteRef
- LocationRef
range: oidref

```
</details>