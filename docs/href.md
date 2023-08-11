# Slot: href


_URL that can be used to identify the location of a document or dataset file relative to the folder containing the ODM file._



URI: [odm:href](http://www.cdisc.org/ns/odm/v2.0/href)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |  yes  |
[Include](Include.md) |  |  yes  |
[ExternalCodeLib](ExternalCodeLib.md) |  |  yes  |
[Image](Image.md) |  |  yes  |
[Coding](Coding.md) |  |  yes  |







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
- leaf
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