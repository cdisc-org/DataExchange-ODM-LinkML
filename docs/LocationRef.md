# Class: LocationRef

_A reference to the user's physical location._




URI: [odm:LocationRef](http://www.cdisc.org/ns/odm/v2.0/LocationRef)


```mermaid
erDiagram
LocationRef {

}
Location {
    oid OID  
    nameType name  
    text role  
}
Query {
    oid OID  
    QuerySourceType source  
    text target  
    QueryType type  
    QueryStateType state  
    datetime lastUpdateDatetime  
    nameType name  
}
Telecom {
    TelecomTypeType telecomType  
    text value  
}
Address {

}
MetaDataVersionRef {
    date effectiveDate  
}
Description {

}
Organization {
    oid OID  
    nameType name  
    text role  
    OrganizationType type  
}

LocationRef ||--|| Location : "locationOID"
Location ||--|o Organization : "organizationOID"
Location ||--|o Description : "description"
Location ||--}o MetaDataVersionRef : "metaDataVersionRef"
Location ||--}o Address : "address"
Location ||--}o Telecom : "telecom"
Location ||--}o Query : "query"
Query ||--|o Value : "value"
Query ||--}o AuditRecord : "auditRecord"
Address ||--|o StreetName : "streetName"
Address ||--|o HouseNumber : "houseNumber"
Address ||--|o City : "city"
Address ||--|o StateProv : "stateProv"
Address ||--|o Country : "country"
Address ||--|o PostalCode : "postalCode"
Address ||--|o GeoPosition : "geoPosition"
Address ||--|o OtherText : "otherText"
MetaDataVersionRef ||--|| Study : "studyOID"
MetaDataVersionRef ||--|| MetaDataVersion : "metaDataVersionOID"
Description ||--}o TranslatedText : "translatedText"
Organization ||--|o Location : "locationOID"
Organization ||--|o Organization : "partOfOrganizationOID"
Organization ||--|o Description : "description"
Organization ||--}o Address : "address"
Organization ||--}o Telecom : "telecom"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [locationOID](locationOID.md) | 1..1 <br/> [Location](Location.md) | Reference to a Location definition. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AuditRecord](AuditRecord.md) | [locationRef](locationRef.md) | range | [LocationRef](LocationRef.md) |
| [Signature](Signature.md) | [locationRef](locationRef.md) | range | [LocationRef](LocationRef.md) |






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
- locationOID
slot_usage:
  locationOID:
    name: locationOID
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
    range: Location
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
  locationOID:
    name: locationOID
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
    range: Location
    required: true
attributes:
  locationOID:
    name: locationOID
    description: Reference to a Location definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID for an AdminData/Location element and the LocationOID for
      the UserRef element contained within the AuditRecord or Signature.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: locationOID
    owner: LocationRef
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: Location
    required: true
class_uri: odm:LocationRef

```
</details>