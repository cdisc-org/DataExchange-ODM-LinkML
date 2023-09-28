# Enum: QueryStateType




_Enumeration used in state_



URI: [QueryStateType](QueryStateType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Candidate | None |  |
| Open | None |  |
| Answered | None |  |
| Closed | None |  |
| Cancelled | None |  |
| Resolved | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [state](state.md) | Status of the Query |
| [state](state.md) | Status of the Query |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: QueryStateType
description: Enumeration used in state
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Candidate:
    text: Candidate
    is_a: QueryStateType
  Open:
    text: Open
    is_a: QueryStateType
  Answered:
    text: Answered
    is_a: QueryStateType
  Closed:
    text: Closed
    is_a: QueryStateType
  Cancelled:
    text: Cancelled
    is_a: QueryStateType
  Resolved:
    text: Resolved
    is_a: QueryStateType

```
</details>
