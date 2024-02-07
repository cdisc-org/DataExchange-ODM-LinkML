# Slot: subjectKey


_Unique identifier for the Subject._



URI: [odm:subjectKey](http://www.cdisc.org/ns/odm/v2.0/subjectKey)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SubjectData](SubjectData.md) | Clinical data for a single subject. |  yes  |
[KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |  yes  |







## Properties

* Range: [subjectKeyType](subjectKeyType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: subjectKey
description: Unique identifier for the Subject.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: subjectKey
domain_of:
- SubjectData
- KeySet
range: subjectKeyType

```
</details>