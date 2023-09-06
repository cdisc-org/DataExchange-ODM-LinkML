# Enum: OrganizationType




_Enumeration used in type_



URI: [OrganizationType](OrganizationType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Sponsor | None |  |
| Site | None |  |
| CRO | None |  |
| Lab | None |  |
| Other | None |  |
| TechnologyProvider | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [type](type.md) | Categorization of organizations associated with clinical studies. |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: OrganizationType
description: Enumeration used in type
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Sponsor:
    text: Sponsor
    is_a: OrganizationType
  Site:
    text: Site
    is_a: OrganizationType
  CRO:
    text: CRO
    is_a: OrganizationType
  Lab:
    text: Lab
    is_a: OrganizationType
  Other:
    text: Other
    is_a: OrganizationType
  TechnologyProvider:
    text: TechnologyProvider
    is_a: OrganizationType

```
</details>
