# Slot: OrderNumber


_Indicates the order in which this StudyEventGroup appears in Metadata displays or data entry applications._



URI: [odm:OrderNumber](http://www.cdisc.org/ns/odm/v2.0/OrderNumber)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific v... |  yes  |
[StudyEventRef](StudyEventRef.md) | This element references a StudyEventDef as it occurs within a specific versio... |  yes  |
[ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyE... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist |  yes  |
[Parameter](Parameter.md) | The Parameter element represents a method parameter used as part of a MethodS... |  yes  |
[ReturnValue](ReturnValue.md) | The ReturnValue element represents a return value used as part of a MethodSig... |  yes  |
[StudyEndPointRef](StudyEndPointRef.md) | Go to start of metadata |  yes  |







## Properties

* Range: [PositiveInteger](PositiveInteger.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: OrderNumber
description: Indicates the order in which this StudyEventGroup appears in Metadata
  displays or data entry applications.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: OrderNumber
domain_of:
- StudyEventGroupRef
- StudyEventRef
- ItemGroupRef
- ItemRef
- CodeListItem
- Parameter
- ReturnValue
- StudyEndPointRef
range: positiveInteger

```
</details>