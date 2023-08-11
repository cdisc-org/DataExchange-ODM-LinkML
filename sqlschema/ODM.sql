

CREATE TABLE "Address" (
	"StreetNameRef" TEXT, 
	"HouseNumberRef" TEXT, 
	"CityRef" TEXT, 
	"StateProvRef" TEXT, 
	"CountryRef" TEXT, 
	"PostalCodeRef" TEXT, 
	"GeoPositionRef" TEXT, 
	"OtherTextRef" TEXT, 
	PRIMARY KEY ("StreetNameRef", "HouseNumberRef", "CityRef", "StateProvRef", "CountryRef", "PostalCodeRef", "GeoPositionRef", "OtherTextRef")
);

CREATE TABLE "AdminData" (
	"StudyOID" TEXT, 
	"UserRefRef" TEXT, 
	"OrganizationRef" TEXT, 
	"LocationRefRef" TEXT, 
	"SignatureDefRef" TEXT, 
	PRIMARY KEY ("StudyOID", "UserRefRef", "OrganizationRef", "LocationRefRef", "SignatureDefRef")
);

CREATE TABLE "Alias" (
	"ContextRef" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	PRIMARY KEY ("ContextRef", "Name")
);

CREATE TABLE "AnnotatedCRF" (
	"DocumentRefRef" TEXT NOT NULL, 
	PRIMARY KEY ("DocumentRefRef")
);

CREATE TABLE "Annotation" (
	"SeqNum" INTEGER NOT NULL, 
	"TransactionTypeRef" VARCHAR(7), 
	"ID" TEXT NOT NULL, 
	"CommentRef" TEXT, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("ID")
);

CREATE TABLE "Arm" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "AuditRecord" (
	"EditPoint" VARCHAR(14), 
	"UsedMethod" VARCHAR(3), 
	"UserRefRef" TEXT NOT NULL, 
	"LocationRefRef" TEXT NOT NULL, 
	"DateTimeStampRef" TEXT NOT NULL, 
	"ReasonForChangeRef" TEXT, 
	"SourceIDRef" TEXT, 
	PRIMARY KEY ("EditPoint", "UsedMethod", "UserRefRef", "LocationRefRef", "DateTimeStampRef", "ReasonForChangeRef", "SourceIDRef")
);

CREATE TABLE "Branching" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Type" VARCHAR(9) NOT NULL, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "CDISCNotes" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "CheckValue" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "City" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Class" (
	"Name" VARCHAR(40) NOT NULL, 
	"SubClassRef" TEXT, 
	PRIMARY KEY ("Name", "SubClassRef")
);

CREATE TABLE "Code" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "CodeListRef" (
	"CodeListOID" TEXT NOT NULL, 
	PRIMARY KEY ("CodeListOID")
);

CREATE TABLE "Coding" (
	"CodeRef" TEXT, 
	"System" TEXT NOT NULL, 
	"SystemName" TEXT, 
	"SystemVersion" TEXT, 
	"Label" TEXT, 
	href TEXT, 
	ref TEXT, 
	"CommentOID" TEXT, 
	PRIMARY KEY ("CodeRef", "System", "SystemName", "SystemVersion", "Label", href, ref, "CommentOID")
);

CREATE TABLE "Comment" (
	"SponsorOrSite" VARCHAR(7), 
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("SponsorOrSite", "TranslatedTextRef")
);

CREATE TABLE "Country" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "CRFCompletionInstructions" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "Criterion" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"ConditionOID" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "DateTimeStamp" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Decode" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "Definition" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "Description" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "DocumentRef" (
	"leafID" TEXT NOT NULL, 
	PRIMARY KEY ("leafID")
);

CREATE TABLE "EntryCriteria" (
	"CriterionRef" TEXT, 
	PRIMARY KEY ("CriterionRef")
);

CREATE TABLE "Epoch" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"SequenceNumber" INTEGER NOT NULL, 
	"DescriptionRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "ErrorMessage" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "ExceptionEvent" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"ConditionOID" TEXT, 
	"DescriptionRef" TEXT, 
	"WorkflowRefRef" TEXT NOT NULL, 
	"StudyEventGroupRefRef" TEXT NOT NULL, 
	"StudyEventRefRef" TEXT NOT NULL, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "ExclusionCriteria" (
	"CriterionRef" TEXT NOT NULL, 
	PRIMARY KEY ("CriterionRef")
);

CREATE TABLE "ExitCriteria" (
	"CriterionRef" TEXT, 
	PRIMARY KEY ("CriterionRef")
);

CREATE TABLE "ExternalCodeLib" (
	"Library" TEXT NOT NULL, 
	"Method" TEXT, 
	"Version" TEXT, 
	ref TEXT, 
	href TEXT, 
	PRIMARY KEY ("Library", "Method", "Version", ref, href)
);

CREATE TABLE "FamilyName" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "FlagType" (
	"CodeListOID" TEXT NOT NULL, 
	_content TEXT, 
	PRIMARY KEY ("CodeListOID", _content)
);

CREATE TABLE "FlagValue" (
	"CodeListOID" TEXT NOT NULL, 
	_content TEXT, 
	PRIMARY KEY ("CodeListOID", _content)
);

CREATE TABLE "FormalExpression" (
	"ContextRef" TEXT, 
	"CodeRef" TEXT NOT NULL, 
	"ExternalCodeLibRef" TEXT NOT NULL, 
	PRIMARY KEY ("ContextRef", "CodeRef", "ExternalCodeLibRef")
);

CREATE TABLE "FullName" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "GeoPosition" (
	"Longitude" TEXT, 
	"Latitude" TEXT, 
	"Altitude" TEXT, 
	PRIMARY KEY ("Longitude", "Latitude", "Altitude")
);

CREATE TABLE "GivenName" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "HouseNumber" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Image" (
	"ImageFileName" TEXT, 
	href TEXT, 
	"MimeType" TEXT, 
	PRIMARY KEY ("ImageFileName", href, "MimeType")
);

CREATE TABLE "ImplementationNotes" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "Include" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	href TEXT, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", href)
);

CREATE TABLE "InclusionCriteria" (
	"CriterionRef" TEXT NOT NULL, 
	PRIMARY KEY ("CriterionRef")
);

CREATE TABLE "InclusionExclusionCriteria" (
	"InclusionCriteriaRef" TEXT, 
	"ExclusionCriteriaRef" TEXT, 
	PRIMARY KEY ("InclusionCriteriaRef", "ExclusionCriteriaRef")
);

CREATE TABLE "InvestigatorRef" (
	"UserOID" TEXT NOT NULL, 
	PRIMARY KEY ("UserOID")
);

CREATE TABLE "ItemGroupRef" (
	"ItemGroupOID" TEXT NOT NULL, 
	"MethodOID" TEXT, 
	"OrderNumber" INTEGER, 
	"Mandatory" VARCHAR(3) NOT NULL, 
	"CollectionExceptionConditionOID" TEXT, 
	PRIMARY KEY ("ItemGroupOID", "MethodOID", "OrderNumber", "Mandatory", "CollectionExceptionConditionOID")
);

CREATE TABLE "ItemRef" (
	"ItemOID" TEXT NOT NULL, 
	"KeySequence" INTEGER, 
	"IsNonStandard" VARCHAR, 
	"HasNoData" VARCHAR, 
	"MethodOID" TEXT, 
	"UnitsItemOID" TEXT, 
	"Repeat" VARCHAR, 
	"Other" VARCHAR, 
	"Role" TEXT, 
	"RoleCodeListOID" TEXT, 
	"Core" TEXT, 
	"PreSpecifiedValue" TEXT, 
	"OrderNumber" INTEGER, 
	"Mandatory" VARCHAR(3) NOT NULL, 
	"CollectionExceptionConditionOID" TEXT, 
	"OriginRef" TEXT, 
	"WhereClauseRefRef" TEXT, 
	PRIMARY KEY ("ItemOID", "KeySequence", "IsNonStandard", "HasNoData", "MethodOID", "UnitsItemOID", "Repeat", "Other", "Role", "RoleCodeListOID", "Core", "PreSpecifiedValue", "OrderNumber", "Mandatory", "CollectionExceptionConditionOID", "OriginRef", "WhereClauseRefRef")
);

CREATE TABLE "KeySet" (
	"StudyOID" TEXT NOT NULL, 
	"SubjectKey" TEXT, 
	"MetaDataVersionOID" TEXT, 
	"StudyEventOID" TEXT, 
	"StudyEventRepeatKey" TEXT, 
	"ItemGroupOID" TEXT, 
	"ItemGroupRepeatKey" TEXT, 
	"ItemOID" TEXT, 
	PRIMARY KEY ("StudyOID", "SubjectKey", "MetaDataVersionOID", "StudyEventOID", "StudyEventRepeatKey", "ItemGroupOID", "ItemGroupRepeatKey", "ItemOID")
);

CREATE TABLE leaf (
	"ID" TEXT NOT NULL, 
	href TEXT NOT NULL, 
	title TEXT NOT NULL, 
	PRIMARY KEY ("ID")
);

CREATE TABLE "LegalReason" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Location" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Role" TEXT, 
	"OrganizationOID" TEXT, 
	"DescriptionRef" TEXT, 
	"AddressRef" TEXT, 
	"TelecomRef" TEXT, 
	"QueryRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "LocationRef" (
	"LocationOID" TEXT NOT NULL, 
	PRIMARY KEY ("LocationOID")
);

CREATE TABLE "Meaning" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "MethodSignature" (
	"ParameterRef" TEXT, 
	"ReturnValueRef" TEXT, 
	PRIMARY KEY ("ParameterRef", "ReturnValueRef")
);

CREATE TABLE "ODMFileMetadata" (
	"FileTypeRef" VARCHAR(13) NOT NULL, 
	"GranularityRef" VARCHAR(15), 
	"ContextRef" VARCHAR(10), 
	"FileOID" TEXT NOT NULL, 
	"CreationDateTime" DATETIME NOT NULL, 
	"PriorFileOID" TEXT, 
	"AsOfDateTime" DATETIME, 
	"ODMVersionRef" TEXT, 
	"Originator" TEXT, 
	"SourceSystem" TEXT, 
	"SourceSystemVersion" TEXT, 
	"DescriptionRef" TEXT, 
	"StudyRef" TEXT, 
	"AdminDataRef" TEXT, 
	"ReferenceDataRef" TEXT, 
	"ClinicalDataRef" TEXT, 
	"AssociationRef" TEXT, 
	PRIMARY KEY ("FileTypeRef", "GranularityRef", "ContextRef", "FileOID", "CreationDateTime", "PriorFileOID", "AsOfDateTime", "ODMVersionRef", "Originator", "SourceSystem", "SourceSystemVersion", "DescriptionRef", "StudyRef", "AdminDataRef", "ReferenceDataRef", "ClinicalDataRef", "AssociationRef")
);

CREATE TABLE "Organization" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Role" TEXT, 
	"Type" VARCHAR(18) NOT NULL, 
	"LocationOID" TEXT, 
	"PartOfOrganizationOID" TEXT, 
	"DescriptionRef" TEXT, 
	"AddressRef" TEXT, 
	"TelecomRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "Origin" (
	"Type" VARCHAR(13) NOT NULL, 
	"Source" VARCHAR(12), 
	"DescriptionRef" TEXT, 
	"SourceItemsRef" TEXT, 
	"CodingRef" TEXT, 
	"DocumentRefRef" TEXT, 
	PRIMARY KEY ("Type", "Source", "DescriptionRef", "SourceItemsRef", "CodingRef", "DocumentRefRef")
);

CREATE TABLE "OtherText" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Parameter" (
	"Name" TEXT NOT NULL, 
	"DataTypeRef" VARCHAR(18) NOT NULL, 
	"DefinitionRef" TEXT, 
	"OrderNumber" INTEGER, 
	PRIMARY KEY ("Name", "DataTypeRef", "DefinitionRef", "OrderNumber")
);

CREATE TABLE "ParameterValue" (
	"ValueRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("ValueRef", "CodingRef")
);

CREATE TABLE "PostalCode" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Prefix" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Prompt" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "Query" (
	"OID" TEXT NOT NULL, 
	"Source" VARCHAR(15) NOT NULL, 
	"Target" TEXT, 
	"Type" VARCHAR(6), 
	"State" VARCHAR(9) NOT NULL, 
	"LastUpdateDatetime" DATETIME NOT NULL, 
	"Name" TEXT, 
	"ValueRef" TEXT NOT NULL, 
	"AuditRecordRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "Question" (
	"TranslatedTextRef" TEXT NOT NULL, 
	PRIMARY KEY ("TranslatedTextRef")
);

CREATE TABLE "RangeCheck" (
	"ComparatorRef" VARCHAR(5), 
	"SoftHard" VARCHAR(4), 
	"ItemOID" TEXT, 
	"ErrorMessageRef" TEXT, 
	"MethodSignatureRef" TEXT, 
	"FormalExpressionRef" TEXT, 
	"CheckValueRef" TEXT NOT NULL, 
	PRIMARY KEY ("ComparatorRef", "SoftHard", "ItemOID", "ErrorMessageRef", "MethodSignatureRef", "FormalExpressionRef", "CheckValueRef")
);

CREATE TABLE "ReasonForChange" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "ReturnValue" (
	"Name" TEXT NOT NULL, 
	"DataTypeRef" VARCHAR(18) NOT NULL, 
	"DefinitionRef" TEXT, 
	"OrderNumber" INTEGER, 
	PRIMARY KEY ("Name", "DataTypeRef", "DefinitionRef", "OrderNumber")
);

CREATE TABLE "Selection" (
	"Path" TEXT NOT NULL, 
	PRIMARY KEY ("Path")
);

CREATE TABLE "Signature" (
	"ID" TEXT NOT NULL, 
	"UserRefRef" TEXT NOT NULL, 
	"LocationRefRef" TEXT NOT NULL, 
	"SignatureRefRef" TEXT NOT NULL, 
	"DateTimeStampRef" TEXT NOT NULL, 
	PRIMARY KEY ("ID")
);

CREATE TABLE "SignatureDef" (
	"OID" TEXT NOT NULL, 
	"Methodology" VARCHAR(10), 
	"MeaningRef" TEXT NOT NULL, 
	"LegalReasonRef" TEXT NOT NULL, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "SignatureRef" (
	"SignatureOID" TEXT NOT NULL, 
	PRIMARY KEY ("SignatureOID")
);

CREATE TABLE "SiteRef" (
	"LocationOID" TEXT NOT NULL, 
	PRIMARY KEY ("LocationOID")
);

CREATE TABLE "SourceID" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "SourceItem" (
	"ItemOID" TEXT, 
	"ItemGroupOID" TEXT, 
	"MetaDataVersionOID" TEXT, 
	"StudyOID" TEXT, 
	"leafID" TEXT NOT NULL, 
	"Name" TEXT, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("leafID")
);

CREATE TABLE "SourceItems" (
	"SourceItemRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("SourceItemRef", "CodingRef")
);

CREATE TABLE "Standard" (
	"OID" TEXT NOT NULL, 
	"Name" VARCHAR(11) NOT NULL, 
	"Type" VARCHAR(2) NOT NULL, 
	"PublishingSet" VARCHAR(10), 
	"Version" TEXT NOT NULL, 
	"Status" TEXT NOT NULL, 
	"CommentOID" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "Standards" (
	"StandardRef" TEXT NOT NULL, 
	PRIMARY KEY ("StandardRef")
);

CREATE TABLE "StateProv" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "StreetName" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Study" (
	"OID" TEXT NOT NULL, 
	"StudyName" TEXT NOT NULL, 
	"ProtocolName" TEXT NOT NULL, 
	"VersionID" TEXT, 
	"VersionName" TEXT, 
	"Status" TEXT, 
	"DescriptionRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyEndPoint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Type" VARCHAR(9), 
	"Level" VARCHAR(11), 
	"DescriptionRef" TEXT NOT NULL, 
	"FormalExpressionRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyEndPointRef" (
	"StudyEndPointOID" TEXT NOT NULL, 
	"OrderNumber" INTEGER, 
	PRIMARY KEY ("StudyEndPointOID", "OrderNumber")
);

CREATE TABLE "StudyEndPoints" (
	"StudyEndPointRefRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyEndPointRefRef")
);

CREATE TABLE "StudyEstimand" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"StudyTargetPopulationRefRef" TEXT, 
	"StudyInterventionRefRef" TEXT, 
	"StudyEndPointRefRef" TEXT, 
	"SummaryMeasureRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyEstimands" (
	"StudyEstimandRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyEstimandRef")
);

CREATE TABLE "StudyEventGroupRef" (
	"StudyEventGroupOID" TEXT NOT NULL, 
	"OrderNumber" INTEGER, 
	"Mandatory" VARCHAR(3) NOT NULL, 
	"CollectionExceptionConditionOID" TEXT, 
	"DescriptionRef" TEXT, 
	PRIMARY KEY ("StudyEventGroupOID", "OrderNumber", "Mandatory", "CollectionExceptionConditionOID", "DescriptionRef")
);

CREATE TABLE "StudyEventRef" (
	"StudyEventOID" TEXT NOT NULL, 
	"OrderNumber" INTEGER, 
	"Mandatory" VARCHAR(3) NOT NULL, 
	"CollectionExceptionConditionOID" TEXT, 
	PRIMARY KEY ("StudyEventOID", "OrderNumber", "Mandatory", "CollectionExceptionConditionOID")
);

CREATE TABLE "StudyIndication" (
	"OID" TEXT NOT NULL, 
	"DescriptionRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyIndications" (
	"StudyIndicationRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyIndicationRef")
);

CREATE TABLE "StudyIntervention" (
	"OID" TEXT NOT NULL, 
	"DescriptionRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyInterventionRef" (
	"StudyInterventionOID" TEXT NOT NULL, 
	PRIMARY KEY ("StudyInterventionOID")
);

CREATE TABLE "StudyInterventions" (
	"StudyInterventionRefRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyInterventionRefRef")
);

CREATE TABLE "StudyObjective" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Type" VARCHAR(11), 
	"DescriptionRef" TEXT, 
	"StudyEndPointRefRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyObjectives" (
	"StudyObjectiveRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyObjectiveRef")
);

CREATE TABLE "StudyParameter" (
	"OID" TEXT NOT NULL, 
	"Term" TEXT NOT NULL, 
	"ShortName" TEXT, 
	"ParameterValueRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyStructure" (
	"DescriptionRef" TEXT, 
	"ArmRef" TEXT, 
	"EpochRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	PRIMARY KEY ("DescriptionRef", "ArmRef", "EpochRef", "WorkflowRefRef")
);

CREATE TABLE "StudySummary" (
	"StudyParameterRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyParameterRef")
);

CREATE TABLE "StudyTargetPopulation" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	"FormalExpressionRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyTargetPopulationRef" (
	"StudyTargetPopulationOID" TEXT NOT NULL, 
	PRIMARY KEY ("StudyTargetPopulationOID")
);

CREATE TABLE "StudyTiming" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyTimings" (
	"StudyTimingRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyTimingRef")
);

CREATE TABLE "SubClass" (
	"Name" VARCHAR(28) NOT NULL, 
	"ParentClass" TEXT, 
	PRIMARY KEY ("Name", "ParentClass")
);

CREATE TABLE "Suffix" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "SummaryMeasure" (
	"DescriptionRef" TEXT NOT NULL, 
	PRIMARY KEY ("DescriptionRef")
);

CREATE TABLE "SupplementalDoc" (
	"DocumentRefRef" TEXT NOT NULL, 
	PRIMARY KEY ("DocumentRefRef")
);

CREATE TABLE "Transition" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"SourceOID" TEXT NOT NULL, 
	"TargetOID" TEXT NOT NULL, 
	"StartConditionOID" TEXT, 
	"EndConditionOID" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "TranslatedText" (
	_language TEXT, 
	type TEXT NOT NULL, 
	_content TEXT, 
	PRIMARY KEY (_language, type, _content)
);

CREATE TABLE "TrialPhase" (
	"ValueRef" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	PRIMARY KEY ("ValueRef", "DescriptionRef")
);

CREATE TABLE "User" (
	"OID" TEXT NOT NULL, 
	"UserTypeRef" VARCHAR(13), 
	"OrganizationOID" TEXT, 
	"LocationOID" TEXT, 
	"UserNameRef" TEXT, 
	"PrefixRef" TEXT, 
	"SuffixRef" TEXT, 
	"FullNameRef" TEXT, 
	"GivenNameRef" TEXT, 
	"FamilyNameRef" TEXT, 
	"ImageRef" TEXT, 
	"AddressRef" TEXT, 
	"TelecomRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "UserName" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "UserRef" (
	"UserOID" TEXT NOT NULL, 
	PRIMARY KEY ("UserOID")
);

CREATE TABLE "Value" (
	"SeqNum" INTEGER, 
	_content TEXT, 
	PRIMARY KEY ("SeqNum", _content)
);

CREATE TABLE "ValueListRef" (
	"ValueListOID" TEXT NOT NULL, 
	PRIMARY KEY ("ValueListOID")
);

CREATE TABLE "WhereClauseRef" (
	"WhereClauseOID" TEXT NOT NULL, 
	PRIMARY KEY ("WhereClauseOID")
);

CREATE TABLE "WorkflowRef" (
	"WorkflowOID" TEXT NOT NULL, 
	PRIMARY KEY ("WorkflowOID")
);

CREATE TABLE "WorkflowStart" (
	"StartOID" TEXT NOT NULL, 
	PRIMARY KEY ("StartOID")
);

CREATE TABLE "AbsoluteTimingConstraint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"StudyEventGroupOID" TEXT, 
	"StudyEventOID" TEXT, 
	"TimepointTarget" TEXT NOT NULL, 
	"TimepointPreWindow" TEXT, 
	"TimepointPostWindow" TEXT, 
	"DescriptionRef" TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);

CREATE TABLE "Association" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	"KeySetRef" TEXT NOT NULL, 
	"AnnotationRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", "KeySetRef", "AnnotationRef"), 
	FOREIGN KEY("AnnotationRef") REFERENCES "Annotation" ("ID")
);

CREATE TABLE "ClinicalData" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	"SubjectDataRef" TEXT, 
	"ItemGroupDataRef" TEXT, 
	"QueryRef" TEXT, 
	"AuditRecordRef" TEXT, 
	"SignatureRefRef" TEXT, 
	"AnnotationRef" TEXT, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", "SubjectDataRef", "ItemGroupDataRef", "QueryRef", "AuditRecordRef", "SignatureRefRef", "AnnotationRef"), 
	FOREIGN KEY("SignatureRefRef") REFERENCES "Signature" ("ID")
);

CREATE TABLE "DefaultTransition" (
	"TargetTransitionOID" TEXT NOT NULL, 
	"Branching_OID" TEXT, 
	PRIMARY KEY ("TargetTransitionOID", "Branching_OID"), 
	FOREIGN KEY("Branching_OID") REFERENCES "Branching" ("OID")
);

CREATE TABLE "DurationTimingConstraint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"StructuralElementOID" TEXT NOT NULL, 
	"DurationTarget" TEXT NOT NULL, 
	"DurationPreWindow" TEXT, 
	"DurationPostWindow" TEXT, 
	"DescriptionRef" TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);

CREATE TABLE "Flag" (
	"FlagValueRef" TEXT NOT NULL, 
	"FlagTypeRef" TEXT, 
	"Annotation_ID" TEXT, 
	PRIMARY KEY ("FlagValueRef", "FlagTypeRef", "Annotation_ID"), 
	FOREIGN KEY("Annotation_ID") REFERENCES "Annotation" ("ID")
);

CREATE TABLE "IntercurrentEvent" (
	"DescriptionRef" TEXT NOT NULL, 
	"StudyEstimand_OID" TEXT, 
	PRIMARY KEY ("DescriptionRef", "StudyEstimand_OID"), 
	FOREIGN KEY("StudyEstimand_OID") REFERENCES "StudyEstimand" ("OID")
);

CREATE TABLE "ItemData" (
	"ItemOID" TEXT NOT NULL, 
	"TransactionTypeRef" VARCHAR(7), 
	"IsNull" VARCHAR, 
	"ValueRef" TEXT, 
	"QueryRef" TEXT, 
	"AuditRecordRef" TEXT, 
	"SignatureRefRef" TEXT, 
	"AnnotationRef" TEXT, 
	PRIMARY KEY ("ItemOID", "TransactionTypeRef", "IsNull", "ValueRef", "QueryRef", "AuditRecordRef", "SignatureRefRef", "AnnotationRef"), 
	FOREIGN KEY("SignatureRefRef") REFERENCES "Signature" ("ID")
);

CREATE TABLE "ItemGroupData" (
	"ItemGroupOID" TEXT NOT NULL, 
	"ItemGroupRepeatKey" TEXT, 
	"TransactionTypeRef" VARCHAR(7), 
	"ItemGroupDataSeq" INTEGER, 
	"QueryRef" TEXT, 
	"ItemGroupDataRef" TEXT, 
	"ItemDataRef" TEXT, 
	"AuditRecordRef" TEXT, 
	"SignatureRefRef" TEXT, 
	"AnnotationRef" TEXT, 
	PRIMARY KEY ("ItemGroupOID", "ItemGroupRepeatKey", "TransactionTypeRef", "ItemGroupDataSeq", "QueryRef", "ItemGroupDataRef", "ItemDataRef", "AuditRecordRef", "SignatureRefRef", "AnnotationRef"), 
	FOREIGN KEY("SignatureRefRef") REFERENCES "Signature" ("ID")
);

CREATE TABLE "MetaDataVersion" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"IncludeRef" TEXT, 
	"StandardsRef" TEXT, 
	"AnnotatedCRFRef" TEXT, 
	"SupplementalDocRef" TEXT, 
	"ProtocolRef" TEXT, 
	"leafRef" TEXT, 
	"Study_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("Study_OID") REFERENCES "Study" ("OID")
);

CREATE TABLE "MetaDataVersionRef" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	"EffectiveDate" DATE NOT NULL, 
	"Location_OID" TEXT, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", "EffectiveDate", "Location_OID"), 
	FOREIGN KEY("Location_OID") REFERENCES "Location" ("OID")
);

CREATE TABLE "PDFPageRef" (
	"PageRefs" TEXT, 
	"FirstPage" INTEGER, 
	"LastPage" INTEGER, 
	"Type" VARCHAR(16) NOT NULL, 
	"Title" TEXT, 
	"DocumentRef_leafID" TEXT, 
	PRIMARY KEY ("PageRefs", "FirstPage", "LastPage", "Type", "Title", "DocumentRef_leafID"), 
	FOREIGN KEY("DocumentRef_leafID") REFERENCES "DocumentRef" ("leafID")
);

CREATE TABLE "Protocol" (
	"DescriptionRef" TEXT, 
	"StudySummaryRef" TEXT, 
	"StudyStructureRef" TEXT, 
	"TrialPhaseRef" TEXT, 
	"StudyTimingsRef" TEXT, 
	"StudyIndicationsRef" TEXT, 
	"StudyInterventionsRef" TEXT, 
	"StudyObjectivesRef" TEXT, 
	"StudyEndPointsRef" TEXT, 
	"StudyTargetPopulationRefRef" TEXT, 
	"StudyEstimandsRef" TEXT, 
	"InclusionExclusionCriteriaRef" TEXT, 
	"StudyEventGroupRefRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	"AliasRef" TEXT, 
	PRIMARY KEY ("DescriptionRef", "StudySummaryRef", "StudyStructureRef", "TrialPhaseRef", "StudyTimingsRef", "StudyIndicationsRef", "StudyInterventionsRef", "StudyObjectivesRef", "StudyEndPointsRef", "StudyTargetPopulationRefRef", "StudyEstimandsRef", "InclusionExclusionCriteriaRef", "StudyEventGroupRefRef", "WorkflowRefRef", "AliasRef"), 
	FOREIGN KEY("StudyTargetPopulationRefRef") REFERENCES "StudyTargetPopulation" ("OID")
);

CREATE TABLE "ReferenceData" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	"ItemGroupDataRef" TEXT, 
	"AuditRecordRef" TEXT, 
	"SignatureRefRef" TEXT, 
	"AnnotationRef" TEXT, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", "ItemGroupDataRef", "AuditRecordRef", "SignatureRefRef", "AnnotationRef"), 
	FOREIGN KEY("SignatureRefRef") REFERENCES "Signature" ("ID")
);

CREATE TABLE "RelativeTimingConstraint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"PredecessorOID" TEXT, 
	"SuccessorOID" TEXT, 
	"Type" VARCHAR(14), 
	"TimepointRelativeTarget" TEXT NOT NULL, 
	"TimepointPreWindow" TEXT, 
	"TimepointPostWindow" TEXT, 
	"DescriptionRef" TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);

CREATE TABLE "Resource" (
	"Type" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Attribute" TEXT, 
	"Label" TEXT, 
	"SelectionRef" TEXT, 
	"SourceItem_leafID" TEXT, 
	PRIMARY KEY ("Type", "Name", "Attribute", "Label", "SelectionRef", "SourceItem_leafID"), 
	FOREIGN KEY("SourceItem_leafID") REFERENCES "SourceItem" ("leafID")
);

CREATE TABLE "StudyEventData" (
	"StudyEventOID" TEXT NOT NULL, 
	"StudyEventRepeatKey" TEXT, 
	"TransactionTypeRef" VARCHAR(7), 
	"ItemGroupDataRef" TEXT, 
	"QueryRef" TEXT, 
	"AuditRecordRef" TEXT, 
	"SignatureRefRef" TEXT, 
	"AnnotationRef" TEXT, 
	PRIMARY KEY ("StudyEventOID", "StudyEventRepeatKey", "TransactionTypeRef", "ItemGroupDataRef", "QueryRef", "AuditRecordRef", "SignatureRefRef", "AnnotationRef"), 
	FOREIGN KEY("SignatureRefRef") REFERENCES "Signature" ("ID")
);

CREATE TABLE "SubjectData" (
	"SubjectKey" TEXT NOT NULL, 
	"TransactionTypeRef" VARCHAR(7), 
	"InvestigatorRefRef" TEXT, 
	"SiteRefRef" TEXT, 
	"StudyEventDataRef" TEXT, 
	"QueryRef" TEXT, 
	"AuditRecordRef" TEXT, 
	"SignatureRefRef" TEXT, 
	"AnnotationRef" TEXT, 
	PRIMARY KEY ("SubjectKey", "TransactionTypeRef", "InvestigatorRefRef", "SiteRefRef", "StudyEventDataRef", "QueryRef", "AuditRecordRef", "SignatureRefRef", "AnnotationRef"), 
	FOREIGN KEY("SignatureRefRef") REFERENCES "Signature" ("ID")
);

CREATE TABLE "TargetTransition" (
	"TargetTransitionOID" TEXT NOT NULL, 
	"ConditionOID" TEXT, 
	"Branching_OID" TEXT, 
	PRIMARY KEY ("TargetTransitionOID", "ConditionOID", "Branching_OID"), 
	FOREIGN KEY("Branching_OID") REFERENCES "Branching" ("OID")
);

CREATE TABLE "TransitionTimingConstraint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"TransitionOID" TEXT NOT NULL, 
	"MethodOID" TEXT, 
	"Type" VARCHAR(14), 
	"TimepointTarget" TEXT NOT NULL, 
	"TimepointPreWindow" TEXT, 
	"TimepointPostWindow" TEXT, 
	"DescriptionRef" TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);

CREATE TABLE "CodeList" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DataTypeRef" VARCHAR(7) NOT NULL, 
	"CommentOID" TEXT, 
	"StandardOID" TEXT, 
	"IsNonStandard" VARCHAR, 
	"DescriptionRef" TEXT, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "CommentDef" (
	"OID" TEXT NOT NULL, 
	"DescriptionRef" TEXT NOT NULL, 
	"DocumentRefRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "ConditionDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT NOT NULL, 
	"MethodSignatureRef" TEXT NOT NULL, 
	"FormalExpressionRef" TEXT, 
	"AliasRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "ItemDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DataTypeRef" VARCHAR(18) NOT NULL, 
	"Length" INTEGER, 
	"DisplayFormat" TEXT, 
	"VariableSet" TEXT, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"DefinitionRef" TEXT, 
	"QuestionRef" TEXT, 
	"PromptRef" TEXT, 
	"CRFCompletionInstructionsRef" TEXT, 
	"ImplementationNotesRef" TEXT, 
	"CDISCNotesRef" TEXT, 
	"RangeCheckRef" TEXT, 
	"CodeListRefRef" TEXT, 
	"ValueListRefRef" TEXT, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "ItemGroupDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Repeating" VARCHAR(7) NOT NULL, 
	"RepeatingLimit" INTEGER, 
	"IsReferenceData" VARCHAR(3), 
	"Structure" TEXT, 
	"ArchiveLocationID" TEXT, 
	"DatasetName" TEXT, 
	"Domain" TEXT, 
	"Type" TEXT NOT NULL, 
	"Purpose" TEXT, 
	"StandardOID" TEXT, 
	"IsNonStandard" VARCHAR, 
	"HasNoData" VARCHAR, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"ClassRef" TEXT, 
	"CodingRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	"OriginRef" TEXT, 
	"AliasRef" TEXT, 
	"leafRef" TEXT, 
	"ItemGroupRefRef" TEXT, 
	"ItemRefRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("leafRef") REFERENCES leaf ("ID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "MethodDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Type" VARCHAR(11), 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT NOT NULL, 
	"MethodSignatureRef" TEXT NOT NULL, 
	"FormalExpressionRef" TEXT, 
	"AliasRef" TEXT, 
	"DocumentRefRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "StudyEventDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Repeating" VARCHAR(3) NOT NULL, 
	"Type" VARCHAR(11) NOT NULL, 
	"Category" TEXT, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"ItemGroupRefRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "StudyEventGroupDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"ArmOID" TEXT, 
	"EpochOID" TEXT, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	"CodingRef" TEXT, 
	"StudyEventGroupRefRef" TEXT, 
	"StudyEventRefRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "ValueListDef" (
	"OID" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"ItemRefRef" TEXT NOT NULL, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "WhereClauseDef" (
	"OID" TEXT NOT NULL, 
	"CommentOID" TEXT, 
	"RangeCheckRef" TEXT NOT NULL, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "WorkflowDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"WorkflowStartRef" TEXT NOT NULL, 
	"TransitionRef" TEXT, 
	"BranchingRef" TEXT, 
	"MetaDataVersion_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("TransitionRef") REFERENCES "Transition" ("OID"), 
	FOREIGN KEY("BranchingRef") REFERENCES "Branching" ("OID"), 
	FOREIGN KEY("MetaDataVersion_OID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "CodeListItem" (
	"CodedValue" TEXT NOT NULL, 
	"Rank" TEXT, 
	"Other" VARCHAR, 
	"OrderNumber" INTEGER, 
	"ExtendedValue" VARCHAR, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"DecodeRef" TEXT, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	"CodeList_OID" TEXT, 
	PRIMARY KEY ("CodedValue", "Rank", "Other", "OrderNumber", "ExtendedValue", "CommentOID", "DescriptionRef", "DecodeRef", "CodingRef", "AliasRef", "CodeList_OID"), 
	FOREIGN KEY("CodeList_OID") REFERENCES "CodeList" ("OID")
);

CREATE TABLE "WorkflowEnd" (
	"EndOID" TEXT NOT NULL, 
	_content TEXT, 
	"WorkflowDef_OID" TEXT, 
	PRIMARY KEY ("EndOID", _content, "WorkflowDef_OID"), 
	FOREIGN KEY("WorkflowDef_OID") REFERENCES "WorkflowDef" ("OID")
);
