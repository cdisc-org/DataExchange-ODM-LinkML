# Slot: FormalExpressionRef


_FormalExpression reference: A FormalExpression used within a ConditionDef or a RangeCheck must evaluate to True or False. A FormalExpression referenced within a MethodDef having Type Imputation, Computation, or Transpose must evaluate to the correct DataType for an Item that may be imputed or computed using the Method. A FormalExpression gets parameter and return value definitions from the MethodSignature element. The data types in the MethodSignature parameters and return values must match the corresponding data types in the FormalExpression._



URI: [odm:FormalExpressionRef](http://www.cdisc.org/ns/odm/v2.0/FormalExpressionRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item. It repr... |  yes  |
[MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |  yes  |
[ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |  yes  |
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
description: 'FormalExpression reference: A FormalExpression used within a ConditionDef
  or a RangeCheck must evaluate to True or False. A FormalExpression referenced within
  a MethodDef having Type Imputation, Computation, or Transpose must evaluate to the
  correct DataType for an Item that may be imputed or computed using the Method. A
  FormalExpression gets parameter and return value definitions from the MethodSignature
  element. The data types in the MethodSignature parameters and return values must
  match the corresponding data types in the FormalExpression.'
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