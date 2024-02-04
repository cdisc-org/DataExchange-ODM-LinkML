# Enum: OriginSource




_Enumeration used in source_



URI: [OriginSource](OriginSource)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Investigator | ncit:C25936 |  |
| Sponsor | ncit:C70793 |  |
| Subject | ncit:C41189 |  |
| Vendor | ncit:C68608 |  |




## Slots

| Name | Description |
| ---  | --- |
| [source](source.md) | Indicates the party responsible for the data's origin type. |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: OriginSource
description: Enumeration used in source
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Investigator:
    text: Investigator
    meaning: ncit:C25936
    is_a: OriginSource
  Sponsor:
    text: Sponsor
    meaning: ncit:C70793
    is_a: OriginSource
  Subject:
    text: Subject
    meaning: ncit:C41189
    is_a: OriginSource
  Vendor:
    text: Vendor
    meaning: ncit:C68608
    is_a: OriginSource

```
</details>
