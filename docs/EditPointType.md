# Enum: EditPointType



URI: [EditPointType](EditPointType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Monitoring | None |  |
| DataManagement | None |  |
| DBAudit | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [EditPoint](EditPoint.md) | Identifies the phase of data processing in which update action occurred |
| [EditPoint](EditPoint.md) | Identifies the phase of data processing in which update action occurred |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: EditPointType
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Monitoring:
    text: Monitoring
    is_a: EditPointType
  DataManagement:
    text: DataManagement
    is_a: EditPointType
  DBAudit:
    text: DBAudit
    is_a: EditPointType

```
</details>
