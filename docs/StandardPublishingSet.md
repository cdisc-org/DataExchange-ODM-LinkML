# Enum: StandardPublishingSet




_Enumeration used in publishingSet_



URI: [StandardPublishingSet](StandardPublishingSet)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ADaM | ncit:C180548 |  |
| CDASH | ncit:C180549 |  |
| DEFINE-XML | ncit:C180550 |  |
| SDTM | ncit:C180551 |  |
| SEND | ncit:C180552 |  |




## Slots

| Name | Description |
| ---  | --- |
| [publishingSet](publishingSet.md) | Set of published files of Standard when Type="CT" (e.g. SDTM, ADaM, SEND, CDA... |
| [publishingSet](publishingSet.md) | The name of the publishing set that contains the published standard. |




## Aliases


* C172331



## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: StandardPublishingSet
conforms_to: ncit
description: Enumeration used in publishingSet
from_schema: http://www.cdisc.org/ns/odm/v2.0
aliases:
- C172331
rank: 1000
code_set: ncit:C172331
permissible_values:
  ADaM:
    text: ADaM
    meaning: ncit:C180548
    is_a: StandardPublishingSet
  CDASH:
    text: CDASH
    meaning: ncit:C180549
    is_a: StandardPublishingSet
  DEFINE-XML:
    text: DEFINE-XML
    meaning: ncit:C180550
    is_a: StandardPublishingSet
  SDTM:
    text: SDTM
    meaning: ncit:C180551
    is_a: StandardPublishingSet
  SEND:
    text: SEND
    meaning: ncit:C180552
    is_a: StandardPublishingSet

```
</details>
