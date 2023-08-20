# Slot: ValueRef


_Human-readable designation of the trial phase._



URI: [odm:ValueRef](http://www.cdisc.org/ns/odm/v2.0/ValueRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[TrialPhase](TrialPhase.md) | The TrialPhase element designates the phase of the study in the clinical tria... |  yes  |
[ParameterValue](ParameterValue.md) | This element contains the value of the study parameter as text content |  yes  |
[Telecom](Telecom.md) | The telecommunication contacts points of a user, a location, or an organizati... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |
[Query](Query.md) | The Query element represents a request for clarification on a data item colle... |  yes  |







## Properties

* Range: [Value](Value.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ValueRef
description: Human-readable designation of the trial phase.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: ValueRef
domain_of:
- TrialPhase
- ParameterValue
- Telecom
- ItemData
- Query
range: Value

```
</details>