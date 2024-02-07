# Slot: signature


_Signature reference: An electronic signature applies to a collection of clinical data. This indicates that some user accepts legal responsibility for that data. See 21 CFR Part 11. The signature identifies the person signing, the location of signing, the signature meaning (via the referenced SignatureDef), the date and time of signing, and (in the case of a digital signature) an encrypted hash of the included data._



URI: [odm:signature](http://www.cdisc.org/ns/odm/v2.0/signature)



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







## Properties

* Range: [Signature](Signature.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: signature
description: 'Signature reference: An electronic signature applies to a collection
  of clinical data. This indicates that some user accepts legal responsibility for
  that data. See 21 CFR Part 11. The signature identifies the person signing, the
  location of signing, the signature meaning (via the referenced SignatureDef), the
  date and time of signing, and (in the case of a digital signature) an encrypted
  hash of the included data.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: signature
domain_of:
- ReferenceData
- ClinicalData
- SubjectData
- StudyEventData
- ItemGroupData
- ItemData
range: Signature

```
</details>