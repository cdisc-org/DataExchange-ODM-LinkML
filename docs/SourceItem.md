# Class: SourceItem

_Provides the information needed to identify the source metadata._




URI: [odm:SourceItem](http://www.cdisc.org/ns/odm/v2.0/SourceItem)


```mermaid
erDiagram
SourceItem {
    nameType name  
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
Resource {
    text type  
    nameType name  
    text attribute  
    text label  
}
Selection {
    text path  
}
Leaf {
    oid ID  
    uriorcurie href  
}
Title {
    text content  
}
Study {
    oid OID  
    nameType studyName  
    nameType protocolName  
    nameType versionID  
    nameType versionName  
    nameType status  
}
MetaDataVersion {
    oid OID  
    nameType name  
}
Description {

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
ItemGroupRef {
    positiveInteger orderNumber  
    YesOrNo mandatory  
}
Alias {
    text context  
    text name  
}
Origin {
    OriginType type  
    OriginSource source  
}
WorkflowRef {

}
Class {
    ItemGroupClass name  
}
CommentDef {
    oid OID  
}
Standard {
    oid OID  
    StandardName name  
    StandardType type  
    StandardPublishingSet publishingSet  
    text version  
    StandardStatus status  
}
ItemDef {
    oid OID  
    nameType name  
    DataType dataType  
    positiveInteger length  
    text displayFormat  
    text variableSet  
}
ValueListRef {

}
CodeListRef {

}
RangeCheck {
    Comparator comparator  
    SoftOrHard softHard  
}
CDISCNotes {

}
ImplementationNotes {

}
CRFCompletionInstructions {

}
Prompt {

}
Question {

}
Definition {

}

SourceItem ||--|o ItemDef : "itemOID"
SourceItem ||--|o ItemGroupDef : "itemGroupOID"
SourceItem ||--|o MetaDataVersion : "metaDataVersionOID"
SourceItem ||--|o Study : "studyOID"
SourceItem ||--|o Leaf : "leafID"
SourceItem ||--}o Resource : "resource"
SourceItem ||--}o Coding : "coding"
Resource ||--}o Selection : "selection"
Leaf ||--|o Title : "title"
Study ||--|o Description : "description"
Study ||--}o MetaDataVersion : "metaDataVersion"
MetaDataVersion ||--|o CommentDef : "commentOID"
MetaDataVersion ||--|o Description : "description"
MetaDataVersion ||--|o Include : "include"
MetaDataVersion ||--|o Standards : "standards"
MetaDataVersion ||--|o AnnotatedCRF : "annotatedCRF"
MetaDataVersion ||--|o SupplementalDoc : "supplementalDoc"
MetaDataVersion ||--}o ValueListDef : "valueListDef"
MetaDataVersion ||--}o WhereClauseDef : "whereClauseDef"
MetaDataVersion ||--|o Protocol : "protocol"
MetaDataVersion ||--}o WorkflowDef : "workflowDef"
MetaDataVersion ||--}o StudyEventGroupDef : "studyEventGroupDef"
MetaDataVersion ||--}o StudyEventDef : "studyEventDef"
MetaDataVersion ||--}o ItemGroupDef : "itemGroupDef"
MetaDataVersion ||--}o ItemDef : "itemDef"
MetaDataVersion ||--}o CodeList : "codeList"
MetaDataVersion ||--}o ConditionDef : "conditionDef"
MetaDataVersion ||--}o MethodDef : "methodDef"
MetaDataVersion ||--}o CommentDef : "commentDef"
MetaDataVersion ||--}o Leaf : "leaf"
Description ||--}o TranslatedText : "translatedText"
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
ItemGroupRef ||--|| ItemGroupDef : "itemGroupOID"
ItemGroupRef ||--|o MethodDef : "methodOID"
ItemGroupRef ||--|o ConditionDef : "collectionExceptionConditionOID"
Origin ||--|o Description : "description"
Origin ||--|o SourceItems : "sourceItems"
Origin ||--}o Coding : "coding"
Origin ||--}o DocumentRef : "documentRef"
WorkflowRef ||--|| WorkflowDef : "workflowOID"
Class ||--}o SubClass : "subClass"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"
Standard ||--|o CommentDef : "commentOID"
ItemDef ||--|o CommentDef : "commentOID"
ItemDef ||--|o Description : "description"
ItemDef ||--|o Definition : "definition"
ItemDef ||--|o Question : "question"
ItemDef ||--|o Prompt : "prompt"
ItemDef ||--|o CRFCompletionInstructions : "cRFCompletionInstructions"
ItemDef ||--|o ImplementationNotes : "implementationNotes"
ItemDef ||--|o CDISCNotes : "cDISCNotes"
ItemDef ||--}o RangeCheck : "rangeCheck"
ItemDef ||--|o CodeListRef : "codeListRef"
ItemDef ||--|o ValueListRef : "valueListRef"
ItemDef ||--}o Coding : "coding"
ItemDef ||--}o Alias : "alias"
ValueListRef ||--|| ValueListDef : "valueListOID"
CodeListRef ||--|| CodeList : "codeListOID"
RangeCheck ||--|o ItemDef : "itemOID"
RangeCheck ||--|o ErrorMessage : "errorMessage"
RangeCheck ||--|o MethodSignature : "methodSignature"
RangeCheck ||--}o FormalExpression : "formalExpression"
RangeCheck ||--}o CheckValue : "checkValue"
CDISCNotes ||--}o TranslatedText : "translatedText"
ImplementationNotes ||--}o TranslatedText : "translatedText"
CRFCompletionInstructions ||--}o TranslatedText : "translatedText"
Prompt ||--}o TranslatedText : "translatedText"
Question ||--}o TranslatedText : "translatedText"
Definition ||--}o TranslatedText : "translatedText"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [itemOID](itemOID.md) | 0..1 <br/> [ItemDef](ItemDef.md) | References the ItemDef that provides the variable metadata. | direct |
| [itemGroupOID](itemGroupOID.md) | 0..1 <br/> [ItemGroupDef](ItemGroupDef.md) | References the ItemGroupDef that provides the ItemGroup or dataset metadata. | direct |
| [metaDataVersionOID](metaDataVersionOID.md) | 0..1 <br/> [MetaDataVersion](MetaDataVersion.md) | References the MetaDataVersion that provides the metadata when referencing an... | direct |
| [studyOID](studyOID.md) | 0..1 <br/> [Study](Study.md) | References the Study that provides the metadata when referencing another ODM ... | direct |
| [leafID](leafID.md) | 0..1 <br/> [Leaf](Leaf.md) | References a leaf element that provides a reference to another ODM document. ... | direct |
| [name](name.md) | 0..1 <br/> [nameType](nameType.md) | Provides a way to connect an argument to a parameter when SourceItems are inp... | direct |
| [resource](resource.md) | 0..* <br/> [Resource](Resource.md) | Resource reference: Describes an external resource used as the source for the... | direct |
| [coding](coding.md) | 0..* <br/> [Coding](Coding.md) | Coding reference: Coding references a symbol from a defined code system. It u... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SourceItems](SourceItems.md) | [sourceItem](sourceItem.md) | range | [SourceItem](SourceItem.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/SourceItem](https://wiki.cdisc.org/display/PUB/SourceItem)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SourceItem |
| native | odm:SourceItem |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SourceItem
description: Provides the information needed to identify the source metadata.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SourceItem
rank: 1000
slots:
- itemOID
- itemGroupOID
- metaDataVersionOID
- studyOID
- leafID
- name
- resource
- coding
slot_usage:
  itemOID:
    name: itemOID
    description: References the ItemDef that provides the variable metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemDef element. The referenced ItemDef element can
      be in the same ODM document or another ODM document.'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
  itemGroupOID:
    name: itemGroupOID
    description: References the ItemGroupDef that provides the ItemGroup or dataset
      metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemGroupDef element. The referenced ItemGroupDef
      element can be in the same ODM document or another ODM document.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID of a MetaDataVersion element. The referenced MetaDataVersion
      element can be in the same ODM document or another ODM document. Must be provided
      if the reference is not to an object within the same MetaDataVersion element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
  studyOID:
    name: studyOID
    description: References the Study that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an Study element. The referenced Study element can be
      in the same ODM document or another ODM document. Must be provided if the reference
      is not to an object within the same Study element.'
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: Study
  leafID:
    name: leafID
    description: References a leaf element that provides a reference to another ODM
      document. This is necessary when the source ItemOID references an ItemDef contained
      in a different ODM document.
    comments:
    - 'Optional

      range: IDREF

      When referencing another ODM document it is necessary to have values for the
      MetaDataVersionOID and StudyOID attributes.'
    domain_of:
    - DocumentRef
    - SourceItem
    range: Leaf
  name:
    name: name
    description: Provides a way to connect an argument to a parameter when SourceItems
      are inputs to methods. It allows the name used in the programming code in the
      method description to make it easier to trace the use of the value.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: nameType
  resource:
    name: resource
    multivalued: true
    domain_of:
    - SourceItem
    range: Resource
    inlined: true
    inlined_as_list: true
  coding:
    name: coding
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
class_uri: odm:SourceItem

```
</details>

### Induced

<details>
```yaml
name: SourceItem
description: Provides the information needed to identify the source metadata.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/SourceItem
rank: 1000
slot_usage:
  itemOID:
    name: itemOID
    description: References the ItemDef that provides the variable metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemDef element. The referenced ItemDef element can
      be in the same ODM document or another ODM document.'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
  itemGroupOID:
    name: itemGroupOID
    description: References the ItemGroupDef that provides the ItemGroup or dataset
      metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemGroupDef element. The referenced ItemGroupDef
      element can be in the same ODM document or another ODM document.'
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID of a MetaDataVersion element. The referenced MetaDataVersion
      element can be in the same ODM document or another ODM document. Must be provided
      if the reference is not to an object within the same MetaDataVersion element.'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
  studyOID:
    name: studyOID
    description: References the Study that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an Study element. The referenced Study element can be
      in the same ODM document or another ODM document. Must be provided if the reference
      is not to an object within the same Study element.'
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: Study
  leafID:
    name: leafID
    description: References a leaf element that provides a reference to another ODM
      document. This is necessary when the source ItemOID references an ItemDef contained
      in a different ODM document.
    comments:
    - 'Optional

      range: IDREF

      When referencing another ODM document it is necessary to have values for the
      MetaDataVersionOID and StudyOID attributes.'
    domain_of:
    - DocumentRef
    - SourceItem
    range: Leaf
  name:
    name: name
    description: Provides a way to connect an argument to a parameter when SourceItems
      are inputs to methods. It allows the name used in the programming code in the
      method description to make it easier to trace the use of the value.
    comments:
    - 'Optional

      range: name'
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: nameType
  resource:
    name: resource
    multivalued: true
    domain_of:
    - SourceItem
    range: Resource
    inlined: true
    inlined_as_list: true
  coding:
    name: coding
    multivalued: true
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
attributes:
  itemOID:
    name: itemOID
    description: References the ItemDef that provides the variable metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemDef element. The referenced ItemDef element can
      be in the same ODM document or another ODM document.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemOID
    owner: SourceItem
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
  itemGroupOID:
    name: itemGroupOID
    description: References the ItemGroupDef that provides the ItemGroup or dataset
      metadata.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an ItemGroupDef element. The referenced ItemGroupDef
      element can be in the same ODM document or another ODM document.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemGroupOID
    owner: SourceItem
    domain_of:
    - ItemGroupRef
    - SourceItem
    - ItemGroupData
    - KeySet
    range: ItemGroupDef
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References the MetaDataVersion that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID of a MetaDataVersion element. The referenced MetaDataVersion
      element can be in the same ODM document or another ODM document. Must be provided
      if the reference is not to an object within the same MetaDataVersion element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: metaDataVersionOID
    owner: SourceItem
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
  studyOID:
    name: studyOID
    description: References the Study that provides the metadata when referencing
      another ODM document.
    comments:
    - 'Optional

      range: oidref

      Must match the OID for an Study element. The referenced Study element can be
      in the same ODM document or another ODM document. Must be provided if the reference
      is not to an object within the same Study element.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyOID
    owner: SourceItem
    domain_of:
    - Include
    - SourceItem
    - AdminData
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: Study
  leafID:
    name: leafID
    description: References a leaf element that provides a reference to another ODM
      document. This is necessary when the source ItemOID references an ItemDef contained
      in a different ODM document.
    comments:
    - 'Optional

      range: IDREF

      When referencing another ODM document it is necessary to have values for the
      MetaDataVersionOID and StudyOID attributes.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: leafID
    owner: SourceItem
    domain_of:
    - DocumentRef
    - SourceItem
    range: Leaf
  name:
    name: name
    description: Provides a way to connect an argument to a parameter when SourceItems
      are inputs to methods. It allows the name used in the programming code in the
      method description to make it easier to trace the use of the value.
    comments:
    - 'Optional

      range: name'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: name
    owner: SourceItem
    domain_of:
    - Alias
    - MetaDataVersion
    - Standard
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Class
    - SubClass
    - SourceItem
    - Resource
    - ItemDef
    - CodeList
    - MethodDef
    - Parameter
    - ReturnValue
    - ConditionDef
    - StudyObjective
    - StudyEndPoint
    - StudyTargetPopulation
    - StudyEstimand
    - Arm
    - Epoch
    - StudyTiming
    - TransitionTimingConstraint
    - AbsoluteTimingConstraint
    - RelativeTimingConstraint
    - DurationTimingConstraint
    - WorkflowDef
    - Transition
    - Branching
    - Criterion
    - Organization
    - Location
    - Query
    range: nameType
  resource:
    name: resource
    description: 'Resource reference: Describes an external resource used as the source
      for the parent ItemGroup or Item.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: resource
    owner: SourceItem
    domain_of:
    - SourceItem
    range: Resource
    inlined: true
    inlined_as_list: true
  coding:
    name: coding
    description: 'Coding reference: Coding references a symbol from a defined code
      system. It uses a code defined in a terminology system to associate semantics
      with a given term, codelist, variable, or group of variables. The presence of
      a Coding element associates a meaning to its parent element. Including multiple
      Coding elements for a given parent indicates synonymous meanings provided by
      different code systems or code system versions.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: coding
    owner: SourceItem
    domain_of:
    - StudyEventGroupDef
    - StudyEventDef
    - ItemGroupDef
    - Origin
    - SourceItems
    - SourceItem
    - ItemDef
    - CodeList
    - CodeListItem
    - StudyIndication
    - StudyIntervention
    - StudyTargetPopulation
    - StudyParameter
    - ParameterValue
    - Criterion
    - Annotation
    range: Coding
    inlined: true
    inlined_as_list: true
class_uri: odm:SourceItem

```
</details>