# Class: UserRef

_A reference to information about a specific user of a clinical data collection or data management system._




URI: [odm:UserRef](http://www.cdisc.org/ns/odm/v2.0/UserRef)


```mermaid
erDiagram
UserRef {

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

UserRef ||--|| User : "userOID"
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
| [userOID](userOID.md) | 1..1 <br/> [User](User.md) | Reference to the User definition. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AuditRecord](AuditRecord.md) | [userRef](userRef.md) | range | [UserRef](UserRef.md) |
| [Signature](Signature.md) | [userRef](userRef.md) | range | [UserRef](UserRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/UserRef](https://wiki.cdisc.org/display/PUB/UserRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:UserRef |
| native | odm:UserRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UserRef
description: A reference to information about a specific user of a clinical data collection
  or data management system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/UserRef
rank: 1000
slots:
- userOID
slot_usage:
  userOID:
    name: userOID
    description: Reference to the User definition.
    comments:
    - 'Required

      Must match the OID attribute of an AdminData/User element. If used within a
      ClinicalData element, the ClinicalData StudyOID attribute must match the StudyOID
      attribute in the the AdminData element.'
    domain_of:
    - InvestigatorRef
    - UserRef
    range: User
    required: true
class_uri: odm:UserRef

```
</details>

### Induced

<details>
```yaml
name: UserRef
description: A reference to information about a specific user of a clinical data collection
  or data management system.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/UserRef
rank: 1000
slot_usage:
  userOID:
    name: userOID
    description: Reference to the User definition.
    comments:
    - 'Required

      Must match the OID attribute of an AdminData/User element. If used within a
      ClinicalData element, the ClinicalData StudyOID attribute must match the StudyOID
      attribute in the the AdminData element.'
    domain_of:
    - InvestigatorRef
    - UserRef
    range: User
    required: true
attributes:
  userOID:
    name: userOID
    description: Reference to the User definition.
    comments:
    - 'Required

      Must match the OID attribute of an AdminData/User element. If used within a
      ClinicalData element, the ClinicalData StudyOID attribute must match the StudyOID
      attribute in the the AdminData element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: userOID
    owner: UserRef
    domain_of:
    - InvestigatorRef
    - UserRef
    range: User
    required: true
class_uri: odm:UserRef

```
</details>