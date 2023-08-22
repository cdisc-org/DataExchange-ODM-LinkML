# CDISC Operational Data Model v2

ODM is a vendor-neutral, platform-independent format for exchanging and archiving clinical and translational research data, along with their associated metadata, administrative data, reference data, and audit information.

URI: http://www.cdisc.org/ns/odm/v2.0

Name: odm



## Schema Diagram
```mermaid 
erDiagram
ODMFileMetadata {
    FileType FileTypeRef  
    Granularity GranularityRef  
    Context ContextRef  
    oid FileOID  
    datetime CreationDateTime  
    oidref PriorFileOID  
    datetime AsOfDateTime  
    ODMVersion ODMVersionRef  
    text Originator  
    text SourceSystem  
    text SourceSystemVersion  
}
Association {
    oidref StudyOID  
    oidref MetaDataVersionOID  
}
Annotation {
    positiveInteger SeqNum  
    TransactionType TransactionTypeRef  
    oid ID  
}
KeySet {
    oidref StudyOID  
    subjectKey SubjectKey  
    oidref MetaDataVersionOID  
    oidref StudyEventOID  
    repeatKey StudyEventRepeatKey  
    oidref ItemGroupOID  
    repeatKey ItemGroupRepeatKey  
    oidref ItemOID  
}
ClinicalData {
    oidref StudyOID  
    oidref MetaDataVersionOID  
}
Signature {
    oid ID  
}
AuditRecord {
    EditPointType EditPoint  
    YesOrNo UsedMethod  
}
Query {
    oid OID  
    QuerySourceType Source  
    text Target  
    QueryType Type  
    QueryStateType State  
    datetime LastUpdateDatetime  
    name Name  
}
ItemGroupData {
    oidref ItemGroupOID  
    repeatKey ItemGroupRepeatKey  
    TransactionType TransactionTypeRef  
    positiveInteger ItemGroupDataSeq  
}
SubjectData {
    subjectKey SubjectKey  
    TransactionType TransactionTypeRef  
}
ReferenceData {
    oidref StudyOID  
    oidref MetaDataVersionOID  
}
AdminData {
    oidref StudyOID  
}
SignatureDef {
    oid OID  
    SignMethod Methodology  
}
Location {
    oid OID  
    name Name  
    text Role  
    oidref OrganizationOID  
}
Organization {
    oid OID  
    name Name  
    text Role  
    OrganizationType Type  
    oidref LocationOID  
    oidref PartOfOrganizationOID  
}
User {
    oid OID  
    UserType UserTypeRef  
    oidref OrganizationOID  
    oidref LocationOID  
}
Study {
    oid OID  
    name StudyName  
    name ProtocolName  
    name VersionID  
    name VersionName  
    name Status  
}
MetaDataVersion {
    oid OID  
    name Name  
    oidref CommentOID  
}
Description {

}

ODMFileMetadata ||--|o Description : "DescriptionRef"
ODMFileMetadata ||--}o Study : "StudyRef"
ODMFileMetadata ||--}o AdminData : "AdminDataRef"
ODMFileMetadata ||--}o ReferenceData : "ReferenceDataRef"
ODMFileMetadata ||--}o ClinicalData : "ClinicalDataRef"
ODMFileMetadata ||--}o Association : "AssociationRef"
Association ||--|o KeySet : "KeySetRef"
Association ||--|o Annotation : "AnnotationRef"
Annotation ||--|o Comment : "CommentRef"
Annotation ||--}o Coding : "CodingRef"
Annotation ||--}o Flag : "FlagRef"
ClinicalData ||--}o SubjectData : "SubjectDataRef"
ClinicalData ||--}o ItemGroupData : "ItemGroupDataRef"
ClinicalData ||--}o Query : "QueryRef"
ClinicalData ||--|o AuditRecord : "AuditRecordRef"
ClinicalData ||--|o Signature : "SignatureRefRef"
ClinicalData ||--|o Annotation : "AnnotationRef"
Signature ||--|o UserRef : "UserRefRef"
Signature ||--|o LocationRef : "LocationRefRef"
Signature ||--|o SignatureRef : "SignatureRefRef"
Signature ||--|o DateTimeStamp : "DateTimeStampRef"
AuditRecord ||--|o UserRef : "UserRefRef"
AuditRecord ||--|o LocationRef : "LocationRefRef"
AuditRecord ||--|o DateTimeStamp : "DateTimeStampRef"
AuditRecord ||--|o ReasonForChange : "ReasonForChangeRef"
AuditRecord ||--|o SourceID : "SourceIDRef"
Query ||--|o Value : "ValueRef"
Query ||--}o AuditRecord : "AuditRecordRef"
ItemGroupData ||--}o Query : "QueryRef"
ItemGroupData ||--}o ItemGroupData : "ItemGroupDataRef"
ItemGroupData ||--}o ItemData : "ItemDataRef"
ItemGroupData ||--|o AuditRecord : "AuditRecordRef"
ItemGroupData ||--|o Signature : "SignatureRefRef"
ItemGroupData ||--|o Annotation : "AnnotationRef"
SubjectData ||--|o InvestigatorRef : "InvestigatorRefRef"
SubjectData ||--|o SiteRef : "SiteRefRef"
SubjectData ||--}o StudyEventData : "StudyEventDataRef"
SubjectData ||--}o Query : "QueryRef"
SubjectData ||--|o AuditRecord : "AuditRecordRef"
SubjectData ||--|o Signature : "SignatureRefRef"
SubjectData ||--|o Annotation : "AnnotationRef"
ReferenceData ||--}o ItemGroupData : "ItemGroupDataRef"
ReferenceData ||--|o AuditRecord : "AuditRecordRef"
ReferenceData ||--|o Signature : "SignatureRefRef"
ReferenceData ||--|o Annotation : "AnnotationRef"
AdminData ||--}o User : "UserRefRef"
AdminData ||--}o Organization : "OrganizationRef"
AdminData ||--}o Location : "LocationRefRef"
AdminData ||--}o SignatureDef : "SignatureDefRef"
SignatureDef ||--|o Meaning : "MeaningRef"
SignatureDef ||--|o LegalReason : "LegalReasonRef"
Location ||--|o Description : "DescriptionRef"
Location ||--}o MetaDataVersionRef : "MetaDataVersionRefRef"
Location ||--}o Address : "AddressRef"
Location ||--}o Telecom : "TelecomRef"
Location ||--}o Query : "QueryRef"
Organization ||--|o Description : "DescriptionRef"
Organization ||--}o Address : "AddressRef"
Organization ||--}o Telecom : "TelecomRef"
User ||--|o UserName : "UserNameRef"
User ||--|o Prefix : "PrefixRef"
User ||--|o Suffix : "SuffixRef"
User ||--|o FullName : "FullNameRef"
User ||--|o GivenName : "GivenNameRef"
User ||--|o FamilyName : "FamilyNameRef"
User ||--|o Image : "ImageRef"
User ||--}o Address : "AddressRef"
User ||--}o Telecom : "TelecomRef"
Study ||--|o Description : "DescriptionRef"
Study ||--}o MetaDataVersion : "MetaDataVersionRefRef"
MetaDataVersion ||--|o Description : "DescriptionRef"
MetaDataVersion ||--|o Include : "IncludeRef"
MetaDataVersion ||--|o Standards : "StandardsRef"
MetaDataVersion ||--|o AnnotatedCRF : "AnnotatedCRFRef"
MetaDataVersion ||--|o SupplementalDoc : "SupplementalDocRef"
MetaDataVersion ||--}o ValueListDef : "ValueListDefRef"
MetaDataVersion ||--}o WhereClauseDef : "WhereClauseDefRef"
MetaDataVersion ||--|o Protocol : "ProtocolRef"
MetaDataVersion ||--}o WorkflowDef : "WorkflowDefRef"
MetaDataVersion ||--}o StudyEventGroupDef : "StudyEventGroupDefRef"
MetaDataVersion ||--}o StudyEventDef : "StudyEventDefRef"
MetaDataVersion ||--}o ItemGroupDef : "ItemGroupDefRef"
MetaDataVersion ||--}o ItemDef : "ItemDefRef"
MetaDataVersion ||--}o CodeList : "CodeListRefRef"
MetaDataVersion ||--}o ConditionDef : "ConditionDefRef"
MetaDataVersion ||--}o MethodDef : "MethodDefRef"
MetaDataVersion ||--}o CommentDef : "CommentDefRef"
MetaDataVersion ||--}o Leaf : "LeafRef"
Description ||--}o TranslatedText : "TranslatedTextRef"

```


## Classes
_Classes provide templates for organizing data. Data objects instantiate classes in the schema. Each class has a set of slots (aka fields, attributes) that are applicable to it. See [LinkML documentation](https://linkml.io/linkml/schemas/models.html#classes) for more information._

| Class | Description |
| --- | --- |
| [Alias](Alias.md) | An Alias provides an additional name for an element. The Context attribute sp... |
| [Description](Description.md) | A free-text description of the containing metadata component, unless restrict... |
| [TranslatedText](TranslatedText.md) | Human-readable text that is appropriate for a particular language. Translated... |
| [Study](Study.md) | This element collects static structural information about an individual study... |
| [MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. ... |
| [DocumentRef](DocumentRef.md) | Links to a leaf element with the location of the document. |
| [PDFPageRef](PDFPageRef.md) | This element is the container for CRF page references. |
| [Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |
| [Title](Title.md) | Text with the label for the document or dataset. |
| [Include](Include.md) | The Include metadata element allows a reference to a prior metadata version. |
| [Standards](Standards.md) | The Standards element provides a container for the list of Standard elements ... |
| [Standard](Standard.md) | The Standard element describes each standard used within the MetaDataVersion ... |
| [AnnotatedCRF](AnnotatedCRF.md) | An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document ... |
| [SupplementalDoc](SupplementalDoc.md) | Supplemental data definitions |
| [ValueListDef](ValueListDef.md) | The following table specifies the XML structure for valuelist metadata. The V... |
| [WhereClauseRef](WhereClauseRef.md) | The WhereClauseRef references the WhereClauseDef element that describes the c... |
| [WhereClauseDef](WhereClauseDef.md) | The WhereClauseDef element specifies a condition. |
| [StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific v... |
| [StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller ... |
| [StudyEventRef](StudyEventRef.md) | This element references a StudyEventDef as it occurs within a specific versio... |
| [StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data ... |
| [ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyE... |
| [ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur... |
| [Class](Class.md) | The Class element identifies which predefined Class within the model applies ... |
| [SubClass](SubClass.md) | This element contains SubClass definitions. |
| [ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The li... |
| [Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or Ite... |
| [SourceItems](SourceItems.md) | Identifies source items as needed to support automated data capture and end-t... |
| [SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |
| [Resource](Resource.md) | Describes an external resource used as the source for the parent ItemGroup or... |
| [Selection](Selection.md) | Template for machine-readable/executable expression for retrieving the data o... |
| [ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item prope... |
| [Question](Question.md) | A label shown to a human user when prompted to provide data for an item on pa... |
| [Definition](Definition.md) | Definition of the item. |
| [Prompt](Prompt.md) | A prompt text shown to a human user when prompted to provide data for an item... |
| [CRFCompletionInstructions](CRFCompletionInstructions.md) | Instructions for the clinical site on how to enter collected information on t... |
| [ImplementationNotes](ImplementationNotes.md) | Further information, such as rationale and implementation instructions, on ho... |
| [CDISCNotes](CDISCNotes.md) | Explanatory text for the variable. |
| [RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item. It repr... |
| [CheckValue](CheckValue.md) | A comparison value used in a range check. |
| [ErrorMessage](ErrorMessage.md) | Error message provided to user when the range check fails. |
| [CodeListRef](CodeListRef.md) | A reference to a CodeList definition. |
| [ValueListRef](ValueListRef.md) | The ValueListRef element is the OID of the ValueListDef that contains the val... |
| [CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a referen... |
| [CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display va... |
| [Decode](Decode.md) | The displayed value relating to the CodeListItem/@CodedValue. This is often a... |
| [MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of oth... |
| [MethodSignature](MethodSignature.md) | A MethodSignature defines the parameters and return values for a method. The ... |
| [Parameter](Parameter.md) | The Parameter element represents a method parameter used as part of a MethodS... |
| [ReturnValue](ReturnValue.md) | The ReturnValue element represents a return value used as part of a MethodSig... |
| [ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition. |
| [FormalExpression](FormalExpression.md) | A FormalExpression used within a ConditionDef or a RangeCheck must evaluate t... |
| [Code](Code.md) | Contains the source code that represents a FormalExpression in a given Contex... |
| [ExternalCodeLib](ExternalCodeLib.md) | The ExternalCodeLib element references a FormalExpression in an external code... |
| [CommentDef](CommentDef.md) | The Comment element allows referencing short comments self-contained in the X... |
| [Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a ... |
| [StudyStructure](StudyStructure.md) | The StudyStructure element describes the general structure of a clinical stud... |
| [TrialPhase](TrialPhase.md) | The TrialPhase element designates the phase of the study in the clinical tria... |
| [StudyIndications](StudyIndications.md) | StudyIndications is a container element for individual StudyIndication elemen... |
| [StudyIndication](StudyIndication.md) | This element describes a study indication (e.g., condition, disease) for the ... |
| [StudyInterventions](StudyInterventions.md) | The StudyInterventions element is a container element for individual StudyInt... |
| [StudyIntervention](StudyIntervention.md) | This element describes a study intervention (e.g., medication, treatment, the... |
| [StudyObjectives](StudyObjectives.md) | The StudyObjectives is a container element for individual StudyObjective elem... |
| [StudyObjective](StudyObjective.md) | The reason for performing a study in terms of the scientific questions to be ... |
| [StudyEndPointRef](StudyEndPointRef.md) | Go to start of metadata |
| [StudyEndPoints](StudyEndPoints.md) | The StudyEndPoints element is a container element for individual StudyEndPoin... |
| [StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistical... |
| [StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical ... |
| [StudyEstimands](StudyEstimands.md) | StudyEstimands is a container element for individual StudyEstimand elements. |
| [StudyEstimand](StudyEstimand.md) | A precise description of the treatment effect reflecting the clinical questio... |
| [InclusionExclusionCriteria](InclusionExclusionCriteria.md) | The InclusionExclusionCriteria element can contain 2 lists of Criterion eleme... |
| [InclusionCriteria](InclusionCriteria.md) | The InclusionCriteria is a container element for Criterion elements describin... |
| [ExclusionCriteria](ExclusionCriteria.md) | The ExclusionCriteria is a container element for Criterion elements describin... |
| [StudyTargetPopulationRef](StudyTargetPopulationRef.md) | The StudyTargetPopulationRef references a StudyTargetPopulation to which the ... |
| [StudyInterventionRef](StudyInterventionRef.md) | The StudyInterventionRef references an intervention that is taken as the trea... |
| [IntercurrentEvent](IntercurrentEvent.md) | The IntercurrentEvent element describes an intercurrent event for an estimand... |
| [SummaryMeasure](SummaryMeasure.md) | The SummaryMeasure element describes a summary measure for an estimand (e.g.,... |
| [Arm](Arm.md) | An Arm element provides the declaration of a study arm. Arms do not have any ... |
| [Epoch](Epoch.md) | The planned period of subjects' participation in the trial is divided into se... |
| [WorkflowRef](WorkflowRef.md) | The WorkflowRef references a workflow definition |
| [StudySummary](StudySummary.md) | The StudyParameter element allows to provide a set of study design parameters... |
| [StudyParameter](StudyParameter.md) | A StudyParameter defines a study design parameter for which the value or valu... |
| [ParameterValue](ParameterValue.md) | This element contains the value of the study parameter as text content. |
| [StudyTimings](StudyTimings.md) | The StudyTimings element is a container element for individual StudyTiming el... |
| [StudyTiming](StudyTiming.md) | The StudyTiming element defines a timing constraint within the study, which c... |
| [TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a trans... |
| [AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, rep... |
| [RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint b... |
| [DurationTimingConstraint](DurationTimingConstraint.md) | The DurationTimingConstraint constrains the duration of an activity represent... |
| [WorkflowDef](WorkflowDef.md) | A WorkflowDef defines an automated workflow for a study. |
| [WorkflowStart](WorkflowStart.md) | WorkflowStart references a structural element that begins the automated workf... |
| [Transition](Transition.md) | A Transition defines a link between 2 structural elements in a workflow. When... |
| [Branching](Branching.md) | This element describes the branching in a workflow from a source (start) stru... |
| [TargetTransition](TargetTransition.md) | TargetTransition provides a reference to a Transition element that is the tar... |
| [DefaultTransition](DefaultTransition.md) | The DefaultTransition references the Transition that needs to be executed whe... |
| [WorkflowEnd](WorkflowEnd.md) | A WorkflowEnd references a structural element with which the workflows ends. |
| [Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depen... |
| [AdminData](AdminData.md) | Administrative information about users, locations, organizations, and electro... |
| [User](User.md) | Information about a specific user of a clinical data collection or data manag... |
| [UserName](UserName.md) | The user's login identification in the sender's system. |
| [Prefix](Prefix.md) | Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhi... |
| [Suffix](Suffix.md) | This element may include credentials, or suffixes (e.g., Jr., III). |
| [FullName](FullName.md) | The user's full formal name. May be a combination of Prefix, GivenName, Famil... |
| [GivenName](GivenName.md) | The user's initial given name or all given names. |
| [FamilyName](FamilyName.md) | The user's surname (family name). |
| [Image](Image.md) | A visual depiction of the user. |
| [Organization](Organization.md) | An organization can reference a parent organization. Users may be associated ... |
| [Location](Location.md) | A physical location associated with data collection and/or treatment of subje... |
| [Address](Address.md) | The postal address for a user, location, or organization. |
| [Telecom](Telecom.md) | The telecommunication contacts points of a user, a location, or an organizati... |
| [StreetName](StreetName.md) | The street name part of a user's postal address. |
| [HouseNumber](HouseNumber.md) | The house number part of a user's postal address. |
| [City](City.md) | The city name part of a user's postal address. |
| [StateProv](StateProv.md) | The state or province name part of a user's postal address. |
| [Country](Country.md) | The country name part of a user's postal address. For CDISC SDTM or trial reg... |
| [PostalCode](PostalCode.md) | The postal code part of a user's postal address. |
| [GeoPosition](GeoPosition.md) | The geographical position using the World Geodetic System WGS84. |
| [OtherText](OtherText.md) | Any other text needed as part of a user's postal address. |
| [MetaDataVersionRef](MetaDataVersionRef.md) | A reference to a MetaDataVersion used at the containing Location. The Effecti... |
| [SignatureDef](SignatureDef.md) | Provides Metadata for signatures included in the /ODM/ClinicalData. |
| [Meaning](Meaning.md) | A short name or description for this signature. It should reflect the context... |
| [LegalReason](LegalReason.md) | The responsibility statement associated with a signature (e.g., "The signer a... |
| [ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data. For ex... |
| [ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects. |
| [SubjectData](SubjectData.md) | Clinical data for a single subject. |
| [SiteRef](SiteRef.md) | Provides a reference to the site that the SubjectData record is associated wi... |
| [InvestigatorRef](InvestigatorRef.md) | Provides a reference to the user who created the SubjectData record in the so... |
| [StudyEventData](StudyEventData.md) | Clinical data for a study event (visit). The model supports repeating study e... |
| [ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaData... |
| [ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an ite... |
| [AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or m... |
| [UserRef](UserRef.md) | A reference to information about a specific user of a clinical data collectio... |
| [LocationRef](LocationRef.md) | A reference to the user's physical location. |
| [DateTimeStamp](DateTimeStamp.md) | Date and time when an action was performed. |
| [ReasonForChange](ReasonForChange.md) | A user-supplied reason for a data change. |
| [SourceID](SourceID.md) | Information that identifies the source of the data within an originating syst... |
| [Signature](Signature.md) | An electronic signature applies to a collection of clinical data. This indica... |
| [SignatureRef](SignatureRef.md) | A reference to the signature meaning. |
| [Association](Association.md) | An association permits an annotation to be placed on an ordered pair of entit... |
| [KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event)... |
| [Annotation](Annotation.md) | A general note about clinical data. If an annotation has both a comment and f... |
| [Comment](Comment.md) | A free-text (uninterpreted) comment about clinical data. The comment may have... |
| [Flag](Flag.md) | A machine-processable annotation. |
| [FlagValue](FlagValue.md) | The value of the flag. The meaning of this value is typically dependent on th... |
| [FlagType](FlagType.md) | The type of flag. This determines the purpose and semantics of the flag. |
| [Coding](Coding.md) | Coding references a symbol from a defined code system. It uses a code defined... |
| [Query](Query.md) | The Query element represents a request for clarification on a data item colle... |
| [Value](Value.md) | The data collected for an item. This data is represented according to DataTyp... |
| [ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents. The ODM element is the top-level (root) eleme... |


## Slots
_Slots (aka attributes, fields, columns, properties) can be associated with classes to specify what fields instances of that class can have. Slots operate the same way as “fields” in traditional object languages and the same ways as “columns” in spreadsheets and relational databases. See LinkML documentation [here](https://linkml.io/linkml/schemas/models.html#slots) and [here](https://linkml.io/linkml/schemas/slots.html) for more information._
 
| Slot | Description |
| --- | --- |
| [IsNull](IsNull.md) | Flag specifying that an item's value is to be set to null. In the interest of... |
| [Mandatory](Mandatory.md) | Indicator of whether this StudyEventGroup must appear in the study clinical d... |
| [Role](Role.md) | The Role for the referenced ItemDef. The Role attribute provides a single rol... |
| [Longitude](Longitude.md) | Longitude component of geoposition coordinates in decimal degrees. May requir... |
| [OID](OID.md) | Unique identifier of the version within the XML document. |
| [leafID](leafID.md) | References a leaf element that provides a reference to another ODM document. ... |
| [CodeRef](CodeRef.md) | A string pattern that identifies a concept as defined by the code system. |
| [SignatureOID](SignatureOID.md) | Reference to the SignatureDef . |
| [FileOID](FileOID.md) | A unique identifier for this file. |
| [SystemVersion](SystemVersion.md) | Identifies the version of the code system |
| [ContextRef](ContextRef.md) | Identifies applicable domain or scope of the mapping. |
| [TitleRef](TitleRef.md) | Text with the label for the document or dataset. |
| [PriorFileOID](PriorFileOID.md) | Reference to the previous file (if any) in a series. |
| [Altitude](Altitude.md) | Height above sea level in meters. |
| [MimeType](MimeType.md) | Media type of the image |
| [TransactionTypeRef](TransactionTypeRef.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... |
| [EndConditionOID](EndConditionOID.md) | The EndConditionOID references a ConditionDef defining the condition under wh... |
| [Repeating](Repeating.md) | The Repeating flag indicates when this type of study event can occur repeated... |
| [Attribute](Attribute.md) | Field provided by the Name attribute where the data or information can be obt... |
| [DatasetName](DatasetName.md) | Name of a file containing the ItemGroupData for this ItemGroupDef. The name a... |
| [Level](Level.md) | Defined level for the Study Objective |
| [Length](Length.md) | The Length attribute is optional when DataType is text, string, |
| [PartOfOrganizationOID](PartOfOrganizationOID.md) | Reference to a parent organization. |
| [Latitude](Latitude.md) | Latitude component of geoposition coordinate in decimal degrees degrees. May ... |
| [StudyEventRepeatKey](StudyEventRepeatKey.md) | A key used to distinguish between repeats of the same type of study event for... |
| [SourceOID](SourceOID.md) | References the definition of the source structural element for the transition... |
| [Target](Target.md) | Element upon which the Query is raised. The parent element is the Target when... |
| [ShortName](ShortName.md) | Short name or code for the parameter. |
| [ArmOID](ArmOID.md) | Reference to an Arm element defined in the study. |
| [ProtocolName](ProtocolName.md) | Protocol identifier or protocol number assigned to the study. It is used by t... |
| [Source](Source.md) | Indicates the party responsible for the data's origin type. |
| [ItemGroupRepeatKey](ItemGroupRepeatKey.md) | A key used to distinguish between repeats of the same type of item group. |
| [Purpose](Purpose.md) | Purpose of the ItemGroup. |
| [SoftHard](SoftHard.md) | Type of range check. Soft indicates that a warning occurs when the RangeCheck... |
| [UserOID](UserOID.md) | Reference to a User definition. |
| [Name](Name.md) | General observation Sub Class. |
| [ItemGroupOID](ItemGroupOID.md) | Reference to the ItemGroupDef . |
| [CommentOID](CommentOID.md) | The Comment identifier that this value refers to. Needed when the WhereClause... |
| [DurationTarget](DurationTarget.md) | Constrains the duration of an activity represented by a Study, Epoch, StudyEv... |
| [Term](Term.md) | Longer name. Provides the full name of the parameter. |
| [DataTypeRef](DataTypeRef.md) | The DataType attribute specifies how the corresponding value |
| [StudyEventOID](StudyEventOID.md) | Reference to the StudyEventDef . |
| [Label](Label.md) | Used to link the value to a named MethodDef parameter. |
| [EndOID](EndOID.md) | Reference to the definition of the structural element that ends the workflow.... |
| [SponsorOrSite](SponsorOrSite.md) | Source of the comment. |
| [Core](Core.md) | CDASH, ADaM, SDTM, and SEND Core designations. |
| [EditPoint](EditPoint.md) | Identifies the phase of data processing in which update action occurred. |
| [StructuralElementOID](StructuralElementOID.md) | OID of a structural element such as a Study, Epoch, StudyEventGroup, StudyEve... |
| [SubjectKey](SubjectKey.md) | Unique identifier for the Subject. |
| [UserTypeRef](UserTypeRef.md) | User's role in the study. |
| [SourceSystemVersion](SourceSystemVersion.md) | The version of the "SourceSystem" above. |
| [StudyTargetPopulationOID](StudyTargetPopulationOID.md) |  |
| [Status](Status.md) | Status of Standard. |
| [StudyEventGroupOID](StudyEventGroupOID.md) | Reference to the StudyEventGroupDef . |
| [State](State.md) | Status of the Query |
| [IsReferenceData](IsReferenceData.md) | Specifies whether this ItemGroupDef is used for non-subject data. |
| [DefinitionRef](DefinitionRef.md) | A free-text definition of the parameter |
| [GranularityRef](GranularityRef.md) | Granularity is intended to give the sender a shorthand way to Describes the s... |
| [LastPage](LastPage.md) | Last page in a range of pages. |
| [ConditionOID](ConditionOID.md) | Reference to a ConditionDef defining the condition under which the transition... |
| [SeqNum](SeqNum.md) | When more than 1 Value element exists this attribute uniquely identifies each... |
| [HasNoData](HasNoData.md) | Used to indicate that an ItemGroupDef has no data. May be used at sponsor's d... |
| [UnitsItemOID](UnitsItemOID.md) | Reference to a sibling ItemRef element that represents the unit specification... |
| [System](System.md) | Identifies the code system that defines the code. If the code is taken from a... |
| [ODMVersionRef](ODMVersionRef.md) | The version of the ODM standard used. |
| [Originator](Originator.md) | The organization that generated the ODM file. |
| [PreSpecifiedValue](PreSpecifiedValue.md) | Prefill value or a default value for a field that is automatically populated. |
| [CollectionExceptionConditionOID](CollectionExceptionConditionOID.md) | Reference to a ConditionDef |
| [TimepointTarget](TimepointTarget.md) | The planned time between the 2 activities defined by the transition in the wo... |
| [StartOID](StartOID.md) | Reference to the definition of the structural element that starts the workflo... |
| [language](language.md) | language context for internationalisation and localisation |
| [WhereClauseOID](WhereClauseOID.md) | Reference to the unique ID of a WhereClauseDef element |
| [PageRefs](PageRefs.md) | List of PDF pages separated by a space. |
| [KeySequence](KeySequence.md) | Indicates that this item is a key for the enclosing element. It also provides... |
| [Path](Path.md) | Provides the machine-executable instruction or template for it to obtain the ... |
| [SequenceNumber](SequenceNumber.md) | Order of the Epoch |
| [ItemGroupDataSeq](ItemGroupDataSeq.md) | Unique sequence # for each ItemGroupData child element (record) in the contai... |
| [href](href.md) | URL that can be used to identify the location of a document or dataset file r... |
| [Library](Library.md) | The name of the external library containing the FormalExpression. |
| [TimepointPreWindow](TimepointPreWindow.md) | Specifies the amount of time prior to the TimepointTarget, the time between t... |
| [Version](Version.md) | Version of Standard. |
| [PredecessorOID](PredecessorOID.md) | Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that occurs immed... |
| [ref](ref.md) | Reference to a local instance (e.g. file) of the external library containing ... |
| [OrganizationOID](OrganizationOID.md) | Reference to an Organization elment. |
| [Type](Type.md) | Type of page for page references indicated in the PageRefs attribute. |
| [VersionName](VersionName.md) | Short descriptive label for the version of the study, e.g. "Initial go live" ... |
| [RoleCodeListOID](RoleCodeListOID.md) | Reference to a CodeList that defines the allowable values of Role for the Stu... |
| [TelecomType](TelecomType.md) |  |
| [MetaDataVersionOID](MetaDataVersionOID.md) | References a prior MetaDataVersion within the Study referenced by the StudyOI... |
| [TimepointPostWindow](TimepointPostWindow.md) | Specifies the amount of time after the TimepointTarget, the time between the ... |
| [RepeatingLimit](RepeatingLimit.md) | Maximum number of repeats. |
| [FirstPage](FirstPage.md) | First page in a range of pages. |
| [StartConditionOID](StartConditionOID.md) | The StartConditionOID references a ConditionDef specifying a condition that m... |
| [ID](ID.md) | Unique identifier for the leaf that is referenced. |
| [Methodology](Methodology.md) | Defines the type of electronic signature, including the meaning as required b... |
| [SuccessorOID](SuccessorOID.md) | Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs immedi... |
| [EffectiveDate](EffectiveDate.md) | Datetime stamp when this MetaDataVersion was published at this location. |
| [IsNonStandard](IsNonStandard.md) | Required for ADaM, SDTM, or SEND if StandardOID is not provided. |
| [LastUpdateDatetime](LastUpdateDatetime.md) | When was this Query updated? Will correspond to the creation date or the last... |
| [StudyOID](StudyOID.md) | References the Study that provides a prior metadata version. This attribute a... |
| [CodeListOID](CodeListOID.md) | Reference to the CodeList definition that provides the allowable values for I... |
| [Category](Category.md) | The Category attribute is typically used to indicate the study phase appropri... |
| [DurationPreWindow](DurationPreWindow.md) | Defines the amount of time by which the targetted duration may be reduced. |
| [StudyEndPointOID](StudyEndPointOID.md) | Reference to the StudyEndPoint . |
| [Dictionary](Dictionary.md) |  |
| [ValueRef](ValueRef.md) | Human-readable designation of the trial phase. |
| [Rank](Rank.md) | Numeric significance of the CodeListItem relative to others in the CodeList. ... |
| [PublishingSet](PublishingSet.md) | Set of published files of Standard when Type="CT" (e.g. SDTM, ADaM, SEND, CDA... |
| [UsedMethod](UsedMethod.md) | Indicates that the action was made by the system rather than a data entry for... |
| [TransitionOID](TransitionOID.md) | References the workflow Transition on which the timing constraint must be exe... |
| [Structure](Structure.md) | Description of the level of detail represented by individual records in the I... |
| [LeafID](LeafID.md) | Unique identifier for the Leaf element with the document location. |
| [LocationOID](LocationOID.md) | Reference to a Location element. |
| [ComparatorRef](ComparatorRef.md) | Comparison operator used to compare the item and value(s). |
| [CreationDateTime](CreationDateTime.md) | Time of creation of the file containing the document. |
| [ExtendedValue](ExtendedValue.md) |  |
| [TimepointRelativeTarget](TimepointRelativeTarget.md) | The relative timing between two activities or groups of activities. |
| [TargetTransitionOID](TargetTransitionOID.md) | Reference to the Transition that is one of the targets of the branching. |
| [VersionID](VersionID.md) | Identifier for the specific version of the study in the source system that th... |
| [WorkflowOID](WorkflowOID.md) | Reference to a WorfkflowDef |
| [AsOfDateTime](AsOfDateTime.md) | The date/time at which the source database was queried in order to create thi... |
| [SourceSystem](SourceSystem.md) | The computer system or database management system that is the source of the i... |
| [DisplayFormat](DisplayFormat.md) | Display format supports data visualization of numeric float and date values. |
| [StandardOID](StandardOID.md) | Reference to a Standard element. |
| [OrderNumber](OrderNumber.md) | Indicates the order in which this StudyEventGroup appears in Metadata display... |
| [ArchiveLocationID](ArchiveLocationID.md) | Reference to the unique ID of a leaf element that provides the actual locatio... |
| [TargetOID](TargetOID.md) | References the definition of the target structural element for the transition... |
| [ParentClass](ParentClass.md) | Parent class of the Sub Class |
| [Method](Method.md) | The name of the method or function that contains the FormalExpression code. |
| [ImageFileName](ImageFileName.md) | The file name of or file path to the picture |
| [ItemOID](ItemOID.md) | Reference to the ItemDef . |
| [SystemName](SystemName.md) | Human readable name for the code system. |
| [Other](Other.md) | Flag to indicate that the Item represents "other" content added to an ItemGro... |
| [StudyName](StudyName.md) | Sponsoring organization's internal name for the study. If no internal name is... |
| [StudyInterventionOID](StudyInterventionOID.md) | Reference to a StudyIntervention |
| [VariableSet](VariableSet.md) | ADaM variable set, e.g. Dose, Analysis Parameter, Treatment Timing. |
| [Repeat](Repeat.md) | Indicates that the item serves as the item over which repeats are to be perfo... |
| [Domain](Domain.md) | Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup data. The... |
| [FileTypeRef](FileTypeRef.md) | Snapshot means that the document contains only the current state of the data ... |
| [EpochOID](EpochOID.md) | Reference to an Epoch element defined in the study. |
| [DurationPostWindow](DurationPostWindow.md) | Defines the amount of time by which the targetted duration may be increased. |
| [CodedValue](CodedValue.md) | Value of the codelist item (as it would occur in clinical data). |
| [ValueListOID](ValueListOID.md) | Reference to the unique ID of a ValueListDef element that provides value-leve... |
| [MethodOID](MethodOID.md) | Reference to a MethodDef that will provide one or more data rows as output. T... |
| [TranslatedTextRef](TranslatedTextRef.md) | TranslatedText reference: Human-readable text that is appropriate for a parti... |
| [content](content.md) | multi-line text content from between XML tags |
| [DescriptionRef](DescriptionRef.md) | Description reference: A free-text description of the containing metadata com... |
| [MetaDataVersionRefRef](MetaDataVersionRefRef.md) | MetaDataVersionRef reference: A reference to a MetaDataVersion used at the co... |
| [IncludeRef](IncludeRef.md) | Include reference: The Include metadata element allows a reference to a prior... |
| [StandardsRef](StandardsRef.md) | Standards reference: The Standards element provides a container for the list ... |
| [AnnotatedCRFRef](AnnotatedCRFRef.md) | AnnotatedCRF reference: An Annotated Case Report Form (CRF) is a Portable Fil... |
| [SupplementalDocRef](SupplementalDocRef.md) | SupplementalDoc reference: Supplemental data definitions |
| [ValueListDefRef](ValueListDefRef.md) | ValueListDef reference: The following table specifies the XML structure for v... |
| [WhereClauseDefRef](WhereClauseDefRef.md) | WhereClauseDef reference: The WhereClauseDef element specifies a condition. |
| [ProtocolRef](ProtocolRef.md) | Protocol reference: The Protocol element lists the kinds of study events that... |
| [WorkflowDefRef](WorkflowDefRef.md) | WorkflowDef reference: A WorkflowDef defines an automated workflow for a stud... |
| [StudyEventGroupDefRef](StudyEventGroupDefRef.md) | StudyEventGroupDef reference: StudyEventGroupDef is a study building block th... |
| [StudyEventDefRef](StudyEventDefRef.md) | StudyEventDef reference: StudyEventDef represents the definition of an activi... |
| [ItemGroupDefRef](ItemGroupDefRef.md) | ItemGroupDef reference: An ItemGroupDef describes a type of variable or field... |
| [ItemDefRef](ItemDefRef.md) | ItemDef reference: An ItemDef describes a type of item that can occur within ... |
| [CodeListRefRef](CodeListRefRef.md) | CodeListRef reference: A reference to a CodeList definition. |
| [ConditionDefRef](ConditionDefRef.md) | ConditionDef reference: A ConditionDef defines a boolean condition. |
| [MethodDefRef](MethodDefRef.md) | MethodDef reference: A MethodDef defines how a data value can be obtained fro... |
| [CommentDefRef](CommentDefRef.md) | CommentDef reference: The Comment element allows referencing short comments s... |
| [LeafRef](LeafRef.md) | Leaf reference: Contains the XLink information referenced by DocumentRef or A... |
| [PDFPageRefRef](PDFPageRefRef.md) | The PDFPageRef element is a container for page references in a PDF file. |
| [StandardRef](StandardRef.md) | Definition of a standard referenced in the Define-XML document. |
| [DocumentRefRef](DocumentRefRef.md) | The DocumentRef element is a container for page references in a PDF file. |
| [ItemRefRef](ItemRefRef.md) | ItemRef reference: A reference to an ItemDef as it occurs within a specific I... |
| [RangeCheckRef](RangeCheckRef.md) | RangeCheck reference: A RangeCheck defines a constraint on the value of the e... |
| [WorkflowRefRef](WorkflowRefRef.md) | WorkflowRef reference: The WorkflowRef references a workflow definition |
| [CodingRef](CodingRef.md) | Coding reference: Coding references a symbol from a defined code system. It u... |
| [StudyEventGroupRefRef](StudyEventGroupRefRef.md) | StudyEventGroupRef reference: This element references a StudyEventGroupDef as... |
| [StudyEventRefRef](StudyEventRefRef.md) | StudyEventRef reference: This element references a StudyEventDef as it occurs... |
| [ItemGroupRefRef](ItemGroupRefRef.md) | ItemGroupRef reference: ItemGroupRef references an ItemGroupDef as it occurs ... |
| [AliasRef](AliasRef.md) | Alias reference: An Alias provides an additional name for an element. The Con... |
| [ClassRef](ClassRef.md) | Class reference: The Class element identifies which predefined Class within t... |
| [OriginRef](OriginRef.md) | Origin reference: Origin defines the source metadata, where applicable, for O... |
| [SubClassRef](SubClassRef.md) | SubClass reference: This element contains SubClass definitions. |
| [WhereClauseRefRef](WhereClauseRefRef.md) | WhereClauseRef reference: The WhereClauseRef references the WhereClauseDef el... |
| [SourceItemsRef](SourceItemsRef.md) | SourceItems reference: Identifies source items as needed to support automated... |
| [SourceItemRef](SourceItemRef.md) | SourceItem reference: Provides the information needed to identify the source ... |
| [ResourceRef](ResourceRef.md) | Resource reference: Describes an external resource used as the source for the... |
| [SelectionRef](SelectionRef.md) | Selection reference: Template for machine-readable/executable expression for ... |
| [QuestionRef](QuestionRef.md) | Question reference: A label shown to a human user when prompted to provide da... |
| [PromptRef](PromptRef.md) | Prompt reference: A prompt text shown to a human user when prompted to provid... |
| [CRFCompletionInstructionsRef](CRFCompletionInstructionsRef.md) | CRFCompletionInstructions reference: Instructions for the clinical site on ho... |
| [ImplementationNotesRef](ImplementationNotesRef.md) | ImplementationNotes reference: Further information, such as rationale and imp... |
| [CDISCNotesRef](CDISCNotesRef.md) | CDISCNotes reference: Explanatory text for the variable. |
| [ValueListRefRef](ValueListRefRef.md) | ValueListRef reference: The ValueListRef element is the OID of the ValueListD... |
| [ErrorMessageRef](ErrorMessageRef.md) | ErrorMessage reference: Error message provided to user when the range check f... |
| [MethodSignatureRef](MethodSignatureRef.md) | MethodSignature reference: A MethodSignature defines the parameters and retur... |
| [FormalExpressionRef](FormalExpressionRef.md) | FormalExpression reference: A FormalExpression used within a ConditionDef or ... |
| [CheckValueRef](CheckValueRef.md) | CheckValue reference: A comparison value used in a range check. |
| [CodeListItemRef](CodeListItemRef.md) | CodeListItem reference: Defines an individual member value of a codelist. It ... |
| [DecodeRef](DecodeRef.md) | Decode reference: The displayed value relating to the CodeListItem/@CodedValu... |
| [ParameterRef](ParameterRef.md) | Parameter reference: The Parameter element represents a method parameter used... |
| [ReturnValueRef](ReturnValueRef.md) | ReturnValue reference: The ReturnValue element represents a return value used... |
| [ExternalCodeLibRef](ExternalCodeLibRef.md) | ExternalCodeLib reference: The ExternalCodeLib element references a FormalExp... |
| [StudySummaryRef](StudySummaryRef.md) | StudySummary reference: The StudyParameter element allows to provide a set of... |
| [StudyStructureRef](StudyStructureRef.md) | StudyStructure reference: The StudyStructure element describes the general st... |
| [TrialPhaseRef](TrialPhaseRef.md) | TrialPhase reference: The TrialPhase element designates the phase of the stud... |
| [StudyTimingsRef](StudyTimingsRef.md) | StudyTimings reference: The StudyTimings element is a container element for i... |
| [StudyIndicationsRef](StudyIndicationsRef.md) | StudyIndications reference: StudyIndications is a container element for indiv... |
| [StudyInterventionsRef](StudyInterventionsRef.md) | StudyInterventions reference: The StudyInterventions element is a container e... |
| [StudyObjectivesRef](StudyObjectivesRef.md) | StudyObjectives reference: The StudyObjectives is a container element for ind... |
| [StudyEndPointsRef](StudyEndPointsRef.md) | StudyEndPoints reference: The StudyEndPoints element is a container element f... |
| [StudyTargetPopulationRefRef](StudyTargetPopulationRefRef.md) | StudyTargetPopulationRef reference: The StudyTargetPopulationRef references a... |
| [StudyEstimandsRef](StudyEstimandsRef.md) | StudyEstimands reference: StudyEstimands is a container element for individua... |
| [InclusionExclusionCriteriaRef](InclusionExclusionCriteriaRef.md) | InclusionExclusionCriteria reference: The InclusionExclusionCriteria element ... |
| [ArmRef](ArmRef.md) | Arm reference: An Arm element provides the declaration of a study arm. Arms d... |
| [EpochRef](EpochRef.md) | Epoch reference: The planned period of subjects' participation in the trial i... |
| [StudyIndicationRef](StudyIndicationRef.md) | StudyIndication reference: This element describes a study indication (e.g., c... |
| [StudyInterventionRefRef](StudyInterventionRefRef.md) | StudyInterventionRef reference: The StudyInterventionRef references an interv... |
| [StudyObjectiveRef](StudyObjectiveRef.md) | StudyObjective reference: The reason for performing a study in terms of the s... |
| [StudyEndPointRefRef](StudyEndPointRefRef.md) | StudyEndPointRef reference: Go to start of metadata |
| [StudyEstimandRef](StudyEstimandRef.md) | StudyEstimand reference: A precise description of the treatment effect reflec... |
| [IntercurrentEventRef](IntercurrentEventRef.md) | IntercurrentEvent reference: The IntercurrentEvent element describes an inter... |
| [SummaryMeasureRef](SummaryMeasureRef.md) | SummaryMeasure reference: The SummaryMeasure element describes a summary meas... |
| [InclusionCriteriaRef](InclusionCriteriaRef.md) | InclusionCriteria reference: The InclusionCriteria is a container element for... |
| [ExclusionCriteriaRef](ExclusionCriteriaRef.md) | ExclusionCriteria reference: The ExclusionCriteria is a container element for... |
| [CriterionRef](CriterionRef.md) | Criterion reference: The Criterion represents either an inclusion or an exclu... |
| [StudyParameterRef](StudyParameterRef.md) | StudyParameter reference: A StudyParameter defines a study design parameter f... |
| [ParameterValueRef](ParameterValueRef.md) | ParameterValue reference: This element contains the value of the study parame... |
| [StudyTimingRef](StudyTimingRef.md) | StudyTiming reference: The StudyTiming element defines a timing constraint wi... |
| [AbsoluteTimingConstraintRef](AbsoluteTimingConstraintRef.md) | AbsoluteTimingConstraint reference: The element AbsoluteTimingConstraint is u... |
| [RelativeTimingConstraintRef](RelativeTimingConstraintRef.md) | RelativeTimingConstraint reference: The RelativeTimingConstraint element desc... |
| [TransitionTimingConstraintRef](TransitionTimingConstraintRef.md) | TransitionTimingConstraint reference: The TransitionTimingConstraint element ... |
| [DurationTimingConstraintRef](DurationTimingConstraintRef.md) | DurationTimingConstraint reference: The DurationTimingConstraint constrains t... |
| [WorkflowStartRef](WorkflowStartRef.md) | WorkflowStart reference: WorkflowStart references a structural element that b... |
| [WorkflowEndRef](WorkflowEndRef.md) | WorkflowEnd reference: A WorkflowEnd references a structural element with whi... |
| [TransitionRef](TransitionRef.md) | Transition reference: A Transition defines a link between 2 structural elemen... |
| [BranchingRef](BranchingRef.md) | Branching reference: This element describes the branching in a workflow from ... |
| [TargetTransitionRef](TargetTransitionRef.md) | TargetTransition reference: TargetTransition provides a reference to a Transi... |
| [DefaultTransitionRef](DefaultTransitionRef.md) | DefaultTransition reference: The DefaultTransition references the Transition ... |
| [UserRefRef](UserRefRef.md) | UserRef reference: A reference to information about a specific user of a clin... |
| [OrganizationRef](OrganizationRef.md) | Organization reference: An organization can reference a parent organization. ... |
| [LocationRefRef](LocationRefRef.md) | LocationRef reference: A reference to the user's physical location. |
| [SignatureDefRef](SignatureDefRef.md) | SignatureDef reference: Provides Metadata for signatures included in the /ODM... |
| [UserNameRef](UserNameRef.md) | UserName reference: The user's login identification in the sender's system. |
| [PrefixRef](PrefixRef.md) | Prefix reference: Title or other prefix. Maps to FHIR HumanName.prefix (https... |
| [SuffixRef](SuffixRef.md) | Suffix reference: This element may include credentials, or suffixes (e.g., Jr... |
| [FullNameRef](FullNameRef.md) | FullName reference: The user's full formal name. May be a combination of Pref... |
| [GivenNameRef](GivenNameRef.md) | GivenName reference: The user's initial given name or all given names. |
| [FamilyNameRef](FamilyNameRef.md) | FamilyName reference: The user's surname (family name). |
| [ImageRef](ImageRef.md) | Image reference: A visual depiction of the user. |
| [AddressRef](AddressRef.md) | Address reference: The postal address for a user, location, or organization. |
| [TelecomRef](TelecomRef.md) | Telecom reference: The telecommunication contacts points of a user, a locatio... |
| [QueryRef](QueryRef.md) | Query reference: The Query element represents a request for clarification on ... |
| [StreetNameRef](StreetNameRef.md) | StreetName reference: The street name part of a user's postal address. |
| [HouseNumberRef](HouseNumberRef.md) | HouseNumber reference: The house number part of a user's postal address. |
| [CityRef](CityRef.md) | City reference: The city name part of a user's postal address. |
| [StateProvRef](StateProvRef.md) | StateProv reference: The state or province name part of a user's postal addre... |
| [CountryRef](CountryRef.md) | Country reference: The country name part of a user's postal address. For CDIS... |
| [PostalCodeRef](PostalCodeRef.md) | PostalCode reference: The postal code part of a user's postal address. |
| [GeoPositionRef](GeoPositionRef.md) | GeoPosition reference: The geographical position using the World Geodetic Sys... |
| [OtherTextRef](OtherTextRef.md) | OtherText reference: Any other text needed as part of a user's postal address... |
| [MeaningRef](MeaningRef.md) | Meaning reference: A short name or description for this signature. It should ... |
| [LegalReasonRef](LegalReasonRef.md) | LegalReason reference: The responsibility statement associated with a signatu... |
| [ItemGroupDataRef](ItemGroupDataRef.md) | ItemGroupData reference: Clinical data corresponding to an ItemGroupRef defin... |
| [AuditRecordRef](AuditRecordRef.md) | AuditRecord reference: An AuditRecord carries information pertaining to the c... |
| [SignatureRefRef](SignatureRefRef.md) | SignatureRef reference: A reference to the signature meaning. |
| [AnnotationRef](AnnotationRef.md) | Annotation reference: A general note about clinical data. If an annotation ha... |
| [SubjectDataRef](SubjectDataRef.md) | SubjectData reference: Clinical data for a single subject. |
| [InvestigatorRefRef](InvestigatorRefRef.md) | InvestigatorRef reference: Provides a reference to the user who created the S... |
| [SiteRefRef](SiteRefRef.md) | SiteRef reference: Provides a reference to the site that the SubjectData reco... |
| [StudyEventDataRef](StudyEventDataRef.md) | StudyEventData reference: Clinical data for a study event (visit). The model ... |
| [ItemDataRef](ItemDataRef.md) | ItemData reference: The ItemData element is used for transmission of the clin... |
| [DateTimeStampRef](DateTimeStampRef.md) | DateTimeStamp reference: Date and time when an action was performed. |
| [ReasonForChangeRef](ReasonForChangeRef.md) | ReasonForChange reference: A user-supplied reason for a data change. |
| [SourceIDRef](SourceIDRef.md) | SourceID reference: Information that identifies the source of the data within... |
| [StudyRef](StudyRef.md) | Study reference: This element collects static structural information about an... |
| [AdminDataRef](AdminDataRef.md) | AdminData reference: Administrative information about users, locations, organ... |
| [ReferenceDataRef](ReferenceDataRef.md) | ReferenceData reference: Reference data provides information on how to interp... |
| [ClinicalDataRef](ClinicalDataRef.md) | ClinicalData reference: Clinical data for 1 or more subjects. |
| [AssociationRef](AssociationRef.md) | Association reference: An association permits an annotation to be placed on a... |
| [KeySetRef](KeySetRef.md) | KeySet reference: A KeySet references a single entity (e.g., a study, a subje... |
| [CommentRef](CommentRef.md) | Comment reference: A free-text (uninterpreted) comment about clinical data. T... |
| [FlagRef](FlagRef.md) | Flag reference: A machine-processable annotation. |
| [FlagValueRef](FlagValueRef.md) | FlagValue reference: The value of the flag. The meaning of this value is typi... |
| [FlagTypeRef](FlagTypeRef.md) | FlagType reference: The type of flag. This determines the purpose and semanti... |


## Enumerations
_Enumerations are common features in modeling frameworks. These can be thought of as a “drop-down” of permissible values for a field/slot. See [LinkML documentation](https://linkml.io/linkml/schemas/enums.html) for more information._

| Enumeration | Description |
| --- | --- |
| [DataType](DataType.md) | Enumeration used in DataTypeRef |
| [CLDataType](CLDataType.md) | Enumeration used in DataTypeRef |
| [FileType](FileType.md) | Enumeration used in FileTypeRef |
| [Granularity](Granularity.md) | Enumeration used in GranularityRef |
| [Context](Context.md) | Enumeration used in ContextRef |
| [EventType](EventType.md) | Enumeration used in Type |
| [BranchingType](BranchingType.md) | Enumeration used in Type |
| [StudyObjectiveLevel](StudyObjectiveLevel.md) | Enumeration used in Level |
| [TrialPhaseTypeEnum](TrialPhaseTypeEnum.md) |  |
| [StudyEndPointType](StudyEndPointType.md) | Enumeration used in Type |
| [StudyEstimandLevel](StudyEstimandLevel.md) | Enumeration used in Level |
| [RelativeTimingConstraintType](RelativeTimingConstraintType.md) | Enumeration used in Type |
| [Comparator](Comparator.md) | Enumeration used in ComparatorRef |
| [SoftOrHard](SoftOrHard.md) | Enumeration used in SoftHard |
| [TransactionType](TransactionType.md) | Enumeration used in TransactionTypeRef |
| [UserType](UserType.md) | Enumeration used in UserTypeRef |
| [OrganizationType](OrganizationType.md) | Enumeration used in Type |
| [TelecomTypeType](TelecomTypeType.md) | Enumeration used in TelecomType |
| [CommentType](CommentType.md) | Enumeration used in SponsorOrSite |
| [SignMethod](SignMethod.md) | Enumeration used in Methodology |
| [EditPointType](EditPointType.md) | Enumeration used in EditPoint |
| [YesOrNo](YesOrNo.md) | Enumeration used in IsReferenceData, Mandatory, UsedMethod, Repeating |
| [YesOnly](YesOnly.md) | Enumeration used in IsNonStandard, Repeat, ExtendedValue, IsNull, Other, HasN... |
| [MethodType](MethodType.md) | Enumeration used in Type |
| [ItemGroupRepeatingType](ItemGroupRepeatingType.md) | Enumeration used in Repeating |
| [ItemGroupTypeTypeEnum](ItemGroupTypeTypeEnum.md) |  |
| [QuerySourceType](QuerySourceType.md) | Enumeration used in Source |
| [QueryType](QueryType.md) | Enumeration used in Type |
| [QueryStateType](QueryStateType.md) | Enumeration used in State |
| [DefCoreType](DefCoreType.md) |  |
| [ODMCoreType](ODMCoreType.md) |  |
| [OriginSource](OriginSource.md) | Enumeration used in Source |
| [OriginType](OriginType.md) | Enumeration used in Type |
| [PDFPageType](PDFPageType.md) | Enumeration used in Type |
| [StandardName](StandardName.md) | Enumeration used in Name |
| [StandardPublishingSet](StandardPublishingSet.md) | Enumeration used in PublishingSet |
| [StandardStatusEnum](StandardStatusEnum.md) |  |
| [StandardType](StandardType.md) | Enumeration used in Type |
| [DictionaryNameTypeEnum](DictionaryNameTypeEnum.md) |  |
| [ItemGroupClass](ItemGroupClass.md) | Enumeration used in Name |
| [ItemGroupSubClass](ItemGroupSubClass.md) | Enumeration used in Name |


## Types
_Types in LinkML are scalar data values such as strings, integers, floats, and so on. See [LinkML documentation](https://linkml.io/linkml/schemas/models.html#types) for more information._

| Type | Description |
| --- | --- |
| [text](text.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [positiveInteger](positiveInteger.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [hexBinary](hexBinary.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [base64Binary](base64Binary.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [hexFloat](hexFloat.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [base64Float](base64Float.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [emptyTag](emptyTag.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [partialDate](partialDate.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [tHour](tHour.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [partialTime](partialTime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [tDatetime](tDatetime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [partialDatetime](partialDatetime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [tDuration](tDuration.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [durationDatetime](durationDatetime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [tInterval](tInterval.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [intervalDatetime](intervalDatetime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [tIncomplete](tIncomplete.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [incompleteDatetime](incompleteDatetime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [tIncompleteDate](tIncompleteDate.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [tIncompleteTime](tIncompleteTime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [incompleteTime](incompleteTime.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [incompleteDate](incompleteDate.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [oid](oid.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [oidref](oidref.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [value](value.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [subjectKey](subjectKey.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [repeatKey](repeatKey.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [name](name.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [fileName](fileName.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [ODMVersion](ODMVersion.md) | Version of ODM that the file conforms to. |
| [TrialPhaseType](TrialPhaseType.md) | A terminology codelist relevant to the phase, or stage, of the |
| [ItemGroupTypeType](ItemGroupTypeType.md) | https://wiki.cdisc.org/display/PUB/Data+Formats |
| [CoreType](CoreType.md) | Core. |
| [StandardStatus](StandardStatus.md) | Terminology relevant to the development or publication status of the |
| [DictionaryNameType](DictionaryNameType.md) | A name given to a reference source that lists words and gives their |
| [ItemGroupClassSubClass](ItemGroupClassSubClass.md) | Sub class of a general observation class. Union of ItemGroupClass and |
| [languageType](languageType.md) | language context for internationalisation and localisation |
| [contentType](contentType.md) | multi-line text content from between XML tags |
| [string](string.md) | A character string |
| [integer](integer.md) | An integer |
| [boolean](boolean.md) | A binary (true or false) value |
| [float](float.md) | A real number that conforms to the xsd:float specification |
| [double](double.md) | A real number that conforms to the xsd:double specification |
| [decimal](decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [time](time.md) | A time object represents a (local) time of day, independent of any particular... |
| [date](date.md) | a date (year, month and day) in an idealized calendar |
| [datetime](datetime.md) | The combination of a date and time |
| [date_or_datetime](date_or_datetime.md) | Either a date or a datetime |
| [uriorcurie](uriorcurie.md) | a URI or a CURIE |
| [curie](curie.md) | a compact URI |
| [uri](uri.md) | a complete URI |
| [ncname](ncname.md) | Prefix part of CURIE |
| [objectidentifier](objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [nodeidentifier](nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |


## Subsets
_Elements of a schema can be partitioned into named subsets. These have no semantic meaning, but they can be useful for tagging parts of a schema for different purposes. See [LinkML documentation](https://linkml.io/linkml/schemas/models.html#subsets) for more information._

| Subset | Description |
| --- | --- |
| [AbsoluteTimingConstraintElementExtension](AbsoluteTimingConstraintElementExtension.md) |  |
| [AddressElementExtension](AddressElementExtension.md) |  |
| [AdminDataElementExtension](AdminDataElementExtension.md) |  |
| [AliasElementExtension](AliasElementExtension.md) |  |
| [AnnotatedCRFElementExtension](AnnotatedCRFElementExtension.md) |  |
| [AnnotationElementExtension](AnnotationElementExtension.md) |  |
| [ArmElementExtension](ArmElementExtension.md) |  |
| [AssociationElementExtension](AssociationElementExtension.md) |  |
| [AuditRecordElementExtension](AuditRecordElementExtension.md) |  |
| [AuditRecordSignatureNotationGroup](AuditRecordSignatureNotationGroup.md) |  |
| [BranchingElementExtension](BranchingElementExtension.md) |  |
| [CDISCNotesElementExtension](CDISCNotesElementExtension.md) |  |
| [ClassElementExtension](ClassElementExtension.md) |  |
| [ClinicalDataElementExtension](ClinicalDataElementExtension.md) |  |
| [CodeListElementExtension](CodeListElementExtension.md) |  |
| [CodeListItemElementExtension](CodeListItemElementExtension.md) |  |
| [CodeListRefElementExtension](CodeListRefElementExtension.md) |  |
| [CodingElementExtension](CodingElementExtension.md) |  |
| [CommentDefElementExtension](CommentDefElementExtension.md) |  |
| [CommentElementExtension](CommentElementExtension.md) |  |
| [ConditionDefElementExtension](ConditionDefElementExtension.md) |  |
| [CRFCompletionInstructionsElementExtension](CRFCompletionInstructionsElementExtension.md) |  |
| [CriterionElementExtension](CriterionElementExtension.md) |  |
| [DecodeElementExtension](DecodeElementExtension.md) |  |
| [DefaultTransitionElementExtension](DefaultTransitionElementExtension.md) |  |
| [DefinitionElementExtension](DefinitionElementExtension.md) |  |
| [DescriptionElementExtension](DescriptionElementExtension.md) |  |
| [DocumentRefElementExtension](DocumentRefElementExtension.md) |  |
| [DurationTimingConstraintElementExtension](DurationTimingConstraintElementExtension.md) |  |
| [EpochElementExtension](EpochElementExtension.md) |  |
| [ErrorMessageElementExtension](ErrorMessageElementExtension.md) |  |
| [ExceptionEventGroupDefinition](ExceptionEventGroupDefinition.md) |  |
| [ExclusionCriteriaElementExtension](ExclusionCriteriaElementExtension.md) |  |
| [FlagElementExtension](FlagElementExtension.md) |  |
| [FormalExpressionElementExtension](FormalExpressionElementExtension.md) |  |
| [GeoPositionElementExtension](GeoPositionElementExtension.md) |  |
| [ImageElementExtension](ImageElementExtension.md) |  |
| [ImplementationNotesElementExtension](ImplementationNotesElementExtension.md) |  |
| [IncludeElementExtension](IncludeElementExtension.md) |  |
| [InclusionCriteriaElementExtension](InclusionCriteriaElementExtension.md) |  |
| [InclusionExclusionCriteriaElementExtension](InclusionExclusionCriteriaElementExtension.md) |  |
| [IntercurrentEventElementExtension](IntercurrentEventElementExtension.md) |  |
| [InvestigatorRefElementExtension](InvestigatorRefElementExtension.md) |  |
| [ItemDataElementExtension](ItemDataElementExtension.md) |  |
| [ItemDefElementExtension](ItemDefElementExtension.md) |  |
| [ItemGroupDataElementExtension](ItemGroupDataElementExtension.md) |  |
| [ItemGroupDataGroup](ItemGroupDataGroup.md) |  |
| [ItemGroupDefElementExtension](ItemGroupDefElementExtension.md) |  |
| [ItemGroupDefGroup](ItemGroupDefGroup.md) |  |
| [ItemGroupRefElementExtension](ItemGroupRefElementExtension.md) |  |
| [ItemRefElementExtension](ItemRefElementExtension.md) |  |
| [KeySetElementExtension](KeySetElementExtension.md) |  |
| [LeafElementExtension](LeafElementExtension.md) |  |
| [LocationElementExtension](LocationElementExtension.md) |  |
| [LocationRefElementExtension](LocationRefElementExtension.md) |  |
| [MetaDataVersionElementExtension](MetaDataVersionElementExtension.md) |  |
| [MetaDataVersionPreIncludeElementExtension](MetaDataVersionPreIncludeElementExtension.md) |  |
| [MetaDataVersionRefElementExtension](MetaDataVersionRefElementExtension.md) |  |
| [MethodDefElementExtension](MethodDefElementExtension.md) |  |
| [MethodSignatureElementExtension](MethodSignatureElementExtension.md) |  |
| [ODMElementExtension](ODMElementExtension.md) |  |
| [OrganizationElementExtension](OrganizationElementExtension.md) |  |
| [OriginElementExtension](OriginElementExtension.md) |  |
| [ParameterElementExtension](ParameterElementExtension.md) |  |
| [ParameterValueElementExtension](ParameterValueElementExtension.md) |  |
| [PromptElementExtension](PromptElementExtension.md) |  |
| [ProtocolElementExtension](ProtocolElementExtension.md) |  |
| [QueryElementExtension](QueryElementExtension.md) |  |
| [QuestionElementExtension](QuestionElementExtension.md) |  |
| [RangeCheckElementExtension](RangeCheckElementExtension.md) |  |
| [ReferenceDataElementExtension](ReferenceDataElementExtension.md) |  |
| [RelativeTimingConstraintElementExtension](RelativeTimingConstraintElementExtension.md) |  |
| [ResourceElementExtension](ResourceElementExtension.md) |  |
| [ReturnValueElementExtension](ReturnValueElementExtension.md) |  |
| [SelectionElementExtension](SelectionElementExtension.md) |  |
| [SignatureDefElementExtension](SignatureDefElementExtension.md) |  |
| [SignatureElementExtension](SignatureElementExtension.md) |  |
| [SignatureRefElementExtension](SignatureRefElementExtension.md) |  |
| [SiteRefElementExtension](SiteRefElementExtension.md) |  |
| [SourceItemElementExtension](SourceItemElementExtension.md) |  |
| [StandardElementExtension](StandardElementExtension.md) |  |
| [StudyElementExtension](StudyElementExtension.md) |  |
| [StudyEndPointElementExtension](StudyEndPointElementExtension.md) |  |
| [StudyEndPointRefElementExtension](StudyEndPointRefElementExtension.md) |  |
| [StudyEstimandElementExtension](StudyEstimandElementExtension.md) |  |
| [StudyEventDataElementExtension](StudyEventDataElementExtension.md) |  |
| [StudyEventDefElementExtension](StudyEventDefElementExtension.md) |  |
| [StudyEventDefGroup](StudyEventDefGroup.md) |  |
| [StudyEventGroupDefElementExtension](StudyEventGroupDefElementExtension.md) |  |
| [StudyEventGroupRefElementExtension](StudyEventGroupRefElementExtension.md) |  |
| [StudyEventRefElementExtension](StudyEventRefElementExtension.md) |  |
| [StudyIndicationElementExtension](StudyIndicationElementExtension.md) |  |
| [StudyInterventionElementExtension](StudyInterventionElementExtension.md) |  |
| [StudyObjectiveElementExtension](StudyObjectiveElementExtension.md) |  |
| [StudyParameterElementExtension](StudyParameterElementExtension.md) |  |
| [StudyStructureElementExtension](StudyStructureElementExtension.md) |  |
| [StudySummaryElementExtension](StudySummaryElementExtension.md) |  |
| [StudyTargetPopulationElementExtension](StudyTargetPopulationElementExtension.md) |  |
| [StudyTimingElementExtension](StudyTimingElementExtension.md) |  |
| [SubjectDataElementExtension](SubjectDataElementExtension.md) |  |
| [SummaryMeasureElementExtension](SummaryMeasureElementExtension.md) |  |
| [SupplementalDocElementExtension](SupplementalDocElementExtension.md) |  |
| [TargetTransitionElementExtension](TargetTransitionElementExtension.md) |  |
| [TelecomElementExtension](TelecomElementExtension.md) |  |
| [TransitionElementExtension](TransitionElementExtension.md) |  |
| [TransitionTimingConstraintElementExtension](TransitionTimingConstraintElementExtension.md) |  |
| [TrialPhaseElementExtension](TrialPhaseElementExtension.md) |  |
| [UserElementExtension](UserElementExtension.md) |  |
| [UserRefElementExtension](UserRefElementExtension.md) |  |
| [ValueListDefElementExtension](ValueListDefElementExtension.md) |  |
| [ValueListRefElementExtension](ValueListRefElementExtension.md) |  |
| [WhereClauseDefElementExtension](WhereClauseDefElementExtension.md) |  |
| [WhereClauseRefElementExtension](WhereClauseRefElementExtension.md) |  |
| [WorkflowDefElementExtension](WorkflowDefElementExtension.md) |  |
| [WorkflowRefElementExtension](WorkflowRefElementExtension.md) |  |
| [WorkflowStartElementExtension](WorkflowStartElementExtension.md) |  |
| [WorkflowTransitionGroupDefinition](WorkflowTransitionGroupDefinition.md) |  |
