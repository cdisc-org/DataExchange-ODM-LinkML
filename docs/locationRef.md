# Slot: locationRef


_LocationRef reference: A reference to the user's physical location._



URI: [odm:locationRef](http://www.cdisc.org/ns/odm/v2.0/locationRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data. This indica... |  yes  |







## Properties

* Range: [LocationRef](LocationRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: locationRef
description: 'LocationRef reference: A reference to the user''s physical location.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: locationRef
domain_of:
- AuditRecord
- Signature
range: LocationRef

```
</details>