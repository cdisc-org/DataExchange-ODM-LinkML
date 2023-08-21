# Slot: Title


_Text with the label for the document reference._



URI: [odm:Title](http://www.cdisc.org/ns/odm/v2.0/Title)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PDFPageRef](PDFPageRef.md) | This element is the container for CRF page references. |  yes  |
[Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |  yes  |







## Properties

* Range: [text](text.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Title
description: Text with the label for the document reference.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Title
domain_of:
- PDFPageRef
- Leaf
range: text

```
</details>