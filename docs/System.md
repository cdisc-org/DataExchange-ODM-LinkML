# Slot: System


_Identifies the code system that defines the code. If the code is taken from a code system resource then the URL for the code system should be used._



URI: [odm:System](http://www.cdisc.org/ns/odm/v2.0/System)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Coding](Coding.md) | Coding references a symbol from a defined code system. It uses a code defined... |  yes  |







## Properties

* Range: [uriorcurie](uriorcurie.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: System
description: Identifies the code system that defines the code. If the code is taken
  from a code system resource then the URL for the code system should be used.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: System
domain_of:
- Coding
range: uriorcurie

```
</details>