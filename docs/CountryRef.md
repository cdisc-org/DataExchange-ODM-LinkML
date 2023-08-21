# Slot: CountryRef


_Country reference: The country name part of a user's postal address. For CDISC SDTM or trial registry applications, this must be represented by an ISO 3166 3-letter or US-GENC country code (e.g., FRA for France, JPN for Japan)._



URI: [odm:CountryRef](http://www.cdisc.org/ns/odm/v2.0/CountryRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Address](Address.md) | The postal address for a user, location, or organization. |  yes  |







## Properties

* Range: [Country](Country.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: CountryRef
description: 'Country reference: The country name part of a user''s postal address.
  For CDISC SDTM or trial registry applications, this must be represented by an ISO
  3166 3-letter or US-GENC country code (e.g., FRA for France, JPN for Japan).'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: CountryRef
domain_of:
- Address
range: Country

```
</details>