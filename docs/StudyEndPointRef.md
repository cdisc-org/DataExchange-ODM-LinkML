# Class: StudyEndPointRef

_A reference to a StudyEndPoint as it occurs within a specific StudyObjective._




URI: [odm:StudyEndPointRef](http://www.cdisc.org/ns/odm/v2.0/StudyEndPointRef)


```mermaid
erDiagram
StudyEndPointRef {
    oidref studyEndPointOID  
    positiveInteger orderNumber  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyEndPointOID](studyEndPointOID.md) | 1..1 <br/> [oidref](oidref.md) | Reference to the StudyEndPoint . | direct |
| [orderNumber](orderNumber.md) | 0..1 <br/> [positiveInteger](positiveInteger.md) | Indicates the order in which this StudyEndPointRef appears in Metadata displa... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyObjective](StudyObjective.md) | [studyEndPointRef](studyEndPointRef.md) | range | [StudyEndPointRef](StudyEndPointRef.md) |
| [StudyEstimand](StudyEstimand.md) | [studyEndPointRef](studyEndPointRef.md) | range | [StudyEndPointRef](StudyEndPointRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/StudyEndPointRef](https://wiki.cdisc.org/display/PUB/StudyEndPointRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:StudyEndPointRef |
| native | odm:StudyEndPointRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyEndPointRef
description: A reference to a StudyEndPoint as it occurs within a specific StudyObjective.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEndPointRef
rank: 1000
slots:
- studyEndPointOID
- orderNumber
slot_usage:
  studyEndPointOID:
    name: studyEndPointOID
    description: Reference to the StudyEndPoint .
    comments:
    - 'Required

      Must match the OID atttribute for a StudyEndPoint in the Study/MetaDataVersion/Protocol.'
    domain_of:
    - StudyEndPointRef
    range: oidref
    required: true
  orderNumber:
    name: orderNumber
    description: Indicates the order in which this StudyEndPointRef appears in Metadata
      displays or data entry applications.
    comments:
    - 'Optional

      OrderNumber must be a positive integer. The StudyEndPointRefs within a StudyObjective
      must not have duplicate OrderNumber values'
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
class_uri: odm:StudyEndPointRef

```
</details>

### Induced

<details>
```yaml
name: StudyEndPointRef
description: A reference to a StudyEndPoint as it occurs within a specific StudyObjective.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/StudyEndPointRef
rank: 1000
slot_usage:
  studyEndPointOID:
    name: studyEndPointOID
    description: Reference to the StudyEndPoint .
    comments:
    - 'Required

      Must match the OID atttribute for a StudyEndPoint in the Study/MetaDataVersion/Protocol.'
    domain_of:
    - StudyEndPointRef
    range: oidref
    required: true
  orderNumber:
    name: orderNumber
    description: Indicates the order in which this StudyEndPointRef appears in Metadata
      displays or data entry applications.
    comments:
    - 'Optional

      OrderNumber must be a positive integer. The StudyEndPointRefs within a StudyObjective
      must not have duplicate OrderNumber values'
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
attributes:
  studyEndPointOID:
    name: studyEndPointOID
    description: Reference to the StudyEndPoint .
    comments:
    - 'Required

      Must match the OID atttribute for a StudyEndPoint in the Study/MetaDataVersion/Protocol.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyEndPointOID
    owner: StudyEndPointRef
    domain_of:
    - StudyEndPointRef
    range: oidref
    required: true
  orderNumber:
    name: orderNumber
    description: Indicates the order in which this StudyEndPointRef appears in Metadata
      displays or data entry applications.
    comments:
    - 'Optional

      OrderNumber must be a positive integer. The StudyEndPointRefs within a StudyObjective
      must not have duplicate OrderNumber values'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: orderNumber
    owner: StudyEndPointRef
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
class_uri: odm:StudyEndPointRef

```
</details>