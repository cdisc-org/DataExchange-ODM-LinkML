

CREATE TABLE "AbsoluteTimingConstraint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"StudyEventGroupOID" TEXT, 
	"StudyEventOID" TEXT, 
	"TimepointTarget" TEXT NOT NULL, 
	"TimepointPreWindow" TEXT, 
	"TimepointPostWindow" TEXT, 
	PRIMARY KEY ("OID", "Name", "StudyEventGroupOID", "StudyEventOID", "TimepointTarget", "TimepointPreWindow", "TimepointPostWindow")
);

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
	"UserRef" TEXT, 
	"OrganizationRef" TEXT, 
	"LocationRef" TEXT, 
	"SignatureDefRef" TEXT, 
	PRIMARY KEY ("StudyOID", "UserRef", "OrganizationRef", "LocationRef", "SignatureDefRef")
);

CREATE TABLE "Alias" (
	"Context" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	PRIMARY KEY ("Context", "Name")
);

CREATE TABLE "Annotation" (
	"SeqNum" INTEGER NOT NULL, 
	"TransactionType" VARCHAR(7), 
	"ID" TEXT, 
	"CommentRef" TEXT, 
	"CodingRef" TEXT, 
	"FlagRef" TEXT, 
	PRIMARY KEY ("SeqNum", "TransactionType", "ID", "CommentRef", "CodingRef", "FlagRef")
);

CREATE TABLE "Arm" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "DescriptionRef", "WorkflowRefRef")
);

CREATE TABLE "Association" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	"KeySetRef" TEXT NOT NULL, 
	"AnnotationRef" TEXT NOT NULL, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", "KeySetRef", "AnnotationRef")
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
	"TargetTransitionRef" TEXT NOT NULL, 
	"DefaultTransitionRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "Type", "TargetTransitionRef", "DefaultTransitionRef")
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
	PRIMARY KEY ("Name")
);

CREATE TABLE "ClinicalData" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	"SubjectDataRef" TEXT, 
	"ItemGroupDataRef" TEXT, 
	"QueryRef" TEXT, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", "SubjectDataRef", "ItemGroupDataRef", "QueryRef")
);

CREATE TABLE "Code" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "CodeList" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DataType" VARCHAR(7) NOT NULL, 
	"CommentOID" TEXT, 
	"StandardOID" TEXT, 
	"IsNonStandard" VARCHAR, 
	"DescriptionRef" TEXT, 
	"ExternalCodeListRef" TEXT, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "DataType", "CommentOID", "StandardOID", "IsNonStandard", "DescriptionRef", "ExternalCodeListRef", "CodingRef", "AliasRef")
);

CREATE TABLE "CodeListItem" (
	"CodedValue" TEXT NOT NULL, 
	"Rank" TEXT, 
	"Other" VARCHAR, 
	"OrderNumber" INTEGER, 
	"ExtendedValue" VARCHAR, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"DecodeRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	PRIMARY KEY ("CodedValue", "Rank", "Other", "OrderNumber", "ExtendedValue", "CommentOID", "DescriptionRef", "DecodeRef", "CodingRef", "AliasRef")
);

CREATE TABLE "CodeListRef" (
	"CodeListOID" TEXT NOT NULL, 
	PRIMARY KEY ("CodeListOID")
);

CREATE TABLE "Coding" (
	"Code" TEXT NOT NULL, 
	"System" TEXT NOT NULL, 
	"SystemName" TEXT, 
	"SystemVersion" TEXT, 
	"Label" TEXT, 
	href TEXT, 
	"CommentOID" TEXT, 
	PRIMARY KEY ("Code", "System", "SystemName", "SystemVersion", "Label", href, "CommentOID")
);

CREATE TABLE "Comment" (
	"SponsorOrSite" VARCHAR(7), 
	PRIMARY KEY ("SponsorOrSite")
);

CREATE TABLE "CommentDef" (
	"OID" TEXT NOT NULL, 
	"DescriptionRef" TEXT NOT NULL, 
	"DocumentRefRef" TEXT, 
	PRIMARY KEY ("OID", "DescriptionRef", "DocumentRefRef")
);

CREATE TABLE "ConditionDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT NOT NULL, 
	"MethodSignatureRef" TEXT NOT NULL, 
	"FormalExpressionRef" TEXT, 
	"AliasRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "CommentOID", "DescriptionRef", "MethodSignatureRef", "FormalExpressionRef", "AliasRef")
);

CREATE TABLE "Country" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Criterion" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"ConditionOID" TEXT NOT NULL, 
	PRIMARY KEY ("OID", "Name", "ConditionOID")
);

CREATE TABLE "DateTimeStamp" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "DefaultTransition" (
	"TargetTransitionOID" TEXT NOT NULL, 
	PRIMARY KEY ("TargetTransitionOID")
);

CREATE TABLE "DocumentRef" (
	"leafID" TEXT NOT NULL, 
	PRIMARY KEY ("leafID")
);

CREATE TABLE "DurationTimingConstraint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"StructuralElementOID" TEXT NOT NULL, 
	"DurationTarget" TEXT NOT NULL, 
	"DurationPreWindow" TEXT, 
	"DurationPostWindow" TEXT, 
	PRIMARY KEY ("OID", "Name", "StructuralElementOID", "DurationTarget", "DurationPreWindow", "DurationPostWindow")
);

CREATE TABLE "EnumeratedItem" (
	"CodedValue" TEXT NOT NULL, 
	"Rank" TEXT, 
	"Other" VARCHAR, 
	"OrderNumber" INTEGER, 
	"ExtendedValue" VARCHAR, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	PRIMARY KEY ("CodedValue", "Rank", "Other", "OrderNumber", "ExtendedValue", "CommentOID", "DescriptionRef", "CodingRef", "AliasRef")
);

CREATE TABLE "Epoch" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"SequenceNumber" INTEGER NOT NULL, 
	PRIMARY KEY ("OID", "Name", "SequenceNumber")
);

CREATE TABLE "ExceptionEvent" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"ConditionOID" TEXT, 
	PRIMARY KEY ("OID", "Name", "ConditionOID")
);

CREATE TABLE "ExternalCodeLib" (
	"Library" TEXT NOT NULL, 
	"Method" TEXT, 
	"Version" TEXT, 
	ref TEXT, 
	href TEXT, 
	PRIMARY KEY ("Library", "Method", "Version", ref, href)
);

CREATE TABLE "ExternalCodeList" (
	"Dictionary" TEXT, 
	"Version" TEXT, 
	href TEXT, 
	ref TEXT, 
	PRIMARY KEY ("Dictionary", "Version", href, ref)
);

CREATE TABLE "FamilyName" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "Flag" (
	"FlagValueRef" TEXT NOT NULL, 
	"FlagTypeRef" TEXT, 
	PRIMARY KEY ("FlagValueRef", "FlagTypeRef")
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
	"Context" TEXT, 
	PRIMARY KEY ("Context")
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

CREATE TABLE "Include" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	href TEXT, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", href)
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

CREATE TABLE "ItemData" (
	"ItemOID" TEXT NOT NULL, 
	"TransactionType" VARCHAR(7), 
	"IsNull" VARCHAR, 
	"ValueRef" TEXT, 
	"QueryRef" TEXT, 
	PRIMARY KEY ("ItemOID", "TransactionType", "IsNull", "ValueRef", "QueryRef")
);

CREATE TABLE "ItemDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DataType" VARCHAR(18) NOT NULL, 
	"Length" INTEGER, 
	"DisplayFormat" TEXT, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"QuestionRef" TEXT, 
	"RangeCheckRef" TEXT, 
	"CodeListRefRef" TEXT, 
	"ValueListRefRef" TEXT, 
	"CodingRef" TEXT, 
	"AliasRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "DataType", "Length", "DisplayFormat", "CommentOID", "DescriptionRef", "QuestionRef", "RangeCheckRef", "CodeListRefRef", "ValueListRefRef", "CodingRef", "AliasRef")
);

CREATE TABLE "ItemGroupData" (
	"ItemGroupOID" TEXT NOT NULL, 
	"ItemGroupRepeatKey" TEXT, 
	"TransactionType" VARCHAR(7), 
	"ItemGroupDataSeq" INTEGER, 
	PRIMARY KEY ("ItemGroupOID", "ItemGroupRepeatKey", "TransactionType", "ItemGroupDataSeq")
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
	PRIMARY KEY ("OID", "Name", "Repeating", "RepeatingLimit", "IsReferenceData", "Structure", "ArchiveLocationID", "DatasetName", "Domain", "Type", "Purpose", "StandardOID", "IsNonStandard", "HasNoData", "CommentOID", "DescriptionRef", "ClassRef", "CodingRef", "WorkflowRefRef", "OriginRef", "AliasRef", "leafRef")
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
	"OrderNumber" INTEGER, 
	"Mandatory" VARCHAR(3) NOT NULL, 
	"CollectionExceptionConditionOID" TEXT, 
	"OriginRef" TEXT, 
	"WhereClauseRefRef" TEXT, 
	PRIMARY KEY ("ItemOID", "KeySequence", "IsNonStandard", "HasNoData", "MethodOID", "UnitsItemOID", "Repeat", "Other", "Role", "RoleCodeListOID", "OrderNumber", "Mandatory", "CollectionExceptionConditionOID", "OriginRef", "WhereClauseRefRef")
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
	PRIMARY KEY ("ID", href)
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
	"MetaDataVersionRefRef" TEXT NOT NULL, 
	"AddressRef" TEXT, 
	"TelecomRef" TEXT, 
	"QueryRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "Role", "OrganizationOID", "DescriptionRef", "MetaDataVersionRefRef", "AddressRef", "TelecomRef", "QueryRef")
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

CREATE TABLE "MetaDataVersion" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"CommentOID" TEXT, 
	"DescriptionRef" TEXT, 
	"IncludeRef" TEXT, 
	"StandardsRef" TEXT, 
	"AnnotatedCRFRef" TEXT, 
	"SupplementalDocRef" TEXT, 
	"ValueListDefRef" TEXT, 
	"WhereClauseDefRef" TEXT, 
	"ProtocolRef" TEXT, 
	"WorkflowDefRef" TEXT, 
	"StudyEventGroupDefRef" TEXT, 
	"StudyEventDefRef" TEXT, 
	"ItemGroupDefRef" TEXT, 
	"ItemDefRef" TEXT, 
	"CodeListRef" TEXT, 
	"ConditionDefRef" TEXT, 
	"MethodDefRef" TEXT, 
	"CommentDefRef" TEXT, 
	"leafRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "CommentOID", "DescriptionRef", "IncludeRef", "StandardsRef", "AnnotatedCRFRef", "SupplementalDocRef", "ValueListDefRef", "WhereClauseDefRef", "ProtocolRef", "WorkflowDefRef", "StudyEventGroupDefRef", "StudyEventDefRef", "ItemGroupDefRef", "ItemDefRef", "CodeListRef", "ConditionDefRef", "MethodDefRef", "CommentDefRef", "leafRef")
);

CREATE TABLE "MetaDataVersionRef" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	"EffectiveDate" DATE NOT NULL, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID", "EffectiveDate")
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
	PRIMARY KEY ("OID", "Name", "Type", "CommentOID", "DescriptionRef", "MethodSignatureRef", "FormalExpressionRef", "AliasRef", "DocumentRefRef")
);

CREATE TABLE "MethodSignature" (
	"ParameterRef" TEXT, 
	"ReturnValueRef" TEXT, 
	PRIMARY KEY ("ParameterRef", "ReturnValueRef")
);

CREATE TABLE "ODMFileMetadata" (
	"FileType" VARCHAR(13) NOT NULL, 
	"Granularity" VARCHAR(15), 
	"Context" VARCHAR(10), 
	"FileOID" TEXT NOT NULL, 
	"CreationDateTime" DATETIME NOT NULL, 
	"PriorFileOID" TEXT, 
	"AsOfDateTime" DATETIME, 
	"ODMVersion" TEXT, 
	"Originator" TEXT, 
	"SourceSystem" TEXT, 
	"SourceSystemVersion" TEXT, 
	"DescriptionRef" TEXT, 
	"StudyRef" TEXT, 
	"AdminDataRef" TEXT, 
	"ReferenceDataRef" TEXT, 
	"ClinicalDataRef" TEXT, 
	"AssociationRef" TEXT, 
	PRIMARY KEY ("FileType", "Granularity", "Context", "FileOID", "CreationDateTime", "PriorFileOID", "AsOfDateTime", "ODMVersion", "Originator", "SourceSystem", "SourceSystemVersion", "DescriptionRef", "StudyRef", "AdminDataRef", "ReferenceDataRef", "ClinicalDataRef", "AssociationRef")
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
	PRIMARY KEY ("OID", "Name", "Role", "Type", "LocationOID", "PartOfOrganizationOID", "DescriptionRef", "AddressRef", "TelecomRef")
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
	"DataType" VARCHAR(18) NOT NULL, 
	"Definition" TEXT, 
	"OrderNumber" INTEGER, 
	PRIMARY KEY ("Name", "DataType", "Definition", "OrderNumber")
);

CREATE TABLE "ParameterValue" (
	"Value" TEXT NOT NULL, 
	PRIMARY KEY ("Value")
);

CREATE TABLE "PDFPageRef" (
	"PageRefs" TEXT, 
	"FirstPage" INTEGER, 
	"LastPage" INTEGER, 
	"Type" VARCHAR(16) NOT NULL, 
	"Title" TEXT, 
	PRIMARY KEY ("PageRefs", "FirstPage", "LastPage", "Type", "Title")
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
	"StudyTargetPopulationRef" TEXT, 
	"StudyEstimandsRef" TEXT, 
	"InclusionExclusionCriteriaRef" TEXT, 
	"StudyEventGroupRefRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	"AliasRef" TEXT, 
	PRIMARY KEY ("DescriptionRef", "StudySummaryRef", "StudyStructureRef", "TrialPhaseRef", "StudyTimingsRef", "StudyIndicationsRef", "StudyInterventionsRef", "StudyObjectivesRef", "StudyEndPointsRef", "StudyTargetPopulationRef", "StudyEstimandsRef", "InclusionExclusionCriteriaRef", "StudyEventGroupRefRef", "WorkflowRefRef", "AliasRef")
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
	PRIMARY KEY ("OID", "Source", "Target", "Type", "State", "LastUpdateDatetime", "Name", "ValueRef", "AuditRecordRef")
);

CREATE TABLE "RangeCheck" (
	"Comparator" VARCHAR(5), 
	"SoftHard" VARCHAR(4), 
	"ItemOID" TEXT, 
	PRIMARY KEY ("Comparator", "SoftHard", "ItemOID")
);

CREATE TABLE "ReasonForChange" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "ReferenceData" (
	"StudyOID" TEXT NOT NULL, 
	"MetaDataVersionOID" TEXT NOT NULL, 
	PRIMARY KEY ("StudyOID", "MetaDataVersionOID")
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
	PRIMARY KEY ("OID", "Name", "PredecessorOID", "SuccessorOID", "Type", "TimepointRelativeTarget", "TimepointPreWindow", "TimepointPostWindow")
);

CREATE TABLE "Resource" (
	"Type" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Attribute" TEXT, 
	"Label" TEXT, 
	PRIMARY KEY ("Type", "Name", "Attribute", "Label")
);

CREATE TABLE "ReturnValue" (
	"Name" TEXT NOT NULL, 
	"DataType" VARCHAR(18) NOT NULL, 
	"Definition" TEXT, 
	"OrderNumber" INTEGER, 
	PRIMARY KEY ("Name", "DataType", "Definition", "OrderNumber")
);

CREATE TABLE "Selection" (
	"Path" TEXT NOT NULL, 
	PRIMARY KEY ("Path")
);

CREATE TABLE "Signature" (
	"ID" TEXT, 
	"UserRefRef" TEXT NOT NULL, 
	"LocationRefRef" TEXT NOT NULL, 
	"SignatureRefRef" TEXT NOT NULL, 
	"DateTimeStampRef" TEXT NOT NULL, 
	PRIMARY KEY ("ID", "UserRefRef", "LocationRefRef", "SignatureRefRef", "DateTimeStampRef")
);

CREATE TABLE "SignatureDef" (
	"OID" TEXT NOT NULL, 
	"Methodology" VARCHAR(10), 
	"MeaningRef" TEXT NOT NULL, 
	"LegalReasonRef" TEXT NOT NULL, 
	PRIMARY KEY ("OID", "Methodology", "MeaningRef", "LegalReasonRef")
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
	"leafID" TEXT, 
	"Name" TEXT, 
	"ResourceRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("ItemOID", "ItemGroupOID", "MetaDataVersionOID", "StudyOID", "leafID", "Name", "ResourceRef", "CodingRef")
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
	PRIMARY KEY ("OID", "Name", "Type", "PublishingSet", "Version", "Status", "CommentOID")
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
	"DescriptionRef" TEXT, 
	"MetaDataVersionRef" TEXT NOT NULL, 
	PRIMARY KEY ("OID", "StudyName", "ProtocolName", "DescriptionRef", "MetaDataVersionRef")
);

CREATE TABLE "StudyEndPoint" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Type" VARCHAR(9), 
	"DescriptionRef" TEXT NOT NULL, 
	"FormalExpressionRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "Type", "DescriptionRef", "FormalExpressionRef")
);

CREATE TABLE "StudyEndPointRef" (
	"StudyEndPointOID" TEXT NOT NULL, 
	"OrderNumber" INTEGER, 
	PRIMARY KEY ("StudyEndPointOID", "OrderNumber")
);

CREATE TABLE "StudyEstimand" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"StudyTargetPopulationRefRef" TEXT, 
	"StudyInterventionRefRef" TEXT, 
	"StudyEndPointRefRef" TEXT, 
	"IntercurrentEventRef" TEXT, 
	"SummaryMeasureRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "DescriptionRef", "StudyTargetPopulationRefRef", "StudyInterventionRefRef", "StudyEndPointRefRef", "IntercurrentEventRef", "SummaryMeasureRef")
);

CREATE TABLE "StudyEventData" (
	"StudyEventOID" TEXT NOT NULL, 
	"StudyEventRepeatKey" TEXT, 
	"TransactionType" VARCHAR(7), 
	"ItemGroupDataRef" TEXT, 
	"QueryRef" TEXT, 
	PRIMARY KEY ("StudyEventOID", "StudyEventRepeatKey", "TransactionType", "ItemGroupDataRef", "QueryRef")
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
	PRIMARY KEY ("OID", "Name", "Repeating", "Type", "Category", "CommentOID", "DescriptionRef", "ItemGroupRefRef", "WorkflowRefRef", "CodingRef", "AliasRef")
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
	PRIMARY KEY ("OID", "Name", "ArmOID", "EpochOID", "CommentOID", "DescriptionRef", "WorkflowRefRef", "CodingRef")
);

CREATE TABLE "StudyEventGroupRef" (
	"StudyEventGroupOID" TEXT NOT NULL, 
	"OrderNumber" INTEGER, 
	"Mandatory" VARCHAR(3) NOT NULL, 
	"CollectionExceptionConditionOID" TEXT, 
	PRIMARY KEY ("StudyEventGroupOID", "OrderNumber", "Mandatory", "CollectionExceptionConditionOID")
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
	PRIMARY KEY ("OID", "DescriptionRef", "CodingRef")
);

CREATE TABLE "StudyIntervention" (
	"OID" TEXT NOT NULL, 
	"DescriptionRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("OID", "DescriptionRef", "CodingRef")
);

CREATE TABLE "StudyInterventionRef" (
	"StudyInterventionOID" TEXT NOT NULL, 
	PRIMARY KEY ("StudyInterventionOID")
);

CREATE TABLE "StudyObjective" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"Type" VARCHAR(9), 
	"DescriptionRef" TEXT NOT NULL, 
	"StudyEndPointRefRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "Type", "DescriptionRef", "StudyEndPointRefRef")
);

CREATE TABLE "StudyParameter" (
	"OID" TEXT NOT NULL, 
	"Term" TEXT NOT NULL, 
	"ShortName" TEXT, 
	"ParameterValueRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	PRIMARY KEY ("OID", "Term", "ShortName", "ParameterValueRef", "CodingRef")
);

CREATE TABLE "StudyStructure" (
	"DescriptionRef" TEXT, 
	"ArmRef" TEXT, 
	"EpochRef" TEXT, 
	"WorkflowRefRef" TEXT, 
	PRIMARY KEY ("DescriptionRef", "ArmRef", "EpochRef", "WorkflowRefRef")
);

CREATE TABLE "StudyTargetPopulation" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT NOT NULL, 
	"CodingRef" TEXT, 
	"FormalExpressionRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "DescriptionRef", "CodingRef", "FormalExpressionRef")
);

CREATE TABLE "StudyTargetPopulationRef" (
	"StudyTargetPopulationOID" TEXT NOT NULL, 
	PRIMARY KEY ("StudyTargetPopulationOID")
);

CREATE TABLE "StudyTiming" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"AbsoluteTimingConstraintRef" TEXT, 
	"RelativeTimingConstraintRef" TEXT, 
	"TransitionTimingConstraintRef" TEXT, 
	"DurationTimingConstraintRef" TEXT, 
	PRIMARY KEY ("OID", "Name", "AbsoluteTimingConstraintRef", "RelativeTimingConstraintRef", "TransitionTimingConstraintRef", "DurationTimingConstraintRef")
);

CREATE TABLE "SubClass" (
	"Name" VARCHAR(28) NOT NULL, 
	"ParentClass" TEXT, 
	PRIMARY KEY ("Name", "ParentClass")
);

CREATE TABLE "SubjectData" (
	"SubjectKey" TEXT NOT NULL, 
	"TransactionType" VARCHAR(7), 
	"InvestigatorRefRef" TEXT, 
	"SiteRefRef" TEXT, 
	"StudyEventDataRef" TEXT, 
	"QueryRef" TEXT, 
	PRIMARY KEY ("SubjectKey", "TransactionType", "InvestigatorRefRef", "SiteRefRef", "StudyEventDataRef", "QueryRef")
);

CREATE TABLE "Suffix" (
	_content TEXT, 
	range TEXT, 
	PRIMARY KEY (_content, range)
);

CREATE TABLE "TargetTransition" (
	"TargetTransitionOID" TEXT NOT NULL, 
	"ConditionOID" TEXT, 
	PRIMARY KEY ("TargetTransitionOID", "ConditionOID")
);

CREATE TABLE "Transition" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"SourceOID" TEXT NOT NULL, 
	"TargetOID" TEXT NOT NULL, 
	"StartConditionOID" TEXT, 
	"EndConditionOID" TEXT, 
	PRIMARY KEY ("OID", "Name", "SourceOID", "TargetOID", "StartConditionOID", "EndConditionOID")
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
	PRIMARY KEY ("OID", "Name", "TransitionOID", "MethodOID", "Type", "TimepointTarget", "TimepointPreWindow", "TimepointPostWindow")
);

CREATE TABLE "TranslatedText" (
	_language TEXT, 
	type TEXT NOT NULL, 
	PRIMARY KEY (_language, type)
);

CREATE TABLE "TrialPhase" (
	"Value" TEXT NOT NULL, 
	PRIMARY KEY ("Value")
);

CREATE TABLE "User" (
	"OID" TEXT NOT NULL, 
	"UserType" VARCHAR(13), 
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
	PRIMARY KEY ("OID", "UserType", "OrganizationOID", "LocationOID", "UserNameRef", "PrefixRef", "SuffixRef", "FullNameRef", "GivenNameRef", "FamilyNameRef", "ImageRef", "AddressRef", "TelecomRef")
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

CREATE TABLE "ValueListDef" (
	"OID" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"ItemRefRef" TEXT NOT NULL, 
	PRIMARY KEY ("OID", "DescriptionRef", "ItemRefRef")
);

CREATE TABLE "ValueListRef" (
	"ValueListOID" TEXT NOT NULL, 
	PRIMARY KEY ("ValueListOID")
);

CREATE TABLE "WhereClauseDef" (
	"OID" TEXT NOT NULL, 
	"CommentOID" TEXT, 
	PRIMARY KEY ("OID", "CommentOID")
);

CREATE TABLE "WhereClauseRef" (
	"WhereClauseOID" TEXT NOT NULL, 
	PRIMARY KEY ("WhereClauseOID")
);

CREATE TABLE "WorkflowDef" (
	"OID" TEXT NOT NULL, 
	"Name" TEXT NOT NULL, 
	"DescriptionRef" TEXT, 
	"WorkflowStartRef" TEXT NOT NULL, 
	"WorkflowEndRef" TEXT NOT NULL, 
	PRIMARY KEY ("OID", "Name", "DescriptionRef", "WorkflowStartRef", "WorkflowEndRef")
);

CREATE TABLE "WorkflowEnd" (
	"EndOID" TEXT NOT NULL, 
	_content TEXT, 
	PRIMARY KEY ("EndOID", _content)
);

CREATE TABLE "WorkflowRef" (
	"WorkflowOID" TEXT NOT NULL, 
	PRIMARY KEY ("WorkflowOID")
);

CREATE TABLE "WorkflowStart" (
	"StartOID" TEXT NOT NULL, 
	PRIMARY KEY ("StartOID")
);
