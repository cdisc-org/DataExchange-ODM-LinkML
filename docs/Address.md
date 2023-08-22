# Class: Address

_The postal address for a user, location, or organization._




URI: [odm:Address](http://www.cdisc.org/ns/odm/v2.0/Address)


```mermaid
erDiagram
Address {

}
OtherText {
    text content  
}
GeoPosition {
    decimal Longitude  
    decimal Latitude  
    decimal Altitude  
}
PostalCode {
    text content  
}
Country {
    text content  
}
StateProv {
    text content  
}
City {
    text content  
}
HouseNumber {
    text content  
}
StreetName {
    text content  
}

Address ||--|o StreetName : "StreetNameRef"
Address ||--|o HouseNumber : "HouseNumberRef"
Address ||--|o City : "CityRef"
Address ||--|o StateProv : "StateProvRef"
Address ||--|o Country : "CountryRef"
Address ||--|o PostalCode : "PostalCodeRef"
Address ||--|o GeoPosition : "GeoPositionRef"
Address ||--|o OtherText : "OtherTextRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StreetNameRef](StreetNameRef.md) | 0..1 <br/> [StreetName](StreetName.md) | StreetName reference: The street name part of a user's postal address. | direct |
| [HouseNumberRef](HouseNumberRef.md) | 0..1 <br/> [HouseNumber](HouseNumber.md) | HouseNumber reference: The house number part of a user's postal address. | direct |
| [CityRef](CityRef.md) | 0..1 <br/> [City](City.md) | City reference: The city name part of a user's postal address. | direct |
| [StateProvRef](StateProvRef.md) | 0..1 <br/> [StateProv](StateProv.md) | StateProv reference: The state or province name part of a user's postal addre... | direct |
| [CountryRef](CountryRef.md) | 0..1 <br/> [Country](Country.md) | Country reference: The country name part of a user's postal address. For CDIS... | direct |
| [PostalCodeRef](PostalCodeRef.md) | 0..1 <br/> [PostalCode](PostalCode.md) | PostalCode reference: The postal code part of a user's postal address. | direct |
| [GeoPositionRef](GeoPositionRef.md) | 0..1 <br/> [GeoPosition](GeoPosition.md) | GeoPosition reference: The geographical position using the World Geodetic Sys... | direct |
| [OtherTextRef](OtherTextRef.md) | 0..1 <br/> [OtherText](OtherText.md) | OtherText reference: Any other text needed as part of a user's postal address... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [User](User.md) | [AddressRef](AddressRef.md) | range | [Address](Address.md) |
| [Organization](Organization.md) | [AddressRef](AddressRef.md) | range | [Address](Address.md) |
| [Location](Location.md) | [AddressRef](AddressRef.md) | range | [Address](Address.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Address](https://wiki.cdisc.org/display/PUB/Address)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Address |
| native | odm:Address |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Address
description: The postal address for a user, location, or organization.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Address
rank: 1000
slots:
- StreetNameRef
- HouseNumberRef
- CityRef
- StateProvRef
- CountryRef
- PostalCodeRef
- GeoPositionRef
- OtherTextRef
slot_usage:
  StreetNameRef:
    name: StreetNameRef
    domain_of:
    - Address
    range: StreetName
    maximum_cardinality: 1
  HouseNumberRef:
    name: HouseNumberRef
    domain_of:
    - Address
    range: HouseNumber
    maximum_cardinality: 1
  CityRef:
    name: CityRef
    domain_of:
    - Address
    range: City
    maximum_cardinality: 1
  StateProvRef:
    name: StateProvRef
    domain_of:
    - Address
    range: StateProv
    maximum_cardinality: 1
  CountryRef:
    name: CountryRef
    domain_of:
    - Address
    range: Country
    maximum_cardinality: 1
  PostalCodeRef:
    name: PostalCodeRef
    domain_of:
    - Address
    range: PostalCode
    maximum_cardinality: 1
  GeoPositionRef:
    name: GeoPositionRef
    domain_of:
    - Address
    range: GeoPosition
    maximum_cardinality: 1
  OtherTextRef:
    name: OtherTextRef
    domain_of:
    - Address
    range: OtherText
    maximum_cardinality: 1
class_uri: odm:Address

```
</details>

### Induced

<details>
```yaml
name: Address
description: The postal address for a user, location, or organization.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Address
rank: 1000
slot_usage:
  StreetNameRef:
    name: StreetNameRef
    domain_of:
    - Address
    range: StreetName
    maximum_cardinality: 1
  HouseNumberRef:
    name: HouseNumberRef
    domain_of:
    - Address
    range: HouseNumber
    maximum_cardinality: 1
  CityRef:
    name: CityRef
    domain_of:
    - Address
    range: City
    maximum_cardinality: 1
  StateProvRef:
    name: StateProvRef
    domain_of:
    - Address
    range: StateProv
    maximum_cardinality: 1
  CountryRef:
    name: CountryRef
    domain_of:
    - Address
    range: Country
    maximum_cardinality: 1
  PostalCodeRef:
    name: PostalCodeRef
    domain_of:
    - Address
    range: PostalCode
    maximum_cardinality: 1
  GeoPositionRef:
    name: GeoPositionRef
    domain_of:
    - Address
    range: GeoPosition
    maximum_cardinality: 1
  OtherTextRef:
    name: OtherTextRef
    domain_of:
    - Address
    range: OtherText
    maximum_cardinality: 1
attributes:
  StreetNameRef:
    name: StreetNameRef
    description: 'StreetName reference: The street name part of a user''s postal address.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StreetNameRef
    owner: Address
    domain_of:
    - Address
    range: StreetName
    maximum_cardinality: 1
  HouseNumberRef:
    name: HouseNumberRef
    description: 'HouseNumber reference: The house number part of a user''s postal
      address.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: HouseNumberRef
    owner: Address
    domain_of:
    - Address
    range: HouseNumber
    maximum_cardinality: 1
  CityRef:
    name: CityRef
    description: 'City reference: The city name part of a user''s postal address.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: CityRef
    owner: Address
    domain_of:
    - Address
    range: City
    maximum_cardinality: 1
  StateProvRef:
    name: StateProvRef
    description: 'StateProv reference: The state or province name part of a user''s
      postal address.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: StateProvRef
    owner: Address
    domain_of:
    - Address
    range: StateProv
    maximum_cardinality: 1
  CountryRef:
    name: CountryRef
    description: 'Country reference: The country name part of a user''s postal address.
      For CDISC SDTM or trial registry applications, this must be represented by an
      ISO 3166 3-letter or US-GENC country code (e.g., FRA for France, JPN for Japan).'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: CountryRef
    owner: Address
    domain_of:
    - Address
    range: Country
    maximum_cardinality: 1
  PostalCodeRef:
    name: PostalCodeRef
    description: 'PostalCode reference: The postal code part of a user''s postal address.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: PostalCodeRef
    owner: Address
    domain_of:
    - Address
    range: PostalCode
    maximum_cardinality: 1
  GeoPositionRef:
    name: GeoPositionRef
    description: 'GeoPosition reference: The geographical position using the World
      Geodetic System WGS84.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: GeoPositionRef
    owner: Address
    domain_of:
    - Address
    range: GeoPosition
    maximum_cardinality: 1
  OtherTextRef:
    name: OtherTextRef
    description: 'OtherText reference: Any other text needed as part of a user''s
      postal address.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: OtherTextRef
    owner: Address
    domain_of:
    - Address
    range: OtherText
    maximum_cardinality: 1
class_uri: odm:Address

```
</details>