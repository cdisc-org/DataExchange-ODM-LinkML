# Class: GeoPosition

_The geographical position using the World Geodetic System WGS84._




URI: [odm:GeoPosition](http://www.cdisc.org/ns/odm/v2.0/GeoPosition)


```mermaid
erDiagram
GeoPosition {
    decimal Longitude  
    decimal Latitude  
    decimal Altitude  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [Longitude](Longitude.md) | 0..1 <br/> [decimal](decimal.md) | Longitude component of geoposition coordinates in decimal degrees. May requir... | direct |
| [Latitude](Latitude.md) | 0..1 <br/> [decimal](decimal.md) | Latitude component of geoposition coordinate in decimal degrees degrees. May ... | direct |
| [Altitude](Altitude.md) | 0..1 <br/> [decimal](decimal.md) | Height above sea level in meters. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Address](Address.md) | [GeoPositionRef](GeoPositionRef.md) | range | [GeoPosition](GeoPosition.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/GeoPosition](https://wiki.cdisc.org/display/PUB/GeoPosition)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:GeoPosition |
| native | odm:GeoPosition |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeoPosition
description: The geographical position using the World Geodetic System WGS84.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/GeoPosition
rank: 1000
slots:
- Longitude
- Latitude
- Altitude
slot_usage:
  Longitude:
    name: Longitude
    description: Longitude component of geoposition coordinates in decimal degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  Latitude:
    name: Latitude
    description: Latitude component of geoposition coordinate in decimal degrees degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  Altitude:
    name: Altitude
    description: Height above sea level in meters.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
class_uri: odm:GeoPosition

```
</details>

### Induced

<details>
```yaml
name: GeoPosition
description: The geographical position using the World Geodetic System WGS84.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/GeoPosition
rank: 1000
slot_usage:
  Longitude:
    name: Longitude
    description: Longitude component of geoposition coordinates in decimal degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  Latitude:
    name: Latitude
    description: Latitude component of geoposition coordinate in decimal degrees degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  Altitude:
    name: Altitude
    description: Height above sea level in meters.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
attributes:
  Longitude:
    name: Longitude
    description: Longitude component of geoposition coordinates in decimal degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Longitude
    owner: GeoPosition
    domain_of:
    - GeoPosition
    range: decimal
  Latitude:
    name: Latitude
    description: Latitude component of geoposition coordinate in decimal degrees degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Latitude
    owner: GeoPosition
    domain_of:
    - GeoPosition
    range: decimal
  Altitude:
    name: Altitude
    description: Height above sea level in meters.
    comments:
    - 'Optional

      range: decimal'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Altitude
    owner: GeoPosition
    domain_of:
    - GeoPosition
    range: decimal
class_uri: odm:GeoPosition

```
</details>