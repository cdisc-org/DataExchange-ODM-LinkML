# Enum: EventType




_Enumeration used in type_



URI: [EventType](EventType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Scheduled | None |  |
| Unscheduled | None |  |
| Common | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [type](type.md) | Specifies the StudyEvent Type. The study protocol document usually specifies ... |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: EventType
description: Enumeration used in type
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Scheduled:
    text: Scheduled
    is_a: EventType
  Unscheduled:
    text: Unscheduled
    is_a: EventType
  Common:
    text: Common
    is_a: EventType

```
</details>
