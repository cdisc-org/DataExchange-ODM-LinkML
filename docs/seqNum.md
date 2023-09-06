# Slot: seqNum


_When more than 1 Value element exists this attribute uniquely identifies each Value and defines the order of a Value in a list of Values._



URI: [odm:seqNum](http://www.cdisc.org/ns/odm/v2.0/seqNum)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Annotation](Annotation.md) | A general note about clinical data. If an annotation has both a comment and f... |  yes  |
[Value](Value.md) | The data collected for an item. This data is represented according to DataTyp... |  yes  |







## Properties

* Range: [positiveInteger](positiveInteger.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: seqNum
description: When more than 1 Value element exists this attribute uniquely identifies
  each Value and defines the order of a Value in a list of Values.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: seqNum
domain_of:
- Annotation
- Value
range: positiveInteger

```
</details>