# Slot: Attribute


_Field provided by the Name attribute where the data or information can be obtained. Examples are "valueQuantity.value" or "valueQuantity.unit" for the case of an HL7-FHIR "Observation", "Repeating" for the case of an ODM ItemGroupDef element, "unit" for the case of an HL7-CDA doseQuantity, "Code" or "Name" for the case of field 5 (which is composite) of an HL7-v2 OBX message. The Name and Attribute attributes are meant to provide traceability documentation._



URI: [odm:Attribute](http://www.cdisc.org/ns/odm/v2.0/Attribute)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Resource](Resource.md) | Describes an external resource used as the source for the parent ItemGroup or... |  yes  |







## Properties

* Range: [Text](Text.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: Attribute
description: Field provided by the Name attribute where the data or information can
  be obtained. Examples are "valueQuantity.value" or "valueQuantity.unit" for the
  case of an HL7-FHIR "Observation", "Repeating" for the case of an ODM ItemGroupDef
  element, "unit" for the case of an HL7-CDA doseQuantity, "Code" or "Name" for the
  case of field 5 (which is composite) of an HL7-v2 OBX message. The Name and Attribute
  attributes are meant to provide traceability documentation.
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: Attribute
domain_of:
- Resource
range: text

```
</details>