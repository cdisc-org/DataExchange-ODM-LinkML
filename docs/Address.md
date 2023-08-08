# Class: Address



URI: [odm:Address](http://www.cdisc.org/ns/odm/v2.0/Address)



```mermaid
 classDiagram
    class Address
      Address : CityRef
        
          Address --|> City : CityRef
        
      Address : CountryRef
        
          Address --|> Country : CountryRef
        
      Address : GeoPositionRef
        
          Address --|> GeoPosition : GeoPositionRef
        
      Address : HouseNumberRef
        
          Address --|> HouseNumber : HouseNumberRef
        
      Address : OtherTextRef
        
          Address --|> OtherText : OtherTextRef
        
      Address : PostalCodeRef
        
          Address --|> PostalCode : PostalCodeRef
        
      Address : StateProvRef
        
          Address --|> StateProv : StateProvRef
        
      Address : StreetNameRef
        
          Address --|> StreetName : StreetNameRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [StreetNameRef](StreetNameRef.md) | 0..1 <br/> [StreetName](StreetName.md) |  | direct |
| [HouseNumberRef](HouseNumberRef.md) | 0..1 <br/> [HouseNumber](HouseNumber.md) |  | direct |
| [CityRef](CityRef.md) | 0..1 <br/> [City](City.md) |  | direct |
| [StateProvRef](StateProvRef.md) | 0..1 <br/> [StateProv](StateProv.md) |  | direct |
| [CountryRef](CountryRef.md) | 0..1 <br/> [Country](Country.md) |  | direct |
| [PostalCodeRef](PostalCodeRef.md) | 0..1 <br/> [PostalCode](PostalCode.md) |  | direct |
| [GeoPositionRef](GeoPositionRef.md) | 0..1 <br/> [GeoPosition](GeoPosition.md) |  | direct |
| [OtherTextRef](OtherTextRef.md) | 0..1 <br/> [OtherText](OtherText.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Organization](Organization.md) | [AddressRef](AddressRef.md) | range | [Address](Address.md) |
| [User](User.md) | [AddressRef](AddressRef.md) | range | [Address](Address.md) |
| [Location](Location.md) | [AddressRef](AddressRef.md) | range | [Address](Address.md) |






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
from_schema: http://www.cdisc.org/ns/odm/v2.0
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
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  HouseNumberRef:
    name: HouseNumberRef
    domain_of:
    - Address
    range: HouseNumber
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  CityRef:
    name: CityRef
    domain_of:
    - Address
    range: City
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  StateProvRef:
    name: StateProvRef
    domain_of:
    - Address
    range: StateProv
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  CountryRef:
    name: CountryRef
    domain_of:
    - Address
    range: Country
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  PostalCodeRef:
    name: PostalCodeRef
    domain_of:
    - Address
    range: PostalCode
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  GeoPositionRef:
    name: GeoPositionRef
    domain_of:
    - Address
    range: GeoPosition
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  OtherTextRef:
    name: OtherTextRef
    domain_of:
    - Address
    range: OtherText
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
class_uri: odm:Address

```
</details>

### Induced

<details>
```yaml
name: Address
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  StreetNameRef:
    name: StreetNameRef
    domain_of:
    - Address
    range: StreetName
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  HouseNumberRef:
    name: HouseNumberRef
    domain_of:
    - Address
    range: HouseNumber
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  CityRef:
    name: CityRef
    domain_of:
    - Address
    range: City
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  StateProvRef:
    name: StateProvRef
    domain_of:
    - Address
    range: StateProv
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  CountryRef:
    name: CountryRef
    domain_of:
    - Address
    range: Country
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  PostalCodeRef:
    name: PostalCodeRef
    domain_of:
    - Address
    range: PostalCode
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  GeoPositionRef:
    name: GeoPositionRef
    domain_of:
    - Address
    range: GeoPosition
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  OtherTextRef:
    name: OtherTextRef
    domain_of:
    - Address
    range: OtherText
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
attributes:
  StreetNameRef:
    name: StreetNameRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StreetNameRef
    owner: Address
    domain_of:
    - Address
    range: StreetName
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  HouseNumberRef:
    name: HouseNumberRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: HouseNumberRef
    owner: Address
    domain_of:
    - Address
    range: HouseNumber
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  CityRef:
    name: CityRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CityRef
    owner: Address
    domain_of:
    - Address
    range: City
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  StateProvRef:
    name: StateProvRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: StateProvRef
    owner: Address
    domain_of:
    - Address
    range: StateProv
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  CountryRef:
    name: CountryRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CountryRef
    owner: Address
    domain_of:
    - Address
    range: Country
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  PostalCodeRef:
    name: PostalCodeRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: PostalCodeRef
    owner: Address
    domain_of:
    - Address
    range: PostalCode
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  GeoPositionRef:
    name: GeoPositionRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: GeoPositionRef
    owner: Address
    domain_of:
    - Address
    range: GeoPosition
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
  OtherTextRef:
    name: OtherTextRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: OtherTextRef
    owner: Address
    domain_of:
    - Address
    range: OtherText
    required: false
    minimum_cardinality: 0
    maximum_cardinality: 1
class_uri: odm:Address

```
</details>