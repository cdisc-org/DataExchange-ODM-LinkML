# Class: Telecom

_The telecommunication contacts points of a user, a location, or an organization. The Type attribute designates the type of contact._




URI: [odm:Telecom](http://www.cdisc.org/ns/odm/v2.0/Telecom)


```mermaid
erDiagram
Telecom {
    TelecomTypeType telecomType  
    text value  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [telecomType](telecomType.md) | 1..1 <br/> [TelecomTypeType](TelecomTypeType.md) |  | direct |
| [value](value.md) | 1..1 <br/> [text](text.md) | Human-readable designation of the trial phase. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [User](User.md) | [telecom](telecom.md) | range | [Telecom](Telecom.md) |
| [Organization](Organization.md) | [telecom](telecom.md) | range | [Telecom](Telecom.md) |
| [Location](Location.md) | [telecom](telecom.md) | range | [Telecom](Telecom.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Telecom](https://wiki.cdisc.org/display/PUB/Telecom)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Telecom |
| native | odm:Telecom |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Telecom
description: The telecommunication contacts points of a user, a location, or an organization.
  The Type attribute designates the type of contact.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Telecom
rank: 1000
slots:
- telecomType
- value
slot_usage:
  telecomType:
    name: telecomType
    comments:
    - 'Required

      enum values: (Email | Pager | Phone | Fax | SMS | URL | Other)

      Values are aligned with FHIR ContactPoint/System data element.'
    domain_of:
    - Telecom
    range: TelecomTypeType
    required: true
  value:
    name: value
    comments:
    - 'Required

      range: text'
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: text
    required: true
class_uri: odm:Telecom

```
</details>

### Induced

<details>
```yaml
name: Telecom
description: The telecommunication contacts points of a user, a location, or an organization.
  The Type attribute designates the type of contact.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Telecom
rank: 1000
slot_usage:
  telecomType:
    name: telecomType
    comments:
    - 'Required

      enum values: (Email | Pager | Phone | Fax | SMS | URL | Other)

      Values are aligned with FHIR ContactPoint/System data element.'
    domain_of:
    - Telecom
    range: TelecomTypeType
    required: true
  value:
    name: value
    comments:
    - 'Required

      range: text'
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: text
    required: true
attributes:
  telecomType:
    name: telecomType
    comments:
    - 'Required

      enum values: (Email | Pager | Phone | Fax | SMS | URL | Other)

      Values are aligned with FHIR ContactPoint/System data element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: telecomType
    owner: Telecom
    domain_of:
    - Telecom
    range: TelecomTypeType
    required: true
  value:
    name: value
    description: Human-readable designation of the trial phase.
    comments:
    - 'Required

      range: text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: value
    owner: Telecom
    domain_of:
    - TrialPhase
    - ParameterValue
    - Telecom
    - ItemData
    - Query
    range: text
    required: true
class_uri: odm:Telecom

```
</details>