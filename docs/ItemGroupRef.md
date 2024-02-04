# Class: ItemGroupRef

_ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyEventDef or ItemGroupDef. The list of ItemGroupRefs identifies the types of item groups that are allowed to occur within this type of studyevent or (nested) item group. The ItemGroupRefs within a single StudyEventDef or ItemGroupDef must not have duplicate ItemGroupOID or OrderNumber attribute values._




URI: [odm:ItemGroupRef](http://www.cdisc.org/ns/odm/v2.0/ItemGroupRef)


```mermaid
erDiagram
ItemGroupRef {
    positiveInteger orderNumber  
    YesOrNo mandatory  
}
ConditionDef {
    oid OID  
    nameType name  
}
Alias {
    text context  
    text name  
}
FormalExpression {
    text context  
}
MethodSignature {

}
Description {

}
CommentDef {
    oid OID  
}
MethodDef {
    oid OID  
    nameType name  
    MethodType type  
}
DocumentRef {
    oid leafID  
}
ItemGroupDef {
    oid OID  
    nameType name  
    ItemGroupRepeatingType repeating  
    positiveInteger repeatingLimit  
    YesOrNo isReferenceData  
    text structure  
    nameType datasetName  
    text domain  
    ItemGroupTypeType type  
    text purpose  
    YesOnly isNonStandard  
    YesOnly hasNoData  
}
ItemRef {
    positiveInteger keySequence  
    YesOnly isNonStandard  
    YesOnly hasNoData  
    YesOnly repeat  
    YesOnly other  
    text role  
    CoreType core  
    text preSpecifiedValue  
    positiveInteger orderNumber  
    YesOrNo mandatory  
}
Leaf {
    oid ID  
    uriorcurie href  
}
Origin {
    OriginType type  
    OriginSource source  
}
WorkflowRef {

}
Coding {
    text code  
    uriorcurie system  
    text systemName  
    text systemVersion  
    text label  
    uriorcurie href  
    uriorcurie ref  
    text commentOID  
}
Class {
    ItemGroupClass name  
}
Standard {
    oid OID  
    StandardName name  
    StandardType type  
    StandardPublishingSet publishingSet  
    text version  
    StandardStatus status  
}

ItemGroupRef ||--|| ItemGroupDef : "itemGroupOID"
ItemGroupRef ||--|o MethodDef : "methodOID"
ItemGroupRef ||--|o ConditionDef : "collectionExceptionConditionOID"
ConditionDef ||--|o CommentDef : "commentOID"
ConditionDef ||--|o Description : "description"
ConditionDef ||--|o MethodSignature : "methodSignature"
ConditionDef ||--}o FormalExpression : "formalExpression"
ConditionDef ||--}o Alias : "alias"
FormalExpression ||--|o Code : "code"
FormalExpression ||--|o ExternalCodeLib : "externalCodeLib"
MethodSignature ||--}o Parameter : "parameter"
MethodSignature ||--}o ReturnValue : "returnValue"
Description ||--}o TranslatedText : "translatedText"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"
MethodDef ||--|o CommentDef : "commentOID"
MethodDef ||--|o Description : "description"
MethodDef ||--|o MethodSignature : "methodSignature"
MethodDef ||--}o FormalExpression : "formalExpression"
MethodDef ||--}o Alias : "alias"
MethodDef ||--}o DocumentRef : "documentRef"
DocumentRef ||--}o PDFPageRef : "pDFPageRef"
ItemGroupDef ||--|o Leaf : "archiveLocationID"
ItemGroupDef ||--|o Standard : "standardOID"
ItemGroupDef ||--|o CommentDef : "commentOID"
ItemGroupDef ||--|o Description : "description"
ItemGroupDef ||--|o Class : "itemGroupClass"
ItemGroupDef ||--}o Coding : "coding"
ItemGroupDef ||--|o WorkflowRef : "workflowRef"
ItemGroupDef ||--}o Origin : "origin"
ItemGroupDef ||--}o Alias : "alias"
ItemGroupDef ||--|o Leaf : "leaf"
ItemGroupDef ||--}o ItemGroupRef : "itemGroupRef"
ItemGroupDef ||--}o ItemRef : "itemRef"
ItemRef ||--|| ItemDef : "itemOID"
ItemRef ||--|o MethodDef : "methodOID"
ItemRef ||--|o ItemDef : "unitsItemOID"
ItemRef ||--|o CodeList : "roleCodeListOID"
ItemRef ||--|o ConditionDef : "collectionExceptionConditionOID"
ItemRef ||--}o Origin : "origin"
ItemRef ||--}o WhereClauseRef : "whereClauseRef"
Leaf ||--|o Title : "title"
Origin ||--|o Description : "description"
Origin ||--|o SourceItems : "sourceItems"
Origin ||--}o Coding : "coding"
Origin ||--}o DocumentRef : "documentRef"
WorkflowRef ||--|| WorkflowDef : "workflowOID"
Class ||--}o SubClass : "subClass"
Standard ||--|o CommentDef : "commentOID"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [itemGroupOID](itemGroupOID.md) | 1..1 <br/> [ItemGroupDef](ItemGroupDef.md) | Reference to the ItemGroupDef . | direct |
| [methodOID](methodOID.md) | 0..1 <br/> [MethodDef](MethodDef.md) | Reference to a MethodDef that will provide one or more data rows as output. T... | direct |
| [orderNumber](orderNumber.md) | 0..1 <br/> [positiveInteger](positiveInteger.md) | Indicates the order in which this ItemGroup appears in Metadata displays or d... | direct |
| [mandatory](mandatory.md) | 1..1 <br/> [YesOrNo](YesOrNo.md) | The Mandatory flag indicates that the clinical data for an instance of the co... | direct |
| [collectionExceptionConditionOID](collectionExceptionConditionOID.md) | 0..1 <br/> [ConditionDef](ConditionDef.md) | Reference to a ConditionDef If the CollectionExceptionConditionOID attribute ... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyEventDef](StudyEventDef.md) | [itemGroupRef](itemGroupRef.md) | range | [ItemGroupRef](ItemGroupRef.md) |
| [ItemGroupDef](ItemGroupDef.md) | [itemGroupRef](itemGroupRef.md) | range | [ItemGroupRef](ItemGroupRef.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/ItemGroupRef](https://wiki.cdisc.org/display/PUB/ItemGroupRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:ItemGroupRef |
| native | odm:ItemGroupRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ItemGroupRef
description: ItemGroupRef references an ItemGroupDef as it occurs within a specific
  StudyEventDef or ItemGroupDef. The list of ItemGroupRefs identifies the types of
  item groups that are allowed to occur within this type of studyevent or (nested)
  item group. The ItemGroupRefs within a single StudyEventDef or ItemGroupDef must
  not have duplicate ItemGroupOID or OrderNumber attribute values.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ItemGroupRef
rank: 1000
slots:
- itemGroupOID
- methodOID
- orderNumber
- mandatory
- collectionExceptionConditionOID
slot_usage:
  itemGroupOID:
    name: itemGroupOID
    description: Reference to the ItemGroupDef .
    comments:
    - 'Required

      range: oidref

      Must match the OID atttribute for an ItemGroupDef in the Study/MetaDataVersion.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
    required: true
  methodOID:
    name: methodOID
    description: Reference to a MethodDef that will provide one or more data rows
      as output. The MethodDef is used to prepopulate items
    comments:
    - 'Optional

      range: oidref

      The MethodOID value must match the OID attribute for a MethodDef in this Study/MetaDataVersion.'
    domain_of:
    - ItemGroupRef
    - ItemRef
    - TransitionTimingConstraint
    range: MethodDef
  orderNumber:
    name: orderNumber
    description: Indicates the order in which this ItemGroup appears in Metadata displays
      or data entry applications. The OrderNumber attribute provides an ordering on
      the ItemGroupDefs (within StudyEventDef or ItemGroupDef) for use whenever a
      list of ItemGroupDefs is presented to a user. Order of execution is preferably
      defined in a workflow (see Section 3.2.2.1.8, WorkflowDef ) but when used without
      a workflow, may be used the define the order in which data entry forms are presented
      in an application UI.
    comments:
    - 'Optional

      range: positiveInteger

      The StudyEventRefs within a StudyEventGroup must not have duplicate OrderNumber
      values'
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
  mandatory:
    name: mandatory
    description: The Mandatory flag indicates that the clinical data for an instance
      of the containing event or ItemGroup would be incomplete without an instance
      of this type of ItemGroup. ODM clinical data files that are incomplete in this
      sense may be considered incomplete for study review and analysis purposes.
    comments:
    - 'Required

      enum values: (Yes | No)

      When the value is Yes, the data for each subject in the study must include a
      StudyEventData element with this StudyEventOID.'
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: YesOrNo
    required: true
  collectionExceptionConditionOID:
    name: collectionExceptionConditionOID
    description: Reference to a ConditionDef If the CollectionExceptionConditionOID
      attribute is provided, the ConditionDef it references describes the circumstances
      under which data for this ItemGroup should not be collected.
    comments:
    - 'Optional

      range: oidref

      The CollectionExceptionConditionOID value must match the OID attribute for a
      ConditionDef in this Study/MetaDataVersion'
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: ConditionDef
class_uri: odm:ItemGroupRef

```
</details>

### Induced

<details>
```yaml
name: ItemGroupRef
description: ItemGroupRef references an ItemGroupDef as it occurs within a specific
  StudyEventDef or ItemGroupDef. The list of ItemGroupRefs identifies the types of
  item groups that are allowed to occur within this type of studyevent or (nested)
  item group. The ItemGroupRefs within a single StudyEventDef or ItemGroupDef must
  not have duplicate ItemGroupOID or OrderNumber attribute values.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/ItemGroupRef
rank: 1000
slot_usage:
  itemGroupOID:
    name: itemGroupOID
    description: Reference to the ItemGroupDef .
    comments:
    - 'Required

      range: oidref

      Must match the OID atttribute for an ItemGroupDef in the Study/MetaDataVersion.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
    required: true
  methodOID:
    name: methodOID
    description: Reference to a MethodDef that will provide one or more data rows
      as output. The MethodDef is used to prepopulate items
    comments:
    - 'Optional

      range: oidref

      The MethodOID value must match the OID attribute for a MethodDef in this Study/MetaDataVersion.'
    domain_of:
    - ItemGroupRef
    - ItemRef
    - TransitionTimingConstraint
    range: MethodDef
  orderNumber:
    name: orderNumber
    description: Indicates the order in which this ItemGroup appears in Metadata displays
      or data entry applications. The OrderNumber attribute provides an ordering on
      the ItemGroupDefs (within StudyEventDef or ItemGroupDef) for use whenever a
      list of ItemGroupDefs is presented to a user. Order of execution is preferably
      defined in a workflow (see Section 3.2.2.1.8, WorkflowDef ) but when used without
      a workflow, may be used the define the order in which data entry forms are presented
      in an application UI.
    comments:
    - 'Optional

      range: positiveInteger

      The StudyEventRefs within a StudyEventGroup must not have duplicate OrderNumber
      values'
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
  mandatory:
    name: mandatory
    description: The Mandatory flag indicates that the clinical data for an instance
      of the containing event or ItemGroup would be incomplete without an instance
      of this type of ItemGroup. ODM clinical data files that are incomplete in this
      sense may be considered incomplete for study review and analysis purposes.
    comments:
    - 'Required

      enum values: (Yes | No)

      When the value is Yes, the data for each subject in the study must include a
      StudyEventData element with this StudyEventOID.'
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: YesOrNo
    required: true
  collectionExceptionConditionOID:
    name: collectionExceptionConditionOID
    description: Reference to a ConditionDef If the CollectionExceptionConditionOID
      attribute is provided, the ConditionDef it references describes the circumstances
      under which data for this ItemGroup should not be collected.
    comments:
    - 'Optional

      range: oidref

      The CollectionExceptionConditionOID value must match the OID attribute for a
      ConditionDef in this Study/MetaDataVersion'
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: ConditionDef
attributes:
  itemGroupOID:
    name: itemGroupOID
    description: Reference to the ItemGroupDef .
    comments:
    - 'Required

      range: oidref

      Must match the OID atttribute for an ItemGroupDef in the Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemGroupOID
    owner: ItemGroupRef
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
    required: true
  methodOID:
    name: methodOID
    description: Reference to a MethodDef that will provide one or more data rows
      as output. The MethodDef is used to prepopulate items
    comments:
    - 'Optional

      range: oidref

      The MethodOID value must match the OID attribute for a MethodDef in this Study/MetaDataVersion.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: methodOID
    owner: ItemGroupRef
    domain_of:
    - ItemGroupRef
    - ItemRef
    - TransitionTimingConstraint
    range: MethodDef
  orderNumber:
    name: orderNumber
    description: Indicates the order in which this ItemGroup appears in Metadata displays
      or data entry applications. The OrderNumber attribute provides an ordering on
      the ItemGroupDefs (within StudyEventDef or ItemGroupDef) for use whenever a
      list of ItemGroupDefs is presented to a user. Order of execution is preferably
      defined in a workflow (see Section 3.2.2.1.8, WorkflowDef ) but when used without
      a workflow, may be used the define the order in which data entry forms are presented
      in an application UI.
    comments:
    - 'Optional

      range: positiveInteger

      The StudyEventRefs within a StudyEventGroup must not have duplicate OrderNumber
      values'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: orderNumber
    owner: ItemGroupRef
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
  mandatory:
    name: mandatory
    description: The Mandatory flag indicates that the clinical data for an instance
      of the containing event or ItemGroup would be incomplete without an instance
      of this type of ItemGroup. ODM clinical data files that are incomplete in this
      sense may be considered incomplete for study review and analysis purposes.
    comments:
    - 'Required

      enum values: (Yes | No)

      When the value is Yes, the data for each subject in the study must include a
      StudyEventData element with this StudyEventOID.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: mandatory
    owner: ItemGroupRef
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: YesOrNo
    required: true
  collectionExceptionConditionOID:
    name: collectionExceptionConditionOID
    description: Reference to a ConditionDef If the CollectionExceptionConditionOID
      attribute is provided, the ConditionDef it references describes the circumstances
      under which data for this ItemGroup should not be collected.
    comments:
    - 'Optional

      range: oidref

      The CollectionExceptionConditionOID value must match the OID attribute for a
      ConditionDef in this Study/MetaDataVersion'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: collectionExceptionConditionOID
    owner: ItemGroupRef
    domain_of:
    - StudyEventGroupRef
    - StudyEventRef
    - ItemGroupRef
    - ItemRef
    range: ConditionDef
class_uri: odm:ItemGroupRef

```
</details>