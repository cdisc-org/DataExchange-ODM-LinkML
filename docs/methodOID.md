# Slot: methodOID


_Reference to a MethodDef that will provide one or more data rows as output. The MethodDef is used to prepopulate items_



URI: [odm:methodOID](http://www.cdisc.org/ns/odm/v2.0/methodOID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyE... |  yes  |
[ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |  yes  |
[TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |  yes  |







## Properties

* Range: [MethodDef](MethodDef.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: methodOID
description: Reference to a MethodDef that will provide one or more data rows as output.
  The MethodDef is used to prepopulate items
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
alias: methodOID
domain_of:
- ItemGroupRef
- ItemRef
- TransitionTimingConstraint
range: MethodDef

```
</details>