# Enum: StandardPublishingSet



URI: [StandardPublishingSet](StandardPublishingSet)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ADaM | nci:ExtCodeID:C180548 |  |
| CDASH | nci:ExtCodeID:C180549 |  |
| DEFINE-XML | nci:ExtCodeID:C180550 |  |
| SDTM | nci:ExtCodeID:C180551 |  |
| SEND | nci:ExtCodeID:C180552 |  |




## Slots

| Name | Description |
| ---  | --- |
| [PublishingSet](PublishingSet.md) | Set of published files of Standard when Type="CT" (e |
| [PublishingSet](PublishingSet.md) | The name of the publishing set that contains the published standard |




## Aliases


* C172331



## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StandardPublishingSet
conforms_to: nci:ExtCodeID:C172331
from_schema: http://www.cdisc.org/ns/odm/v2.0
aliases:
- C172331
rank: 1000
code_set: nci:ExtCodeID
permissible_values:
  ADaM:
    text: ADaM
    meaning: nci:ExtCodeID:C180548
    is_a: StandardPublishingSet
  CDASH:
    text: CDASH
    meaning: nci:ExtCodeID:C180549
    is_a: StandardPublishingSet
  DEFINE-XML:
    text: DEFINE-XML
    meaning: nci:ExtCodeID:C180550
    is_a: StandardPublishingSet
  SDTM:
    text: SDTM
    meaning: nci:ExtCodeID:C180551
    is_a: StandardPublishingSet
  SEND:
    text: SEND
    meaning: nci:ExtCodeID:C180552
    is_a: StandardPublishingSet

```
</details>
