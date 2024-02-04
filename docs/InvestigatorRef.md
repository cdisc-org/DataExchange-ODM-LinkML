# Class: InvestigatorRef

_Provides a reference to the user who created the SubjectData record in the source system._




URI: [odm:InvestigatorRef](http://www.cdisc.org/ns/odm/v2.0/InvestigatorRef)


```mermaid
erDiagram
InvestigatorRef {

}
User {
    oid OID  
    UserType userType  
}
Telecom {
    TelecomTypeType telecomType  
    text value  
}
Address {

}
Image {
    fileName imageFileName  
    text href  
    text mimeType  
}
FamilyName {
    text content  
}
GivenName {
    text content  
}
FullName {
    text content  
}
Suffix {
    text content  
}
Prefix {
    text content  
}
UserName {
    text content  
}
Location {
    oid OID  
    nameType name  
    text role  
}
Organization {
    oid OID  
    nameType name  
    text role  
    OrganizationType type  
}

InvestigatorRef ||--|| User : "userOID"
User ||--|o Organization : "organizationOID"
User ||--|o Location : "locationOID"
User ||--|o UserName : "userName"
User ||--|o Prefix : "prefix"
User ||--|o Suffix : "suffix"
User ||--|o FullName : "fullName"
User ||--|o GivenName : "givenName"
User ||--|o FamilyName : "familyName"
User ||--|o Image : "image"
User ||--}o Address : "address"
User ||--}o Telecom : "telecom"
Address ||--|o StreetName : "streetName"
Address ||--|o HouseNumber : "houseNumber"
Address ||--|o City : "city"
Address ||--|o StateProv : "stateProv"
Address ||--|o Country : "country"
Address ||--|o PostalCode : "postalCode"
Address ||--|o GeoPosition : "geoPosition"
Address ||--|o OtherText : "otherText"
Location ||--|o Organization : "organizationOID"
Location ||--|o Description : "description"
Location ||--}o MetaDataVersionRef : "metaDataVersionRef"
Location ||--}o Address : "address"
Location ||--}o Telecom : "telecom"
Location ||--}o Query : "query"
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
| [userOID](userOID.md) | 1..1 <br/> [User](User.md) | Reference to a User definition. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SubjectData](SubjectData.md) | [investigatorRef](investigatorRef.md) | range | [InvestigatorRef](InvestigatorRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/InvestigatorRef](https://wiki.cdisc.org/display/PUB/InvestigatorRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:InvestigatorRef |
| native | odm:InvestigatorRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InvestigatorRef
description: Provides a reference to the user who created the SubjectData record in
  the source system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/InvestigatorRef
rank: 1000
slots:
- userOID
slot_usage:
  userOID:
    name: userOID
    description: Reference to a User definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID attribute for an AdminData/User element where the AdminData/@StudyOID
      matches the ClinicalData/@StudyOID.'
    domain_of:
    - InvestigatorRef
    - UserRef
    range: User
    required: true
class_uri: odm:InvestigatorRef

```
</details>

### Induced

<details>
```yaml
name: InvestigatorRef
description: Provides a reference to the user who created the SubjectData record in
  the source system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/InvestigatorRef
rank: 1000
slot_usage:
  userOID:
    name: userOID
    description: Reference to a User definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID attribute for an AdminData/User element where the AdminData/@StudyOID
      matches the ClinicalData/@StudyOID.'
    domain_of:
    - InvestigatorRef
    - UserRef
    range: User
    required: true
attributes:
  userOID:
    name: userOID
    description: Reference to a User definition.
    comments:
    - 'Required

      range: oidref

      Must match the OID attribute for an AdminData/User element where the AdminData/@StudyOID
      matches the ClinicalData/@StudyOID.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: userOID
    owner: InvestigatorRef
    domain_of:
    - InvestigatorRef
    - UserRef
    range: User
    required: true
class_uri: odm:InvestigatorRef

```
</details>