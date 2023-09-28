# Enum: Context




_Enumeration used in context_



URI: [Context](Context)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Archive | None |  |
| Exchange | None |  |
| Submission | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [context](context.md) | Indicates the intended usage of the ODM document. Archive - indicates that th... |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Context
description: Enumeration used in context
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Archive:
    text: Archive
    is_a: Context
  Exchange:
    text: Exchange
    is_a: Context
  Submission:
    text: Submission
    is_a: Context

```
</details>
