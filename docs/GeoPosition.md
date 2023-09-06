# Class: GeoPosition

_The geographical position using the World Geodetic System WGS84._




URI: [odm:GeoPosition](http://www.cdisc.org/ns/odm/v2.0/GeoPosition)


```mermaid
erDiagram
GeoPosition {
    decimal longitude  
    decimal latitude  
    decimal altitude  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [longitude](longitude.md) | 0..1 <br/> [decimal](decimal.md) | Longitude component of geoposition coordinates in decimal degrees. May requir... | direct |
| [latitude](latitude.md) | 0..1 <br/> [decimal](decimal.md) | Latitude component of geoposition coordinate in decimal degrees degrees. May ... | direct |
| [altitude](altitude.md) | 0..1 <br/> [decimal](decimal.md) | Height above sea level in meters. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Address](Address.md) | [geoPosition](geoPosition.md) | range | [GeoPosition](GeoPosition.md) |






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
- longitude
- latitude
- altitude
slot_usage:
  longitude:
    name: longitude
    description: Longitude component of geoposition coordinates in decimal degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  latitude:
    name: latitude
    description: Latitude component of geoposition coordinate in decimal degrees degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  altitude:
    name: altitude
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
  longitude:
    name: longitude
    description: Longitude component of geoposition coordinates in decimal degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  latitude:
    name: latitude
    description: Latitude component of geoposition coordinate in decimal degrees degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
  altitude:
    name: altitude
    description: Height above sea level in meters.
    comments:
    - 'Optional

      range: decimal'
    domain_of:
    - GeoPosition
    range: decimal
attributes:
  longitude:
    name: longitude
    description: Longitude component of geoposition coordinates in decimal degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: longitude
    owner: GeoPosition
    domain_of:
    - GeoPosition
    range: decimal
  latitude:
    name: latitude
    description: Latitude component of geoposition coordinate in decimal degrees degrees.
      May require conversion from degrees, minutes, seconds format.
    comments:
    - 'Optional

      range: decimal'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: latitude
    owner: GeoPosition
    domain_of:
    - GeoPosition
    range: decimal
  altitude:
    name: altitude
    description: Height above sea level in meters.
    comments:
    - 'Optional

      range: decimal'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: altitude
    owner: GeoPosition
    domain_of:
    - GeoPosition
    range: decimal
class_uri: odm:GeoPosition

```
</details>