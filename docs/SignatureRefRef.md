# Slot: SignatureRefRef


_SignatureRef reference: A reference to the signature meaning._



URI: [odm:SignatureRefRef](http://www.cdisc.org/ns/odm/v2.0/SignatureRefRef)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data. For ex... |  yes  |
[ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects. |  yes  |
[SubjectData](SubjectData.md) | Clinical data for a single subject. |  yes  |
[StudyEventData](StudyEventData.md) | Clinical data for a study event (visit). The model supports repeating study e... |  yes  |
[ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |  yes  |
[ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |  yes  |
[Signature](Signature.md) | An electronic signature applies to a collection of clinical data. This indica... |  yes  |







## Properties

* Range: [SignatureRef](SignatureRef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: SignatureRefRef
description: 'SignatureRef reference: A reference to the signature meaning.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: SignatureRefRef
domain_of:
- ReferenceData
- ClinicalData
- SubjectData
- StudyEventData
- ItemGroupData
- ItemData
- Signature
range: SignatureRef

```
</details>