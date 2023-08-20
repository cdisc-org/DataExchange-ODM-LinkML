# odm



URI: http://www.cdisc.org/ns/odm/v2.0

Name: odm



## Classes

| Class | Description |
| --- | --- |
| [AbsoluteTimingConstraint](AbsoluteTimingConstraint.md) | The element AbsoluteTimingConstraint is used to specify when an activity, represented by either a StudyEventGroup or StudyEvent, can take place.  |
| [Address](Address.md) | The postal address for a user, location, or organization. |
| [AdminData](AdminData.md) | Administrative information about users, locations, organizations, and electronic signatures. |
| [Alias](Alias.md) | An Alias provides an additional name for an element. The Context attribute specifies the application domain in which this additional name is relevant. |
| [AnnotatedCRF](AnnotatedCRF.md) | An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document that provides the mapping of data collection fields to the variables or discrete variable values contained within the datasets. |
| [Annotation](Annotation.md) | A general note about clinical data. If an annotation has both a comment and flags, the flags should be related to the comment. |
| [Arm](Arm.md) | An Arm element provides the declaration of a study arm. Arms do not have any ordering relative to one another. |
| [Association](Association.md) | An association permits an annotation to be placed on an ordered pair of entities rather than on just one. The first and second KeySets identify the start and end of the annotated "link." |
| [AuditRecord](AuditRecord.md) | An AuditRecord carries information pertaining to the creation, deletion, or modification of clinical data. This information includes who performed that action, and where, when, and why that action was performed.AuditRecord information describes a change to clinical data, but is not itself clinical data. The value of some clinical data can always be changed by a subsequent transaction, but history cannot be changed, only added to. Element NameAuditRecordParent ElementsReferenceData, ClinicalData, SubjectData, StudyEventData, ItemGroupData, ItemData, QueryElement XPath(s)/ODM/AdminData/Location/Query/AuditRecord/ODM/ReferenceData/AuditRecord/ODM/ClinicalData/AuditRecord/ODM/ClinicalData/Query/AuditRecord/ODM/ClinicalData/SubjectData/AuditRecord/ODM/ClinicalData/SubjectData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/Query/AuditRecordElement Textual ValueNoneUsage/Business RulesBusiness Rule(s):For the Archive use case, all AuditRecord information in the data collection system must be provided within the ODM ClinicalData.When the ODM FileType attribute is set to Transactional, every ClinicalData that has a TransactionType must also have an AuditRecord.Other Information:An AuditRecord applies to any descendant data element that allows a TransactionType and does not have an AuditRecord. Query elements must have their own AuditRecord(s).AuditRecord information describes a change to clinical data, but is not itself clinical data. The value of some clinical data can always be changed by a subsequent transaction, but history cannot be changed -- only added to.AttributesEditPoint, UsedMethod.Child Elements(UserRef, LocationRef, DateTimeStamp, ReasonForChange?, SourceID?) |
| [Branching](Branching.md) | This element describes the branching in a workflow from a source (start) structural element to 2 or more target structural elements, over a Transition element. |
| [CDISCNotes](CDISCNotes.md) | Explanatory text for the variable. |
| [CheckValue](CheckValue.md) | A comparison value used in a range check.  |
| [City](City.md) | The city name part of a user's postal address. |
| [Class](Class.md) | Element NameClassParent ElementsItemGroupDefElement XPath(s)/ODM/Study/MetaDataVersion/ItemGroupDef/ClassElement Textual ValueNoneAttributesNameChild Elements(SubClass*)Usage/Business RulesBusiness Rule(s):One Class element is allowed for each ItemGroupDef element for a dataset that follows the CDISC SDTMIG, SENDIG, or ADaMIG.For analysis datasets, if the ItemGroupDef IsNonStandard attribute is used, the Class should not be provided. |
| [ClinicalData](ClinicalData.md) | Clinical data for 1 or more subjects. |
| [Code](Code.md) | Contains the source code that represents a FormalExpression in a given Context. The source code must be executable, and the MethodSignature defines the input parameters and return values for the code. |
| [CodeList](CodeList.md) | Defines a discrete set of permitted values for an item, or provides a reference to a codelist or dictionary maintained by an external organization via the Coding element, or a combination of both. Examples provided under Coding.Element NameCodeListParent ElementsMetaDataVersionElement XPath(s)/ODM/Study/MetaDataVersion/CodeListElement Textual ValueNoneAttributesOID, Name, DataType, CommentOID, StandardOID, IsNonStandardChild Elements(Description?, CodeListItem*, Coding*, Alias*)Usage/Business Rules |
| [CodeListItem](CodeListItem.md) | Defines an individual member value of a codelist. It may include a display value in the child Decode element |
| [CodeListRef](CodeListRef.md) | A reference to a CodeList definition. |
| [Coding](Coding.md) | Coding references a symbol from a defined code system. It uses a code defined in a terminology system to associate semantics with a given term, codelist, variable, or group of variables. The presence of a Coding element associates a meaning to its parent element. Including multiple Coding elements for a given parent indicates synonymous meanings provided by different code systems or code system versions. |
| [Comment](Comment.md) | A free-text (uninterpreted) comment about clinical data. The comment may have come from the sponsor or the clinical site. |
| [CommentDef](CommentDef.md) | The Comment element allows referencing short comments self-contained in the XML document or long comments normally included in external documents. For comments included in external documents, the reference could include specific pages of a document where the comments are included. |
| [ConditionDef](ConditionDef.md) | A ConditionDef defines a boolean condition.Element NameConditionDefParent ElementsMetaDataVersionElement XPath(s)/ODM/Study/MetaDataVersion/ConditionDefElement Textual ValueNoneAttributesOID, Name, CommentOIDChild Elements(Description, MethodSignature, FormalExpression*, Alias*)The Description element must be provided and should include a prose description. The MethodSignature element must also be provided and identifies the input parameter and return values for the ConditionDef.Usage/Business RulesBusiness Rule(s):The MethodSignature ReturnValue for ConditionDef must always equal boolean.If a FormalExpression is provided, it must contain a machine-readable expression that will evaluate to True or False.Other Information:The Description and MethodSignature are the normative content of the ConditionDef. The ConditionDef is referenced by the CollectionExceptionConditionOID attribute within a study metadata component which may be omitted under circumstances defined by the condition (i.e., when the FormalExpression evaluates to True).Multiple FormalExpressions can be provided if each has a different Context attribute, allowing the same expression to be represented in forms appropriate to multiple systems.If an application cannot interpret any of the FormalExpressions or does not normally support conditional data collection, data for the referencing study metadata component should be collected as though no Condition is specified.In cases where a MethodSignature element exists without an associated FormalExpression, the MethodSignature supports improved traceability. It also serves the case where one role defines the MethodDef or ConditionDef, but another role provides the executable FormalExpression. |
| [Country](Country.md) | The country name part of a user's postal address. For CDISC SDTM or trial registry applications, this must be represented by an ISO 3166 3-letter or US-GENC country code (e.g., FRA for France, JPN for Japan). |
| [CRFCompletionInstructions](CRFCompletionInstructions.md) | Instructions for the clinical site on how to enter collected information on the CRF. |
| [Criterion](Criterion.md) | The Criterion represents either an inclusion or an exclusion criterion, depending on the parent element (i.e., InclusionCriteria, ExclusionCriteria). |
| [DateTimeStamp](DateTimeStamp.md) | Element NameDateTimeStampParent ElementsAuditRecord, SignatureElement XPath(s)/ODM/AdminData/Location/Query/AuditRecord/ODM/ClinicalData/Query/AuditRecord/ODM/ClinicalData/SubjectData/AuditRecord/ODM/ClinicalData/SubjecData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEvent/AuditRecord/ODM/ClinicalData/SubjecData/StudyEvent/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/AuditRecord/ODM/ClinicalData/SubjecData/StudyEvent/ItemGroupData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/ItemData/AuditRecord/ODM/ClinicalData/SubjecData/StudyEvent/ItemGroupData/ItemData/Query/AuditRecord/ODM/ClinicalData/SubjectData/Signature/ODM/ClinicalData/SubjectData/StudyEvent/Signature/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/Signature/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/ItemData/SignatureElement Textual ValuedatetimeAttributesNoneChild ElementsNoneUsage/Business Rules |
| [Decode](Decode.md) | The displayed value relating to the CodeListItem/@CodedValue. This is often a label corresponding to a short name or alpha-numeric code. The actual Decode text is provided in a TranslatedText element so that it can be provided in different languages on a case report form or tabular data summary. |
| [DefaultTransition](DefaultTransition.md) | Element NameDefaultTransitionParent ElementsBranchingElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/WorkflowDef/Branching/DefaultTransitionElement Textual ValueNoneAttributesTargetTransitionOIDChild ElementsNoneUsage/Business Rules |
| [Definition](Definition.md) | Definition of the item. |
| [Description](Description.md) | A free-text description of the containing metadata component, unless restricted by Business Rules. |
| [DocumentRef](DocumentRef.md) | Links to a leaf element with the location of the document. |
| [DurationTimingConstraint](DurationTimingConstraint.md) | None |
| [EntryCriteria](EntryCriteria.md) | None |
| [Epoch](Epoch.md) | The planned period of subjects' participation in the trial is divided into sequential epochs. Each epoch is a period of time that serves a purpose in the trial as a whole. Epochs cannot overlap. The sequence of the epoch in the study is provided by the SequenceNumber attribute, the first epoch in the study being assigned the sequence number 1. Sequence numbers are subsequent. |
| [ErrorMessage](ErrorMessage.md) | Error message provided to user when the range check fails. |
| [ExceptionEvent](ExceptionEvent.md) | An ExceptionEvent describes an event that occurs suddenly in a study and that was not planned as part of the normal workflow of the study. Examples are adverse events, death of a subject not caused by an adverse event, etc. |
| [ExclusionCriteria](ExclusionCriteria.md) | The ExclusionCriteria is a container element for Criterion elements describing exclusion criteria for subjects in the study. When a list is provided, not meeting any of the criteria in the list may lead to exclusion of enrollment in the study. |
| [ExitCriteria](ExitCriteria.md) | None |
| [ExternalCodeLib](ExternalCodeLib.md) | The ExternalCodeLib element references a FormalExpression in an external code library, such as a file or GitHub. The intention is to make it possible to reference existing code libraries where the code is maintained as well as making it simpler to include longer, more complex FormalExpressions. The Library attribute provides the name of the external library, whereas ref or href provides a reference to the repository that can be used to retrieve the code. The Method attribute provides the name of the method in the file referenced for cases where multiple methods are provided in the source code file. The Version element provides the version of the external FormalExpression code referenced. |
| [FamilyName](FamilyName.md) | The user's surname (family name). |
| [Flag](Flag.md) | Element NameFlagParent ElementsAnnotationElement XPath(s)/ODM/ReferenceData/Annotation/Flag/ODM/ReferenceData/ItemGroupData/Annotation/Flag/ODM/ReferenceData/ItemGroupData/ItemData/Annotation/Flag/ODM/ClinicalData/Annotation/Flag/ODM/ClinicalData/ItemGroupData/Annotation/Flag/ODM/ClinicalData/ItemGroupData/ItemData/Annotation/Flag/ODM/ClinicalData/SubjectData/Annotation/Flag/ODM/ClinicalData/SubjectData/StudyEventData/Annotation/Flag/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/Annotation/Flag/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/Annotation/FlagElement Textual ValueNoneAttributesNoneChild Elements(FlagValue, FlagType?)Usage/Business Rules |
| [FlagType](FlagType.md) | The type of flag. This determines the purpose and semantics of the flag. |
| [FlagValue](FlagValue.md) | The value of the flag. The meaning of this value is typically dependent on the associated FlagType. The actual value must be a member of the referenced CodeList |
| [FormalExpression](FormalExpression.md) | A FormalExpression used within a ConditionDef or a RangeCheck must evaluate to True or False. A FormalExpression referenced within a MethodDef having Type Imputation, Computation, or Transpose must evaluate to the correct DataType for an Item that may be imputed or computed using the Method. A FormalExpression gets parameter and return value definitions from the MethodSignature element. The data types in the MethodSignature parameters and return values must match the corresponding data types in the FormalExpression.  |
| [FullName](FullName.md) | The user's full formal name. May be a combination of Prefix, GivenName, FamilyName & Suffix. Intended to be used for display. |
| [GeoPosition](GeoPosition.md) | The geographical position using the World Geodetic System WGS84.  |
| [GivenName](GivenName.md) | The user's initial given name or all given names.  |
| [HouseNumber](HouseNumber.md) | The house number part of a user's postal address. |
| [Image](Image.md) | A visual depiction of the user. |
| [ImplementationNotes](ImplementationNotes.md) | Further information, such as rationale and implementation instructions, on how to implement the CRF data collection fields. |
| [Include](Include.md) | The Include metadata element allows a reference to a prior metadata version. |
| [InclusionCriteria](InclusionCriteria.md) | The InclusionCriteria is a container element for Criterion elements describing inclusion criteria for subjects in the study. When a list is provided, subjects must meet each of the criteria in the list in order to enroll in the study. |
| [InclusionExclusionCriteria](InclusionExclusionCriteria.md) | The InclusionExclusionCriteria element can contain 2 lists of Criterion elements, represented by the 2 elements InclusionCriteria and ExclusionCriteria. Together, these criteria determine the eligibility of a subject for the study. The actual condition to be evaluated is contained in an ODM ConditionDef, which is referenced by each Criterion‟s ConditionOID attribute. |
| [IntercurrentEvent](IntercurrentEvent.md) | Element NameInterCurrentEventParent ElementsStudyEstimandElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimand/InterCurrentEventElement Textual ValueNoneAttributesNoneChild ElementsDescriptionUsage/Business Rules |
| [InvestigatorRef](InvestigatorRef.md) | Provides a reference to the user who created the SubjectData record in the source system.  |
| [ItemData](ItemData.md) | The ItemData element is used for transmission of the clinical data for an item. The model does not support repeating items within a single item group. |
| [ItemDef](ItemDef.md) | An ItemDef describes a type of item that can occur within a study. Item properties include name, datatype, range, or codelist restrictions, and several other properties. |
| [ItemGroupData](ItemGroupData.md) | Clinical data corresponding to an ItemGroupRef defined in the active MetaDataVersion.  |
| [ItemGroupDef](ItemGroupDef.md) | An ItemGroupDef describes a type of variable or field grouping that can occur within a study. |
| [ItemGroupRef](ItemGroupRef.md) | ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyEventDef or ItemGroupDef. The list of ItemGroupRefs identifies the types of item groups that are allowed to occur within this type of studyevent or (nested) item group. The ItemGroupRefs within a single StudyEventDef or ItemGroupDef must not have duplicate ItemGroupOID or OrderNumber attribute values. |
| [ItemRef](ItemRef.md) | A reference to an ItemDef as it occurs within a specific ItemGroupDef. The list of ItemRefs identifies the types of items that are allowed to occur within this type of item group. |
| [KeySet](KeySet.md) | A KeySet references a single entity (e.g., a study, a subject, a study event). Only those attributes needed to specify the particular entity are required, and all others must be omitted (see Section 2.7, Clinical Data Keys). |
| [Leaf](Leaf.md) | Contains the XLink information referenced by DocumentRef or ArchiveLocationID |
| [LegalReason](LegalReason.md) | The responsibility statement associated with a signature (e.g., "The signer accepts responsibility for the accuracy of this data."). |
| [Location](Location.md) | A physical location associated with data collection and/or treatment of subjects.  |
| [LocationRef](LocationRef.md) | A reference to the user's physical location. |
| [Meaning](Meaning.md) | A short name or description for this signature. It should reflect the context of the signature and/or the text that appears when the signature is applied in the user interface. |
| [MetaDataVersion](MetaDataVersion.md) | The metadata for a study is defined in a series of MetaDataVersion elements. Through this mechanism (multiple MetaDataVersion elements), the model supports the incremental deployment of "mid-stream study changes," and thus can handle a situation where multiple versions of the metadata are being used simultaneously (e.g., due to delays in IRB approval at various sites). |
| [MetaDataVersionRef](MetaDataVersionRef.md) | A reference to a MetaDataVersion used at the containing Location. The EffectiveDate reflects the possibility that the metadata may change over the course of the study. |
| [MethodDef](MethodDef.md) | A MethodDef defines how a data value can be obtained from a collection of other data values. |
| [MethodSignature](MethodSignature.md) | A MethodSignature defines the parameters and return values for a method. The MethodSignature improves traceability while enhancing the ability for automation engines to execute a MethodDef's FormalExpression. Most Methods use one or more input parameters and return one or more values.  |
| [ODMFileMetadata](ODMFileMetadata.md) | Root element for ODM Documents. The ODM element is the top-level (root) element of each ODM document. |
| [Organization](Organization.md) | An organization can reference a parent organization. Users may be associated with an Organization. An Organization may be associated with a Location. A User, Location, or Organization may have an address. |
| [Origin](Origin.md) | Origin defines the source metadata, where applicable, for ODM ItemRefs or ItemGroupRefs. Origin as a child element replaces the Origin attribute in ODM v1.3 that exists for the ItemDef and ItemGroupDef elements.The Origin element is based on the def:Origin element in Define-XML v2.1 with the Trace-XML v1.0 extension. Element NameOriginParent ElementsItemGroupDef, ItemRefElement XPath(s)/ODM/Study/MetaDataVersion/ValueListDef/ItemRef/Origin/ODM/Study/MetaDataVersion/ItemGroupDef/Origin/ODM/Study/MetaDataVersion/ItemGroupDef/ItemRef/OriginElement Textual ValueNoneAttributesType, SourceChild Elements(Description?, SourceItems?, Coding*, DocumentRef*)The SourceItems element contains SourceItem child elements that reference the source variables, if any, for a given ItemRef. SourceItem elements provide machine-readable traceability and identify specific arguments for a MethodDef, specially when used with an Origin with Type="Derived".Usage/Business Rules |
| [OtherText](OtherText.md) | Any other text needed as part of a user's postal address. |
| [Parameter](Parameter.md) | The Parameter element represents a method parameter used as part of a MethodSignature in MethodDef, ConditionDef, or RangeCheck. |
| [ParameterValue](ParameterValue.md) | This element contains the value of the study parameter as text content. |
| [PDFPageRef](PDFPageRef.md) | This element is the container for CRF page references. |
| [PostalCode](PostalCode.md) | The postal code part of a user's postal address. |
| [Prefix](Prefix.md) | Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhir/datatypes.html#humanname). |
| [Prompt](Prompt.md) | A prompt text shown to a human user when prompted to provide data for an item on paper or on a screen. The Prompt is a short version of the question. |
| [Protocol](Protocol.md) | The Protocol element lists the kinds of study events that can occur within a specific version of a study. All clinical data must occur within one of these study events. |
| [Query](Query.md) | The Query element represents a request for clarification on a data item collected for a clinical trial, specifically a request from a sponsor or sponsor’s representative to an investigator to resolve an error or inconsistency discovered during data review. Queries can be created manually by individuals such as site monitors or data managers or automatically by systems. The full text of the Query exists in the Value child element. The optional Name attribute provide the means to provide a short identifier that can be included in listing or user interfaces. |
| [Question](Question.md) | A label shown to a human user when prompted to provide data for an item on paper or on a screen. |
| [RangeCheck](RangeCheck.md) | A RangeCheck defines a constraint on the value of the enclosing item. It represents an expression that evaluates to True when the ItemData value is valid or False when the ItemData value is invalid. The expression is specified using either Comparator and CheckValue or using FormalExpressions. |
| [ReasonForChange](ReasonForChange.md) | A user-supplied reason for a data change. |
| [ReferenceData](ReferenceData.md) | Reference data provides information on how to interpret clinical data. For example, reference data might include lab normal ranges. For a study that uses CDISC standards, reference data might include SDTM Trial Design datasets. |
| [RelativeTimingConstraint](RelativeTimingConstraint.md) | The RelativeTimingConstraint element describes a relative timing constraint between 2 activities or groups of activities, represented by StudyEventGroups, StudyEvents, ItemGroups, or Items. |
| [Resource](Resource.md) | Describes an external resource used as the source for the parent ItemGroup or Item.  |
| [ReturnValue](ReturnValue.md) | The ReturnValue element represents a return value used as part of a MethodSignature in MethodDef, ConditionDef, or RangeCheck. A return value identifies values passed from the Method to the calling element. A ReturnValue may be computed by a FormalExpression. |
| [Selection](Selection.md) | Template for machine-readable/executable expression for retrieving the data or information from an external resource. |
| [Signature](Signature.md) | An electronic signature applies to a collection of clinical data. This indicates that some user accepts legal responsibility for that data. See 21 CFR Part 11. The signature identifies the person signing, the location of signing, the signature meaning (via the referenced SignatureDef), the date and time of signing, and (in the case of a digital signature) an encrypted hash of the included data. |
| [SignatureDef](SignatureDef.md) | Provides Metadata for signatures included in the /ODM/ClinicalData. |
| [SignatureRef](SignatureRef.md) | Element NameSignatureRefParent ElementsSignatureElement XPath(s)/ODM/ReferenceData/Signature/SignatureRef/ODM/ReferenceData/ItemGroupData/Signature/SignatureRef/ODM/ReferenceData/ItemGroupData/ItemData/Signature/SignatureRef/ODM/ClinicalData/Signature/SignatureRef/ODM/ClinicalData/ItemGroupData/Signature/SignatureRef/ODM/ClinicalData/ItemGroupData/ItemData/Signature/SignatureRef/ODM/ClinicalData/SubjectData/Signature/SignatureRef/ODM/ClinicalData/SubjectData/StudyEventData/Signature/SignatureRef/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/Signature/SignatureRef/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/Signature/SignatureRefElement Textual ValueNoneAttributesSignatureOIDChild ElementsNoneUsage/Business Rules |
| [SiteRef](SiteRef.md) | lement NameSiteRefParent ElementsSubjectDataElement XPath(s)/ODM/ClinicalData/SubjectData/SiteRefElement Textual ValueNoneAttributesLocationOIDChild ElementsNoneUsage/Business RulesBusiness Rule(s):Must be provided when the /ODM/FileType is Transactional. |
| [SourceID](SourceID.md) | Information that identifies the source of the data within an originating system. |
| [SourceItem](SourceItem.md) | Provides the information needed to identify the source metadata. |
| [SourceItems](SourceItems.md) | Identifies source items as needed to support automated data capture and end-to-end traceability. |
| [Standard](Standard.md) | The Standard element describes each standard used within the MetaDataVersion element. |
| [Standards](Standards.md) | The Standards element provides a container for the list of Standard elements referenced in the MetaDataVersion for the Study.. |
| [StateProv](StateProv.md) | The state or province name part of a user's postal address. |
| [StreetName](StreetName.md) | The street name part of a user's postal address. |
| [Study](Study.md) | This element collects static structural information about an individual study.Element NameStudyParent ElementsODMElement XPath(s)/ODM/StudyElement Textual ValueNone AttributesOID, StudyName, ProtocolName, VersionID, VersionName, StatusChild Elements(Description?, MetaDataVersion*)Usage/Business RulesBusiness Rule(s): Required when ODM/@Granularity is in (All | Metadata) |
| [StudyEndPoint](StudyEndPoint.md) | A study end point reflects an outcome measure of interest that is statistically analyzed to address a particular research question for the study. It typically specifies the type of assessments made; the timing of those assessments; the assessment tools used; and other details, as applicable, such as how multiple assessments within an individual are to be combined. |
| [StudyEndPointRef](StudyEndPointRef.md) | Go to start of metadata |
| [StudyEndPoints](StudyEndPoints.md) | Go to start of metadata |
| [StudyEstimand](StudyEstimand.md) | Element NameStudyEstimandParent ElementsStudyEstimandsElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimandElement Textual ValueNoneAttributesOID, NameChild Elements(Description?, StudyTargetPopulationRef?, StudyInterventionRef?, StudyEndpointRef?, IntercurrentEvent*, SummaryMeasure?)Usage/Business Rules |
| [StudyEstimands](StudyEstimands.md) | Element NameStudyEstimandsParent ElementsProtocolElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimandsElement Textual ValueNoneUsage/Business RulesAttributesTypeChild Elements(StudyEstimand*) |
| [StudyEventData](StudyEventData.md) | Clinical data for a study event (visit). The model supports repeating study events (e.g., when the same set of information is collected for a series of patient visits). |
| [StudyEventDef](StudyEventDef.md) | StudyEventDef represents the definition of an activity in a study where data is collected. For example, a study event may represent a set of item groups that represent data collection instruments to be completed for a subject during a visit in a study. The visit occurs as part of a study workflow, and the workflow is referenced in the study event. |
| [StudyEventGroupDef](StudyEventGroupDef.md) | StudyEventGroupDef is a study building block that groups a number of smaller building blocks, which can themselves be StudyEventGroups or StudyEvents. It thus allows nesting of building blocks. |
| [StudyEventGroupRef](StudyEventGroupRef.md) | This element references a StudyEventGroupDef as it occurs within a specific version of a study. The list of StudyEventGroupRefs identifies the types of study group events that are allowed to occur within the study. |
| [StudyEventRef](StudyEventRef.md) | This element references a StudyEventDef as it occurs within a specific version of a study. The list of StudyEventRefs identifies the types of study events that are allowed to occur within the study.  |
| [StudyIndication](StudyIndication.md) | This element describes a study indication (e.g., condition, disease) for the clinical study. The human-readable description is provided in the Description element. The Coding element can be used to provide a machine-readable code for the indication (e.g., SNOMED-CT code 26929004 for "Alzheimer's disease"). |
| [StudyIndications](StudyIndications.md) | StudyIndications is a container element for individual StudyIndication elements. |
| [StudyIntervention](StudyIntervention.md) | This element describes a study intervention (e.g., medication, treatment, therapy) for the clinical study. The human-readable description is provided in the Description element. The Coding element can be used to provide a machine-readable code for the indication (e.g., ATC M01AE01 code for "Ibuprofen" when used as a nonsteroidal anti-inflammatory drug). |
| [StudyInterventionRef](StudyInterventionRef.md) | Element NameStudyInterventionRefParent ElementsStudyEstimandElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimandElement Textual ValueNoneAttributesStudyInterventionOIDChild ElementsNoneUsage/Business RulesOptional |
| [StudyInterventions](StudyInterventions.md) | The StudyInterventions element is a container element for individual StudyIntervention elements.Element NameStudyInterventionsParent Element(s)ProtocolElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyInterventionsElement Text ValueNoneAttributesNoneChild Elements(StudyIntervention+)Usage/Business Rules |
| [StudyObjective](StudyObjective.md) | Element NameStudyObjectiveParent ElementStudyObjectivesElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyObjectives/StudyObjectiveElement Textual ValueNoneAttributesOID, Name, LevelChild Elements (Description?, StudyEndPointRef*)Usage/Business Rules |
| [StudyObjectives](StudyObjectives.md) | The StudyObjectives is a container element for individual StudyObjective elements. |
| [StudyParameter](StudyParameter.md) | A StudyParameter defines a study design parameter for which the value or values are delivered in the ParameterValue child element or elements. |
| [StudyStructure](StudyStructure.md) | The StudyStructure element describes the general structure of a clinical study with arms, epochs, and workflows. |
| [StudySummary](StudySummary.md) | The StudyParameter element allows to provide a set of study design parameters such as anticipated number of subjects, minimum and maximum age of the participants, or planned number of arms. |
| [StudyTargetPopulation](StudyTargetPopulation.md) | The StudyTargetPopulation describes the population targeted for the clinical study. |
| [StudyTargetPopulationRef](StudyTargetPopulationRef.md) | Element NameStudyTargetPopulationRefParent ElementsStudyEstimandElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimand/StudyTargetPopulationRefElement Textual ValueNoneAttributesStudyTargetPopulationOIDChild ElementsNoneUsage/Business Rules |
| [StudyTiming](StudyTiming.md) | The StudyTiming element defines a timing constraint within the study, which can be an absolute timing constraint (e.g., start of the screening visit must be between 1 January 2022 and 31 December 2022), a relative timing constraint (e.g., visit 2 must be within 30 days after visit 1 with a window of +/- 1 week), a transition timing constraint (i.e., timing constraint on a transition within a defined workflow), or a duration timing constraint (e.g., the duration of visit 2 is planned to take hours with a window of 30 minutes). |
| [StudyTimings](StudyTimings.md) | The StudyTimings element is a container element for individual StudyTiming elements. |
| [SubClass](SubClass.md) | This element contains SubClass definitions. |
| [SubjectData](SubjectData.md) | Clinical data for a single subject. |
| [Suffix](Suffix.md) | This element may include credentials, or suffixes (e.g., Jr., III). |
| [SummaryMeasure](SummaryMeasure.md) | Element NameSummaryMeasureParent ElementsStudyEstimandElement XPath(s)/ODM/Study/MetaDataVersion/Protocol/StudyEstimands/StudyEstimand/SummaryMeasureElement Textual ValueNoneAttributesNoneChild ElementsDescriptionUsage/Business Rules |
| [SupplementalDoc](SupplementalDoc.md) | Supplemental data definitions |
| [TargetTransition](TargetTransition.md) | Provides a reference to a Transition element. |
| [Telecom](Telecom.md) | The telecommunication contacts points of a user, a location, or an organization. The Type attribute designates the type of contact. |
| [Transition](Transition.md) | A Transition defines a link between 2 structural elements in a workflow. When the execution of the transition is dependent upon a timing constraint that is either directly defined or calculated, a TransitionTimingConstraint must be defined, referencing the current Transition.  |
| [TransitionTimingConstraint](TransitionTimingConstraint.md) | The TransitionTimingConstraint element defines a timing constraint on a transition between structural elements as defined in a workflow. As such, it is a non-blocking constraint. This means that the transition is set on hold as long as the timing condition is not fulfilled, and is executed as soon as the timing condition is fulfilled. |
| [TranslatedText](TranslatedText.md) | Human-readable text that is appropriate for a particular language. TranslatedText elements typically occur in a series, presenting a set of alternative textual renditions for different languages and types. |
| [TrialPhase](TrialPhase.md) | The TrialPhase element designates the phase of the study in the clinical trial. |
| [User](User.md) | Information about a specific user of a clinical data collection or data management system. |
| [UserName](UserName.md) | The user's login identification in the sender's system. |
| [UserRef](UserRef.md) | Element NameUserRefParent ElementsAuditRecord, SignatureElement XPath(s)/ODM/AdminData/Location/Query/AuditRecord/ODM/ClinicalData/Query/AuditRecord/ODM/ClinicalData/SubjectData/AuditRecord/ODM/ClinicalData/SubjecData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEvent/AuditRecord/ODM/ClinicalData/SubjecData/StudyEvent/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/AuditRecord/ODM/ClinicalData/SubjecData/StudyEvent/ItemGroupData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/ItemData/AuditRecord/ODM/ClinicalData/SubjecData/StudyEvent/ItemGroupData/ItemData/Query/AuditRecord/ODM/ClinicalData/SubjectData/Signature/ODM/ClinicalData/SubjectData/StudyEvent/Signature/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/Signature/ODM/ClinicalData/SubjectData/StudyEvent/ItemGroupData/ItemData/SignatureElement Textual ValueNoneAttributesUserOIDChild ElementsNoneUsage/Business Rules |
| [Value](Value.md) | The data collected for an item. This data is represented according to DataType attribute of the ItemDef referenced by the ItemOID attribute in the parent ItemData element. |
| [ValueListDef](ValueListDef.md) | The following table specifies the XML structure for valuelist metadata. The ValueListDef element contains ItemRef elements that reference ItemDef elements that provide the value-level metadata details |
| [ValueListRef](ValueListRef.md) | The ValueListRef element is the OID of the ValueListDef that contains the valuelist definition associated with the variable. If value-level metadata is required for a variable, a ValueListRef element should be provided as a child element on the ItemDef for the variable definition. |
| [WhereClauseDef](WhereClauseDef.md) | The WhereClauseDef element specifies a condition. |
| [WhereClauseRef](WhereClauseRef.md) | The WhereClauseRef references the WhereClauseDef element that describes the conditions under which the variable values are defined by the referenced ItemDef. |
| [WorkflowDef](WorkflowDef.md) | A WorkflowDef defines an automated workflow for a study. |
| [WorkflowEnd](WorkflowEnd.md) | A WorkflowEnd references a structural element with which the workflows ends. |
| [WorkflowRef](WorkflowRef.md) | The WorkflowRef references a workflow definition |
| [WorkflowStart](WorkflowStart.md) | WorkflowStart references a structural element that begins the automated workflow. |



## Slots

| Slot | Description |
| --- | --- |
| [_content](_content.md) | multi-line text content from between XML tags |
| [_language](_language.md) | language context for internationalisation and localisation |
| [AbsoluteTimingConstraintRef](AbsoluteTimingConstraintRef.md) |  |
| [AddressRef](AddressRef.md) |  |
| [AdminDataRef](AdminDataRef.md) |  |
| [AliasRef](AliasRef.md) |  |
| [Altitude](Altitude.md) | Height above sea level in meters |
| [AnnotatedCRFRef](AnnotatedCRFRef.md) |  |
| [AnnotationRef](AnnotationRef.md) |  |
| [ArchiveLocationID](ArchiveLocationID.md) | Reference to the unique ID of a leaf element that provides the actual locatio... |
| [ArmOID](ArmOID.md) | Reference to an Arm element defined in the study |
| [ArmRef](ArmRef.md) |  |
| [AsOfDateTime](AsOfDateTime.md) | The date/time at which the source database was queried in order to create thi... |
| [AssociationRef](AssociationRef.md) |  |
| [Attribute](Attribute.md) | Field provided by the Name attribute where the data or information can be obt... |
| [AuditRecordRef](AuditRecordRef.md) |  |
| [BranchingRef](BranchingRef.md) |  |
| [Category](Category.md) | The Category attribute is typically used to indicate the study phase appropri... |
| [CDISCNotesRef](CDISCNotesRef.md) |  |
| [CheckValueRef](CheckValueRef.md) |  |
| [CityRef](CityRef.md) |  |
| [ClassRef](ClassRef.md) |  |
| [ClinicalDataRef](ClinicalDataRef.md) |  |
| [CodedValue](CodedValue.md) | Value of the codelist item (as it would occur in clinical data) |
| [CodeListItemRef](CodeListItemRef.md) |  |
| [CodeListOID](CodeListOID.md) | Reference to the CodeList definition that provides the allowable values for I... |
| [CodeListRefRef](CodeListRefRef.md) |  |
| [CodeRef](CodeRef.md) | A string pattern that identifies a concept as defined by the code system |
| [CodingRef](CodingRef.md) |  |
| [CollectionExceptionConditionOID](CollectionExceptionConditionOID.md) | Reference to a ConditionDef |
| [CommentDefRef](CommentDefRef.md) |  |
| [CommentOID](CommentOID.md) | The Comment identifier that this value refers to |
| [CommentRef](CommentRef.md) |  |
| [ComparatorRef](ComparatorRef.md) | Comparison operator used to compare the item and value(s) |
| [ConditionDefRef](ConditionDefRef.md) |  |
| [ConditionOID](ConditionOID.md) | Reference to a ConditionDef defining the condition under which the transition... |
| [ContextRef](ContextRef.md) | Identifies applicable domain or scope of the mapping |
| [Core](Core.md) | CDASH, ADaM, SDTM, and SEND Core designations |
| [CountryRef](CountryRef.md) |  |
| [CreationDateTime](CreationDateTime.md) | Time of creation of the file containing the document |
| [CRFCompletionInstructionsRef](CRFCompletionInstructionsRef.md) |  |
| [CriterionRef](CriterionRef.md) |  |
| [DatasetName](DatasetName.md) | Name of a file containing the ItemGroupData for this ItemGroupDef |
| [DataTypeRef](DataTypeRef.md) | The DataType attribute specifies how the corresponding value |
| [DateTimeStampRef](DateTimeStampRef.md) |  |
| [DecodeRef](DecodeRef.md) |  |
| [DefaultTransitionRef](DefaultTransitionRef.md) |  |
| [DefinitionRef](DefinitionRef.md) | A free-text definition of the parameter |
| [DescriptionRef](DescriptionRef.md) |  |
| [Dictionary](Dictionary.md) |  |
| [DisplayFormat](DisplayFormat.md) | Display format supports data visualization of numeric float and date values |
| [DocumentRefRef](DocumentRefRef.md) | The DocumentRef element is a container for page references in a PDF file |
| [Domain](Domain.md) | Identifies the scope or CDISC SDTMIG/SENDIG Domain of the ItemGroup data |
| [DurationPostWindow](DurationPostWindow.md) |  |
| [DurationPreWindow](DurationPreWindow.md) |  |
| [DurationTarget](DurationTarget.md) |  |
| [DurationTimingConstraintRef](DurationTimingConstraintRef.md) |  |
| [EditPoint](EditPoint.md) | Identifies the phase of data processing in which update action occurred |
| [EffectiveDate](EffectiveDate.md) | Datetime stamp when this MetaDataVersion was published at this location |
| [EndConditionOID](EndConditionOID.md) | The EndConditionOID references a ConditionDef defining the condition under wh... |
| [EndOID](EndOID.md) | Reference to the definition of the structural element that ends the workflow |
| [EpochOID](EpochOID.md) | Reference to an Epoch element defined in the study |
| [EpochRef](EpochRef.md) |  |
| [ErrorMessageRef](ErrorMessageRef.md) |  |
| [ExclusionCriteriaRef](ExclusionCriteriaRef.md) |  |
| [ExtendedValue](ExtendedValue.md) |  |
| [ExternalCodeLibRef](ExternalCodeLibRef.md) |  |
| [FamilyNameRef](FamilyNameRef.md) |  |
| [FileOID](FileOID.md) | A unique identifier for this file |
| [FileTypeRef](FileTypeRef.md) | Snapshot means that the document contains only the current state of the data ... |
| [FirstPage](FirstPage.md) | First page in a range of pages |
| [FlagRef](FlagRef.md) |  |
| [FlagTypeRef](FlagTypeRef.md) |  |
| [FlagValueRef](FlagValueRef.md) |  |
| [FormalExpressionRef](FormalExpressionRef.md) |  |
| [FullNameRef](FullNameRef.md) |  |
| [GeoPositionRef](GeoPositionRef.md) |  |
| [GivenNameRef](GivenNameRef.md) |  |
| [GranularityRef](GranularityRef.md) | Granularity is intended to give the sender a shorthand way to Describes the s... |
| [HasNoData](HasNoData.md) | Used to indicate that an ItemGroupDef has no data |
| [HouseNumberRef](HouseNumberRef.md) |  |
| [href](href.md) | URL that can be used to identify the location of a document or dataset file r... |
| [ID](ID.md) | Unique identifier for the leaf that is referenced |
| [ImageFileName](ImageFileName.md) | The file name of or file path to the picture |
| [ImageRef](ImageRef.md) |  |
| [ImplementationNotesRef](ImplementationNotesRef.md) |  |
| [IncludeRef](IncludeRef.md) |  |
| [InclusionCriteriaRef](InclusionCriteriaRef.md) |  |
| [InclusionExclusionCriteriaRef](InclusionExclusionCriteriaRef.md) |  |
| [IntercurrentEventRef](IntercurrentEventRef.md) |  |
| [InvestigatorRefRef](InvestigatorRefRef.md) |  |
| [IsNonStandard](IsNonStandard.md) | Required for ADaM, SDTM, or SEND if StandardOID is not provided |
| [IsNull](IsNull.md) | Flag specifying that an item's value is to be set to null |
| [IsReferenceData](IsReferenceData.md) | Specifies whether this ItemGroupDef is used for non-subject data |
| [ItemDataRef](ItemDataRef.md) |  |
| [ItemDefRef](ItemDefRef.md) |  |
| [ItemGroupDataRef](ItemGroupDataRef.md) |  |
| [ItemGroupDataSeq](ItemGroupDataSeq.md) | Unique sequence # for each ItemGroupData child element (record) in the contai... |
| [ItemGroupDefRef](ItemGroupDefRef.md) |  |
| [ItemGroupOID](ItemGroupOID.md) | Reference to the ItemGroupDef  |
| [ItemGroupRefRef](ItemGroupRefRef.md) |  |
| [ItemGroupRepeatKey](ItemGroupRepeatKey.md) | A key used to distinguish between repeats of the same type of item group |
| [ItemOID](ItemOID.md) | Reference to the ItemDef  |
| [ItemRefRef](ItemRefRef.md) |  |
| [KeySequence](KeySequence.md) | Indicates that this item is a key for the enclosing element |
| [KeySetRef](KeySetRef.md) |  |
| [Label](Label.md) | Used to link the value to a named MethodDef parameter |
| [LastPage](LastPage.md) | Last page in a range of pages |
| [LastUpdateDatetime](LastUpdateDatetime.md) | When was this Query updated? Will correspond to the creation date or the last... |
| [Latitude](Latitude.md) | Latitude component of geoposition coordinate in decimal degrees degrees |
| [leafID](leafID.md) | References a leaf element that provides a reference to another ODM document |
| [LeafID](LeafID.md) | Unique identifier for the Leaf element with the document location |
| [LeafRef](LeafRef.md) |  |
| [LegalReasonRef](LegalReasonRef.md) |  |
| [Length](Length.md) | The Length attribute is optional when DataType is text, string, |
| [Level](Level.md) | Defined level for the Study Objective |
| [Library](Library.md) | The name of the external library containing the FormalExpression |
| [LocationOID](LocationOID.md) | Reference to a Location element |
| [LocationRefRef](LocationRefRef.md) |  |
| [Longitude](Longitude.md) | Longitude component of geoposition coordinates in decimal degrees |
| [Mandatory](Mandatory.md) | Indicator of whether this StudyEventGroup must appear in the study clinical d... |
| [MeaningRef](MeaningRef.md) |  |
| [MetaDataVersionOID](MetaDataVersionOID.md) | References a prior MetaDataVersion within the Study referenced by the StudyOI... |
| [MetaDataVersionRefRef](MetaDataVersionRefRef.md) |  |
| [Method](Method.md) | The name of the method or function that contains the FormalExpression code |
| [MethodDefRef](MethodDefRef.md) |  |
| [MethodOID](MethodOID.md) | Reference to a MethodDef that will provide one or more data rows as output |
| [Methodology](Methodology.md) | Defines the type of electronic signature, including the meaning as required b... |
| [MethodSignatureRef](MethodSignatureRef.md) |  |
| [MimeType](MimeType.md) | Media type of the image |
| [Name](Name.md) | General observation Sub Class |
| [ODMVersionRef](ODMVersionRef.md) | The version of the ODM standard used |
| [OID](OID.md) | Unique identifier of the version within the XML document |
| [OrderNumber](OrderNumber.md) | Indicates the order in which this StudyEventGroup appears in Metadata display... |
| [OrganizationOID](OrganizationOID.md) | Reference to an Organization elment |
| [OrganizationRef](OrganizationRef.md) |  |
| [Originator](Originator.md) | The organization that generated the ODM file |
| [OriginRef](OriginRef.md) |  |
| [Other](Other.md) | Flag to indicate that the Item represents "other" content added to an ItemGro... |
| [OtherTextRef](OtherTextRef.md) |  |
| [PageRefs](PageRefs.md) | List of PDF pages separated by a space |
| [ParameterRef](ParameterRef.md) |  |
| [ParameterValueRef](ParameterValueRef.md) |  |
| [ParentClass](ParentClass.md) | Parent class of the Sub Class |
| [PartOfOrganizationOID](PartOfOrganizationOID.md) | Reference to a parent organization |
| [Path](Path.md) | Provides the machine-executable instruction or template for it to obtain the ... |
| [PDFPageRefRef](PDFPageRefRef.md) | The PDFPageRef element is a container for page references in a PDF file |
| [PostalCodeRef](PostalCodeRef.md) |  |
| [PredecessorOID](PredecessorOID.md) | Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item that occurs immed... |
| [PrefixRef](PrefixRef.md) |  |
| [PreSpecifiedValue](PreSpecifiedValue.md) | Prefill value or a default value for a field that is automatically populated |
| [PriorFileOID](PriorFileOID.md) | Reference to the previous file (if any) in a series |
| [PromptRef](PromptRef.md) |  |
| [ProtocolName](ProtocolName.md) | P rotocol identifier or protocol number assigned to the study  |
| [ProtocolRef](ProtocolRef.md) |  |
| [PublishingSet](PublishingSet.md) | Set of published files of Standard when Type="CT" (e |
| [Purpose](Purpose.md) | Purpose of the ItemGroup |
| [QueryRef](QueryRef.md) |  |
| [QuestionRef](QuestionRef.md) |  |
| [RangeCheckRef](RangeCheckRef.md) |  |
| [Rank](Rank.md) | Numeric significance of the CodeListItem relative to others in the CodeList |
| [ReasonForChangeRef](ReasonForChangeRef.md) |  |
| [ref](ref.md) | Reference to a local instance (e |
| [ReferenceDataRef](ReferenceDataRef.md) |  |
| [RelativeTimingConstraintRef](RelativeTimingConstraintRef.md) |  |
| [Repeat](Repeat.md) | Indicates that the item serves as the item over which repeats are to be perfo... |
| [Repeating](Repeating.md) | The Repeating flag indicates when this type of study event can occur repeated... |
| [RepeatingLimit](RepeatingLimit.md) | Maximum number of repeats |
| [ResourceRef](ResourceRef.md) |  |
| [ReturnValueRef](ReturnValueRef.md) |  |
| [Role](Role.md) | The Role for the referenced ItemDef |
| [RoleCodeListOID](RoleCodeListOID.md) | Reference to a CodeList that defines the allowable values of Role for the Stu... |
| [SelectionRef](SelectionRef.md) |  |
| [SeqNum](SeqNum.md) | When more than 1 Value element exists this attribute uniquely identifies each... |
| [SequenceNumber](SequenceNumber.md) | Order of the Epoch  |
| [ShortName](ShortName.md) | Short name or code for the parameter |
| [SignatureDefRef](SignatureDefRef.md) |  |
| [SignatureOID](SignatureOID.md) | Reference to the SignatureDef  |
| [SignatureRefRef](SignatureRefRef.md) |  |
| [SiteRefRef](SiteRefRef.md) |  |
| [SoftHard](SoftHard.md) | Type of range check |
| [Source](Source.md) | I ndicates the party responsible for the data's origin type |
| [SourceIDRef](SourceIDRef.md) |  |
| [SourceItemRef](SourceItemRef.md) |  |
| [SourceItemsRef](SourceItemsRef.md) |  |
| [SourceOID](SourceOID.md) | References the definition of the source structural element for the transition |
| [SourceSystem](SourceSystem.md) | The computer system or database management system that is the source of the i... |
| [SourceSystemVersion](SourceSystemVersion.md) | The version of the "SourceSystem" above |
| [SponsorOrSite](SponsorOrSite.md) | Source of the comment |
| [StandardOID](StandardOID.md) | Reference to a Standard element |
| [StandardRef](StandardRef.md) | Definition of a standard referenced in the Define-XML document |
| [StandardsRef](StandardsRef.md) |  |
| [StartConditionOID](StartConditionOID.md) | The StartConditionOID references a ConditionDef specifying a condition that m... |
| [StartOID](StartOID.md) | Reference to the definition of the structural element that starts the workflo... |
| [State](State.md) | Status of the Query |
| [StateProvRef](StateProvRef.md) |  |
| [Status](Status.md) | Status of Standard |
| [StreetNameRef](StreetNameRef.md) |  |
| [StructuralElementOID](StructuralElementOID.md) |  |
| [Structure](Structure.md) | Description of the level of detail represented by individual records in the I... |
| [StudyEndPointOID](StudyEndPointOID.md) | Reference to the StudyEndPoint  |
| [StudyEndPointRefRef](StudyEndPointRefRef.md) |  |
| [StudyEndPointsRef](StudyEndPointsRef.md) |  |
| [StudyEstimandRef](StudyEstimandRef.md) |  |
| [StudyEstimandsRef](StudyEstimandsRef.md) |  |
| [StudyEventDataRef](StudyEventDataRef.md) |  |
| [StudyEventDefRef](StudyEventDefRef.md) |  |
| [StudyEventGroupDefRef](StudyEventGroupDefRef.md) |  |
| [StudyEventGroupOID](StudyEventGroupOID.md) | Reference to the StudyEventGroupDef  |
| [StudyEventGroupRefRef](StudyEventGroupRefRef.md) |  |
| [StudyEventOID](StudyEventOID.md) | Reference to the StudyEventDef  |
| [StudyEventRefRef](StudyEventRefRef.md) |  |
| [StudyEventRepeatKey](StudyEventRepeatKey.md) | A key used to distinguish between repeats of the same type of study event for... |
| [StudyIndicationRef](StudyIndicationRef.md) |  |
| [StudyIndicationsRef](StudyIndicationsRef.md) |  |
| [StudyInterventionOID](StudyInterventionOID.md) | Reference to a StudyIntervention |
| [StudyInterventionRefRef](StudyInterventionRefRef.md) |  |
| [StudyInterventionsRef](StudyInterventionsRef.md) |  |
| [StudyName](StudyName.md) | Sponsoring organization's internal name for the study |
| [StudyObjectiveRef](StudyObjectiveRef.md) |  |
| [StudyObjectivesRef](StudyObjectivesRef.md) |  |
| [StudyOID](StudyOID.md) | References the Study that provides a prior metadata version |
| [StudyParameterRef](StudyParameterRef.md) |  |
| [StudyRef](StudyRef.md) |  |
| [StudyStructureRef](StudyStructureRef.md) |  |
| [StudySummaryRef](StudySummaryRef.md) |  |
| [StudyTargetPopulationOID](StudyTargetPopulationOID.md) |  |
| [StudyTargetPopulationRefRef](StudyTargetPopulationRefRef.md) |  |
| [StudyTimingRef](StudyTimingRef.md) |  |
| [StudyTimingsRef](StudyTimingsRef.md) |  |
| [SubClassRef](SubClassRef.md) |  |
| [SubjectDataRef](SubjectDataRef.md) |  |
| [SubjectKey](SubjectKey.md) | Unique identifier for the Subject |
| [SuccessorOID](SuccessorOID.md) | Identifies a StudyEventGroup, StudyEvent, ItemGroup or Item tha occurs immedi... |
| [SuffixRef](SuffixRef.md) |  |
| [SummaryMeasureRef](SummaryMeasureRef.md) |  |
| [SupplementalDocRef](SupplementalDocRef.md) |  |
| [System](System.md) | Identifies the code system that defines the code |
| [SystemName](SystemName.md) | Human readable name for the code system |
| [SystemVersion](SystemVersion.md) | Identifies the version of the code system |
| [Target](Target.md) | Element upon which the Query is raised |
| [TargetOID](TargetOID.md) | References the definition of the target structural element for the transition |
| [TargetTransitionOID](TargetTransitionOID.md) | Reference to the Transition that is one of the targets of the branching |
| [TargetTransitionRef](TargetTransitionRef.md) |  |
| [TelecomRef](TelecomRef.md) |  |
| [TelecomType](TelecomType.md) |  |
| [Term](Term.md) | Longer name |
| [TimepointPostWindow](TimepointPostWindow.md) | Specifies the amount of time after the TimepointTarget, the time between the ... |
| [TimepointPreWindow](TimepointPreWindow.md) | Specifies the amount of time prior to the TimepointTarget, the time between t... |
| [TimepointRelativeTarget](TimepointRelativeTarget.md) | The relative timing between two activities or groups of activities |
| [TimepointTarget](TimepointTarget.md) | The planned time between the 2 activities defined by the transition in the wo... |
| [Title](Title.md) | Text with the label for the document reference |
| [TransactionTypeRef](TransactionTypeRef.md) | Identifies the transaction type when /ODM/@FileType is Transactional and ther... |
| [TransitionOID](TransitionOID.md) | References the workflow Transition on which the timing constraint must be exe... |
| [TransitionRef](TransitionRef.md) |  |
| [TransitionTimingConstraintRef](TransitionTimingConstraintRef.md) |  |
| [TranslatedTextRef](TranslatedTextRef.md) |  |
| [TrialPhaseRef](TrialPhaseRef.md) |  |
| [Type](Type.md) | Type of page for page references indicated in the PageRefs attribute |
| [UnitsItemOID](UnitsItemOID.md) | Reference to a sibling ItemRef element that represents the unit specification... |
| [UsedMethod](UsedMethod.md) | Indicates that the action was made by the system rather than a data entry for... |
| [UserNameRef](UserNameRef.md) |  |
| [UserOID](UserOID.md) | Reference to a User definition |
| [UserRefRef](UserRefRef.md) |  |
| [UserTypeRef](UserTypeRef.md) | User's role in the study |
| [ValueListDefRef](ValueListDefRef.md) |  |
| [ValueListOID](ValueListOID.md) | Reference to the unique ID of a ValueListDef element that provides value-leve... |
| [ValueListRefRef](ValueListRefRef.md) |  |
| [ValueRef](ValueRef.md) | Human-readable designation of the trial phase |
| [VariableSet](VariableSet.md) | ADaM variable set, e |
| [Version](Version.md) | Version of Standard |
| [VersionID](VersionID.md) | Identifier for the specific version of the study in the source system that th... |
| [VersionName](VersionName.md) | Short descriptive label for the version of the study, e |
| [WhereClauseDefRef](WhereClauseDefRef.md) |  |
| [WhereClauseOID](WhereClauseOID.md) | Reference to the unique ID of a WhereClauseDef element |
| [WhereClauseRefRef](WhereClauseRefRef.md) |  |
| [WorkflowDefRef](WorkflowDefRef.md) |  |
| [WorkflowEndRef](WorkflowEndRef.md) |  |
| [WorkflowOID](WorkflowOID.md) | Reference to a WorfkflowDef |
| [WorkflowRefRef](WorkflowRefRef.md) |  |
| [WorkflowStartRef](WorkflowStartRef.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [BranchingType](BranchingType.md) |  |
| [CLDataType](CLDataType.md) |  |
| [CommentType](CommentType.md) |  |
| [Comparator](Comparator.md) |  |
| [Context](Context.md) |  |
| [DataType](DataType.md) |  |
| [DefCoreType](DefCoreType.md) |  |
| [DictionaryNameTypeEnum](DictionaryNameTypeEnum.md) |  |
| [EditPointType](EditPointType.md) |  |
| [EventType](EventType.md) |  |
| [FileType](FileType.md) |  |
| [Granularity](Granularity.md) |  |
| [ItemGroupClass](ItemGroupClass.md) |  |
| [ItemGroupRepeatingType](ItemGroupRepeatingType.md) |  |
| [ItemGroupSubClass](ItemGroupSubClass.md) |  |
| [ItemGroupTypeTypeEnum](ItemGroupTypeTypeEnum.md) |  |
| [MethodType](MethodType.md) |  |
| [ODMCoreType](ODMCoreType.md) |  |
| [OrganizationType](OrganizationType.md) |  |
| [OriginSource](OriginSource.md) |  |
| [OriginType](OriginType.md) |  |
| [PDFPageType](PDFPageType.md) |  |
| [QuerySourceType](QuerySourceType.md) |  |
| [QueryStateType](QueryStateType.md) |  |
| [QueryType](QueryType.md) |  |
| [RelativeTimingConstraintType](RelativeTimingConstraintType.md) |  |
| [SignMethod](SignMethod.md) |  |
| [SoftOrHard](SoftOrHard.md) |  |
| [StandardName](StandardName.md) |  |
| [StandardPublishingSet](StandardPublishingSet.md) |  |
| [StandardStatusEnum](StandardStatusEnum.md) |  |
| [StandardType](StandardType.md) |  |
| [StudyEndPointType](StudyEndPointType.md) |  |
| [StudyEstimandLevel](StudyEstimandLevel.md) |  |
| [StudyObjectiveLevel](StudyObjectiveLevel.md) |  |
| [TelecomTypeType](TelecomTypeType.md) |  |
| [TransactionType](TransactionType.md) |  |
| [TrialPhaseTypeEnum](TrialPhaseTypeEnum.md) |  |
| [UserType](UserType.md) |  |
| [YesOnly](YesOnly.md) |  |
| [YesOrNo](YesOrNo.md) |  |


## Types

| Type | Description |
| --- | --- |
| [ContentType](ContentType.md) | multi-line text content from between XML tags |
| [LanguageType](LanguageType.md) | language context for internationalisation and localisation |
| [Base64Binary](Base64Binary.md) |  |
| [Base64Float](Base64Float.md) |  |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [CoreType](CoreType.md) | Core |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [DictionaryNameType](DictionaryNameType.md) | A name given to a reference source that lists words and gives their |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [DurationDatetime](DurationDatetime.md) |  |
| [EmptyTag](EmptyTag.md) |  |
| [FileName](FileName.md) |  |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [HexBinary](HexBinary.md) |  |
| [HexFloat](HexFloat.md) |  |
| [IncompleteDate](IncompleteDate.md) |  |
| [IncompleteDatetime](IncompleteDatetime.md) |  |
| [IncompleteTime](IncompleteTime.md) |  |
| [Integer](Integer.md) | An integer |
| [IntervalDatetime](IntervalDatetime.md) |  |
| [ItemGroupClassSubClass](ItemGroupClassSubClass.md) | Sub class of a general observation class |
| [ItemGroupTypeType](ItemGroupTypeType.md) |  |
| [Name](Name.md) |  |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [ODMVersion](ODMVersion.md) | Version of ODM that the file conforms to |
| [Oid](Oid.md) |  |
| [Oidref](Oidref.md) |  |
| [PartialDate](PartialDate.md) |  |
| [PartialDatetime](PartialDatetime.md) |  |
| [PartialTime](PartialTime.md) |  |
| [PositiveInteger](PositiveInteger.md) |  |
| [RepeatKey](RepeatKey.md) |  |
| [StandardStatus](StandardStatus.md) | Terminology relevant to the development or publication status of the |
| [String](String.md) | A character string |
| [SubjectKey](SubjectKey.md) |  |
| [TDatetime](TDatetime.md) |  |
| [TDuration](TDuration.md) |  |
| [Text](Text.md) |  |
| [THour](THour.md) |  |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [TIncomplete](TIncomplete.md) |  |
| [TIncompleteDate](TIncompleteDate.md) |  |
| [TIncompleteTime](TIncompleteTime.md) |  |
| [TInterval](TInterval.md) |  |
| [TrialPhaseType](TrialPhaseType.md) | A terminology codelist relevant to the phase, or stage, of the |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |
| [Value](Value.md) |  |


## Subsets

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
| [EntryCriteriaElementExtension](EntryCriteriaElementExtension.md) |  |
| [EpochElementExtension](EpochElementExtension.md) |  |
| [ErrorMessageElementExtension](ErrorMessageElementExtension.md) |  |
| [ExceptionEventElementExtension](ExceptionEventElementExtension.md) |  |
| [ExceptionEventGroupDefinition](ExceptionEventGroupDefinition.md) |  |
| [ExclusionCriteriaElementExtension](ExclusionCriteriaElementExtension.md) |  |
| [ExitCriteriaElementExtension](ExitCriteriaElementExtension.md) |  |
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
| [SourceItemsElementExtension](SourceItemsElementExtension.md) |  |
| [StandardElementExtension](StandardElementExtension.md) |  |
| [StudyElementExtension](StudyElementExtension.md) |  |
| [StudyEndPointElementExtension](StudyEndPointElementExtension.md) |  |
| [StudyEndPointRefElementExtension](StudyEndPointRefElementExtension.md) |  |
| [StudyEndPointsElementExtension](StudyEndPointsElementExtension.md) |  |
| [StudyEstimandElementExtension](StudyEstimandElementExtension.md) |  |
| [StudyEstimandsElementExtension](StudyEstimandsElementExtension.md) |  |
| [StudyEventDataElementExtension](StudyEventDataElementExtension.md) |  |
| [StudyEventDefElementExtension](StudyEventDefElementExtension.md) |  |
| [StudyEventDefGroup](StudyEventDefGroup.md) |  |
| [StudyEventGroupDefElementExtension](StudyEventGroupDefElementExtension.md) |  |
| [StudyEventGroupRefElementExtension](StudyEventGroupRefElementExtension.md) |  |
| [StudyEventRefElementExtension](StudyEventRefElementExtension.md) |  |
| [StudyIndicationElementExtension](StudyIndicationElementExtension.md) |  |
| [StudyIndicationsElementExtension](StudyIndicationsElementExtension.md) |  |
| [StudyInterventionElementExtension](StudyInterventionElementExtension.md) |  |
| [StudyInterventionsElementExtension](StudyInterventionsElementExtension.md) |  |
| [StudyObjectiveElementExtension](StudyObjectiveElementExtension.md) |  |
| [StudyObjectivesElementExtension](StudyObjectivesElementExtension.md) |  |
| [StudyParameterElementExtension](StudyParameterElementExtension.md) |  |
| [StudyStructureElementExtension](StudyStructureElementExtension.md) |  |
| [StudySummaryElementExtension](StudySummaryElementExtension.md) |  |
| [StudyTargetPopulationElementExtension](StudyTargetPopulationElementExtension.md) |  |
| [StudyTimingElementExtension](StudyTimingElementExtension.md) |  |
| [StudyTimingsElementExtension](StudyTimingsElementExtension.md) |  |
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
