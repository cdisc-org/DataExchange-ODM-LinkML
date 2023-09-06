# Enum: TransactionType




_Enumeration used in transactionType_



URI: [TransactionType](TransactionType)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Insert | None |  |
| Update | None |  |
| Remove | None |  |
| Upsert | None |  |
| Context | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [transactionType](transactionType.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... |
| [transactionType](transactionType.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... |
| [transactionType](transactionType.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... |
| [transactionType](transactionType.md) | The TransactionType attribute need not be present in a Snapshot document. |
| [transactionType](transactionType.md) | Records the TransactionType for this ItemData instance in the source system. |
| [transactionType](transactionType.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TransactionType
description: Enumeration used in transactionType
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  Insert:
    text: Insert
    is_a: TransactionType
  Update:
    text: Update
    is_a: TransactionType
  Remove:
    text: Remove
    is_a: TransactionType
  Upsert:
    text: Upsert
    is_a: TransactionType
  Context:
    text: Context
    is_a: TransactionType

```
</details>
