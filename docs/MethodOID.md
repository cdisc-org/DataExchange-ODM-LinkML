# Slot: MethodOID


_Reference to a MethodDef that will provide one or more data rows as output. The MethodDef is used to prepopulate items_



URI: [odm:MethodOID](http://www.cdisc.org/ns/odm/v2.0/MethodOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyE... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |







## Properties

* Range: [Oidref](Oidref.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: MethodOID
description: Reference to a MethodDef that will provide one or more data rows as output.
  The MethodDef is used to prepopulate items
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: MethodOID
domain_of:
- ItemGroupRef
- ItemRef
- TransitionTimingConstraint
range: oidref

```
</details>