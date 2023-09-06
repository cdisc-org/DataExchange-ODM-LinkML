

CREATE TABLE "Address" (
	"streetName" TEXT, 
	"houseNumber" TEXT, 
	city TEXT, 
	"stateProv" TEXT, 
	country TEXT, 
	"postalCode" TEXT, 
	"geoPosition" TEXT, 
	"otherText" TEXT, 
	PRIMARY KEY ("streetName", "houseNumber", city, "stateProv", country, "postalCode", "geoPosition", "otherText")
);

CREATE TABLE "AdminData" (
	"studyOID" TEXT, 
	user TEXT, 
	organization TEXT, 
	location TEXT, 
	"signatureDef" TEXT, 
	PRIMARY KEY ("studyOID", user, organization, location, "signatureDef")
);

CREATE TABLE "Alias" (
	context TEXT NOT NULL, 
	name TEXT NOT NULL, 
	PRIMARY KEY (context, name)
);

CREATE TABLE "AnnotatedCRF" (
	"documentRef" TEXT, 
	PRIMARY KEY ("documentRef")
);

CREATE TABLE "Annotation" (
	"seqNum" INTEGER NOT NULL, 
	"transactionType" VARCHAR(7), 
	"iD" TEXT NOT NULL, 
	comment TEXT, 
	coding TEXT, 
	PRIMARY KEY ("iD")
);

CREATE TABLE "Arm" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"workflowRef" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "AuditRecord" (
	"editPoint" VARCHAR(14), 
	"usedMethod" VARCHAR(3), 
	"userRef" TEXT, 
	"locationRef" TEXT, 
	"dateTimeStamp" TEXT, 
	"reasonForChange" TEXT, 
	"sourceID" TEXT, 
	PRIMARY KEY ("editPoint", "usedMethod", "userRef", "locationRef", "dateTimeStamp", "reasonForChange", "sourceID")
);

CREATE TABLE "CDISCNotes" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "CheckValue" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "City" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Class" (
	name VARCHAR(40) NOT NULL, 
	"subClass" TEXT, 
	PRIMARY KEY (name, "subClass")
);

CREATE TABLE "Code" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "CodeListRef" (
	"codeListOID" TEXT NOT NULL, 
	PRIMARY KEY ("codeListOID")
);

CREATE TABLE "Coding" (
	code TEXT, 
	system TEXT NOT NULL, 
	"systemName" TEXT, 
	"systemVersion" TEXT, 
	label TEXT, 
	href TEXT, 
	ref TEXT, 
	"commentOID" TEXT, 
	PRIMARY KEY (code, system, "systemName", "systemVersion", label, href, ref, "commentOID")
);

CREATE TABLE "Comment" (
	"sponsorOrSite" VARCHAR(7), 
	"translatedText" TEXT, 
	PRIMARY KEY ("sponsorOrSite", "translatedText")
);

CREATE TABLE "Country" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "CRFCompletionInstructions" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "Criterion" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"conditionOID" TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "DateTimeStamp" (
	content DATETIME, 
	PRIMARY KEY (content)
);

CREATE TABLE "Decode" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "Definition" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "Description" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "DocumentRef" (
	"leafID" TEXT NOT NULL, 
	"pDFPageRef" TEXT, 
	PRIMARY KEY ("leafID", "pDFPageRef")
);

CREATE TABLE "Epoch" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"sequenceNumber" INTEGER NOT NULL, 
	description TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "ErrorMessage" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "ExclusionCriteria" (
	criterion TEXT, 
	PRIMARY KEY (criterion)
);

CREATE TABLE "ExternalCodeLib" (
	library TEXT NOT NULL, 
	method TEXT, 
	version TEXT, 
	ref TEXT, 
	href TEXT, 
	PRIMARY KEY (library, method, version, ref, href)
);

CREATE TABLE "FamilyName" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "FlagType" (
	"codeListOID" TEXT NOT NULL, 
	content TEXT, 
	PRIMARY KEY ("codeListOID", content)
);

CREATE TABLE "FlagValue" (
	"codeListOID" TEXT NOT NULL, 
	content TEXT, 
	PRIMARY KEY ("codeListOID", content)
);

CREATE TABLE "FormalExpression" (
	context TEXT, 
	code TEXT, 
	"externalCodeLib" TEXT, 
	PRIMARY KEY (context, code, "externalCodeLib")
);

CREATE TABLE "FullName" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "GeoPosition" (
	longitude TEXT, 
	latitude TEXT, 
	altitude TEXT, 
	PRIMARY KEY (longitude, latitude, altitude)
);

CREATE TABLE "GivenName" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "HouseNumber" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Image" (
	"imageFileName" TEXT, 
	href TEXT, 
	"mimeType" TEXT, 
	PRIMARY KEY ("imageFileName", href, "mimeType")
);

CREATE TABLE "ImplementationNotes" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "Include" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	href TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", href)
);

CREATE TABLE "InclusionCriteria" (
	criterion TEXT, 
	PRIMARY KEY (criterion)
);

CREATE TABLE "InclusionExclusionCriteria" (
	"inclusionCriteria" TEXT, 
	"exclusionCriteria" TEXT, 
	PRIMARY KEY ("inclusionCriteria", "exclusionCriteria")
);

CREATE TABLE "InvestigatorRef" (
	"userOID" TEXT NOT NULL, 
	PRIMARY KEY ("userOID")
);

CREATE TABLE "ItemGroupRef" (
	"itemGroupOID" TEXT NOT NULL, 
	"methodOID" TEXT, 
	"orderNumber" INTEGER, 
	mandatory VARCHAR(3) NOT NULL, 
	"collectionExceptionConditionOID" TEXT, 
	PRIMARY KEY ("itemGroupOID", "methodOID", "orderNumber", mandatory, "collectionExceptionConditionOID")
);

CREATE TABLE "ItemRef" (
	"itemOID" TEXT NOT NULL, 
	"keySequence" INTEGER, 
	"isNonStandard" VARCHAR, 
	"hasNoData" VARCHAR, 
	"methodOID" TEXT, 
	"unitsItemOID" TEXT, 
	repeat VARCHAR, 
	other VARCHAR, 
	role TEXT, 
	"roleCodeListOID" TEXT, 
	core TEXT, 
	"preSpecifiedValue" TEXT, 
	"orderNumber" INTEGER, 
	mandatory VARCHAR(3) NOT NULL, 
	"collectionExceptionConditionOID" TEXT, 
	origin TEXT, 
	"whereClauseRef" TEXT, 
	PRIMARY KEY ("itemOID", "keySequence", "isNonStandard", "hasNoData", "methodOID", "unitsItemOID", repeat, other, role, "roleCodeListOID", core, "preSpecifiedValue", "orderNumber", mandatory, "collectionExceptionConditionOID", origin, "whereClauseRef")
);

CREATE TABLE "KeySet" (
	"studyOID" TEXT NOT NULL, 
	"subjectKey" TEXT, 
	"metaDataVersionOID" TEXT, 
	"studyEventOID" TEXT, 
	"studyEventRepeatKey" TEXT, 
	"itemGroupOID" TEXT, 
	"itemGroupRepeatKey" TEXT, 
	"itemOID" TEXT, 
	PRIMARY KEY ("studyOID", "subjectKey", "metaDataVersionOID", "studyEventOID", "studyEventRepeatKey", "itemGroupOID", "itemGroupRepeatKey", "itemOID")
);

CREATE TABLE "Leaf" (
	"iD" TEXT NOT NULL, 
	href TEXT NOT NULL, 
	title TEXT, 
	PRIMARY KEY ("iD")
);

CREATE TABLE "LegalReason" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Location" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	role TEXT, 
	"organizationOID" TEXT, 
	description TEXT, 
	address TEXT, 
	telecom TEXT, 
	"query" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "LocationRef" (
	"locationOID" TEXT NOT NULL, 
	PRIMARY KEY ("locationOID")
);

CREATE TABLE "Meaning" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "MethodSignature" (
	parameter TEXT, 
	"returnValue" TEXT, 
	PRIMARY KEY (parameter, "returnValue")
);

CREATE TABLE "ODMFileMetadata" (
	"fileType" VARCHAR(13) NOT NULL, 
	granularity VARCHAR(15), 
	context VARCHAR(10), 
	"fileOID" TEXT NOT NULL, 
	"creationDateTime" DATETIME NOT NULL, 
	"priorFileOID" TEXT, 
	"asOfDateTime" DATETIME, 
	"oDMVersion" TEXT, 
	originator TEXT, 
	"sourceSystem" TEXT, 
	"sourceSystemVersion" TEXT, 
	description TEXT, 
	study TEXT, 
	"adminData" TEXT, 
	"referenceData" TEXT, 
	"clinicalData" TEXT, 
	association TEXT, 
	PRIMARY KEY ("fileType", granularity, context, "fileOID", "creationDateTime", "priorFileOID", "asOfDateTime", "oDMVersion", originator, "sourceSystem", "sourceSystemVersion", description, study, "adminData", "referenceData", "clinicalData", association)
);

CREATE TABLE "Organization" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	role TEXT, 
	type VARCHAR(18) NOT NULL, 
	"locationOID" TEXT, 
	"partOfOrganizationOID" TEXT, 
	description TEXT, 
	address TEXT, 
	telecom TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "Origin" (
	type VARCHAR(13) NOT NULL, 
	source VARCHAR(12), 
	description TEXT, 
	"sourceItems" TEXT, 
	coding TEXT, 
	"documentRef" TEXT, 
	PRIMARY KEY (type, source, description, "sourceItems", coding, "documentRef")
);

CREATE TABLE "OtherText" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Parameter" (
	name TEXT NOT NULL, 
	"dataType" VARCHAR(18) NOT NULL, 
	definition TEXT, 
	"orderNumber" INTEGER, 
	PRIMARY KEY (name, "dataType", definition, "orderNumber")
);

CREATE TABLE "ParameterValue" (
	value TEXT NOT NULL, 
	coding TEXT, 
	PRIMARY KEY (value, coding)
);

CREATE TABLE "PDFPageRef" (
	"pageRefs" TEXT, 
	"firstPage" INTEGER, 
	"lastPage" INTEGER, 
	type VARCHAR(16) NOT NULL, 
	title TEXT, 
	PRIMARY KEY ("pageRefs", "firstPage", "lastPage", type, title)
);

CREATE TABLE "PostalCode" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Prefix" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Prompt" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "Query" (
	"oID" TEXT NOT NULL, 
	source VARCHAR(15) NOT NULL, 
	target TEXT, 
	type VARCHAR(6), 
	state VARCHAR(9) NOT NULL, 
	"lastUpdateDatetime" DATETIME NOT NULL, 
	name TEXT, 
	value TEXT, 
	"auditRecord" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "Question" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
);

CREATE TABLE "RangeCheck" (
	comparator VARCHAR(5), 
	"softHard" VARCHAR(4), 
	"itemOID" TEXT, 
	"errorMessage" TEXT, 
	"methodSignature" TEXT, 
	"formalExpression" TEXT, 
	"checkValue" TEXT, 
	PRIMARY KEY (comparator, "softHard", "itemOID", "errorMessage", "methodSignature", "formalExpression", "checkValue")
);

CREATE TABLE "ReasonForChange" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Resource" (
	type TEXT NOT NULL, 
	name TEXT NOT NULL, 
	attribute TEXT, 
	label TEXT, 
	selection TEXT, 
	PRIMARY KEY (type, name, attribute, label, selection)
);

CREATE TABLE "ReturnValue" (
	name TEXT NOT NULL, 
	"dataType" VARCHAR(18) NOT NULL, 
	definition TEXT, 
	"orderNumber" INTEGER, 
	PRIMARY KEY (name, "dataType", definition, "orderNumber")
);

CREATE TABLE "Selection" (
	path TEXT NOT NULL, 
	PRIMARY KEY (path)
);

CREATE TABLE "Signature" (
	"iD" TEXT NOT NULL, 
	"userRef" TEXT, 
	"locationRef" TEXT, 
	"signatureRef" TEXT, 
	"dateTimeStamp" TEXT, 
	PRIMARY KEY ("iD")
);

CREATE TABLE "SignatureDef" (
	"oID" TEXT NOT NULL, 
	methodology VARCHAR(10), 
	meaning TEXT, 
	"legalReason" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "SignatureRef" (
	"signatureOID" TEXT NOT NULL, 
	PRIMARY KEY ("signatureOID")
);

CREATE TABLE "SiteRef" (
	"locationOID" TEXT NOT NULL, 
	PRIMARY KEY ("locationOID")
);

CREATE TABLE "SourceID" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "SourceItem" (
	"itemOID" TEXT, 
	"itemGroupOID" TEXT, 
	"metaDataVersionOID" TEXT, 
	"studyOID" TEXT, 
	"leafID" TEXT, 
	name TEXT, 
	resource TEXT, 
	coding TEXT, 
	PRIMARY KEY ("itemOID", "itemGroupOID", "metaDataVersionOID", "studyOID", "leafID", name, resource, coding)
);

CREATE TABLE "SourceItems" (
	"sourceItem" TEXT, 
	coding TEXT, 
	PRIMARY KEY ("sourceItem", coding)
);

CREATE TABLE "Standard" (
	"oID" TEXT NOT NULL, 
	name VARCHAR(11) NOT NULL, 
	type VARCHAR(2) NOT NULL, 
	"publishingSet" VARCHAR(10), 
	version TEXT NOT NULL, 
	status TEXT NOT NULL, 
	"commentOID" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "Standards" (
	standard TEXT, 
	PRIMARY KEY (standard)
);

CREATE TABLE "StateProv" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "StreetName" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Study" (
	"oID" TEXT NOT NULL, 
	"studyName" TEXT NOT NULL, 
	"protocolName" TEXT NOT NULL, 
	"versionID" TEXT, 
	"versionName" TEXT, 
	status TEXT, 
	description TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyEndPoint" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type VARCHAR(9), 
	level VARCHAR(11), 
	description TEXT, 
	"formalExpression" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyEndPointRef" (
	"studyEndPointOID" TEXT NOT NULL, 
	"orderNumber" INTEGER, 
	PRIMARY KEY ("studyEndPointOID", "orderNumber")
);

CREATE TABLE "StudyEndPoints" (
	"studyEndPoint" TEXT, 
	PRIMARY KEY ("studyEndPoint")
);

CREATE TABLE "StudyEstimand" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	level VARCHAR(11), 
	description TEXT, 
	"studyTargetPopulationRef" TEXT, 
	"studyInterventionRef" TEXT, 
	"studyEndPointRef" TEXT, 
	"summaryMeasure" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyEstimands" (
	"studyEstimand" TEXT, 
	PRIMARY KEY ("studyEstimand")
);

CREATE TABLE "StudyEventGroupRef" (
	"studyEventGroupOID" TEXT NOT NULL, 
	"orderNumber" INTEGER, 
	mandatory VARCHAR(3) NOT NULL, 
	"collectionExceptionConditionOID" TEXT, 
	description TEXT, 
	PRIMARY KEY ("studyEventGroupOID", "orderNumber", mandatory, "collectionExceptionConditionOID", description)
);

CREATE TABLE "StudyIndication" (
	"oID" TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyIndications" (
	"studyIndication" TEXT, 
	PRIMARY KEY ("studyIndication")
);

CREATE TABLE "StudyIntervention" (
	"oID" TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyInterventionRef" (
	"studyInterventionOID" TEXT NOT NULL, 
	PRIMARY KEY ("studyInterventionOID")
);

CREATE TABLE "StudyInterventions" (
	"studyIntervention" TEXT, 
	PRIMARY KEY ("studyIntervention")
);

CREATE TABLE "StudyObjective" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	level VARCHAR(11), 
	description TEXT, 
	"studyEndPointRef" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyObjectives" (
	"studyObjective" TEXT, 
	PRIMARY KEY ("studyObjective")
);

CREATE TABLE "StudyParameter" (
	"oID" TEXT NOT NULL, 
	term TEXT NOT NULL, 
	"shortName" TEXT, 
	"parameterValue" TEXT, 
	coding TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyStructure" (
	description TEXT, 
	arm TEXT, 
	epoch TEXT, 
	"workflowRef" TEXT, 
	PRIMARY KEY (description, arm, epoch, "workflowRef")
);

CREATE TABLE "StudySummary" (
	"studyParameter" TEXT, 
	PRIMARY KEY ("studyParameter")
);

CREATE TABLE "StudyTargetPopulation" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	"formalExpression" TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyTargetPopulationRef" (
	"studyTargetPopulationOID" TEXT NOT NULL, 
	PRIMARY KEY ("studyTargetPopulationOID")
);

CREATE TABLE "StudyTiming" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "StudyTimings" (
	"studyTiming" TEXT, 
	PRIMARY KEY ("studyTiming")
);

CREATE TABLE "SubClass" (
	name VARCHAR(28) NOT NULL, 
	"parentClass" TEXT, 
	PRIMARY KEY (name, "parentClass")
);

CREATE TABLE "Suffix" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "SummaryMeasure" (
	description TEXT, 
	PRIMARY KEY (description)
);

CREATE TABLE "SupplementalDoc" (
	"documentRef" TEXT, 
	PRIMARY KEY ("documentRef")
);

CREATE TABLE "Telecom" (
	"telecomType" VARCHAR(5) NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("telecomType", value)
);

CREATE TABLE "Title" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "TranslatedText" (
	language TEXT, 
	type TEXT NOT NULL, 
	content TEXT, 
	PRIMARY KEY (language, type, content)
);

CREATE TABLE "TrialPhase" (
	value TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (value, description)
);

CREATE TABLE "User" (
	"oID" TEXT NOT NULL, 
	"userType" VARCHAR(13), 
	"organizationOID" TEXT, 
	"locationOID" TEXT, 
	"userName" TEXT, 
	prefix TEXT, 
	suffix TEXT, 
	"fullName" TEXT, 
	"givenName" TEXT, 
	"familyName" TEXT, 
	image TEXT, 
	address TEXT, 
	telecom TEXT, 
	PRIMARY KEY ("oID")
);

CREATE TABLE "UserName" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "UserRef" (
	"userOID" TEXT NOT NULL, 
	PRIMARY KEY ("userOID")
);

CREATE TABLE "Value" (
	"seqNum" INTEGER, 
	content TEXT, 
	PRIMARY KEY ("seqNum", content)
);

CREATE TABLE "ValueListRef" (
	"valueListOID" TEXT NOT NULL, 
	PRIMARY KEY ("valueListOID")
);

CREATE TABLE "WhereClauseRef" (
	"whereClauseOID" TEXT NOT NULL, 
	PRIMARY KEY ("whereClauseOID")
);

CREATE TABLE "WorkflowRef" (
	"workflowOID" TEXT NOT NULL, 
	PRIMARY KEY ("workflowOID")
);

CREATE TABLE "WorkflowStart" (
	"startOID" TEXT NOT NULL, 
	PRIMARY KEY ("startOID")
);

CREATE TABLE "AbsoluteTimingConstraint" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"studyEventGroupOID" TEXT, 
	"studyEventOID" TEXT, 
	"timepointTarget" TEXT NOT NULL, 
	"timepointPreWindow" TEXT, 
	"timepointPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("StudyTiming_oID") REFERENCES "StudyTiming" ("oID")
);

CREATE TABLE "Association" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	"keySet" TEXT, 
	annotation TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "keySet", annotation), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("iD")
);

CREATE TABLE "ClinicalData" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	"subjectData" TEXT, 
	"itemGroupData" TEXT, 
	"query" TEXT, 
	"auditRecord" TEXT, 
	signature TEXT, 
	annotation TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "subjectData", "itemGroupData", "query", "auditRecord", signature, annotation), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("iD"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("iD")
);

CREATE TABLE "DurationTimingConstraint" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"structuralElementOID" TEXT NOT NULL, 
	"durationTarget" TEXT NOT NULL, 
	"durationPreWindow" TEXT, 
	"durationPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("StudyTiming_oID") REFERENCES "StudyTiming" ("oID")
);

CREATE TABLE "Flag" (
	"flagValue" TEXT, 
	"flagType" TEXT, 
	"Annotation_iD" TEXT, 
	PRIMARY KEY ("flagValue", "flagType", "Annotation_iD"), 
	FOREIGN KEY("Annotation_iD") REFERENCES "Annotation" ("iD")
);

CREATE TABLE "IntercurrentEvent" (
	description TEXT, 
	"StudyEstimand_oID" TEXT, 
	PRIMARY KEY (description, "StudyEstimand_oID"), 
	FOREIGN KEY("StudyEstimand_oID") REFERENCES "StudyEstimand" ("oID")
);

CREATE TABLE "ItemData" (
	"itemOID" TEXT NOT NULL, 
	"transactionType" VARCHAR(7), 
	"isNull" VARCHAR, 
	value TEXT, 
	"query" TEXT, 
	"auditRecord" TEXT, 
	signature TEXT, 
	annotation TEXT, 
	PRIMARY KEY ("itemOID", "transactionType", "isNull", value, "query", "auditRecord", signature, annotation), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("iD"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("iD")
);

CREATE TABLE "ItemGroupData" (
	"itemGroupOID" TEXT NOT NULL, 
	"itemGroupRepeatKey" TEXT, 
	"transactionType" VARCHAR(7), 
	"itemGroupDataSeq" INTEGER, 
	"query" TEXT, 
	"itemGroupData" TEXT, 
	"itemData" TEXT, 
	"auditRecord" TEXT, 
	signature TEXT, 
	annotation TEXT, 
	PRIMARY KEY ("itemGroupOID", "itemGroupRepeatKey", "transactionType", "itemGroupDataSeq", "query", "itemGroupData", "itemData", "auditRecord", signature, annotation), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("iD"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("iD")
);

CREATE TABLE "MetaDataVersion" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"commentOID" TEXT, 
	description TEXT, 
	include TEXT, 
	standards TEXT, 
	"annotatedCRF" TEXT, 
	"supplementalDoc" TEXT, 
	protocol TEXT, 
	leaf TEXT, 
	"Study_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("Study_oID") REFERENCES "Study" ("oID")
);

CREATE TABLE "MetaDataVersionRef" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	"effectiveDate" DATE NOT NULL, 
	"Location_oID" TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "effectiveDate", "Location_oID"), 
	FOREIGN KEY("Location_oID") REFERENCES "Location" ("oID")
);

CREATE TABLE "Protocol" (
	description TEXT, 
	"studySummary" TEXT, 
	"studyStructure" TEXT, 
	"trialPhase" TEXT, 
	"studyTimings" TEXT, 
	"studyIndications" TEXT, 
	"studyInterventions" TEXT, 
	"studyObjectives" TEXT, 
	"studyEndPoints" TEXT, 
	"studyTargetPopulation" TEXT, 
	"studyEstimands" TEXT, 
	"inclusionExclusionCriteria" TEXT, 
	"studyEventGroupRef" TEXT, 
	"workflowRef" TEXT, 
	alias TEXT, 
	PRIMARY KEY (description, "studySummary", "studyStructure", "trialPhase", "studyTimings", "studyIndications", "studyInterventions", "studyObjectives", "studyEndPoints", "studyTargetPopulation", "studyEstimands", "inclusionExclusionCriteria", "studyEventGroupRef", "workflowRef", alias), 
	FOREIGN KEY("studyTargetPopulation") REFERENCES "StudyTargetPopulation" ("oID")
);

CREATE TABLE "ReferenceData" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	"itemGroupData" TEXT, 
	"auditRecord" TEXT, 
	signature TEXT, 
	annotation TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "itemGroupData", "auditRecord", signature, annotation), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("iD"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("iD")
);

CREATE TABLE "RelativeTimingConstraint" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"predecessorOID" TEXT, 
	"successorOID" TEXT, 
	type VARCHAR(14), 
	"timepointRelativeTarget" TEXT NOT NULL, 
	"timepointPreWindow" TEXT, 
	"timepointPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("StudyTiming_oID") REFERENCES "StudyTiming" ("oID")
);

CREATE TABLE "StudyEventData" (
	"studyEventOID" TEXT NOT NULL, 
	"studyEventRepeatKey" TEXT, 
	"transactionType" VARCHAR(7), 
	"itemGroupData" TEXT, 
	"query" TEXT, 
	"auditRecord" TEXT, 
	signature TEXT, 
	annotation TEXT, 
	PRIMARY KEY ("studyEventOID", "studyEventRepeatKey", "transactionType", "itemGroupData", "query", "auditRecord", signature, annotation), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("iD"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("iD")
);

CREATE TABLE "SubjectData" (
	"subjectKey" TEXT NOT NULL, 
	"transactionType" VARCHAR(7), 
	"investigatorRef" TEXT, 
	"siteRef" TEXT, 
	"studyEventData" TEXT, 
	"query" TEXT, 
	"auditRecord" TEXT, 
	signature TEXT, 
	annotation TEXT, 
	PRIMARY KEY ("subjectKey", "transactionType", "investigatorRef", "siteRef", "studyEventData", "query", "auditRecord", signature, annotation), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("iD"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("iD")
);

CREATE TABLE "TransitionTimingConstraint" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"transitionOID" TEXT NOT NULL, 
	"methodOID" TEXT, 
	type VARCHAR(14), 
	"timepointTarget" TEXT NOT NULL, 
	"timepointPreWindow" TEXT, 
	"timepointPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("StudyTiming_oID") REFERENCES "StudyTiming" ("oID")
);

CREATE TABLE "CodeList" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"dataType" VARCHAR(7) NOT NULL, 
	"commentOID" TEXT, 
	"standardOID" TEXT, 
	"isNonStandard" VARCHAR, 
	description TEXT, 
	coding TEXT, 
	alias TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "CommentDef" (
	"oID" TEXT NOT NULL, 
	description TEXT, 
	"documentRef" TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "ConditionDef" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"commentOID" TEXT, 
	description TEXT, 
	"methodSignature" TEXT, 
	"formalExpression" TEXT, 
	alias TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "ItemDef" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"dataType" VARCHAR(18) NOT NULL, 
	length INTEGER, 
	"displayFormat" TEXT, 
	"variableSet" TEXT, 
	"commentOID" TEXT, 
	description TEXT, 
	definition TEXT, 
	question TEXT, 
	prompt TEXT, 
	"cRFCompletionInstructions" TEXT, 
	"implementationNotes" TEXT, 
	"cDISCNotes" TEXT, 
	"rangeCheck" TEXT, 
	"codeListRef" TEXT, 
	"valueListRef" TEXT, 
	coding TEXT, 
	alias TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "ItemGroupDef" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	repeating VARCHAR(7) NOT NULL, 
	"repeatingLimit" INTEGER, 
	"isReferenceData" VARCHAR(3), 
	structure TEXT, 
	"archiveLocationID" TEXT, 
	"datasetName" TEXT, 
	domain TEXT, 
	type TEXT NOT NULL, 
	purpose TEXT, 
	"standardOID" TEXT, 
	"isNonStandard" VARCHAR, 
	"hasNoData" VARCHAR, 
	"commentOID" TEXT, 
	description TEXT, 
	"classRef" TEXT, 
	coding TEXT, 
	"workflowRef" TEXT, 
	origin TEXT, 
	alias TEXT, 
	leaf TEXT, 
	"itemGroupRef" TEXT, 
	"itemRef" TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY(leaf) REFERENCES "Leaf" ("iD"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "MethodDef" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type VARCHAR(11), 
	"commentOID" TEXT, 
	description TEXT, 
	"methodSignature" TEXT, 
	"formalExpression" TEXT, 
	alias TEXT, 
	"documentRef" TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "StudyEventDef" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	repeating VARCHAR(3) NOT NULL, 
	type VARCHAR(11) NOT NULL, 
	category TEXT, 
	"commentOID" TEXT, 
	description TEXT, 
	"itemGroupRef" TEXT, 
	"workflowRef" TEXT, 
	coding TEXT, 
	alias TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "StudyEventGroupDef" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"armOID" TEXT, 
	"epochOID" TEXT, 
	"commentOID" TEXT, 
	description TEXT, 
	"workflowRef" TEXT, 
	coding TEXT, 
	"studyEventGroupRef" TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "ValueListDef" (
	"oID" TEXT NOT NULL, 
	description TEXT, 
	"itemRef" TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "WhereClauseDef" (
	"oID" TEXT NOT NULL, 
	"commentOID" TEXT, 
	"rangeCheck" TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "WorkflowDef" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"workflowStart" TEXT, 
	"MetaDataVersion_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("MetaDataVersion_oID") REFERENCES "MetaDataVersion" ("oID")
);

CREATE TABLE "Branching" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type VARCHAR(9) NOT NULL, 
	"WorkflowDef_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("WorkflowDef_oID") REFERENCES "WorkflowDef" ("oID")
);

CREATE TABLE "CodeListItem" (
	"codedValue" TEXT NOT NULL, 
	rank TEXT, 
	other VARCHAR, 
	"orderNumber" INTEGER, 
	"extendedValue" VARCHAR, 
	"commentOID" TEXT, 
	description TEXT, 
	decode TEXT, 
	coding TEXT, 
	alias TEXT, 
	"CodeList_oID" TEXT, 
	PRIMARY KEY ("codedValue", rank, other, "orderNumber", "extendedValue", "commentOID", description, decode, coding, alias, "CodeList_oID"), 
	FOREIGN KEY("CodeList_oID") REFERENCES "CodeList" ("oID")
);

CREATE TABLE "StudyEventRef" (
	"studyEventOID" TEXT NOT NULL, 
	"orderNumber" INTEGER, 
	mandatory VARCHAR(3) NOT NULL, 
	"collectionExceptionConditionOID" TEXT, 
	"StudyEventGroupDef_oID" TEXT, 
	PRIMARY KEY ("studyEventOID", "orderNumber", mandatory, "collectionExceptionConditionOID", "StudyEventGroupDef_oID"), 
	FOREIGN KEY("StudyEventGroupDef_oID") REFERENCES "StudyEventGroupDef" ("oID")
);

CREATE TABLE "Transition" (
	"oID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"sourceOID" TEXT NOT NULL, 
	"targetOID" TEXT NOT NULL, 
	"startConditionOID" TEXT, 
	"endConditionOID" TEXT, 
	"WorkflowDef_oID" TEXT, 
	PRIMARY KEY ("oID"), 
	FOREIGN KEY("WorkflowDef_oID") REFERENCES "WorkflowDef" ("oID")
);

CREATE TABLE "WorkflowEnd" (
	"endOID" TEXT NOT NULL, 
	content TEXT, 
	"WorkflowDef_oID" TEXT, 
	PRIMARY KEY ("endOID", content, "WorkflowDef_oID"), 
	FOREIGN KEY("WorkflowDef_oID") REFERENCES "WorkflowDef" ("oID")
);

CREATE TABLE "DefaultTransition" (
	"targetTransitionOID" TEXT NOT NULL, 
	"Branching_oID" TEXT, 
	PRIMARY KEY ("targetTransitionOID", "Branching_oID"), 
	FOREIGN KEY("Branching_oID") REFERENCES "Branching" ("oID")
);

CREATE TABLE "TargetTransition" (
	"targetTransitionOID" TEXT NOT NULL, 
	"conditionOID" TEXT, 
	"Branching_oID" TEXT, 
	PRIMARY KEY ("targetTransitionOID", "conditionOID", "Branching_oID"), 
	FOREIGN KEY("Branching_oID") REFERENCES "Branching" ("oID")
);
