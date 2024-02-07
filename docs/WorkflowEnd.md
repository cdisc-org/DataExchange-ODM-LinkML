# Class: WorkflowEnd

_A WorkflowEnd references a structural element with which the workflows ends._




URI: [odm:WorkflowEnd](http://www.cdisc.org/ns/odm/v2.0/WorkflowEnd)


```mermaid
erDiagram
WorkflowEnd {
    string endOID  
    text content  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [endOID](endOID.md) | 1..1 <br/> [string](string.md) | Reference to the definition of the structural element that ends the workflow.... | direct |
| [content](content.md) | 0..1 <br/> [text](text.md) | multi-line text content from between XML tags | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowDef](WorkflowDef.md) | [workflowEnd](workflowEnd.md) | range | [WorkflowEnd](WorkflowEnd.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/WorkflowEnd](https://wiki.cdisc.org/display/PUB/WorkflowEnd)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:WorkflowEnd |
| native | odm:WorkflowEnd |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkflowEnd
description: A WorkflowEnd references a structural element with which the workflows
  ends.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/WorkflowEnd
rank: 1000
slots:
- endOID
- content
slot_usage:
  endOID:
    name: endOID
    description: Reference to the definition of the structural element that ends the
      workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef
      element.
    comments:
    - 'Required

      range: oidref

      The EndOID must match the OID attribute of a StudyEventGroupDef, StudyEventDef,
      ItemGroupDef or ItemDef child element of the MetaDataVersion parent element
      of the WorkflowDef.'
    domain_of:
    - WorkflowEnd
    required: true
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  content:
    name: content
    domain_of:
    - TranslatedText
    - Title
    - CheckValue
    - Code
    - WorkflowEnd
    - UserName
    - Prefix
    - Suffix
    - FullName
    - GivenName
    - FamilyName
    - StreetName
    - HouseNumber
    - City
    - StateProv
    - Country
    - PostalCode
    - OtherText
    - Meaning
    - LegalReason
    - DateTimeStamp
    - ReasonForChange
    - SourceID
    - FlagValue
    - FlagType
    - Value
    range: text
class_uri: odm:WorkflowEnd

```
</details>

### Induced

<details>
```yaml
name: WorkflowEnd
description: A WorkflowEnd references a structural element with which the workflows
  ends.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/WorkflowEnd
rank: 1000
slot_usage:
  endOID:
    name: endOID
    description: Reference to the definition of the structural element that ends the
      workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef
      element.
    comments:
    - 'Required

      range: oidref

      The EndOID must match the OID attribute of a StudyEventGroupDef, StudyEventDef,
      ItemGroupDef or ItemDef child element of the MetaDataVersion parent element
      of the WorkflowDef.'
    domain_of:
    - WorkflowEnd
    required: true
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  content:
    name: content
    domain_of:
    - TranslatedText
    - Title
    - CheckValue
    - Code
    - WorkflowEnd
    - UserName
    - Prefix
    - Suffix
    - FullName
    - GivenName
    - FamilyName
    - StreetName
    - HouseNumber
    - City
    - StateProv
    - Country
    - PostalCode
    - OtherText
    - Meaning
    - LegalReason
    - DateTimeStamp
    - ReasonForChange
    - SourceID
    - FlagValue
    - FlagType
    - Value
    range: text
attributes:
  endOID:
    name: endOID
    description: Reference to the definition of the structural element that ends the
      workflow. It may be a StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef
      element.
    comments:
    - 'Required

      range: oidref

      The EndOID must match the OID attribute of a StudyEventGroupDef, StudyEventDef,
      ItemGroupDef or ItemDef child element of the MetaDataVersion parent element
      of the WorkflowDef.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: endOID
    owner: WorkflowEnd
    domain_of:
    - WorkflowEnd
    range: string
    required: true
    any_of:
    - range: StudyEventGroupDef
    - range: StudyEventDef
    - range: ItemGroupDef
    - range: ItemDef
  content:
    name: content
    description: multi-line text content from between XML tags
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: content
    owner: WorkflowEnd
    domain_of:
    - TranslatedText
    - Title
    - CheckValue
    - Code
    - WorkflowEnd
    - UserName
    - Prefix
    - Suffix
    - FullName
    - GivenName
    - FamilyName
    - StreetName
    - HouseNumber
    - City
    - StateProv
    - Country
    - PostalCode
    - OtherText
    - Meaning
    - LegalReason
    - DateTimeStamp
    - ReasonForChange
    - SourceID
    - FlagValue
    - FlagType
    - Value
    range: text
    inlined: true
class_uri: odm:WorkflowEnd

```
</details>