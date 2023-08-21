# Enum: OriginType




_Enumeration used in Type_



URI: [OriginType](OriginType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Assigned | nci:ExtCodeID:C170547 |  |
| Collected | nci:ExtCodeID:C170548 |  |
| Derived | nci:ExtCodeID:C170549 |  |
| EHR | None |  |
| Not Available | nci:ExtCodeID:C126101 |  |
| Other | nci:ExtCodeID:C17649 |  |
| Predecessor | nci:ExtCodeID:C170550 |  |
| Protocol | nci:ExtCodeID:C170551 |  |




## Slots

| Name | Description |
| ---  | --- |
| [Type](Type.md) | Identifies how the clinical data values were obtained. |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: OriginType
description: Enumeration used in Type
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Assigned:
    text: Assigned
    meaning: nci:ExtCodeID:C170547
    is_a: OriginType
  Collected:
    text: Collected
    meaning: nci:ExtCodeID:C170548
    is_a: OriginType
  Derived:
    text: Derived
    meaning: nci:ExtCodeID:C170549
    is_a: OriginType
  EHR:
    text: EHR
    is_a: OriginType
  Not Available:
    text: Not Available
    meaning: nci:ExtCodeID:C126101
    is_a: OriginType
  Other:
    text: Other
    meaning: nci:ExtCodeID:C17649
    is_a: OriginType
  Predecessor:
    text: Predecessor
    meaning: nci:ExtCodeID:C170550
    is_a: OriginType
  Protocol:
    text: Protocol
    meaning: nci:ExtCodeID:C170551
    is_a: OriginType

```
</details>
