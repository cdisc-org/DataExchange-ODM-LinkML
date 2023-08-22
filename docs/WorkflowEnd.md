# Class: WorkflowEnd


_A WorkflowEnd references a structural element with which the workflows ends._





URI: [odm:WorkflowEnd](http://www.cdisc.org/ns/odm/v2.0/WorkflowEnd)



```mermaid
 classDiagram
    class WorkflowEnd
      WorkflowEnd : _content
        
      WorkflowEnd : EndOID
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [EndOID](EndOID.md) | 1..1 <br/> [oidref](oidref.md) | Reference to the definition of the structural element that ends the workflow.... | direct |
| [_content](_content.md) | 0..1 <br/> [text](text.md) | multi-line text content from between XML tags | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowDef](WorkflowDef.md) | [WorkflowEndRef](WorkflowEndRef.md) | range | [WorkflowEnd](WorkflowEnd.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/WorkflowEnd](https://wiki.cdisc.org/display/ODM2/WorkflowEnd)

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
- https://wiki.cdisc.org/display/ODM2/WorkflowEnd
slots:
- EndOID
- _content
slot_usage:
  EndOID:
    name: EndOID
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
    range: oidref
    required: true
  _content:
    name: _content
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
- https://wiki.cdisc.org/display/ODM2/WorkflowEnd
slot_usage:
  EndOID:
    name: EndOID
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
    range: oidref
    required: true
  _content:
    name: _content
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
  EndOID:
    name: EndOID
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
    alias: EndOID
    owner: WorkflowEnd
    domain_of:
    - WorkflowEnd
    range: oidref
    required: true
  _content:
    name: _content
    description: multi-line text content from between XML tags
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: _content
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