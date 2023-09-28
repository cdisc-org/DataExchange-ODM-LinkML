# Slot: epoch


_Epoch reference: The planned period of subjects' participation in the trial is divided into sequential epochs. Each epoch is a period of time that serves a purpose in the trial as a whole. Epochs cannot overlap. The sequence of the epoch in the study is provided by the SequenceNumber attribute, the first epoch in the study being assigned the sequence number 1. Sequence numbers are subsequent._



URI: [odm:epoch](http://www.cdisc.org/ns/odm/v2.0/epoch)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[StudyStructure](StudyStructure.md) | The StudyStructure element describes the general structure of a clinical stud... |  yes  |







## Properties

* Range: [Epoch](Epoch.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: epoch
description: 'Epoch reference: The planned period of subjects'' participation in the
  trial is divided into sequential epochs. Each epoch is a period of time that serves
  a purpose in the trial as a whole. Epochs cannot overlap. The sequence of the epoch
  in the study is provided by the SequenceNumber attribute, the first epoch in the
  study being assigned the sequence number 1. Sequence numbers are subsequent.'
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
identifier: false
alias: epoch
domain_of:
- StudyStructure
range: Epoch

```
</details>