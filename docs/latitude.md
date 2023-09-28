# Slot: latitude


_Latitude component of geoposition coordinate in decimal degrees degrees. May require conversion from degrees, minutes, seconds format._



URI: [odm:latitude](http://www.cdisc.org/ns/odm/v2.0/latitude)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeoPosition](GeoPosition.md) | The geographical position using the World Geodetic System WGS84. |  yes  |







## Properties

* Range: [decimal](decimal.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: latitude
description: Latitude component of geoposition coordinate in decimal degrees degrees.
  May require conversion from degrees, minutes, seconds format.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: latitude
domain_of:
- GeoPosition
range: decimal

```
</details>