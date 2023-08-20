# Slot: Label


_Used to link the value to a named MethodDef parameter._



URI: [odm:Label](http://www.cdisc.org/ns/odm/v2.0/Label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Resource](Resource.md) | Describes an external resource used as the source for the parent ItemGroup or... |  yes  |
[Coding](Coding.md) | Coding references a symbol from a defined code system |  yes  |







## Properties

* Range: [Text](Text.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Label
description: Used to link the value to a named MethodDef parameter.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Label
domain_of:
- Resource
- Coding
range: text

```
</details>