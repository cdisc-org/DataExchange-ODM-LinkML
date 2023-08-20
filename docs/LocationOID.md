# Slot: LocationOID


_Reference to a Location element._



URI: [odm:LocationOID](http://www.cdisc.org/ns/odm/v2.0/LocationOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[User](User.md) | Information about a specific user of a clinical data collection or data manag... |  yes  |
[Organization](Organization.md) | An organization can reference a parent organization |  yes  |
[SiteRef](SiteRef.md) | lement NameSiteRefParent ElementsSubjectDataElement XPath(s)/ODM/ClinicalData... |  yes  |
[LocationRef](LocationRef.md) | A reference to the user's physical location |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: LocationOID
description: Reference to a Location element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: LocationOID
domain_of:
- User
- Organization
- SiteRef
- LocationRef
range: oidref

```
</details>