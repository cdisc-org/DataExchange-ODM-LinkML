# Slot: orderNumber


_Indicates the order in which this StudyEventGroup appears in Metadata displays or data entry applications._



URI: [odm:orderNumber](http://www.cdisc.org/ns/odm/v2.0/orderNumber)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific v... |  yes  |
[StudyEventRef](StudyEventRef.md) | This element references a StudyEventDef as it occurs within a specific versio... |  yes  |
[ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyE... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |
[CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |  yes  |
[Parameter](Parameter.md) | The Parameter element represents a method parameter used as part of a MethodS... |  yes  |
[ReturnValue](ReturnValue.md) | The ReturnValue element represents a return value used as part of a MethodSig... |  yes  |
[StudyEndPointRef](StudyEndPointRef.md) | A reference to a StudyEndPoint as it occurs within a specific StudyObjective. |  yes  |







## Properties

* Range: [positiveInteger](positiveInteger.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: orderNumber
description: Indicates the order in which this StudyEventGroup appears in Metadata
  displays or data entry applications.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: orderNumber
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