# Class: UserRef

_A reference to information about a specific user of a clinical data collection or data management system._




URI: [odm:UserRef](http://www.cdisc.org/ns/odm/v2.0/UserRef)


```mermaid
erDiagram
UserRef {
    oidref userOID  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [userOID](userOID.md) | 1..1 <br/> [oidref](oidref.md) | Reference to the User definition. | direct |

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
    range: oidref
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
    range: oidref
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
    range: oidref
    required: true
class_uri: odm:UserRef

```
</details>