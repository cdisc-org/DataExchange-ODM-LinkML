# Slot: href


_URL that can be used to identify the location of a document or dataset file relative to the folder containing the ODM file._



URI: [odm:href](http://www.cdisc.org/ns/odm/v2.0/href)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |  yes  |
[Include](Include.md) | The Include metadata element allows a reference to a prior metadata version |  yes  |
[ExternalCodeLib](ExternalCodeLib.md) | The ExternalCodeLib element references a FormalExpression in an external code... |  yes  |
[Image](Image.md) | A visual depiction of the user |  yes  |
[Coding](Coding.md) | Coding references a symbol from a defined code system |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: href
description: URL that can be used to identify the location of a document or dataset
  file relative to the folder containing the ODM file.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: href
domain_of:
- Leaf
- Include
- ExternalCodeLib
- Image
- Coding
range: string
any_of:
- range: uriorcurie
- range: text

```
</details>