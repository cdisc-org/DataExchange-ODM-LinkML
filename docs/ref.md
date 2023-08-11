# Slot: ref

URI: [odm:ref](http://www.cdisc.org/ns/odm/v2.0/ref)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ExternalCodeLib](ExternalCodeLib.md) |  |  yes  |
[Coding](Coding.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: ref
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