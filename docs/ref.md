# Slot: ref


_Reference to a local instance (e.g. file) of the external library containing the FormalExpression code._



URI: [odm:ref](http://www.cdisc.org/ns/odm/v2.0/ref)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ExternalCodeLib](ExternalCodeLib.md) | The ExternalCodeLib element references a FormalExpression in an external code... |  yes  |
[Coding](Coding.md) | Coding references a symbol from a defined code system |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ref
description: Reference to a local instance (e.g. file) of the external library containing
  the FormalExpression code.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: ref
domain_of:
- ExternalCodeLib
- Coding
range: string
any_of:
- range: text
- range: uriorcurie

```
</details>