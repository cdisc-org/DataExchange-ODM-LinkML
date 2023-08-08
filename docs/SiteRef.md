# Class: SiteRef



URI: [odm:SiteRef](http://www.cdisc.org/ns/odm/v2.0/SiteRef)



```mermaid
 classDiagram
    class SiteRef
      SiteRef : LocationOID
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [LocationOID](LocationOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SubjectData](SubjectData.md) | [SiteRefRef](SiteRefRef.md) | range | [SiteRef](SiteRef.md) |






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
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- LocationOID
slot_usage:
  LocationOID:
    name: LocationOID
    domain_of:
    - Organization
    - SiteRef
    - LocationRef
    - User
    range: oidref
    required: true
class_uri: odm:SiteRef

```
</details>

### Induced

<details>
```yaml
name: SiteRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  LocationOID:
    name: LocationOID
    domain_of:
    - Organization
    - SiteRef
    - LocationRef
    - User
    range: oidref
    required: true
attributes:
  LocationOID:
    name: LocationOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: LocationOID
    owner: SiteRef
    domain_of:
    - Organization
    - SiteRef
    - LocationRef
    - User
    range: oidref
    required: true
class_uri: odm:SiteRef

```
</details>