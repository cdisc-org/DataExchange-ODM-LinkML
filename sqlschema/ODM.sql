

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
	"ID" TEXT NOT NULL, 
	comment TEXT, 
	coding TEXT, 
	PRIMARY KEY ("ID")
);

CREATE TABLE "Arm" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"workflowRef" TEXT, 
	PRIMARY KEY ("OID")
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

CREATE TABLE "CommentDef" (
	"OID" TEXT NOT NULL, 
	description TEXT, 
	"documentRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "Country" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "CRFCompletionInstructions" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
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
	PRIMARY KEY ("leafID")
);

CREATE TABLE "Epoch" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"sequenceNumber" INTEGER NOT NULL, 
	description TEXT, 
	PRIMARY KEY ("OID")
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

CREATE TABLE "InclusionCriteria" (
	criterion TEXT, 
	PRIMARY KEY (criterion)
);

CREATE TABLE "InclusionExclusionCriteria" (
	"inclusionCriteria" TEXT, 
	"exclusionCriteria" TEXT, 
	PRIMARY KEY ("inclusionCriteria", "exclusionCriteria")
);

CREATE TABLE "Leaf" (
	"ID" TEXT NOT NULL, 
	href TEXT NOT NULL, 
	title TEXT, 
	PRIMARY KEY ("ID")
);

CREATE TABLE "LegalReason" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Location" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	role TEXT, 
	"organizationOID" TEXT, 
	description TEXT, 
	address TEXT, 
	telecom TEXT, 
	"query" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("organizationOID") REFERENCES "Organization" ("OID")
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
	PRIMARY KEY ("fileOID"), 
	FOREIGN KEY("priorFileOID") REFERENCES "ODMFileMetadata" ("fileOID")
);

CREATE TABLE "Organization" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	role TEXT, 
	type VARCHAR(18) NOT NULL, 
	"locationOID" TEXT, 
	"partOfOrganizationOID" TEXT, 
	description TEXT, 
	address TEXT, 
	telecom TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("locationOID") REFERENCES "Location" ("OID"), 
	FOREIGN KEY("partOfOrganizationOID") REFERENCES "Organization" ("OID")
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
	"OID" TEXT NOT NULL, 
	source VARCHAR(15) NOT NULL, 
	target TEXT, 
	type VARCHAR(6), 
	state VARCHAR(9) NOT NULL, 
	"lastUpdateDatetime" DATETIME NOT NULL, 
	name TEXT, 
	value TEXT, 
	"auditRecord" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "Question" (
	"translatedText" TEXT, 
	PRIMARY KEY ("translatedText")
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
	"ID" TEXT NOT NULL, 
	"userRef" TEXT, 
	"locationRef" TEXT, 
	"signatureRef" TEXT, 
	"dateTimeStamp" TEXT, 
	PRIMARY KEY ("ID")
);

CREATE TABLE "SignatureDef" (
	"OID" TEXT NOT NULL, 
	methodology VARCHAR(10), 
	meaning TEXT, 
	"legalReason" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "SourceID" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "SourceItems" (
	"sourceItem" TEXT, 
	coding TEXT, 
	PRIMARY KEY ("sourceItem", coding)
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
	"OID" TEXT NOT NULL, 
	"studyName" TEXT NOT NULL, 
	"protocolName" TEXT NOT NULL, 
	"versionID" TEXT, 
	"versionName" TEXT, 
	status TEXT, 
	description TEXT, 
	"metaDataVersion" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyEndPoint" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type VARCHAR(9), 
	level VARCHAR(11), 
	description TEXT, 
	"formalExpression" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyEndPoints" (
	"studyEndPoint" TEXT, 
	PRIMARY KEY ("studyEndPoint")
);

CREATE TABLE "StudyEstimand" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	level VARCHAR(11), 
	description TEXT, 
	"studyTargetPopulationRef" TEXT, 
	"studyInterventionRef" TEXT, 
	"studyEndPointRef" TEXT, 
	"summaryMeasure" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyEstimands" (
	"studyEstimand" TEXT, 
	PRIMARY KEY ("studyEstimand")
);

CREATE TABLE "StudyIndication" (
	"OID" TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyIndications" (
	"studyIndication" TEXT, 
	PRIMARY KEY ("studyIndication")
);

CREATE TABLE "StudyIntervention" (
	"OID" TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyInterventions" (
	"studyIntervention" TEXT, 
	PRIMARY KEY ("studyIntervention")
);

CREATE TABLE "StudyObjective" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	level VARCHAR(11), 
	description TEXT, 
	"studyEndPointRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyObjectives" (
	"studyObjective" TEXT, 
	PRIMARY KEY ("studyObjective")
);

CREATE TABLE "StudyParameter" (
	"OID" TEXT NOT NULL, 
	term TEXT NOT NULL, 
	"shortName" TEXT, 
	"parameterValue" TEXT, 
	coding TEXT, 
	PRIMARY KEY ("OID")
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
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	"formalExpression" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "StudyTiming" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	PRIMARY KEY ("OID")
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

CREATE TABLE "UserName" (
	content TEXT, 
	PRIMARY KEY (content)
);

CREATE TABLE "Value" (
	"seqNum" INTEGER, 
	content TEXT, 
	PRIMARY KEY ("seqNum", content)
);

CREATE TABLE "ValueListDef" (
	"OID" TEXT NOT NULL, 
	description TEXT, 
	"itemRef" TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "WorkflowDef" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"workflowStart" TEXT, 
	transition TEXT, 
	PRIMARY KEY ("OID")
);

CREATE TABLE "WorkflowStart" (
	"startOID" TEXT NOT NULL, 
	PRIMARY KEY ("startOID")
);

CREATE TABLE "AdminData" (
	"studyOID" TEXT, 
	user TEXT, 
	organization TEXT, 
	location TEXT, 
	"signatureDef" TEXT, 
	"ODMFileMetadata_fileOID" TEXT, 
	PRIMARY KEY ("studyOID", user, organization, location, "signatureDef", "ODMFileMetadata_fileOID"), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("ODMFileMetadata_fileOID") REFERENCES "ODMFileMetadata" ("fileOID")
);

CREATE TABLE "Branching" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type VARCHAR(9) NOT NULL, 
	"WorkflowDef_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("WorkflowDef_OID") REFERENCES "WorkflowDef" ("OID")
);

CREATE TABLE "ConditionDef" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"commentOID" TEXT, 
	description TEXT, 
	"methodSignature" TEXT, 
	"formalExpression" TEXT, 
	alias TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "DurationTimingConstraint" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"structuralElementOID" TEXT NOT NULL, 
	"durationTarget" TEXT NOT NULL, 
	"durationPreWindow" TEXT, 
	"durationPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);

CREATE TABLE "Flag" (
	"flagValue" TEXT, 
	"flagType" TEXT, 
	"Annotation_ID" TEXT, 
	PRIMARY KEY ("flagValue", "flagType", "Annotation_ID"), 
	FOREIGN KEY("Annotation_ID") REFERENCES "Annotation" ("ID")
);

CREATE TABLE "IntercurrentEvent" (
	description TEXT, 
	"StudyEstimand_OID" TEXT, 
	PRIMARY KEY (description, "StudyEstimand_OID"), 
	FOREIGN KEY("StudyEstimand_OID") REFERENCES "StudyEstimand" ("OID")
);

CREATE TABLE "ItemDef" (
	"OID" TEXT NOT NULL, 
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
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "LocationRef" (
	"locationOID" TEXT NOT NULL, 
	PRIMARY KEY ("locationOID"), 
	FOREIGN KEY("locationOID") REFERENCES "Location" ("OID")
);

CREATE TABLE "MetaDataVersion" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"commentOID" TEXT, 
	description TEXT, 
	include TEXT, 
	standards TEXT, 
	"annotatedCRF" TEXT, 
	"supplementalDoc" TEXT, 
	"valueListDef" TEXT, 
	"whereClauseDef" TEXT, 
	protocol TEXT, 
	"workflowDef" TEXT, 
	"studyEventGroupDef" TEXT, 
	"studyEventDef" TEXT, 
	"itemGroupDef" TEXT, 
	"itemDef" TEXT, 
	"codeList" TEXT, 
	"conditionDef" TEXT, 
	"methodDef" TEXT, 
	"commentDef" TEXT, 
	leaf TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "MethodDef" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type VARCHAR(11), 
	"commentOID" TEXT, 
	description TEXT, 
	"methodSignature" TEXT, 
	"formalExpression" TEXT, 
	alias TEXT, 
	"documentRef" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "PDFPageRef" (
	"pageRefs" TEXT, 
	"firstPage" INTEGER, 
	"lastPage" INTEGER, 
	type VARCHAR(16) NOT NULL, 
	title TEXT, 
	"DocumentRef_leafID" TEXT, 
	PRIMARY KEY ("pageRefs", "firstPage", "lastPage", type, title, "DocumentRef_leafID"), 
	FOREIGN KEY("DocumentRef_leafID") REFERENCES "DocumentRef" ("leafID")
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
	FOREIGN KEY("studyTargetPopulation") REFERENCES "StudyTargetPopulation" ("OID")
);

CREATE TABLE "RelativeTimingConstraint" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"predecessorOID" TEXT, 
	"successorOID" TEXT, 
	type VARCHAR(14), 
	"timepointRelativeTarget" TEXT NOT NULL, 
	"timepointPreWindow" TEXT, 
	"timepointPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);

CREATE TABLE "SignatureRef" (
	"signatureOID" TEXT NOT NULL, 
	PRIMARY KEY ("signatureOID"), 
	FOREIGN KEY("signatureOID") REFERENCES "SignatureDef" ("OID")
);

CREATE TABLE "SiteRef" (
	"locationOID" TEXT NOT NULL, 
	PRIMARY KEY ("locationOID"), 
	FOREIGN KEY("locationOID") REFERENCES "Location" ("OID")
);

CREATE TABLE "Standard" (
	"OID" TEXT NOT NULL, 
	name VARCHAR(11) NOT NULL, 
	type VARCHAR(2) NOT NULL, 
	"publishingSet" VARCHAR(10), 
	version TEXT NOT NULL, 
	status TEXT NOT NULL, 
	"commentOID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "StudyEndPointRef" (
	"studyEndPointOID" TEXT NOT NULL, 
	"orderNumber" INTEGER, 
	PRIMARY KEY ("studyEndPointOID", "orderNumber"), 
	FOREIGN KEY("studyEndPointOID") REFERENCES "StudyEndPoint" ("OID")
);

CREATE TABLE "StudyEventDef" (
	"OID" TEXT NOT NULL, 
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
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "StudyEventGroupDef" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"armOID" TEXT, 
	"epochOID" TEXT, 
	"commentOID" TEXT, 
	description TEXT, 
	"workflowRef" TEXT, 
	coding TEXT, 
	"studyEventGroupRef" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("armOID") REFERENCES "Arm" ("OID"), 
	FOREIGN KEY("epochOID") REFERENCES "Epoch" ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "StudyInterventionRef" (
	"studyInterventionOID" TEXT NOT NULL, 
	PRIMARY KEY ("studyInterventionOID"), 
	FOREIGN KEY("studyInterventionOID") REFERENCES "StudyIntervention" ("OID")
);

CREATE TABLE "StudyTargetPopulationRef" (
	"studyTargetPopulationOID" TEXT NOT NULL, 
	PRIMARY KEY ("studyTargetPopulationOID"), 
	FOREIGN KEY("studyTargetPopulationOID") REFERENCES "StudyTargetPopulation" ("OID")
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
	FOREIGN KEY(signature) REFERENCES "Signature" ("ID"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("ID")
);

CREATE TABLE "User" (
	"OID" TEXT NOT NULL, 
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
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("organizationOID") REFERENCES "Organization" ("OID"), 
	FOREIGN KEY("locationOID") REFERENCES "Location" ("OID")
);

CREATE TABLE "ValueListRef" (
	"valueListOID" TEXT NOT NULL, 
	PRIMARY KEY ("valueListOID"), 
	FOREIGN KEY("valueListOID") REFERENCES "ValueListDef" ("OID")
);

CREATE TABLE "WhereClauseDef" (
	"OID" TEXT NOT NULL, 
	"commentOID" TEXT, 
	"rangeCheck" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID")
);

CREATE TABLE "WorkflowEnd" (
	"endOID" TEXT NOT NULL, 
	content TEXT, 
	"WorkflowDef_OID" TEXT, 
	PRIMARY KEY ("endOID", content, "WorkflowDef_OID"), 
	FOREIGN KEY("WorkflowDef_OID") REFERENCES "WorkflowDef" ("OID")
);

CREATE TABLE "WorkflowRef" (
	"workflowOID" TEXT NOT NULL, 
	PRIMARY KEY ("workflowOID"), 
	FOREIGN KEY("workflowOID") REFERENCES "WorkflowDef" ("OID")
);

CREATE TABLE "AbsoluteTimingConstraint" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"studyEventGroupOID" TEXT, 
	"studyEventOID" TEXT, 
	"timepointTarget" TEXT NOT NULL, 
	"timepointPreWindow" TEXT, 
	"timepointPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("studyEventGroupOID") REFERENCES "StudyEventGroupDef" ("OID"), 
	FOREIGN KEY("studyEventOID") REFERENCES "StudyEventDef" ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);

CREATE TABLE "Association" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	"keySet" TEXT, 
	annotation TEXT, 
	"ODMFileMetadata_fileOID" TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "keySet", annotation, "ODMFileMetadata_fileOID"), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("metaDataVersionOID") REFERENCES "MetaDataVersion" ("OID"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("ID"), 
	FOREIGN KEY("ODMFileMetadata_fileOID") REFERENCES "ODMFileMetadata" ("fileOID")
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
	"ODMFileMetadata_fileOID" TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "subjectData", "itemGroupData", "query", "auditRecord", signature, annotation, "ODMFileMetadata_fileOID"), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("metaDataVersionOID") REFERENCES "MetaDataVersion" ("OID"), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("ID"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("ID"), 
	FOREIGN KEY("ODMFileMetadata_fileOID") REFERENCES "ODMFileMetadata" ("fileOID")
);

CREATE TABLE "CodeList" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"dataType" VARCHAR(7) NOT NULL, 
	"commentOID" TEXT, 
	"standardOID" TEXT, 
	"isNonStandard" VARCHAR, 
	description TEXT, 
	coding TEXT, 
	alias TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID"), 
	FOREIGN KEY("standardOID") REFERENCES "Standard" ("OID")
);

CREATE TABLE "Criterion" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"conditionOID" TEXT NOT NULL, 
	description TEXT, 
	coding TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("conditionOID") REFERENCES "ConditionDef" ("OID")
);

CREATE TABLE "Include" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	href TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", href), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("metaDataVersionOID") REFERENCES "MetaDataVersion" ("OID")
);

CREATE TABLE "InvestigatorRef" (
	"userOID" TEXT NOT NULL, 
	PRIMARY KEY ("userOID"), 
	FOREIGN KEY("userOID") REFERENCES "User" ("OID")
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
	FOREIGN KEY("itemOID") REFERENCES "ItemDef" ("OID"), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("ID"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("ID")
);

CREATE TABLE "ItemGroupDef" (
	"OID" TEXT NOT NULL, 
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
	"itemGroupClass" TEXT, 
	coding TEXT, 
	"workflowRef" TEXT, 
	origin TEXT, 
	alias TEXT, 
	leaf TEXT, 
	"itemGroupRef" TEXT, 
	"itemRef" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("archiveLocationID") REFERENCES "Leaf" ("ID"), 
	FOREIGN KEY("standardOID") REFERENCES "Standard" ("OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID"), 
	FOREIGN KEY(leaf) REFERENCES "Leaf" ("ID")
);

CREATE TABLE "MetaDataVersionRef" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	"effectiveDate" DATE NOT NULL, 
	"Location_OID" TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "effectiveDate", "Location_OID"), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("metaDataVersionOID") REFERENCES "MetaDataVersion" ("OID"), 
	FOREIGN KEY("Location_OID") REFERENCES "Location" ("OID")
);

CREATE TABLE "RangeCheck" (
	comparator VARCHAR(5), 
	"softHard" VARCHAR(4), 
	"itemOID" TEXT, 
	"errorMessage" TEXT, 
	"methodSignature" TEXT, 
	"formalExpression" TEXT, 
	"checkValue" TEXT, 
	PRIMARY KEY (comparator, "softHard", "itemOID", "errorMessage", "methodSignature", "formalExpression", "checkValue"), 
	FOREIGN KEY("itemOID") REFERENCES "ItemDef" ("OID")
);

CREATE TABLE "ReferenceData" (
	"studyOID" TEXT NOT NULL, 
	"metaDataVersionOID" TEXT NOT NULL, 
	"itemGroupData" TEXT, 
	"auditRecord" TEXT, 
	signature TEXT, 
	annotation TEXT, 
	"ODMFileMetadata_fileOID" TEXT, 
	PRIMARY KEY ("studyOID", "metaDataVersionOID", "itemGroupData", "auditRecord", signature, annotation, "ODMFileMetadata_fileOID"), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("metaDataVersionOID") REFERENCES "MetaDataVersion" ("OID"), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("ID"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("ID"), 
	FOREIGN KEY("ODMFileMetadata_fileOID") REFERENCES "ODMFileMetadata" ("fileOID")
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
	FOREIGN KEY("studyEventOID") REFERENCES "StudyEventDef" ("OID"), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("ID"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("ID")
);

CREATE TABLE "StudyEventGroupRef" (
	"studyEventGroupOID" TEXT NOT NULL, 
	"orderNumber" INTEGER, 
	mandatory VARCHAR(3) NOT NULL, 
	"collectionExceptionConditionOID" TEXT, 
	description TEXT, 
	PRIMARY KEY ("studyEventGroupOID", "orderNumber", mandatory, "collectionExceptionConditionOID", description), 
	FOREIGN KEY("studyEventGroupOID") REFERENCES "StudyEventGroupDef" ("OID"), 
	FOREIGN KEY("collectionExceptionConditionOID") REFERENCES "ConditionDef" ("OID")
);

CREATE TABLE "StudyEventRef" (
	"studyEventOID" TEXT NOT NULL, 
	"orderNumber" INTEGER, 
	mandatory VARCHAR(3) NOT NULL, 
	"collectionExceptionConditionOID" TEXT, 
	"StudyEventGroupDef_OID" TEXT, 
	PRIMARY KEY ("studyEventOID", "orderNumber", mandatory, "collectionExceptionConditionOID", "StudyEventGroupDef_OID"), 
	FOREIGN KEY("studyEventOID") REFERENCES "StudyEventDef" ("OID"), 
	FOREIGN KEY("collectionExceptionConditionOID") REFERENCES "ConditionDef" ("OID"), 
	FOREIGN KEY("StudyEventGroupDef_OID") REFERENCES "StudyEventGroupDef" ("OID")
);

CREATE TABLE "Transition" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"sourceOID" TEXT NOT NULL, 
	"targetOID" TEXT NOT NULL, 
	"startConditionOID" TEXT, 
	"endConditionOID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("startConditionOID") REFERENCES "ConditionDef" ("OID"), 
	FOREIGN KEY("endConditionOID") REFERENCES "ConditionDef" ("OID")
);

CREATE TABLE "UserRef" (
	"userOID" TEXT NOT NULL, 
	PRIMARY KEY ("userOID"), 
	FOREIGN KEY("userOID") REFERENCES "User" ("OID")
);

CREATE TABLE "WhereClauseRef" (
	"whereClauseOID" TEXT NOT NULL, 
	PRIMARY KEY ("whereClauseOID"), 
	FOREIGN KEY("whereClauseOID") REFERENCES "WhereClauseDef" ("OID")
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
	"CodeList_OID" TEXT, 
	PRIMARY KEY ("codedValue", rank, other, "orderNumber", "extendedValue", "commentOID", description, decode, coding, alias, "CodeList_OID"), 
	FOREIGN KEY("commentOID") REFERENCES "CommentDef" ("OID"), 
	FOREIGN KEY("CodeList_OID") REFERENCES "CodeList" ("OID")
);

CREATE TABLE "CodeListRef" (
	"codeListOID" TEXT NOT NULL, 
	PRIMARY KEY ("codeListOID"), 
	FOREIGN KEY("codeListOID") REFERENCES "CodeList" ("OID")
);

CREATE TABLE "DefaultTransition" (
	"targetTransitionOID" TEXT NOT NULL, 
	"Branching_OID" TEXT, 
	PRIMARY KEY ("targetTransitionOID", "Branching_OID"), 
	FOREIGN KEY("targetTransitionOID") REFERENCES "Transition" ("OID"), 
	FOREIGN KEY("Branching_OID") REFERENCES "Branching" ("OID")
);

CREATE TABLE "FlagType" (
	"codeListOID" TEXT NOT NULL, 
	content TEXT, 
	PRIMARY KEY ("codeListOID", content), 
	FOREIGN KEY("codeListOID") REFERENCES "CodeList" ("OID")
);

CREATE TABLE "FlagValue" (
	"codeListOID" TEXT NOT NULL, 
	content TEXT, 
	PRIMARY KEY ("codeListOID", content), 
	FOREIGN KEY("codeListOID") REFERENCES "CodeList" ("OID")
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
	FOREIGN KEY("itemGroupOID") REFERENCES "ItemGroupDef" ("OID"), 
	FOREIGN KEY(signature) REFERENCES "Signature" ("ID"), 
	FOREIGN KEY(annotation) REFERENCES "Annotation" ("ID")
);

CREATE TABLE "ItemGroupRef" (
	"itemGroupOID" TEXT NOT NULL, 
	"methodOID" TEXT, 
	"orderNumber" INTEGER, 
	mandatory VARCHAR(3) NOT NULL, 
	"collectionExceptionConditionOID" TEXT, 
	PRIMARY KEY ("itemGroupOID", "methodOID", "orderNumber", mandatory, "collectionExceptionConditionOID"), 
	FOREIGN KEY("itemGroupOID") REFERENCES "ItemGroupDef" ("OID"), 
	FOREIGN KEY("methodOID") REFERENCES "MethodDef" ("OID"), 
	FOREIGN KEY("collectionExceptionConditionOID") REFERENCES "ConditionDef" ("OID")
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
	PRIMARY KEY ("itemOID", "keySequence", "isNonStandard", "hasNoData", "methodOID", "unitsItemOID", repeat, other, role, "roleCodeListOID", core, "preSpecifiedValue", "orderNumber", mandatory, "collectionExceptionConditionOID", origin, "whereClauseRef"), 
	FOREIGN KEY("itemOID") REFERENCES "ItemDef" ("OID"), 
	FOREIGN KEY("methodOID") REFERENCES "MethodDef" ("OID"), 
	FOREIGN KEY("unitsItemOID") REFERENCES "ItemDef" ("OID"), 
	FOREIGN KEY("roleCodeListOID") REFERENCES "CodeList" ("OID"), 
	FOREIGN KEY("collectionExceptionConditionOID") REFERENCES "ConditionDef" ("OID")
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
	PRIMARY KEY ("studyOID", "subjectKey", "metaDataVersionOID", "studyEventOID", "studyEventRepeatKey", "itemGroupOID", "itemGroupRepeatKey", "itemOID"), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("metaDataVersionOID") REFERENCES "MetaDataVersion" ("OID"), 
	FOREIGN KEY("studyEventOID") REFERENCES "StudyEventDef" ("OID"), 
	FOREIGN KEY("itemGroupOID") REFERENCES "ItemGroupDef" ("OID"), 
	FOREIGN KEY("itemOID") REFERENCES "ItemDef" ("OID")
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
	PRIMARY KEY ("itemOID", "itemGroupOID", "metaDataVersionOID", "studyOID", "leafID", name, resource, coding), 
	FOREIGN KEY("itemOID") REFERENCES "ItemDef" ("OID"), 
	FOREIGN KEY("itemGroupOID") REFERENCES "ItemGroupDef" ("OID"), 
	FOREIGN KEY("metaDataVersionOID") REFERENCES "MetaDataVersion" ("OID"), 
	FOREIGN KEY("studyOID") REFERENCES "Study" ("OID"), 
	FOREIGN KEY("leafID") REFERENCES "Leaf" ("ID")
);

CREATE TABLE "TargetTransition" (
	"targetTransitionOID" TEXT NOT NULL, 
	"conditionOID" TEXT, 
	"Branching_OID" TEXT, 
	PRIMARY KEY ("targetTransitionOID", "conditionOID", "Branching_OID"), 
	FOREIGN KEY("targetTransitionOID") REFERENCES "Transition" ("OID"), 
	FOREIGN KEY("conditionOID") REFERENCES "ConditionDef" ("OID"), 
	FOREIGN KEY("Branching_OID") REFERENCES "Branching" ("OID")
);

CREATE TABLE "TransitionTimingConstraint" (
	"OID" TEXT NOT NULL, 
	name TEXT NOT NULL, 
	"transitionOID" TEXT NOT NULL, 
	"methodOID" TEXT, 
	type VARCHAR(14), 
	"timepointTarget" TEXT NOT NULL, 
	"timepointPreWindow" TEXT, 
	"timepointPostWindow" TEXT, 
	description TEXT, 
	"StudyTiming_OID" TEXT, 
	PRIMARY KEY ("OID"), 
	FOREIGN KEY("transitionOID") REFERENCES "Transition" ("OID"), 
	FOREIGN KEY("methodOID") REFERENCES "MethodDef" ("OID"), 
	FOREIGN KEY("StudyTiming_OID") REFERENCES "StudyTiming" ("OID")
);
