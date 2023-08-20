# Class: SiteRef


_lement NameSiteRefParent ElementsSubjectDataElement XPath(s)/ODM/ClinicalData/SubjectData/SiteRefElement Textual ValueNoneAttributesLocationOIDChild ElementsNoneUsage/Business RulesBusiness Rule(s):Must be provided when the /ODM/FileType is Transactional._





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
| [LocationOID](LocationOID.md) | 1..1 <br/> [Oidref](Oidref.md) | Reference to a Location definition | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SubjectData](SubjectData.md) | [SiteRefRef](SiteRefRef.md) | range | [SiteRef](SiteRef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/SiteRef](https://wiki.cdisc.org/display/ODM2/SiteRef)

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
description: lement NameSiteRefParent ElementsSubjectDataElement XPath(s)/ODM/ClinicalData/SubjectData/SiteRefElement
  Textual ValueNoneAttributesLocationOIDChild ElementsNoneUsage/Business RulesBusiness
  Rule(s):Must be provided when the /ODM/FileType is Transactional.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SiteRef
slots:
- LocationOID
slot_usage:
  LocationOID:
    name: LocationOID
    description: Reference to a Location definition.
    comments:
    - 'Required

      range:oidref

      Must match the OID attribute value for an AdminData/Location element where the
      AdminData/@StudyOID attribute matches the ClinicalData/@StudyOID. '
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
    required: true
class_uri: odm:SiteRef

```
</details>

### Induced

<details>
```yaml
name: SiteRef
description: lement NameSiteRefParent ElementsSubjectDataElement XPath(s)/ODM/ClinicalData/SubjectData/SiteRefElement
  Textual ValueNoneAttributesLocationOIDChild ElementsNoneUsage/Business RulesBusiness
  Rule(s):Must be provided when the /ODM/FileType is Transactional.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/SiteRef
slot_usage:
  LocationOID:
    name: LocationOID
    description: Reference to a Location definition.
    comments:
    - 'Required

      range:oidref

      Must match the OID attribute value for an AdminData/Location element where the
      AdminData/@StudyOID attribute matches the ClinicalData/@StudyOID. '
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

      range:oidref

      Must match the OID attribute value for an AdminData/Location element where the
      AdminData/@StudyOID attribute matches the ClinicalData/@StudyOID. '
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: LocationOID
    owner: SiteRef
    domain_of:
    - User
    - Organization
    - SiteRef
    - LocationRef
    range: oidref
    required: true
class_uri: odm:SiteRef

```
</details>