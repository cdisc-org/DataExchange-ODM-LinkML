# Slot: length


_The Length attribute is optional when DataType is text, string,_

_                    integer, or float; and should not be used for the other_

_                    datatypes._



URI: [odm:length](http://www.cdisc.org/ns/odm/v2.0/length)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |  yes  |







## Properties

* Range: [positiveInteger](positiveInteger.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: length
description: "The Length attribute is optional when DataType is text, string,\n  \
  \                  integer, or float; and should not be used for the other\n   \
  \                 datatypes."
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: length
domain_of:
- ItemDef
range: positiveInteger

```
</details>