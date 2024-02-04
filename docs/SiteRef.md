# Class: SiteRef

_Provides a reference to the site that the SubjectData record is associated with in the source system._




URI: [odm:SiteRef](http://www.cdisc.org/ns/odm/v2.0/SiteRef)


```mermaid
erDiagram
SiteRef {

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

SiteRef ||--|| Location : "locationOID"
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
| [SubjectData](SubjectData.md) | [siteRef](siteRef.md) | range | [SiteRef](SiteRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/SiteRef](https://wiki.cdisc.org/display/PUB/SiteRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SiteRef |
| native | odm:SiteRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SiteRef
description: Provides a reference to the site that the SubjectData record is associated
  with in the source system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SiteRef
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

      Must match the OID attribute value for an AdminData/Location element where the
      AdminData/@StudyOID attribute matches the ClinicalData/@StudyOID.'
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: Location
    required: true
class_uri: odm:SiteRef

```
</details>

### Induced

<details>
```yaml
name: SiteRef
description: Provides a reference to the site that the SubjectData record is associated
  with in the source system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SiteRef
rank: 1000
slot_usage:
  locationOID:
    name: locationOID
    description: Reference to a Location definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID attribute value for an AdminData/Location element where the
      AdminData/@StudyOID attribute matches the ClinicalData/@StudyOID.'
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

      Must match the OID attribute value for an AdminData/Location element where the
      AdminData/@StudyOID attribute matches the ClinicalData/@StudyOID.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: locationOID
    owner: SiteRef
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: Location
    required: true
class_uri: odm:SiteRef

```
</details>