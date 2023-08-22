# Class: LocationRef

_A reference to the user's physical location._




URI: [odm:LocationRef](http://www.cdisc.org/ns/odm/v2.0/LocationRef)


```mermaid
erDiagram
LocationRef {
    oidref LocationOID  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [LocationOID](LocationOID.md) | 1..1 <br/> [oidref](oidref.md) | Reference to a Location definition. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AuditRecord](AuditRecord.md) | [LocationRefRef](LocationRefRef.md) | range | [LocationRef](LocationRef.md) |
| [Signature](Signature.md) | [LocationRefRef](LocationRefRef.md) | range | [LocationRef](LocationRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/LocationRef](https://wiki.cdisc.org/display/PUB/LocationRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:LocationRef |
| native | odm:LocationRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LocationRef
description: A reference to the user's physical location.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/LocationRef
rank: 1000
slots:
- LocationOID
slot_usage:
  LocationOID:
    name: LocationOID
    description: Reference to a Location definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID for an AdminData/Location element and the LocationOID for
      the UserRef element contained within the AuditRecord or Signature.'
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
    required: true
class_uri: odm:LocationRef

```
</details>

### Induced

<details>
```yaml
name: LocationRef
description: A reference to the user's physical location.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/LocationRef
rank: 1000
slot_usage:
  LocationOID:
    name: LocationOID
    description: Reference to a Location definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID for an AdminData/Location element and the LocationOID for
      the UserRef element contained within the AuditRecord or Signature.'
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
    required: true
attributes:
  LocationOID:
    name: LocationOID
    description: Reference to a Location definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID for an AdminData/Location element and the LocationOID for
      the UserRef element contained within the AuditRecord or Signature.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: LocationOID
    owner: LocationRef
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
    required: true
class_uri: odm:LocationRef

```
</details>