# Slot: TitleRef


_Text with the label for the document or dataset._



URI: [odm:TitleRef](http://www.cdisc.org/ns/odm/v2.0/TitleRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PDFPageRef](PDFPageRef.md) | This element is the container for CRF page references. |  yes  |
[Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |  yes  |







## Properties

* Range: [Title](Title.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: TitleRef
description: Text with the label for the document or dataset.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: TitleRef
domain_of:
- PDFPageRef
- Leaf
range: Title

```
</details>