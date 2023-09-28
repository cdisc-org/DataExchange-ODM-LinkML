# Enum: StandardType




_Enumeration used in type_



URI: [StandardType](StandardType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CT | nci:ExtCodeID:C163415 |  |
| IG | nci:ExtCodeID:C170454 |  |




## Slots

| Name | Description |
| ---  | --- |
| [type](type.md) | The type of standard. |




## Aliases


* C170451



## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StandardType
conforms_to: nci:ExtCodeID:C170451
description: Enumeration used in type
from_schema: http://www.cdisc.org/ns/odm/v2.0
aliases:
- C170451
rank: 1000
code_set: nci:ExtCodeID
permissible_values:
  CT:
    text: CT
    meaning: nci:ExtCodeID:C163415
    is_a: StandardType
  IG:
    text: IG
    meaning: nci:ExtCodeID:C170454
    is_a: StandardType

```
</details>
