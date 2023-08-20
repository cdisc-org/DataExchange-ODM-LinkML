# Enum: ItemGroupSubClass



URI: [ItemGroupSubClass](ItemGroupSubClass)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ADVERSE EVENT | nci:ExtCodeID:C176265 |  |
| MEDICAL DEVICE TIME-TO-EVENT | nci:ExtCodeID:C177920 |  |
| NON-COMPARTMENTAL ANALYSIS | nci:ExtCodeID:C172452 |  |
| TIME-TO-EVENT | nci:ExtCodeID:C165637 |  |




## Slots

| Name | Description |
| ---  | --- |
| [Name](Name.md) | Name of the SubClass |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ItemGroupSubClass
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  ADVERSE EVENT:
    text: ADVERSE EVENT
    meaning: nci:ExtCodeID:C176265
    is_a: ItemGroupSubClass
  MEDICAL DEVICE TIME-TO-EVENT:
    text: MEDICAL DEVICE TIME-TO-EVENT
    meaning: nci:ExtCodeID:C177920
    is_a: ItemGroupSubClass
  NON-COMPARTMENTAL ANALYSIS:
    text: NON-COMPARTMENTAL ANALYSIS
    meaning: nci:ExtCodeID:C172452
    is_a: ItemGroupSubClass
  TIME-TO-EVENT:
    text: TIME-TO-EVENT
    meaning: nci:ExtCodeID:C165637
    is_a: ItemGroupSubClass

```
</details>
