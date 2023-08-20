# Slot: FormalExpressionRef

URI: [odm:FormalExpressionRef](http://www.cdisc.org/ns/odm/v2.0/FormalExpressionRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition |  yes  |
[StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |  yes  |
[StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |  yes  |







## Properties

* Range: [FormalExpression](FormalExpression.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: FormalExpressionRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: FormalExpressionRef
domain_of:
- RangeCheck
- MethodDef
- ConditionDef
- StudyEndPoint
- StudyTargetPopulation
range: FormalExpression

```
</details>