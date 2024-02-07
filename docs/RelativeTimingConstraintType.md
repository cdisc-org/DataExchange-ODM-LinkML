# Enum: RelativeTimingConstraintType




_Enumeration used in type_



URI: [RelativeTimingConstraintType](RelativeTimingConstraintType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| StartToStart | None |  |
| StartToFinish | None |  |
| FinishToStart | None |  |
| FinishToFinish | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [type](type.md) | Defines how the timing is to be defined between the two activities, starting ... |
| [type](type.md) | Defines how the timing is to be defined between the two activities, starting ... |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: RelativeTimingConstraintType
description: Enumeration used in type
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  StartToStart:
    text: StartToStart
    is_a: RelativeTimingConstraintType
  StartToFinish:
    text: StartToFinish
    is_a: RelativeTimingConstraintType
  FinishToStart:
    text: FinishToStart
    is_a: RelativeTimingConstraintType
  FinishToFinish:
    text: FinishToFinish
    is_a: RelativeTimingConstraintType

```
</details>
