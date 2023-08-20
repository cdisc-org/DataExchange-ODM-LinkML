# Enum: FileType



URI: [FileType](FileType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Snapshot | None |  |
| Transactional | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [FileTypeRef](FileTypeRef.md) | Snapshot means that the document contains only the current state of the data ... |
| [FileTypeRef](FileTypeRef.md) | Snapshot means that the document contains only the current state of the data ... |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: FileType
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Snapshot:
    text: Snapshot
    is_a: FileType
  Transactional:
    text: Transactional
    is_a: FileType

```
</details>
