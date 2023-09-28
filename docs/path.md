# Slot: path


_Provides the machine-executable instruction or template for it to obtain the data or information from the resource. The value of the Path attribute can either be an absolute path, or a relative path starting from the information in the "Name" and "Attribute" attributes of the parent Resource element._



URI: [odm:path](http://www.cdisc.org/ns/odm/v2.0/path)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Selection](Selection.md) | Template for machine-readable/executable expression for retrieving the data o... |  yes  |







## Properties

* Range: [text](text.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: path
description: Provides the machine-executable instruction or template for it to obtain
  the data or information from the resource. The value of the Path attribute can either
  be an absolute path, or a relative path starting from the information in the "Name"
  and "Attribute" attributes of the parent Resource element.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: path
domain_of:
- Selection
range: text

```
</details>