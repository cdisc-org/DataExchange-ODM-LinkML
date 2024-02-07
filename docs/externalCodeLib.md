# Slot: externalCodeLib


_ExternalCodeLib reference: The ExternalCodeLib element references a FormalExpression in an external code library, such as a file or GitHub. The intention is to make it possible to reference existing code libraries where the code is maintained as well as making it simpler to include longer, more complex FormalExpressions. The Library attribute provides the name of the external library, whereas ref or href provides a reference to the repository that can be used to retrieve the code. The Method attribute provides the name of the method in the file referenced for cases where multiple methods are provided in the source code file. The Version element provides the version of the external FormalExpression code referenced._



URI: [odm:externalCodeLib](http://www.cdisc.org/ns/odm/v2.0/externalCodeLib)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FormalExpression](FormalExpression.md) | A FormalExpression used within a ConditionDef or a RangeCheck must evaluate t... |  yes  |







## Properties

* Range: [ExternalCodeLib](ExternalCodeLib.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: externalCodeLib
description: 'ExternalCodeLib reference: The ExternalCodeLib element references a
  FormalExpression in an external code library, such as a file or GitHub. The intention
  is to make it possible to reference existing code libraries where the code is maintained
  as well as making it simpler to include longer, more complex FormalExpressions.
  The Library attribute provides the name of the external library, whereas ref or
  href provides a reference to the repository that can be used to retrieve the code.
  The Method attribute provides the name of the method in the file referenced for
  cases where multiple methods are provided in the source code file. The Version element
  provides the version of the external FormalExpression code referenced.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: externalCodeLib
domain_of:
- FormalExpression
range: ExternalCodeLib

```
</details>