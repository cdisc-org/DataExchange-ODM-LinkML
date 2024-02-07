# Slot: label


_Used to link the value to a named MethodDef parameter._



URI: [odm:label](http://www.cdisc.org/ns/odm/v2.0/label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Resource](Resource.md) | Describes an external resource used as the source for the parent ItemGroup or... |  yes  |
[Coding](Coding.md) | Coding references a symbol from a defined code system. It uses a code defined... |  yes  |







## Properties

* Range: [text](text.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: label
description: Used to link the value to a named MethodDef parameter.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: label
domain_of:
- Resource
- Coding
range: text

```
</details>