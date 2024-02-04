# Class: Include

_The Include metadata element allows a reference to a prior metadata version._




URI: [odm:Include](http://www.cdisc.org/ns/odm/v2.0/Include)


```mermaid
erDiagram
Include {
    uriorcurie href  
}
MetaDataVersion {
    oid OID  
    nameType name  
}
Leaf {
    oid ID  
    uriorcurie href  
}
CommentDef {
    oid OID  
}
MethodDef {
    oid OID  
    nameType name  
    MethodType type  
}
ConditionDef {
    oid OID  
    nameType name  
}
CodeList {
    oid OID  
    nameType name  
    CLDataType dataType  
    YesOnly isNonStandard  
}
ItemDef {
    oid OID  
    nameType name  
    DataType dataType  
    positiveInteger length  
    text displayFormat  
    text variableSet  
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
StudyEventDef {
    oid OID  
    nameType name  
    YesOrNo repeating  
    EventType type  
    text category  
}
StudyEventGroupDef {
    oid OID  
    nameType name  
}
WorkflowDef {
    oid OID  
    nameType name  
}
Protocol {

}
WhereClauseDef {
    oid OID  
}
ValueListDef {
    oid OID  
}
SupplementalDoc {

}
AnnotatedCRF {

}
Standards {

}
Description {

}
Study {
    oid OID  
    nameType studyName  
    nameType protocolName  
    nameType versionID  
    nameType versionName  
    nameType status  
}

Include ||--|| Study : "studyOID"
Include ||--|| MetaDataVersion : "metaDataVersionOID"
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
Leaf ||--|o Title : "title"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"
MethodDef ||--|o CommentDef : "commentOID"
MethodDef ||--|o Description : "description"
MethodDef ||--|o MethodSignature : "methodSignature"
MethodDef ||--}o FormalExpression : "formalExpression"
MethodDef ||--}o Alias : "alias"
MethodDef ||--}o DocumentRef : "documentRef"
ConditionDef ||--|o CommentDef : "commentOID"
ConditionDef ||--|o Description : "description"
ConditionDef ||--|o MethodSignature : "methodSignature"
ConditionDef ||--}o FormalExpression : "formalExpression"
ConditionDef ||--}o Alias : "alias"
CodeList ||--|o CommentDef : "commentOID"
CodeList ||--|o Standard : "standardOID"
CodeList ||--|o Description : "description"
CodeList ||--}o CodeListItem : "codeListItem"
CodeList ||--}o Coding : "coding"
CodeList ||--}o Alias : "alias"
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
StudyEventDef ||--|o CommentDef : "commentOID"
StudyEventDef ||--|o Description : "description"
StudyEventDef ||--}o ItemGroupRef : "itemGroupRef"
StudyEventDef ||--|o WorkflowRef : "workflowRef"
StudyEventDef ||--}o Coding : "coding"
StudyEventDef ||--}o Alias : "alias"
StudyEventGroupDef ||--|o Arm : "armOID"
StudyEventGroupDef ||--|o Epoch : "epochOID"
StudyEventGroupDef ||--|o CommentDef : "commentOID"
StudyEventGroupDef ||--|o Description : "description"
StudyEventGroupDef ||--|o WorkflowRef : "workflowRef"
StudyEventGroupDef ||--}o Coding : "coding"
StudyEventGroupDef ||--}o StudyEventGroupRef : "studyEventGroupRef"
StudyEventGroupDef ||--}o StudyEventRef : "studyEventRef"
WorkflowDef ||--|o Description : "description"
WorkflowDef ||--|o WorkflowStart : "workflowStart"
WorkflowDef ||--}o WorkflowEnd : "workflowEnd"
WorkflowDef ||--}o Transition : "transition"
WorkflowDef ||--}o Branching : "branching"
Protocol ||--|o Description : "description"
Protocol ||--|o StudySummary : "studySummary"
Protocol ||--|o StudyStructure : "studyStructure"
Protocol ||--|o TrialPhase : "trialPhase"
Protocol ||--|o StudyTimings : "studyTimings"
Protocol ||--|o StudyIndications : "studyIndications"
Protocol ||--|o StudyInterventions : "studyInterventions"
Protocol ||--|o StudyObjectives : "studyObjectives"
Protocol ||--|o StudyEndPoints : "studyEndPoints"
Protocol ||--|o StudyTargetPopulation : "studyTargetPopulation"
Protocol ||--|o StudyEstimands : "studyEstimands"
Protocol ||--|o InclusionExclusionCriteria : "inclusionExclusionCriteria"
Protocol ||--}o StudyEventGroupRef : "studyEventGroupRef"
Protocol ||--|o WorkflowRef : "workflowRef"
Protocol ||--}o Alias : "alias"
WhereClauseDef ||--|o CommentDef : "commentOID"
WhereClauseDef ||--}o RangeCheck : "rangeCheck"
ValueListDef ||--|o Description : "description"
ValueListDef ||--}o ItemRef : "itemRef"
SupplementalDoc ||--}o DocumentRef : "documentRef"
AnnotatedCRF ||--}o DocumentRef : "documentRef"
Standards ||--}o Standard : "standard"
Description ||--}o TranslatedText : "translatedText"
Study ||--|o Description : "description"
Study ||--}o MetaDataVersion : "metaDataVersion"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [studyOID](studyOID.md) | 1..1 <br/> [Study](Study.md) | References the Study that provides a prior metadata version. This attribute a... | direct |
| [metaDataVersionOID](metaDataVersionOID.md) | 1..1 <br/> [MetaDataVersion](MetaDataVersion.md) | References a prior MetaDataVersion within the Study referenced by the StudyOI... | direct |
| [href](href.md) | 0..1 <br/> [uriorcurie](uriorcurie.md) | Reference to the location where the to be included Study-Metadata definition ... | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetaDataVersion](MetaDataVersion.md) | [include](include.md) | range | [Include](Include.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/Include](https://wiki.cdisc.org/display/PUB/Include)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Include |
| native | odm:Include |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Include
description: The Include metadata element allows a reference to a prior metadata version.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Include
rank: 1000
slots:
- studyOID
- metaDataVersionOID
- href
slot_usage:
  studyOID:
    name: studyOID
    description: References the Study that provides a prior metadata version. This
      attribute allows an Include element to reference a metadata version in another
      study. Thus, it is possible for many studies to share a set of common metadata
      definitions
    comments:
    - 'Required

      range: oidref'
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
    required: true
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References a prior MetaDataVersion within the Study referenced by
      the StudyOID attribute.
    comments:
    - 'Required

      range: oidref'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
    required: true
  href:
    name: href
    description: Reference to the location where the to be included Study-Metadata
      definition can be accessed. The href attribute allows to provide the location
      (as a URL) of the ODM where the to-be-included elements can be retrieved, in
      the case that the combination of the referenced study and metadataversion is
      not present in the same file. The reference can be to a file (e.g., "file:///d:/MyStudies/MyStudy/PriorVersionODM.xml")
      or be an API call (e.g., " https://www.MyCompany.com/MyStudies?StudyOID=MyStudy&MetaDataVersionOID=MV.001
      ").
    comments:
    - 'Optional

      range: URI'
    domain_of:
    - Leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: uriorcurie
class_uri: odm:Include

```
</details>

### Induced

<details>
```yaml
name: Include
description: The Include metadata element allows a reference to a prior metadata version.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/Include
rank: 1000
slot_usage:
  studyOID:
    name: studyOID
    description: References the Study that provides a prior metadata version. This
      attribute allows an Include element to reference a metadata version in another
      study. Thus, it is possible for many studies to share a set of common metadata
      definitions
    comments:
    - 'Required

      range: oidref'
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
    required: true
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References a prior MetaDataVersion within the Study referenced by
      the StudyOID attribute.
    comments:
    - 'Required

      range: oidref'
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
    required: true
  href:
    name: href
    description: Reference to the location where the to be included Study-Metadata
      definition can be accessed. The href attribute allows to provide the location
      (as a URL) of the ODM where the to-be-included elements can be retrieved, in
      the case that the combination of the referenced study and metadataversion is
      not present in the same file. The reference can be to a file (e.g., "file:///d:/MyStudies/MyStudy/PriorVersionODM.xml")
      or be an API call (e.g., " https://www.MyCompany.com/MyStudies?StudyOID=MyStudy&MetaDataVersionOID=MV.001
      ").
    comments:
    - 'Optional

      range: URI'
    domain_of:
    - Leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: uriorcurie
attributes:
  studyOID:
    name: studyOID
    description: References the Study that provides a prior metadata version. This
      attribute allows an Include element to reference a metadata version in another
      study. Thus, it is possible for many studies to share a set of common metadata
      definitions
    comments:
    - 'Required

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: studyOID
    owner: Include
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
    required: true
  metaDataVersionOID:
    name: metaDataVersionOID
    description: References a prior MetaDataVersion within the Study referenced by
      the StudyOID attribute.
    comments:
    - 'Required

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: metaDataVersionOID
    owner: Include
    domain_of:
    - Include
    - SourceItem
    - MetaDataVersionRef
    - ReferenceData
    - ClinicalData
    - Association
    - KeySet
    range: MetaDataVersion
    required: true
  href:
    name: href
    description: Reference to the location where the to be included Study-Metadata
      definition can be accessed. The href attribute allows to provide the location
      (as a URL) of the ODM where the to-be-included elements can be retrieved, in
      the case that the combination of the referenced study and metadataversion is
      not present in the same file. The reference can be to a file (e.g., "file:///d:/MyStudies/MyStudy/PriorVersionODM.xml")
      or be an API call (e.g., " https://www.MyCompany.com/MyStudies?StudyOID=MyStudy&MetaDataVersionOID=MV.001
      ").
    comments:
    - 'Optional

      range: URI'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: href
    owner: Include
    domain_of:
    - Leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: uriorcurie
class_uri: odm:Include

```
</details>