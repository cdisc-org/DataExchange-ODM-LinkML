# Enum: EventType



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
| [Type](Type.md) | Specifies the StudyEvent Type |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: EventType
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
