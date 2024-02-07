# Auto generated from ODM.yaml by pythongen.py version: 0.9.0
# Generation date: 2024-02-04T20:37:35
# Schema: odm
#
# id: http://www.cdisc.org/ns/odm/v2.0
# description: ODM is a vendor-neutral, platform-independent format for exchanging and archiving clinical and translational research data, along with their associated metadata, administrative data, reference data, and audit information.
# license:

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
ODM = CurieNamespace('odm', 'http://www.cdisc.org/ns/odm/v2.0/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XHTML = CurieNamespace('xhtml', 'http://www.w3.org/1999/xhtml#')
XML = CurieNamespace('xml', 'http://www.w3.org/XML/1998/namespace#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ODM


# Types
class Text(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.text
    type_class_curie = "odm:text"
    type_name = "text"
    type_model_uri = ODM.Text


class PositiveInteger(int):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.positiveInteger
    type_class_curie = "odm:positiveInteger"
    type_name = "positiveInteger"
    type_model_uri = ODM.PositiveInteger


class HexBinary(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.hexBinary
    type_class_curie = "odm:hexBinary"
    type_name = "hexBinary"
    type_model_uri = ODM.HexBinary


class Base64Binary(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.base64Binary
    type_class_curie = "odm:base64Binary"
    type_name = "base64Binary"
    type_model_uri = ODM.Base64Binary


class HexFloat(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.hexFloat
    type_class_curie = "odm:hexFloat"
    type_name = "hexFloat"
    type_model_uri = ODM.HexFloat


class Base64Float(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.base64Float
    type_class_curie = "odm:base64Float"
    type_name = "base64Float"
    type_model_uri = ODM.Base64Float


class EmptyTag(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.emptyTag
    type_class_curie = "odm:emptyTag"
    type_name = "emptyTag"
    type_model_uri = ODM.EmptyTag


class PartialDate(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.partialDate
    type_class_curie = "odm:partialDate"
    type_name = "partialDate"
    type_model_uri = ODM.PartialDate


class THour(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.tHour
    type_class_curie = "odm:tHour"
    type_name = "tHour"
    type_model_uri = ODM.THour


class PartialTime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.partialTime
    type_class_curie = "odm:partialTime"
    type_name = "partialTime"
    type_model_uri = ODM.PartialTime


class TDatetime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.tDatetime
    type_class_curie = "odm:tDatetime"
    type_name = "tDatetime"
    type_model_uri = ODM.TDatetime


class PartialDatetime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.partialDatetime
    type_class_curie = "odm:partialDatetime"
    type_name = "partialDatetime"
    type_model_uri = ODM.PartialDatetime


class TDuration(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.tDuration
    type_class_curie = "odm:tDuration"
    type_name = "tDuration"
    type_model_uri = ODM.TDuration


class DurationDatetime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.durationDatetime
    type_class_curie = "odm:durationDatetime"
    type_name = "durationDatetime"
    type_model_uri = ODM.DurationDatetime


class TInterval(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.tInterval
    type_class_curie = "odm:tInterval"
    type_name = "tInterval"
    type_model_uri = ODM.TInterval


class IntervalDatetime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.intervalDatetime
    type_class_curie = "odm:intervalDatetime"
    type_name = "intervalDatetime"
    type_model_uri = ODM.IntervalDatetime


class TIncomplete(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.tIncomplete
    type_class_curie = "odm:tIncomplete"
    type_name = "tIncomplete"
    type_model_uri = ODM.TIncomplete


class IncompleteDatetime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.incompleteDatetime
    type_class_curie = "odm:incompleteDatetime"
    type_name = "incompleteDatetime"
    type_model_uri = ODM.IncompleteDatetime


class TIncompleteDate(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.tIncompleteDate
    type_class_curie = "odm:tIncompleteDate"
    type_name = "tIncompleteDate"
    type_model_uri = ODM.TIncompleteDate


class TIncompleteTime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.tIncompleteTime
    type_class_curie = "odm:tIncompleteTime"
    type_name = "tIncompleteTime"
    type_model_uri = ODM.TIncompleteTime


class IncompleteTime(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.incompleteTime
    type_class_curie = "odm:incompleteTime"
    type_name = "incompleteTime"
    type_model_uri = ODM.IncompleteTime


class IncompleteDate(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.incompleteDate
    type_class_curie = "odm:incompleteDate"
    type_name = "incompleteDate"
    type_model_uri = ODM.IncompleteDate


class Oid(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.oid
    type_class_curie = "odm:oid"
    type_name = "oid"
    type_model_uri = ODM.Oid


class Oidref(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.oidref
    type_class_curie = "odm:oidref"
    type_name = "oidref"
    type_model_uri = ODM.Oidref


class ValueType(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.valueType
    type_class_curie = "odm:valueType"
    type_name = "valueType"
    type_model_uri = ODM.ValueType


class SubjectKeyType(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.subjectKeyType
    type_class_curie = "odm:subjectKeyType"
    type_name = "subjectKeyType"
    type_model_uri = ODM.SubjectKeyType


class RepeatKey(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.repeatKey
    type_class_curie = "odm:repeatKey"
    type_name = "repeatKey"
    type_model_uri = ODM.RepeatKey


class NameType(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.nameType
    type_class_curie = "odm:nameType"
    type_name = "nameType"
    type_model_uri = ODM.NameType


class FileName(URIorCURIE):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.fileName
    type_class_curie = "odm:fileName"
    type_name = "fileName"
    type_model_uri = ODM.FileName


class ODMVersion(str):
    """ Version of ODM that the file conforms to. """
    type_class_uri = ODM.ODMVersion
    type_class_curie = "odm:ODMVersion"
    type_name = "ODMVersion"
    type_model_uri = ODM.ODMVersion


class TrialPhaseType(str):
    """ A terminology codelist relevant to the phase, or stage, of the
                clinical trial. """
    type_class_uri = ODM.TrialPhaseType
    type_class_curie = "odm:TrialPhaseType"
    type_name = "TrialPhaseType"
    type_model_uri = ODM.TrialPhaseType


class ItemGroupTypeType(str):
    """ https://wiki.cdisc.org/display/PUB/Data+Formats """
    type_class_uri = ODM.ItemGroupTypeType
    type_class_curie = "odm:ItemGroupTypeType"
    type_name = "ItemGroupTypeType"
    type_model_uri = ODM.ItemGroupTypeType


class CoreType(str):
    """ Core. """
    type_class_uri = ODM.CoreType
    type_class_curie = "odm:CoreType"
    type_name = "CoreType"
    type_model_uri = ODM.CoreType


class StandardStatus(str):
    """ Terminology relevant to the development or publication status of the
                standard. """
    type_class_uri = ODM.StandardStatus
    type_class_curie = "odm:StandardStatus"
    type_name = "StandardStatus"
    type_model_uri = ODM.StandardStatus


class DictionaryNameType(str):
    """ A name given to a reference source that lists words and gives their
                meaning. (NCI) """
    type_class_uri = ODM.DictionaryNameType
    type_class_curie = "odm:DictionaryNameType"
    type_name = "DictionaryNameType"
    type_model_uri = ODM.DictionaryNameType


class ItemGroupClassSubClass(str):
    """ Sub class of a general observation class. Union of ItemGroupClass and
                ItemGroupSubClass """
    type_class_uri = ODM.ItemGroupClassSubClass
    type_class_curie = "odm:ItemGroupClassSubClass"
    type_name = "ItemGroupClassSubClass"
    type_model_uri = ODM.ItemGroupClassSubClass


class LanguageType(str):
    """ language context for internationalisation and localisation """
    type_class_uri = XML.lang
    type_class_curie = "xml:lang"
    type_name = "languageType"
    type_model_uri = ODM.LanguageType


class ContentType(str):
    """ multi-line text content from between XML tags """
    type_class_uri = XHTML.div
    type_class_curie = "xhtml:div"
    type_name = "contentType"
    type_model_uri = ODM.ContentType


class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = ODM.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = ODM.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = ODM.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = ODM.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = ODM.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = ODM.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = ODM.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = ODM.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = ODM.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = ODM.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = ODM.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = ODM.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = ODM.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = ODM.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = ODM.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = ODM.Nodeidentifier


# Class references
class StudyOID(extended_str):
    pass


class MetaDataVersionOID(extended_str):
    pass


class DocumentRefLeafID(extended_str):
    pass


class LeafID(extended_str):
    pass


class StandardOID(extended_str):
    pass


class ValueListDefOID(extended_str):
    pass


class WhereClauseDefOID(extended_str):
    pass


class StudyEventGroupDefOID(extended_str):
    pass


class StudyEventDefOID(extended_str):
    pass


class ItemGroupDefOID(extended_str):
    pass


class ItemDefOID(extended_str):
    pass


class CodeListOID(extended_str):
    pass


class MethodDefOID(extended_str):
    pass


class ConditionDefOID(extended_str):
    pass


class CommentDefOID(extended_str):
    pass


class StudyIndicationOID(extended_str):
    pass


class StudyInterventionOID(extended_str):
    pass


class StudyObjectiveOID(extended_str):
    pass


class StudyEndPointOID(extended_str):
    pass


class StudyTargetPopulationOID(extended_str):
    pass


class StudyEstimandOID(extended_str):
    pass


class ArmOID(extended_str):
    pass


class EpochOID(extended_str):
    pass


class StudyParameterOID(extended_str):
    pass


class StudyTimingOID(extended_str):
    pass


class TransitionTimingConstraintOID(extended_str):
    pass


class AbsoluteTimingConstraintOID(extended_str):
    pass


class RelativeTimingConstraintOID(extended_str):
    pass


class DurationTimingConstraintOID(extended_str):
    pass


class WorkflowDefOID(extended_str):
    pass


class TransitionOID(extended_str):
    pass


class BranchingOID(extended_str):
    pass


class CriterionOID(extended_str):
    pass


class UserOID(extended_str):
    pass


class OrganizationOID(extended_str):
    pass


class LocationOID(extended_str):
    pass


class SignatureDefOID(extended_str):
    pass


class SignatureID(extended_str):
    pass


class AnnotationID(extended_str):
    pass


class QueryOID(extended_str):
    pass


class ODMFileMetadataFileOID(extended_str):
    pass


@dataclass
class Alias(YAMLRoot):
    """
    An Alias provides an additional name for an element. The Context attribute specifies the application domain in
    which this additional name is relevant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Alias
    class_class_curie: ClassVar[str] = "odm:Alias"
    class_name: ClassVar[str] = "Alias"
    class_model_uri: ClassVar[URIRef] = ODM.Alias

    context: str = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, str):
            self.context = str(self.context)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Description(YAMLRoot):
    """
    A free-text description of the containing metadata component, unless restricted by Business Rules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Description
    class_class_curie: ClassVar[str] = "odm:Description"
    class_name: ClassVar[str] = "Description"
    class_model_uri: ClassVar[URIRef] = ODM.Description

    translatedText: Optional[Union[Union[dict, "TranslatedText"], List[Union[dict, "TranslatedText"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class TranslatedText(YAMLRoot):
    """
    Human-readable text that is appropriate for a particular language. TranslatedText elements typically occur in a
    series, presenting a set of alternative textual renditions for different languages and types.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.TranslatedText
    class_class_curie: ClassVar[str] = "odm:TranslatedText"
    class_name: ClassVar[str] = "TranslatedText"
    class_model_uri: ClassVar[URIRef] = ODM.TranslatedText

    type: str = None
    language: Optional[str] = None
    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Study(YAMLRoot):
    """
    This element collects static structural information about an individual study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Study
    class_class_curie: ClassVar[str] = "odm:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = ODM.Study

    OID: Union[str, StudyOID] = None
    studyName: str = None
    protocolName: str = None
    versionID: Optional[str] = None
    versionName: Optional[str] = None
    status: Optional[str] = None
    description: Optional[Union[dict, Description]] = None
    metaDataVersion: Optional[Union[Dict[Union[str, MetaDataVersionOID], Union[dict, "MetaDataVersion"]], List[Union[dict, "MetaDataVersion"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyOID):
            self.OID = StudyOID(self.OID)

        if self._is_empty(self.studyName):
            self.MissingRequiredField("studyName")
        if not isinstance(self.studyName, str):
            self.studyName = str(self.studyName)

        if self._is_empty(self.protocolName):
            self.MissingRequiredField("protocolName")
        if not isinstance(self.protocolName, str):
            self.protocolName = str(self.protocolName)

        if self.versionID is not None and not isinstance(self.versionID, str):
            self.versionID = str(self.versionID)

        if self.versionName is not None and not isinstance(self.versionName, str):
            self.versionName = str(self.versionName)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        self._normalize_inlined_as_list(slot_name="metaDataVersion", slot_type=MetaDataVersion, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MetaDataVersion(YAMLRoot):
    """
    The metadata for a study is defined in a series of MetaDataVersion elements. Through this mechanism (multiple
    MetaDataVersion elements), the model supports the incremental deployment of "mid-stream study changes," and thus
    can handle a situation where multiple versions of the metadata are being used simultaneously (e.g., due to delays
    in IRB approval at various sites).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.MetaDataVersion
    class_class_curie: ClassVar[str] = "odm:MetaDataVersion"
    class_name: ClassVar[str] = "MetaDataVersion"
    class_model_uri: ClassVar[URIRef] = ODM.MetaDataVersion

    OID: Union[str, MetaDataVersionOID] = None
    name: str = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    include: Optional[Union[dict, "Include"]] = None
    standards: Optional[Union[dict, "Standards"]] = None
    annotatedCRF: Optional[Union[dict, "AnnotatedCRF"]] = None
    supplementalDoc: Optional[Union[dict, "SupplementalDoc"]] = None
    valueListDef: Optional[Union[Dict[Union[str, ValueListDefOID], Union[dict, "ValueListDef"]], List[Union[dict, "ValueListDef"]]]] = empty_dict()
    whereClauseDef: Optional[Union[Dict[Union[str, WhereClauseDefOID], Union[dict, "WhereClauseDef"]], List[Union[dict, "WhereClauseDef"]]]] = empty_dict()
    protocol: Optional[Union[dict, "Protocol"]] = None
    workflowDef: Optional[Union[Dict[Union[str, WorkflowDefOID], Union[dict, "WorkflowDef"]], List[Union[dict, "WorkflowDef"]]]] = empty_dict()
    studyEventGroupDef: Optional[Union[Dict[Union[str, StudyEventGroupDefOID], Union[dict, "StudyEventGroupDef"]], List[Union[dict, "StudyEventGroupDef"]]]] = empty_dict()
    studyEventDef: Optional[Union[Dict[Union[str, StudyEventDefOID], Union[dict, "StudyEventDef"]], List[Union[dict, "StudyEventDef"]]]] = empty_dict()
    itemGroupDef: Optional[Union[Dict[Union[str, ItemGroupDefOID], Union[dict, "ItemGroupDef"]], List[Union[dict, "ItemGroupDef"]]]] = empty_dict()
    itemDef: Optional[Union[Dict[Union[str, ItemDefOID], Union[dict, "ItemDef"]], List[Union[dict, "ItemDef"]]]] = empty_dict()
    codeList: Optional[Union[Dict[Union[str, CodeListOID], Union[dict, "CodeList"]], List[Union[dict, "CodeList"]]]] = empty_dict()
    conditionDef: Optional[Union[Dict[Union[str, ConditionDefOID], Union[dict, "ConditionDef"]], List[Union[dict, "ConditionDef"]]]] = empty_dict()
    methodDef: Optional[Union[Dict[Union[str, MethodDefOID], Union[dict, "MethodDef"]], List[Union[dict, "MethodDef"]]]] = empty_dict()
    commentDef: Optional[Union[Dict[Union[str, CommentDefOID], Union[dict, "CommentDef"]], List[Union[dict, "CommentDef"]]]] = empty_dict()
    leaf: Optional[Union[Dict[Union[str, LeafID], Union[dict, "Leaf"]], List[Union[dict, "Leaf"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, MetaDataVersionOID):
            self.OID = MetaDataVersionOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.include is not None and not isinstance(self.include, Include):
            self.include = Include(**as_dict(self.include))

        if self.standards is not None and not isinstance(self.standards, Standards):
            self.standards = Standards(**as_dict(self.standards))

        if self.annotatedCRF is not None and not isinstance(self.annotatedCRF, AnnotatedCRF):
            self.annotatedCRF = AnnotatedCRF(**as_dict(self.annotatedCRF))

        if self.supplementalDoc is not None and not isinstance(self.supplementalDoc, SupplementalDoc):
            self.supplementalDoc = SupplementalDoc(**as_dict(self.supplementalDoc))

        self._normalize_inlined_as_list(slot_name="valueListDef", slot_type=ValueListDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="whereClauseDef", slot_type=WhereClauseDef, key_name="OID", keyed=True)

        if self.protocol is not None and not isinstance(self.protocol, Protocol):
            self.protocol = Protocol(**as_dict(self.protocol))

        self._normalize_inlined_as_list(slot_name="workflowDef", slot_type=WorkflowDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="studyEventGroupDef", slot_type=StudyEventGroupDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="studyEventDef", slot_type=StudyEventDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="itemGroupDef", slot_type=ItemGroupDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="itemDef", slot_type=ItemDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="codeList", slot_type=CodeList, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="conditionDef", slot_type=ConditionDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="methodDef", slot_type=MethodDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="commentDef", slot_type=CommentDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="leaf", slot_type=Leaf, key_name="ID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DocumentRef(YAMLRoot):
    """
    Links to a leaf element with the location of the document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.DocumentRef
    class_class_curie: ClassVar[str] = "odm:DocumentRef"
    class_name: ClassVar[str] = "DocumentRef"
    class_model_uri: ClassVar[URIRef] = ODM.DocumentRef

    leafID: Union[str, DocumentRefLeafID] = None
    pDFPageRef: Optional[Union[Union[dict, "PDFPageRef"], List[Union[dict, "PDFPageRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.leafID):
            self.MissingRequiredField("leafID")
        if not isinstance(self.leafID, DocumentRefLeafID):
            self.leafID = DocumentRefLeafID(self.leafID)

        if not isinstance(self.pDFPageRef, list):
            self.pDFPageRef = [self.pDFPageRef] if self.pDFPageRef is not None else []
        self.pDFPageRef = [v if isinstance(v, PDFPageRef) else PDFPageRef(**as_dict(v)) for v in self.pDFPageRef]

        super().__post_init__(**kwargs)


@dataclass
class PDFPageRef(YAMLRoot):
    """
    This element is the container for CRF page references.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.PDFPageRef
    class_class_curie: ClassVar[str] = "odm:PDFPageRef"
    class_name: ClassVar[str] = "PDFPageRef"
    class_model_uri: ClassVar[URIRef] = ODM.PDFPageRef

    type: Union[str, "PDFPageType"] = None
    pageRefs: Optional[str] = None
    firstPage: Optional[int] = None
    lastPage: Optional[int] = None
    title: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, PDFPageType):
            self.type = PDFPageType(self.type)

        if self.pageRefs is not None and not isinstance(self.pageRefs, str):
            self.pageRefs = str(self.pageRefs)

        if self.firstPage is not None and not isinstance(self.firstPage, int):
            self.firstPage = int(self.firstPage)

        if self.lastPage is not None and not isinstance(self.lastPage, int):
            self.lastPage = int(self.lastPage)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass
class Leaf(YAMLRoot):
    """
    Contains the XLink information referenced by DocumentRef or ArchiveLocationID
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Leaf
    class_class_curie: ClassVar[str] = "odm:Leaf"
    class_name: ClassVar[str] = "Leaf"
    class_model_uri: ClassVar[URIRef] = ODM.Leaf

    ID: Union[str, LeafID] = None
    href: Union[str, URIorCURIE] = None
    title: Optional[Union[dict, "Title"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, LeafID):
            self.ID = LeafID(self.ID)

        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, URIorCURIE):
            self.href = URIorCURIE(self.href)

        if self.title is not None and not isinstance(self.title, Title):
            self.title = Title(**as_dict(self.title))

        super().__post_init__(**kwargs)


@dataclass
class Title(YAMLRoot):
    """
    Text with the label for the document or dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Title
    class_class_curie: ClassVar[str] = "odm:Title"
    class_name: ClassVar[str] = "Title"
    class_model_uri: ClassVar[URIRef] = ODM.Title

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Include(YAMLRoot):
    """
    The Include metadata element allows a reference to a prior metadata version.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Include
    class_class_curie: ClassVar[str] = "odm:Include"
    class_name: ClassVar[str] = "Include"
    class_model_uri: ClassVar[URIRef] = ODM.Include

    studyOID: Union[str, StudyOID] = None
    metaDataVersionOID: Union[str, MetaDataVersionOID] = None
    href: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyOID):
            self.MissingRequiredField("studyOID")
        if not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        if self._is_empty(self.metaDataVersionOID):
            self.MissingRequiredField("metaDataVersionOID")
        if not isinstance(self.metaDataVersionOID, MetaDataVersionOID):
            self.metaDataVersionOID = MetaDataVersionOID(self.metaDataVersionOID)

        if self.href is not None and not isinstance(self.href, URIorCURIE):
            self.href = URIorCURIE(self.href)

        super().__post_init__(**kwargs)


@dataclass
class Standards(YAMLRoot):
    """
    The Standards element provides a container for the list of Standard elements referenced in the MetaDataVersion for
    the Study..
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Standards
    class_class_curie: ClassVar[str] = "odm:Standards"
    class_name: ClassVar[str] = "Standards"
    class_model_uri: ClassVar[URIRef] = ODM.Standards

    standard: Optional[Union[Dict[Union[str, StandardOID], Union[dict, "Standard"]], List[Union[dict, "Standard"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="standard", slot_type=Standard, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Standard(YAMLRoot):
    """
    The Standard element describes each standard used within the MetaDataVersion element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Standard
    class_class_curie: ClassVar[str] = "odm:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = ODM.Standard

    OID: Union[str, StandardOID] = None
    name: Union[str, "StandardName"] = None
    type: Union[str, "StandardType"] = None
    version: str = None
    status: str = None
    publishingSet: Optional[Union[str, "StandardPublishingSet"]] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StandardOID):
            self.OID = StandardOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, StandardName):
            self.name = StandardName(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, StandardType):
            self.type = StandardType(self.type)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, str):
            self.status = str(self.status)

        if self.publishingSet is not None and not isinstance(self.publishingSet, StandardPublishingSet):
            self.publishingSet = StandardPublishingSet(self.publishingSet)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        super().__post_init__(**kwargs)


@dataclass
class AnnotatedCRF(YAMLRoot):
    """
    An Annotated Case Report Form (CRF) is a Portable File Format (PDF) document that provides the mapping of data
    collection fields to the variables or discrete variable values contained within the datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.AnnotatedCRF
    class_class_curie: ClassVar[str] = "odm:AnnotatedCRF"
    class_name: ClassVar[str] = "AnnotatedCRF"
    class_model_uri: ClassVar[URIRef] = ODM.AnnotatedCRF

    documentRef: Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="documentRef", slot_type=DocumentRef, key_name="leafID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class SupplementalDoc(YAMLRoot):
    """
    Supplemental data definitions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SupplementalDoc
    class_class_curie: ClassVar[str] = "odm:SupplementalDoc"
    class_name: ClassVar[str] = "SupplementalDoc"
    class_model_uri: ClassVar[URIRef] = ODM.SupplementalDoc

    documentRef: Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="documentRef", slot_type=DocumentRef, key_name="leafID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class ValueListDef(YAMLRoot):
    """
    The following table specifies the XML structure for valuelist metadata. The ValueListDef element contains ItemRef
    elements that reference ItemDef elements that provide the value-level metadata details
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ValueListDef
    class_class_curie: ClassVar[str] = "odm:ValueListDef"
    class_name: ClassVar[str] = "ValueListDef"
    class_model_uri: ClassVar[URIRef] = ODM.ValueListDef

    OID: Union[str, ValueListDefOID] = None
    description: Optional[Union[dict, Description]] = None
    itemRef: Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ValueListDefOID):
            self.OID = ValueListDefOID(self.OID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.itemRef, list):
            self.itemRef = [self.itemRef] if self.itemRef is not None else []
        self.itemRef = [v if isinstance(v, ItemRef) else ItemRef(**as_dict(v)) for v in self.itemRef]

        super().__post_init__(**kwargs)


@dataclass
class WhereClauseRef(YAMLRoot):
    """
    The WhereClauseRef references the WhereClauseDef element that describes the conditions under which the variable
    values are defined by the referenced ItemDef.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.WhereClauseRef
    class_class_curie: ClassVar[str] = "odm:WhereClauseRef"
    class_name: ClassVar[str] = "WhereClauseRef"
    class_model_uri: ClassVar[URIRef] = ODM.WhereClauseRef

    whereClauseOID: Union[str, WhereClauseDefOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.whereClauseOID):
            self.MissingRequiredField("whereClauseOID")
        if not isinstance(self.whereClauseOID, WhereClauseDefOID):
            self.whereClauseOID = WhereClauseDefOID(self.whereClauseOID)

        super().__post_init__(**kwargs)


@dataclass
class WhereClauseDef(YAMLRoot):
    """
    The WhereClauseDef element specifies a condition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.WhereClauseDef
    class_class_curie: ClassVar[str] = "odm:WhereClauseDef"
    class_name: ClassVar[str] = "WhereClauseDef"
    class_model_uri: ClassVar[URIRef] = ODM.WhereClauseDef

    OID: Union[str, WhereClauseDefOID] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    rangeCheck: Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, WhereClauseDefOID):
            self.OID = WhereClauseDefOID(self.OID)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if not isinstance(self.rangeCheck, list):
            self.rangeCheck = [self.rangeCheck] if self.rangeCheck is not None else []
        self.rangeCheck = [v if isinstance(v, RangeCheck) else RangeCheck(**as_dict(v)) for v in self.rangeCheck]

        super().__post_init__(**kwargs)


@dataclass
class StudyEventGroupRef(YAMLRoot):
    """
    This element references a StudyEventGroupDef as it occurs within a specific version of a study. The list of
    StudyEventGroupRefs identifies the types of study group events that are allowed to occur within the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEventGroupRef
    class_class_curie: ClassVar[str] = "odm:StudyEventGroupRef"
    class_name: ClassVar[str] = "StudyEventGroupRef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEventGroupRef

    studyEventGroupOID: Union[str, StudyEventGroupDefOID] = None
    mandatory: Union[str, "YesOrNo"] = None
    orderNumber: Optional[int] = None
    collectionExceptionConditionOID: Optional[Union[str, ConditionDefOID]] = None
    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyEventGroupOID):
            self.MissingRequiredField("studyEventGroupOID")
        if not isinstance(self.studyEventGroupOID, StudyEventGroupDefOID):
            self.studyEventGroupOID = StudyEventGroupDefOID(self.studyEventGroupOID)

        if self._is_empty(self.mandatory):
            self.MissingRequiredField("mandatory")
        if not isinstance(self.mandatory, YesOrNo):
            self.mandatory = YesOrNo(self.mandatory)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        if self.collectionExceptionConditionOID is not None and not isinstance(self.collectionExceptionConditionOID, ConditionDefOID):
            self.collectionExceptionConditionOID = ConditionDefOID(self.collectionExceptionConditionOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class StudyEventGroupDef(YAMLRoot):
    """
    StudyEventGroupDef is a study building block that groups a number of smaller building blocks, which can themselves
    be StudyEventGroups or StudyEvents. It thus allows nesting of building blocks.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEventGroupDef
    class_class_curie: ClassVar[str] = "odm:StudyEventGroupDef"
    class_name: ClassVar[str] = "StudyEventGroupDef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEventGroupDef

    OID: Union[str, StudyEventGroupDefOID] = None
    name: str = None
    armOID: Optional[Union[str, ArmOID]] = None
    epochOID: Optional[Union[str, EpochOID]] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    workflowRef: Optional[Union[dict, "WorkflowRef"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    studyEventGroupRef: Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]] = empty_list()
    studyEventRef: Optional[Union[Union[dict, "StudyEventRef"], List[Union[dict, "StudyEventRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEventGroupDefOID):
            self.OID = StudyEventGroupDefOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.armOID is not None and not isinstance(self.armOID, ArmOID):
            self.armOID = ArmOID(self.armOID)

        if self.epochOID is not None and not isinstance(self.epochOID, EpochOID):
            self.epochOID = EpochOID(self.epochOID)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.workflowRef is not None and not isinstance(self.workflowRef, WorkflowRef):
            self.workflowRef = WorkflowRef(**as_dict(self.workflowRef))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if not isinstance(self.studyEventGroupRef, list):
            self.studyEventGroupRef = [self.studyEventGroupRef] if self.studyEventGroupRef is not None else []
        self.studyEventGroupRef = [v if isinstance(v, StudyEventGroupRef) else StudyEventGroupRef(**as_dict(v)) for v in self.studyEventGroupRef]

        if not isinstance(self.studyEventRef, list):
            self.studyEventRef = [self.studyEventRef] if self.studyEventRef is not None else []
        self.studyEventRef = [v if isinstance(v, StudyEventRef) else StudyEventRef(**as_dict(v)) for v in self.studyEventRef]

        super().__post_init__(**kwargs)


@dataclass
class StudyEventRef(YAMLRoot):
    """
    This element references a StudyEventDef as it occurs within a specific version of a study. The list of
    StudyEventRefs identifies the types of study events that are allowed to occur within the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEventRef
    class_class_curie: ClassVar[str] = "odm:StudyEventRef"
    class_name: ClassVar[str] = "StudyEventRef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEventRef

    studyEventOID: Union[str, StudyEventDefOID] = None
    mandatory: Union[str, "YesOrNo"] = None
    orderNumber: Optional[int] = None
    collectionExceptionConditionOID: Optional[Union[str, ConditionDefOID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyEventOID):
            self.MissingRequiredField("studyEventOID")
        if not isinstance(self.studyEventOID, StudyEventDefOID):
            self.studyEventOID = StudyEventDefOID(self.studyEventOID)

        if self._is_empty(self.mandatory):
            self.MissingRequiredField("mandatory")
        if not isinstance(self.mandatory, YesOrNo):
            self.mandatory = YesOrNo(self.mandatory)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        if self.collectionExceptionConditionOID is not None and not isinstance(self.collectionExceptionConditionOID, ConditionDefOID):
            self.collectionExceptionConditionOID = ConditionDefOID(self.collectionExceptionConditionOID)

        super().__post_init__(**kwargs)


@dataclass
class StudyEventDef(YAMLRoot):
    """
    StudyEventDef represents the definition of an activity in a study where data is collected. For example, a study
    event may represent a set of item groups that represent data collection instruments to be completed for a subject
    during a visit in a study. The visit occurs as part of a study workflow, and the workflow is referenced in the
    study event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEventDef
    class_class_curie: ClassVar[str] = "odm:StudyEventDef"
    class_name: ClassVar[str] = "StudyEventDef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEventDef

    OID: Union[str, StudyEventDefOID] = None
    name: str = None
    repeating: Union[str, "YesOrNo"] = None
    type: Union[str, "EventType"] = None
    category: Optional[str] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    itemGroupRef: Optional[Union[Union[dict, "ItemGroupRef"], List[Union[dict, "ItemGroupRef"]]]] = empty_list()
    workflowRef: Optional[Union[dict, "WorkflowRef"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEventDefOID):
            self.OID = StudyEventDefOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.repeating):
            self.MissingRequiredField("repeating")
        if not isinstance(self.repeating, YesOrNo):
            self.repeating = YesOrNo(self.repeating)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, EventType):
            self.type = EventType(self.type)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.itemGroupRef, list):
            self.itemGroupRef = [self.itemGroupRef] if self.itemGroupRef is not None else []
        self.itemGroupRef = [v if isinstance(v, ItemGroupRef) else ItemGroupRef(**as_dict(v)) for v in self.itemGroupRef]

        if self.workflowRef is not None and not isinstance(self.workflowRef, WorkflowRef):
            self.workflowRef = WorkflowRef(**as_dict(self.workflowRef))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        super().__post_init__(**kwargs)


@dataclass
class ItemGroupRef(YAMLRoot):
    """
    ItemGroupRef references an ItemGroupDef as it occurs within a specific StudyEventDef or ItemGroupDef. The list of
    ItemGroupRefs identifies the types of item groups that are allowed to occur within this type of studyevent or
    (nested) item group. The ItemGroupRefs within a single StudyEventDef or ItemGroupDef must not have duplicate
    ItemGroupOID or OrderNumber attribute values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ItemGroupRef
    class_class_curie: ClassVar[str] = "odm:ItemGroupRef"
    class_name: ClassVar[str] = "ItemGroupRef"
    class_model_uri: ClassVar[URIRef] = ODM.ItemGroupRef

    itemGroupOID: Union[str, ItemGroupDefOID] = None
    mandatory: Union[str, "YesOrNo"] = None
    methodOID: Optional[Union[str, MethodDefOID]] = None
    orderNumber: Optional[int] = None
    collectionExceptionConditionOID: Optional[Union[str, ConditionDefOID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.itemGroupOID):
            self.MissingRequiredField("itemGroupOID")
        if not isinstance(self.itemGroupOID, ItemGroupDefOID):
            self.itemGroupOID = ItemGroupDefOID(self.itemGroupOID)

        if self._is_empty(self.mandatory):
            self.MissingRequiredField("mandatory")
        if not isinstance(self.mandatory, YesOrNo):
            self.mandatory = YesOrNo(self.mandatory)

        if self.methodOID is not None and not isinstance(self.methodOID, MethodDefOID):
            self.methodOID = MethodDefOID(self.methodOID)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        if self.collectionExceptionConditionOID is not None and not isinstance(self.collectionExceptionConditionOID, ConditionDefOID):
            self.collectionExceptionConditionOID = ConditionDefOID(self.collectionExceptionConditionOID)

        super().__post_init__(**kwargs)


@dataclass
class ItemGroupDef(YAMLRoot):
    """
    An ItemGroupDef describes a type of variable or field grouping that can occur within a study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ItemGroupDef
    class_class_curie: ClassVar[str] = "odm:ItemGroupDef"
    class_name: ClassVar[str] = "ItemGroupDef"
    class_model_uri: ClassVar[URIRef] = ODM.ItemGroupDef

    OID: Union[str, ItemGroupDefOID] = None
    name: str = None
    repeating: Union[str, "ItemGroupRepeatingType"] = None
    type: str = None
    repeatingLimit: Optional[int] = None
    isReferenceData: Optional[Union[str, "YesOrNo"]] = None
    structure: Optional[str] = None
    archiveLocationID: Optional[Union[str, LeafID]] = None
    datasetName: Optional[str] = None
    domain: Optional[str] = None
    purpose: Optional[str] = None
    standardOID: Optional[Union[str, StandardOID]] = None
    isNonStandard: Optional[Union[str, "YesOnly"]] = None
    hasNoData: Optional[Union[str, "YesOnly"]] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    itemGroupClass: Optional[Union[dict, "Class"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    workflowRef: Optional[Union[dict, "WorkflowRef"]] = None
    origin: Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]] = empty_list()
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()
    leaf: Optional[Union[str, LeafID]] = None
    itemGroupRef: Optional[Union[Union[dict, ItemGroupRef], List[Union[dict, ItemGroupRef]]]] = empty_list()
    itemRef: Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ItemGroupDefOID):
            self.OID = ItemGroupDefOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.repeating):
            self.MissingRequiredField("repeating")
        if not isinstance(self.repeating, ItemGroupRepeatingType):
            self.repeating = ItemGroupRepeatingType(self.repeating)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.repeatingLimit is not None and not isinstance(self.repeatingLimit, int):
            self.repeatingLimit = int(self.repeatingLimit)

        if self.isReferenceData is not None and not isinstance(self.isReferenceData, YesOrNo):
            self.isReferenceData = YesOrNo(self.isReferenceData)

        if self.structure is not None and not isinstance(self.structure, str):
            self.structure = str(self.structure)

        if self.archiveLocationID is not None and not isinstance(self.archiveLocationID, LeafID):
            self.archiveLocationID = LeafID(self.archiveLocationID)

        if self.datasetName is not None and not isinstance(self.datasetName, str):
            self.datasetName = str(self.datasetName)

        if self.domain is not None and not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if self.standardOID is not None and not isinstance(self.standardOID, StandardOID):
            self.standardOID = StandardOID(self.standardOID)

        if self.isNonStandard is not None and not isinstance(self.isNonStandard, YesOnly):
            self.isNonStandard = YesOnly(self.isNonStandard)

        if self.hasNoData is not None and not isinstance(self.hasNoData, YesOnly):
            self.hasNoData = YesOnly(self.hasNoData)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.itemGroupClass is not None and not isinstance(self.itemGroupClass, Class):
            self.itemGroupClass = Class(**as_dict(self.itemGroupClass))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if self.workflowRef is not None and not isinstance(self.workflowRef, WorkflowRef):
            self.workflowRef = WorkflowRef(**as_dict(self.workflowRef))

        if not isinstance(self.origin, list):
            self.origin = [self.origin] if self.origin is not None else []
        self.origin = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origin]

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        if self.leaf is not None and not isinstance(self.leaf, LeafID):
            self.leaf = LeafID(self.leaf)

        if not isinstance(self.itemGroupRef, list):
            self.itemGroupRef = [self.itemGroupRef] if self.itemGroupRef is not None else []
        self.itemGroupRef = [v if isinstance(v, ItemGroupRef) else ItemGroupRef(**as_dict(v)) for v in self.itemGroupRef]

        if not isinstance(self.itemRef, list):
            self.itemRef = [self.itemRef] if self.itemRef is not None else []
        self.itemRef = [v if isinstance(v, ItemRef) else ItemRef(**as_dict(v)) for v in self.itemRef]

        super().__post_init__(**kwargs)


@dataclass
class Class(YAMLRoot):
    """
    The Class element identifies which predefined Class within the model applies to the definition of the dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Class
    class_class_curie: ClassVar[str] = "odm:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = ODM.Class

    name: Union[str, "ItemGroupClass"] = None
    subClass: Optional[Union[Union[dict, "SubClass"], List[Union[dict, "SubClass"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ItemGroupClass):
            self.name = ItemGroupClass(self.name)

        if not isinstance(self.subClass, list):
            self.subClass = [self.subClass] if self.subClass is not None else []
        self.subClass = [v if isinstance(v, SubClass) else SubClass(**as_dict(v)) for v in self.subClass]

        super().__post_init__(**kwargs)


@dataclass
class SubClass(YAMLRoot):
    """
    This element contains SubClass definitions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SubClass
    class_class_curie: ClassVar[str] = "odm:SubClass"
    class_name: ClassVar[str] = "SubClass"
    class_model_uri: ClassVar[URIRef] = ODM.SubClass

    name: Union[str, "ItemGroupSubClass"] = None
    parentClass: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ItemGroupSubClass):
            self.name = ItemGroupSubClass(self.name)

        if self.parentClass is not None and not isinstance(self.parentClass, str):
            self.parentClass = str(self.parentClass)

        super().__post_init__(**kwargs)


@dataclass
class ItemRef(YAMLRoot):
    """
    A reference to an ItemDef as it occurs within a specific ItemGroupDef. The list of ItemRefs identifies the types
    of items that are allowed to occur within this type of item group.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ItemRef
    class_class_curie: ClassVar[str] = "odm:ItemRef"
    class_name: ClassVar[str] = "ItemRef"
    class_model_uri: ClassVar[URIRef] = ODM.ItemRef

    itemOID: Union[str, ItemDefOID] = None
    mandatory: Union[str, "YesOrNo"] = None
    keySequence: Optional[int] = None
    isNonStandard: Optional[Union[str, "YesOnly"]] = None
    hasNoData: Optional[Union[str, "YesOnly"]] = None
    methodOID: Optional[Union[str, MethodDefOID]] = None
    unitsItemOID: Optional[Union[str, ItemDefOID]] = None
    repeat: Optional[Union[str, "YesOnly"]] = None
    other: Optional[Union[str, "YesOnly"]] = None
    role: Optional[str] = None
    roleCodeListOID: Optional[Union[str, CodeListOID]] = None
    core: Optional[str] = None
    preSpecifiedValue: Optional[str] = None
    orderNumber: Optional[int] = None
    collectionExceptionConditionOID: Optional[Union[str, ConditionDefOID]] = None
    origin: Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]] = empty_list()
    whereClauseRef: Optional[Union[Union[dict, WhereClauseRef], List[Union[dict, WhereClauseRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.itemOID):
            self.MissingRequiredField("itemOID")
        if not isinstance(self.itemOID, ItemDefOID):
            self.itemOID = ItemDefOID(self.itemOID)

        if self._is_empty(self.mandatory):
            self.MissingRequiredField("mandatory")
        if not isinstance(self.mandatory, YesOrNo):
            self.mandatory = YesOrNo(self.mandatory)

        if self.keySequence is not None and not isinstance(self.keySequence, int):
            self.keySequence = int(self.keySequence)

        if self.isNonStandard is not None and not isinstance(self.isNonStandard, YesOnly):
            self.isNonStandard = YesOnly(self.isNonStandard)

        if self.hasNoData is not None and not isinstance(self.hasNoData, YesOnly):
            self.hasNoData = YesOnly(self.hasNoData)

        if self.methodOID is not None and not isinstance(self.methodOID, MethodDefOID):
            self.methodOID = MethodDefOID(self.methodOID)

        if self.unitsItemOID is not None and not isinstance(self.unitsItemOID, ItemDefOID):
            self.unitsItemOID = ItemDefOID(self.unitsItemOID)

        if self.repeat is not None and not isinstance(self.repeat, YesOnly):
            self.repeat = YesOnly(self.repeat)

        if self.other is not None and not isinstance(self.other, YesOnly):
            self.other = YesOnly(self.other)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.roleCodeListOID is not None and not isinstance(self.roleCodeListOID, CodeListOID):
            self.roleCodeListOID = CodeListOID(self.roleCodeListOID)

        if self.core is not None and not isinstance(self.core, str):
            self.core = str(self.core)

        if self.preSpecifiedValue is not None and not isinstance(self.preSpecifiedValue, str):
            self.preSpecifiedValue = str(self.preSpecifiedValue)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        if self.collectionExceptionConditionOID is not None and not isinstance(self.collectionExceptionConditionOID, ConditionDefOID):
            self.collectionExceptionConditionOID = ConditionDefOID(self.collectionExceptionConditionOID)

        if not isinstance(self.origin, list):
            self.origin = [self.origin] if self.origin is not None else []
        self.origin = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origin]

        if not isinstance(self.whereClauseRef, list):
            self.whereClauseRef = [self.whereClauseRef] if self.whereClauseRef is not None else []
        self.whereClauseRef = [v if isinstance(v, WhereClauseRef) else WhereClauseRef(**as_dict(v)) for v in self.whereClauseRef]

        super().__post_init__(**kwargs)


@dataclass
class Origin(YAMLRoot):
    """
    Origin defines the source metadata, where applicable, for ODM ItemRefs or ItemGroupRefs. Origin as a child element
    replaces the Origin attribute in ODM v1.3 that exists for the ItemDef and ItemGroupDef elements.The Origin element
    is based on the def:Origin element in Define-XML v2.1 with the Trace-XML v1.0 extension.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Origin
    class_class_curie: ClassVar[str] = "odm:Origin"
    class_name: ClassVar[str] = "Origin"
    class_model_uri: ClassVar[URIRef] = ODM.Origin

    type: Union[str, "OriginType"] = None
    source: Optional[Union[str, "OriginSource"]] = None
    description: Optional[Union[dict, Description]] = None
    sourceItems: Optional[Union[dict, "SourceItems"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    documentRef: Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OriginType):
            self.type = OriginType(self.type)

        if self.source is not None and not isinstance(self.source, OriginSource):
            self.source = OriginSource(self.source)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.sourceItems is not None and not isinstance(self.sourceItems, SourceItems):
            self.sourceItems = SourceItems(**as_dict(self.sourceItems))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        self._normalize_inlined_as_list(slot_name="documentRef", slot_type=DocumentRef, key_name="leafID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class SourceItems(YAMLRoot):
    """
    Identifies source items as needed to support automated data capture and end-to-end traceability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SourceItems
    class_class_curie: ClassVar[str] = "odm:SourceItems"
    class_name: ClassVar[str] = "SourceItems"
    class_model_uri: ClassVar[URIRef] = ODM.SourceItems

    sourceItem: Optional[Union[Union[dict, "SourceItem"], List[Union[dict, "SourceItem"]]]] = empty_list()
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.sourceItem, list):
            self.sourceItem = [self.sourceItem] if self.sourceItem is not None else []
        self.sourceItem = [v if isinstance(v, SourceItem) else SourceItem(**as_dict(v)) for v in self.sourceItem]

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        super().__post_init__(**kwargs)


@dataclass
class SourceItem(YAMLRoot):
    """
    Provides the information needed to identify the source metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SourceItem
    class_class_curie: ClassVar[str] = "odm:SourceItem"
    class_name: ClassVar[str] = "SourceItem"
    class_model_uri: ClassVar[URIRef] = ODM.SourceItem

    itemOID: Optional[Union[str, ItemDefOID]] = None
    itemGroupOID: Optional[Union[str, ItemGroupDefOID]] = None
    metaDataVersionOID: Optional[Union[str, MetaDataVersionOID]] = None
    studyOID: Optional[Union[str, StudyOID]] = None
    leafID: Optional[Union[str, LeafID]] = None
    name: Optional[str] = None
    resource: Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]] = empty_list()
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.itemOID is not None and not isinstance(self.itemOID, ItemDefOID):
            self.itemOID = ItemDefOID(self.itemOID)

        if self.itemGroupOID is not None and not isinstance(self.itemGroupOID, ItemGroupDefOID):
            self.itemGroupOID = ItemGroupDefOID(self.itemGroupOID)

        if self.metaDataVersionOID is not None and not isinstance(self.metaDataVersionOID, MetaDataVersionOID):
            self.metaDataVersionOID = MetaDataVersionOID(self.metaDataVersionOID)

        if self.studyOID is not None and not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        if self.leafID is not None and not isinstance(self.leafID, LeafID):
            self.leafID = LeafID(self.leafID)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.resource, list):
            self.resource = [self.resource] if self.resource is not None else []
        self.resource = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.resource]

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        super().__post_init__(**kwargs)


@dataclass
class Resource(YAMLRoot):
    """
    Describes an external resource used as the source for the parent ItemGroup or Item.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Resource
    class_class_curie: ClassVar[str] = "odm:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = ODM.Resource

    type: str = None
    name: str = None
    attribute: Optional[str] = None
    label: Optional[str] = None
    selection: Optional[Union[Union[dict, "Selection"], List[Union[dict, "Selection"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.attribute is not None and not isinstance(self.attribute, str):
            self.attribute = str(self.attribute)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.selection, list):
            self.selection = [self.selection] if self.selection is not None else []
        self.selection = [v if isinstance(v, Selection) else Selection(**as_dict(v)) for v in self.selection]

        super().__post_init__(**kwargs)


@dataclass
class Selection(YAMLRoot):
    """
    Template for machine-readable/executable expression for retrieving the data or information from an external
    resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Selection
    class_class_curie: ClassVar[str] = "odm:Selection"
    class_name: ClassVar[str] = "Selection"
    class_model_uri: ClassVar[URIRef] = ODM.Selection

    path: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass
class ItemDef(YAMLRoot):
    """
    An ItemDef describes a type of item that can occur within a study. Item properties include name, datatype, range,
    or codelist restrictions, and several other properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ItemDef
    class_class_curie: ClassVar[str] = "odm:ItemDef"
    class_name: ClassVar[str] = "ItemDef"
    class_model_uri: ClassVar[URIRef] = ODM.ItemDef

    OID: Union[str, ItemDefOID] = None
    name: str = None
    dataType: Union[str, "DataType"] = None
    length: Optional[int] = None
    displayFormat: Optional[str] = None
    variableSet: Optional[str] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    definition: Optional[Union[dict, "Definition"]] = None
    question: Optional[Union[dict, "Question"]] = None
    prompt: Optional[Union[dict, "Prompt"]] = None
    cRFCompletionInstructions: Optional[Union[dict, "CRFCompletionInstructions"]] = None
    implementationNotes: Optional[Union[dict, "ImplementationNotes"]] = None
    cDISCNotes: Optional[Union[dict, "CDISCNotes"]] = None
    rangeCheck: Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]] = empty_list()
    codeListRef: Optional[Union[dict, "CodeListRef"]] = None
    valueListRef: Optional[Union[dict, "ValueListRef"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ItemDefOID):
            self.OID = ItemDefOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, DataType):
            self.dataType = DataType(self.dataType)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.displayFormat is not None and not isinstance(self.displayFormat, str):
            self.displayFormat = str(self.displayFormat)

        if self.variableSet is not None and not isinstance(self.variableSet, str):
            self.variableSet = str(self.variableSet)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.definition is not None and not isinstance(self.definition, Definition):
            self.definition = Definition(**as_dict(self.definition))

        if self.question is not None and not isinstance(self.question, Question):
            self.question = Question(**as_dict(self.question))

        if self.prompt is not None and not isinstance(self.prompt, Prompt):
            self.prompt = Prompt(**as_dict(self.prompt))

        if self.cRFCompletionInstructions is not None and not isinstance(self.cRFCompletionInstructions, CRFCompletionInstructions):
            self.cRFCompletionInstructions = CRFCompletionInstructions(**as_dict(self.cRFCompletionInstructions))

        if self.implementationNotes is not None and not isinstance(self.implementationNotes, ImplementationNotes):
            self.implementationNotes = ImplementationNotes(**as_dict(self.implementationNotes))

        if self.cDISCNotes is not None and not isinstance(self.cDISCNotes, CDISCNotes):
            self.cDISCNotes = CDISCNotes(**as_dict(self.cDISCNotes))

        if not isinstance(self.rangeCheck, list):
            self.rangeCheck = [self.rangeCheck] if self.rangeCheck is not None else []
        self.rangeCheck = [v if isinstance(v, RangeCheck) else RangeCheck(**as_dict(v)) for v in self.rangeCheck]

        if self.codeListRef is not None and not isinstance(self.codeListRef, CodeListRef):
            self.codeListRef = CodeListRef(**as_dict(self.codeListRef))

        if self.valueListRef is not None and not isinstance(self.valueListRef, ValueListRef):
            self.valueListRef = ValueListRef(**as_dict(self.valueListRef))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        super().__post_init__(**kwargs)


@dataclass
class Question(YAMLRoot):
    """
    A label shown to a human user when prompted to provide data for an item on paper or on a screen.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Question
    class_class_curie: ClassVar[str] = "odm:Question"
    class_name: ClassVar[str] = "Question"
    class_model_uri: ClassVar[URIRef] = ODM.Question

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class Definition(YAMLRoot):
    """
    Definition of the item.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Definition
    class_class_curie: ClassVar[str] = "odm:Definition"
    class_name: ClassVar[str] = "Definition"
    class_model_uri: ClassVar[URIRef] = ODM.Definition

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class Prompt(YAMLRoot):
    """
    A prompt text shown to a human user when prompted to provide data for an item on paper or on a screen. The Prompt
    is a short version of the question.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Prompt
    class_class_curie: ClassVar[str] = "odm:Prompt"
    class_name: ClassVar[str] = "Prompt"
    class_model_uri: ClassVar[URIRef] = ODM.Prompt

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class CRFCompletionInstructions(YAMLRoot):
    """
    Instructions for the clinical site on how to enter collected information on the CRF.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.CRFCompletionInstructions
    class_class_curie: ClassVar[str] = "odm:CRFCompletionInstructions"
    class_name: ClassVar[str] = "CRFCompletionInstructions"
    class_model_uri: ClassVar[URIRef] = ODM.CRFCompletionInstructions

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class ImplementationNotes(YAMLRoot):
    """
    Further information, such as rationale and implementation instructions, on how to implement the CRF data
    collection fields.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ImplementationNotes
    class_class_curie: ClassVar[str] = "odm:ImplementationNotes"
    class_name: ClassVar[str] = "ImplementationNotes"
    class_model_uri: ClassVar[URIRef] = ODM.ImplementationNotes

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class CDISCNotes(YAMLRoot):
    """
    Explanatory text for the variable.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.CDISCNotes
    class_class_curie: ClassVar[str] = "odm:CDISCNotes"
    class_name: ClassVar[str] = "CDISCNotes"
    class_model_uri: ClassVar[URIRef] = ODM.CDISCNotes

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class RangeCheck(YAMLRoot):
    """
    A RangeCheck defines a constraint on the value of the enclosing item. It represents an expression that evaluates
    to True when the ItemData value is valid or False when the ItemData value is invalid. The expression is specified
    using either Comparator and CheckValue or using FormalExpressions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.RangeCheck
    class_class_curie: ClassVar[str] = "odm:RangeCheck"
    class_name: ClassVar[str] = "RangeCheck"
    class_model_uri: ClassVar[URIRef] = ODM.RangeCheck

    comparator: Optional[Union[str, "Comparator"]] = None
    softHard: Optional[Union[str, "SoftOrHard"]] = None
    itemOID: Optional[Union[str, ItemDefOID]] = None
    errorMessage: Optional[Union[dict, "ErrorMessage"]] = None
    methodSignature: Optional[Union[dict, "MethodSignature"]] = None
    formalExpression: Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]] = empty_list()
    checkValue: Optional[Union[Union[dict, "CheckValue"], List[Union[dict, "CheckValue"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.comparator is not None and not isinstance(self.comparator, Comparator):
            self.comparator = Comparator(self.comparator)

        if self.softHard is not None and not isinstance(self.softHard, SoftOrHard):
            self.softHard = SoftOrHard(self.softHard)

        if self.itemOID is not None and not isinstance(self.itemOID, ItemDefOID):
            self.itemOID = ItemDefOID(self.itemOID)

        if self.errorMessage is not None and not isinstance(self.errorMessage, ErrorMessage):
            self.errorMessage = ErrorMessage(**as_dict(self.errorMessage))

        if self.methodSignature is not None and not isinstance(self.methodSignature, MethodSignature):
            self.methodSignature = MethodSignature(**as_dict(self.methodSignature))

        if not isinstance(self.formalExpression, list):
            self.formalExpression = [self.formalExpression] if self.formalExpression is not None else []
        self.formalExpression = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.formalExpression]

        if not isinstance(self.checkValue, list):
            self.checkValue = [self.checkValue] if self.checkValue is not None else []
        self.checkValue = [v if isinstance(v, CheckValue) else CheckValue(**as_dict(v)) for v in self.checkValue]

        super().__post_init__(**kwargs)


@dataclass
class CheckValue(YAMLRoot):
    """
    A comparison value used in a range check.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.CheckValue
    class_class_curie: ClassVar[str] = "odm:CheckValue"
    class_name: ClassVar[str] = "CheckValue"
    class_model_uri: ClassVar[URIRef] = ODM.CheckValue

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class ErrorMessage(YAMLRoot):
    """
    Error message provided to user when the range check fails.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ErrorMessage
    class_class_curie: ClassVar[str] = "odm:ErrorMessage"
    class_name: ClassVar[str] = "ErrorMessage"
    class_model_uri: ClassVar[URIRef] = ODM.ErrorMessage

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class CodeListRef(YAMLRoot):
    """
    A reference to a CodeList definition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.CodeListRef
    class_class_curie: ClassVar[str] = "odm:CodeListRef"
    class_name: ClassVar[str] = "CodeListRef"
    class_model_uri: ClassVar[URIRef] = ODM.CodeListRef

    codeListOID: Union[str, CodeListOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.codeListOID):
            self.MissingRequiredField("codeListOID")
        if not isinstance(self.codeListOID, CodeListOID):
            self.codeListOID = CodeListOID(self.codeListOID)

        super().__post_init__(**kwargs)


@dataclass
class ValueListRef(YAMLRoot):
    """
    The ValueListRef element is the OID of the ValueListDef that contains the valuelist definition associated with the
    variable. If value-level metadata is required for a variable, a ValueListRef element should be provided as a child
    element on the ItemDef for the variable definition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ValueListRef
    class_class_curie: ClassVar[str] = "odm:ValueListRef"
    class_name: ClassVar[str] = "ValueListRef"
    class_model_uri: ClassVar[URIRef] = ODM.ValueListRef

    valueListOID: Union[str, ValueListDefOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.valueListOID):
            self.MissingRequiredField("valueListOID")
        if not isinstance(self.valueListOID, ValueListDefOID):
            self.valueListOID = ValueListDefOID(self.valueListOID)

        super().__post_init__(**kwargs)


@dataclass
class CodeList(YAMLRoot):
    """
    Defines a discrete set of permitted values for an item, or provides a reference to a codelist or dictionary
    maintained by an external organization via the Coding element, or a combination of both. Examples provided under
    Coding.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.CodeList
    class_class_curie: ClassVar[str] = "odm:CodeList"
    class_name: ClassVar[str] = "CodeList"
    class_model_uri: ClassVar[URIRef] = ODM.CodeList

    OID: Union[str, CodeListOID] = None
    name: str = None
    dataType: Union[str, "CLDataType"] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    standardOID: Optional[Union[str, StandardOID]] = None
    isNonStandard: Optional[Union[str, "YesOnly"]] = None
    description: Optional[Union[dict, Description]] = None
    codeListItem: Optional[Union[Union[dict, "CodeListItem"], List[Union[dict, "CodeListItem"]]]] = empty_list()
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, CodeListOID):
            self.OID = CodeListOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, CLDataType):
            self.dataType = CLDataType(self.dataType)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.standardOID is not None and not isinstance(self.standardOID, StandardOID):
            self.standardOID = StandardOID(self.standardOID)

        if self.isNonStandard is not None and not isinstance(self.isNonStandard, YesOnly):
            self.isNonStandard = YesOnly(self.isNonStandard)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.codeListItem, list):
            self.codeListItem = [self.codeListItem] if self.codeListItem is not None else []
        self.codeListItem = [v if isinstance(v, CodeListItem) else CodeListItem(**as_dict(v)) for v in self.codeListItem]

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        super().__post_init__(**kwargs)


@dataclass
class CodeListItem(YAMLRoot):
    """
    Defines an individual member value of a codelist. It may include a display value in the child Decode element
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.CodeListItem
    class_class_curie: ClassVar[str] = "odm:CodeListItem"
    class_name: ClassVar[str] = "CodeListItem"
    class_model_uri: ClassVar[URIRef] = ODM.CodeListItem

    codedValue: str = None
    rank: Optional[Decimal] = None
    other: Optional[Union[str, "YesOnly"]] = None
    orderNumber: Optional[int] = None
    extendedValue: Optional[Union[str, "YesOnly"]] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    decode: Optional[Union[dict, "Decode"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.codedValue):
            self.MissingRequiredField("codedValue")
        if not isinstance(self.codedValue, str):
            self.codedValue = str(self.codedValue)

        if self.rank is not None and not isinstance(self.rank, Decimal):
            self.rank = Decimal(self.rank)

        if self.other is not None and not isinstance(self.other, YesOnly):
            self.other = YesOnly(self.other)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        if self.extendedValue is not None and not isinstance(self.extendedValue, YesOnly):
            self.extendedValue = YesOnly(self.extendedValue)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.decode is not None and not isinstance(self.decode, Decode):
            self.decode = Decode(**as_dict(self.decode))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        super().__post_init__(**kwargs)


@dataclass
class Decode(YAMLRoot):
    """
    The displayed value relating to the CodeListItem/@CodedValue. This is often a label corresponding to a short name
    or alpha-numeric code. The actual Decode text is provided in a TranslatedText element so that it can be provided
    in different languages on a case report form or tabular data summary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Decode
    class_class_curie: ClassVar[str] = "odm:Decode"
    class_name: ClassVar[str] = "Decode"
    class_model_uri: ClassVar[URIRef] = ODM.Decode

    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class MethodDef(YAMLRoot):
    """
    A MethodDef defines how a data value can be obtained from a collection of other data values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.MethodDef
    class_class_curie: ClassVar[str] = "odm:MethodDef"
    class_name: ClassVar[str] = "MethodDef"
    class_model_uri: ClassVar[URIRef] = ODM.MethodDef

    OID: Union[str, MethodDefOID] = None
    name: str = None
    type: Optional[Union[str, "MethodType"]] = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    methodSignature: Optional[Union[dict, "MethodSignature"]] = None
    formalExpression: Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]] = empty_list()
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()
    documentRef: Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, MethodDefOID):
            self.OID = MethodDefOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.type is not None and not isinstance(self.type, MethodType):
            self.type = MethodType(self.type)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.methodSignature is not None and not isinstance(self.methodSignature, MethodSignature):
            self.methodSignature = MethodSignature(**as_dict(self.methodSignature))

        if not isinstance(self.formalExpression, list):
            self.formalExpression = [self.formalExpression] if self.formalExpression is not None else []
        self.formalExpression = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.formalExpression]

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        self._normalize_inlined_as_list(slot_name="documentRef", slot_type=DocumentRef, key_name="leafID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MethodSignature(YAMLRoot):
    """
    A MethodSignature defines the parameters and return values for a method. The MethodSignature improves traceability
    while enhancing the ability for automation engines to execute a MethodDef's FormalExpression. Most Methods use one
    or more input parameters and return one or more values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.MethodSignature
    class_class_curie: ClassVar[str] = "odm:MethodSignature"
    class_name: ClassVar[str] = "MethodSignature"
    class_model_uri: ClassVar[URIRef] = ODM.MethodSignature

    parameter: Optional[Union[Union[dict, "Parameter"], List[Union[dict, "Parameter"]]]] = empty_list()
    returnValue: Optional[Union[Union[dict, "ReturnValue"], List[Union[dict, "ReturnValue"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.parameter, list):
            self.parameter = [self.parameter] if self.parameter is not None else []
        self.parameter = [v if isinstance(v, Parameter) else Parameter(**as_dict(v)) for v in self.parameter]

        if not isinstance(self.returnValue, list):
            self.returnValue = [self.returnValue] if self.returnValue is not None else []
        self.returnValue = [v if isinstance(v, ReturnValue) else ReturnValue(**as_dict(v)) for v in self.returnValue]

        super().__post_init__(**kwargs)


@dataclass
class Parameter(YAMLRoot):
    """
    The Parameter element represents a method parameter used as part of a MethodSignature in MethodDef, ConditionDef,
    or RangeCheck.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Parameter
    class_class_curie: ClassVar[str] = "odm:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = ODM.Parameter

    name: str = None
    dataType: Union[str, "DataType"] = None
    definition: Optional[str] = None
    orderNumber: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, DataType):
            self.dataType = DataType(self.dataType)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        super().__post_init__(**kwargs)


@dataclass
class ReturnValue(YAMLRoot):
    """
    The ReturnValue element represents a return value used as part of a MethodSignature in MethodDef, ConditionDef, or
    RangeCheck. A return value identifies values passed from the Method to the calling element. A ReturnValue may be
    computed by a FormalExpression.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ReturnValue
    class_class_curie: ClassVar[str] = "odm:ReturnValue"
    class_name: ClassVar[str] = "ReturnValue"
    class_model_uri: ClassVar[URIRef] = ODM.ReturnValue

    name: str = None
    dataType: Union[str, "DataType"] = None
    definition: Optional[str] = None
    orderNumber: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, DataType):
            self.dataType = DataType(self.dataType)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        super().__post_init__(**kwargs)


@dataclass
class ConditionDef(YAMLRoot):
    """
    A ConditionDef defines a boolean condition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ConditionDef
    class_class_curie: ClassVar[str] = "odm:ConditionDef"
    class_name: ClassVar[str] = "ConditionDef"
    class_model_uri: ClassVar[URIRef] = ODM.ConditionDef

    OID: Union[str, ConditionDefOID] = None
    name: str = None
    commentOID: Optional[Union[str, CommentDefOID]] = None
    description: Optional[Union[dict, Description]] = None
    methodSignature: Optional[Union[dict, MethodSignature]] = None
    formalExpression: Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]] = empty_list()
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ConditionDefOID):
            self.OID = ConditionDefOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.commentOID is not None and not isinstance(self.commentOID, CommentDefOID):
            self.commentOID = CommentDefOID(self.commentOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.methodSignature is not None and not isinstance(self.methodSignature, MethodSignature):
            self.methodSignature = MethodSignature(**as_dict(self.methodSignature))

        if not isinstance(self.formalExpression, list):
            self.formalExpression = [self.formalExpression] if self.formalExpression is not None else []
        self.formalExpression = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.formalExpression]

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        super().__post_init__(**kwargs)


@dataclass
class FormalExpression(YAMLRoot):
    """
    A FormalExpression used within a ConditionDef or a RangeCheck must evaluate to True or False. A FormalExpression
    referenced within a MethodDef having Type Imputation, Computation, or Transpose must evaluate to the correct
    DataType for an Item that may be imputed or computed using the Method. A FormalExpression gets parameter and
    return value definitions from the MethodSignature element. The data types in the MethodSignature parameters and
    return values must match the corresponding data types in the FormalExpression.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.FormalExpression
    class_class_curie: ClassVar[str] = "odm:FormalExpression"
    class_name: ClassVar[str] = "FormalExpression"
    class_model_uri: ClassVar[URIRef] = ODM.FormalExpression

    context: Optional[str] = None
    code: Optional[Union[dict, "Code"]] = None
    externalCodeLib: Optional[Union[dict, "ExternalCodeLib"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.code is not None and not isinstance(self.code, Code):
            self.code = Code(**as_dict(self.code))

        if self.externalCodeLib is not None and not isinstance(self.externalCodeLib, ExternalCodeLib):
            self.externalCodeLib = ExternalCodeLib(**as_dict(self.externalCodeLib))

        super().__post_init__(**kwargs)


@dataclass
class Code(YAMLRoot):
    """
    Contains the source code that represents a FormalExpression in a given Context. The source code must be
    executable, and the MethodSignature defines the input parameters and return values for the code.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Code
    class_class_curie: ClassVar[str] = "odm:Code"
    class_name: ClassVar[str] = "Code"
    class_model_uri: ClassVar[URIRef] = ODM.Code

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class ExternalCodeLib(YAMLRoot):
    """
    The ExternalCodeLib element references a FormalExpression in an external code library, such as a file or GitHub.
    The intention is to make it possible to reference existing code libraries where the code is maintained as well as
    making it simpler to include longer, more complex FormalExpressions. The Library attribute provides the name of
    the external library, whereas ref or href provides a reference to the repository that can be used to retrieve the
    code. The Method attribute provides the name of the method in the file referenced for cases where multiple methods
    are provided in the source code file. The Version element provides the version of the external FormalExpression
    code referenced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ExternalCodeLib
    class_class_curie: ClassVar[str] = "odm:ExternalCodeLib"
    class_name: ClassVar[str] = "ExternalCodeLib"
    class_model_uri: ClassVar[URIRef] = ODM.ExternalCodeLib

    library: str = None
    method: Optional[str] = None
    version: Optional[str] = None
    ref: Optional[str] = None
    href: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.library):
            self.MissingRequiredField("library")
        if not isinstance(self.library, str):
            self.library = str(self.library)

        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.ref is not None and not isinstance(self.ref, str):
            self.ref = str(self.ref)

        if self.href is not None and not isinstance(self.href, URIorCURIE):
            self.href = URIorCURIE(self.href)

        super().__post_init__(**kwargs)


@dataclass
class CommentDef(YAMLRoot):
    """
    The Comment element allows referencing short comments self-contained in the XML document or long comments normally
    included in external documents. For comments included in external documents, the reference could include specific
    pages of a document where the comments are included.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.CommentDef
    class_class_curie: ClassVar[str] = "odm:CommentDef"
    class_name: ClassVar[str] = "CommentDef"
    class_model_uri: ClassVar[URIRef] = ODM.CommentDef

    OID: Union[str, CommentDefOID] = None
    description: Optional[Union[dict, Description]] = None
    documentRef: Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, CommentDefOID):
            self.OID = CommentDefOID(self.OID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        self._normalize_inlined_as_list(slot_name="documentRef", slot_type=DocumentRef, key_name="leafID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Protocol(YAMLRoot):
    """
    The Protocol element lists the kinds of study events that can occur within a specific version of a study. All
    clinical data must occur within one of these study events.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Protocol
    class_class_curie: ClassVar[str] = "odm:Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = ODM.Protocol

    description: Optional[Union[dict, Description]] = None
    studySummary: Optional[Union[dict, "StudySummary"]] = None
    studyStructure: Optional[Union[dict, "StudyStructure"]] = None
    trialPhase: Optional[Union[dict, "TrialPhase"]] = None
    studyTimings: Optional[Union[dict, "StudyTimings"]] = None
    studyIndications: Optional[Union[dict, "StudyIndications"]] = None
    studyInterventions: Optional[Union[dict, "StudyInterventions"]] = None
    studyObjectives: Optional[Union[dict, "StudyObjectives"]] = None
    studyEndPoints: Optional[Union[dict, "StudyEndPoints"]] = None
    studyTargetPopulation: Optional[Union[str, StudyTargetPopulationOID]] = None
    studyEstimands: Optional[Union[dict, "StudyEstimands"]] = None
    inclusionExclusionCriteria: Optional[Union[dict, "InclusionExclusionCriteria"]] = None
    studyEventGroupRef: Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]] = empty_list()
    workflowRef: Optional[Union[dict, "WorkflowRef"]] = None
    alias: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.studySummary is not None and not isinstance(self.studySummary, StudySummary):
            self.studySummary = StudySummary(**as_dict(self.studySummary))

        if self.studyStructure is not None and not isinstance(self.studyStructure, StudyStructure):
            self.studyStructure = StudyStructure(**as_dict(self.studyStructure))

        if self.trialPhase is not None and not isinstance(self.trialPhase, TrialPhase):
            self.trialPhase = TrialPhase(**as_dict(self.trialPhase))

        if self.studyTimings is not None and not isinstance(self.studyTimings, StudyTimings):
            self.studyTimings = StudyTimings(**as_dict(self.studyTimings))

        if self.studyIndications is not None and not isinstance(self.studyIndications, StudyIndications):
            self.studyIndications = StudyIndications(**as_dict(self.studyIndications))

        if self.studyInterventions is not None and not isinstance(self.studyInterventions, StudyInterventions):
            self.studyInterventions = StudyInterventions(**as_dict(self.studyInterventions))

        if self.studyObjectives is not None and not isinstance(self.studyObjectives, StudyObjectives):
            self.studyObjectives = StudyObjectives(**as_dict(self.studyObjectives))

        if self.studyEndPoints is not None and not isinstance(self.studyEndPoints, StudyEndPoints):
            self.studyEndPoints = StudyEndPoints(**as_dict(self.studyEndPoints))

        if self.studyTargetPopulation is not None and not isinstance(self.studyTargetPopulation, StudyTargetPopulationOID):
            self.studyTargetPopulation = StudyTargetPopulationOID(self.studyTargetPopulation)

        if self.studyEstimands is not None and not isinstance(self.studyEstimands, StudyEstimands):
            self.studyEstimands = StudyEstimands(**as_dict(self.studyEstimands))

        if self.inclusionExclusionCriteria is not None and not isinstance(self.inclusionExclusionCriteria, InclusionExclusionCriteria):
            self.inclusionExclusionCriteria = InclusionExclusionCriteria(**as_dict(self.inclusionExclusionCriteria))

        if not isinstance(self.studyEventGroupRef, list):
            self.studyEventGroupRef = [self.studyEventGroupRef] if self.studyEventGroupRef is not None else []
        self.studyEventGroupRef = [v if isinstance(v, StudyEventGroupRef) else StudyEventGroupRef(**as_dict(v)) for v in self.studyEventGroupRef]

        if self.workflowRef is not None and not isinstance(self.workflowRef, WorkflowRef):
            self.workflowRef = WorkflowRef(**as_dict(self.workflowRef))

        if not isinstance(self.alias, list):
            self.alias = [self.alias] if self.alias is not None else []
        self.alias = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.alias]

        super().__post_init__(**kwargs)


@dataclass
class StudyStructure(YAMLRoot):
    """
    The StudyStructure element describes the general structure of a clinical study with arms, epochs, and workflows.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyStructure
    class_class_curie: ClassVar[str] = "odm:StudyStructure"
    class_name: ClassVar[str] = "StudyStructure"
    class_model_uri: ClassVar[URIRef] = ODM.StudyStructure

    description: Optional[Union[dict, Description]] = None
    arm: Optional[Union[Dict[Union[str, ArmOID], Union[dict, "Arm"]], List[Union[dict, "Arm"]]]] = empty_dict()
    epoch: Optional[Union[Dict[Union[str, EpochOID], Union[dict, "Epoch"]], List[Union[dict, "Epoch"]]]] = empty_dict()
    workflowRef: Optional[Union[dict, "WorkflowRef"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        self._normalize_inlined_as_list(slot_name="arm", slot_type=Arm, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="epoch", slot_type=Epoch, key_name="OID", keyed=True)

        if self.workflowRef is not None and not isinstance(self.workflowRef, WorkflowRef):
            self.workflowRef = WorkflowRef(**as_dict(self.workflowRef))

        super().__post_init__(**kwargs)


@dataclass
class TrialPhase(YAMLRoot):
    """
    The TrialPhase element designates the phase of the study in the clinical trial.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.TrialPhase
    class_class_curie: ClassVar[str] = "odm:TrialPhase"
    class_name: ClassVar[str] = "TrialPhase"
    class_model_uri: ClassVar[URIRef] = ODM.TrialPhase

    value: str = None
    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class StudyIndications(YAMLRoot):
    """
    StudyIndications is a container element for individual StudyIndication elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyIndications
    class_class_curie: ClassVar[str] = "odm:StudyIndications"
    class_name: ClassVar[str] = "StudyIndications"
    class_model_uri: ClassVar[URIRef] = ODM.StudyIndications

    studyIndication: Optional[Union[Dict[Union[str, StudyIndicationOID], Union[dict, "StudyIndication"]], List[Union[dict, "StudyIndication"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="studyIndication", slot_type=StudyIndication, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyIndication(YAMLRoot):
    """
    This element describes a study indication (e.g., condition, disease) for the clinical study. The human-readable
    description is provided in the Description element. The Coding element can be used to provide a machine-readable
    code for the indication (e.g., SNOMED-CT code 26929004 for "Alzheimer's disease").
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyIndication
    class_class_curie: ClassVar[str] = "odm:StudyIndication"
    class_name: ClassVar[str] = "StudyIndication"
    class_model_uri: ClassVar[URIRef] = ODM.StudyIndication

    OID: Union[str, StudyIndicationOID] = None
    description: Optional[Union[dict, Description]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyIndicationOID):
            self.OID = StudyIndicationOID(self.OID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        super().__post_init__(**kwargs)


@dataclass
class StudyInterventions(YAMLRoot):
    """
    The StudyInterventions element is a container element for individual StudyIntervention elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyInterventions
    class_class_curie: ClassVar[str] = "odm:StudyInterventions"
    class_name: ClassVar[str] = "StudyInterventions"
    class_model_uri: ClassVar[URIRef] = ODM.StudyInterventions

    studyIntervention: Optional[Union[Dict[Union[str, StudyInterventionOID], Union[dict, "StudyIntervention"]], List[Union[dict, "StudyIntervention"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="studyIntervention", slot_type=StudyIntervention, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyIntervention(YAMLRoot):
    """
    This element describes a study intervention (e.g., medication, treatment, therapy) for the clinical study. The
    human-readable description is provided in the Description element. The Coding element can be used to provide a
    machine-readable code for the indication (e.g., ATC M01AE01 code for "Ibuprofen" when used as a nonsteroidal
    anti-inflammatory drug).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyIntervention
    class_class_curie: ClassVar[str] = "odm:StudyIntervention"
    class_name: ClassVar[str] = "StudyIntervention"
    class_model_uri: ClassVar[URIRef] = ODM.StudyIntervention

    OID: Union[str, StudyInterventionOID] = None
    description: Optional[Union[dict, Description]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyInterventionOID):
            self.OID = StudyInterventionOID(self.OID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        super().__post_init__(**kwargs)


@dataclass
class StudyObjectives(YAMLRoot):
    """
    The StudyObjectives is a container element for individual StudyObjective elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyObjectives
    class_class_curie: ClassVar[str] = "odm:StudyObjectives"
    class_name: ClassVar[str] = "StudyObjectives"
    class_model_uri: ClassVar[URIRef] = ODM.StudyObjectives

    studyObjective: Optional[Union[Dict[Union[str, StudyObjectiveOID], Union[dict, "StudyObjective"]], List[Union[dict, "StudyObjective"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="studyObjective", slot_type=StudyObjective, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyObjective(YAMLRoot):
    """
    The reason for performing a study in terms of the scientific questions to be answered by the analysis of data
    collected during the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyObjective
    class_class_curie: ClassVar[str] = "odm:StudyObjective"
    class_name: ClassVar[str] = "StudyObjective"
    class_model_uri: ClassVar[URIRef] = ODM.StudyObjective

    OID: Union[str, StudyObjectiveOID] = None
    name: str = None
    level: Optional[Union[str, "StudyObjectiveLevel"]] = None
    description: Optional[Union[dict, Description]] = None
    studyEndPointRef: Optional[Union[Union[dict, "StudyEndPointRef"], List[Union[dict, "StudyEndPointRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyObjectiveOID):
            self.OID = StudyObjectiveOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.level is not None and not isinstance(self.level, StudyObjectiveLevel):
            self.level = StudyObjectiveLevel(self.level)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.studyEndPointRef, list):
            self.studyEndPointRef = [self.studyEndPointRef] if self.studyEndPointRef is not None else []
        self.studyEndPointRef = [v if isinstance(v, StudyEndPointRef) else StudyEndPointRef(**as_dict(v)) for v in self.studyEndPointRef]

        super().__post_init__(**kwargs)


@dataclass
class StudyEndPointRef(YAMLRoot):
    """
    A reference to a StudyEndPoint as it occurs within a specific StudyObjective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEndPointRef
    class_class_curie: ClassVar[str] = "odm:StudyEndPointRef"
    class_name: ClassVar[str] = "StudyEndPointRef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEndPointRef

    studyEndPointOID: Union[str, StudyEndPointOID] = None
    orderNumber: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyEndPointOID):
            self.MissingRequiredField("studyEndPointOID")
        if not isinstance(self.studyEndPointOID, StudyEndPointOID):
            self.studyEndPointOID = StudyEndPointOID(self.studyEndPointOID)

        if self.orderNumber is not None and not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        super().__post_init__(**kwargs)


@dataclass
class StudyEndPoints(YAMLRoot):
    """
    The StudyEndPoints element is a container element for individual StudyEndPoint elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEndPoints
    class_class_curie: ClassVar[str] = "odm:StudyEndPoints"
    class_name: ClassVar[str] = "StudyEndPoints"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEndPoints

    studyEndPoint: Optional[Union[Dict[Union[str, StudyEndPointOID], Union[dict, "StudyEndPoint"]], List[Union[dict, "StudyEndPoint"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="studyEndPoint", slot_type=StudyEndPoint, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyEndPoint(YAMLRoot):
    """
    A study end point reflects an outcome measure of interest that is statistically analyzed to address a particular
    research question for the study. It typically specifies the type of assessments made; the timing of those
    assessments; the assessment tools used; and other details, as applicable, such as how multiple assessments within
    an individual are to be combined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEndPoint
    class_class_curie: ClassVar[str] = "odm:StudyEndPoint"
    class_name: ClassVar[str] = "StudyEndPoint"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEndPoint

    OID: Union[str, StudyEndPointOID] = None
    name: str = None
    type: Optional[Union[str, "StudyEndPointType"]] = None
    level: Optional[Union[str, "StudyEstimandLevel"]] = None
    description: Optional[Union[dict, Description]] = None
    formalExpression: Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEndPointOID):
            self.OID = StudyEndPointOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.type is not None and not isinstance(self.type, StudyEndPointType):
            self.type = StudyEndPointType(self.type)

        if self.level is not None and not isinstance(self.level, StudyEstimandLevel):
            self.level = StudyEstimandLevel(self.level)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.formalExpression, list):
            self.formalExpression = [self.formalExpression] if self.formalExpression is not None else []
        self.formalExpression = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.formalExpression]

        super().__post_init__(**kwargs)


@dataclass
class StudyTargetPopulation(YAMLRoot):
    """
    The StudyTargetPopulation describes the population targeted for the clinical study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyTargetPopulation
    class_class_curie: ClassVar[str] = "odm:StudyTargetPopulation"
    class_name: ClassVar[str] = "StudyTargetPopulation"
    class_model_uri: ClassVar[URIRef] = ODM.StudyTargetPopulation

    OID: Union[str, StudyTargetPopulationOID] = None
    name: str = None
    description: Optional[Union[dict, Description]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    formalExpression: Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyTargetPopulationOID):
            self.OID = StudyTargetPopulationOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if not isinstance(self.formalExpression, list):
            self.formalExpression = [self.formalExpression] if self.formalExpression is not None else []
        self.formalExpression = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.formalExpression]

        super().__post_init__(**kwargs)


@dataclass
class StudyEstimands(YAMLRoot):
    """
    StudyEstimands is a container element for individual StudyEstimand elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEstimands
    class_class_curie: ClassVar[str] = "odm:StudyEstimands"
    class_name: ClassVar[str] = "StudyEstimands"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEstimands

    studyEstimand: Optional[Union[Dict[Union[str, StudyEstimandOID], Union[dict, "StudyEstimand"]], List[Union[dict, "StudyEstimand"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="studyEstimand", slot_type=StudyEstimand, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyEstimand(YAMLRoot):
    """
    A precise description of the treatment effect reflecting the clinical question posed by a given clinical trial
    objective. It summarises at a population level what the outcomes would be in the same patients under different
    treatment conditions being compared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEstimand
    class_class_curie: ClassVar[str] = "odm:StudyEstimand"
    class_name: ClassVar[str] = "StudyEstimand"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEstimand

    OID: Union[str, StudyEstimandOID] = None
    name: str = None
    level: Optional[Union[str, "StudyEstimandLevel"]] = None
    description: Optional[Union[dict, Description]] = None
    studyTargetPopulationRef: Optional[Union[dict, "StudyTargetPopulationRef"]] = None
    studyInterventionRef: Optional[Union[dict, "StudyInterventionRef"]] = None
    studyEndPointRef: Optional[Union[dict, StudyEndPointRef]] = None
    intercurrentEvent: Optional[Union[Union[dict, "IntercurrentEvent"], List[Union[dict, "IntercurrentEvent"]]]] = empty_list()
    summaryMeasure: Optional[Union[dict, "SummaryMeasure"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEstimandOID):
            self.OID = StudyEstimandOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.level is not None and not isinstance(self.level, StudyEstimandLevel):
            self.level = StudyEstimandLevel(self.level)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.studyTargetPopulationRef is not None and not isinstance(self.studyTargetPopulationRef, StudyTargetPopulationRef):
            self.studyTargetPopulationRef = StudyTargetPopulationRef(**as_dict(self.studyTargetPopulationRef))

        if self.studyInterventionRef is not None and not isinstance(self.studyInterventionRef, StudyInterventionRef):
            self.studyInterventionRef = StudyInterventionRef(**as_dict(self.studyInterventionRef))

        if self.studyEndPointRef is not None and not isinstance(self.studyEndPointRef, StudyEndPointRef):
            self.studyEndPointRef = StudyEndPointRef(**as_dict(self.studyEndPointRef))

        if not isinstance(self.intercurrentEvent, list):
            self.intercurrentEvent = [self.intercurrentEvent] if self.intercurrentEvent is not None else []
        self.intercurrentEvent = [v if isinstance(v, IntercurrentEvent) else IntercurrentEvent(**as_dict(v)) for v in self.intercurrentEvent]

        if self.summaryMeasure is not None and not isinstance(self.summaryMeasure, SummaryMeasure):
            self.summaryMeasure = SummaryMeasure(**as_dict(self.summaryMeasure))

        super().__post_init__(**kwargs)


@dataclass
class InclusionExclusionCriteria(YAMLRoot):
    """
    The InclusionExclusionCriteria element can contain 2 lists of Criterion elements, represented by the 2 elements
    InclusionCriteria and ExclusionCriteria. Together, these criteria determine the eligibility of a subject for the
    study. The actual condition to be evaluated is contained in an ODM ConditionDef, which is referenced by each
    Criterion‟s ConditionOID attribute.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.InclusionExclusionCriteria
    class_class_curie: ClassVar[str] = "odm:InclusionExclusionCriteria"
    class_name: ClassVar[str] = "InclusionExclusionCriteria"
    class_model_uri: ClassVar[URIRef] = ODM.InclusionExclusionCriteria

    inclusionCriteria: Optional[Union[dict, "InclusionCriteria"]] = None
    exclusionCriteria: Optional[Union[dict, "ExclusionCriteria"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.inclusionCriteria is not None and not isinstance(self.inclusionCriteria, InclusionCriteria):
            self.inclusionCriteria = InclusionCriteria(**as_dict(self.inclusionCriteria))

        if self.exclusionCriteria is not None and not isinstance(self.exclusionCriteria, ExclusionCriteria):
            self.exclusionCriteria = ExclusionCriteria(**as_dict(self.exclusionCriteria))

        super().__post_init__(**kwargs)


@dataclass
class InclusionCriteria(YAMLRoot):
    """
    The InclusionCriteria is a container element for Criterion elements describing inclusion criteria for subjects in
    the study. When a list is provided, subjects must meet each of the criteria in the list in order to enroll in the
    study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.InclusionCriteria
    class_class_curie: ClassVar[str] = "odm:InclusionCriteria"
    class_name: ClassVar[str] = "InclusionCriteria"
    class_model_uri: ClassVar[URIRef] = ODM.InclusionCriteria

    criterion: Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="criterion", slot_type=Criterion, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class ExclusionCriteria(YAMLRoot):
    """
    The ExclusionCriteria is a container element for Criterion elements describing exclusion criteria for subjects in
    the study. When a list is provided, not meeting any of the criteria in the list may lead to exclusion of
    enrollment in the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ExclusionCriteria
    class_class_curie: ClassVar[str] = "odm:ExclusionCriteria"
    class_name: ClassVar[str] = "ExclusionCriteria"
    class_model_uri: ClassVar[URIRef] = ODM.ExclusionCriteria

    criterion: Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="criterion", slot_type=Criterion, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyTargetPopulationRef(YAMLRoot):
    """
    The StudyTargetPopulationRef references a StudyTargetPopulation to which the estimand applies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyTargetPopulationRef
    class_class_curie: ClassVar[str] = "odm:StudyTargetPopulationRef"
    class_name: ClassVar[str] = "StudyTargetPopulationRef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyTargetPopulationRef

    studyTargetPopulationOID: Union[str, StudyTargetPopulationOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyTargetPopulationOID):
            self.MissingRequiredField("studyTargetPopulationOID")
        if not isinstance(self.studyTargetPopulationOID, StudyTargetPopulationOID):
            self.studyTargetPopulationOID = StudyTargetPopulationOID(self.studyTargetPopulationOID)

        super().__post_init__(**kwargs)


@dataclass
class StudyInterventionRef(YAMLRoot):
    """
    The StudyInterventionRef references an intervention that is taken as the treatment for the estimand.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyInterventionRef
    class_class_curie: ClassVar[str] = "odm:StudyInterventionRef"
    class_name: ClassVar[str] = "StudyInterventionRef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyInterventionRef

    studyInterventionOID: Union[str, StudyInterventionOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyInterventionOID):
            self.MissingRequiredField("studyInterventionOID")
        if not isinstance(self.studyInterventionOID, StudyInterventionOID):
            self.studyInterventionOID = StudyInterventionOID(self.studyInterventionOID)

        super().__post_init__(**kwargs)


@dataclass
class IntercurrentEvent(YAMLRoot):
    """
    The IntercurrentEvent element describes an intercurrent event for an estimand (e.g., treatment discontinuation).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.IntercurrentEvent
    class_class_curie: ClassVar[str] = "odm:IntercurrentEvent"
    class_name: ClassVar[str] = "IntercurrentEvent"
    class_model_uri: ClassVar[URIRef] = ODM.IntercurrentEvent

    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class SummaryMeasure(YAMLRoot):
    """
    The SummaryMeasure element describes a summary measure for an estimand (e.g., proportion of patients with an
    improvement).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SummaryMeasure
    class_class_curie: ClassVar[str] = "odm:SummaryMeasure"
    class_name: ClassVar[str] = "SummaryMeasure"
    class_model_uri: ClassVar[URIRef] = ODM.SummaryMeasure

    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class Arm(YAMLRoot):
    """
    An Arm element provides the declaration of a study arm. Arms do not have any ordering relative to one another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Arm
    class_class_curie: ClassVar[str] = "odm:Arm"
    class_name: ClassVar[str] = "Arm"
    class_model_uri: ClassVar[URIRef] = ODM.Arm

    OID: Union[str, ArmOID] = None
    name: str = None
    description: Optional[Union[dict, Description]] = None
    workflowRef: Optional[Union[dict, "WorkflowRef"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ArmOID):
            self.OID = ArmOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.workflowRef is not None and not isinstance(self.workflowRef, WorkflowRef):
            self.workflowRef = WorkflowRef(**as_dict(self.workflowRef))

        super().__post_init__(**kwargs)


@dataclass
class Epoch(YAMLRoot):
    """
    The planned period of subjects' participation in the trial is divided into sequential epochs. Each epoch is a
    period of time that serves a purpose in the trial as a whole. Epochs cannot overlap. The sequence of the epoch in
    the study is provided by the SequenceNumber attribute, the first epoch in the study being assigned the sequence
    number 1. Sequence numbers are subsequent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Epoch
    class_class_curie: ClassVar[str] = "odm:Epoch"
    class_name: ClassVar[str] = "Epoch"
    class_model_uri: ClassVar[URIRef] = ODM.Epoch

    OID: Union[str, EpochOID] = None
    name: str = None
    sequenceNumber: int = None
    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, EpochOID):
            self.OID = EpochOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.sequenceNumber):
            self.MissingRequiredField("sequenceNumber")
        if not isinstance(self.sequenceNumber, int):
            self.sequenceNumber = int(self.sequenceNumber)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class WorkflowRef(YAMLRoot):
    """
    The WorkflowRef references a workflow definition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.WorkflowRef
    class_class_curie: ClassVar[str] = "odm:WorkflowRef"
    class_name: ClassVar[str] = "WorkflowRef"
    class_model_uri: ClassVar[URIRef] = ODM.WorkflowRef

    workflowOID: Union[str, WorkflowDefOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.workflowOID):
            self.MissingRequiredField("workflowOID")
        if not isinstance(self.workflowOID, WorkflowDefOID):
            self.workflowOID = WorkflowDefOID(self.workflowOID)

        super().__post_init__(**kwargs)


@dataclass
class StudySummary(YAMLRoot):
    """
    The StudyParameter element allows to provide a set of study design parameters such as anticipated number of
    subjects, minimum and maximum age of the participants, or planned number of arms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudySummary
    class_class_curie: ClassVar[str] = "odm:StudySummary"
    class_name: ClassVar[str] = "StudySummary"
    class_model_uri: ClassVar[URIRef] = ODM.StudySummary

    studyParameter: Optional[Union[Dict[Union[str, StudyParameterOID], Union[dict, "StudyParameter"]], List[Union[dict, "StudyParameter"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="studyParameter", slot_type=StudyParameter, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyParameter(YAMLRoot):
    """
    A StudyParameter defines a study design parameter for which the value or values are delivered in the
    ParameterValue child element or elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyParameter
    class_class_curie: ClassVar[str] = "odm:StudyParameter"
    class_name: ClassVar[str] = "StudyParameter"
    class_model_uri: ClassVar[URIRef] = ODM.StudyParameter

    OID: Union[str, StudyParameterOID] = None
    term: str = None
    shortName: Optional[str] = None
    parameterValue: Optional[Union[dict, "ParameterValue"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyParameterOID):
            self.OID = StudyParameterOID(self.OID)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, str):
            self.term = str(self.term)

        if self.shortName is not None and not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self.parameterValue is not None and not isinstance(self.parameterValue, ParameterValue):
            self.parameterValue = ParameterValue(**as_dict(self.parameterValue))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        super().__post_init__(**kwargs)


@dataclass
class ParameterValue(YAMLRoot):
    """
    This element contains the value of the study parameter as text content.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ParameterValue
    class_class_curie: ClassVar[str] = "odm:ParameterValue"
    class_name: ClassVar[str] = "ParameterValue"
    class_model_uri: ClassVar[URIRef] = ODM.ParameterValue

    value: str = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        super().__post_init__(**kwargs)


@dataclass
class StudyTimings(YAMLRoot):
    """
    The StudyTimings element is a container element for individual StudyTiming elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyTimings
    class_class_curie: ClassVar[str] = "odm:StudyTimings"
    class_name: ClassVar[str] = "StudyTimings"
    class_model_uri: ClassVar[URIRef] = ODM.StudyTimings

    studyTiming: Optional[Union[Dict[Union[str, StudyTimingOID], Union[dict, "StudyTiming"]], List[Union[dict, "StudyTiming"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="studyTiming", slot_type=StudyTiming, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class StudyTiming(YAMLRoot):
    """
    The StudyTiming element defines a timing constraint within the study, which can be an absolute timing constraint
    (e.g., start of the screening visit must be between 1 January 2022 and 31 December 2022), a relative timing
    constraint (e.g., visit 2 must be within 30 days after visit 1 with a window of +/- 1 week), a transition timing
    constraint (i.e., timing constraint on a transition within a defined workflow), or a duration timing constraint
    (e.g., the duration of visit 2 is planned to take hours with a window of 30 minutes).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyTiming
    class_class_curie: ClassVar[str] = "odm:StudyTiming"
    class_name: ClassVar[str] = "StudyTiming"
    class_model_uri: ClassVar[URIRef] = ODM.StudyTiming

    OID: Union[str, StudyTimingOID] = None
    name: str = None
    absoluteTimingConstraint: Optional[Union[Dict[Union[str, AbsoluteTimingConstraintOID], Union[dict, "AbsoluteTimingConstraint"]], List[Union[dict, "AbsoluteTimingConstraint"]]]] = empty_dict()
    relativeTimingConstraint: Optional[Union[Dict[Union[str, RelativeTimingConstraintOID], Union[dict, "RelativeTimingConstraint"]], List[Union[dict, "RelativeTimingConstraint"]]]] = empty_dict()
    transitionTimingConstraint: Optional[Union[Dict[Union[str, TransitionTimingConstraintOID], Union[dict, "TransitionTimingConstraint"]], List[Union[dict, "TransitionTimingConstraint"]]]] = empty_dict()
    durationTimingConstraint: Optional[Union[Dict[Union[str, DurationTimingConstraintOID], Union[dict, "DurationTimingConstraint"]], List[Union[dict, "DurationTimingConstraint"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyTimingOID):
            self.OID = StudyTimingOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="absoluteTimingConstraint", slot_type=AbsoluteTimingConstraint, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="relativeTimingConstraint", slot_type=RelativeTimingConstraint, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="transitionTimingConstraint", slot_type=TransitionTimingConstraint, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="durationTimingConstraint", slot_type=DurationTimingConstraint, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class TransitionTimingConstraint(YAMLRoot):
    """
    The TransitionTimingConstraint element defines a timing constraint on a transition between structural elements as
    defined in a workflow. As such, it is a non-blocking constraint. This means that the transition is set on hold as
    long as the timing condition is not fulfilled, and is executed as soon as the timing condition is fulfilled.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.TransitionTimingConstraint
    class_class_curie: ClassVar[str] = "odm:TransitionTimingConstraint"
    class_name: ClassVar[str] = "TransitionTimingConstraint"
    class_model_uri: ClassVar[URIRef] = ODM.TransitionTimingConstraint

    OID: Union[str, TransitionTimingConstraintOID] = None
    name: str = None
    transitionOID: Union[str, TransitionOID] = None
    timepointTarget: str = None
    methodOID: Optional[Union[str, MethodDefOID]] = None
    type: Optional[Union[str, "RelativeTimingConstraintType"]] = None
    timepointPreWindow: Optional[str] = None
    timepointPostWindow: Optional[str] = None
    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, TransitionTimingConstraintOID):
            self.OID = TransitionTimingConstraintOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.transitionOID):
            self.MissingRequiredField("transitionOID")
        if not isinstance(self.transitionOID, TransitionOID):
            self.transitionOID = TransitionOID(self.transitionOID)

        if self._is_empty(self.timepointTarget):
            self.MissingRequiredField("timepointTarget")
        if not isinstance(self.timepointTarget, str):
            self.timepointTarget = str(self.timepointTarget)

        if self.methodOID is not None and not isinstance(self.methodOID, MethodDefOID):
            self.methodOID = MethodDefOID(self.methodOID)

        if self.type is not None and not isinstance(self.type, RelativeTimingConstraintType):
            self.type = RelativeTimingConstraintType(self.type)

        if self.timepointPreWindow is not None and not isinstance(self.timepointPreWindow, str):
            self.timepointPreWindow = str(self.timepointPreWindow)

        if self.timepointPostWindow is not None and not isinstance(self.timepointPostWindow, str):
            self.timepointPostWindow = str(self.timepointPostWindow)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class AbsoluteTimingConstraint(YAMLRoot):
    """
    The element AbsoluteTimingConstraint is used to specify when an activity, represented by either a StudyEventGroup
    or StudyEvent, can take place.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.AbsoluteTimingConstraint
    class_class_curie: ClassVar[str] = "odm:AbsoluteTimingConstraint"
    class_name: ClassVar[str] = "AbsoluteTimingConstraint"
    class_model_uri: ClassVar[URIRef] = ODM.AbsoluteTimingConstraint

    OID: Union[str, AbsoluteTimingConstraintOID] = None
    name: str = None
    timepointTarget: str = None
    studyEventGroupOID: Optional[Union[str, StudyEventGroupDefOID]] = None
    studyEventOID: Optional[Union[str, StudyEventDefOID]] = None
    timepointPreWindow: Optional[str] = None
    timepointPostWindow: Optional[str] = None
    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, AbsoluteTimingConstraintOID):
            self.OID = AbsoluteTimingConstraintOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.timepointTarget):
            self.MissingRequiredField("timepointTarget")
        if not isinstance(self.timepointTarget, str):
            self.timepointTarget = str(self.timepointTarget)

        if self.studyEventGroupOID is not None and not isinstance(self.studyEventGroupOID, StudyEventGroupDefOID):
            self.studyEventGroupOID = StudyEventGroupDefOID(self.studyEventGroupOID)

        if self.studyEventOID is not None and not isinstance(self.studyEventOID, StudyEventDefOID):
            self.studyEventOID = StudyEventDefOID(self.studyEventOID)

        if self.timepointPreWindow is not None and not isinstance(self.timepointPreWindow, str):
            self.timepointPreWindow = str(self.timepointPreWindow)

        if self.timepointPostWindow is not None and not isinstance(self.timepointPostWindow, str):
            self.timepointPostWindow = str(self.timepointPostWindow)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class RelativeTimingConstraint(YAMLRoot):
    """
    The RelativeTimingConstraint element describes a relative timing constraint between 2 activities or groups of
    activities, represented by StudyEventGroups, StudyEvents, ItemGroups, or Items.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.RelativeTimingConstraint
    class_class_curie: ClassVar[str] = "odm:RelativeTimingConstraint"
    class_name: ClassVar[str] = "RelativeTimingConstraint"
    class_model_uri: ClassVar[URIRef] = ODM.RelativeTimingConstraint

    OID: Union[str, RelativeTimingConstraintOID] = None
    name: str = None
    timepointRelativeTarget: str = None
    predecessorOID: Optional[str] = None
    successorOID: Optional[str] = None
    type: Optional[Union[str, "RelativeTimingConstraintType"]] = None
    timepointPreWindow: Optional[str] = None
    timepointPostWindow: Optional[str] = None
    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, RelativeTimingConstraintOID):
            self.OID = RelativeTimingConstraintOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.timepointRelativeTarget):
            self.MissingRequiredField("timepointRelativeTarget")
        if not isinstance(self.timepointRelativeTarget, str):
            self.timepointRelativeTarget = str(self.timepointRelativeTarget)

        if self.predecessorOID is not None and not isinstance(self.predecessorOID, str):
            self.predecessorOID = str(self.predecessorOID)

        if self.successorOID is not None and not isinstance(self.successorOID, str):
            self.successorOID = str(self.successorOID)

        if self.type is not None and not isinstance(self.type, RelativeTimingConstraintType):
            self.type = RelativeTimingConstraintType(self.type)

        if self.timepointPreWindow is not None and not isinstance(self.timepointPreWindow, str):
            self.timepointPreWindow = str(self.timepointPreWindow)

        if self.timepointPostWindow is not None and not isinstance(self.timepointPostWindow, str):
            self.timepointPostWindow = str(self.timepointPostWindow)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class DurationTimingConstraint(YAMLRoot):
    """
    The DurationTimingConstraint constrains the duration of an activity represented by a study, epoch,
    StudyEventGroupDef, StudyEventDef, ItemGroupDef, or ItemDef. It is used to constrain the duration of the visit,
    activity, or any other structural element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.DurationTimingConstraint
    class_class_curie: ClassVar[str] = "odm:DurationTimingConstraint"
    class_name: ClassVar[str] = "DurationTimingConstraint"
    class_model_uri: ClassVar[URIRef] = ODM.DurationTimingConstraint

    OID: Union[str, DurationTimingConstraintOID] = None
    name: str = None
    structuralElementOID: str = None
    durationTarget: str = None
    durationPreWindow: Optional[str] = None
    durationPostWindow: Optional[str] = None
    description: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, DurationTimingConstraintOID):
            self.OID = DurationTimingConstraintOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.structuralElementOID):
            self.MissingRequiredField("structuralElementOID")
        if not isinstance(self.structuralElementOID, str):
            self.structuralElementOID = str(self.structuralElementOID)

        if self._is_empty(self.durationTarget):
            self.MissingRequiredField("durationTarget")
        if not isinstance(self.durationTarget, str):
            self.durationTarget = str(self.durationTarget)

        if self.durationPreWindow is not None and not isinstance(self.durationPreWindow, str):
            self.durationPreWindow = str(self.durationPreWindow)

        if self.durationPostWindow is not None and not isinstance(self.durationPostWindow, str):
            self.durationPostWindow = str(self.durationPostWindow)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        super().__post_init__(**kwargs)


@dataclass
class WorkflowDef(YAMLRoot):
    """
    A WorkflowDef defines an automated workflow for a study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.WorkflowDef
    class_class_curie: ClassVar[str] = "odm:WorkflowDef"
    class_name: ClassVar[str] = "WorkflowDef"
    class_model_uri: ClassVar[URIRef] = ODM.WorkflowDef

    OID: Union[str, WorkflowDefOID] = None
    name: str = None
    description: Optional[Union[dict, Description]] = None
    workflowStart: Optional[Union[dict, "WorkflowStart"]] = None
    workflowEnd: Optional[Union[Union[dict, "WorkflowEnd"], List[Union[dict, "WorkflowEnd"]]]] = empty_list()
    transition: Optional[Union[Dict[Union[str, TransitionOID], Union[dict, "Transition"]], List[Union[dict, "Transition"]]]] = empty_dict()
    branching: Optional[Union[Dict[Union[str, BranchingOID], Union[dict, "Branching"]], List[Union[dict, "Branching"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, WorkflowDefOID):
            self.OID = WorkflowDefOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if self.workflowStart is not None and not isinstance(self.workflowStart, WorkflowStart):
            self.workflowStart = WorkflowStart(**as_dict(self.workflowStart))

        if not isinstance(self.workflowEnd, list):
            self.workflowEnd = [self.workflowEnd] if self.workflowEnd is not None else []
        self.workflowEnd = [v if isinstance(v, WorkflowEnd) else WorkflowEnd(**as_dict(v)) for v in self.workflowEnd]

        self._normalize_inlined_as_list(slot_name="transition", slot_type=Transition, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="branching", slot_type=Branching, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class WorkflowStart(YAMLRoot):
    """
    WorkflowStart references a structural element that begins the automated workflow.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.WorkflowStart
    class_class_curie: ClassVar[str] = "odm:WorkflowStart"
    class_name: ClassVar[str] = "WorkflowStart"
    class_model_uri: ClassVar[URIRef] = ODM.WorkflowStart

    startOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.startOID):
            self.MissingRequiredField("startOID")
        if not isinstance(self.startOID, str):
            self.startOID = str(self.startOID)

        super().__post_init__(**kwargs)


@dataclass
class Transition(YAMLRoot):
    """
    A Transition defines a link between 2 structural elements in a workflow. When the execution of the transition is
    dependent upon a timing constraint that is either directly defined or calculated, a TransitionTimingConstraint
    must be defined, referencing the current Transition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Transition
    class_class_curie: ClassVar[str] = "odm:Transition"
    class_name: ClassVar[str] = "Transition"
    class_model_uri: ClassVar[URIRef] = ODM.Transition

    OID: Union[str, TransitionOID] = None
    name: str = None
    sourceOID: str = None
    targetOID: str = None
    startConditionOID: Optional[Union[str, ConditionDefOID]] = None
    endConditionOID: Optional[Union[str, ConditionDefOID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, TransitionOID):
            self.OID = TransitionOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.sourceOID):
            self.MissingRequiredField("sourceOID")
        if not isinstance(self.sourceOID, str):
            self.sourceOID = str(self.sourceOID)

        if self._is_empty(self.targetOID):
            self.MissingRequiredField("targetOID")
        if not isinstance(self.targetOID, str):
            self.targetOID = str(self.targetOID)

        if self.startConditionOID is not None and not isinstance(self.startConditionOID, ConditionDefOID):
            self.startConditionOID = ConditionDefOID(self.startConditionOID)

        if self.endConditionOID is not None and not isinstance(self.endConditionOID, ConditionDefOID):
            self.endConditionOID = ConditionDefOID(self.endConditionOID)

        super().__post_init__(**kwargs)


@dataclass
class Branching(YAMLRoot):
    """
    This element describes the branching in a workflow from a source (start) structural element to 2 or more target
    structural elements, over a Transition element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Branching
    class_class_curie: ClassVar[str] = "odm:Branching"
    class_name: ClassVar[str] = "Branching"
    class_model_uri: ClassVar[URIRef] = ODM.Branching

    OID: Union[str, BranchingOID] = None
    name: str = None
    type: Union[str, "BranchingType"] = None
    targetTransition: Optional[Union[Union[dict, "TargetTransition"], List[Union[dict, "TargetTransition"]]]] = empty_list()
    defaultTransition: Optional[Union[Union[dict, "DefaultTransition"], List[Union[dict, "DefaultTransition"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, BranchingOID):
            self.OID = BranchingOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, BranchingType):
            self.type = BranchingType(self.type)

        if not isinstance(self.targetTransition, list):
            self.targetTransition = [self.targetTransition] if self.targetTransition is not None else []
        self.targetTransition = [v if isinstance(v, TargetTransition) else TargetTransition(**as_dict(v)) for v in self.targetTransition]

        if not isinstance(self.defaultTransition, list):
            self.defaultTransition = [self.defaultTransition] if self.defaultTransition is not None else []
        self.defaultTransition = [v if isinstance(v, DefaultTransition) else DefaultTransition(**as_dict(v)) for v in self.defaultTransition]

        super().__post_init__(**kwargs)


@dataclass
class TargetTransition(YAMLRoot):
    """
    TargetTransition provides a reference to a Transition element that is the target of a branching.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.TargetTransition
    class_class_curie: ClassVar[str] = "odm:TargetTransition"
    class_name: ClassVar[str] = "TargetTransition"
    class_model_uri: ClassVar[URIRef] = ODM.TargetTransition

    targetTransitionOID: Union[str, TransitionOID] = None
    conditionOID: Optional[Union[str, ConditionDefOID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.targetTransitionOID):
            self.MissingRequiredField("targetTransitionOID")
        if not isinstance(self.targetTransitionOID, TransitionOID):
            self.targetTransitionOID = TransitionOID(self.targetTransitionOID)

        if self.conditionOID is not None and not isinstance(self.conditionOID, ConditionDefOID):
            self.conditionOID = ConditionDefOID(self.conditionOID)

        super().__post_init__(**kwargs)


@dataclass
class DefaultTransition(YAMLRoot):
    """
    The DefaultTransition references the Transition that needs to be executed when none of the TargetTransitions can
    be executed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.DefaultTransition
    class_class_curie: ClassVar[str] = "odm:DefaultTransition"
    class_name: ClassVar[str] = "DefaultTransition"
    class_model_uri: ClassVar[URIRef] = ODM.DefaultTransition

    targetTransitionOID: Union[str, TransitionOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.targetTransitionOID):
            self.MissingRequiredField("targetTransitionOID")
        if not isinstance(self.targetTransitionOID, TransitionOID):
            self.targetTransitionOID = TransitionOID(self.targetTransitionOID)

        super().__post_init__(**kwargs)


@dataclass
class WorkflowEnd(YAMLRoot):
    """
    A WorkflowEnd references a structural element with which the workflows ends.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.WorkflowEnd
    class_class_curie: ClassVar[str] = "odm:WorkflowEnd"
    class_name: ClassVar[str] = "WorkflowEnd"
    class_model_uri: ClassVar[URIRef] = ODM.WorkflowEnd

    endOID: str = None
    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.endOID):
            self.MissingRequiredField("endOID")
        if not isinstance(self.endOID, str):
            self.endOID = str(self.endOID)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Criterion(YAMLRoot):
    """
    The Criterion represents either an inclusion or an exclusion criterion, depending on the parent element (i.e.,
    InclusionCriteria, ExclusionCriteria).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Criterion
    class_class_curie: ClassVar[str] = "odm:Criterion"
    class_name: ClassVar[str] = "Criterion"
    class_model_uri: ClassVar[URIRef] = ODM.Criterion

    OID: Union[str, CriterionOID] = None
    name: str = None
    conditionOID: Union[str, ConditionDefOID] = None
    description: Optional[Union[dict, Description]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, CriterionOID):
            self.OID = CriterionOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.conditionOID):
            self.MissingRequiredField("conditionOID")
        if not isinstance(self.conditionOID, ConditionDefOID):
            self.conditionOID = ConditionDefOID(self.conditionOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        super().__post_init__(**kwargs)


@dataclass
class AdminData(YAMLRoot):
    """
    Administrative information about users, locations, organizations, and electronic signatures.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.AdminData
    class_class_curie: ClassVar[str] = "odm:AdminData"
    class_name: ClassVar[str] = "AdminData"
    class_model_uri: ClassVar[URIRef] = ODM.AdminData

    studyOID: Optional[Union[str, StudyOID]] = None
    user: Optional[Union[Dict[Union[str, UserOID], Union[dict, "User"]], List[Union[dict, "User"]]]] = empty_dict()
    organization: Optional[Union[Dict[Union[str, OrganizationOID], Union[dict, "Organization"]], List[Union[dict, "Organization"]]]] = empty_dict()
    location: Optional[Union[Dict[Union[str, LocationOID], Union[dict, "Location"]], List[Union[dict, "Location"]]]] = empty_dict()
    signatureDef: Optional[Union[Dict[Union[str, SignatureDefOID], Union[dict, "SignatureDef"]], List[Union[dict, "SignatureDef"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.studyOID is not None and not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        self._normalize_inlined_as_list(slot_name="user", slot_type=User, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="organization", slot_type=Organization, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="location", slot_type=Location, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="signatureDef", slot_type=SignatureDef, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class User(YAMLRoot):
    """
    Information about a specific user of a clinical data collection or data management system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.User
    class_class_curie: ClassVar[str] = "odm:User"
    class_name: ClassVar[str] = "User"
    class_model_uri: ClassVar[URIRef] = ODM.User

    OID: Union[str, UserOID] = None
    userType: Optional[Union[str, "UserType"]] = None
    organizationOID: Optional[Union[str, OrganizationOID]] = None
    locationOID: Optional[Union[str, LocationOID]] = None
    userName: Optional[Union[dict, "UserName"]] = None
    prefix: Optional[Union[dict, "Prefix"]] = None
    suffix: Optional[Union[dict, "Suffix"]] = None
    fullName: Optional[Union[dict, "FullName"]] = None
    givenName: Optional[Union[dict, "GivenName"]] = None
    familyName: Optional[Union[dict, "FamilyName"]] = None
    image: Optional[Union[dict, "Image"]] = None
    address: Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]] = empty_list()
    telecom: Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, UserOID):
            self.OID = UserOID(self.OID)

        if self.userType is not None and not isinstance(self.userType, UserType):
            self.userType = UserType(self.userType)

        if self.organizationOID is not None and not isinstance(self.organizationOID, OrganizationOID):
            self.organizationOID = OrganizationOID(self.organizationOID)

        if self.locationOID is not None and not isinstance(self.locationOID, LocationOID):
            self.locationOID = LocationOID(self.locationOID)

        if self.userName is not None and not isinstance(self.userName, UserName):
            self.userName = UserName(**as_dict(self.userName))

        if self.prefix is not None and not isinstance(self.prefix, Prefix):
            self.prefix = Prefix(**as_dict(self.prefix))

        if self.suffix is not None and not isinstance(self.suffix, Suffix):
            self.suffix = Suffix(**as_dict(self.suffix))

        if self.fullName is not None and not isinstance(self.fullName, FullName):
            self.fullName = FullName(**as_dict(self.fullName))

        if self.givenName is not None and not isinstance(self.givenName, GivenName):
            self.givenName = GivenName(**as_dict(self.givenName))

        if self.familyName is not None and not isinstance(self.familyName, FamilyName):
            self.familyName = FamilyName(**as_dict(self.familyName))

        if self.image is not None and not isinstance(self.image, Image):
            self.image = Image(**as_dict(self.image))

        if not isinstance(self.address, list):
            self.address = [self.address] if self.address is not None else []
        self.address = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.address]

        if not isinstance(self.telecom, list):
            self.telecom = [self.telecom] if self.telecom is not None else []
        self.telecom = [v if isinstance(v, Telecom) else Telecom(**as_dict(v)) for v in self.telecom]

        super().__post_init__(**kwargs)


@dataclass
class UserName(YAMLRoot):
    """
    The user's login identification in the sender's system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.UserName
    class_class_curie: ClassVar[str] = "odm:UserName"
    class_name: ClassVar[str] = "UserName"
    class_model_uri: ClassVar[URIRef] = ODM.UserName

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Prefix(YAMLRoot):
    """
    Title or other prefix. Maps to FHIR HumanName.prefix (https://www.hl7.org/fhir/datatypes.html#humanname).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Prefix
    class_class_curie: ClassVar[str] = "odm:Prefix"
    class_name: ClassVar[str] = "Prefix"
    class_model_uri: ClassVar[URIRef] = ODM.Prefix

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Suffix(YAMLRoot):
    """
    This element may include credentials, or suffixes (e.g., Jr., III).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Suffix
    class_class_curie: ClassVar[str] = "odm:Suffix"
    class_name: ClassVar[str] = "Suffix"
    class_model_uri: ClassVar[URIRef] = ODM.Suffix

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class FullName(YAMLRoot):
    """
    The user's full formal name. May be a combination of Prefix, GivenName, FamilyName & Suffix. Intended to be used
    for display.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.FullName
    class_class_curie: ClassVar[str] = "odm:FullName"
    class_name: ClassVar[str] = "FullName"
    class_model_uri: ClassVar[URIRef] = ODM.FullName

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class GivenName(YAMLRoot):
    """
    The user's initial given name or all given names.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.GivenName
    class_class_curie: ClassVar[str] = "odm:GivenName"
    class_name: ClassVar[str] = "GivenName"
    class_model_uri: ClassVar[URIRef] = ODM.GivenName

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class FamilyName(YAMLRoot):
    """
    The user's surname (family name).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.FamilyName
    class_class_curie: ClassVar[str] = "odm:FamilyName"
    class_name: ClassVar[str] = "FamilyName"
    class_model_uri: ClassVar[URIRef] = ODM.FamilyName

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Image(YAMLRoot):
    """
    A visual depiction of the user.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Image
    class_class_curie: ClassVar[str] = "odm:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = ODM.Image

    imageFileName: Optional[URIorCURIE] = None
    href: Optional[str] = None
    mimeType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.imageFileName is not None and not isinstance(self.imageFileName, URIorCURIE):
            self.imageFileName = URIorCURIE(self.imageFileName)

        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.mimeType is not None and not isinstance(self.mimeType, str):
            self.mimeType = str(self.mimeType)

        super().__post_init__(**kwargs)


@dataclass
class Organization(YAMLRoot):
    """
    An organization can reference a parent organization. Users may be associated with an Organization. An Organization
    may be associated with a Location. A User, Location, or Organization may have an address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Organization
    class_class_curie: ClassVar[str] = "odm:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = ODM.Organization

    OID: Union[str, OrganizationOID] = None
    name: str = None
    type: Union[str, "OrganizationType"] = None
    role: Optional[str] = None
    locationOID: Optional[Union[str, LocationOID]] = None
    partOfOrganizationOID: Optional[Union[str, OrganizationOID]] = None
    description: Optional[Union[dict, Description]] = None
    address: Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]] = empty_list()
    telecom: Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, OrganizationOID):
            self.OID = OrganizationOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OrganizationType):
            self.type = OrganizationType(self.type)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.locationOID is not None and not isinstance(self.locationOID, LocationOID):
            self.locationOID = LocationOID(self.locationOID)

        if self.partOfOrganizationOID is not None and not isinstance(self.partOfOrganizationOID, OrganizationOID):
            self.partOfOrganizationOID = OrganizationOID(self.partOfOrganizationOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.address, list):
            self.address = [self.address] if self.address is not None else []
        self.address = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.address]

        if not isinstance(self.telecom, list):
            self.telecom = [self.telecom] if self.telecom is not None else []
        self.telecom = [v if isinstance(v, Telecom) else Telecom(**as_dict(v)) for v in self.telecom]

        super().__post_init__(**kwargs)


@dataclass
class Location(YAMLRoot):
    """
    A physical location associated with data collection and/or treatment of subjects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Location
    class_class_curie: ClassVar[str] = "odm:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = ODM.Location

    OID: Union[str, LocationOID] = None
    name: str = None
    role: Optional[str] = None
    organizationOID: Optional[Union[str, OrganizationOID]] = None
    description: Optional[Union[dict, Description]] = None
    metaDataVersionRef: Optional[Union[Union[dict, "MetaDataVersionRef"], List[Union[dict, "MetaDataVersionRef"]]]] = empty_list()
    address: Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]] = empty_list()
    telecom: Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]] = empty_list()
    query: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, LocationOID):
            self.OID = LocationOID(self.OID)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.organizationOID is not None and not isinstance(self.organizationOID, OrganizationOID):
            self.organizationOID = OrganizationOID(self.organizationOID)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        if not isinstance(self.metaDataVersionRef, list):
            self.metaDataVersionRef = [self.metaDataVersionRef] if self.metaDataVersionRef is not None else []
        self.metaDataVersionRef = [v if isinstance(v, MetaDataVersionRef) else MetaDataVersionRef(**as_dict(v)) for v in self.metaDataVersionRef]

        if not isinstance(self.address, list):
            self.address = [self.address] if self.address is not None else []
        self.address = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.address]

        if not isinstance(self.telecom, list):
            self.telecom = [self.telecom] if self.telecom is not None else []
        self.telecom = [v if isinstance(v, Telecom) else Telecom(**as_dict(v)) for v in self.telecom]

        self._normalize_inlined_as_list(slot_name="query", slot_type=Query, key_name="OID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Address(YAMLRoot):
    """
    The postal address for a user, location, or organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Address
    class_class_curie: ClassVar[str] = "odm:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = ODM.Address

    streetName: Optional[Union[dict, "StreetName"]] = None
    houseNumber: Optional[Union[dict, "HouseNumber"]] = None
    city: Optional[Union[dict, "City"]] = None
    stateProv: Optional[Union[dict, "StateProv"]] = None
    country: Optional[Union[dict, "Country"]] = None
    postalCode: Optional[Union[dict, "PostalCode"]] = None
    geoPosition: Optional[Union[dict, "GeoPosition"]] = None
    otherText: Optional[Union[dict, "OtherText"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.streetName is not None and not isinstance(self.streetName, StreetName):
            self.streetName = StreetName(**as_dict(self.streetName))

        if self.houseNumber is not None and not isinstance(self.houseNumber, HouseNumber):
            self.houseNumber = HouseNumber(**as_dict(self.houseNumber))

        if self.city is not None and not isinstance(self.city, City):
            self.city = City(**as_dict(self.city))

        if self.stateProv is not None and not isinstance(self.stateProv, StateProv):
            self.stateProv = StateProv(**as_dict(self.stateProv))

        if self.country is not None and not isinstance(self.country, Country):
            self.country = Country(**as_dict(self.country))

        if self.postalCode is not None and not isinstance(self.postalCode, PostalCode):
            self.postalCode = PostalCode(**as_dict(self.postalCode))

        if self.geoPosition is not None and not isinstance(self.geoPosition, GeoPosition):
            self.geoPosition = GeoPosition(**as_dict(self.geoPosition))

        if self.otherText is not None and not isinstance(self.otherText, OtherText):
            self.otherText = OtherText(**as_dict(self.otherText))

        super().__post_init__(**kwargs)


@dataclass
class Telecom(YAMLRoot):
    """
    The telecommunication contacts points of a user, a location, or an organization. The Type attribute designates the
    type of contact.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Telecom
    class_class_curie: ClassVar[str] = "odm:Telecom"
    class_name: ClassVar[str] = "Telecom"
    class_model_uri: ClassVar[URIRef] = ODM.Telecom

    telecomType: Union[str, "TelecomTypeType"] = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.telecomType):
            self.MissingRequiredField("telecomType")
        if not isinstance(self.telecomType, TelecomTypeType):
            self.telecomType = TelecomTypeType(self.telecomType)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class StreetName(YAMLRoot):
    """
    The street name part of a user's postal address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StreetName
    class_class_curie: ClassVar[str] = "odm:StreetName"
    class_name: ClassVar[str] = "StreetName"
    class_model_uri: ClassVar[URIRef] = ODM.StreetName

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class HouseNumber(YAMLRoot):
    """
    The house number part of a user's postal address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.HouseNumber
    class_class_curie: ClassVar[str] = "odm:HouseNumber"
    class_name: ClassVar[str] = "HouseNumber"
    class_model_uri: ClassVar[URIRef] = ODM.HouseNumber

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class City(YAMLRoot):
    """
    The city name part of a user's postal address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.City
    class_class_curie: ClassVar[str] = "odm:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = ODM.City

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class StateProv(YAMLRoot):
    """
    The state or province name part of a user's postal address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StateProv
    class_class_curie: ClassVar[str] = "odm:StateProv"
    class_name: ClassVar[str] = "StateProv"
    class_model_uri: ClassVar[URIRef] = ODM.StateProv

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Country(YAMLRoot):
    """
    The country name part of a user's postal address. For CDISC SDTM or trial registry applications, this must be
    represented by an ISO 3166 3-letter or US-GENC country code (e.g., FRA for France, JPN for Japan).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Country
    class_class_curie: ClassVar[str] = "odm:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = ODM.Country

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class PostalCode(YAMLRoot):
    """
    The postal code part of a user's postal address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.PostalCode
    class_class_curie: ClassVar[str] = "odm:PostalCode"
    class_name: ClassVar[str] = "PostalCode"
    class_model_uri: ClassVar[URIRef] = ODM.PostalCode

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class GeoPosition(YAMLRoot):
    """
    The geographical position using the World Geodetic System WGS84.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.GeoPosition
    class_class_curie: ClassVar[str] = "odm:GeoPosition"
    class_name: ClassVar[str] = "GeoPosition"
    class_model_uri: ClassVar[URIRef] = ODM.GeoPosition

    longitude: Optional[Decimal] = None
    latitude: Optional[Decimal] = None
    altitude: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.longitude is not None and not isinstance(self.longitude, Decimal):
            self.longitude = Decimal(self.longitude)

        if self.latitude is not None and not isinstance(self.latitude, Decimal):
            self.latitude = Decimal(self.latitude)

        if self.altitude is not None and not isinstance(self.altitude, Decimal):
            self.altitude = Decimal(self.altitude)

        super().__post_init__(**kwargs)


@dataclass
class OtherText(YAMLRoot):
    """
    Any other text needed as part of a user's postal address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.OtherText
    class_class_curie: ClassVar[str] = "odm:OtherText"
    class_name: ClassVar[str] = "OtherText"
    class_model_uri: ClassVar[URIRef] = ODM.OtherText

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class MetaDataVersionRef(YAMLRoot):
    """
    A reference to a MetaDataVersion used at the containing Location. The EffectiveDate reflects the possibility that
    the metadata may change over the course of the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.MetaDataVersionRef
    class_class_curie: ClassVar[str] = "odm:MetaDataVersionRef"
    class_name: ClassVar[str] = "MetaDataVersionRef"
    class_model_uri: ClassVar[URIRef] = ODM.MetaDataVersionRef

    studyOID: Union[str, StudyOID] = None
    metaDataVersionOID: Union[str, MetaDataVersionOID] = None
    effectiveDate: Union[str, XSDDate] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyOID):
            self.MissingRequiredField("studyOID")
        if not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        if self._is_empty(self.metaDataVersionOID):
            self.MissingRequiredField("metaDataVersionOID")
        if not isinstance(self.metaDataVersionOID, MetaDataVersionOID):
            self.metaDataVersionOID = MetaDataVersionOID(self.metaDataVersionOID)

        if self._is_empty(self.effectiveDate):
            self.MissingRequiredField("effectiveDate")
        if not isinstance(self.effectiveDate, XSDDate):
            self.effectiveDate = XSDDate(self.effectiveDate)

        super().__post_init__(**kwargs)


@dataclass
class SignatureDef(YAMLRoot):
    """
    Provides Metadata for signatures included in the /ODM/ClinicalData.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SignatureDef
    class_class_curie: ClassVar[str] = "odm:SignatureDef"
    class_name: ClassVar[str] = "SignatureDef"
    class_model_uri: ClassVar[URIRef] = ODM.SignatureDef

    OID: Union[str, SignatureDefOID] = None
    methodology: Optional[Union[str, "SignMethod"]] = None
    meaning: Optional[Union[dict, "Meaning"]] = None
    legalReason: Optional[Union[dict, "LegalReason"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, SignatureDefOID):
            self.OID = SignatureDefOID(self.OID)

        if self.methodology is not None and not isinstance(self.methodology, SignMethod):
            self.methodology = SignMethod(self.methodology)

        if self.meaning is not None and not isinstance(self.meaning, Meaning):
            self.meaning = Meaning(**as_dict(self.meaning))

        if self.legalReason is not None and not isinstance(self.legalReason, LegalReason):
            self.legalReason = LegalReason(**as_dict(self.legalReason))

        super().__post_init__(**kwargs)


@dataclass
class Meaning(YAMLRoot):
    """
    A short name or description for this signature. It should reflect the context of the signature and/or the text
    that appears when the signature is applied in the user interface.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Meaning
    class_class_curie: ClassVar[str] = "odm:Meaning"
    class_name: ClassVar[str] = "Meaning"
    class_model_uri: ClassVar[URIRef] = ODM.Meaning

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class LegalReason(YAMLRoot):
    """
    The responsibility statement associated with a signature (e.g., "The signer accepts responsibility for the
    accuracy of this data.").
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.LegalReason
    class_class_curie: ClassVar[str] = "odm:LegalReason"
    class_name: ClassVar[str] = "LegalReason"
    class_model_uri: ClassVar[URIRef] = ODM.LegalReason

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class ReferenceData(YAMLRoot):
    """
    Reference data provides information on how to interpret clinical data. For example, reference data might include
    lab normal ranges. For a study that uses CDISC standards, reference data might include SDTM Trial Design datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ReferenceData
    class_class_curie: ClassVar[str] = "odm:ReferenceData"
    class_name: ClassVar[str] = "ReferenceData"
    class_model_uri: ClassVar[URIRef] = ODM.ReferenceData

    studyOID: Union[str, StudyOID] = None
    metaDataVersionOID: Union[str, MetaDataVersionOID] = None
    itemGroupData: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    auditRecord: Optional[Union[dict, "AuditRecord"]] = None
    signature: Optional[Union[str, SignatureID]] = None
    annotation: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyOID):
            self.MissingRequiredField("studyOID")
        if not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        if self._is_empty(self.metaDataVersionOID):
            self.MissingRequiredField("metaDataVersionOID")
        if not isinstance(self.metaDataVersionOID, MetaDataVersionOID):
            self.metaDataVersionOID = MetaDataVersionOID(self.metaDataVersionOID)

        if not isinstance(self.itemGroupData, list):
            self.itemGroupData = [self.itemGroupData] if self.itemGroupData is not None else []
        self.itemGroupData = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.itemGroupData]

        if self.auditRecord is not None and not isinstance(self.auditRecord, AuditRecord):
            self.auditRecord = AuditRecord(**as_dict(self.auditRecord))

        if self.signature is not None and not isinstance(self.signature, SignatureID):
            self.signature = SignatureID(self.signature)

        if self.annotation is not None and not isinstance(self.annotation, AnnotationID):
            self.annotation = AnnotationID(self.annotation)

        super().__post_init__(**kwargs)


@dataclass
class ClinicalData(YAMLRoot):
    """
    Clinical data for 1 or more subjects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ClinicalData
    class_class_curie: ClassVar[str] = "odm:ClinicalData"
    class_name: ClassVar[str] = "ClinicalData"
    class_model_uri: ClassVar[URIRef] = ODM.ClinicalData

    studyOID: Union[str, StudyOID] = None
    metaDataVersionOID: Union[str, MetaDataVersionOID] = None
    subjectData: Optional[Union[Union[dict, "SubjectData"], List[Union[dict, "SubjectData"]]]] = empty_list()
    itemGroupData: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    query: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    auditRecord: Optional[Union[dict, "AuditRecord"]] = None
    signature: Optional[Union[str, SignatureID]] = None
    annotation: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyOID):
            self.MissingRequiredField("studyOID")
        if not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        if self._is_empty(self.metaDataVersionOID):
            self.MissingRequiredField("metaDataVersionOID")
        if not isinstance(self.metaDataVersionOID, MetaDataVersionOID):
            self.metaDataVersionOID = MetaDataVersionOID(self.metaDataVersionOID)

        if not isinstance(self.subjectData, list):
            self.subjectData = [self.subjectData] if self.subjectData is not None else []
        self.subjectData = [v if isinstance(v, SubjectData) else SubjectData(**as_dict(v)) for v in self.subjectData]

        if not isinstance(self.itemGroupData, list):
            self.itemGroupData = [self.itemGroupData] if self.itemGroupData is not None else []
        self.itemGroupData = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.itemGroupData]

        self._normalize_inlined_as_list(slot_name="query", slot_type=Query, key_name="OID", keyed=True)

        if self.auditRecord is not None and not isinstance(self.auditRecord, AuditRecord):
            self.auditRecord = AuditRecord(**as_dict(self.auditRecord))

        if self.signature is not None and not isinstance(self.signature, SignatureID):
            self.signature = SignatureID(self.signature)

        if self.annotation is not None and not isinstance(self.annotation, AnnotationID):
            self.annotation = AnnotationID(self.annotation)

        super().__post_init__(**kwargs)


@dataclass
class SubjectData(YAMLRoot):
    """
    Clinical data for a single subject.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SubjectData
    class_class_curie: ClassVar[str] = "odm:SubjectData"
    class_name: ClassVar[str] = "SubjectData"
    class_model_uri: ClassVar[URIRef] = ODM.SubjectData

    subjectKey: str = None
    transactionType: Optional[Union[str, "TransactionType"]] = None
    investigatorRef: Optional[Union[dict, "InvestigatorRef"]] = None
    siteRef: Optional[Union[dict, "SiteRef"]] = None
    studyEventData: Optional[Union[Union[dict, "StudyEventData"], List[Union[dict, "StudyEventData"]]]] = empty_list()
    query: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    auditRecord: Optional[Union[dict, "AuditRecord"]] = None
    signature: Optional[Union[str, SignatureID]] = None
    annotation: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subjectKey):
            self.MissingRequiredField("subjectKey")
        if not isinstance(self.subjectKey, str):
            self.subjectKey = str(self.subjectKey)

        if self.transactionType is not None and not isinstance(self.transactionType, TransactionType):
            self.transactionType = TransactionType(self.transactionType)

        if self.investigatorRef is not None and not isinstance(self.investigatorRef, InvestigatorRef):
            self.investigatorRef = InvestigatorRef(**as_dict(self.investigatorRef))

        if self.siteRef is not None and not isinstance(self.siteRef, SiteRef):
            self.siteRef = SiteRef(**as_dict(self.siteRef))

        if not isinstance(self.studyEventData, list):
            self.studyEventData = [self.studyEventData] if self.studyEventData is not None else []
        self.studyEventData = [v if isinstance(v, StudyEventData) else StudyEventData(**as_dict(v)) for v in self.studyEventData]

        self._normalize_inlined_as_list(slot_name="query", slot_type=Query, key_name="OID", keyed=True)

        if self.auditRecord is not None and not isinstance(self.auditRecord, AuditRecord):
            self.auditRecord = AuditRecord(**as_dict(self.auditRecord))

        if self.signature is not None and not isinstance(self.signature, SignatureID):
            self.signature = SignatureID(self.signature)

        if self.annotation is not None and not isinstance(self.annotation, AnnotationID):
            self.annotation = AnnotationID(self.annotation)

        super().__post_init__(**kwargs)


@dataclass
class SiteRef(YAMLRoot):
    """
    Provides a reference to the site that the SubjectData record is associated with in the source system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SiteRef
    class_class_curie: ClassVar[str] = "odm:SiteRef"
    class_name: ClassVar[str] = "SiteRef"
    class_model_uri: ClassVar[URIRef] = ODM.SiteRef

    locationOID: Union[str, LocationOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.locationOID):
            self.MissingRequiredField("locationOID")
        if not isinstance(self.locationOID, LocationOID):
            self.locationOID = LocationOID(self.locationOID)

        super().__post_init__(**kwargs)


@dataclass
class InvestigatorRef(YAMLRoot):
    """
    Provides a reference to the user who created the SubjectData record in the source system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.InvestigatorRef
    class_class_curie: ClassVar[str] = "odm:InvestigatorRef"
    class_name: ClassVar[str] = "InvestigatorRef"
    class_model_uri: ClassVar[URIRef] = ODM.InvestigatorRef

    userOID: Union[str, UserOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.userOID):
            self.MissingRequiredField("userOID")
        if not isinstance(self.userOID, UserOID):
            self.userOID = UserOID(self.userOID)

        super().__post_init__(**kwargs)


@dataclass
class StudyEventData(YAMLRoot):
    """
    Clinical data for a study event (visit). The model supports repeating study events (e.g., when the same set of
    information is collected for a series of patient visits).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEventData
    class_class_curie: ClassVar[str] = "odm:StudyEventData"
    class_name: ClassVar[str] = "StudyEventData"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEventData

    studyEventOID: Union[str, StudyEventDefOID] = None
    studyEventRepeatKey: Optional[str] = None
    transactionType: Optional[Union[str, "TransactionType"]] = None
    itemGroupData: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    query: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    auditRecord: Optional[Union[dict, "AuditRecord"]] = None
    signature: Optional[Union[str, SignatureID]] = None
    annotation: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyEventOID):
            self.MissingRequiredField("studyEventOID")
        if not isinstance(self.studyEventOID, StudyEventDefOID):
            self.studyEventOID = StudyEventDefOID(self.studyEventOID)

        if self.studyEventRepeatKey is not None and not isinstance(self.studyEventRepeatKey, str):
            self.studyEventRepeatKey = str(self.studyEventRepeatKey)

        if self.transactionType is not None and not isinstance(self.transactionType, TransactionType):
            self.transactionType = TransactionType(self.transactionType)

        if not isinstance(self.itemGroupData, list):
            self.itemGroupData = [self.itemGroupData] if self.itemGroupData is not None else []
        self.itemGroupData = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.itemGroupData]

        self._normalize_inlined_as_list(slot_name="query", slot_type=Query, key_name="OID", keyed=True)

        if self.auditRecord is not None and not isinstance(self.auditRecord, AuditRecord):
            self.auditRecord = AuditRecord(**as_dict(self.auditRecord))

        if self.signature is not None and not isinstance(self.signature, SignatureID):
            self.signature = SignatureID(self.signature)

        if self.annotation is not None and not isinstance(self.annotation, AnnotationID):
            self.annotation = AnnotationID(self.annotation)

        super().__post_init__(**kwargs)


@dataclass
class ItemGroupData(YAMLRoot):
    """
    Clinical data corresponding to an ItemGroupRef defined in the active MetaDataVersion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ItemGroupData
    class_class_curie: ClassVar[str] = "odm:ItemGroupData"
    class_name: ClassVar[str] = "ItemGroupData"
    class_model_uri: ClassVar[URIRef] = ODM.ItemGroupData

    itemGroupOID: Union[str, ItemGroupDefOID] = None
    itemGroupRepeatKey: Optional[str] = None
    transactionType: Optional[Union[str, "TransactionType"]] = None
    itemGroupDataSeq: Optional[int] = None
    query: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    itemGroupData: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    itemData: Optional[Union[Union[dict, "ItemData"], List[Union[dict, "ItemData"]]]] = empty_list()
    auditRecord: Optional[Union[dict, "AuditRecord"]] = None
    signature: Optional[Union[str, SignatureID]] = None
    annotation: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.itemGroupOID):
            self.MissingRequiredField("itemGroupOID")
        if not isinstance(self.itemGroupOID, ItemGroupDefOID):
            self.itemGroupOID = ItemGroupDefOID(self.itemGroupOID)

        if self.itemGroupRepeatKey is not None and not isinstance(self.itemGroupRepeatKey, str):
            self.itemGroupRepeatKey = str(self.itemGroupRepeatKey)

        if self.transactionType is not None and not isinstance(self.transactionType, TransactionType):
            self.transactionType = TransactionType(self.transactionType)

        if self.itemGroupDataSeq is not None and not isinstance(self.itemGroupDataSeq, int):
            self.itemGroupDataSeq = int(self.itemGroupDataSeq)

        self._normalize_inlined_as_list(slot_name="query", slot_type=Query, key_name="OID", keyed=True)

        if not isinstance(self.itemGroupData, list):
            self.itemGroupData = [self.itemGroupData] if self.itemGroupData is not None else []
        self.itemGroupData = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.itemGroupData]

        if not isinstance(self.itemData, list):
            self.itemData = [self.itemData] if self.itemData is not None else []
        self.itemData = [v if isinstance(v, ItemData) else ItemData(**as_dict(v)) for v in self.itemData]

        if self.auditRecord is not None and not isinstance(self.auditRecord, AuditRecord):
            self.auditRecord = AuditRecord(**as_dict(self.auditRecord))

        if self.signature is not None and not isinstance(self.signature, SignatureID):
            self.signature = SignatureID(self.signature)

        if self.annotation is not None and not isinstance(self.annotation, AnnotationID):
            self.annotation = AnnotationID(self.annotation)

        super().__post_init__(**kwargs)


@dataclass
class ItemData(YAMLRoot):
    """
    The ItemData element is used for transmission of the clinical data for an item. The model does not support
    repeating items within a single item group.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ItemData
    class_class_curie: ClassVar[str] = "odm:ItemData"
    class_name: ClassVar[str] = "ItemData"
    class_model_uri: ClassVar[URIRef] = ODM.ItemData

    itemOID: Union[str, ItemDefOID] = None
    transactionType: Optional[Union[str, "TransactionType"]] = None
    isNull: Optional[Union[str, "YesOnly"]] = None
    value: Optional[Union[Union[dict, "Value"], List[Union[dict, "Value"]]]] = empty_list()
    query: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    auditRecord: Optional[Union[dict, "AuditRecord"]] = None
    signature: Optional[Union[str, SignatureID]] = None
    annotation: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.itemOID):
            self.MissingRequiredField("itemOID")
        if not isinstance(self.itemOID, ItemDefOID):
            self.itemOID = ItemDefOID(self.itemOID)

        if self.transactionType is not None and not isinstance(self.transactionType, TransactionType):
            self.transactionType = TransactionType(self.transactionType)

        if self.isNull is not None and not isinstance(self.isNull, YesOnly):
            self.isNull = YesOnly(self.isNull)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [v if isinstance(v, Value) else Value(**as_dict(v)) for v in self.value]

        self._normalize_inlined_as_list(slot_name="query", slot_type=Query, key_name="OID", keyed=True)

        if self.auditRecord is not None and not isinstance(self.auditRecord, AuditRecord):
            self.auditRecord = AuditRecord(**as_dict(self.auditRecord))

        if self.signature is not None and not isinstance(self.signature, SignatureID):
            self.signature = SignatureID(self.signature)

        if self.annotation is not None and not isinstance(self.annotation, AnnotationID):
            self.annotation = AnnotationID(self.annotation)

        super().__post_init__(**kwargs)


@dataclass
class AuditRecord(YAMLRoot):
    """
    An AuditRecord carries information pertaining to the creation, deletion, or modification of clinical data. This
    information includes who performed that action, and where, when, and why that action was performed.AuditRecord
    information describes a change to clinical data, but is not itself clinical data. The value of some clinical data
    can always be changed by a subsequent transaction, but history cannot be changed, only added to.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.AuditRecord
    class_class_curie: ClassVar[str] = "odm:AuditRecord"
    class_name: ClassVar[str] = "AuditRecord"
    class_model_uri: ClassVar[URIRef] = ODM.AuditRecord

    editPoint: Optional[Union[str, "EditPointType"]] = None
    usedMethod: Optional[Union[str, "YesOrNo"]] = None
    userRef: Optional[Union[dict, "UserRef"]] = None
    locationRef: Optional[Union[dict, "LocationRef"]] = None
    dateTimeStamp: Optional[Union[dict, "DateTimeStamp"]] = None
    reasonForChange: Optional[Union[dict, "ReasonForChange"]] = None
    sourceID: Optional[Union[dict, "SourceID"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.editPoint is not None and not isinstance(self.editPoint, EditPointType):
            self.editPoint = EditPointType(self.editPoint)

        if self.usedMethod is not None and not isinstance(self.usedMethod, YesOrNo):
            self.usedMethod = YesOrNo(self.usedMethod)

        if self.userRef is not None and not isinstance(self.userRef, UserRef):
            self.userRef = UserRef(**as_dict(self.userRef))

        if self.locationRef is not None and not isinstance(self.locationRef, LocationRef):
            self.locationRef = LocationRef(**as_dict(self.locationRef))

        if self.dateTimeStamp is not None and not isinstance(self.dateTimeStamp, DateTimeStamp):
            self.dateTimeStamp = DateTimeStamp(**as_dict(self.dateTimeStamp))

        if self.reasonForChange is not None and not isinstance(self.reasonForChange, ReasonForChange):
            self.reasonForChange = ReasonForChange(**as_dict(self.reasonForChange))

        if self.sourceID is not None and not isinstance(self.sourceID, SourceID):
            self.sourceID = SourceID(**as_dict(self.sourceID))

        super().__post_init__(**kwargs)


@dataclass
class UserRef(YAMLRoot):
    """
    A reference to information about a specific user of a clinical data collection or data management system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.UserRef
    class_class_curie: ClassVar[str] = "odm:UserRef"
    class_name: ClassVar[str] = "UserRef"
    class_model_uri: ClassVar[URIRef] = ODM.UserRef

    userOID: Union[str, UserOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.userOID):
            self.MissingRequiredField("userOID")
        if not isinstance(self.userOID, UserOID):
            self.userOID = UserOID(self.userOID)

        super().__post_init__(**kwargs)


@dataclass
class LocationRef(YAMLRoot):
    """
    A reference to the user's physical location.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.LocationRef
    class_class_curie: ClassVar[str] = "odm:LocationRef"
    class_name: ClassVar[str] = "LocationRef"
    class_model_uri: ClassVar[URIRef] = ODM.LocationRef

    locationOID: Union[str, LocationOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.locationOID):
            self.MissingRequiredField("locationOID")
        if not isinstance(self.locationOID, LocationOID):
            self.locationOID = LocationOID(self.locationOID)

        super().__post_init__(**kwargs)


@dataclass
class DateTimeStamp(YAMLRoot):
    """
    Date and time when an action was performed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.DateTimeStamp
    class_class_curie: ClassVar[str] = "odm:DateTimeStamp"
    class_name: ClassVar[str] = "DateTimeStamp"
    class_model_uri: ClassVar[URIRef] = ODM.DateTimeStamp

    content: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, XSDDateTime):
            self.content = XSDDateTime(self.content)

        super().__post_init__(**kwargs)


@dataclass
class ReasonForChange(YAMLRoot):
    """
    A user-supplied reason for a data change.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ReasonForChange
    class_class_curie: ClassVar[str] = "odm:ReasonForChange"
    class_name: ClassVar[str] = "ReasonForChange"
    class_model_uri: ClassVar[URIRef] = ODM.ReasonForChange

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class SourceID(YAMLRoot):
    """
    Information that identifies the source of the data within an originating system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SourceID
    class_class_curie: ClassVar[str] = "odm:SourceID"
    class_name: ClassVar[str] = "SourceID"
    class_model_uri: ClassVar[URIRef] = ODM.SourceID

    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Signature(YAMLRoot):
    """
    An electronic signature applies to a collection of clinical data. This indicates that some user accepts legal
    responsibility for that data. See 21 CFR Part 11. The signature identifies the person signing, the location of
    signing, the signature meaning (via the referenced SignatureDef), the date and time of signing, and (in the case
    of a digital signature) an encrypted hash of the included data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Signature
    class_class_curie: ClassVar[str] = "odm:Signature"
    class_name: ClassVar[str] = "Signature"
    class_model_uri: ClassVar[URIRef] = ODM.Signature

    ID: Union[str, SignatureID] = None
    userRef: Optional[Union[dict, UserRef]] = None
    locationRef: Optional[Union[dict, LocationRef]] = None
    signatureRef: Optional[Union[dict, "SignatureRef"]] = None
    dateTimeStamp: Optional[Union[dict, DateTimeStamp]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, SignatureID):
            self.ID = SignatureID(self.ID)

        if self.userRef is not None and not isinstance(self.userRef, UserRef):
            self.userRef = UserRef(**as_dict(self.userRef))

        if self.locationRef is not None and not isinstance(self.locationRef, LocationRef):
            self.locationRef = LocationRef(**as_dict(self.locationRef))

        if self.signatureRef is not None and not isinstance(self.signatureRef, SignatureRef):
            self.signatureRef = SignatureRef(**as_dict(self.signatureRef))

        if self.dateTimeStamp is not None and not isinstance(self.dateTimeStamp, DateTimeStamp):
            self.dateTimeStamp = DateTimeStamp(**as_dict(self.dateTimeStamp))

        super().__post_init__(**kwargs)


@dataclass
class SignatureRef(YAMLRoot):
    """
    A reference to the signature meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.SignatureRef
    class_class_curie: ClassVar[str] = "odm:SignatureRef"
    class_name: ClassVar[str] = "SignatureRef"
    class_model_uri: ClassVar[URIRef] = ODM.SignatureRef

    signatureOID: Union[str, SignatureDefOID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.signatureOID):
            self.MissingRequiredField("signatureOID")
        if not isinstance(self.signatureOID, SignatureDefOID):
            self.signatureOID = SignatureDefOID(self.signatureOID)

        super().__post_init__(**kwargs)


@dataclass
class Association(YAMLRoot):
    """
    An association permits an annotation to be placed on an ordered pair of entities rather than on just one. The
    first and second KeySets identify the start and end of the annotated "link.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Association
    class_class_curie: ClassVar[str] = "odm:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = ODM.Association

    studyOID: Union[str, StudyOID] = None
    metaDataVersionOID: Union[str, MetaDataVersionOID] = None
    keySet: Optional[Union[dict, "KeySet"]] = None
    annotation: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyOID):
            self.MissingRequiredField("studyOID")
        if not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        if self._is_empty(self.metaDataVersionOID):
            self.MissingRequiredField("metaDataVersionOID")
        if not isinstance(self.metaDataVersionOID, MetaDataVersionOID):
            self.metaDataVersionOID = MetaDataVersionOID(self.metaDataVersionOID)

        if self.keySet is not None and not isinstance(self.keySet, KeySet):
            self.keySet = KeySet(**as_dict(self.keySet))

        if self.keySet is not None and not isinstance(self.keySet, KeySet):
            self.keySet = KeySet(**as_dict(self.keySet))

        if self.annotation is not None and not isinstance(self.annotation, AnnotationID):
            self.annotation = AnnotationID(self.annotation)

        super().__post_init__(**kwargs)


@dataclass
class KeySet(YAMLRoot):
    """
    A KeySet references a single entity (e.g., a study, a subject, a study event). Only those attributes needed to
    specify the particular entity are required, and all others must be omitted (see Section 2.7, Clinical Data Keys).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.KeySet
    class_class_curie: ClassVar[str] = "odm:KeySet"
    class_name: ClassVar[str] = "KeySet"
    class_model_uri: ClassVar[URIRef] = ODM.KeySet

    studyOID: Union[str, StudyOID] = None
    subjectKey: Optional[str] = None
    metaDataVersionOID: Optional[Union[str, MetaDataVersionOID]] = None
    studyEventOID: Optional[Union[str, StudyEventDefOID]] = None
    studyEventRepeatKey: Optional[str] = None
    itemGroupOID: Optional[Union[str, ItemGroupDefOID]] = None
    itemGroupRepeatKey: Optional[str] = None
    itemOID: Optional[Union[str, ItemDefOID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studyOID):
            self.MissingRequiredField("studyOID")
        if not isinstance(self.studyOID, StudyOID):
            self.studyOID = StudyOID(self.studyOID)

        if self.subjectKey is not None and not isinstance(self.subjectKey, str):
            self.subjectKey = str(self.subjectKey)

        if self.metaDataVersionOID is not None and not isinstance(self.metaDataVersionOID, MetaDataVersionOID):
            self.metaDataVersionOID = MetaDataVersionOID(self.metaDataVersionOID)

        if self.studyEventOID is not None and not isinstance(self.studyEventOID, StudyEventDefOID):
            self.studyEventOID = StudyEventDefOID(self.studyEventOID)

        if self.studyEventRepeatKey is not None and not isinstance(self.studyEventRepeatKey, str):
            self.studyEventRepeatKey = str(self.studyEventRepeatKey)

        if self.itemGroupOID is not None and not isinstance(self.itemGroupOID, ItemGroupDefOID):
            self.itemGroupOID = ItemGroupDefOID(self.itemGroupOID)

        if self.itemGroupRepeatKey is not None and not isinstance(self.itemGroupRepeatKey, str):
            self.itemGroupRepeatKey = str(self.itemGroupRepeatKey)

        if self.itemOID is not None and not isinstance(self.itemOID, ItemDefOID):
            self.itemOID = ItemDefOID(self.itemOID)

        super().__post_init__(**kwargs)


@dataclass
class Annotation(YAMLRoot):
    """
    A general note about clinical data. If an annotation has both a comment and flags, the flags should be related to
    the comment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Annotation
    class_class_curie: ClassVar[str] = "odm:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = ODM.Annotation

    ID: Union[str, AnnotationID] = None
    seqNum: int = None
    transactionType: Optional[Union[str, "TransactionType"]] = None
    comment: Optional[Union[dict, "Comment"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    flag: Optional[Union[Union[dict, "Flag"], List[Union[dict, "Flag"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, AnnotationID):
            self.ID = AnnotationID(self.ID)

        if self._is_empty(self.seqNum):
            self.MissingRequiredField("seqNum")
        if not isinstance(self.seqNum, int):
            self.seqNum = int(self.seqNum)

        if self.transactionType is not None and not isinstance(self.transactionType, TransactionType):
            self.transactionType = TransactionType(self.transactionType)

        if self.comment is not None and not isinstance(self.comment, Comment):
            self.comment = Comment(**as_dict(self.comment))

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        if not isinstance(self.flag, list):
            self.flag = [self.flag] if self.flag is not None else []
        self.flag = [v if isinstance(v, Flag) else Flag(**as_dict(v)) for v in self.flag]

        super().__post_init__(**kwargs)


@dataclass
class Comment(YAMLRoot):
    """
    A free-text (uninterpreted) comment about clinical data. The comment may have come from the sponsor or the
    clinical site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Comment
    class_class_curie: ClassVar[str] = "odm:Comment"
    class_name: ClassVar[str] = "Comment"
    class_model_uri: ClassVar[URIRef] = ODM.Comment

    sponsorOrSite: Optional[Union[str, "CommentType"]] = None
    translatedText: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sponsorOrSite is not None and not isinstance(self.sponsorOrSite, CommentType):
            self.sponsorOrSite = CommentType(self.sponsorOrSite)

        if not isinstance(self.translatedText, list):
            self.translatedText = [self.translatedText] if self.translatedText is not None else []
        self.translatedText = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.translatedText]

        super().__post_init__(**kwargs)


@dataclass
class Flag(YAMLRoot):
    """
    A machine-processable annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Flag
    class_class_curie: ClassVar[str] = "odm:Flag"
    class_name: ClassVar[str] = "Flag"
    class_model_uri: ClassVar[URIRef] = ODM.Flag

    flagValue: Optional[Union[dict, "FlagValue"]] = None
    flagType: Optional[Union[dict, "FlagType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.flagValue is not None and not isinstance(self.flagValue, FlagValue):
            self.flagValue = FlagValue(**as_dict(self.flagValue))

        if self.flagType is not None and not isinstance(self.flagType, FlagType):
            self.flagType = FlagType(**as_dict(self.flagType))

        super().__post_init__(**kwargs)


@dataclass
class FlagValue(YAMLRoot):
    """
    The value of the flag. The meaning of this value is typically dependent on the associated FlagType. The actual
    value must be a member of the referenced CodeList
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.FlagValue
    class_class_curie: ClassVar[str] = "odm:FlagValue"
    class_name: ClassVar[str] = "FlagValue"
    class_model_uri: ClassVar[URIRef] = ODM.FlagValue

    codeListOID: Union[str, CodeListOID] = None
    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.codeListOID):
            self.MissingRequiredField("codeListOID")
        if not isinstance(self.codeListOID, CodeListOID):
            self.codeListOID = CodeListOID(self.codeListOID)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class FlagType(YAMLRoot):
    """
    The type of flag. This determines the purpose and semantics of the flag.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.FlagType
    class_class_curie: ClassVar[str] = "odm:FlagType"
    class_name: ClassVar[str] = "FlagType"
    class_model_uri: ClassVar[URIRef] = ODM.FlagType

    codeListOID: Union[str, CodeListOID] = None
    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.codeListOID):
            self.MissingRequiredField("codeListOID")
        if not isinstance(self.codeListOID, CodeListOID):
            self.codeListOID = CodeListOID(self.codeListOID)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class Coding(YAMLRoot):
    """
    Coding references a symbol from a defined code system. It uses a code defined in a terminology system to associate
    semantics with a given term, codelist, variable, or group of variables. The presence of a Coding element
    associates a meaning to its parent element. Including multiple Coding elements for a given parent indicates
    synonymous meanings provided by different code systems or code system versions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Coding
    class_class_curie: ClassVar[str] = "odm:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = ODM.Coding

    system: Union[str, URIorCURIE] = None
    code: Optional[str] = None
    systemName: Optional[str] = None
    systemVersion: Optional[str] = None
    label: Optional[str] = None
    href: Optional[Union[str, URIorCURIE]] = None
    ref: Optional[Union[str, URIorCURIE]] = None
    commentOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, URIorCURIE):
            self.system = URIorCURIE(self.system)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.systemName is not None and not isinstance(self.systemName, str):
            self.systemName = str(self.systemName)

        if self.systemVersion is not None and not isinstance(self.systemVersion, str):
            self.systemVersion = str(self.systemVersion)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.href is not None and not isinstance(self.href, URIorCURIE):
            self.href = URIorCURIE(self.href)

        if self.ref is not None and not isinstance(self.ref, URIorCURIE):
            self.ref = URIorCURIE(self.ref)

        if self.commentOID is not None and not isinstance(self.commentOID, str):
            self.commentOID = str(self.commentOID)

        super().__post_init__(**kwargs)


@dataclass
class Query(YAMLRoot):
    """
    The Query element represents a request for clarification on a data item collected for a clinical trial,
    specifically a request from a sponsor or sponsor’s representative to an investigator to resolve an error or
    inconsistency discovered during data review. Queries can be created manually by individuals such as site monitors
    or data managers or automatically by systems. The full text of the Query exists in the Value child element. The
    optional Name attribute provide the means to provide a short identifier that can be included in listing or user
    interfaces.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Query
    class_class_curie: ClassVar[str] = "odm:Query"
    class_name: ClassVar[str] = "Query"
    class_model_uri: ClassVar[URIRef] = ODM.Query

    OID: Union[str, QueryOID] = None
    source: Union[str, "QuerySourceType"] = None
    state: Union[str, "QueryStateType"] = None
    lastUpdateDatetime: Union[str, XSDDateTime] = None
    target: Optional[str] = None
    type: Optional[Union[str, "QueryType"]] = None
    name: Optional[str] = None
    value: Optional[Union[dict, "Value"]] = None
    auditRecord: Optional[Union[Union[dict, AuditRecord], List[Union[dict, AuditRecord]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, QueryOID):
            self.OID = QueryOID(self.OID)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, QuerySourceType):
            self.source = QuerySourceType(self.source)

        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, QueryStateType):
            self.state = QueryStateType(self.state)

        if self._is_empty(self.lastUpdateDatetime):
            self.MissingRequiredField("lastUpdateDatetime")
        if not isinstance(self.lastUpdateDatetime, XSDDateTime):
            self.lastUpdateDatetime = XSDDateTime(self.lastUpdateDatetime)

        if self.target is not None and not isinstance(self.target, str):
            self.target = str(self.target)

        if self.type is not None and not isinstance(self.type, QueryType):
            self.type = QueryType(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, Value):
            self.value = Value(**as_dict(self.value))

        if not isinstance(self.auditRecord, list):
            self.auditRecord = [self.auditRecord] if self.auditRecord is not None else []
        self.auditRecord = [v if isinstance(v, AuditRecord) else AuditRecord(**as_dict(v)) for v in self.auditRecord]

        super().__post_init__(**kwargs)


@dataclass
class Value(YAMLRoot):
    """
    The data collected for an item. This data is represented according to DataType attribute of the ItemDef referenced
    by the ItemOID attribute in the parent ItemData element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.Value
    class_class_curie: ClassVar[str] = "odm:Value"
    class_name: ClassVar[str] = "Value"
    class_model_uri: ClassVar[URIRef] = ODM.Value

    seqNum: Optional[int] = None
    content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.seqNum is not None and not isinstance(self.seqNum, int):
            self.seqNum = int(self.seqNum)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass
class ODMFileMetadata(YAMLRoot):
    """
    Root element for ODM Documents. The ODM element is the top-level (root) element of each ODM document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.ODM
    class_class_curie: ClassVar[str] = "odm:ODM"
    class_name: ClassVar[str] = "ODMFileMetadata"
    class_model_uri: ClassVar[URIRef] = ODM.ODMFileMetadata

    fileOID: Union[str, ODMFileMetadataFileOID] = None
    fileType: Union[str, "FileType"] = None
    creationDateTime: Union[str, XSDDateTime] = None
    granularity: Optional[Union[str, "Granularity"]] = None
    context: Optional[Union[str, "Context"]] = None
    priorFileOID: Optional[Union[str, ODMFileMetadataFileOID]] = None
    asOfDateTime: Optional[Union[str, XSDDateTime]] = None
    oDMVersion: Optional[str] = None
    originator: Optional[str] = None
    sourceSystem: Optional[str] = None
    sourceSystemVersion: Optional[str] = None
    description: Optional[Union[dict, Description]] = None
    study: Optional[Union[Dict[Union[str, StudyOID], Union[dict, Study]], List[Union[dict, Study]]]] = empty_dict()
    adminData: Optional[Union[Union[dict, AdminData], List[Union[dict, AdminData]]]] = empty_list()
    referenceData: Optional[Union[Union[dict, ReferenceData], List[Union[dict, ReferenceData]]]] = empty_list()
    clinicalData: Optional[Union[Union[dict, ClinicalData], List[Union[dict, ClinicalData]]]] = empty_list()
    association: Optional[Union[Union[dict, Association], List[Union[dict, Association]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.fileOID):
            self.MissingRequiredField("fileOID")
        if not isinstance(self.fileOID, ODMFileMetadataFileOID):
            self.fileOID = ODMFileMetadataFileOID(self.fileOID)

        if self._is_empty(self.fileType):
            self.MissingRequiredField("fileType")
        if not isinstance(self.fileType, FileType):
            self.fileType = FileType(self.fileType)

        if self._is_empty(self.creationDateTime):
            self.MissingRequiredField("creationDateTime")
        if not isinstance(self.creationDateTime, XSDDateTime):
            self.creationDateTime = XSDDateTime(self.creationDateTime)

        if self.granularity is not None and not isinstance(self.granularity, Granularity):
            self.granularity = Granularity(self.granularity)

        if self.context is not None and not isinstance(self.context, Context):
            self.context = Context(self.context)

        if self.priorFileOID is not None and not isinstance(self.priorFileOID, ODMFileMetadataFileOID):
            self.priorFileOID = ODMFileMetadataFileOID(self.priorFileOID)

        if self.asOfDateTime is not None and not isinstance(self.asOfDateTime, XSDDateTime):
            self.asOfDateTime = XSDDateTime(self.asOfDateTime)

        if self.oDMVersion is not None and not isinstance(self.oDMVersion, str):
            self.oDMVersion = str(self.oDMVersion)

        if self.originator is not None and not isinstance(self.originator, str):
            self.originator = str(self.originator)

        if self.sourceSystem is not None and not isinstance(self.sourceSystem, str):
            self.sourceSystem = str(self.sourceSystem)

        if self.sourceSystemVersion is not None and not isinstance(self.sourceSystemVersion, str):
            self.sourceSystemVersion = str(self.sourceSystemVersion)

        if self.description is not None and not isinstance(self.description, Description):
            self.description = Description(**as_dict(self.description))

        self._normalize_inlined_as_list(slot_name="study", slot_type=Study, key_name="OID", keyed=True)

        if not isinstance(self.adminData, list):
            self.adminData = [self.adminData] if self.adminData is not None else []
        self.adminData = [v if isinstance(v, AdminData) else AdminData(**as_dict(v)) for v in self.adminData]

        if not isinstance(self.referenceData, list):
            self.referenceData = [self.referenceData] if self.referenceData is not None else []
        self.referenceData = [v if isinstance(v, ReferenceData) else ReferenceData(**as_dict(v)) for v in self.referenceData]

        if not isinstance(self.clinicalData, list):
            self.clinicalData = [self.clinicalData] if self.clinicalData is not None else []
        self.clinicalData = [v if isinstance(v, ClinicalData) else ClinicalData(**as_dict(v)) for v in self.clinicalData]

        if not isinstance(self.association, list):
            self.association = [self.association] if self.association is not None else []
        self.association = [v if isinstance(v, Association) else Association(**as_dict(v)) for v in self.association]

        super().__post_init__(**kwargs)


# Enumerations
class DataType(EnumDefinitionImpl):
    """
    Enumeration used in dataType
    """
    integer = PermissibleValue(text="integer")
    decimal = PermissibleValue(text="decimal")
    float = PermissibleValue(text="float")
    double = PermissibleValue(text="double")
    date = PermissibleValue(text="date")
    datetime = PermissibleValue(text="datetime")
    time = PermissibleValue(text="time")
    text = PermissibleValue(text="text")
    string = PermissibleValue(text="string")
    URI = PermissibleValue(text="URI")
    boolean = PermissibleValue(text="boolean")
    hexBinary = PermissibleValue(text="hexBinary")
    base64Binary = PermissibleValue(text="base64Binary")
    hexFloat = PermissibleValue(text="hexFloat")
    base64Float = PermissibleValue(text="base64Float")
    partialDate = PermissibleValue(text="partialDate")
    partialTime = PermissibleValue(text="partialTime")
    partialDatetime = PermissibleValue(text="partialDatetime")
    durationDatetime = PermissibleValue(text="durationDatetime")
    intervalDatetime = PermissibleValue(text="intervalDatetime")
    incompleteDatetime = PermissibleValue(text="incompleteDatetime")
    incompleteDate = PermissibleValue(text="incompleteDate")
    incompleteTime = PermissibleValue(text="incompleteTime")

    _defn = EnumDefinition(
        name="DataType",
        description="Enumeration used in dataType",
    )

class CLDataType(EnumDefinitionImpl):
    """
    Enumeration used in dataType
    """
    integer = PermissibleValue(text="integer")
    decimal = PermissibleValue(text="decimal")
    text = PermissibleValue(text="text")
    string = PermissibleValue(text="string")

    _defn = EnumDefinition(
        name="CLDataType",
        description="Enumeration used in dataType",
    )

class FileType(EnumDefinitionImpl):
    """
    Enumeration used in fileType
    """
    Snapshot = PermissibleValue(text="Snapshot")
    Transactional = PermissibleValue(text="Transactional")

    _defn = EnumDefinition(
        name="FileType",
        description="Enumeration used in fileType",
    )

class Granularity(EnumDefinitionImpl):
    """
    Enumeration used in granularity
    """
    All = PermissibleValue(text="All")
    Metadata = PermissibleValue(text="Metadata")
    AdminData = PermissibleValue(text="AdminData")
    ReferenceData = PermissibleValue(text="ReferenceData")
    AllClinicalData = PermissibleValue(text="AllClinicalData")
    SingleSite = PermissibleValue(text="SingleSite")
    SingleSubject = PermissibleValue(text="SingleSubject")

    _defn = EnumDefinition(
        name="Granularity",
        description="Enumeration used in granularity",
    )

class Context(EnumDefinitionImpl):
    """
    Enumeration used in context
    """
    Archive = PermissibleValue(text="Archive")
    Exchange = PermissibleValue(text="Exchange")
    Submission = PermissibleValue(text="Submission")

    _defn = EnumDefinition(
        name="Context",
        description="Enumeration used in context",
    )

class EventType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    Scheduled = PermissibleValue(text="Scheduled")
    Unscheduled = PermissibleValue(text="Unscheduled")
    Common = PermissibleValue(text="Common")

    _defn = EnumDefinition(
        name="EventType",
        description="Enumeration used in type",
    )

class BranchingType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    Exclusive = PermissibleValue(text="Exclusive")
    Parallel = PermissibleValue(text="Parallel")

    _defn = EnumDefinition(
        name="BranchingType",
        description="Enumeration used in type",
    )

class StudyObjectiveLevel(EnumDefinitionImpl):
    """
    Enumeration used in level
    """
    Primary = PermissibleValue(text="Primary")
    Secondary = PermissibleValue(text="Secondary")
    Exploratory = PermissibleValue(text="Exploratory")

    _defn = EnumDefinition(
        name="StudyObjectiveLevel",
        description="Enumeration used in level",
    )

class TrialPhaseTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TrialPhaseTypeEnum",
        code_set=NCIT.C66737,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "NOT APPLICABLE",
            PermissibleValue(
                text="NOT APPLICABLE",
                meaning=NCIT.C48660))
        setattr(cls, "PHASE 0 TRIAL",
            PermissibleValue(
                text="PHASE 0 TRIAL",
                meaning=NCIT.C54721))
        setattr(cls, "PHASE I TRIAL",
            PermissibleValue(
                text="PHASE I TRIAL",
                meaning=NCIT.C15600))
        setattr(cls, "PHASE I/II TRIAL",
            PermissibleValue(
                text="PHASE I/II TRIAL",
                meaning=NCIT.C15693))
        setattr(cls, "PHASE II TRIAL",
            PermissibleValue(
                text="PHASE II TRIAL",
                meaning=NCIT.C15601))
        setattr(cls, "PHASE II/III TRIAL",
            PermissibleValue(
                text="PHASE II/III TRIAL",
                meaning=NCIT.C15694))
        setattr(cls, "PHASE IIA TRIAL",
            PermissibleValue(
                text="PHASE IIA TRIAL",
                meaning=NCIT.C49686))
        setattr(cls, "PHASE IIB TRIAL",
            PermissibleValue(
                text="PHASE IIB TRIAL",
                meaning=NCIT.C49688))
        setattr(cls, "PHASE III TRIAL",
            PermissibleValue(
                text="PHASE III TRIAL",
                meaning=NCIT.C15602))
        setattr(cls, "PHASE IIIA TRIAL",
            PermissibleValue(
                text="PHASE IIIA TRIAL",
                meaning=NCIT.C49687))
        setattr(cls, "PHASE IIIB TRIAL",
            PermissibleValue(
                text="PHASE IIIB TRIAL",
                meaning=NCIT.C49689))
        setattr(cls, "PHASE IV TRIAL",
            PermissibleValue(
                text="PHASE IV TRIAL",
                meaning=NCIT.C15603))
        setattr(cls, "PHASE V TRIAL",
            PermissibleValue(
                text="PHASE V TRIAL",
                meaning=NCIT.C47865))

class StudyEndPointType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    Simple = PermissibleValue(text="Simple")
    Humane = PermissibleValue(text="Humane")
    Surrogate = PermissibleValue(text="Surrogate")
    Composite = PermissibleValue(text="Composite")

    _defn = EnumDefinition(
        name="StudyEndPointType",
        description="Enumeration used in type",
    )

class StudyEstimandLevel(EnumDefinitionImpl):
    """
    Enumeration used in level
    """
    Primary = PermissibleValue(text="Primary")
    Secondary = PermissibleValue(text="Secondary")
    Exploratory = PermissibleValue(text="Exploratory")

    _defn = EnumDefinition(
        name="StudyEstimandLevel",
        description="Enumeration used in level",
    )

class RelativeTimingConstraintType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    StartToStart = PermissibleValue(text="StartToStart")
    StartToFinish = PermissibleValue(text="StartToFinish")
    FinishToStart = PermissibleValue(text="FinishToStart")
    FinishToFinish = PermissibleValue(text="FinishToFinish")

    _defn = EnumDefinition(
        name="RelativeTimingConstraintType",
        description="Enumeration used in type",
    )

class Comparator(EnumDefinitionImpl):
    """
    Enumeration used in comparator
    """
    LT = PermissibleValue(text="LT")
    LE = PermissibleValue(text="LE")
    GT = PermissibleValue(text="GT")
    GE = PermissibleValue(text="GE")
    EQ = PermissibleValue(text="EQ")
    NE = PermissibleValue(text="NE")
    IN = PermissibleValue(text="IN")
    NOTIN = PermissibleValue(text="NOTIN")

    _defn = EnumDefinition(
        name="Comparator",
        description="Enumeration used in comparator",
    )

class SoftOrHard(EnumDefinitionImpl):
    """
    Enumeration used in softHard
    """
    Soft = PermissibleValue(text="Soft")
    Hard = PermissibleValue(text="Hard")

    _defn = EnumDefinition(
        name="SoftOrHard",
        description="Enumeration used in softHard",
    )

class TransactionType(EnumDefinitionImpl):
    """
    Enumeration used in transactionType
    """
    Insert = PermissibleValue(text="Insert")
    Update = PermissibleValue(text="Update")
    Remove = PermissibleValue(text="Remove")
    Upsert = PermissibleValue(text="Upsert")
    Context = PermissibleValue(text="Context")

    _defn = EnumDefinition(
        name="TransactionType",
        description="Enumeration used in transactionType",
    )

class UserType(EnumDefinitionImpl):
    """
    Enumeration used in userType
    """
    Sponsor = PermissibleValue(text="Sponsor")
    Investigator = PermissibleValue(text="Investigator")
    Lab = PermissibleValue(text="Lab")
    Other = PermissibleValue(text="Other")
    Subject = PermissibleValue(text="Subject")
    Monitor = PermissibleValue(text="Monitor")
    Assessor = PermissibleValue(text="Assessor")

    _defn = EnumDefinition(
        name="UserType",
        description="Enumeration used in userType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data analyst",
            PermissibleValue(text="Data analyst"))
        setattr(cls, "Care provider",
            PermissibleValue(text="Care provider"))

class OrganizationType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    Sponsor = PermissibleValue(text="Sponsor")
    Site = PermissibleValue(text="Site")
    CRO = PermissibleValue(text="CRO")
    Lab = PermissibleValue(text="Lab")
    Other = PermissibleValue(text="Other")
    TechnologyProvider = PermissibleValue(text="TechnologyProvider")

    _defn = EnumDefinition(
        name="OrganizationType",
        description="Enumeration used in type",
    )

class TelecomTypeType(EnumDefinitionImpl):
    """
    Enumeration used in telecomType
    """
    Email = PermissibleValue(text="Email")
    Pager = PermissibleValue(text="Pager")
    Phone = PermissibleValue(text="Phone")
    Fax = PermissibleValue(text="Fax")
    SMS = PermissibleValue(text="SMS")
    URL = PermissibleValue(text="URL")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="TelecomTypeType",
        description="Enumeration used in telecomType",
    )

class CommentType(EnumDefinitionImpl):
    """
    Enumeration used in sponsorOrSite
    """
    Sponsor = PermissibleValue(text="Sponsor")
    Site = PermissibleValue(text="Site")

    _defn = EnumDefinition(
        name="CommentType",
        description="Enumeration used in sponsorOrSite",
    )

class SignMethod(EnumDefinitionImpl):
    """
    Enumeration used in methodology
    """
    Digital = PermissibleValue(text="Digital")
    Electronic = PermissibleValue(text="Electronic")

    _defn = EnumDefinition(
        name="SignMethod",
        description="Enumeration used in methodology",
    )

class EditPointType(EnumDefinitionImpl):
    """
    Enumeration used in editPoint
    """
    Monitoring = PermissibleValue(text="Monitoring")
    DataManagement = PermissibleValue(text="DataManagement")
    DBAudit = PermissibleValue(text="DBAudit")

    _defn = EnumDefinition(
        name="EditPointType",
        description="Enumeration used in editPoint",
    )

class YesOrNo(EnumDefinitionImpl):
    """
    Enumeration used in isReferenceData, repeating, usedMethod, mandatory
    """
    Yes = PermissibleValue(text="Yes")
    No = PermissibleValue(text="No")

    _defn = EnumDefinition(
        name="YesOrNo",
        description="Enumeration used in isReferenceData, repeating, usedMethod, mandatory",
    )

class YesOnly(EnumDefinitionImpl):
    """
    Enumeration used in other, hasNoData, isNull, extendedValue, isNonStandard, repeat
    """
    _defn = EnumDefinition(
        name="YesOnly",
        description="Enumeration used in other, hasNoData, isNull, extendedValue, isNonStandard, repeat",
    )

class MethodType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    Computation = PermissibleValue(text="Computation")
    Imputation = PermissibleValue(text="Imputation")
    Preload = PermissibleValue(text="Preload")
    Transpose = PermissibleValue(text="Transpose")

    _defn = EnumDefinition(
        name="MethodType",
        description="Enumeration used in type",
    )

class ItemGroupRepeatingType(EnumDefinitionImpl):
    """
    Enumeration used in repeating
    """
    No = PermissibleValue(text="No")
    Simple = PermissibleValue(text="Simple")
    Dynamic = PermissibleValue(text="Dynamic")
    Static = PermissibleValue(text="Static")

    _defn = EnumDefinition(
        name="ItemGroupRepeatingType",
        description="Enumeration used in repeating",
    )

class ItemGroupTypeTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ItemGroupTypeTypeEnum",
    )

class QuerySourceType(EnumDefinitionImpl):
    """
    Enumeration used in source
    """
    System = PermissibleValue(text="System")

    _defn = EnumDefinition(
        name="QuerySourceType",
        description="Enumeration used in source",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data Management",
            PermissibleValue(text="Data Management"))
        setattr(cls, "Site Monitor",
            PermissibleValue(text="Site Monitor"))
        setattr(cls, "Coding System",
            PermissibleValue(text="Coding System"))
        setattr(cls, "Safety Reviewer",
            PermissibleValue(text="Safety Reviewer"))

class QueryType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    Manual = PermissibleValue(text="Manual")
    System = PermissibleValue(text="System")

    _defn = EnumDefinition(
        name="QueryType",
        description="Enumeration used in type",
    )

class QueryStateType(EnumDefinitionImpl):
    """
    Enumeration used in state
    """
    Candidate = PermissibleValue(text="Candidate")
    Open = PermissibleValue(text="Open")
    Answered = PermissibleValue(text="Answered")
    Closed = PermissibleValue(text="Closed")
    Cancelled = PermissibleValue(text="Cancelled")
    Resolved = PermissibleValue(text="Resolved")

    _defn = EnumDefinition(
        name="QueryStateType",
        description="Enumeration used in state",
    )

class DefCoreType(EnumDefinitionImpl):

    Cond = PermissibleValue(text="Cond")
    Exp = PermissibleValue(text="Exp")
    Perm = PermissibleValue(text="Perm")
    Req = PermissibleValue(text="Req")

    _defn = EnumDefinition(
        name="DefCoreType",
    )

class ODMCoreType(EnumDefinitionImpl):

    HR = PermissibleValue(text="HR")
    O = PermissibleValue(text="O")

    _defn = EnumDefinition(
        name="ODMCoreType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "R/C",
            PermissibleValue(text="R/C"))

class OriginSource(EnumDefinitionImpl):
    """
    Enumeration used in source
    """
    Investigator = PermissibleValue(
        text="Investigator",
        meaning=NCIT.C25936)
    Sponsor = PermissibleValue(
        text="Sponsor",
        meaning=NCIT.C70793)
    Subject = PermissibleValue(
        text="Subject",
        meaning=NCIT.C41189)
    Vendor = PermissibleValue(
        text="Vendor",
        meaning=NCIT.C68608)

    _defn = EnumDefinition(
        name="OriginSource",
        description="Enumeration used in source",
    )

class OriginType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    Assigned = PermissibleValue(
        text="Assigned",
        meaning=NCIT.C170547)
    Collected = PermissibleValue(
        text="Collected",
        meaning=NCIT.C170548)
    Derived = PermissibleValue(
        text="Derived",
        meaning=NCIT.C170549)
    EHR = PermissibleValue(
        text="EHR",
        meaning=NCIT.C170549)
    Other = PermissibleValue(
        text="Other",
        meaning=NCIT.C17649)
    Predecessor = PermissibleValue(
        text="Predecessor",
        meaning=NCIT.C170550)
    Protocol = PermissibleValue(
        text="Protocol",
        meaning=NCIT.C170551)

    _defn = EnumDefinition(
        name="OriginType",
        description="Enumeration used in type",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Available",
            PermissibleValue(
                text="Not Available",
                meaning=NCIT.C126101))

class PDFPageType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    NamedDestination = PermissibleValue(text="NamedDestination")
    PhysicalRef = PermissibleValue(text="PhysicalRef")

    _defn = EnumDefinition(
        name="PDFPageType",
        description="Enumeration used in type",
    )

class StandardName(EnumDefinitionImpl):
    """
    Enumeration used in name
    """
    ADaMIG = PermissibleValue(
        text="ADaMIG",
        meaning=NCIT.C170552)
    SDTMIG = PermissibleValue(
        text="SDTMIG",
        meaning=NCIT.C170455)
    SENDIG = PermissibleValue(
        text="SENDIG",
        meaning=NCIT.C170456)

    _defn = EnumDefinition(
        name="StandardName",
        description="Enumeration used in name",
        code_set=NCIT.C170452,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CDISC/NCI",
            PermissibleValue(
                text="CDISC/NCI",
                meaning=NCIT.C163415))
        setattr(cls, "SDTMIG-AP",
            PermissibleValue(
                text="SDTMIG-AP",
                meaning=NCIT.C170553))
        setattr(cls, "SDTMIG-MD",
            PermissibleValue(
                text="SDTMIG-MD",
                meaning=NCIT.C170554))
        setattr(cls, "SENDIG-AR",
            PermissibleValue(
                text="SENDIG-AR",
                meaning=NCIT.C181230))
        setattr(cls, "SENDIG-DART",
            PermissibleValue(
                text="SENDIG-DART",
                meaning=NCIT.C170556))

class StandardPublishingSet(EnumDefinitionImpl):
    """
    Enumeration used in publishingSet
    """
    ADaM = PermissibleValue(
        text="ADaM",
        meaning=NCIT.C180548)
    CDASH = PermissibleValue(
        text="CDASH",
        meaning=NCIT.C180549)
    SDTM = PermissibleValue(
        text="SDTM",
        meaning=NCIT.C180551)
    SEND = PermissibleValue(
        text="SEND",
        meaning=NCIT.C180552)

    _defn = EnumDefinition(
        name="StandardPublishingSet",
        description="Enumeration used in publishingSet",
        code_set=NCIT.C172331,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DEFINE-XML",
            PermissibleValue(
                text="DEFINE-XML",
                meaning=NCIT.C180550))

class StandardStatusEnum(EnumDefinitionImpl):

    Draft = PermissibleValue(
        text="Draft",
        meaning=NCIT.C172453)
    Final = PermissibleValue(
        text="Final",
        meaning=NCIT.C172455)
    Provisional = PermissibleValue(
        text="Provisional",
        meaning=NCIT.C172454)

    _defn = EnumDefinition(
        name="StandardStatusEnum",
        code_set=NCIT.C172332,
    )

class StandardType(EnumDefinitionImpl):
    """
    Enumeration used in type
    """
    CT = PermissibleValue(
        text="CT",
        meaning=NCIT.C163415)
    IG = PermissibleValue(
        text="IG",
        meaning=NCIT.C170454)

    _defn = EnumDefinition(
        name="StandardType",
        description="Enumeration used in type",
        code_set=NCIT.C170451,
    )

class DictionaryNameTypeEnum(EnumDefinitionImpl):

    COSTART = PermissibleValue(
        text="COSTART",
        meaning=NCIT.C49471)
    CTCAE = PermissibleValue(
        text="CTCAE",
        meaning=NCIT.C49704)
    ICD = PermissibleValue(
        text="ICD",
        meaning=NCIT.C49474)
    LOINC = PermissibleValue(
        text="LOINC",
        meaning=NCIT.C49476)
    MedDRA = PermissibleValue(
        text="MedDRA",
        meaning=NCIT.C43820)
    SNOMED = PermissibleValue(
        text="SNOMED",
        meaning=NCIT.C53489)
    UNII = PermissibleValue(
        text="UNII",
        meaning=NCIT.C163417)
    WHOART = PermissibleValue(
        text="WHOART",
        meaning=NCIT.C49468)
    WHODD = PermissibleValue(
        text="WHODD",
        meaning=NCIT.C49475)

    _defn = EnumDefinition(
        name="DictionaryNameTypeEnum",
        code_set=NCIT.C66788,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CDISC CT",
            PermissibleValue(
                text="CDISC CT",
                meaning=NCIT.C163415))
        setattr(cls, "D-U-N-S NUMBER",
            PermissibleValue(
                text="D-U-N-S NUMBER",
                meaning=NCIT.C134003))
        setattr(cls, "MED-RT",
            PermissibleValue(
                text="MED-RT",
                meaning=NCIT.C163416))
        setattr(cls, "WHO ATC CLASSIFICATION SYSTEM",
            PermissibleValue(
                text="WHO ATC CLASSIFICATION SYSTEM",
                meaning=NCIT.C154331))

class ItemGroupClass(EnumDefinitionImpl):
    """
    Enumeration used in name
    """
    EVENTS = PermissibleValue(
        text="EVENTS",
        meaning=NCIT.C103372)
    FINDINGS = PermissibleValue(
        text="FINDINGS",
        meaning=NCIT.C103373)
    INTERVENTIONS = PermissibleValue(
        text="INTERVENTIONS",
        meaning=NCIT.C103374)
    RELATIONSHIP = PermissibleValue(
        text="RELATIONSHIP",
        meaning=NCIT.C103376)

    _defn = EnumDefinition(
        name="ItemGroupClass",
        description="Enumeration used in name",
        code_set=NCIT.C103329,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ADAM OTHER",
            PermissibleValue(
                text="ADAM OTHER",
                meaning=NCIT.C103375))
        setattr(cls, "BASIC DATA STRUCTURE",
            PermissibleValue(
                text="BASIC DATA STRUCTURE",
                meaning=NCIT.C103371))
        setattr(cls, "DEVICE LEVEL ANALYSIS DATASET",
            PermissibleValue(
                text="DEVICE LEVEL ANALYSIS DATASET",
                meaning=NCIT.C177921))
        setattr(cls, "FINDINGS ABOUT",
            PermissibleValue(
                text="FINDINGS ABOUT",
                meaning=NCIT.C135396))
        setattr(cls, "MEDICAL DEVICE BASIC DATA STRUCTURE",
            PermissibleValue(
                text="MEDICAL DEVICE BASIC DATA STRUCTURE",
                meaning=NCIT.C177922))
        setattr(cls, "MEDICAL DEVICE OCCURRENCE DATA STRUCTURE",
            PermissibleValue(
                text="MEDICAL DEVICE OCCURRENCE DATA STRUCTURE",
                meaning=NCIT.C177923))
        setattr(cls, "OCCURRENCE DATA STRUCTURE",
            PermissibleValue(
                text="OCCURRENCE DATA STRUCTURE",
                meaning=NCIT.C123454))
        setattr(cls, "SPECIAL PURPOSE",
            PermissibleValue(
                text="SPECIAL PURPOSE",
                meaning=NCIT.C103377))
        setattr(cls, "STUDY REFERENCE",
            PermissibleValue(
                text="STUDY REFERENCE",
                meaning=NCIT.C147271))
        setattr(cls, "SUBJECT LEVEL ANALYSIS DATASET",
            PermissibleValue(
                text="SUBJECT LEVEL ANALYSIS DATASET",
                meaning=NCIT.C103378))
        setattr(cls, "TRIAL DESIGN",
            PermissibleValue(
                text="TRIAL DESIGN",
                meaning=NCIT.C103379))

class ItemGroupSubClass(EnumDefinitionImpl):
    """
    Enumeration used in name
    """
    _defn = EnumDefinition(
        name="ItemGroupSubClass",
        description="Enumeration used in name",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ADVERSE EVENT",
            PermissibleValue(
                text="ADVERSE EVENT",
                meaning=NCIT.C176265))
        setattr(cls, "MEDICAL DEVICE TIME-TO-EVENT",
            PermissibleValue(
                text="MEDICAL DEVICE TIME-TO-EVENT",
                meaning=NCIT.C177920))
        setattr(cls, "NON-COMPARTMENTAL ANALYSIS",
            PermissibleValue(
                text="NON-COMPARTMENTAL ANALYSIS",
                meaning=NCIT.C172452))
        setattr(cls, "TIME-TO-EVENT",
            PermissibleValue(
                text="TIME-TO-EVENT",
                meaning=NCIT.C165637))

# Slots
class slots:
    pass

slots.codedValue = Slot(uri=ODM.codedValue, name="codedValue", curie=ODM.curie('codedValue'),
                   model_uri=ODM.codedValue, domain=None, range=Optional[str])

slots.sponsorOrSite = Slot(uri=ODM.sponsorOrSite, name="sponsorOrSite", curie=ODM.curie('sponsorOrSite'),
                   model_uri=ODM.sponsorOrSite, domain=None, range=Optional[Union[str, "CommentType"]])

slots.state = Slot(uri=ODM.state, name="state", curie=ODM.curie('state'),
                   model_uri=ODM.state, domain=None, range=Optional[Union[str, "QueryStateType"]])

slots.core = Slot(uri=ODM.core, name="core", curie=ODM.curie('core'),
                   model_uri=ODM.core, domain=None, range=Optional[str])

slots.softHard = Slot(uri=ODM.softHard, name="softHard", curie=ODM.curie('softHard'),
                   model_uri=ODM.softHard, domain=None, range=Optional[Union[str, "SoftOrHard"]])

slots.structuralElementOID = Slot(uri=ODM.structuralElementOID, name="structuralElementOID", curie=ODM.curie('structuralElementOID'),
                   model_uri=ODM.structuralElementOID, domain=None, range=Optional[str])

slots.dataType = Slot(uri=ODM.dataType, name="dataType", curie=ODM.curie('dataType'),
                   model_uri=ODM.dataType, domain=None, range=Optional[str])

slots.durationPreWindow = Slot(uri=ODM.durationPreWindow, name="durationPreWindow", curie=ODM.curie('durationPreWindow'),
                   model_uri=ODM.durationPreWindow, domain=None, range=Optional[str])

slots.sourceSystemVersion = Slot(uri=ODM.sourceSystemVersion, name="sourceSystemVersion", curie=ODM.curie('sourceSystemVersion'),
                   model_uri=ODM.sourceSystemVersion, domain=None, range=Optional[str])

slots.fileType = Slot(uri=ODM.fileType, name="fileType", curie=ODM.curie('fileType'),
                   model_uri=ODM.fileType, domain=None, range=Optional[Union[str, "FileType"]])

slots.variableSet = Slot(uri=ODM.variableSet, name="variableSet", curie=ODM.curie('variableSet'),
                   model_uri=ODM.variableSet, domain=None, range=Optional[str])

slots.predecessorOID = Slot(uri=ODM.predecessorOID, name="predecessorOID", curie=ODM.curie('predecessorOID'),
                   model_uri=ODM.predecessorOID, domain=None, range=Optional[str])

slots.href = Slot(uri=ODM.href, name="href", curie=ODM.curie('href'),
                   model_uri=ODM.href, domain=None, range=Optional[str])

slots.epochOID = Slot(uri=ODM.epochOID, name="epochOID", curie=ODM.curie('epochOID'),
                   model_uri=ODM.epochOID, domain=None, range=Optional[Union[str, EpochOID]])

slots.context = Slot(uri=ODM.context, name="context", curie=ODM.curie('context'),
                   model_uri=ODM.context, domain=None, range=Optional[str])

slots.transactionType = Slot(uri=ODM.transactionType, name="transactionType", curie=ODM.curie('transactionType'),
                   model_uri=ODM.transactionType, domain=None, range=Optional[Union[str, "TransactionType"]])

slots.commentOID = Slot(uri=ODM.commentOID, name="commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.commentOID, domain=None, range=Optional[str])

slots.timepointPostWindow = Slot(uri=ODM.timepointPostWindow, name="timepointPostWindow", curie=ODM.curie('timepointPostWindow'),
                   model_uri=ODM.timepointPostWindow, domain=None, range=Optional[str])

slots.rank = Slot(uri=ODM.rank, name="rank", curie=ODM.curie('rank'),
                   model_uri=ODM.rank, domain=None, range=Optional[Decimal])

slots.granularity = Slot(uri=ODM.granularity, name="granularity", curie=ODM.curie('granularity'),
                   model_uri=ODM.granularity, domain=None, range=Optional[Union[str, "Granularity"]])

slots.originator = Slot(uri=ODM.originator, name="originator", curie=ODM.curie('originator'),
                   model_uri=ODM.originator, domain=None, range=Optional[str])

slots.OID = Slot(uri=ODM.OID, name="OID", curie=ODM.curie('OID'),
                   model_uri=ODM.OID, domain=None, range=URIRef)

slots.studyInterventionOID = Slot(uri=ODM.studyInterventionOID, name="studyInterventionOID", curie=ODM.curie('studyInterventionOID'),
                   model_uri=ODM.studyInterventionOID, domain=None, range=Optional[Union[str, StudyInterventionOID]])

slots.timepointTarget = Slot(uri=ODM.timepointTarget, name="timepointTarget", curie=ODM.curie('timepointTarget'),
                   model_uri=ODM.timepointTarget, domain=None, range=Optional[str])

slots.target = Slot(uri=ODM.target, name="target", curie=ODM.curie('target'),
                   model_uri=ODM.target, domain=None, range=Optional[str])

slots.method = Slot(uri=ODM.method, name="method", curie=ODM.curie('method'),
                   model_uri=ODM.method, domain=None, range=Optional[str])

slots.userOID = Slot(uri=ODM.userOID, name="userOID", curie=ODM.curie('userOID'),
                   model_uri=ODM.userOID, domain=None, range=Optional[Union[str, UserOID]])

slots.startConditionOID = Slot(uri=ODM.startConditionOID, name="startConditionOID", curie=ODM.curie('startConditionOID'),
                   model_uri=ODM.startConditionOID, domain=None, range=Optional[Union[str, ConditionDefOID]])

slots.sequenceNumber = Slot(uri=ODM.sequenceNumber, name="sequenceNumber", curie=ODM.curie('sequenceNumber'),
                   model_uri=ODM.sequenceNumber, domain=None, range=Optional[int])

slots.durationPostWindow = Slot(uri=ODM.durationPostWindow, name="durationPostWindow", curie=ODM.curie('durationPostWindow'),
                   model_uri=ODM.durationPostWindow, domain=None, range=Optional[str])

slots.other = Slot(uri=ODM.other, name="other", curie=ODM.curie('other'),
                   model_uri=ODM.other, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.term = Slot(uri=ODM.term, name="term", curie=ODM.curie('term'),
                   model_uri=ODM.term, domain=None, range=Optional[str])

slots.purpose = Slot(uri=ODM.purpose, name="purpose", curie=ODM.curie('purpose'),
                   model_uri=ODM.purpose, domain=None, range=Optional[str])

slots.definition = Slot(uri=ODM.definition, name="definition", curie=ODM.curie('definition'),
                   model_uri=ODM.definition, domain=None, range=Optional[Union[dict, Definition]])

slots.systemName = Slot(uri=ODM.systemName, name="systemName", curie=ODM.curie('systemName'),
                   model_uri=ODM.systemName, domain=None, range=Optional[str])

slots.endOID = Slot(uri=ODM.endOID, name="endOID", curie=ODM.curie('endOID'),
                   model_uri=ODM.endOID, domain=None, range=Optional[str])

slots.studyTargetPopulationOID = Slot(uri=ODM.studyTargetPopulationOID, name="studyTargetPopulationOID", curie=ODM.curie('studyTargetPopulationOID'),
                   model_uri=ODM.studyTargetPopulationOID, domain=None, range=Optional[Union[str, StudyTargetPopulationOID]])

slots.label = Slot(uri=ODM.label, name="label", curie=ODM.curie('label'),
                   model_uri=ODM.label, domain=None, range=Optional[str])

slots.telecomType = Slot(uri=ODM.telecomType, name="telecomType", curie=ODM.curie('telecomType'),
                   model_uri=ODM.telecomType, domain=None, range=Optional[Union[str, "TelecomTypeType"]])

slots.firstPage = Slot(uri=ODM.firstPage, name="firstPage", curie=ODM.curie('firstPage'),
                   model_uri=ODM.firstPage, domain=None, range=Optional[int])

slots.oDMVersion = Slot(uri=ODM.oDMVersion, name="oDMVersion", curie=ODM.curie('oDMVersion'),
                   model_uri=ODM.oDMVersion, domain=None, range=Optional[str])

slots.methodology = Slot(uri=ODM.methodology, name="methodology", curie=ODM.curie('methodology'),
                   model_uri=ODM.methodology, domain=None, range=Optional[Union[str, "SignMethod"]])

slots.transitionOID = Slot(uri=ODM.transitionOID, name="transitionOID", curie=ODM.curie('transitionOID'),
                   model_uri=ODM.transitionOID, domain=None, range=Optional[Union[str, TransitionOID]])

slots.type = Slot(uri=ODM.type, name="type", curie=ODM.curie('type'),
                   model_uri=ODM.type, domain=None, range=Optional[str])

slots.datasetName = Slot(uri=ODM.datasetName, name="datasetName", curie=ODM.curie('datasetName'),
                   model_uri=ODM.datasetName, domain=None, range=Optional[str])

slots.category = Slot(uri=ODM.category, name="category", curie=ODM.curie('category'),
                   model_uri=ODM.category, domain=None, range=Optional[str])

slots.isNull = Slot(uri=ODM.isNull, name="isNull", curie=ODM.curie('isNull'),
                   model_uri=ODM.isNull, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.comparator = Slot(uri=ODM.comparator, name="comparator", curie=ODM.curie('comparator'),
                   model_uri=ODM.comparator, domain=None, range=Optional[Union[str, "Comparator"]])

slots.version = Slot(uri=ODM.version, name="version", curie=ODM.curie('version'),
                   model_uri=ODM.version, domain=None, range=Optional[str])

slots.targetTransitionOID = Slot(uri=ODM.targetTransitionOID, name="targetTransitionOID", curie=ODM.curie('targetTransitionOID'),
                   model_uri=ODM.targetTransitionOID, domain=None, range=Optional[Union[str, TransitionOID]])

slots.studyEventOID = Slot(uri=ODM.studyEventOID, name="studyEventOID", curie=ODM.curie('studyEventOID'),
                   model_uri=ODM.studyEventOID, domain=None, range=Optional[Union[str, StudyEventDefOID]])

slots.leafID = Slot(uri=ODM.leafID, name="leafID", curie=ODM.curie('leafID'),
                   model_uri=ODM.leafID, domain=None, range=Optional[Union[str, LeafID]])

slots.isNonStandard = Slot(uri=ODM.isNonStandard, name="isNonStandard", curie=ODM.curie('isNonStandard'),
                   model_uri=ODM.isNonStandard, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.endConditionOID = Slot(uri=ODM.endConditionOID, name="endConditionOID", curie=ODM.curie('endConditionOID'),
                   model_uri=ODM.endConditionOID, domain=None, range=Optional[Union[str, ConditionDefOID]])

slots.pageRefs = Slot(uri=ODM.pageRefs, name="pageRefs", curie=ODM.curie('pageRefs'),
                   model_uri=ODM.pageRefs, domain=None, range=Optional[str])

slots.conditionOID = Slot(uri=ODM.conditionOID, name="conditionOID", curie=ODM.curie('conditionOID'),
                   model_uri=ODM.conditionOID, domain=None, range=Optional[Union[str, ConditionDefOID]])

slots.mandatory = Slot(uri=ODM.mandatory, name="mandatory", curie=ODM.curie('mandatory'),
                   model_uri=ODM.mandatory, domain=None, range=Optional[Union[str, "YesOrNo"]])

slots.priorFileOID = Slot(uri=ODM.priorFileOID, name="priorFileOID", curie=ODM.curie('priorFileOID'),
                   model_uri=ODM.priorFileOID, domain=None, range=Optional[Union[str, ODMFileMetadataFileOID]])

slots.status = Slot(uri=ODM.status, name="status", curie=ODM.curie('status'),
                   model_uri=ODM.status, domain=None, range=Optional[str])

slots.systemVersion = Slot(uri=ODM.systemVersion, name="systemVersion", curie=ODM.curie('systemVersion'),
                   model_uri=ODM.systemVersion, domain=None, range=Optional[str])

slots.isReferenceData = Slot(uri=ODM.isReferenceData, name="isReferenceData", curie=ODM.curie('isReferenceData'),
                   model_uri=ODM.isReferenceData, domain=None, range=Optional[Union[str, "YesOrNo"]])

slots.title = Slot(uri=ODM.title, name="title", curie=ODM.curie('title'),
                   model_uri=ODM.title, domain=None, range=Optional[Union[dict, Title]])

slots.mimeType = Slot(uri=ODM.mimeType, name="mimeType", curie=ODM.curie('mimeType'),
                   model_uri=ODM.mimeType, domain=None, range=Optional[str])

slots.partOfOrganizationOID = Slot(uri=ODM.partOfOrganizationOID, name="partOfOrganizationOID", curie=ODM.curie('partOfOrganizationOID'),
                   model_uri=ODM.partOfOrganizationOID, domain=None, range=Optional[Union[str, OrganizationOID]])

slots.organizationOID = Slot(uri=ODM.organizationOID, name="organizationOID", curie=ODM.curie('organizationOID'),
                   model_uri=ODM.organizationOID, domain=None, range=Optional[Union[str, OrganizationOID]])

slots.structure = Slot(uri=ODM.structure, name="structure", curie=ODM.curie('structure'),
                   model_uri=ODM.structure, domain=None, range=Optional[str])

slots.studyEventGroupOID = Slot(uri=ODM.studyEventGroupOID, name="studyEventGroupOID", curie=ODM.curie('studyEventGroupOID'),
                   model_uri=ODM.studyEventGroupOID, domain=None, range=Optional[Union[str, StudyEventGroupDefOID]])

slots.displayFormat = Slot(uri=ODM.displayFormat, name="displayFormat", curie=ODM.curie('displayFormat'),
                   model_uri=ODM.displayFormat, domain=None, range=Optional[str])

slots.lastUpdateDatetime = Slot(uri=ODM.lastUpdateDatetime, name="lastUpdateDatetime", curie=ODM.curie('lastUpdateDatetime'),
                   model_uri=ODM.lastUpdateDatetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.ID = Slot(uri=ODM.ID, name="ID", curie=ODM.curie('ID'),
                   model_uri=ODM.ID, domain=None, range=URIRef)

slots.timepointRelativeTarget = Slot(uri=ODM.timepointRelativeTarget, name="timepointRelativeTarget", curie=ODM.curie('timepointRelativeTarget'),
                   model_uri=ODM.timepointRelativeTarget, domain=None, range=Optional[str])

slots.altitude = Slot(uri=ODM.altitude, name="altitude", curie=ODM.curie('altitude'),
                   model_uri=ODM.altitude, domain=None, range=Optional[Decimal])

slots.studyOID = Slot(uri=ODM.studyOID, name="studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.studyOID, domain=None, range=Optional[Union[str, StudyOID]])

slots.library = Slot(uri=ODM.library, name="library", curie=ODM.curie('library'),
                   model_uri=ODM.library, domain=None, range=Optional[str])

slots.durationTarget = Slot(uri=ODM.durationTarget, name="durationTarget", curie=ODM.curie('durationTarget'),
                   model_uri=ODM.durationTarget, domain=None, range=Optional[str])

slots.path = Slot(uri=ODM.path, name="path", curie=ODM.curie('path'),
                   model_uri=ODM.path, domain=None, range=Optional[str])

slots.methodOID = Slot(uri=ODM.methodOID, name="methodOID", curie=ODM.curie('methodOID'),
                   model_uri=ODM.methodOID, domain=None, range=Optional[Union[str, MethodDefOID]])

slots.locationOID = Slot(uri=ODM.locationOID, name="locationOID", curie=ODM.curie('locationOID'),
                   model_uri=ODM.locationOID, domain=None, range=Optional[Union[str, LocationOID]])

slots.longitude = Slot(uri=ODM.longitude, name="longitude", curie=ODM.curie('longitude'),
                   model_uri=ODM.longitude, domain=None, range=Optional[Decimal])

slots.level = Slot(uri=ODM.level, name="level", curie=ODM.curie('level'),
                   model_uri=ODM.level, domain=None, range=Optional[str])

slots.successorOID = Slot(uri=ODM.successorOID, name="successorOID", curie=ODM.curie('successorOID'),
                   model_uri=ODM.successorOID, domain=None, range=Optional[str])

slots.system = Slot(uri=ODM.system, name="system", curie=ODM.curie('system'),
                   model_uri=ODM.system, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.orderNumber = Slot(uri=ODM.orderNumber, name="orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.orderNumber, domain=None, range=Optional[int])

slots.lastPage = Slot(uri=ODM.lastPage, name="lastPage", curie=ODM.curie('lastPage'),
                   model_uri=ODM.lastPage, domain=None, range=Optional[int])

slots.timepointPreWindow = Slot(uri=ODM.timepointPreWindow, name="timepointPreWindow", curie=ODM.curie('timepointPreWindow'),
                   model_uri=ODM.timepointPreWindow, domain=None, range=Optional[str])

slots.signatureOID = Slot(uri=ODM.signatureOID, name="signatureOID", curie=ODM.curie('signatureOID'),
                   model_uri=ODM.signatureOID, domain=None, range=Optional[Union[str, SignatureDefOID]])

slots.valueListOID = Slot(uri=ODM.valueListOID, name="valueListOID", curie=ODM.curie('valueListOID'),
                   model_uri=ODM.valueListOID, domain=None, range=Optional[Union[str, ValueListDefOID]])

slots.latitude = Slot(uri=ODM.latitude, name="latitude", curie=ODM.curie('latitude'),
                   model_uri=ODM.latitude, domain=None, range=Optional[Decimal])

slots.code = Slot(uri=ODM.code, name="code", curie=ODM.curie('code'),
                   model_uri=ODM.code, domain=None, range=Optional[Union[dict, Code]])

slots.dictionary = Slot(uri=ODM.dictionary, name="dictionary", curie=ODM.curie('dictionary'),
                   model_uri=ODM.dictionary, domain=None, range=Optional[str])

slots.collectionExceptionConditionOID = Slot(uri=ODM.collectionExceptionConditionOID, name="collectionExceptionConditionOID", curie=ODM.curie('collectionExceptionConditionOID'),
                   model_uri=ODM.collectionExceptionConditionOID, domain=None, range=Optional[Union[str, ConditionDefOID]])

slots.shortName = Slot(uri=ODM.shortName, name="shortName", curie=ODM.curie('shortName'),
                   model_uri=ODM.shortName, domain=None, range=Optional[str])

slots.effectiveDate = Slot(uri=ODM.effectiveDate, name="effectiveDate", curie=ODM.curie('effectiveDate'),
                   model_uri=ODM.effectiveDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.sourceOID = Slot(uri=ODM.sourceOID, name="sourceOID", curie=ODM.curie('sourceOID'),
                   model_uri=ODM.sourceOID, domain=None, range=Optional[str])

slots.studyEventRepeatKey = Slot(uri=ODM.studyEventRepeatKey, name="studyEventRepeatKey", curie=ODM.curie('studyEventRepeatKey'),
                   model_uri=ODM.studyEventRepeatKey, domain=None, range=Optional[str])

slots.publishingSet = Slot(uri=ODM.publishingSet, name="publishingSet", curie=ODM.curie('publishingSet'),
                   model_uri=ODM.publishingSet, domain=None, range=Optional[Union[str, "StandardPublishingSet"]])

slots.startOID = Slot(uri=ODM.startOID, name="startOID", curie=ODM.curie('startOID'),
                   model_uri=ODM.startOID, domain=None, range=Optional[str])

slots.repeating = Slot(uri=ODM.repeating, name="repeating", curie=ODM.curie('repeating'),
                   model_uri=ODM.repeating, domain=None, range=Optional[str])

slots.repeatingLimit = Slot(uri=ODM.repeatingLimit, name="repeatingLimit", curie=ODM.curie('repeatingLimit'),
                   model_uri=ODM.repeatingLimit, domain=None, range=Optional[int])

slots.itemGroupDataSeq = Slot(uri=ODM.itemGroupDataSeq, name="itemGroupDataSeq", curie=ODM.curie('itemGroupDataSeq'),
                   model_uri=ODM.itemGroupDataSeq, domain=None, range=Optional[int])

slots.studyEndPointOID = Slot(uri=ODM.studyEndPointOID, name="studyEndPointOID", curie=ODM.curie('studyEndPointOID'),
                   model_uri=ODM.studyEndPointOID, domain=None, range=Optional[Union[str, StudyEndPointOID]])

slots.editPoint = Slot(uri=ODM.editPoint, name="editPoint", curie=ODM.curie('editPoint'),
                   model_uri=ODM.editPoint, domain=None, range=Optional[Union[str, "EditPointType"]])

slots.parentClass = Slot(uri=ODM.parentClass, name="parentClass", curie=ODM.curie('parentClass'),
                   model_uri=ODM.parentClass, domain=None, range=Optional[str])

slots.userType = Slot(uri=ODM.userType, name="userType", curie=ODM.curie('userType'),
                   model_uri=ODM.userType, domain=None, range=Optional[Union[str, "UserType"]])

slots.metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.metaDataVersionOID, domain=None, range=Optional[Union[str, MetaDataVersionOID]])

slots.length = Slot(uri=ODM.length, name="length", curie=ODM.curie('length'),
                   model_uri=ODM.length, domain=None, range=Optional[int])

slots.seqNum = Slot(uri=ODM.seqNum, name="seqNum", curie=ODM.curie('seqNum'),
                   model_uri=ODM.seqNum, domain=None, range=Optional[int])

slots.value = Slot(uri=ODM.value, name="value", curie=ODM.curie('value'),
                   model_uri=ODM.value, domain=None, range=Optional[Union[dict, Value]])

slots.extendedValue = Slot(uri=ODM.extendedValue, name="extendedValue", curie=ODM.curie('extendedValue'),
                   model_uri=ODM.extendedValue, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.sourceSystem = Slot(uri=ODM.sourceSystem, name="sourceSystem", curie=ODM.curie('sourceSystem'),
                   model_uri=ODM.sourceSystem, domain=None, range=Optional[str])

slots.source = Slot(uri=ODM.source, name="source", curie=ODM.curie('source'),
                   model_uri=ODM.source, domain=None, range=Optional[str])

slots.itemGroupOID = Slot(uri=ODM.itemGroupOID, name="itemGroupOID", curie=ODM.curie('itemGroupOID'),
                   model_uri=ODM.itemGroupOID, domain=None, range=Optional[Union[str, ItemGroupDefOID]])

slots.preSpecifiedValue = Slot(uri=ODM.preSpecifiedValue, name="preSpecifiedValue", curie=ODM.curie('preSpecifiedValue'),
                   model_uri=ODM.preSpecifiedValue, domain=None, range=Optional[str])

slots.imageFileName = Slot(uri=ODM.imageFileName, name="imageFileName", curie=ODM.curie('imageFileName'),
                   model_uri=ODM.imageFileName, domain=None, range=Optional[URIorCURIE])

slots.asOfDateTime = Slot(uri=ODM.asOfDateTime, name="asOfDateTime", curie=ODM.curie('asOfDateTime'),
                   model_uri=ODM.asOfDateTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.itemGroupRepeatKey = Slot(uri=ODM.itemGroupRepeatKey, name="itemGroupRepeatKey", curie=ODM.curie('itemGroupRepeatKey'),
                   model_uri=ODM.itemGroupRepeatKey, domain=None, range=Optional[str])

slots.name = Slot(uri=ODM.name, name="name", curie=ODM.curie('name'),
                   model_uri=ODM.name, domain=None, range=Optional[str])

slots.itemOID = Slot(uri=ODM.itemOID, name="itemOID", curie=ODM.curie('itemOID'),
                   model_uri=ODM.itemOID, domain=None, range=Optional[Union[str, ItemDefOID]])

slots.armOID = Slot(uri=ODM.armOID, name="armOID", curie=ODM.curie('armOID'),
                   model_uri=ODM.armOID, domain=None, range=Optional[Union[str, ArmOID]])

slots.versionName = Slot(uri=ODM.versionName, name="versionName", curie=ODM.curie('versionName'),
                   model_uri=ODM.versionName, domain=None, range=Optional[str])

slots.subjectKey = Slot(uri=ODM.subjectKey, name="subjectKey", curie=ODM.curie('subjectKey'),
                   model_uri=ODM.subjectKey, domain=None, range=Optional[str])

slots.domain = Slot(uri=ODM.domain, name="domain", curie=ODM.curie('domain'),
                   model_uri=ODM.domain, domain=None, range=Optional[str])

slots.workflowOID = Slot(uri=ODM.workflowOID, name="workflowOID", curie=ODM.curie('workflowOID'),
                   model_uri=ODM.workflowOID, domain=None, range=Optional[Union[str, WorkflowDefOID]])

slots.codeListOID = Slot(uri=ODM.codeListOID, name="codeListOID", curie=ODM.curie('codeListOID'),
                   model_uri=ODM.codeListOID, domain=None, range=Optional[Union[str, CodeListOID]])

slots.role = Slot(uri=ODM.role, name="role", curie=ODM.curie('role'),
                   model_uri=ODM.role, domain=None, range=Optional[str])

slots.fileOID = Slot(uri=ODM.fileOID, name="fileOID", curie=ODM.curie('fileOID'),
                   model_uri=ODM.fileOID, domain=None, range=URIRef)

slots.protocolName = Slot(uri=ODM.protocolName, name="protocolName", curie=ODM.curie('protocolName'),
                   model_uri=ODM.protocolName, domain=None, range=Optional[str])

slots.roleCodeListOID = Slot(uri=ODM.roleCodeListOID, name="roleCodeListOID", curie=ODM.curie('roleCodeListOID'),
                   model_uri=ODM.roleCodeListOID, domain=None, range=Optional[Union[str, CodeListOID]])

slots.targetOID = Slot(uri=ODM.targetOID, name="targetOID", curie=ODM.curie('targetOID'),
                   model_uri=ODM.targetOID, domain=None, range=Optional[str])

slots.repeat = Slot(uri=ODM.repeat, name="repeat", curie=ODM.curie('repeat'),
                   model_uri=ODM.repeat, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.ref = Slot(uri=ODM.ref, name="ref", curie=ODM.curie('ref'),
                   model_uri=ODM.ref, domain=None, range=Optional[str])

slots.standardOID = Slot(uri=ODM.standardOID, name="standardOID", curie=ODM.curie('standardOID'),
                   model_uri=ODM.standardOID, domain=None, range=Optional[Union[str, StandardOID]])

slots.hasNoData = Slot(uri=ODM.hasNoData, name="hasNoData", curie=ODM.curie('hasNoData'),
                   model_uri=ODM.hasNoData, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.studyName = Slot(uri=ODM.studyName, name="studyName", curie=ODM.curie('studyName'),
                   model_uri=ODM.studyName, domain=None, range=Optional[str])

slots.unitsItemOID = Slot(uri=ODM.unitsItemOID, name="unitsItemOID", curie=ODM.curie('unitsItemOID'),
                   model_uri=ODM.unitsItemOID, domain=None, range=Optional[Union[str, ItemDefOID]])

slots.usedMethod = Slot(uri=ODM.usedMethod, name="usedMethod", curie=ODM.curie('usedMethod'),
                   model_uri=ODM.usedMethod, domain=None, range=Optional[Union[str, "YesOrNo"]])

slots.whereClauseOID = Slot(uri=ODM.whereClauseOID, name="whereClauseOID", curie=ODM.curie('whereClauseOID'),
                   model_uri=ODM.whereClauseOID, domain=None, range=Optional[Union[str, WhereClauseDefOID]])

slots.language = Slot(uri=ODM.language, name="language", curie=ODM.curie('language'),
                   model_uri=ODM.language, domain=None, range=Optional[str])

slots.keySequence = Slot(uri=ODM.keySequence, name="keySequence", curie=ODM.curie('keySequence'),
                   model_uri=ODM.keySequence, domain=None, range=Optional[int])

slots.creationDateTime = Slot(uri=ODM.creationDateTime, name="creationDateTime", curie=ODM.curie('creationDateTime'),
                   model_uri=ODM.creationDateTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.attribute = Slot(uri=ODM.attribute, name="attribute", curie=ODM.curie('attribute'),
                   model_uri=ODM.attribute, domain=None, range=Optional[str])

slots.archiveLocationID = Slot(uri=ODM.archiveLocationID, name="archiveLocationID", curie=ODM.curie('archiveLocationID'),
                   model_uri=ODM.archiveLocationID, domain=None, range=Optional[Union[str, LeafID]])

slots.versionID = Slot(uri=ODM.versionID, name="versionID", curie=ODM.curie('versionID'),
                   model_uri=ODM.versionID, domain=None, range=Optional[str])

slots.translatedText = Slot(uri=ODM.translatedText, name="translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.translatedText, domain=None, range=Optional[Union[dict, TranslatedText]])

slots.content = Slot(uri=ODM.content, name="content", curie=ODM.curie('content'),
                   model_uri=ODM.content, domain=None, range=Optional[str])

slots.description = Slot(uri=ODM.description, name="description", curie=ODM.curie('description'),
                   model_uri=ODM.description, domain=None, range=Optional[Union[dict, Description]])

slots.metaDataVersion = Slot(uri=ODM.metaDataVersion, name="metaDataVersion", curie=ODM.curie('metaDataVersion'),
                   model_uri=ODM.metaDataVersion, domain=None, range=Optional[Union[str, MetaDataVersionOID]])

slots.include = Slot(uri=ODM.include, name="include", curie=ODM.curie('include'),
                   model_uri=ODM.include, domain=None, range=Optional[Union[dict, Include]])

slots.standards = Slot(uri=ODM.standards, name="standards", curie=ODM.curie('standards'),
                   model_uri=ODM.standards, domain=None, range=Optional[Union[dict, Standards]])

slots.annotatedCRF = Slot(uri=ODM.annotatedCRF, name="annotatedCRF", curie=ODM.curie('annotatedCRF'),
                   model_uri=ODM.annotatedCRF, domain=None, range=Optional[Union[dict, AnnotatedCRF]])

slots.supplementalDoc = Slot(uri=ODM.supplementalDoc, name="supplementalDoc", curie=ODM.curie('supplementalDoc'),
                   model_uri=ODM.supplementalDoc, domain=None, range=Optional[Union[dict, SupplementalDoc]])

slots.valueListDef = Slot(uri=ODM.valueListDef, name="valueListDef", curie=ODM.curie('valueListDef'),
                   model_uri=ODM.valueListDef, domain=None, range=Optional[Union[str, ValueListDefOID]])

slots.whereClauseDef = Slot(uri=ODM.whereClauseDef, name="whereClauseDef", curie=ODM.curie('whereClauseDef'),
                   model_uri=ODM.whereClauseDef, domain=None, range=Optional[Union[str, WhereClauseDefOID]])

slots.protocol = Slot(uri=ODM.protocol, name="protocol", curie=ODM.curie('protocol'),
                   model_uri=ODM.protocol, domain=None, range=Optional[Union[dict, Protocol]])

slots.workflowDef = Slot(uri=ODM.workflowDef, name="workflowDef", curie=ODM.curie('workflowDef'),
                   model_uri=ODM.workflowDef, domain=None, range=Optional[Union[str, WorkflowDefOID]])

slots.studyEventGroupDef = Slot(uri=ODM.studyEventGroupDef, name="studyEventGroupDef", curie=ODM.curie('studyEventGroupDef'),
                   model_uri=ODM.studyEventGroupDef, domain=None, range=Optional[Union[str, StudyEventGroupDefOID]])

slots.studyEventDef = Slot(uri=ODM.studyEventDef, name="studyEventDef", curie=ODM.curie('studyEventDef'),
                   model_uri=ODM.studyEventDef, domain=None, range=Optional[Union[str, StudyEventDefOID]])

slots.itemGroupDef = Slot(uri=ODM.itemGroupDef, name="itemGroupDef", curie=ODM.curie('itemGroupDef'),
                   model_uri=ODM.itemGroupDef, domain=None, range=Optional[Union[str, ItemGroupDefOID]])

slots.itemDef = Slot(uri=ODM.itemDef, name="itemDef", curie=ODM.curie('itemDef'),
                   model_uri=ODM.itemDef, domain=None, range=Optional[Union[str, ItemDefOID]])

slots.codeList = Slot(uri=ODM.codeList, name="codeList", curie=ODM.curie('codeList'),
                   model_uri=ODM.codeList, domain=None, range=Optional[Union[str, CodeListOID]])

slots.conditionDef = Slot(uri=ODM.conditionDef, name="conditionDef", curie=ODM.curie('conditionDef'),
                   model_uri=ODM.conditionDef, domain=None, range=Optional[Union[str, ConditionDefOID]])

slots.methodDef = Slot(uri=ODM.methodDef, name="methodDef", curie=ODM.curie('methodDef'),
                   model_uri=ODM.methodDef, domain=None, range=Optional[Union[str, MethodDefOID]])

slots.commentDef = Slot(uri=ODM.commentDef, name="commentDef", curie=ODM.curie('commentDef'),
                   model_uri=ODM.commentDef, domain=None, range=Optional[Union[str, CommentDefOID]])

slots.leaf = Slot(uri=ODM.leaf, name="leaf", curie=ODM.curie('leaf'),
                   model_uri=ODM.leaf, domain=None, range=Optional[Union[str, LeafID]])

slots.pDFPageRef = Slot(uri=ODM.pDFPageRef, name="pDFPageRef", curie=ODM.curie('pDFPageRef'),
                   model_uri=ODM.pDFPageRef, domain=None, range=Optional[Union[dict, PDFPageRef]])

slots.standard = Slot(uri=ODM.standard, name="standard", curie=ODM.curie('standard'),
                   model_uri=ODM.standard, domain=None, range=Optional[Union[str, StandardOID]])

slots.documentRef = Slot(uri=ODM.documentRef, name="documentRef", curie=ODM.curie('documentRef'),
                   model_uri=ODM.documentRef, domain=None, range=Optional[Union[str, DocumentRefLeafID]])

slots.itemRef = Slot(uri=ODM.itemRef, name="itemRef", curie=ODM.curie('itemRef'),
                   model_uri=ODM.itemRef, domain=None, range=Optional[Union[dict, ItemRef]])

slots.rangeCheck = Slot(uri=ODM.rangeCheck, name="rangeCheck", curie=ODM.curie('rangeCheck'),
                   model_uri=ODM.rangeCheck, domain=None, range=Optional[Union[dict, RangeCheck]])

slots.workflowRef = Slot(uri=ODM.workflowRef, name="workflowRef", curie=ODM.curie('workflowRef'),
                   model_uri=ODM.workflowRef, domain=None, range=Optional[Union[dict, WorkflowRef]])

slots.coding = Slot(uri=ODM.coding, name="coding", curie=ODM.curie('coding'),
                   model_uri=ODM.coding, domain=None, range=Optional[Union[dict, Coding]])

slots.studyEventGroupRef = Slot(uri=ODM.studyEventGroupRef, name="studyEventGroupRef", curie=ODM.curie('studyEventGroupRef'),
                   model_uri=ODM.studyEventGroupRef, domain=None, range=Optional[Union[dict, StudyEventGroupRef]])

slots.studyEventRef = Slot(uri=ODM.studyEventRef, name="studyEventRef", curie=ODM.curie('studyEventRef'),
                   model_uri=ODM.studyEventRef, domain=None, range=Optional[Union[dict, StudyEventRef]])

slots.itemGroupRef = Slot(uri=ODM.itemGroupRef, name="itemGroupRef", curie=ODM.curie('itemGroupRef'),
                   model_uri=ODM.itemGroupRef, domain=None, range=Optional[Union[dict, ItemGroupRef]])

slots.alias = Slot(uri=ODM.alias, name="alias", curie=ODM.curie('alias'),
                   model_uri=ODM.alias, domain=None, range=Optional[Union[dict, Alias]])

slots.itemGroupClass = Slot(uri=ODM.itemGroupClass, name="itemGroupClass", curie=ODM.curie('itemGroupClass'),
                   model_uri=ODM.itemGroupClass, domain=None, range=Optional[Union[dict, Class]])

slots.origin = Slot(uri=ODM.origin, name="origin", curie=ODM.curie('origin'),
                   model_uri=ODM.origin, domain=None, range=Optional[Union[dict, Origin]])

slots.subClass = Slot(uri=ODM.subClass, name="subClass", curie=ODM.curie('subClass'),
                   model_uri=ODM.subClass, domain=None, range=Optional[Union[dict, SubClass]])

slots.whereClauseRef = Slot(uri=ODM.whereClauseRef, name="whereClauseRef", curie=ODM.curie('whereClauseRef'),
                   model_uri=ODM.whereClauseRef, domain=None, range=Optional[Union[dict, WhereClauseRef]])

slots.sourceItems = Slot(uri=ODM.sourceItems, name="sourceItems", curie=ODM.curie('sourceItems'),
                   model_uri=ODM.sourceItems, domain=None, range=Optional[Union[dict, SourceItems]])

slots.sourceItem = Slot(uri=ODM.sourceItem, name="sourceItem", curie=ODM.curie('sourceItem'),
                   model_uri=ODM.sourceItem, domain=None, range=Optional[Union[dict, SourceItem]])

slots.resource = Slot(uri=ODM.resource, name="resource", curie=ODM.curie('resource'),
                   model_uri=ODM.resource, domain=None, range=Optional[Union[dict, Resource]])

slots.selection = Slot(uri=ODM.selection, name="selection", curie=ODM.curie('selection'),
                   model_uri=ODM.selection, domain=None, range=Optional[Union[dict, Selection]])

slots.question = Slot(uri=ODM.question, name="question", curie=ODM.curie('question'),
                   model_uri=ODM.question, domain=None, range=Optional[Union[dict, Question]])

slots.prompt = Slot(uri=ODM.prompt, name="prompt", curie=ODM.curie('prompt'),
                   model_uri=ODM.prompt, domain=None, range=Optional[Union[dict, Prompt]])

slots.cRFCompletionInstructions = Slot(uri=ODM.cRFCompletionInstructions, name="cRFCompletionInstructions", curie=ODM.curie('cRFCompletionInstructions'),
                   model_uri=ODM.cRFCompletionInstructions, domain=None, range=Optional[Union[dict, CRFCompletionInstructions]])

slots.implementationNotes = Slot(uri=ODM.implementationNotes, name="implementationNotes", curie=ODM.curie('implementationNotes'),
                   model_uri=ODM.implementationNotes, domain=None, range=Optional[Union[dict, ImplementationNotes]])

slots.cDISCNotes = Slot(uri=ODM.cDISCNotes, name="cDISCNotes", curie=ODM.curie('cDISCNotes'),
                   model_uri=ODM.cDISCNotes, domain=None, range=Optional[Union[dict, CDISCNotes]])

slots.codeListRef = Slot(uri=ODM.codeListRef, name="codeListRef", curie=ODM.curie('codeListRef'),
                   model_uri=ODM.codeListRef, domain=None, range=Optional[Union[dict, CodeListRef]])

slots.valueListRef = Slot(uri=ODM.valueListRef, name="valueListRef", curie=ODM.curie('valueListRef'),
                   model_uri=ODM.valueListRef, domain=None, range=Optional[Union[dict, ValueListRef]])

slots.errorMessage = Slot(uri=ODM.errorMessage, name="errorMessage", curie=ODM.curie('errorMessage'),
                   model_uri=ODM.errorMessage, domain=None, range=Optional[Union[dict, ErrorMessage]])

slots.methodSignature = Slot(uri=ODM.methodSignature, name="methodSignature", curie=ODM.curie('methodSignature'),
                   model_uri=ODM.methodSignature, domain=None, range=Optional[Union[dict, MethodSignature]])

slots.formalExpression = Slot(uri=ODM.formalExpression, name="formalExpression", curie=ODM.curie('formalExpression'),
                   model_uri=ODM.formalExpression, domain=None, range=Optional[Union[dict, FormalExpression]])

slots.checkValue = Slot(uri=ODM.checkValue, name="checkValue", curie=ODM.curie('checkValue'),
                   model_uri=ODM.checkValue, domain=None, range=Optional[Union[dict, CheckValue]])

slots.codeListItem = Slot(uri=ODM.codeListItem, name="codeListItem", curie=ODM.curie('codeListItem'),
                   model_uri=ODM.codeListItem, domain=None, range=Optional[Union[dict, CodeListItem]])

slots.decode = Slot(uri=ODM.decode, name="decode", curie=ODM.curie('decode'),
                   model_uri=ODM.decode, domain=None, range=Optional[Union[dict, Decode]])

slots.parameter = Slot(uri=ODM.parameter, name="parameter", curie=ODM.curie('parameter'),
                   model_uri=ODM.parameter, domain=None, range=Optional[Union[dict, Parameter]])

slots.returnValue = Slot(uri=ODM.returnValue, name="returnValue", curie=ODM.curie('returnValue'),
                   model_uri=ODM.returnValue, domain=None, range=Optional[Union[dict, ReturnValue]])

slots.externalCodeLib = Slot(uri=ODM.externalCodeLib, name="externalCodeLib", curie=ODM.curie('externalCodeLib'),
                   model_uri=ODM.externalCodeLib, domain=None, range=Optional[Union[dict, ExternalCodeLib]])

slots.studySummary = Slot(uri=ODM.studySummary, name="studySummary", curie=ODM.curie('studySummary'),
                   model_uri=ODM.studySummary, domain=None, range=Optional[Union[dict, StudySummary]])

slots.studyStructure = Slot(uri=ODM.studyStructure, name="studyStructure", curie=ODM.curie('studyStructure'),
                   model_uri=ODM.studyStructure, domain=None, range=Optional[Union[dict, StudyStructure]])

slots.trialPhase = Slot(uri=ODM.trialPhase, name="trialPhase", curie=ODM.curie('trialPhase'),
                   model_uri=ODM.trialPhase, domain=None, range=Optional[Union[dict, TrialPhase]])

slots.studyTimings = Slot(uri=ODM.studyTimings, name="studyTimings", curie=ODM.curie('studyTimings'),
                   model_uri=ODM.studyTimings, domain=None, range=Optional[Union[dict, StudyTimings]])

slots.studyIndications = Slot(uri=ODM.studyIndications, name="studyIndications", curie=ODM.curie('studyIndications'),
                   model_uri=ODM.studyIndications, domain=None, range=Optional[Union[dict, StudyIndications]])

slots.studyInterventions = Slot(uri=ODM.studyInterventions, name="studyInterventions", curie=ODM.curie('studyInterventions'),
                   model_uri=ODM.studyInterventions, domain=None, range=Optional[Union[dict, StudyInterventions]])

slots.studyObjectives = Slot(uri=ODM.studyObjectives, name="studyObjectives", curie=ODM.curie('studyObjectives'),
                   model_uri=ODM.studyObjectives, domain=None, range=Optional[Union[dict, StudyObjectives]])

slots.studyEndPoints = Slot(uri=ODM.studyEndPoints, name="studyEndPoints", curie=ODM.curie('studyEndPoints'),
                   model_uri=ODM.studyEndPoints, domain=None, range=Optional[Union[dict, StudyEndPoints]])

slots.studyTargetPopulation = Slot(uri=ODM.studyTargetPopulation, name="studyTargetPopulation", curie=ODM.curie('studyTargetPopulation'),
                   model_uri=ODM.studyTargetPopulation, domain=None, range=Optional[Union[str, StudyTargetPopulationOID]])

slots.studyEstimands = Slot(uri=ODM.studyEstimands, name="studyEstimands", curie=ODM.curie('studyEstimands'),
                   model_uri=ODM.studyEstimands, domain=None, range=Optional[Union[dict, StudyEstimands]])

slots.inclusionExclusionCriteria = Slot(uri=ODM.inclusionExclusionCriteria, name="inclusionExclusionCriteria", curie=ODM.curie('inclusionExclusionCriteria'),
                   model_uri=ODM.inclusionExclusionCriteria, domain=None, range=Optional[Union[dict, InclusionExclusionCriteria]])

slots.arm = Slot(uri=ODM.arm, name="arm", curie=ODM.curie('arm'),
                   model_uri=ODM.arm, domain=None, range=Optional[Union[str, ArmOID]])

slots.epoch = Slot(uri=ODM.epoch, name="epoch", curie=ODM.curie('epoch'),
                   model_uri=ODM.epoch, domain=None, range=Optional[Union[str, EpochOID]])

slots.studyIndication = Slot(uri=ODM.studyIndication, name="studyIndication", curie=ODM.curie('studyIndication'),
                   model_uri=ODM.studyIndication, domain=None, range=Optional[Union[str, StudyIndicationOID]])

slots.studyIntervention = Slot(uri=ODM.studyIntervention, name="studyIntervention", curie=ODM.curie('studyIntervention'),
                   model_uri=ODM.studyIntervention, domain=None, range=Optional[Union[str, StudyInterventionOID]])

slots.studyObjective = Slot(uri=ODM.studyObjective, name="studyObjective", curie=ODM.curie('studyObjective'),
                   model_uri=ODM.studyObjective, domain=None, range=Optional[Union[str, StudyObjectiveOID]])

slots.studyEndPointRef = Slot(uri=ODM.studyEndPointRef, name="studyEndPointRef", curie=ODM.curie('studyEndPointRef'),
                   model_uri=ODM.studyEndPointRef, domain=None, range=Optional[Union[dict, StudyEndPointRef]])

slots.studyEndPoint = Slot(uri=ODM.studyEndPoint, name="studyEndPoint", curie=ODM.curie('studyEndPoint'),
                   model_uri=ODM.studyEndPoint, domain=None, range=Optional[Union[str, StudyEndPointOID]])

slots.studyEstimand = Slot(uri=ODM.studyEstimand, name="studyEstimand", curie=ODM.curie('studyEstimand'),
                   model_uri=ODM.studyEstimand, domain=None, range=Optional[Union[str, StudyEstimandOID]])

slots.studyTargetPopulationRef = Slot(uri=ODM.studyTargetPopulationRef, name="studyTargetPopulationRef", curie=ODM.curie('studyTargetPopulationRef'),
                   model_uri=ODM.studyTargetPopulationRef, domain=None, range=Optional[Union[dict, StudyTargetPopulationRef]])

slots.studyInterventionRef = Slot(uri=ODM.studyInterventionRef, name="studyInterventionRef", curie=ODM.curie('studyInterventionRef'),
                   model_uri=ODM.studyInterventionRef, domain=None, range=Optional[Union[dict, StudyInterventionRef]])

slots.intercurrentEvent = Slot(uri=ODM.intercurrentEvent, name="intercurrentEvent", curie=ODM.curie('intercurrentEvent'),
                   model_uri=ODM.intercurrentEvent, domain=None, range=Optional[Union[dict, IntercurrentEvent]])

slots.summaryMeasure = Slot(uri=ODM.summaryMeasure, name="summaryMeasure", curie=ODM.curie('summaryMeasure'),
                   model_uri=ODM.summaryMeasure, domain=None, range=Optional[Union[dict, SummaryMeasure]])

slots.inclusionCriteria = Slot(uri=ODM.inclusionCriteria, name="inclusionCriteria", curie=ODM.curie('inclusionCriteria'),
                   model_uri=ODM.inclusionCriteria, domain=None, range=Optional[Union[dict, InclusionCriteria]])

slots.exclusionCriteria = Slot(uri=ODM.exclusionCriteria, name="exclusionCriteria", curie=ODM.curie('exclusionCriteria'),
                   model_uri=ODM.exclusionCriteria, domain=None, range=Optional[Union[dict, ExclusionCriteria]])

slots.criterion = Slot(uri=ODM.criterion, name="criterion", curie=ODM.curie('criterion'),
                   model_uri=ODM.criterion, domain=None, range=Optional[Union[str, CriterionOID]])

slots.studyParameter = Slot(uri=ODM.studyParameter, name="studyParameter", curie=ODM.curie('studyParameter'),
                   model_uri=ODM.studyParameter, domain=None, range=Optional[Union[str, StudyParameterOID]])

slots.parameterValue = Slot(uri=ODM.parameterValue, name="parameterValue", curie=ODM.curie('parameterValue'),
                   model_uri=ODM.parameterValue, domain=None, range=Optional[Union[dict, ParameterValue]])

slots.studyTiming = Slot(uri=ODM.studyTiming, name="studyTiming", curie=ODM.curie('studyTiming'),
                   model_uri=ODM.studyTiming, domain=None, range=Optional[Union[str, StudyTimingOID]])

slots.absoluteTimingConstraint = Slot(uri=ODM.absoluteTimingConstraint, name="absoluteTimingConstraint", curie=ODM.curie('absoluteTimingConstraint'),
                   model_uri=ODM.absoluteTimingConstraint, domain=None, range=Optional[Union[str, AbsoluteTimingConstraintOID]])

slots.relativeTimingConstraint = Slot(uri=ODM.relativeTimingConstraint, name="relativeTimingConstraint", curie=ODM.curie('relativeTimingConstraint'),
                   model_uri=ODM.relativeTimingConstraint, domain=None, range=Optional[Union[str, RelativeTimingConstraintOID]])

slots.transitionTimingConstraint = Slot(uri=ODM.transitionTimingConstraint, name="transitionTimingConstraint", curie=ODM.curie('transitionTimingConstraint'),
                   model_uri=ODM.transitionTimingConstraint, domain=None, range=Optional[Union[str, TransitionTimingConstraintOID]])

slots.durationTimingConstraint = Slot(uri=ODM.durationTimingConstraint, name="durationTimingConstraint", curie=ODM.curie('durationTimingConstraint'),
                   model_uri=ODM.durationTimingConstraint, domain=None, range=Optional[Union[str, DurationTimingConstraintOID]])

slots.workflowStart = Slot(uri=ODM.workflowStart, name="workflowStart", curie=ODM.curie('workflowStart'),
                   model_uri=ODM.workflowStart, domain=None, range=Optional[Union[dict, WorkflowStart]])

slots.workflowEnd = Slot(uri=ODM.workflowEnd, name="workflowEnd", curie=ODM.curie('workflowEnd'),
                   model_uri=ODM.workflowEnd, domain=None, range=Optional[Union[dict, WorkflowEnd]])

slots.transition = Slot(uri=ODM.transition, name="transition", curie=ODM.curie('transition'),
                   model_uri=ODM.transition, domain=None, range=Optional[Union[str, TransitionOID]])

slots.branching = Slot(uri=ODM.branching, name="branching", curie=ODM.curie('branching'),
                   model_uri=ODM.branching, domain=None, range=Optional[Union[str, BranchingOID]])

slots.targetTransition = Slot(uri=ODM.targetTransition, name="targetTransition", curie=ODM.curie('targetTransition'),
                   model_uri=ODM.targetTransition, domain=None, range=Optional[Union[dict, TargetTransition]])

slots.defaultTransition = Slot(uri=ODM.defaultTransition, name="defaultTransition", curie=ODM.curie('defaultTransition'),
                   model_uri=ODM.defaultTransition, domain=None, range=Optional[Union[dict, DefaultTransition]])

slots.user = Slot(uri=ODM.user, name="user", curie=ODM.curie('user'),
                   model_uri=ODM.user, domain=None, range=Optional[Union[str, UserOID]])

slots.organization = Slot(uri=ODM.organization, name="organization", curie=ODM.curie('organization'),
                   model_uri=ODM.organization, domain=None, range=Optional[Union[str, OrganizationOID]])

slots.location = Slot(uri=ODM.location, name="location", curie=ODM.curie('location'),
                   model_uri=ODM.location, domain=None, range=Optional[Union[str, LocationOID]])

slots.signatureDef = Slot(uri=ODM.signatureDef, name="signatureDef", curie=ODM.curie('signatureDef'),
                   model_uri=ODM.signatureDef, domain=None, range=Optional[Union[str, SignatureDefOID]])

slots.userName = Slot(uri=ODM.userName, name="userName", curie=ODM.curie('userName'),
                   model_uri=ODM.userName, domain=None, range=Optional[Union[dict, UserName]])

slots.prefix = Slot(uri=ODM.prefix, name="prefix", curie=ODM.curie('prefix'),
                   model_uri=ODM.prefix, domain=None, range=Optional[Union[dict, Prefix]])

slots.suffix = Slot(uri=ODM.suffix, name="suffix", curie=ODM.curie('suffix'),
                   model_uri=ODM.suffix, domain=None, range=Optional[Union[dict, Suffix]])

slots.fullName = Slot(uri=ODM.fullName, name="fullName", curie=ODM.curie('fullName'),
                   model_uri=ODM.fullName, domain=None, range=Optional[Union[dict, FullName]])

slots.givenName = Slot(uri=ODM.givenName, name="givenName", curie=ODM.curie('givenName'),
                   model_uri=ODM.givenName, domain=None, range=Optional[Union[dict, GivenName]])

slots.familyName = Slot(uri=ODM.familyName, name="familyName", curie=ODM.curie('familyName'),
                   model_uri=ODM.familyName, domain=None, range=Optional[Union[dict, FamilyName]])

slots.image = Slot(uri=ODM.image, name="image", curie=ODM.curie('image'),
                   model_uri=ODM.image, domain=None, range=Optional[Union[dict, Image]])

slots.address = Slot(uri=ODM.address, name="address", curie=ODM.curie('address'),
                   model_uri=ODM.address, domain=None, range=Optional[Union[dict, Address]])

slots.telecom = Slot(uri=ODM.telecom, name="telecom", curie=ODM.curie('telecom'),
                   model_uri=ODM.telecom, domain=None, range=Optional[Union[dict, Telecom]])

slots.metaDataVersionRef = Slot(uri=ODM.metaDataVersionRef, name="metaDataVersionRef", curie=ODM.curie('metaDataVersionRef'),
                   model_uri=ODM.metaDataVersionRef, domain=None, range=Optional[Union[dict, MetaDataVersionRef]])

slots.query = Slot(uri=ODM.query, name="query", curie=ODM.curie('query'),
                   model_uri=ODM.query, domain=None, range=Optional[Union[str, QueryOID]])

slots.streetName = Slot(uri=ODM.streetName, name="streetName", curie=ODM.curie('streetName'),
                   model_uri=ODM.streetName, domain=None, range=Optional[Union[dict, StreetName]])

slots.houseNumber = Slot(uri=ODM.houseNumber, name="houseNumber", curie=ODM.curie('houseNumber'),
                   model_uri=ODM.houseNumber, domain=None, range=Optional[Union[dict, HouseNumber]])

slots.city = Slot(uri=ODM.city, name="city", curie=ODM.curie('city'),
                   model_uri=ODM.city, domain=None, range=Optional[Union[dict, City]])

slots.stateProv = Slot(uri=ODM.stateProv, name="stateProv", curie=ODM.curie('stateProv'),
                   model_uri=ODM.stateProv, domain=None, range=Optional[Union[dict, StateProv]])

slots.country = Slot(uri=ODM.country, name="country", curie=ODM.curie('country'),
                   model_uri=ODM.country, domain=None, range=Optional[Union[dict, Country]])

slots.postalCode = Slot(uri=ODM.postalCode, name="postalCode", curie=ODM.curie('postalCode'),
                   model_uri=ODM.postalCode, domain=None, range=Optional[Union[dict, PostalCode]])

slots.geoPosition = Slot(uri=ODM.geoPosition, name="geoPosition", curie=ODM.curie('geoPosition'),
                   model_uri=ODM.geoPosition, domain=None, range=Optional[Union[dict, GeoPosition]])

slots.otherText = Slot(uri=ODM.otherText, name="otherText", curie=ODM.curie('otherText'),
                   model_uri=ODM.otherText, domain=None, range=Optional[Union[dict, OtherText]])

slots.meaning = Slot(uri=ODM.meaning, name="meaning", curie=ODM.curie('meaning'),
                   model_uri=ODM.meaning, domain=None, range=Optional[Union[dict, Meaning]])

slots.legalReason = Slot(uri=ODM.legalReason, name="legalReason", curie=ODM.curie('legalReason'),
                   model_uri=ODM.legalReason, domain=None, range=Optional[Union[dict, LegalReason]])

slots.itemGroupData = Slot(uri=ODM.itemGroupData, name="itemGroupData", curie=ODM.curie('itemGroupData'),
                   model_uri=ODM.itemGroupData, domain=None, range=Optional[Union[dict, ItemGroupData]])

slots.auditRecord = Slot(uri=ODM.auditRecord, name="auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.auditRecord, domain=None, range=Optional[Union[dict, AuditRecord]])

slots.signature = Slot(uri=ODM.signature, name="signature", curie=ODM.curie('signature'),
                   model_uri=ODM.signature, domain=None, range=Optional[Union[str, SignatureID]])

slots.annotation = Slot(uri=ODM.annotation, name="annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.annotation, domain=None, range=Optional[Union[str, AnnotationID]])

slots.subjectData = Slot(uri=ODM.subjectData, name="subjectData", curie=ODM.curie('subjectData'),
                   model_uri=ODM.subjectData, domain=None, range=Optional[Union[dict, SubjectData]])

slots.investigatorRef = Slot(uri=ODM.investigatorRef, name="investigatorRef", curie=ODM.curie('investigatorRef'),
                   model_uri=ODM.investigatorRef, domain=None, range=Optional[Union[dict, InvestigatorRef]])

slots.siteRef = Slot(uri=ODM.siteRef, name="siteRef", curie=ODM.curie('siteRef'),
                   model_uri=ODM.siteRef, domain=None, range=Optional[Union[dict, SiteRef]])

slots.studyEventData = Slot(uri=ODM.studyEventData, name="studyEventData", curie=ODM.curie('studyEventData'),
                   model_uri=ODM.studyEventData, domain=None, range=Optional[Union[dict, StudyEventData]])

slots.itemData = Slot(uri=ODM.itemData, name="itemData", curie=ODM.curie('itemData'),
                   model_uri=ODM.itemData, domain=None, range=Optional[Union[dict, ItemData]])

slots.userRef = Slot(uri=ODM.userRef, name="userRef", curie=ODM.curie('userRef'),
                   model_uri=ODM.userRef, domain=None, range=Optional[Union[dict, UserRef]])

slots.locationRef = Slot(uri=ODM.locationRef, name="locationRef", curie=ODM.curie('locationRef'),
                   model_uri=ODM.locationRef, domain=None, range=Optional[Union[dict, LocationRef]])

slots.dateTimeStamp = Slot(uri=ODM.dateTimeStamp, name="dateTimeStamp", curie=ODM.curie('dateTimeStamp'),
                   model_uri=ODM.dateTimeStamp, domain=None, range=Optional[Union[dict, DateTimeStamp]])

slots.reasonForChange = Slot(uri=ODM.reasonForChange, name="reasonForChange", curie=ODM.curie('reasonForChange'),
                   model_uri=ODM.reasonForChange, domain=None, range=Optional[Union[dict, ReasonForChange]])

slots.sourceID = Slot(uri=ODM.sourceID, name="sourceID", curie=ODM.curie('sourceID'),
                   model_uri=ODM.sourceID, domain=None, range=Optional[Union[dict, SourceID]])

slots.signatureRef = Slot(uri=ODM.signatureRef, name="signatureRef", curie=ODM.curie('signatureRef'),
                   model_uri=ODM.signatureRef, domain=None, range=Optional[Union[dict, SignatureRef]])

slots.study = Slot(uri=ODM.study, name="study", curie=ODM.curie('study'),
                   model_uri=ODM.study, domain=None, range=Optional[Union[str, StudyOID]])

slots.adminData = Slot(uri=ODM.adminData, name="adminData", curie=ODM.curie('adminData'),
                   model_uri=ODM.adminData, domain=None, range=Optional[Union[dict, AdminData]])

slots.referenceData = Slot(uri=ODM.referenceData, name="referenceData", curie=ODM.curie('referenceData'),
                   model_uri=ODM.referenceData, domain=None, range=Optional[Union[dict, ReferenceData]])

slots.clinicalData = Slot(uri=ODM.clinicalData, name="clinicalData", curie=ODM.curie('clinicalData'),
                   model_uri=ODM.clinicalData, domain=None, range=Optional[Union[dict, ClinicalData]])

slots.association = Slot(uri=ODM.association, name="association", curie=ODM.curie('association'),
                   model_uri=ODM.association, domain=None, range=Optional[Union[dict, Association]])

slots.keySet = Slot(uri=ODM.keySet, name="keySet", curie=ODM.curie('keySet'),
                   model_uri=ODM.keySet, domain=None, range=Optional[Union[dict, KeySet]])

slots.comment = Slot(uri=ODM.comment, name="comment", curie=ODM.curie('comment'),
                   model_uri=ODM.comment, domain=None, range=Optional[Union[dict, Comment]])

slots.flag = Slot(uri=ODM.flag, name="flag", curie=ODM.curie('flag'),
                   model_uri=ODM.flag, domain=None, range=Optional[Union[dict, Flag]])

slots.flagValue = Slot(uri=ODM.flagValue, name="flagValue", curie=ODM.curie('flagValue'),
                   model_uri=ODM.flagValue, domain=None, range=Optional[Union[dict, FlagValue]])

slots.flagType = Slot(uri=ODM.flagType, name="flagType", curie=ODM.curie('flagType'),
                   model_uri=ODM.flagType, domain=None, range=Optional[Union[dict, FlagType]])

slots.Alias_context = Slot(uri=ODM.context, name="Alias_context", curie=ODM.curie('context'),
                   model_uri=ODM.Alias_context, domain=Alias, range=str)

slots.Alias_name = Slot(uri=ODM.name, name="Alias_name", curie=ODM.curie('name'),
                   model_uri=ODM.Alias_name, domain=Alias, range=str)

slots.Description_translatedText = Slot(uri=ODM.translatedText, name="Description_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.Description_translatedText, domain=Description, range=Optional[Union[Union[dict, "TranslatedText"], List[Union[dict, "TranslatedText"]]]])

slots.TranslatedText_language = Slot(uri=ODM.language, name="TranslatedText_language", curie=ODM.curie('language'),
                   model_uri=ODM.TranslatedText_language, domain=TranslatedText, range=Optional[str])

slots.TranslatedText_type = Slot(uri=ODM.type, name="TranslatedText_type", curie=ODM.curie('type'),
                   model_uri=ODM.TranslatedText_type, domain=TranslatedText, range=str)

slots.TranslatedText_content = Slot(uri=ODM.content, name="TranslatedText_content", curie=ODM.curie('content'),
                   model_uri=ODM.TranslatedText_content, domain=TranslatedText, range=Optional[str])

slots.Study_OID = Slot(uri=ODM.OID, name="Study_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Study_OID, domain=Study, range=Union[str, StudyOID])

slots.Study_studyName = Slot(uri=ODM.studyName, name="Study_studyName", curie=ODM.curie('studyName'),
                   model_uri=ODM.Study_studyName, domain=Study, range=str)

slots.Study_protocolName = Slot(uri=ODM.protocolName, name="Study_protocolName", curie=ODM.curie('protocolName'),
                   model_uri=ODM.Study_protocolName, domain=Study, range=str)

slots.Study_versionID = Slot(uri=ODM.versionID, name="Study_versionID", curie=ODM.curie('versionID'),
                   model_uri=ODM.Study_versionID, domain=Study, range=Optional[str])

slots.Study_versionName = Slot(uri=ODM.versionName, name="Study_versionName", curie=ODM.curie('versionName'),
                   model_uri=ODM.Study_versionName, domain=Study, range=Optional[str])

slots.Study_status = Slot(uri=ODM.status, name="Study_status", curie=ODM.curie('status'),
                   model_uri=ODM.Study_status, domain=Study, range=Optional[str])

slots.Study_description = Slot(uri=ODM.description, name="Study_description", curie=ODM.curie('description'),
                   model_uri=ODM.Study_description, domain=Study, range=Optional[Union[dict, Description]])

slots.Study_metaDataVersion = Slot(uri=ODM.metaDataVersion, name="Study_metaDataVersion", curie=ODM.curie('metaDataVersion'),
                   model_uri=ODM.Study_metaDataVersion, domain=Study, range=Optional[Union[Dict[Union[str, MetaDataVersionOID], Union[dict, "MetaDataVersion"]], List[Union[dict, "MetaDataVersion"]]]])

slots.MetaDataVersion_OID = Slot(uri=ODM.OID, name="MetaDataVersion_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.MetaDataVersion_OID, domain=MetaDataVersion, range=Union[str, MetaDataVersionOID])

slots.MetaDataVersion_name = Slot(uri=ODM.name, name="MetaDataVersion_name", curie=ODM.curie('name'),
                   model_uri=ODM.MetaDataVersion_name, domain=MetaDataVersion, range=str)

slots.MetaDataVersion_commentOID = Slot(uri=ODM.commentOID, name="MetaDataVersion_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.MetaDataVersion_commentOID, domain=MetaDataVersion, range=Optional[Union[str, CommentDefOID]])

slots.MetaDataVersion_description = Slot(uri=ODM.description, name="MetaDataVersion_description", curie=ODM.curie('description'),
                   model_uri=ODM.MetaDataVersion_description, domain=MetaDataVersion, range=Optional[Union[dict, Description]])

slots.MetaDataVersion_include = Slot(uri=ODM.include, name="MetaDataVersion_include", curie=ODM.curie('include'),
                   model_uri=ODM.MetaDataVersion_include, domain=MetaDataVersion, range=Optional[Union[dict, "Include"]])

slots.MetaDataVersion_standards = Slot(uri=ODM.standards, name="MetaDataVersion_standards", curie=ODM.curie('standards'),
                   model_uri=ODM.MetaDataVersion_standards, domain=MetaDataVersion, range=Optional[Union[dict, "Standards"]])

slots.MetaDataVersion_annotatedCRF = Slot(uri=ODM.annotatedCRF, name="MetaDataVersion_annotatedCRF", curie=ODM.curie('annotatedCRF'),
                   model_uri=ODM.MetaDataVersion_annotatedCRF, domain=MetaDataVersion, range=Optional[Union[dict, "AnnotatedCRF"]])

slots.MetaDataVersion_supplementalDoc = Slot(uri=ODM.supplementalDoc, name="MetaDataVersion_supplementalDoc", curie=ODM.curie('supplementalDoc'),
                   model_uri=ODM.MetaDataVersion_supplementalDoc, domain=MetaDataVersion, range=Optional[Union[dict, "SupplementalDoc"]])

slots.MetaDataVersion_valueListDef = Slot(uri=ODM.valueListDef, name="MetaDataVersion_valueListDef", curie=ODM.curie('valueListDef'),
                   model_uri=ODM.MetaDataVersion_valueListDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ValueListDefOID], Union[dict, "ValueListDef"]], List[Union[dict, "ValueListDef"]]]])

slots.MetaDataVersion_whereClauseDef = Slot(uri=ODM.whereClauseDef, name="MetaDataVersion_whereClauseDef", curie=ODM.curie('whereClauseDef'),
                   model_uri=ODM.MetaDataVersion_whereClauseDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, WhereClauseDefOID], Union[dict, "WhereClauseDef"]], List[Union[dict, "WhereClauseDef"]]]])

slots.MetaDataVersion_protocol = Slot(uri=ODM.protocol, name="MetaDataVersion_protocol", curie=ODM.curie('protocol'),
                   model_uri=ODM.MetaDataVersion_protocol, domain=MetaDataVersion, range=Optional[Union[dict, "Protocol"]])

slots.MetaDataVersion_workflowDef = Slot(uri=ODM.workflowDef, name="MetaDataVersion_workflowDef", curie=ODM.curie('workflowDef'),
                   model_uri=ODM.MetaDataVersion_workflowDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, WorkflowDefOID], Union[dict, "WorkflowDef"]], List[Union[dict, "WorkflowDef"]]]])

slots.MetaDataVersion_studyEventGroupDef = Slot(uri=ODM.studyEventGroupDef, name="MetaDataVersion_studyEventGroupDef", curie=ODM.curie('studyEventGroupDef'),
                   model_uri=ODM.MetaDataVersion_studyEventGroupDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, StudyEventGroupDefOID], Union[dict, "StudyEventGroupDef"]], List[Union[dict, "StudyEventGroupDef"]]]])

slots.MetaDataVersion_studyEventDef = Slot(uri=ODM.studyEventDef, name="MetaDataVersion_studyEventDef", curie=ODM.curie('studyEventDef'),
                   model_uri=ODM.MetaDataVersion_studyEventDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, StudyEventDefOID], Union[dict, "StudyEventDef"]], List[Union[dict, "StudyEventDef"]]]])

slots.MetaDataVersion_itemGroupDef = Slot(uri=ODM.itemGroupDef, name="MetaDataVersion_itemGroupDef", curie=ODM.curie('itemGroupDef'),
                   model_uri=ODM.MetaDataVersion_itemGroupDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ItemGroupDefOID], Union[dict, "ItemGroupDef"]], List[Union[dict, "ItemGroupDef"]]]])

slots.MetaDataVersion_itemDef = Slot(uri=ODM.itemDef, name="MetaDataVersion_itemDef", curie=ODM.curie('itemDef'),
                   model_uri=ODM.MetaDataVersion_itemDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ItemDefOID], Union[dict, "ItemDef"]], List[Union[dict, "ItemDef"]]]])

slots.MetaDataVersion_codeList = Slot(uri=ODM.codeList, name="MetaDataVersion_codeList", curie=ODM.curie('codeList'),
                   model_uri=ODM.MetaDataVersion_codeList, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, CodeListOID], Union[dict, "CodeList"]], List[Union[dict, "CodeList"]]]])

slots.MetaDataVersion_conditionDef = Slot(uri=ODM.conditionDef, name="MetaDataVersion_conditionDef", curie=ODM.curie('conditionDef'),
                   model_uri=ODM.MetaDataVersion_conditionDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ConditionDefOID], Union[dict, "ConditionDef"]], List[Union[dict, "ConditionDef"]]]])

slots.MetaDataVersion_methodDef = Slot(uri=ODM.methodDef, name="MetaDataVersion_methodDef", curie=ODM.curie('methodDef'),
                   model_uri=ODM.MetaDataVersion_methodDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, MethodDefOID], Union[dict, "MethodDef"]], List[Union[dict, "MethodDef"]]]])

slots.MetaDataVersion_commentDef = Slot(uri=ODM.commentDef, name="MetaDataVersion_commentDef", curie=ODM.curie('commentDef'),
                   model_uri=ODM.MetaDataVersion_commentDef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, CommentDefOID], Union[dict, "CommentDef"]], List[Union[dict, "CommentDef"]]]])

slots.MetaDataVersion_leaf = Slot(uri=ODM.leaf, name="MetaDataVersion_leaf", curie=ODM.curie('leaf'),
                   model_uri=ODM.MetaDataVersion_leaf, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, LeafID], Union[dict, "Leaf"]], List[Union[dict, "Leaf"]]]])

slots.DocumentRef_leafID = Slot(uri=ODM.leafID, name="DocumentRef_leafID", curie=ODM.curie('leafID'),
                   model_uri=ODM.DocumentRef_leafID, domain=DocumentRef, range=Union[str, DocumentRefLeafID])

slots.DocumentRef_pDFPageRef = Slot(uri=ODM.pDFPageRef, name="DocumentRef_pDFPageRef", curie=ODM.curie('pDFPageRef'),
                   model_uri=ODM.DocumentRef_pDFPageRef, domain=DocumentRef, range=Optional[Union[Union[dict, "PDFPageRef"], List[Union[dict, "PDFPageRef"]]]])

slots.PDFPageRef_pageRefs = Slot(uri=ODM.pageRefs, name="PDFPageRef_pageRefs", curie=ODM.curie('pageRefs'),
                   model_uri=ODM.PDFPageRef_pageRefs, domain=PDFPageRef, range=Optional[str])

slots.PDFPageRef_firstPage = Slot(uri=ODM.firstPage, name="PDFPageRef_firstPage", curie=ODM.curie('firstPage'),
                   model_uri=ODM.PDFPageRef_firstPage, domain=PDFPageRef, range=Optional[int])

slots.PDFPageRef_lastPage = Slot(uri=ODM.lastPage, name="PDFPageRef_lastPage", curie=ODM.curie('lastPage'),
                   model_uri=ODM.PDFPageRef_lastPage, domain=PDFPageRef, range=Optional[int])

slots.PDFPageRef_type = Slot(uri=ODM.type, name="PDFPageRef_type", curie=ODM.curie('type'),
                   model_uri=ODM.PDFPageRef_type, domain=PDFPageRef, range=Union[str, "PDFPageType"])

slots.PDFPageRef_title = Slot(uri=ODM.title, name="PDFPageRef_title", curie=ODM.curie('title'),
                   model_uri=ODM.PDFPageRef_title, domain=PDFPageRef, range=Optional[str])

slots.Leaf_ID = Slot(uri=ODM.ID, name="Leaf_ID", curie=ODM.curie('ID'),
                   model_uri=ODM.Leaf_ID, domain=Leaf, range=Union[str, LeafID])

slots.Leaf_href = Slot(uri=ODM.href, name="Leaf_href", curie=ODM.curie('href'),
                   model_uri=ODM.Leaf_href, domain=Leaf, range=Union[str, URIorCURIE])

slots.Leaf_title = Slot(uri=ODM.title, name="Leaf_title", curie=ODM.curie('title'),
                   model_uri=ODM.Leaf_title, domain=Leaf, range=Optional[Union[dict, "Title"]])

slots.Title_content = Slot(uri=ODM.content, name="Title_content", curie=ODM.curie('content'),
                   model_uri=ODM.Title_content, domain=Title, range=Optional[str])

slots.Include_studyOID = Slot(uri=ODM.studyOID, name="Include_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.Include_studyOID, domain=Include, range=Union[str, StudyOID])

slots.Include_metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="Include_metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.Include_metaDataVersionOID, domain=Include, range=Union[str, MetaDataVersionOID])

slots.Include_href = Slot(uri=ODM.href, name="Include_href", curie=ODM.curie('href'),
                   model_uri=ODM.Include_href, domain=Include, range=Optional[Union[str, URIorCURIE]])

slots.Standards_standard = Slot(uri=ODM.standard, name="Standards_standard", curie=ODM.curie('standard'),
                   model_uri=ODM.Standards_standard, domain=Standards, range=Optional[Union[Dict[Union[str, StandardOID], Union[dict, "Standard"]], List[Union[dict, "Standard"]]]])

slots.Standard_OID = Slot(uri=ODM.OID, name="Standard_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Standard_OID, domain=Standard, range=Union[str, StandardOID])

slots.Standard_name = Slot(uri=ODM.name, name="Standard_name", curie=ODM.curie('name'),
                   model_uri=ODM.Standard_name, domain=Standard, range=Union[str, "StandardName"])

slots.Standard_type = Slot(uri=ODM.type, name="Standard_type", curie=ODM.curie('type'),
                   model_uri=ODM.Standard_type, domain=Standard, range=Union[str, "StandardType"])

slots.Standard_publishingSet = Slot(uri=ODM.publishingSet, name="Standard_publishingSet", curie=ODM.curie('publishingSet'),
                   model_uri=ODM.Standard_publishingSet, domain=Standard, range=Optional[Union[str, "StandardPublishingSet"]])

slots.Standard_version = Slot(uri=ODM.version, name="Standard_version", curie=ODM.curie('version'),
                   model_uri=ODM.Standard_version, domain=Standard, range=str)

slots.Standard_status = Slot(uri=ODM.status, name="Standard_status", curie=ODM.curie('status'),
                   model_uri=ODM.Standard_status, domain=Standard, range=str)

slots.Standard_commentOID = Slot(uri=ODM.commentOID, name="Standard_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.Standard_commentOID, domain=Standard, range=Optional[Union[str, CommentDefOID]])

slots.AnnotatedCRF_documentRef = Slot(uri=ODM.documentRef, name="AnnotatedCRF_documentRef", curie=ODM.curie('documentRef'),
                   model_uri=ODM.AnnotatedCRF_documentRef, domain=AnnotatedCRF, range=Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]])

slots.SupplementalDoc_documentRef = Slot(uri=ODM.documentRef, name="SupplementalDoc_documentRef", curie=ODM.curie('documentRef'),
                   model_uri=ODM.SupplementalDoc_documentRef, domain=SupplementalDoc, range=Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]])

slots.ValueListDef_OID = Slot(uri=ODM.OID, name="ValueListDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ValueListDef_OID, domain=ValueListDef, range=Union[str, ValueListDefOID])

slots.ValueListDef_description = Slot(uri=ODM.description, name="ValueListDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.ValueListDef_description, domain=ValueListDef, range=Optional[Union[dict, Description]])

slots.ValueListDef_itemRef = Slot(uri=ODM.itemRef, name="ValueListDef_itemRef", curie=ODM.curie('itemRef'),
                   model_uri=ODM.ValueListDef_itemRef, domain=ValueListDef, range=Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]])

slots.WhereClauseRef_whereClauseOID = Slot(uri=ODM.whereClauseOID, name="WhereClauseRef_whereClauseOID", curie=ODM.curie('whereClauseOID'),
                   model_uri=ODM.WhereClauseRef_whereClauseOID, domain=WhereClauseRef, range=Union[str, WhereClauseDefOID])

slots.WhereClauseDef_OID = Slot(uri=ODM.OID, name="WhereClauseDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.WhereClauseDef_OID, domain=WhereClauseDef, range=Union[str, WhereClauseDefOID])

slots.WhereClauseDef_commentOID = Slot(uri=ODM.commentOID, name="WhereClauseDef_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.WhereClauseDef_commentOID, domain=WhereClauseDef, range=Optional[Union[str, CommentDefOID]])

slots.WhereClauseDef_rangeCheck = Slot(uri=ODM.rangeCheck, name="WhereClauseDef_rangeCheck", curie=ODM.curie('rangeCheck'),
                   model_uri=ODM.WhereClauseDef_rangeCheck, domain=WhereClauseDef, range=Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]])

slots.StudyEventGroupRef_studyEventGroupOID = Slot(uri=ODM.studyEventGroupOID, name="StudyEventGroupRef_studyEventGroupOID", curie=ODM.curie('studyEventGroupOID'),
                   model_uri=ODM.StudyEventGroupRef_studyEventGroupOID, domain=StudyEventGroupRef, range=Union[str, StudyEventGroupDefOID])

slots.StudyEventGroupRef_orderNumber = Slot(uri=ODM.orderNumber, name="StudyEventGroupRef_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.StudyEventGroupRef_orderNumber, domain=StudyEventGroupRef, range=Optional[int])

slots.StudyEventGroupRef_mandatory = Slot(uri=ODM.mandatory, name="StudyEventGroupRef_mandatory", curie=ODM.curie('mandatory'),
                   model_uri=ODM.StudyEventGroupRef_mandatory, domain=StudyEventGroupRef, range=Union[str, "YesOrNo"])

slots.StudyEventGroupRef_collectionExceptionConditionOID = Slot(uri=ODM.collectionExceptionConditionOID, name="StudyEventGroupRef_collectionExceptionConditionOID", curie=ODM.curie('collectionExceptionConditionOID'),
                   model_uri=ODM.StudyEventGroupRef_collectionExceptionConditionOID, domain=StudyEventGroupRef, range=Optional[Union[str, ConditionDefOID]])

slots.StudyEventGroupRef_description = Slot(uri=ODM.description, name="StudyEventGroupRef_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyEventGroupRef_description, domain=StudyEventGroupRef, range=Optional[Union[dict, Description]])

slots.StudyEventGroupDef_OID = Slot(uri=ODM.OID, name="StudyEventGroupDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEventGroupDef_OID, domain=StudyEventGroupDef, range=Union[str, StudyEventGroupDefOID])

slots.StudyEventGroupDef_name = Slot(uri=ODM.name, name="StudyEventGroupDef_name", curie=ODM.curie('name'),
                   model_uri=ODM.StudyEventGroupDef_name, domain=StudyEventGroupDef, range=str)

slots.StudyEventGroupDef_armOID = Slot(uri=ODM.armOID, name="StudyEventGroupDef_armOID", curie=ODM.curie('armOID'),
                   model_uri=ODM.StudyEventGroupDef_armOID, domain=StudyEventGroupDef, range=Optional[Union[str, ArmOID]])

slots.StudyEventGroupDef_epochOID = Slot(uri=ODM.epochOID, name="StudyEventGroupDef_epochOID", curie=ODM.curie('epochOID'),
                   model_uri=ODM.StudyEventGroupDef_epochOID, domain=StudyEventGroupDef, range=Optional[Union[str, EpochOID]])

slots.StudyEventGroupDef_commentOID = Slot(uri=ODM.commentOID, name="StudyEventGroupDef_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.StudyEventGroupDef_commentOID, domain=StudyEventGroupDef, range=Optional[Union[str, CommentDefOID]])

slots.StudyEventGroupDef_description = Slot(uri=ODM.description, name="StudyEventGroupDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyEventGroupDef_description, domain=StudyEventGroupDef, range=Optional[Union[dict, Description]])

slots.StudyEventGroupDef_workflowRef = Slot(uri=ODM.workflowRef, name="StudyEventGroupDef_workflowRef", curie=ODM.curie('workflowRef'),
                   model_uri=ODM.StudyEventGroupDef_workflowRef, domain=StudyEventGroupDef, range=Optional[Union[dict, "WorkflowRef"]])

slots.StudyEventGroupDef_coding = Slot(uri=ODM.coding, name="StudyEventGroupDef_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.StudyEventGroupDef_coding, domain=StudyEventGroupDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyEventGroupDef_studyEventGroupRef = Slot(uri=ODM.studyEventGroupRef, name="StudyEventGroupDef_studyEventGroupRef", curie=ODM.curie('studyEventGroupRef'),
                   model_uri=ODM.StudyEventGroupDef_studyEventGroupRef, domain=StudyEventGroupDef, range=Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]])

slots.StudyEventGroupDef_studyEventRef = Slot(uri=ODM.studyEventRef, name="StudyEventGroupDef_studyEventRef", curie=ODM.curie('studyEventRef'),
                   model_uri=ODM.StudyEventGroupDef_studyEventRef, domain=StudyEventGroupDef, range=Optional[Union[Union[dict, "StudyEventRef"], List[Union[dict, "StudyEventRef"]]]])

slots.StudyEventRef_studyEventOID = Slot(uri=ODM.studyEventOID, name="StudyEventRef_studyEventOID", curie=ODM.curie('studyEventOID'),
                   model_uri=ODM.StudyEventRef_studyEventOID, domain=StudyEventRef, range=Union[str, StudyEventDefOID])

slots.StudyEventRef_orderNumber = Slot(uri=ODM.orderNumber, name="StudyEventRef_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.StudyEventRef_orderNumber, domain=StudyEventRef, range=Optional[int])

slots.StudyEventRef_mandatory = Slot(uri=ODM.mandatory, name="StudyEventRef_mandatory", curie=ODM.curie('mandatory'),
                   model_uri=ODM.StudyEventRef_mandatory, domain=StudyEventRef, range=Union[str, "YesOrNo"])

slots.StudyEventRef_collectionExceptionConditionOID = Slot(uri=ODM.collectionExceptionConditionOID, name="StudyEventRef_collectionExceptionConditionOID", curie=ODM.curie('collectionExceptionConditionOID'),
                   model_uri=ODM.StudyEventRef_collectionExceptionConditionOID, domain=StudyEventRef, range=Optional[Union[str, ConditionDefOID]])

slots.StudyEventDef_OID = Slot(uri=ODM.OID, name="StudyEventDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEventDef_OID, domain=StudyEventDef, range=Union[str, StudyEventDefOID])

slots.StudyEventDef_name = Slot(uri=ODM.name, name="StudyEventDef_name", curie=ODM.curie('name'),
                   model_uri=ODM.StudyEventDef_name, domain=StudyEventDef, range=str)

slots.StudyEventDef_repeating = Slot(uri=ODM.repeating, name="StudyEventDef_repeating", curie=ODM.curie('repeating'),
                   model_uri=ODM.StudyEventDef_repeating, domain=StudyEventDef, range=Union[str, "YesOrNo"])

slots.StudyEventDef_type = Slot(uri=ODM.type, name="StudyEventDef_type", curie=ODM.curie('type'),
                   model_uri=ODM.StudyEventDef_type, domain=StudyEventDef, range=Union[str, "EventType"])

slots.StudyEventDef_category = Slot(uri=ODM.category, name="StudyEventDef_category", curie=ODM.curie('category'),
                   model_uri=ODM.StudyEventDef_category, domain=StudyEventDef, range=Optional[str])

slots.StudyEventDef_commentOID = Slot(uri=ODM.commentOID, name="StudyEventDef_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.StudyEventDef_commentOID, domain=StudyEventDef, range=Optional[Union[str, CommentDefOID]])

slots.StudyEventDef_description = Slot(uri=ODM.description, name="StudyEventDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyEventDef_description, domain=StudyEventDef, range=Optional[Union[dict, Description]])

slots.StudyEventDef_itemGroupRef = Slot(uri=ODM.itemGroupRef, name="StudyEventDef_itemGroupRef", curie=ODM.curie('itemGroupRef'),
                   model_uri=ODM.StudyEventDef_itemGroupRef, domain=StudyEventDef, range=Optional[Union[Union[dict, "ItemGroupRef"], List[Union[dict, "ItemGroupRef"]]]])

slots.StudyEventDef_workflowRef = Slot(uri=ODM.workflowRef, name="StudyEventDef_workflowRef", curie=ODM.curie('workflowRef'),
                   model_uri=ODM.StudyEventDef_workflowRef, domain=StudyEventDef, range=Optional[Union[dict, "WorkflowRef"]])

slots.StudyEventDef_coding = Slot(uri=ODM.coding, name="StudyEventDef_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.StudyEventDef_coding, domain=StudyEventDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyEventDef_alias = Slot(uri=ODM.alias, name="StudyEventDef_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.StudyEventDef_alias, domain=StudyEventDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.ItemGroupRef_itemGroupOID = Slot(uri=ODM.itemGroupOID, name="ItemGroupRef_itemGroupOID", curie=ODM.curie('itemGroupOID'),
                   model_uri=ODM.ItemGroupRef_itemGroupOID, domain=ItemGroupRef, range=Union[str, ItemGroupDefOID])

slots.ItemGroupRef_methodOID = Slot(uri=ODM.methodOID, name="ItemGroupRef_methodOID", curie=ODM.curie('methodOID'),
                   model_uri=ODM.ItemGroupRef_methodOID, domain=ItemGroupRef, range=Optional[Union[str, MethodDefOID]])

slots.ItemGroupRef_orderNumber = Slot(uri=ODM.orderNumber, name="ItemGroupRef_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.ItemGroupRef_orderNumber, domain=ItemGroupRef, range=Optional[int])

slots.ItemGroupRef_mandatory = Slot(uri=ODM.mandatory, name="ItemGroupRef_mandatory", curie=ODM.curie('mandatory'),
                   model_uri=ODM.ItemGroupRef_mandatory, domain=ItemGroupRef, range=Union[str, "YesOrNo"])

slots.ItemGroupRef_collectionExceptionConditionOID = Slot(uri=ODM.collectionExceptionConditionOID, name="ItemGroupRef_collectionExceptionConditionOID", curie=ODM.curie('collectionExceptionConditionOID'),
                   model_uri=ODM.ItemGroupRef_collectionExceptionConditionOID, domain=ItemGroupRef, range=Optional[Union[str, ConditionDefOID]])

slots.ItemGroupDef_OID = Slot(uri=ODM.OID, name="ItemGroupDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ItemGroupDef_OID, domain=ItemGroupDef, range=Union[str, ItemGroupDefOID])

slots.ItemGroupDef_name = Slot(uri=ODM.name, name="ItemGroupDef_name", curie=ODM.curie('name'),
                   model_uri=ODM.ItemGroupDef_name, domain=ItemGroupDef, range=str)

slots.ItemGroupDef_repeating = Slot(uri=ODM.repeating, name="ItemGroupDef_repeating", curie=ODM.curie('repeating'),
                   model_uri=ODM.ItemGroupDef_repeating, domain=ItemGroupDef, range=Union[str, "ItemGroupRepeatingType"])

slots.ItemGroupDef_repeatingLimit = Slot(uri=ODM.repeatingLimit, name="ItemGroupDef_repeatingLimit", curie=ODM.curie('repeatingLimit'),
                   model_uri=ODM.ItemGroupDef_repeatingLimit, domain=ItemGroupDef, range=Optional[int])

slots.ItemGroupDef_isReferenceData = Slot(uri=ODM.isReferenceData, name="ItemGroupDef_isReferenceData", curie=ODM.curie('isReferenceData'),
                   model_uri=ODM.ItemGroupDef_isReferenceData, domain=ItemGroupDef, range=Optional[Union[str, "YesOrNo"]])

slots.ItemGroupDef_structure = Slot(uri=ODM.structure, name="ItemGroupDef_structure", curie=ODM.curie('structure'),
                   model_uri=ODM.ItemGroupDef_structure, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_archiveLocationID = Slot(uri=ODM.archiveLocationID, name="ItemGroupDef_archiveLocationID", curie=ODM.curie('archiveLocationID'),
                   model_uri=ODM.ItemGroupDef_archiveLocationID, domain=ItemGroupDef, range=Optional[Union[str, LeafID]])

slots.ItemGroupDef_datasetName = Slot(uri=ODM.datasetName, name="ItemGroupDef_datasetName", curie=ODM.curie('datasetName'),
                   model_uri=ODM.ItemGroupDef_datasetName, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_domain = Slot(uri=ODM.domain, name="ItemGroupDef_domain", curie=ODM.curie('domain'),
                   model_uri=ODM.ItemGroupDef_domain, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_type = Slot(uri=ODM.type, name="ItemGroupDef_type", curie=ODM.curie('type'),
                   model_uri=ODM.ItemGroupDef_type, domain=ItemGroupDef, range=str)

slots.ItemGroupDef_purpose = Slot(uri=ODM.purpose, name="ItemGroupDef_purpose", curie=ODM.curie('purpose'),
                   model_uri=ODM.ItemGroupDef_purpose, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_standardOID = Slot(uri=ODM.standardOID, name="ItemGroupDef_standardOID", curie=ODM.curie('standardOID'),
                   model_uri=ODM.ItemGroupDef_standardOID, domain=ItemGroupDef, range=Optional[Union[str, StandardOID]])

slots.ItemGroupDef_isNonStandard = Slot(uri=ODM.isNonStandard, name="ItemGroupDef_isNonStandard", curie=ODM.curie('isNonStandard'),
                   model_uri=ODM.ItemGroupDef_isNonStandard, domain=ItemGroupDef, range=Optional[Union[str, "YesOnly"]])

slots.ItemGroupDef_hasNoData = Slot(uri=ODM.hasNoData, name="ItemGroupDef_hasNoData", curie=ODM.curie('hasNoData'),
                   model_uri=ODM.ItemGroupDef_hasNoData, domain=ItemGroupDef, range=Optional[Union[str, "YesOnly"]])

slots.ItemGroupDef_commentOID = Slot(uri=ODM.commentOID, name="ItemGroupDef_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.ItemGroupDef_commentOID, domain=ItemGroupDef, range=Optional[Union[str, CommentDefOID]])

slots.ItemGroupDef_description = Slot(uri=ODM.description, name="ItemGroupDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.ItemGroupDef_description, domain=ItemGroupDef, range=Optional[Union[dict, Description]])

slots.ItemGroupDef_itemGroupClass = Slot(uri=ODM.itemGroupClass, name="ItemGroupDef_itemGroupClass", curie=ODM.curie('itemGroupClass'),
                   model_uri=ODM.ItemGroupDef_itemGroupClass, domain=ItemGroupDef, range=Optional[Union[dict, "Class"]])

slots.ItemGroupDef_coding = Slot(uri=ODM.coding, name="ItemGroupDef_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.ItemGroupDef_coding, domain=ItemGroupDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.ItemGroupDef_workflowRef = Slot(uri=ODM.workflowRef, name="ItemGroupDef_workflowRef", curie=ODM.curie('workflowRef'),
                   model_uri=ODM.ItemGroupDef_workflowRef, domain=ItemGroupDef, range=Optional[Union[dict, "WorkflowRef"]])

slots.ItemGroupDef_origin = Slot(uri=ODM.origin, name="ItemGroupDef_origin", curie=ODM.curie('origin'),
                   model_uri=ODM.ItemGroupDef_origin, domain=ItemGroupDef, range=Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]])

slots.ItemGroupDef_alias = Slot(uri=ODM.alias, name="ItemGroupDef_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.ItemGroupDef_alias, domain=ItemGroupDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.ItemGroupDef_leaf = Slot(uri=ODM.leaf, name="ItemGroupDef_leaf", curie=ODM.curie('leaf'),
                   model_uri=ODM.ItemGroupDef_leaf, domain=ItemGroupDef, range=Optional[Union[str, LeafID]])

slots.ItemGroupDef_itemGroupRef = Slot(uri=ODM.itemGroupRef, name="ItemGroupDef_itemGroupRef", curie=ODM.curie('itemGroupRef'),
                   model_uri=ODM.ItemGroupDef_itemGroupRef, domain=ItemGroupDef, range=Optional[Union[Union[dict, ItemGroupRef], List[Union[dict, ItemGroupRef]]]])

slots.ItemGroupDef_itemRef = Slot(uri=ODM.itemRef, name="ItemGroupDef_itemRef", curie=ODM.curie('itemRef'),
                   model_uri=ODM.ItemGroupDef_itemRef, domain=ItemGroupDef, range=Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]])

slots.Class_name = Slot(uri=ODM.name, name="Class_name", curie=ODM.curie('name'),
                   model_uri=ODM.Class_name, domain=Class, range=Union[str, "ItemGroupClass"])

slots.Class_subClass = Slot(uri=ODM.subClass, name="Class_subClass", curie=ODM.curie('subClass'),
                   model_uri=ODM.Class_subClass, domain=Class, range=Optional[Union[Union[dict, "SubClass"], List[Union[dict, "SubClass"]]]])

slots.SubClass_name = Slot(uri=ODM.name, name="SubClass_name", curie=ODM.curie('name'),
                   model_uri=ODM.SubClass_name, domain=SubClass, range=Union[str, "ItemGroupSubClass"])

slots.SubClass_parentClass = Slot(uri=ODM.parentClass, name="SubClass_parentClass", curie=ODM.curie('parentClass'),
                   model_uri=ODM.SubClass_parentClass, domain=SubClass, range=Optional[str])

slots.ItemRef_itemOID = Slot(uri=ODM.itemOID, name="ItemRef_itemOID", curie=ODM.curie('itemOID'),
                   model_uri=ODM.ItemRef_itemOID, domain=ItemRef, range=Union[str, ItemDefOID])

slots.ItemRef_keySequence = Slot(uri=ODM.keySequence, name="ItemRef_keySequence", curie=ODM.curie('keySequence'),
                   model_uri=ODM.ItemRef_keySequence, domain=ItemRef, range=Optional[int])

slots.ItemRef_isNonStandard = Slot(uri=ODM.isNonStandard, name="ItemRef_isNonStandard", curie=ODM.curie('isNonStandard'),
                   model_uri=ODM.ItemRef_isNonStandard, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_hasNoData = Slot(uri=ODM.hasNoData, name="ItemRef_hasNoData", curie=ODM.curie('hasNoData'),
                   model_uri=ODM.ItemRef_hasNoData, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_methodOID = Slot(uri=ODM.methodOID, name="ItemRef_methodOID", curie=ODM.curie('methodOID'),
                   model_uri=ODM.ItemRef_methodOID, domain=ItemRef, range=Optional[Union[str, MethodDefOID]])

slots.ItemRef_unitsItemOID = Slot(uri=ODM.unitsItemOID, name="ItemRef_unitsItemOID", curie=ODM.curie('unitsItemOID'),
                   model_uri=ODM.ItemRef_unitsItemOID, domain=ItemRef, range=Optional[Union[str, ItemDefOID]])

slots.ItemRef_repeat = Slot(uri=ODM.repeat, name="ItemRef_repeat", curie=ODM.curie('repeat'),
                   model_uri=ODM.ItemRef_repeat, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_other = Slot(uri=ODM.other, name="ItemRef_other", curie=ODM.curie('other'),
                   model_uri=ODM.ItemRef_other, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_role = Slot(uri=ODM.role, name="ItemRef_role", curie=ODM.curie('role'),
                   model_uri=ODM.ItemRef_role, domain=ItemRef, range=Optional[str])

slots.ItemRef_roleCodeListOID = Slot(uri=ODM.roleCodeListOID, name="ItemRef_roleCodeListOID", curie=ODM.curie('roleCodeListOID'),
                   model_uri=ODM.ItemRef_roleCodeListOID, domain=ItemRef, range=Optional[Union[str, CodeListOID]])

slots.ItemRef_core = Slot(uri=ODM.core, name="ItemRef_core", curie=ODM.curie('core'),
                   model_uri=ODM.ItemRef_core, domain=ItemRef, range=Optional[str])

slots.ItemRef_preSpecifiedValue = Slot(uri=ODM.preSpecifiedValue, name="ItemRef_preSpecifiedValue", curie=ODM.curie('preSpecifiedValue'),
                   model_uri=ODM.ItemRef_preSpecifiedValue, domain=ItemRef, range=Optional[str])

slots.ItemRef_orderNumber = Slot(uri=ODM.orderNumber, name="ItemRef_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.ItemRef_orderNumber, domain=ItemRef, range=Optional[int])

slots.ItemRef_mandatory = Slot(uri=ODM.mandatory, name="ItemRef_mandatory", curie=ODM.curie('mandatory'),
                   model_uri=ODM.ItemRef_mandatory, domain=ItemRef, range=Union[str, "YesOrNo"])

slots.ItemRef_collectionExceptionConditionOID = Slot(uri=ODM.collectionExceptionConditionOID, name="ItemRef_collectionExceptionConditionOID", curie=ODM.curie('collectionExceptionConditionOID'),
                   model_uri=ODM.ItemRef_collectionExceptionConditionOID, domain=ItemRef, range=Optional[Union[str, ConditionDefOID]])

slots.ItemRef_origin = Slot(uri=ODM.origin, name="ItemRef_origin", curie=ODM.curie('origin'),
                   model_uri=ODM.ItemRef_origin, domain=ItemRef, range=Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]])

slots.ItemRef_whereClauseRef = Slot(uri=ODM.whereClauseRef, name="ItemRef_whereClauseRef", curie=ODM.curie('whereClauseRef'),
                   model_uri=ODM.ItemRef_whereClauseRef, domain=ItemRef, range=Optional[Union[Union[dict, WhereClauseRef], List[Union[dict, WhereClauseRef]]]])

slots.Origin_type = Slot(uri=ODM.type, name="Origin_type", curie=ODM.curie('type'),
                   model_uri=ODM.Origin_type, domain=Origin, range=Union[str, "OriginType"])

slots.Origin_source = Slot(uri=ODM.source, name="Origin_source", curie=ODM.curie('source'),
                   model_uri=ODM.Origin_source, domain=Origin, range=Optional[Union[str, "OriginSource"]])

slots.Origin_description = Slot(uri=ODM.description, name="Origin_description", curie=ODM.curie('description'),
                   model_uri=ODM.Origin_description, domain=Origin, range=Optional[Union[dict, Description]])

slots.Origin_sourceItems = Slot(uri=ODM.sourceItems, name="Origin_sourceItems", curie=ODM.curie('sourceItems'),
                   model_uri=ODM.Origin_sourceItems, domain=Origin, range=Optional[Union[dict, "SourceItems"]])

slots.Origin_coding = Slot(uri=ODM.coding, name="Origin_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.Origin_coding, domain=Origin, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Origin_documentRef = Slot(uri=ODM.documentRef, name="Origin_documentRef", curie=ODM.curie('documentRef'),
                   model_uri=ODM.Origin_documentRef, domain=Origin, range=Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]])

slots.SourceItems_sourceItem = Slot(uri=ODM.sourceItem, name="SourceItems_sourceItem", curie=ODM.curie('sourceItem'),
                   model_uri=ODM.SourceItems_sourceItem, domain=SourceItems, range=Optional[Union[Union[dict, "SourceItem"], List[Union[dict, "SourceItem"]]]])

slots.SourceItems_coding = Slot(uri=ODM.coding, name="SourceItems_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.SourceItems_coding, domain=SourceItems, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.SourceItem_itemOID = Slot(uri=ODM.itemOID, name="SourceItem_itemOID", curie=ODM.curie('itemOID'),
                   model_uri=ODM.SourceItem_itemOID, domain=SourceItem, range=Optional[Union[str, ItemDefOID]])

slots.SourceItem_itemGroupOID = Slot(uri=ODM.itemGroupOID, name="SourceItem_itemGroupOID", curie=ODM.curie('itemGroupOID'),
                   model_uri=ODM.SourceItem_itemGroupOID, domain=SourceItem, range=Optional[Union[str, ItemGroupDefOID]])

slots.SourceItem_metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="SourceItem_metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.SourceItem_metaDataVersionOID, domain=SourceItem, range=Optional[Union[str, MetaDataVersionOID]])

slots.SourceItem_studyOID = Slot(uri=ODM.studyOID, name="SourceItem_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.SourceItem_studyOID, domain=SourceItem, range=Optional[Union[str, StudyOID]])

slots.SourceItem_leafID = Slot(uri=ODM.leafID, name="SourceItem_leafID", curie=ODM.curie('leafID'),
                   model_uri=ODM.SourceItem_leafID, domain=SourceItem, range=Optional[Union[str, LeafID]])

slots.SourceItem_name = Slot(uri=ODM.name, name="SourceItem_name", curie=ODM.curie('name'),
                   model_uri=ODM.SourceItem_name, domain=SourceItem, range=Optional[str])

slots.SourceItem_resource = Slot(uri=ODM.resource, name="SourceItem_resource", curie=ODM.curie('resource'),
                   model_uri=ODM.SourceItem_resource, domain=SourceItem, range=Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]])

slots.SourceItem_coding = Slot(uri=ODM.coding, name="SourceItem_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.SourceItem_coding, domain=SourceItem, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Resource_type = Slot(uri=ODM.type, name="Resource_type", curie=ODM.curie('type'),
                   model_uri=ODM.Resource_type, domain=Resource, range=str)

slots.Resource_name = Slot(uri=ODM.name, name="Resource_name", curie=ODM.curie('name'),
                   model_uri=ODM.Resource_name, domain=Resource, range=str)

slots.Resource_attribute = Slot(uri=ODM.attribute, name="Resource_attribute", curie=ODM.curie('attribute'),
                   model_uri=ODM.Resource_attribute, domain=Resource, range=Optional[str])

slots.Resource_label = Slot(uri=ODM.label, name="Resource_label", curie=ODM.curie('label'),
                   model_uri=ODM.Resource_label, domain=Resource, range=Optional[str])

slots.Resource_selection = Slot(uri=ODM.selection, name="Resource_selection", curie=ODM.curie('selection'),
                   model_uri=ODM.Resource_selection, domain=Resource, range=Optional[Union[Union[dict, "Selection"], List[Union[dict, "Selection"]]]])

slots.Selection_path = Slot(uri=ODM.path, name="Selection_path", curie=ODM.curie('path'),
                   model_uri=ODM.Selection_path, domain=Selection, range=str)

slots.ItemDef_OID = Slot(uri=ODM.OID, name="ItemDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ItemDef_OID, domain=ItemDef, range=Union[str, ItemDefOID])

slots.ItemDef_name = Slot(uri=ODM.name, name="ItemDef_name", curie=ODM.curie('name'),
                   model_uri=ODM.ItemDef_name, domain=ItemDef, range=str)

slots.ItemDef_dataType = Slot(uri=ODM.dataType, name="ItemDef_dataType", curie=ODM.curie('dataType'),
                   model_uri=ODM.ItemDef_dataType, domain=ItemDef, range=Union[str, "DataType"])

slots.ItemDef_length = Slot(uri=ODM.length, name="ItemDef_length", curie=ODM.curie('length'),
                   model_uri=ODM.ItemDef_length, domain=ItemDef, range=Optional[int])

slots.ItemDef_displayFormat = Slot(uri=ODM.displayFormat, name="ItemDef_displayFormat", curie=ODM.curie('displayFormat'),
                   model_uri=ODM.ItemDef_displayFormat, domain=ItemDef, range=Optional[str])

slots.ItemDef_variableSet = Slot(uri=ODM.variableSet, name="ItemDef_variableSet", curie=ODM.curie('variableSet'),
                   model_uri=ODM.ItemDef_variableSet, domain=ItemDef, range=Optional[str])

slots.ItemDef_commentOID = Slot(uri=ODM.commentOID, name="ItemDef_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.ItemDef_commentOID, domain=ItemDef, range=Optional[Union[str, CommentDefOID]])

slots.ItemDef_description = Slot(uri=ODM.description, name="ItemDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.ItemDef_description, domain=ItemDef, range=Optional[Union[dict, Description]])

slots.ItemDef_definition = Slot(uri=ODM.definition, name="ItemDef_definition", curie=ODM.curie('definition'),
                   model_uri=ODM.ItemDef_definition, domain=ItemDef, range=Optional[Union[dict, "Definition"]])

slots.ItemDef_question = Slot(uri=ODM.question, name="ItemDef_question", curie=ODM.curie('question'),
                   model_uri=ODM.ItemDef_question, domain=ItemDef, range=Optional[Union[dict, "Question"]])

slots.ItemDef_prompt = Slot(uri=ODM.prompt, name="ItemDef_prompt", curie=ODM.curie('prompt'),
                   model_uri=ODM.ItemDef_prompt, domain=ItemDef, range=Optional[Union[dict, "Prompt"]])

slots.ItemDef_cRFCompletionInstructions = Slot(uri=ODM.cRFCompletionInstructions, name="ItemDef_cRFCompletionInstructions", curie=ODM.curie('cRFCompletionInstructions'),
                   model_uri=ODM.ItemDef_cRFCompletionInstructions, domain=ItemDef, range=Optional[Union[dict, "CRFCompletionInstructions"]])

slots.ItemDef_implementationNotes = Slot(uri=ODM.implementationNotes, name="ItemDef_implementationNotes", curie=ODM.curie('implementationNotes'),
                   model_uri=ODM.ItemDef_implementationNotes, domain=ItemDef, range=Optional[Union[dict, "ImplementationNotes"]])

slots.ItemDef_cDISCNotes = Slot(uri=ODM.cDISCNotes, name="ItemDef_cDISCNotes", curie=ODM.curie('cDISCNotes'),
                   model_uri=ODM.ItemDef_cDISCNotes, domain=ItemDef, range=Optional[Union[dict, "CDISCNotes"]])

slots.ItemDef_rangeCheck = Slot(uri=ODM.rangeCheck, name="ItemDef_rangeCheck", curie=ODM.curie('rangeCheck'),
                   model_uri=ODM.ItemDef_rangeCheck, domain=ItemDef, range=Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]])

slots.ItemDef_codeListRef = Slot(uri=ODM.codeListRef, name="ItemDef_codeListRef", curie=ODM.curie('codeListRef'),
                   model_uri=ODM.ItemDef_codeListRef, domain=ItemDef, range=Optional[Union[dict, "CodeListRef"]])

slots.ItemDef_valueListRef = Slot(uri=ODM.valueListRef, name="ItemDef_valueListRef", curie=ODM.curie('valueListRef'),
                   model_uri=ODM.ItemDef_valueListRef, domain=ItemDef, range=Optional[Union[dict, "ValueListRef"]])

slots.ItemDef_coding = Slot(uri=ODM.coding, name="ItemDef_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.ItemDef_coding, domain=ItemDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.ItemDef_alias = Slot(uri=ODM.alias, name="ItemDef_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.ItemDef_alias, domain=ItemDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.Question_translatedText = Slot(uri=ODM.translatedText, name="Question_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.Question_translatedText, domain=Question, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.Definition_translatedText = Slot(uri=ODM.translatedText, name="Definition_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.Definition_translatedText, domain=Definition, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.Prompt_translatedText = Slot(uri=ODM.translatedText, name="Prompt_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.Prompt_translatedText, domain=Prompt, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.CRFCompletionInstructions_translatedText = Slot(uri=ODM.translatedText, name="CRFCompletionInstructions_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.CRFCompletionInstructions_translatedText, domain=CRFCompletionInstructions, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.ImplementationNotes_translatedText = Slot(uri=ODM.translatedText, name="ImplementationNotes_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.ImplementationNotes_translatedText, domain=ImplementationNotes, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.CDISCNotes_translatedText = Slot(uri=ODM.translatedText, name="CDISCNotes_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.CDISCNotes_translatedText, domain=CDISCNotes, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.RangeCheck_comparator = Slot(uri=ODM.comparator, name="RangeCheck_comparator", curie=ODM.curie('comparator'),
                   model_uri=ODM.RangeCheck_comparator, domain=RangeCheck, range=Optional[Union[str, "Comparator"]])

slots.RangeCheck_softHard = Slot(uri=ODM.softHard, name="RangeCheck_softHard", curie=ODM.curie('softHard'),
                   model_uri=ODM.RangeCheck_softHard, domain=RangeCheck, range=Optional[Union[str, "SoftOrHard"]])

slots.RangeCheck_itemOID = Slot(uri=ODM.itemOID, name="RangeCheck_itemOID", curie=ODM.curie('itemOID'),
                   model_uri=ODM.RangeCheck_itemOID, domain=RangeCheck, range=Optional[Union[str, ItemDefOID]])

slots.RangeCheck_errorMessage = Slot(uri=ODM.errorMessage, name="RangeCheck_errorMessage", curie=ODM.curie('errorMessage'),
                   model_uri=ODM.RangeCheck_errorMessage, domain=RangeCheck, range=Optional[Union[dict, "ErrorMessage"]])

slots.RangeCheck_methodSignature = Slot(uri=ODM.methodSignature, name="RangeCheck_methodSignature", curie=ODM.curie('methodSignature'),
                   model_uri=ODM.RangeCheck_methodSignature, domain=RangeCheck, range=Optional[Union[dict, "MethodSignature"]])

slots.RangeCheck_formalExpression = Slot(uri=ODM.formalExpression, name="RangeCheck_formalExpression", curie=ODM.curie('formalExpression'),
                   model_uri=ODM.RangeCheck_formalExpression, domain=RangeCheck, range=Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]])

slots.RangeCheck_checkValue = Slot(uri=ODM.checkValue, name="RangeCheck_checkValue", curie=ODM.curie('checkValue'),
                   model_uri=ODM.RangeCheck_checkValue, domain=RangeCheck, range=Optional[Union[Union[dict, "CheckValue"], List[Union[dict, "CheckValue"]]]])

slots.CheckValue_content = Slot(uri=ODM.content, name="CheckValue_content", curie=ODM.curie('content'),
                   model_uri=ODM.CheckValue_content, domain=CheckValue, range=Optional[str])

slots.ErrorMessage_translatedText = Slot(uri=ODM.translatedText, name="ErrorMessage_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.ErrorMessage_translatedText, domain=ErrorMessage, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.CodeListRef_codeListOID = Slot(uri=ODM.codeListOID, name="CodeListRef_codeListOID", curie=ODM.curie('codeListOID'),
                   model_uri=ODM.CodeListRef_codeListOID, domain=CodeListRef, range=Union[str, CodeListOID])

slots.ValueListRef_valueListOID = Slot(uri=ODM.valueListOID, name="ValueListRef_valueListOID", curie=ODM.curie('valueListOID'),
                   model_uri=ODM.ValueListRef_valueListOID, domain=ValueListRef, range=Union[str, ValueListDefOID])

slots.CodeList_OID = Slot(uri=ODM.OID, name="CodeList_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.CodeList_OID, domain=CodeList, range=Union[str, CodeListOID])

slots.CodeList_name = Slot(uri=ODM.name, name="CodeList_name", curie=ODM.curie('name'),
                   model_uri=ODM.CodeList_name, domain=CodeList, range=str)

slots.CodeList_dataType = Slot(uri=ODM.dataType, name="CodeList_dataType", curie=ODM.curie('dataType'),
                   model_uri=ODM.CodeList_dataType, domain=CodeList, range=Union[str, "CLDataType"])

slots.CodeList_commentOID = Slot(uri=ODM.commentOID, name="CodeList_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.CodeList_commentOID, domain=CodeList, range=Optional[Union[str, CommentDefOID]])

slots.CodeList_standardOID = Slot(uri=ODM.standardOID, name="CodeList_standardOID", curie=ODM.curie('standardOID'),
                   model_uri=ODM.CodeList_standardOID, domain=CodeList, range=Optional[Union[str, StandardOID]])

slots.CodeList_isNonStandard = Slot(uri=ODM.isNonStandard, name="CodeList_isNonStandard", curie=ODM.curie('isNonStandard'),
                   model_uri=ODM.CodeList_isNonStandard, domain=CodeList, range=Optional[Union[str, "YesOnly"]])

slots.CodeList_description = Slot(uri=ODM.description, name="CodeList_description", curie=ODM.curie('description'),
                   model_uri=ODM.CodeList_description, domain=CodeList, range=Optional[Union[dict, Description]])

slots.CodeList_codeListItem = Slot(uri=ODM.codeListItem, name="CodeList_codeListItem", curie=ODM.curie('codeListItem'),
                   model_uri=ODM.CodeList_codeListItem, domain=CodeList, range=Optional[Union[Union[dict, "CodeListItem"], List[Union[dict, "CodeListItem"]]]])

slots.CodeList_coding = Slot(uri=ODM.coding, name="CodeList_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.CodeList_coding, domain=CodeList, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.CodeList_alias = Slot(uri=ODM.alias, name="CodeList_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.CodeList_alias, domain=CodeList, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.CodeListItem_codedValue = Slot(uri=ODM.codedValue, name="CodeListItem_codedValue", curie=ODM.curie('codedValue'),
                   model_uri=ODM.CodeListItem_codedValue, domain=CodeListItem, range=str)

slots.CodeListItem_rank = Slot(uri=ODM.rank, name="CodeListItem_rank", curie=ODM.curie('rank'),
                   model_uri=ODM.CodeListItem_rank, domain=CodeListItem, range=Optional[Decimal])

slots.CodeListItem_other = Slot(uri=ODM.other, name="CodeListItem_other", curie=ODM.curie('other'),
                   model_uri=ODM.CodeListItem_other, domain=CodeListItem, range=Optional[Union[str, "YesOnly"]])

slots.CodeListItem_orderNumber = Slot(uri=ODM.orderNumber, name="CodeListItem_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.CodeListItem_orderNumber, domain=CodeListItem, range=Optional[int])

slots.CodeListItem_extendedValue = Slot(uri=ODM.extendedValue, name="CodeListItem_extendedValue", curie=ODM.curie('extendedValue'),
                   model_uri=ODM.CodeListItem_extendedValue, domain=CodeListItem, range=Optional[Union[str, "YesOnly"]])

slots.CodeListItem_commentOID = Slot(uri=ODM.commentOID, name="CodeListItem_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.CodeListItem_commentOID, domain=CodeListItem, range=Optional[Union[str, CommentDefOID]])

slots.CodeListItem_description = Slot(uri=ODM.description, name="CodeListItem_description", curie=ODM.curie('description'),
                   model_uri=ODM.CodeListItem_description, domain=CodeListItem, range=Optional[Union[dict, Description]])

slots.CodeListItem_decode = Slot(uri=ODM.decode, name="CodeListItem_decode", curie=ODM.curie('decode'),
                   model_uri=ODM.CodeListItem_decode, domain=CodeListItem, range=Optional[Union[dict, "Decode"]])

slots.CodeListItem_coding = Slot(uri=ODM.coding, name="CodeListItem_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.CodeListItem_coding, domain=CodeListItem, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.CodeListItem_alias = Slot(uri=ODM.alias, name="CodeListItem_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.CodeListItem_alias, domain=CodeListItem, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.Decode_translatedText = Slot(uri=ODM.translatedText, name="Decode_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.Decode_translatedText, domain=Decode, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.MethodDef_OID = Slot(uri=ODM.OID, name="MethodDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.MethodDef_OID, domain=MethodDef, range=Union[str, MethodDefOID])

slots.MethodDef_name = Slot(uri=ODM.name, name="MethodDef_name", curie=ODM.curie('name'),
                   model_uri=ODM.MethodDef_name, domain=MethodDef, range=str)

slots.MethodDef_type = Slot(uri=ODM.type, name="MethodDef_type", curie=ODM.curie('type'),
                   model_uri=ODM.MethodDef_type, domain=MethodDef, range=Optional[Union[str, "MethodType"]])

slots.MethodDef_commentOID = Slot(uri=ODM.commentOID, name="MethodDef_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.MethodDef_commentOID, domain=MethodDef, range=Optional[Union[str, CommentDefOID]])

slots.MethodDef_description = Slot(uri=ODM.description, name="MethodDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.MethodDef_description, domain=MethodDef, range=Optional[Union[dict, Description]])

slots.MethodDef_methodSignature = Slot(uri=ODM.methodSignature, name="MethodDef_methodSignature", curie=ODM.curie('methodSignature'),
                   model_uri=ODM.MethodDef_methodSignature, domain=MethodDef, range=Optional[Union[dict, "MethodSignature"]])

slots.MethodDef_formalExpression = Slot(uri=ODM.formalExpression, name="MethodDef_formalExpression", curie=ODM.curie('formalExpression'),
                   model_uri=ODM.MethodDef_formalExpression, domain=MethodDef, range=Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]])

slots.MethodDef_alias = Slot(uri=ODM.alias, name="MethodDef_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.MethodDef_alias, domain=MethodDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.MethodDef_documentRef = Slot(uri=ODM.documentRef, name="MethodDef_documentRef", curie=ODM.curie('documentRef'),
                   model_uri=ODM.MethodDef_documentRef, domain=MethodDef, range=Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]])

slots.MethodSignature_parameter = Slot(uri=ODM.parameter, name="MethodSignature_parameter", curie=ODM.curie('parameter'),
                   model_uri=ODM.MethodSignature_parameter, domain=MethodSignature, range=Optional[Union[Union[dict, "Parameter"], List[Union[dict, "Parameter"]]]])

slots.MethodSignature_returnValue = Slot(uri=ODM.returnValue, name="MethodSignature_returnValue", curie=ODM.curie('returnValue'),
                   model_uri=ODM.MethodSignature_returnValue, domain=MethodSignature, range=Optional[Union[Union[dict, "ReturnValue"], List[Union[dict, "ReturnValue"]]]])

slots.Parameter_name = Slot(uri=ODM.name, name="Parameter_name", curie=ODM.curie('name'),
                   model_uri=ODM.Parameter_name, domain=Parameter, range=str)

slots.Parameter_dataType = Slot(uri=ODM.dataType, name="Parameter_dataType", curie=ODM.curie('dataType'),
                   model_uri=ODM.Parameter_dataType, domain=Parameter, range=Union[str, "DataType"])

slots.Parameter_definition = Slot(uri=ODM.definition, name="Parameter_definition", curie=ODM.curie('definition'),
                   model_uri=ODM.Parameter_definition, domain=Parameter, range=Optional[str])

slots.Parameter_orderNumber = Slot(uri=ODM.orderNumber, name="Parameter_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.Parameter_orderNumber, domain=Parameter, range=Optional[int])

slots.ReturnValue_name = Slot(uri=ODM.name, name="ReturnValue_name", curie=ODM.curie('name'),
                   model_uri=ODM.ReturnValue_name, domain=ReturnValue, range=str)

slots.ReturnValue_dataType = Slot(uri=ODM.dataType, name="ReturnValue_dataType", curie=ODM.curie('dataType'),
                   model_uri=ODM.ReturnValue_dataType, domain=ReturnValue, range=Union[str, "DataType"])

slots.ReturnValue_definition = Slot(uri=ODM.definition, name="ReturnValue_definition", curie=ODM.curie('definition'),
                   model_uri=ODM.ReturnValue_definition, domain=ReturnValue, range=Optional[str])

slots.ReturnValue_orderNumber = Slot(uri=ODM.orderNumber, name="ReturnValue_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.ReturnValue_orderNumber, domain=ReturnValue, range=Optional[int])

slots.ConditionDef_OID = Slot(uri=ODM.OID, name="ConditionDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ConditionDef_OID, domain=ConditionDef, range=Union[str, ConditionDefOID])

slots.ConditionDef_name = Slot(uri=ODM.name, name="ConditionDef_name", curie=ODM.curie('name'),
                   model_uri=ODM.ConditionDef_name, domain=ConditionDef, range=str)

slots.ConditionDef_commentOID = Slot(uri=ODM.commentOID, name="ConditionDef_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.ConditionDef_commentOID, domain=ConditionDef, range=Optional[Union[str, CommentDefOID]])

slots.ConditionDef_description = Slot(uri=ODM.description, name="ConditionDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.ConditionDef_description, domain=ConditionDef, range=Optional[Union[dict, Description]])

slots.ConditionDef_methodSignature = Slot(uri=ODM.methodSignature, name="ConditionDef_methodSignature", curie=ODM.curie('methodSignature'),
                   model_uri=ODM.ConditionDef_methodSignature, domain=ConditionDef, range=Optional[Union[dict, MethodSignature]])

slots.ConditionDef_formalExpression = Slot(uri=ODM.formalExpression, name="ConditionDef_formalExpression", curie=ODM.curie('formalExpression'),
                   model_uri=ODM.ConditionDef_formalExpression, domain=ConditionDef, range=Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]])

slots.ConditionDef_alias = Slot(uri=ODM.alias, name="ConditionDef_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.ConditionDef_alias, domain=ConditionDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.FormalExpression_context = Slot(uri=ODM.context, name="FormalExpression_context", curie=ODM.curie('context'),
                   model_uri=ODM.FormalExpression_context, domain=FormalExpression, range=Optional[str])

slots.FormalExpression_code = Slot(uri=ODM.code, name="FormalExpression_code", curie=ODM.curie('code'),
                   model_uri=ODM.FormalExpression_code, domain=FormalExpression, range=Optional[Union[dict, "Code"]])

slots.FormalExpression_externalCodeLib = Slot(uri=ODM.externalCodeLib, name="FormalExpression_externalCodeLib", curie=ODM.curie('externalCodeLib'),
                   model_uri=ODM.FormalExpression_externalCodeLib, domain=FormalExpression, range=Optional[Union[dict, "ExternalCodeLib"]])

slots.Code_content = Slot(uri=ODM.content, name="Code_content", curie=ODM.curie('content'),
                   model_uri=ODM.Code_content, domain=Code, range=Optional[str])

slots.ExternalCodeLib_library = Slot(uri=ODM.library, name="ExternalCodeLib_library", curie=ODM.curie('library'),
                   model_uri=ODM.ExternalCodeLib_library, domain=ExternalCodeLib, range=str)

slots.ExternalCodeLib_method = Slot(uri=ODM.method, name="ExternalCodeLib_method", curie=ODM.curie('method'),
                   model_uri=ODM.ExternalCodeLib_method, domain=ExternalCodeLib, range=Optional[str])

slots.ExternalCodeLib_version = Slot(uri=ODM.version, name="ExternalCodeLib_version", curie=ODM.curie('version'),
                   model_uri=ODM.ExternalCodeLib_version, domain=ExternalCodeLib, range=Optional[str])

slots.ExternalCodeLib_ref = Slot(uri=ODM.ref, name="ExternalCodeLib_ref", curie=ODM.curie('ref'),
                   model_uri=ODM.ExternalCodeLib_ref, domain=ExternalCodeLib, range=Optional[str])

slots.ExternalCodeLib_href = Slot(uri=ODM.href, name="ExternalCodeLib_href", curie=ODM.curie('href'),
                   model_uri=ODM.ExternalCodeLib_href, domain=ExternalCodeLib, range=Optional[Union[str, URIorCURIE]])

slots.CommentDef_OID = Slot(uri=ODM.OID, name="CommentDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.CommentDef_OID, domain=CommentDef, range=Union[str, CommentDefOID])

slots.CommentDef_description = Slot(uri=ODM.description, name="CommentDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.CommentDef_description, domain=CommentDef, range=Optional[Union[dict, Description]])

slots.CommentDef_documentRef = Slot(uri=ODM.documentRef, name="CommentDef_documentRef", curie=ODM.curie('documentRef'),
                   model_uri=ODM.CommentDef_documentRef, domain=CommentDef, range=Optional[Union[Dict[Union[str, DocumentRefLeafID], Union[dict, DocumentRef]], List[Union[dict, DocumentRef]]]])

slots.Protocol_description = Slot(uri=ODM.description, name="Protocol_description", curie=ODM.curie('description'),
                   model_uri=ODM.Protocol_description, domain=Protocol, range=Optional[Union[dict, Description]])

slots.Protocol_studySummary = Slot(uri=ODM.studySummary, name="Protocol_studySummary", curie=ODM.curie('studySummary'),
                   model_uri=ODM.Protocol_studySummary, domain=Protocol, range=Optional[Union[dict, "StudySummary"]])

slots.Protocol_studyStructure = Slot(uri=ODM.studyStructure, name="Protocol_studyStructure", curie=ODM.curie('studyStructure'),
                   model_uri=ODM.Protocol_studyStructure, domain=Protocol, range=Optional[Union[dict, "StudyStructure"]])

slots.Protocol_trialPhase = Slot(uri=ODM.trialPhase, name="Protocol_trialPhase", curie=ODM.curie('trialPhase'),
                   model_uri=ODM.Protocol_trialPhase, domain=Protocol, range=Optional[Union[dict, "TrialPhase"]])

slots.Protocol_studyTimings = Slot(uri=ODM.studyTimings, name="Protocol_studyTimings", curie=ODM.curie('studyTimings'),
                   model_uri=ODM.Protocol_studyTimings, domain=Protocol, range=Optional[Union[dict, "StudyTimings"]])

slots.Protocol_studyIndications = Slot(uri=ODM.studyIndications, name="Protocol_studyIndications", curie=ODM.curie('studyIndications'),
                   model_uri=ODM.Protocol_studyIndications, domain=Protocol, range=Optional[Union[dict, "StudyIndications"]])

slots.Protocol_studyInterventions = Slot(uri=ODM.studyInterventions, name="Protocol_studyInterventions", curie=ODM.curie('studyInterventions'),
                   model_uri=ODM.Protocol_studyInterventions, domain=Protocol, range=Optional[Union[dict, "StudyInterventions"]])

slots.Protocol_studyObjectives = Slot(uri=ODM.studyObjectives, name="Protocol_studyObjectives", curie=ODM.curie('studyObjectives'),
                   model_uri=ODM.Protocol_studyObjectives, domain=Protocol, range=Optional[Union[dict, "StudyObjectives"]])

slots.Protocol_studyEndPoints = Slot(uri=ODM.studyEndPoints, name="Protocol_studyEndPoints", curie=ODM.curie('studyEndPoints'),
                   model_uri=ODM.Protocol_studyEndPoints, domain=Protocol, range=Optional[Union[dict, "StudyEndPoints"]])

slots.Protocol_studyTargetPopulation = Slot(uri=ODM.studyTargetPopulation, name="Protocol_studyTargetPopulation", curie=ODM.curie('studyTargetPopulation'),
                   model_uri=ODM.Protocol_studyTargetPopulation, domain=Protocol, range=Optional[Union[str, StudyTargetPopulationOID]])

slots.Protocol_studyEstimands = Slot(uri=ODM.studyEstimands, name="Protocol_studyEstimands", curie=ODM.curie('studyEstimands'),
                   model_uri=ODM.Protocol_studyEstimands, domain=Protocol, range=Optional[Union[dict, "StudyEstimands"]])

slots.Protocol_inclusionExclusionCriteria = Slot(uri=ODM.inclusionExclusionCriteria, name="Protocol_inclusionExclusionCriteria", curie=ODM.curie('inclusionExclusionCriteria'),
                   model_uri=ODM.Protocol_inclusionExclusionCriteria, domain=Protocol, range=Optional[Union[dict, "InclusionExclusionCriteria"]])

slots.Protocol_studyEventGroupRef = Slot(uri=ODM.studyEventGroupRef, name="Protocol_studyEventGroupRef", curie=ODM.curie('studyEventGroupRef'),
                   model_uri=ODM.Protocol_studyEventGroupRef, domain=Protocol, range=Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]])

slots.Protocol_workflowRef = Slot(uri=ODM.workflowRef, name="Protocol_workflowRef", curie=ODM.curie('workflowRef'),
                   model_uri=ODM.Protocol_workflowRef, domain=Protocol, range=Optional[Union[dict, "WorkflowRef"]])

slots.Protocol_alias = Slot(uri=ODM.alias, name="Protocol_alias", curie=ODM.curie('alias'),
                   model_uri=ODM.Protocol_alias, domain=Protocol, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.StudyStructure_description = Slot(uri=ODM.description, name="StudyStructure_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyStructure_description, domain=StudyStructure, range=Optional[Union[dict, Description]])

slots.StudyStructure_arm = Slot(uri=ODM.arm, name="StudyStructure_arm", curie=ODM.curie('arm'),
                   model_uri=ODM.StudyStructure_arm, domain=StudyStructure, range=Optional[Union[Dict[Union[str, ArmOID], Union[dict, "Arm"]], List[Union[dict, "Arm"]]]])

slots.StudyStructure_epoch = Slot(uri=ODM.epoch, name="StudyStructure_epoch", curie=ODM.curie('epoch'),
                   model_uri=ODM.StudyStructure_epoch, domain=StudyStructure, range=Optional[Union[Dict[Union[str, EpochOID], Union[dict, "Epoch"]], List[Union[dict, "Epoch"]]]])

slots.StudyStructure_workflowRef = Slot(uri=ODM.workflowRef, name="StudyStructure_workflowRef", curie=ODM.curie('workflowRef'),
                   model_uri=ODM.StudyStructure_workflowRef, domain=StudyStructure, range=Optional[Union[dict, "WorkflowRef"]])

slots.TrialPhase_value = Slot(uri=ODM.value, name="TrialPhase_value", curie=ODM.curie('value'),
                   model_uri=ODM.TrialPhase_value, domain=TrialPhase, range=str)

slots.TrialPhase_description = Slot(uri=ODM.description, name="TrialPhase_description", curie=ODM.curie('description'),
                   model_uri=ODM.TrialPhase_description, domain=TrialPhase, range=Optional[Union[dict, Description]])

slots.StudyIndications_studyIndication = Slot(uri=ODM.studyIndication, name="StudyIndications_studyIndication", curie=ODM.curie('studyIndication'),
                   model_uri=ODM.StudyIndications_studyIndication, domain=StudyIndications, range=Optional[Union[Dict[Union[str, StudyIndicationOID], Union[dict, "StudyIndication"]], List[Union[dict, "StudyIndication"]]]])

slots.StudyIndication_OID = Slot(uri=ODM.OID, name="StudyIndication_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyIndication_OID, domain=StudyIndication, range=Union[str, StudyIndicationOID])

slots.StudyIndication_description = Slot(uri=ODM.description, name="StudyIndication_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyIndication_description, domain=StudyIndication, range=Optional[Union[dict, Description]])

slots.StudyIndication_coding = Slot(uri=ODM.coding, name="StudyIndication_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.StudyIndication_coding, domain=StudyIndication, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyInterventions_studyIntervention = Slot(uri=ODM.studyIntervention, name="StudyInterventions_studyIntervention", curie=ODM.curie('studyIntervention'),
                   model_uri=ODM.StudyInterventions_studyIntervention, domain=StudyInterventions, range=Optional[Union[Dict[Union[str, StudyInterventionOID], Union[dict, "StudyIntervention"]], List[Union[dict, "StudyIntervention"]]]])

slots.StudyIntervention_OID = Slot(uri=ODM.OID, name="StudyIntervention_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyIntervention_OID, domain=StudyIntervention, range=Union[str, StudyInterventionOID])

slots.StudyIntervention_description = Slot(uri=ODM.description, name="StudyIntervention_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyIntervention_description, domain=StudyIntervention, range=Optional[Union[dict, Description]])

slots.StudyIntervention_coding = Slot(uri=ODM.coding, name="StudyIntervention_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.StudyIntervention_coding, domain=StudyIntervention, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyObjectives_studyObjective = Slot(uri=ODM.studyObjective, name="StudyObjectives_studyObjective", curie=ODM.curie('studyObjective'),
                   model_uri=ODM.StudyObjectives_studyObjective, domain=StudyObjectives, range=Optional[Union[Dict[Union[str, StudyObjectiveOID], Union[dict, "StudyObjective"]], List[Union[dict, "StudyObjective"]]]])

slots.StudyObjective_OID = Slot(uri=ODM.OID, name="StudyObjective_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyObjective_OID, domain=StudyObjective, range=Union[str, StudyObjectiveOID])

slots.StudyObjective_name = Slot(uri=ODM.name, name="StudyObjective_name", curie=ODM.curie('name'),
                   model_uri=ODM.StudyObjective_name, domain=StudyObjective, range=str)

slots.StudyObjective_level = Slot(uri=ODM.level, name="StudyObjective_level", curie=ODM.curie('level'),
                   model_uri=ODM.StudyObjective_level, domain=StudyObjective, range=Optional[Union[str, "StudyObjectiveLevel"]])

slots.StudyObjective_description = Slot(uri=ODM.description, name="StudyObjective_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyObjective_description, domain=StudyObjective, range=Optional[Union[dict, Description]])

slots.StudyObjective_studyEndPointRef = Slot(uri=ODM.studyEndPointRef, name="StudyObjective_studyEndPointRef", curie=ODM.curie('studyEndPointRef'),
                   model_uri=ODM.StudyObjective_studyEndPointRef, domain=StudyObjective, range=Optional[Union[Union[dict, "StudyEndPointRef"], List[Union[dict, "StudyEndPointRef"]]]])

slots.StudyEndPointRef_studyEndPointOID = Slot(uri=ODM.studyEndPointOID, name="StudyEndPointRef_studyEndPointOID", curie=ODM.curie('studyEndPointOID'),
                   model_uri=ODM.StudyEndPointRef_studyEndPointOID, domain=StudyEndPointRef, range=Union[str, StudyEndPointOID])

slots.StudyEndPointRef_orderNumber = Slot(uri=ODM.orderNumber, name="StudyEndPointRef_orderNumber", curie=ODM.curie('orderNumber'),
                   model_uri=ODM.StudyEndPointRef_orderNumber, domain=StudyEndPointRef, range=Optional[int])

slots.StudyEndPoints_studyEndPoint = Slot(uri=ODM.studyEndPoint, name="StudyEndPoints_studyEndPoint", curie=ODM.curie('studyEndPoint'),
                   model_uri=ODM.StudyEndPoints_studyEndPoint, domain=StudyEndPoints, range=Optional[Union[Dict[Union[str, StudyEndPointOID], Union[dict, "StudyEndPoint"]], List[Union[dict, "StudyEndPoint"]]]])

slots.StudyEndPoint_OID = Slot(uri=ODM.OID, name="StudyEndPoint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEndPoint_OID, domain=StudyEndPoint, range=Union[str, StudyEndPointOID])

slots.StudyEndPoint_name = Slot(uri=ODM.name, name="StudyEndPoint_name", curie=ODM.curie('name'),
                   model_uri=ODM.StudyEndPoint_name, domain=StudyEndPoint, range=str)

slots.StudyEndPoint_type = Slot(uri=ODM.type, name="StudyEndPoint_type", curie=ODM.curie('type'),
                   model_uri=ODM.StudyEndPoint_type, domain=StudyEndPoint, range=Optional[Union[str, "StudyEndPointType"]])

slots.StudyEndPoint_level = Slot(uri=ODM.level, name="StudyEndPoint_level", curie=ODM.curie('level'),
                   model_uri=ODM.StudyEndPoint_level, domain=StudyEndPoint, range=Optional[Union[str, "StudyEstimandLevel"]])

slots.StudyEndPoint_description = Slot(uri=ODM.description, name="StudyEndPoint_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyEndPoint_description, domain=StudyEndPoint, range=Optional[Union[dict, Description]])

slots.StudyEndPoint_formalExpression = Slot(uri=ODM.formalExpression, name="StudyEndPoint_formalExpression", curie=ODM.curie('formalExpression'),
                   model_uri=ODM.StudyEndPoint_formalExpression, domain=StudyEndPoint, range=Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]])

slots.StudyTargetPopulation_OID = Slot(uri=ODM.OID, name="StudyTargetPopulation_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyTargetPopulation_OID, domain=StudyTargetPopulation, range=Union[str, StudyTargetPopulationOID])

slots.StudyTargetPopulation_name = Slot(uri=ODM.name, name="StudyTargetPopulation_name", curie=ODM.curie('name'),
                   model_uri=ODM.StudyTargetPopulation_name, domain=StudyTargetPopulation, range=str)

slots.StudyTargetPopulation_description = Slot(uri=ODM.description, name="StudyTargetPopulation_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyTargetPopulation_description, domain=StudyTargetPopulation, range=Optional[Union[dict, Description]])

slots.StudyTargetPopulation_coding = Slot(uri=ODM.coding, name="StudyTargetPopulation_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.StudyTargetPopulation_coding, domain=StudyTargetPopulation, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyTargetPopulation_formalExpression = Slot(uri=ODM.formalExpression, name="StudyTargetPopulation_formalExpression", curie=ODM.curie('formalExpression'),
                   model_uri=ODM.StudyTargetPopulation_formalExpression, domain=StudyTargetPopulation, range=Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]])

slots.StudyEstimands_studyEstimand = Slot(uri=ODM.studyEstimand, name="StudyEstimands_studyEstimand", curie=ODM.curie('studyEstimand'),
                   model_uri=ODM.StudyEstimands_studyEstimand, domain=StudyEstimands, range=Optional[Union[Dict[Union[str, StudyEstimandOID], Union[dict, "StudyEstimand"]], List[Union[dict, "StudyEstimand"]]]])

slots.StudyEstimand_OID = Slot(uri=ODM.OID, name="StudyEstimand_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEstimand_OID, domain=StudyEstimand, range=Union[str, StudyEstimandOID])

slots.StudyEstimand_name = Slot(uri=ODM.name, name="StudyEstimand_name", curie=ODM.curie('name'),
                   model_uri=ODM.StudyEstimand_name, domain=StudyEstimand, range=str)

slots.StudyEstimand_level = Slot(uri=ODM.level, name="StudyEstimand_level", curie=ODM.curie('level'),
                   model_uri=ODM.StudyEstimand_level, domain=StudyEstimand, range=Optional[Union[str, "StudyEstimandLevel"]])

slots.StudyEstimand_description = Slot(uri=ODM.description, name="StudyEstimand_description", curie=ODM.curie('description'),
                   model_uri=ODM.StudyEstimand_description, domain=StudyEstimand, range=Optional[Union[dict, Description]])

slots.StudyEstimand_studyTargetPopulationRef = Slot(uri=ODM.studyTargetPopulationRef, name="StudyEstimand_studyTargetPopulationRef", curie=ODM.curie('studyTargetPopulationRef'),
                   model_uri=ODM.StudyEstimand_studyTargetPopulationRef, domain=StudyEstimand, range=Optional[Union[dict, "StudyTargetPopulationRef"]])

slots.StudyEstimand_studyInterventionRef = Slot(uri=ODM.studyInterventionRef, name="StudyEstimand_studyInterventionRef", curie=ODM.curie('studyInterventionRef'),
                   model_uri=ODM.StudyEstimand_studyInterventionRef, domain=StudyEstimand, range=Optional[Union[dict, "StudyInterventionRef"]])

slots.StudyEstimand_studyEndPointRef = Slot(uri=ODM.studyEndPointRef, name="StudyEstimand_studyEndPointRef", curie=ODM.curie('studyEndPointRef'),
                   model_uri=ODM.StudyEstimand_studyEndPointRef, domain=StudyEstimand, range=Optional[Union[dict, StudyEndPointRef]])

slots.StudyEstimand_intercurrentEvent = Slot(uri=ODM.intercurrentEvent, name="StudyEstimand_intercurrentEvent", curie=ODM.curie('intercurrentEvent'),
                   model_uri=ODM.StudyEstimand_intercurrentEvent, domain=StudyEstimand, range=Optional[Union[Union[dict, "IntercurrentEvent"], List[Union[dict, "IntercurrentEvent"]]]])

slots.StudyEstimand_summaryMeasure = Slot(uri=ODM.summaryMeasure, name="StudyEstimand_summaryMeasure", curie=ODM.curie('summaryMeasure'),
                   model_uri=ODM.StudyEstimand_summaryMeasure, domain=StudyEstimand, range=Optional[Union[dict, "SummaryMeasure"]])

slots.InclusionExclusionCriteria_inclusionCriteria = Slot(uri=ODM.inclusionCriteria, name="InclusionExclusionCriteria_inclusionCriteria", curie=ODM.curie('inclusionCriteria'),
                   model_uri=ODM.InclusionExclusionCriteria_inclusionCriteria, domain=InclusionExclusionCriteria, range=Optional[Union[dict, "InclusionCriteria"]])

slots.InclusionExclusionCriteria_exclusionCriteria = Slot(uri=ODM.exclusionCriteria, name="InclusionExclusionCriteria_exclusionCriteria", curie=ODM.curie('exclusionCriteria'),
                   model_uri=ODM.InclusionExclusionCriteria_exclusionCriteria, domain=InclusionExclusionCriteria, range=Optional[Union[dict, "ExclusionCriteria"]])

slots.InclusionCriteria_criterion = Slot(uri=ODM.criterion, name="InclusionCriteria_criterion", curie=ODM.curie('criterion'),
                   model_uri=ODM.InclusionCriteria_criterion, domain=InclusionCriteria, range=Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]])

slots.ExclusionCriteria_criterion = Slot(uri=ODM.criterion, name="ExclusionCriteria_criterion", curie=ODM.curie('criterion'),
                   model_uri=ODM.ExclusionCriteria_criterion, domain=ExclusionCriteria, range=Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]])

slots.StudyTargetPopulationRef_studyTargetPopulationOID = Slot(uri=ODM.studyTargetPopulationOID, name="StudyTargetPopulationRef_studyTargetPopulationOID", curie=ODM.curie('studyTargetPopulationOID'),
                   model_uri=ODM.StudyTargetPopulationRef_studyTargetPopulationOID, domain=StudyTargetPopulationRef, range=Union[str, StudyTargetPopulationOID])

slots.StudyInterventionRef_studyInterventionOID = Slot(uri=ODM.studyInterventionOID, name="StudyInterventionRef_studyInterventionOID", curie=ODM.curie('studyInterventionOID'),
                   model_uri=ODM.StudyInterventionRef_studyInterventionOID, domain=StudyInterventionRef, range=Union[str, StudyInterventionOID])

slots.IntercurrentEvent_description = Slot(uri=ODM.description, name="IntercurrentEvent_description", curie=ODM.curie('description'),
                   model_uri=ODM.IntercurrentEvent_description, domain=IntercurrentEvent, range=Optional[Union[dict, Description]])

slots.SummaryMeasure_description = Slot(uri=ODM.description, name="SummaryMeasure_description", curie=ODM.curie('description'),
                   model_uri=ODM.SummaryMeasure_description, domain=SummaryMeasure, range=Optional[Union[dict, Description]])

slots.Arm_OID = Slot(uri=ODM.OID, name="Arm_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Arm_OID, domain=Arm, range=Union[str, ArmOID])

slots.Arm_name = Slot(uri=ODM.name, name="Arm_name", curie=ODM.curie('name'),
                   model_uri=ODM.Arm_name, domain=Arm, range=str)

slots.Arm_description = Slot(uri=ODM.description, name="Arm_description", curie=ODM.curie('description'),
                   model_uri=ODM.Arm_description, domain=Arm, range=Optional[Union[dict, Description]])

slots.Arm_workflowRef = Slot(uri=ODM.workflowRef, name="Arm_workflowRef", curie=ODM.curie('workflowRef'),
                   model_uri=ODM.Arm_workflowRef, domain=Arm, range=Optional[Union[dict, "WorkflowRef"]])

slots.Epoch_OID = Slot(uri=ODM.OID, name="Epoch_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Epoch_OID, domain=Epoch, range=Union[str, EpochOID])

slots.Epoch_name = Slot(uri=ODM.name, name="Epoch_name", curie=ODM.curie('name'),
                   model_uri=ODM.Epoch_name, domain=Epoch, range=str)

slots.Epoch_sequenceNumber = Slot(uri=ODM.sequenceNumber, name="Epoch_sequenceNumber", curie=ODM.curie('sequenceNumber'),
                   model_uri=ODM.Epoch_sequenceNumber, domain=Epoch, range=int)

slots.Epoch_description = Slot(uri=ODM.description, name="Epoch_description", curie=ODM.curie('description'),
                   model_uri=ODM.Epoch_description, domain=Epoch, range=Optional[Union[dict, Description]])

slots.WorkflowRef_workflowOID = Slot(uri=ODM.workflowOID, name="WorkflowRef_workflowOID", curie=ODM.curie('workflowOID'),
                   model_uri=ODM.WorkflowRef_workflowOID, domain=WorkflowRef, range=Union[str, WorkflowDefOID])

slots.StudySummary_studyParameter = Slot(uri=ODM.studyParameter, name="StudySummary_studyParameter", curie=ODM.curie('studyParameter'),
                   model_uri=ODM.StudySummary_studyParameter, domain=StudySummary, range=Optional[Union[Dict[Union[str, StudyParameterOID], Union[dict, "StudyParameter"]], List[Union[dict, "StudyParameter"]]]])

slots.StudyParameter_OID = Slot(uri=ODM.OID, name="StudyParameter_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyParameter_OID, domain=StudyParameter, range=Union[str, StudyParameterOID])

slots.StudyParameter_term = Slot(uri=ODM.term, name="StudyParameter_term", curie=ODM.curie('term'),
                   model_uri=ODM.StudyParameter_term, domain=StudyParameter, range=str)

slots.StudyParameter_shortName = Slot(uri=ODM.shortName, name="StudyParameter_shortName", curie=ODM.curie('shortName'),
                   model_uri=ODM.StudyParameter_shortName, domain=StudyParameter, range=Optional[str])

slots.StudyParameter_parameterValue = Slot(uri=ODM.parameterValue, name="StudyParameter_parameterValue", curie=ODM.curie('parameterValue'),
                   model_uri=ODM.StudyParameter_parameterValue, domain=StudyParameter, range=Optional[Union[dict, "ParameterValue"]])

slots.StudyParameter_coding = Slot(uri=ODM.coding, name="StudyParameter_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.StudyParameter_coding, domain=StudyParameter, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.ParameterValue_value = Slot(uri=ODM.value, name="ParameterValue_value", curie=ODM.curie('value'),
                   model_uri=ODM.ParameterValue_value, domain=ParameterValue, range=str)

slots.ParameterValue_coding = Slot(uri=ODM.coding, name="ParameterValue_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.ParameterValue_coding, domain=ParameterValue, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyTimings_studyTiming = Slot(uri=ODM.studyTiming, name="StudyTimings_studyTiming", curie=ODM.curie('studyTiming'),
                   model_uri=ODM.StudyTimings_studyTiming, domain=StudyTimings, range=Optional[Union[Dict[Union[str, StudyTimingOID], Union[dict, "StudyTiming"]], List[Union[dict, "StudyTiming"]]]])

slots.StudyTiming_OID = Slot(uri=ODM.OID, name="StudyTiming_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyTiming_OID, domain=StudyTiming, range=Union[str, StudyTimingOID])

slots.StudyTiming_name = Slot(uri=ODM.name, name="StudyTiming_name", curie=ODM.curie('name'),
                   model_uri=ODM.StudyTiming_name, domain=StudyTiming, range=str)

slots.StudyTiming_absoluteTimingConstraint = Slot(uri=ODM.absoluteTimingConstraint, name="StudyTiming_absoluteTimingConstraint", curie=ODM.curie('absoluteTimingConstraint'),
                   model_uri=ODM.StudyTiming_absoluteTimingConstraint, domain=StudyTiming, range=Optional[Union[Dict[Union[str, AbsoluteTimingConstraintOID], Union[dict, "AbsoluteTimingConstraint"]], List[Union[dict, "AbsoluteTimingConstraint"]]]])

slots.StudyTiming_relativeTimingConstraint = Slot(uri=ODM.relativeTimingConstraint, name="StudyTiming_relativeTimingConstraint", curie=ODM.curie('relativeTimingConstraint'),
                   model_uri=ODM.StudyTiming_relativeTimingConstraint, domain=StudyTiming, range=Optional[Union[Dict[Union[str, RelativeTimingConstraintOID], Union[dict, "RelativeTimingConstraint"]], List[Union[dict, "RelativeTimingConstraint"]]]])

slots.StudyTiming_transitionTimingConstraint = Slot(uri=ODM.transitionTimingConstraint, name="StudyTiming_transitionTimingConstraint", curie=ODM.curie('transitionTimingConstraint'),
                   model_uri=ODM.StudyTiming_transitionTimingConstraint, domain=StudyTiming, range=Optional[Union[Dict[Union[str, TransitionTimingConstraintOID], Union[dict, "TransitionTimingConstraint"]], List[Union[dict, "TransitionTimingConstraint"]]]])

slots.StudyTiming_durationTimingConstraint = Slot(uri=ODM.durationTimingConstraint, name="StudyTiming_durationTimingConstraint", curie=ODM.curie('durationTimingConstraint'),
                   model_uri=ODM.StudyTiming_durationTimingConstraint, domain=StudyTiming, range=Optional[Union[Dict[Union[str, DurationTimingConstraintOID], Union[dict, "DurationTimingConstraint"]], List[Union[dict, "DurationTimingConstraint"]]]])

slots.TransitionTimingConstraint_OID = Slot(uri=ODM.OID, name="TransitionTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.TransitionTimingConstraint_OID, domain=TransitionTimingConstraint, range=Union[str, TransitionTimingConstraintOID])

slots.TransitionTimingConstraint_name = Slot(uri=ODM.name, name="TransitionTimingConstraint_name", curie=ODM.curie('name'),
                   model_uri=ODM.TransitionTimingConstraint_name, domain=TransitionTimingConstraint, range=str)

slots.TransitionTimingConstraint_transitionOID = Slot(uri=ODM.transitionOID, name="TransitionTimingConstraint_transitionOID", curie=ODM.curie('transitionOID'),
                   model_uri=ODM.TransitionTimingConstraint_transitionOID, domain=TransitionTimingConstraint, range=Union[str, TransitionOID])

slots.TransitionTimingConstraint_methodOID = Slot(uri=ODM.methodOID, name="TransitionTimingConstraint_methodOID", curie=ODM.curie('methodOID'),
                   model_uri=ODM.TransitionTimingConstraint_methodOID, domain=TransitionTimingConstraint, range=Optional[Union[str, MethodDefOID]])

slots.TransitionTimingConstraint_type = Slot(uri=ODM.type, name="TransitionTimingConstraint_type", curie=ODM.curie('type'),
                   model_uri=ODM.TransitionTimingConstraint_type, domain=TransitionTimingConstraint, range=Optional[Union[str, "RelativeTimingConstraintType"]])

slots.TransitionTimingConstraint_timepointTarget = Slot(uri=ODM.timepointTarget, name="TransitionTimingConstraint_timepointTarget", curie=ODM.curie('timepointTarget'),
                   model_uri=ODM.TransitionTimingConstraint_timepointTarget, domain=TransitionTimingConstraint, range=str)

slots.TransitionTimingConstraint_timepointPreWindow = Slot(uri=ODM.timepointPreWindow, name="TransitionTimingConstraint_timepointPreWindow", curie=ODM.curie('timepointPreWindow'),
                   model_uri=ODM.TransitionTimingConstraint_timepointPreWindow, domain=TransitionTimingConstraint, range=Optional[str])

slots.TransitionTimingConstraint_timepointPostWindow = Slot(uri=ODM.timepointPostWindow, name="TransitionTimingConstraint_timepointPostWindow", curie=ODM.curie('timepointPostWindow'),
                   model_uri=ODM.TransitionTimingConstraint_timepointPostWindow, domain=TransitionTimingConstraint, range=Optional[str])

slots.TransitionTimingConstraint_description = Slot(uri=ODM.description, name="TransitionTimingConstraint_description", curie=ODM.curie('description'),
                   model_uri=ODM.TransitionTimingConstraint_description, domain=TransitionTimingConstraint, range=Optional[Union[dict, Description]])

slots.AbsoluteTimingConstraint_OID = Slot(uri=ODM.OID, name="AbsoluteTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.AbsoluteTimingConstraint_OID, domain=AbsoluteTimingConstraint, range=Union[str, AbsoluteTimingConstraintOID])

slots.AbsoluteTimingConstraint_name = Slot(uri=ODM.name, name="AbsoluteTimingConstraint_name", curie=ODM.curie('name'),
                   model_uri=ODM.AbsoluteTimingConstraint_name, domain=AbsoluteTimingConstraint, range=str)

slots.AbsoluteTimingConstraint_studyEventGroupOID = Slot(uri=ODM.studyEventGroupOID, name="AbsoluteTimingConstraint_studyEventGroupOID", curie=ODM.curie('studyEventGroupOID'),
                   model_uri=ODM.AbsoluteTimingConstraint_studyEventGroupOID, domain=AbsoluteTimingConstraint, range=Optional[Union[str, StudyEventGroupDefOID]])

slots.AbsoluteTimingConstraint_studyEventOID = Slot(uri=ODM.studyEventOID, name="AbsoluteTimingConstraint_studyEventOID", curie=ODM.curie('studyEventOID'),
                   model_uri=ODM.AbsoluteTimingConstraint_studyEventOID, domain=AbsoluteTimingConstraint, range=Optional[Union[str, StudyEventDefOID]])

slots.AbsoluteTimingConstraint_timepointTarget = Slot(uri=ODM.timepointTarget, name="AbsoluteTimingConstraint_timepointTarget", curie=ODM.curie('timepointTarget'),
                   model_uri=ODM.AbsoluteTimingConstraint_timepointTarget, domain=AbsoluteTimingConstraint, range=str)

slots.AbsoluteTimingConstraint_timepointPreWindow = Slot(uri=ODM.timepointPreWindow, name="AbsoluteTimingConstraint_timepointPreWindow", curie=ODM.curie('timepointPreWindow'),
                   model_uri=ODM.AbsoluteTimingConstraint_timepointPreWindow, domain=AbsoluteTimingConstraint, range=Optional[str])

slots.AbsoluteTimingConstraint_timepointPostWindow = Slot(uri=ODM.timepointPostWindow, name="AbsoluteTimingConstraint_timepointPostWindow", curie=ODM.curie('timepointPostWindow'),
                   model_uri=ODM.AbsoluteTimingConstraint_timepointPostWindow, domain=AbsoluteTimingConstraint, range=Optional[str])

slots.AbsoluteTimingConstraint_description = Slot(uri=ODM.description, name="AbsoluteTimingConstraint_description", curie=ODM.curie('description'),
                   model_uri=ODM.AbsoluteTimingConstraint_description, domain=AbsoluteTimingConstraint, range=Optional[Union[dict, Description]])

slots.RelativeTimingConstraint_OID = Slot(uri=ODM.OID, name="RelativeTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.RelativeTimingConstraint_OID, domain=RelativeTimingConstraint, range=Union[str, RelativeTimingConstraintOID])

slots.RelativeTimingConstraint_name = Slot(uri=ODM.name, name="RelativeTimingConstraint_name", curie=ODM.curie('name'),
                   model_uri=ODM.RelativeTimingConstraint_name, domain=RelativeTimingConstraint, range=str)

slots.RelativeTimingConstraint_predecessorOID = Slot(uri=ODM.predecessorOID, name="RelativeTimingConstraint_predecessorOID", curie=ODM.curie('predecessorOID'),
                   model_uri=ODM.RelativeTimingConstraint_predecessorOID, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_successorOID = Slot(uri=ODM.successorOID, name="RelativeTimingConstraint_successorOID", curie=ODM.curie('successorOID'),
                   model_uri=ODM.RelativeTimingConstraint_successorOID, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_type = Slot(uri=ODM.type, name="RelativeTimingConstraint_type", curie=ODM.curie('type'),
                   model_uri=ODM.RelativeTimingConstraint_type, domain=RelativeTimingConstraint, range=Optional[Union[str, "RelativeTimingConstraintType"]])

slots.RelativeTimingConstraint_timepointRelativeTarget = Slot(uri=ODM.timepointRelativeTarget, name="RelativeTimingConstraint_timepointRelativeTarget", curie=ODM.curie('timepointRelativeTarget'),
                   model_uri=ODM.RelativeTimingConstraint_timepointRelativeTarget, domain=RelativeTimingConstraint, range=str)

slots.RelativeTimingConstraint_timepointPreWindow = Slot(uri=ODM.timepointPreWindow, name="RelativeTimingConstraint_timepointPreWindow", curie=ODM.curie('timepointPreWindow'),
                   model_uri=ODM.RelativeTimingConstraint_timepointPreWindow, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_timepointPostWindow = Slot(uri=ODM.timepointPostWindow, name="RelativeTimingConstraint_timepointPostWindow", curie=ODM.curie('timepointPostWindow'),
                   model_uri=ODM.RelativeTimingConstraint_timepointPostWindow, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_description = Slot(uri=ODM.description, name="RelativeTimingConstraint_description", curie=ODM.curie('description'),
                   model_uri=ODM.RelativeTimingConstraint_description, domain=RelativeTimingConstraint, range=Optional[Union[dict, Description]])

slots.DurationTimingConstraint_OID = Slot(uri=ODM.OID, name="DurationTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.DurationTimingConstraint_OID, domain=DurationTimingConstraint, range=Union[str, DurationTimingConstraintOID])

slots.DurationTimingConstraint_name = Slot(uri=ODM.name, name="DurationTimingConstraint_name", curie=ODM.curie('name'),
                   model_uri=ODM.DurationTimingConstraint_name, domain=DurationTimingConstraint, range=str)

slots.DurationTimingConstraint_structuralElementOID = Slot(uri=ODM.structuralElementOID, name="DurationTimingConstraint_structuralElementOID", curie=ODM.curie('structuralElementOID'),
                   model_uri=ODM.DurationTimingConstraint_structuralElementOID, domain=DurationTimingConstraint, range=str)

slots.DurationTimingConstraint_durationTarget = Slot(uri=ODM.durationTarget, name="DurationTimingConstraint_durationTarget", curie=ODM.curie('durationTarget'),
                   model_uri=ODM.DurationTimingConstraint_durationTarget, domain=DurationTimingConstraint, range=str)

slots.DurationTimingConstraint_durationPreWindow = Slot(uri=ODM.durationPreWindow, name="DurationTimingConstraint_durationPreWindow", curie=ODM.curie('durationPreWindow'),
                   model_uri=ODM.DurationTimingConstraint_durationPreWindow, domain=DurationTimingConstraint, range=Optional[str])

slots.DurationTimingConstraint_durationPostWindow = Slot(uri=ODM.durationPostWindow, name="DurationTimingConstraint_durationPostWindow", curie=ODM.curie('durationPostWindow'),
                   model_uri=ODM.DurationTimingConstraint_durationPostWindow, domain=DurationTimingConstraint, range=Optional[str])

slots.DurationTimingConstraint_description = Slot(uri=ODM.description, name="DurationTimingConstraint_description", curie=ODM.curie('description'),
                   model_uri=ODM.DurationTimingConstraint_description, domain=DurationTimingConstraint, range=Optional[Union[dict, Description]])

slots.WorkflowDef_OID = Slot(uri=ODM.OID, name="WorkflowDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.WorkflowDef_OID, domain=WorkflowDef, range=Union[str, WorkflowDefOID])

slots.WorkflowDef_name = Slot(uri=ODM.name, name="WorkflowDef_name", curie=ODM.curie('name'),
                   model_uri=ODM.WorkflowDef_name, domain=WorkflowDef, range=str)

slots.WorkflowDef_description = Slot(uri=ODM.description, name="WorkflowDef_description", curie=ODM.curie('description'),
                   model_uri=ODM.WorkflowDef_description, domain=WorkflowDef, range=Optional[Union[dict, Description]])

slots.WorkflowDef_workflowStart = Slot(uri=ODM.workflowStart, name="WorkflowDef_workflowStart", curie=ODM.curie('workflowStart'),
                   model_uri=ODM.WorkflowDef_workflowStart, domain=WorkflowDef, range=Optional[Union[dict, "WorkflowStart"]])

slots.WorkflowDef_workflowEnd = Slot(uri=ODM.workflowEnd, name="WorkflowDef_workflowEnd", curie=ODM.curie('workflowEnd'),
                   model_uri=ODM.WorkflowDef_workflowEnd, domain=WorkflowDef, range=Optional[Union[Union[dict, "WorkflowEnd"], List[Union[dict, "WorkflowEnd"]]]])

slots.WorkflowDef_transition = Slot(uri=ODM.transition, name="WorkflowDef_transition", curie=ODM.curie('transition'),
                   model_uri=ODM.WorkflowDef_transition, domain=WorkflowDef, range=Optional[Union[Dict[Union[str, TransitionOID], Union[dict, "Transition"]], List[Union[dict, "Transition"]]]])

slots.WorkflowDef_branching = Slot(uri=ODM.branching, name="WorkflowDef_branching", curie=ODM.curie('branching'),
                   model_uri=ODM.WorkflowDef_branching, domain=WorkflowDef, range=Optional[Union[Dict[Union[str, BranchingOID], Union[dict, "Branching"]], List[Union[dict, "Branching"]]]])

slots.WorkflowStart_startOID = Slot(uri=ODM.startOID, name="WorkflowStart_startOID", curie=ODM.curie('startOID'),
                   model_uri=ODM.WorkflowStart_startOID, domain=WorkflowStart, range=str)

slots.Transition_OID = Slot(uri=ODM.OID, name="Transition_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Transition_OID, domain=Transition, range=Union[str, TransitionOID])

slots.Transition_name = Slot(uri=ODM.name, name="Transition_name", curie=ODM.curie('name'),
                   model_uri=ODM.Transition_name, domain=Transition, range=str)

slots.Transition_sourceOID = Slot(uri=ODM.sourceOID, name="Transition_sourceOID", curie=ODM.curie('sourceOID'),
                   model_uri=ODM.Transition_sourceOID, domain=Transition, range=str)

slots.Transition_targetOID = Slot(uri=ODM.targetOID, name="Transition_targetOID", curie=ODM.curie('targetOID'),
                   model_uri=ODM.Transition_targetOID, domain=Transition, range=str)

slots.Transition_startConditionOID = Slot(uri=ODM.startConditionOID, name="Transition_startConditionOID", curie=ODM.curie('startConditionOID'),
                   model_uri=ODM.Transition_startConditionOID, domain=Transition, range=Optional[Union[str, ConditionDefOID]])

slots.Transition_endConditionOID = Slot(uri=ODM.endConditionOID, name="Transition_endConditionOID", curie=ODM.curie('endConditionOID'),
                   model_uri=ODM.Transition_endConditionOID, domain=Transition, range=Optional[Union[str, ConditionDefOID]])

slots.Branching_OID = Slot(uri=ODM.OID, name="Branching_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Branching_OID, domain=Branching, range=Union[str, BranchingOID])

slots.Branching_name = Slot(uri=ODM.name, name="Branching_name", curie=ODM.curie('name'),
                   model_uri=ODM.Branching_name, domain=Branching, range=str)

slots.Branching_type = Slot(uri=ODM.type, name="Branching_type", curie=ODM.curie('type'),
                   model_uri=ODM.Branching_type, domain=Branching, range=Union[str, "BranchingType"])

slots.Branching_targetTransition = Slot(uri=ODM.targetTransition, name="Branching_targetTransition", curie=ODM.curie('targetTransition'),
                   model_uri=ODM.Branching_targetTransition, domain=Branching, range=Optional[Union[Union[dict, "TargetTransition"], List[Union[dict, "TargetTransition"]]]])

slots.Branching_defaultTransition = Slot(uri=ODM.defaultTransition, name="Branching_defaultTransition", curie=ODM.curie('defaultTransition'),
                   model_uri=ODM.Branching_defaultTransition, domain=Branching, range=Optional[Union[Union[dict, "DefaultTransition"], List[Union[dict, "DefaultTransition"]]]])

slots.TargetTransition_targetTransitionOID = Slot(uri=ODM.targetTransitionOID, name="TargetTransition_targetTransitionOID", curie=ODM.curie('targetTransitionOID'),
                   model_uri=ODM.TargetTransition_targetTransitionOID, domain=TargetTransition, range=Union[str, TransitionOID])

slots.TargetTransition_conditionOID = Slot(uri=ODM.conditionOID, name="TargetTransition_conditionOID", curie=ODM.curie('conditionOID'),
                   model_uri=ODM.TargetTransition_conditionOID, domain=TargetTransition, range=Optional[Union[str, ConditionDefOID]])

slots.DefaultTransition_targetTransitionOID = Slot(uri=ODM.targetTransitionOID, name="DefaultTransition_targetTransitionOID", curie=ODM.curie('targetTransitionOID'),
                   model_uri=ODM.DefaultTransition_targetTransitionOID, domain=DefaultTransition, range=Union[str, TransitionOID])

slots.WorkflowEnd_endOID = Slot(uri=ODM.endOID, name="WorkflowEnd_endOID", curie=ODM.curie('endOID'),
                   model_uri=ODM.WorkflowEnd_endOID, domain=WorkflowEnd, range=str)

slots.WorkflowEnd_content = Slot(uri=ODM.content, name="WorkflowEnd_content", curie=ODM.curie('content'),
                   model_uri=ODM.WorkflowEnd_content, domain=WorkflowEnd, range=Optional[str])

slots.Criterion_OID = Slot(uri=ODM.OID, name="Criterion_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Criterion_OID, domain=Criterion, range=Union[str, CriterionOID])

slots.Criterion_name = Slot(uri=ODM.name, name="Criterion_name", curie=ODM.curie('name'),
                   model_uri=ODM.Criterion_name, domain=Criterion, range=str)

slots.Criterion_conditionOID = Slot(uri=ODM.conditionOID, name="Criterion_conditionOID", curie=ODM.curie('conditionOID'),
                   model_uri=ODM.Criterion_conditionOID, domain=Criterion, range=Union[str, ConditionDefOID])

slots.Criterion_description = Slot(uri=ODM.description, name="Criterion_description", curie=ODM.curie('description'),
                   model_uri=ODM.Criterion_description, domain=Criterion, range=Optional[Union[dict, Description]])

slots.Criterion_coding = Slot(uri=ODM.coding, name="Criterion_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.Criterion_coding, domain=Criterion, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.AdminData_studyOID = Slot(uri=ODM.studyOID, name="AdminData_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.AdminData_studyOID, domain=AdminData, range=Optional[Union[str, StudyOID]])

slots.AdminData_user = Slot(uri=ODM.user, name="AdminData_user", curie=ODM.curie('user'),
                   model_uri=ODM.AdminData_user, domain=AdminData, range=Optional[Union[Dict[Union[str, UserOID], Union[dict, "User"]], List[Union[dict, "User"]]]])

slots.AdminData_organization = Slot(uri=ODM.organization, name="AdminData_organization", curie=ODM.curie('organization'),
                   model_uri=ODM.AdminData_organization, domain=AdminData, range=Optional[Union[Dict[Union[str, OrganizationOID], Union[dict, "Organization"]], List[Union[dict, "Organization"]]]])

slots.AdminData_location = Slot(uri=ODM.location, name="AdminData_location", curie=ODM.curie('location'),
                   model_uri=ODM.AdminData_location, domain=AdminData, range=Optional[Union[Dict[Union[str, LocationOID], Union[dict, "Location"]], List[Union[dict, "Location"]]]])

slots.AdminData_signatureDef = Slot(uri=ODM.signatureDef, name="AdminData_signatureDef", curie=ODM.curie('signatureDef'),
                   model_uri=ODM.AdminData_signatureDef, domain=AdminData, range=Optional[Union[Dict[Union[str, SignatureDefOID], Union[dict, "SignatureDef"]], List[Union[dict, "SignatureDef"]]]])

slots.User_OID = Slot(uri=ODM.OID, name="User_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.User_OID, domain=User, range=Union[str, UserOID])

slots.User_userType = Slot(uri=ODM.userType, name="User_userType", curie=ODM.curie('userType'),
                   model_uri=ODM.User_userType, domain=User, range=Optional[Union[str, "UserType"]])

slots.User_organizationOID = Slot(uri=ODM.organizationOID, name="User_organizationOID", curie=ODM.curie('organizationOID'),
                   model_uri=ODM.User_organizationOID, domain=User, range=Optional[Union[str, OrganizationOID]])

slots.User_locationOID = Slot(uri=ODM.locationOID, name="User_locationOID", curie=ODM.curie('locationOID'),
                   model_uri=ODM.User_locationOID, domain=User, range=Optional[Union[str, LocationOID]])

slots.User_userName = Slot(uri=ODM.userName, name="User_userName", curie=ODM.curie('userName'),
                   model_uri=ODM.User_userName, domain=User, range=Optional[Union[dict, "UserName"]])

slots.User_prefix = Slot(uri=ODM.prefix, name="User_prefix", curie=ODM.curie('prefix'),
                   model_uri=ODM.User_prefix, domain=User, range=Optional[Union[dict, "Prefix"]])

slots.User_suffix = Slot(uri=ODM.suffix, name="User_suffix", curie=ODM.curie('suffix'),
                   model_uri=ODM.User_suffix, domain=User, range=Optional[Union[dict, "Suffix"]])

slots.User_fullName = Slot(uri=ODM.fullName, name="User_fullName", curie=ODM.curie('fullName'),
                   model_uri=ODM.User_fullName, domain=User, range=Optional[Union[dict, "FullName"]])

slots.User_givenName = Slot(uri=ODM.givenName, name="User_givenName", curie=ODM.curie('givenName'),
                   model_uri=ODM.User_givenName, domain=User, range=Optional[Union[dict, "GivenName"]])

slots.User_familyName = Slot(uri=ODM.familyName, name="User_familyName", curie=ODM.curie('familyName'),
                   model_uri=ODM.User_familyName, domain=User, range=Optional[Union[dict, "FamilyName"]])

slots.User_image = Slot(uri=ODM.image, name="User_image", curie=ODM.curie('image'),
                   model_uri=ODM.User_image, domain=User, range=Optional[Union[dict, "Image"]])

slots.User_address = Slot(uri=ODM.address, name="User_address", curie=ODM.curie('address'),
                   model_uri=ODM.User_address, domain=User, range=Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]])

slots.User_telecom = Slot(uri=ODM.telecom, name="User_telecom", curie=ODM.curie('telecom'),
                   model_uri=ODM.User_telecom, domain=User, range=Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]])

slots.UserName_content = Slot(uri=ODM.content, name="UserName_content", curie=ODM.curie('content'),
                   model_uri=ODM.UserName_content, domain=UserName, range=Optional[str])

slots.Prefix_content = Slot(uri=ODM.content, name="Prefix_content", curie=ODM.curie('content'),
                   model_uri=ODM.Prefix_content, domain=Prefix, range=Optional[str])

slots.Suffix_content = Slot(uri=ODM.content, name="Suffix_content", curie=ODM.curie('content'),
                   model_uri=ODM.Suffix_content, domain=Suffix, range=Optional[str])

slots.FullName_content = Slot(uri=ODM.content, name="FullName_content", curie=ODM.curie('content'),
                   model_uri=ODM.FullName_content, domain=FullName, range=Optional[str])

slots.GivenName_content = Slot(uri=ODM.content, name="GivenName_content", curie=ODM.curie('content'),
                   model_uri=ODM.GivenName_content, domain=GivenName, range=Optional[str])

slots.FamilyName_content = Slot(uri=ODM.content, name="FamilyName_content", curie=ODM.curie('content'),
                   model_uri=ODM.FamilyName_content, domain=FamilyName, range=Optional[str])

slots.Image_imageFileName = Slot(uri=ODM.imageFileName, name="Image_imageFileName", curie=ODM.curie('imageFileName'),
                   model_uri=ODM.Image_imageFileName, domain=Image, range=Optional[URIorCURIE])

slots.Image_href = Slot(uri=ODM.href, name="Image_href", curie=ODM.curie('href'),
                   model_uri=ODM.Image_href, domain=Image, range=Optional[str])

slots.Image_mimeType = Slot(uri=ODM.mimeType, name="Image_mimeType", curie=ODM.curie('mimeType'),
                   model_uri=ODM.Image_mimeType, domain=Image, range=Optional[str])

slots.Organization_OID = Slot(uri=ODM.OID, name="Organization_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Organization_OID, domain=Organization, range=Union[str, OrganizationOID])

slots.Organization_name = Slot(uri=ODM.name, name="Organization_name", curie=ODM.curie('name'),
                   model_uri=ODM.Organization_name, domain=Organization, range=str)

slots.Organization_role = Slot(uri=ODM.role, name="Organization_role", curie=ODM.curie('role'),
                   model_uri=ODM.Organization_role, domain=Organization, range=Optional[str])

slots.Organization_type = Slot(uri=ODM.type, name="Organization_type", curie=ODM.curie('type'),
                   model_uri=ODM.Organization_type, domain=Organization, range=Union[str, "OrganizationType"])

slots.Organization_locationOID = Slot(uri=ODM.locationOID, name="Organization_locationOID", curie=ODM.curie('locationOID'),
                   model_uri=ODM.Organization_locationOID, domain=Organization, range=Optional[Union[str, LocationOID]])

slots.Organization_partOfOrganizationOID = Slot(uri=ODM.partOfOrganizationOID, name="Organization_partOfOrganizationOID", curie=ODM.curie('partOfOrganizationOID'),
                   model_uri=ODM.Organization_partOfOrganizationOID, domain=Organization, range=Optional[Union[str, OrganizationOID]])

slots.Organization_description = Slot(uri=ODM.description, name="Organization_description", curie=ODM.curie('description'),
                   model_uri=ODM.Organization_description, domain=Organization, range=Optional[Union[dict, Description]])

slots.Organization_address = Slot(uri=ODM.address, name="Organization_address", curie=ODM.curie('address'),
                   model_uri=ODM.Organization_address, domain=Organization, range=Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]])

slots.Organization_telecom = Slot(uri=ODM.telecom, name="Organization_telecom", curie=ODM.curie('telecom'),
                   model_uri=ODM.Organization_telecom, domain=Organization, range=Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]])

slots.Location_OID = Slot(uri=ODM.OID, name="Location_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Location_OID, domain=Location, range=Union[str, LocationOID])

slots.Location_name = Slot(uri=ODM.name, name="Location_name", curie=ODM.curie('name'),
                   model_uri=ODM.Location_name, domain=Location, range=str)

slots.Location_role = Slot(uri=ODM.role, name="Location_role", curie=ODM.curie('role'),
                   model_uri=ODM.Location_role, domain=Location, range=Optional[str])

slots.Location_organizationOID = Slot(uri=ODM.organizationOID, name="Location_organizationOID", curie=ODM.curie('organizationOID'),
                   model_uri=ODM.Location_organizationOID, domain=Location, range=Optional[Union[str, OrganizationOID]])

slots.Location_description = Slot(uri=ODM.description, name="Location_description", curie=ODM.curie('description'),
                   model_uri=ODM.Location_description, domain=Location, range=Optional[Union[dict, Description]])

slots.Location_metaDataVersionRef = Slot(uri=ODM.metaDataVersionRef, name="Location_metaDataVersionRef", curie=ODM.curie('metaDataVersionRef'),
                   model_uri=ODM.Location_metaDataVersionRef, domain=Location, range=Optional[Union[Union[dict, "MetaDataVersionRef"], List[Union[dict, "MetaDataVersionRef"]]]])

slots.Location_address = Slot(uri=ODM.address, name="Location_address", curie=ODM.curie('address'),
                   model_uri=ODM.Location_address, domain=Location, range=Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]])

slots.Location_telecom = Slot(uri=ODM.telecom, name="Location_telecom", curie=ODM.curie('telecom'),
                   model_uri=ODM.Location_telecom, domain=Location, range=Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]])

slots.Location_query = Slot(uri=ODM.query, name="Location_query", curie=ODM.curie('query'),
                   model_uri=ODM.Location_query, domain=Location, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.Address_streetName = Slot(uri=ODM.streetName, name="Address_streetName", curie=ODM.curie('streetName'),
                   model_uri=ODM.Address_streetName, domain=Address, range=Optional[Union[dict, "StreetName"]])

slots.Address_houseNumber = Slot(uri=ODM.houseNumber, name="Address_houseNumber", curie=ODM.curie('houseNumber'),
                   model_uri=ODM.Address_houseNumber, domain=Address, range=Optional[Union[dict, "HouseNumber"]])

slots.Address_city = Slot(uri=ODM.city, name="Address_city", curie=ODM.curie('city'),
                   model_uri=ODM.Address_city, domain=Address, range=Optional[Union[dict, "City"]])

slots.Address_stateProv = Slot(uri=ODM.stateProv, name="Address_stateProv", curie=ODM.curie('stateProv'),
                   model_uri=ODM.Address_stateProv, domain=Address, range=Optional[Union[dict, "StateProv"]])

slots.Address_country = Slot(uri=ODM.country, name="Address_country", curie=ODM.curie('country'),
                   model_uri=ODM.Address_country, domain=Address, range=Optional[Union[dict, "Country"]])

slots.Address_postalCode = Slot(uri=ODM.postalCode, name="Address_postalCode", curie=ODM.curie('postalCode'),
                   model_uri=ODM.Address_postalCode, domain=Address, range=Optional[Union[dict, "PostalCode"]])

slots.Address_geoPosition = Slot(uri=ODM.geoPosition, name="Address_geoPosition", curie=ODM.curie('geoPosition'),
                   model_uri=ODM.Address_geoPosition, domain=Address, range=Optional[Union[dict, "GeoPosition"]])

slots.Address_otherText = Slot(uri=ODM.otherText, name="Address_otherText", curie=ODM.curie('otherText'),
                   model_uri=ODM.Address_otherText, domain=Address, range=Optional[Union[dict, "OtherText"]])

slots.Telecom_telecomType = Slot(uri=ODM.telecomType, name="Telecom_telecomType", curie=ODM.curie('telecomType'),
                   model_uri=ODM.Telecom_telecomType, domain=Telecom, range=Union[str, "TelecomTypeType"])

slots.Telecom_value = Slot(uri=ODM.value, name="Telecom_value", curie=ODM.curie('value'),
                   model_uri=ODM.Telecom_value, domain=Telecom, range=str)

slots.StreetName_content = Slot(uri=ODM.content, name="StreetName_content", curie=ODM.curie('content'),
                   model_uri=ODM.StreetName_content, domain=StreetName, range=Optional[str])

slots.HouseNumber_content = Slot(uri=ODM.content, name="HouseNumber_content", curie=ODM.curie('content'),
                   model_uri=ODM.HouseNumber_content, domain=HouseNumber, range=Optional[str])

slots.City_content = Slot(uri=ODM.content, name="City_content", curie=ODM.curie('content'),
                   model_uri=ODM.City_content, domain=City, range=Optional[str])

slots.StateProv_content = Slot(uri=ODM.content, name="StateProv_content", curie=ODM.curie('content'),
                   model_uri=ODM.StateProv_content, domain=StateProv, range=Optional[str])

slots.Country_content = Slot(uri=ODM.content, name="Country_content", curie=ODM.curie('content'),
                   model_uri=ODM.Country_content, domain=Country, range=Optional[str])

slots.PostalCode_content = Slot(uri=ODM.content, name="PostalCode_content", curie=ODM.curie('content'),
                   model_uri=ODM.PostalCode_content, domain=PostalCode, range=Optional[str])

slots.GeoPosition_longitude = Slot(uri=ODM.longitude, name="GeoPosition_longitude", curie=ODM.curie('longitude'),
                   model_uri=ODM.GeoPosition_longitude, domain=GeoPosition, range=Optional[Decimal])

slots.GeoPosition_latitude = Slot(uri=ODM.latitude, name="GeoPosition_latitude", curie=ODM.curie('latitude'),
                   model_uri=ODM.GeoPosition_latitude, domain=GeoPosition, range=Optional[Decimal])

slots.GeoPosition_altitude = Slot(uri=ODM.altitude, name="GeoPosition_altitude", curie=ODM.curie('altitude'),
                   model_uri=ODM.GeoPosition_altitude, domain=GeoPosition, range=Optional[Decimal])

slots.OtherText_content = Slot(uri=ODM.content, name="OtherText_content", curie=ODM.curie('content'),
                   model_uri=ODM.OtherText_content, domain=OtherText, range=Optional[str])

slots.MetaDataVersionRef_studyOID = Slot(uri=ODM.studyOID, name="MetaDataVersionRef_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.MetaDataVersionRef_studyOID, domain=MetaDataVersionRef, range=Union[str, StudyOID])

slots.MetaDataVersionRef_metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="MetaDataVersionRef_metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.MetaDataVersionRef_metaDataVersionOID, domain=MetaDataVersionRef, range=Union[str, MetaDataVersionOID])

slots.MetaDataVersionRef_effectiveDate = Slot(uri=ODM.effectiveDate, name="MetaDataVersionRef_effectiveDate", curie=ODM.curie('effectiveDate'),
                   model_uri=ODM.MetaDataVersionRef_effectiveDate, domain=MetaDataVersionRef, range=Union[str, XSDDate])

slots.SignatureDef_OID = Slot(uri=ODM.OID, name="SignatureDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.SignatureDef_OID, domain=SignatureDef, range=Union[str, SignatureDefOID])

slots.SignatureDef_methodology = Slot(uri=ODM.methodology, name="SignatureDef_methodology", curie=ODM.curie('methodology'),
                   model_uri=ODM.SignatureDef_methodology, domain=SignatureDef, range=Optional[Union[str, "SignMethod"]])

slots.SignatureDef_meaning = Slot(uri=ODM.meaning, name="SignatureDef_meaning", curie=ODM.curie('meaning'),
                   model_uri=ODM.SignatureDef_meaning, domain=SignatureDef, range=Optional[Union[dict, "Meaning"]])

slots.SignatureDef_legalReason = Slot(uri=ODM.legalReason, name="SignatureDef_legalReason", curie=ODM.curie('legalReason'),
                   model_uri=ODM.SignatureDef_legalReason, domain=SignatureDef, range=Optional[Union[dict, "LegalReason"]])

slots.Meaning_content = Slot(uri=ODM.content, name="Meaning_content", curie=ODM.curie('content'),
                   model_uri=ODM.Meaning_content, domain=Meaning, range=Optional[str])

slots.LegalReason_content = Slot(uri=ODM.content, name="LegalReason_content", curie=ODM.curie('content'),
                   model_uri=ODM.LegalReason_content, domain=LegalReason, range=Optional[str])

slots.ReferenceData_studyOID = Slot(uri=ODM.studyOID, name="ReferenceData_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.ReferenceData_studyOID, domain=ReferenceData, range=Union[str, StudyOID])

slots.ReferenceData_metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="ReferenceData_metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.ReferenceData_metaDataVersionOID, domain=ReferenceData, range=Union[str, MetaDataVersionOID])

slots.ReferenceData_itemGroupData = Slot(uri=ODM.itemGroupData, name="ReferenceData_itemGroupData", curie=ODM.curie('itemGroupData'),
                   model_uri=ODM.ReferenceData_itemGroupData, domain=ReferenceData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.ReferenceData_auditRecord = Slot(uri=ODM.auditRecord, name="ReferenceData_auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.ReferenceData_auditRecord, domain=ReferenceData, range=Optional[Union[dict, "AuditRecord"]])

slots.ReferenceData_signature = Slot(uri=ODM.signature, name="ReferenceData_signature", curie=ODM.curie('signature'),
                   model_uri=ODM.ReferenceData_signature, domain=ReferenceData, range=Optional[Union[str, SignatureID]])

slots.ReferenceData_annotation = Slot(uri=ODM.annotation, name="ReferenceData_annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.ReferenceData_annotation, domain=ReferenceData, range=Optional[Union[str, AnnotationID]])

slots.ClinicalData_studyOID = Slot(uri=ODM.studyOID, name="ClinicalData_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.ClinicalData_studyOID, domain=ClinicalData, range=Union[str, StudyOID])

slots.ClinicalData_metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="ClinicalData_metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.ClinicalData_metaDataVersionOID, domain=ClinicalData, range=Union[str, MetaDataVersionOID])

slots.ClinicalData_subjectData = Slot(uri=ODM.subjectData, name="ClinicalData_subjectData", curie=ODM.curie('subjectData'),
                   model_uri=ODM.ClinicalData_subjectData, domain=ClinicalData, range=Optional[Union[Union[dict, "SubjectData"], List[Union[dict, "SubjectData"]]]])

slots.ClinicalData_itemGroupData = Slot(uri=ODM.itemGroupData, name="ClinicalData_itemGroupData", curie=ODM.curie('itemGroupData'),
                   model_uri=ODM.ClinicalData_itemGroupData, domain=ClinicalData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.ClinicalData_query = Slot(uri=ODM.query, name="ClinicalData_query", curie=ODM.curie('query'),
                   model_uri=ODM.ClinicalData_query, domain=ClinicalData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.ClinicalData_auditRecord = Slot(uri=ODM.auditRecord, name="ClinicalData_auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.ClinicalData_auditRecord, domain=ClinicalData, range=Optional[Union[dict, "AuditRecord"]])

slots.ClinicalData_signature = Slot(uri=ODM.signature, name="ClinicalData_signature", curie=ODM.curie('signature'),
                   model_uri=ODM.ClinicalData_signature, domain=ClinicalData, range=Optional[Union[str, SignatureID]])

slots.ClinicalData_annotation = Slot(uri=ODM.annotation, name="ClinicalData_annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.ClinicalData_annotation, domain=ClinicalData, range=Optional[Union[str, AnnotationID]])

slots.SubjectData_subjectKey = Slot(uri=ODM.subjectKey, name="SubjectData_subjectKey", curie=ODM.curie('subjectKey'),
                   model_uri=ODM.SubjectData_subjectKey, domain=SubjectData, range=str)

slots.SubjectData_transactionType = Slot(uri=ODM.transactionType, name="SubjectData_transactionType", curie=ODM.curie('transactionType'),
                   model_uri=ODM.SubjectData_transactionType, domain=SubjectData, range=Optional[Union[str, "TransactionType"]])

slots.SubjectData_investigatorRef = Slot(uri=ODM.investigatorRef, name="SubjectData_investigatorRef", curie=ODM.curie('investigatorRef'),
                   model_uri=ODM.SubjectData_investigatorRef, domain=SubjectData, range=Optional[Union[dict, "InvestigatorRef"]])

slots.SubjectData_siteRef = Slot(uri=ODM.siteRef, name="SubjectData_siteRef", curie=ODM.curie('siteRef'),
                   model_uri=ODM.SubjectData_siteRef, domain=SubjectData, range=Optional[Union[dict, "SiteRef"]])

slots.SubjectData_studyEventData = Slot(uri=ODM.studyEventData, name="SubjectData_studyEventData", curie=ODM.curie('studyEventData'),
                   model_uri=ODM.SubjectData_studyEventData, domain=SubjectData, range=Optional[Union[Union[dict, "StudyEventData"], List[Union[dict, "StudyEventData"]]]])

slots.SubjectData_query = Slot(uri=ODM.query, name="SubjectData_query", curie=ODM.curie('query'),
                   model_uri=ODM.SubjectData_query, domain=SubjectData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.SubjectData_auditRecord = Slot(uri=ODM.auditRecord, name="SubjectData_auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.SubjectData_auditRecord, domain=SubjectData, range=Optional[Union[dict, "AuditRecord"]])

slots.SubjectData_signature = Slot(uri=ODM.signature, name="SubjectData_signature", curie=ODM.curie('signature'),
                   model_uri=ODM.SubjectData_signature, domain=SubjectData, range=Optional[Union[str, SignatureID]])

slots.SubjectData_annotation = Slot(uri=ODM.annotation, name="SubjectData_annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.SubjectData_annotation, domain=SubjectData, range=Optional[Union[str, AnnotationID]])

slots.SiteRef_locationOID = Slot(uri=ODM.locationOID, name="SiteRef_locationOID", curie=ODM.curie('locationOID'),
                   model_uri=ODM.SiteRef_locationOID, domain=SiteRef, range=Union[str, LocationOID])

slots.InvestigatorRef_userOID = Slot(uri=ODM.userOID, name="InvestigatorRef_userOID", curie=ODM.curie('userOID'),
                   model_uri=ODM.InvestigatorRef_userOID, domain=InvestigatorRef, range=Union[str, UserOID])

slots.StudyEventData_studyEventOID = Slot(uri=ODM.studyEventOID, name="StudyEventData_studyEventOID", curie=ODM.curie('studyEventOID'),
                   model_uri=ODM.StudyEventData_studyEventOID, domain=StudyEventData, range=Union[str, StudyEventDefOID])

slots.StudyEventData_studyEventRepeatKey = Slot(uri=ODM.studyEventRepeatKey, name="StudyEventData_studyEventRepeatKey", curie=ODM.curie('studyEventRepeatKey'),
                   model_uri=ODM.StudyEventData_studyEventRepeatKey, domain=StudyEventData, range=Optional[str])

slots.StudyEventData_transactionType = Slot(uri=ODM.transactionType, name="StudyEventData_transactionType", curie=ODM.curie('transactionType'),
                   model_uri=ODM.StudyEventData_transactionType, domain=StudyEventData, range=Optional[Union[str, "TransactionType"]])

slots.StudyEventData_itemGroupData = Slot(uri=ODM.itemGroupData, name="StudyEventData_itemGroupData", curie=ODM.curie('itemGroupData'),
                   model_uri=ODM.StudyEventData_itemGroupData, domain=StudyEventData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.StudyEventData_query = Slot(uri=ODM.query, name="StudyEventData_query", curie=ODM.curie('query'),
                   model_uri=ODM.StudyEventData_query, domain=StudyEventData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.StudyEventData_auditRecord = Slot(uri=ODM.auditRecord, name="StudyEventData_auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.StudyEventData_auditRecord, domain=StudyEventData, range=Optional[Union[dict, "AuditRecord"]])

slots.StudyEventData_signature = Slot(uri=ODM.signature, name="StudyEventData_signature", curie=ODM.curie('signature'),
                   model_uri=ODM.StudyEventData_signature, domain=StudyEventData, range=Optional[Union[str, SignatureID]])

slots.StudyEventData_annotation = Slot(uri=ODM.annotation, name="StudyEventData_annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.StudyEventData_annotation, domain=StudyEventData, range=Optional[Union[str, AnnotationID]])

slots.ItemGroupData_itemGroupOID = Slot(uri=ODM.itemGroupOID, name="ItemGroupData_itemGroupOID", curie=ODM.curie('itemGroupOID'),
                   model_uri=ODM.ItemGroupData_itemGroupOID, domain=ItemGroupData, range=Union[str, ItemGroupDefOID])

slots.ItemGroupData_itemGroupRepeatKey = Slot(uri=ODM.itemGroupRepeatKey, name="ItemGroupData_itemGroupRepeatKey", curie=ODM.curie('itemGroupRepeatKey'),
                   model_uri=ODM.ItemGroupData_itemGroupRepeatKey, domain=ItemGroupData, range=Optional[str])

slots.ItemGroupData_transactionType = Slot(uri=ODM.transactionType, name="ItemGroupData_transactionType", curie=ODM.curie('transactionType'),
                   model_uri=ODM.ItemGroupData_transactionType, domain=ItemGroupData, range=Optional[Union[str, "TransactionType"]])

slots.ItemGroupData_itemGroupDataSeq = Slot(uri=ODM.itemGroupDataSeq, name="ItemGroupData_itemGroupDataSeq", curie=ODM.curie('itemGroupDataSeq'),
                   model_uri=ODM.ItemGroupData_itemGroupDataSeq, domain=ItemGroupData, range=Optional[int])

slots.ItemGroupData_query = Slot(uri=ODM.query, name="ItemGroupData_query", curie=ODM.curie('query'),
                   model_uri=ODM.ItemGroupData_query, domain=ItemGroupData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.ItemGroupData_itemGroupData = Slot(uri=ODM.itemGroupData, name="ItemGroupData_itemGroupData", curie=ODM.curie('itemGroupData'),
                   model_uri=ODM.ItemGroupData_itemGroupData, domain=ItemGroupData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.ItemGroupData_itemData = Slot(uri=ODM.itemData, name="ItemGroupData_itemData", curie=ODM.curie('itemData'),
                   model_uri=ODM.ItemGroupData_itemData, domain=ItemGroupData, range=Optional[Union[Union[dict, "ItemData"], List[Union[dict, "ItemData"]]]])

slots.ItemGroupData_auditRecord = Slot(uri=ODM.auditRecord, name="ItemGroupData_auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.ItemGroupData_auditRecord, domain=ItemGroupData, range=Optional[Union[dict, "AuditRecord"]])

slots.ItemGroupData_signature = Slot(uri=ODM.signature, name="ItemGroupData_signature", curie=ODM.curie('signature'),
                   model_uri=ODM.ItemGroupData_signature, domain=ItemGroupData, range=Optional[Union[str, SignatureID]])

slots.ItemGroupData_annotation = Slot(uri=ODM.annotation, name="ItemGroupData_annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.ItemGroupData_annotation, domain=ItemGroupData, range=Optional[Union[str, AnnotationID]])

slots.ItemData_itemOID = Slot(uri=ODM.itemOID, name="ItemData_itemOID", curie=ODM.curie('itemOID'),
                   model_uri=ODM.ItemData_itemOID, domain=ItemData, range=Union[str, ItemDefOID])

slots.ItemData_transactionType = Slot(uri=ODM.transactionType, name="ItemData_transactionType", curie=ODM.curie('transactionType'),
                   model_uri=ODM.ItemData_transactionType, domain=ItemData, range=Optional[Union[str, "TransactionType"]])

slots.ItemData_isNull = Slot(uri=ODM.isNull, name="ItemData_isNull", curie=ODM.curie('isNull'),
                   model_uri=ODM.ItemData_isNull, domain=ItemData, range=Optional[Union[str, "YesOnly"]])

slots.ItemData_value = Slot(uri=ODM.value, name="ItemData_value", curie=ODM.curie('value'),
                   model_uri=ODM.ItemData_value, domain=ItemData, range=Optional[Union[Union[dict, "Value"], List[Union[dict, "Value"]]]])

slots.ItemData_query = Slot(uri=ODM.query, name="ItemData_query", curie=ODM.curie('query'),
                   model_uri=ODM.ItemData_query, domain=ItemData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.ItemData_auditRecord = Slot(uri=ODM.auditRecord, name="ItemData_auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.ItemData_auditRecord, domain=ItemData, range=Optional[Union[dict, "AuditRecord"]])

slots.ItemData_signature = Slot(uri=ODM.signature, name="ItemData_signature", curie=ODM.curie('signature'),
                   model_uri=ODM.ItemData_signature, domain=ItemData, range=Optional[Union[str, SignatureID]])

slots.ItemData_annotation = Slot(uri=ODM.annotation, name="ItemData_annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.ItemData_annotation, domain=ItemData, range=Optional[Union[str, AnnotationID]])

slots.AuditRecord_editPoint = Slot(uri=ODM.editPoint, name="AuditRecord_editPoint", curie=ODM.curie('editPoint'),
                   model_uri=ODM.AuditRecord_editPoint, domain=AuditRecord, range=Optional[Union[str, "EditPointType"]])

slots.AuditRecord_usedMethod = Slot(uri=ODM.usedMethod, name="AuditRecord_usedMethod", curie=ODM.curie('usedMethod'),
                   model_uri=ODM.AuditRecord_usedMethod, domain=AuditRecord, range=Optional[Union[str, "YesOrNo"]])

slots.AuditRecord_userRef = Slot(uri=ODM.userRef, name="AuditRecord_userRef", curie=ODM.curie('userRef'),
                   model_uri=ODM.AuditRecord_userRef, domain=AuditRecord, range=Optional[Union[dict, "UserRef"]])

slots.AuditRecord_locationRef = Slot(uri=ODM.locationRef, name="AuditRecord_locationRef", curie=ODM.curie('locationRef'),
                   model_uri=ODM.AuditRecord_locationRef, domain=AuditRecord, range=Optional[Union[dict, "LocationRef"]])

slots.AuditRecord_dateTimeStamp = Slot(uri=ODM.dateTimeStamp, name="AuditRecord_dateTimeStamp", curie=ODM.curie('dateTimeStamp'),
                   model_uri=ODM.AuditRecord_dateTimeStamp, domain=AuditRecord, range=Optional[Union[dict, "DateTimeStamp"]])

slots.AuditRecord_reasonForChange = Slot(uri=ODM.reasonForChange, name="AuditRecord_reasonForChange", curie=ODM.curie('reasonForChange'),
                   model_uri=ODM.AuditRecord_reasonForChange, domain=AuditRecord, range=Optional[Union[dict, "ReasonForChange"]])

slots.AuditRecord_sourceID = Slot(uri=ODM.sourceID, name="AuditRecord_sourceID", curie=ODM.curie('sourceID'),
                   model_uri=ODM.AuditRecord_sourceID, domain=AuditRecord, range=Optional[Union[dict, "SourceID"]])

slots.UserRef_userOID = Slot(uri=ODM.userOID, name="UserRef_userOID", curie=ODM.curie('userOID'),
                   model_uri=ODM.UserRef_userOID, domain=UserRef, range=Union[str, UserOID])

slots.LocationRef_locationOID = Slot(uri=ODM.locationOID, name="LocationRef_locationOID", curie=ODM.curie('locationOID'),
                   model_uri=ODM.LocationRef_locationOID, domain=LocationRef, range=Union[str, LocationOID])

slots.DateTimeStamp_content = Slot(uri=ODM.content, name="DateTimeStamp_content", curie=ODM.curie('content'),
                   model_uri=ODM.DateTimeStamp_content, domain=DateTimeStamp, range=Optional[Union[str, XSDDateTime]])

slots.ReasonForChange_content = Slot(uri=ODM.content, name="ReasonForChange_content", curie=ODM.curie('content'),
                   model_uri=ODM.ReasonForChange_content, domain=ReasonForChange, range=Optional[str])

slots.SourceID_content = Slot(uri=ODM.content, name="SourceID_content", curie=ODM.curie('content'),
                   model_uri=ODM.SourceID_content, domain=SourceID, range=Optional[str])

slots.Signature_ID = Slot(uri=ODM.ID, name="Signature_ID", curie=ODM.curie('ID'),
                   model_uri=ODM.Signature_ID, domain=Signature, range=Union[str, SignatureID])

slots.Signature_userRef = Slot(uri=ODM.userRef, name="Signature_userRef", curie=ODM.curie('userRef'),
                   model_uri=ODM.Signature_userRef, domain=Signature, range=Optional[Union[dict, UserRef]])

slots.Signature_locationRef = Slot(uri=ODM.locationRef, name="Signature_locationRef", curie=ODM.curie('locationRef'),
                   model_uri=ODM.Signature_locationRef, domain=Signature, range=Optional[Union[dict, LocationRef]])

slots.Signature_signatureRef = Slot(uri=ODM.signatureRef, name="Signature_signatureRef", curie=ODM.curie('signatureRef'),
                   model_uri=ODM.Signature_signatureRef, domain=Signature, range=Optional[Union[dict, "SignatureRef"]])

slots.Signature_dateTimeStamp = Slot(uri=ODM.dateTimeStamp, name="Signature_dateTimeStamp", curie=ODM.curie('dateTimeStamp'),
                   model_uri=ODM.Signature_dateTimeStamp, domain=Signature, range=Optional[Union[dict, DateTimeStamp]])

slots.SignatureRef_signatureOID = Slot(uri=ODM.signatureOID, name="SignatureRef_signatureOID", curie=ODM.curie('signatureOID'),
                   model_uri=ODM.SignatureRef_signatureOID, domain=SignatureRef, range=Union[str, SignatureDefOID])

slots.Association_studyOID = Slot(uri=ODM.studyOID, name="Association_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.Association_studyOID, domain=Association, range=Union[str, StudyOID])

slots.Association_metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="Association_metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.Association_metaDataVersionOID, domain=Association, range=Union[str, MetaDataVersionOID])

slots.Association_keySet = Slot(uri=ODM.keySet, name="Association_keySet", curie=ODM.curie('keySet'),
                   model_uri=ODM.Association_keySet, domain=Association, range=Optional[Union[dict, "KeySet"]])

slots.Association_annotation = Slot(uri=ODM.annotation, name="Association_annotation", curie=ODM.curie('annotation'),
                   model_uri=ODM.Association_annotation, domain=Association, range=Optional[Union[str, AnnotationID]])

slots.KeySet_studyOID = Slot(uri=ODM.studyOID, name="KeySet_studyOID", curie=ODM.curie('studyOID'),
                   model_uri=ODM.KeySet_studyOID, domain=KeySet, range=Union[str, StudyOID])

slots.KeySet_subjectKey = Slot(uri=ODM.subjectKey, name="KeySet_subjectKey", curie=ODM.curie('subjectKey'),
                   model_uri=ODM.KeySet_subjectKey, domain=KeySet, range=Optional[str])

slots.KeySet_metaDataVersionOID = Slot(uri=ODM.metaDataVersionOID, name="KeySet_metaDataVersionOID", curie=ODM.curie('metaDataVersionOID'),
                   model_uri=ODM.KeySet_metaDataVersionOID, domain=KeySet, range=Optional[Union[str, MetaDataVersionOID]])

slots.KeySet_studyEventOID = Slot(uri=ODM.studyEventOID, name="KeySet_studyEventOID", curie=ODM.curie('studyEventOID'),
                   model_uri=ODM.KeySet_studyEventOID, domain=KeySet, range=Optional[Union[str, StudyEventDefOID]])

slots.KeySet_studyEventRepeatKey = Slot(uri=ODM.studyEventRepeatKey, name="KeySet_studyEventRepeatKey", curie=ODM.curie('studyEventRepeatKey'),
                   model_uri=ODM.KeySet_studyEventRepeatKey, domain=KeySet, range=Optional[str])

slots.KeySet_itemGroupOID = Slot(uri=ODM.itemGroupOID, name="KeySet_itemGroupOID", curie=ODM.curie('itemGroupOID'),
                   model_uri=ODM.KeySet_itemGroupOID, domain=KeySet, range=Optional[Union[str, ItemGroupDefOID]])

slots.KeySet_itemGroupRepeatKey = Slot(uri=ODM.itemGroupRepeatKey, name="KeySet_itemGroupRepeatKey", curie=ODM.curie('itemGroupRepeatKey'),
                   model_uri=ODM.KeySet_itemGroupRepeatKey, domain=KeySet, range=Optional[str])

slots.KeySet_itemOID = Slot(uri=ODM.itemOID, name="KeySet_itemOID", curie=ODM.curie('itemOID'),
                   model_uri=ODM.KeySet_itemOID, domain=KeySet, range=Optional[Union[str, ItemDefOID]])

slots.Annotation_seqNum = Slot(uri=ODM.seqNum, name="Annotation_seqNum", curie=ODM.curie('seqNum'),
                   model_uri=ODM.Annotation_seqNum, domain=Annotation, range=int)

slots.Annotation_transactionType = Slot(uri=ODM.transactionType, name="Annotation_transactionType", curie=ODM.curie('transactionType'),
                   model_uri=ODM.Annotation_transactionType, domain=Annotation, range=Optional[Union[str, "TransactionType"]])

slots.Annotation_ID = Slot(uri=ODM.ID, name="Annotation_ID", curie=ODM.curie('ID'),
                   model_uri=ODM.Annotation_ID, domain=Annotation, range=Union[str, AnnotationID])

slots.Annotation_comment = Slot(uri=ODM.comment, name="Annotation_comment", curie=ODM.curie('comment'),
                   model_uri=ODM.Annotation_comment, domain=Annotation, range=Optional[Union[dict, "Comment"]])

slots.Annotation_coding = Slot(uri=ODM.coding, name="Annotation_coding", curie=ODM.curie('coding'),
                   model_uri=ODM.Annotation_coding, domain=Annotation, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Annotation_flag = Slot(uri=ODM.flag, name="Annotation_flag", curie=ODM.curie('flag'),
                   model_uri=ODM.Annotation_flag, domain=Annotation, range=Optional[Union[Union[dict, "Flag"], List[Union[dict, "Flag"]]]])

slots.Comment_sponsorOrSite = Slot(uri=ODM.sponsorOrSite, name="Comment_sponsorOrSite", curie=ODM.curie('sponsorOrSite'),
                   model_uri=ODM.Comment_sponsorOrSite, domain=Comment, range=Optional[Union[str, "CommentType"]])

slots.Comment_translatedText = Slot(uri=ODM.translatedText, name="Comment_translatedText", curie=ODM.curie('translatedText'),
                   model_uri=ODM.Comment_translatedText, domain=Comment, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.Flag_flagValue = Slot(uri=ODM.flagValue, name="Flag_flagValue", curie=ODM.curie('flagValue'),
                   model_uri=ODM.Flag_flagValue, domain=Flag, range=Optional[Union[dict, "FlagValue"]])

slots.Flag_flagType = Slot(uri=ODM.flagType, name="Flag_flagType", curie=ODM.curie('flagType'),
                   model_uri=ODM.Flag_flagType, domain=Flag, range=Optional[Union[dict, "FlagType"]])

slots.FlagValue_codeListOID = Slot(uri=ODM.codeListOID, name="FlagValue_codeListOID", curie=ODM.curie('codeListOID'),
                   model_uri=ODM.FlagValue_codeListOID, domain=FlagValue, range=Union[str, CodeListOID])

slots.FlagValue_content = Slot(uri=ODM.content, name="FlagValue_content", curie=ODM.curie('content'),
                   model_uri=ODM.FlagValue_content, domain=FlagValue, range=Optional[str])

slots.FlagType_codeListOID = Slot(uri=ODM.codeListOID, name="FlagType_codeListOID", curie=ODM.curie('codeListOID'),
                   model_uri=ODM.FlagType_codeListOID, domain=FlagType, range=Union[str, CodeListOID])

slots.FlagType_content = Slot(uri=ODM.content, name="FlagType_content", curie=ODM.curie('content'),
                   model_uri=ODM.FlagType_content, domain=FlagType, range=Optional[str])

slots.Coding_code = Slot(uri=ODM.code, name="Coding_code", curie=ODM.curie('code'),
                   model_uri=ODM.Coding_code, domain=Coding, range=Optional[str])

slots.Coding_system = Slot(uri=ODM.system, name="Coding_system", curie=ODM.curie('system'),
                   model_uri=ODM.Coding_system, domain=Coding, range=Union[str, URIorCURIE])

slots.Coding_systemName = Slot(uri=ODM.systemName, name="Coding_systemName", curie=ODM.curie('systemName'),
                   model_uri=ODM.Coding_systemName, domain=Coding, range=Optional[str])

slots.Coding_systemVersion = Slot(uri=ODM.systemVersion, name="Coding_systemVersion", curie=ODM.curie('systemVersion'),
                   model_uri=ODM.Coding_systemVersion, domain=Coding, range=Optional[str])

slots.Coding_label = Slot(uri=ODM.label, name="Coding_label", curie=ODM.curie('label'),
                   model_uri=ODM.Coding_label, domain=Coding, range=Optional[str])

slots.Coding_href = Slot(uri=ODM.href, name="Coding_href", curie=ODM.curie('href'),
                   model_uri=ODM.Coding_href, domain=Coding, range=Optional[Union[str, URIorCURIE]])

slots.Coding_ref = Slot(uri=ODM.ref, name="Coding_ref", curie=ODM.curie('ref'),
                   model_uri=ODM.Coding_ref, domain=Coding, range=Optional[Union[str, URIorCURIE]])

slots.Coding_commentOID = Slot(uri=ODM.commentOID, name="Coding_commentOID", curie=ODM.curie('commentOID'),
                   model_uri=ODM.Coding_commentOID, domain=Coding, range=Optional[str])

slots.Query_OID = Slot(uri=ODM.OID, name="Query_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Query_OID, domain=Query, range=Union[str, QueryOID])

slots.Query_source = Slot(uri=ODM.source, name="Query_source", curie=ODM.curie('source'),
                   model_uri=ODM.Query_source, domain=Query, range=Union[str, "QuerySourceType"])

slots.Query_target = Slot(uri=ODM.target, name="Query_target", curie=ODM.curie('target'),
                   model_uri=ODM.Query_target, domain=Query, range=Optional[str])

slots.Query_type = Slot(uri=ODM.type, name="Query_type", curie=ODM.curie('type'),
                   model_uri=ODM.Query_type, domain=Query, range=Optional[Union[str, "QueryType"]])

slots.Query_state = Slot(uri=ODM.state, name="Query_state", curie=ODM.curie('state'),
                   model_uri=ODM.Query_state, domain=Query, range=Union[str, "QueryStateType"])

slots.Query_lastUpdateDatetime = Slot(uri=ODM.lastUpdateDatetime, name="Query_lastUpdateDatetime", curie=ODM.curie('lastUpdateDatetime'),
                   model_uri=ODM.Query_lastUpdateDatetime, domain=Query, range=Union[str, XSDDateTime])

slots.Query_name = Slot(uri=ODM.name, name="Query_name", curie=ODM.curie('name'),
                   model_uri=ODM.Query_name, domain=Query, range=Optional[str])

slots.Query_value = Slot(uri=ODM.value, name="Query_value", curie=ODM.curie('value'),
                   model_uri=ODM.Query_value, domain=Query, range=Optional[Union[dict, "Value"]])

slots.Query_auditRecord = Slot(uri=ODM.auditRecord, name="Query_auditRecord", curie=ODM.curie('auditRecord'),
                   model_uri=ODM.Query_auditRecord, domain=Query, range=Optional[Union[Union[dict, AuditRecord], List[Union[dict, AuditRecord]]]])

slots.Value_seqNum = Slot(uri=ODM.seqNum, name="Value_seqNum", curie=ODM.curie('seqNum'),
                   model_uri=ODM.Value_seqNum, domain=Value, range=Optional[int])

slots.Value_content = Slot(uri=ODM.content, name="Value_content", curie=ODM.curie('content'),
                   model_uri=ODM.Value_content, domain=Value, range=Optional[str])

slots.ODMFileMetadata_fileType = Slot(uri=ODM.fileType, name="ODMFileMetadata_fileType", curie=ODM.curie('fileType'),
                   model_uri=ODM.ODMFileMetadata_fileType, domain=ODMFileMetadata, range=Union[str, "FileType"])

slots.ODMFileMetadata_granularity = Slot(uri=ODM.granularity, name="ODMFileMetadata_granularity", curie=ODM.curie('granularity'),
                   model_uri=ODM.ODMFileMetadata_granularity, domain=ODMFileMetadata, range=Optional[Union[str, "Granularity"]])

slots.ODMFileMetadata_context = Slot(uri=ODM.context, name="ODMFileMetadata_context", curie=ODM.curie('context'),
                   model_uri=ODM.ODMFileMetadata_context, domain=ODMFileMetadata, range=Optional[Union[str, "Context"]])

slots.ODMFileMetadata_fileOID = Slot(uri=ODM.fileOID, name="ODMFileMetadata_fileOID", curie=ODM.curie('fileOID'),
                   model_uri=ODM.ODMFileMetadata_fileOID, domain=ODMFileMetadata, range=Union[str, ODMFileMetadataFileOID])

slots.ODMFileMetadata_creationDateTime = Slot(uri=ODM.creationDateTime, name="ODMFileMetadata_creationDateTime", curie=ODM.curie('creationDateTime'),
                   model_uri=ODM.ODMFileMetadata_creationDateTime, domain=ODMFileMetadata, range=Union[str, XSDDateTime])

slots.ODMFileMetadata_priorFileOID = Slot(uri=ODM.priorFileOID, name="ODMFileMetadata_priorFileOID", curie=ODM.curie('priorFileOID'),
                   model_uri=ODM.ODMFileMetadata_priorFileOID, domain=ODMFileMetadata, range=Optional[Union[str, ODMFileMetadataFileOID]])

slots.ODMFileMetadata_asOfDateTime = Slot(uri=ODM.asOfDateTime, name="ODMFileMetadata_asOfDateTime", curie=ODM.curie('asOfDateTime'),
                   model_uri=ODM.ODMFileMetadata_asOfDateTime, domain=ODMFileMetadata, range=Optional[Union[str, XSDDateTime]])

slots.ODMFileMetadata_oDMVersion = Slot(uri=ODM.oDMVersion, name="ODMFileMetadata_oDMVersion", curie=ODM.curie('oDMVersion'),
                   model_uri=ODM.ODMFileMetadata_oDMVersion, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_originator = Slot(uri=ODM.originator, name="ODMFileMetadata_originator", curie=ODM.curie('originator'),
                   model_uri=ODM.ODMFileMetadata_originator, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_sourceSystem = Slot(uri=ODM.sourceSystem, name="ODMFileMetadata_sourceSystem", curie=ODM.curie('sourceSystem'),
                   model_uri=ODM.ODMFileMetadata_sourceSystem, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_sourceSystemVersion = Slot(uri=ODM.sourceSystemVersion, name="ODMFileMetadata_sourceSystemVersion", curie=ODM.curie('sourceSystemVersion'),
                   model_uri=ODM.ODMFileMetadata_sourceSystemVersion, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_description = Slot(uri=ODM.description, name="ODMFileMetadata_description", curie=ODM.curie('description'),
                   model_uri=ODM.ODMFileMetadata_description, domain=ODMFileMetadata, range=Optional[Union[dict, Description]])

slots.ODMFileMetadata_study = Slot(uri=ODM.study, name="ODMFileMetadata_study", curie=ODM.curie('study'),
                   model_uri=ODM.ODMFileMetadata_study, domain=ODMFileMetadata, range=Optional[Union[Dict[Union[str, StudyOID], Union[dict, Study]], List[Union[dict, Study]]]])

slots.ODMFileMetadata_adminData = Slot(uri=ODM.adminData, name="ODMFileMetadata_adminData", curie=ODM.curie('adminData'),
                   model_uri=ODM.ODMFileMetadata_adminData, domain=ODMFileMetadata, range=Optional[Union[Union[dict, AdminData], List[Union[dict, AdminData]]]])

slots.ODMFileMetadata_referenceData = Slot(uri=ODM.referenceData, name="ODMFileMetadata_referenceData", curie=ODM.curie('referenceData'),
                   model_uri=ODM.ODMFileMetadata_referenceData, domain=ODMFileMetadata, range=Optional[Union[Union[dict, ReferenceData], List[Union[dict, ReferenceData]]]])

slots.ODMFileMetadata_clinicalData = Slot(uri=ODM.clinicalData, name="ODMFileMetadata_clinicalData", curie=ODM.curie('clinicalData'),
                   model_uri=ODM.ODMFileMetadata_clinicalData, domain=ODMFileMetadata, range=Optional[Union[Union[dict, ClinicalData], List[Union[dict, ClinicalData]]]])

slots.ODMFileMetadata_association = Slot(uri=ODM.association, name="ODMFileMetadata_association", curie=ODM.curie('association'),
                   model_uri=ODM.ODMFileMetadata_association, domain=ODMFileMetadata, range=Optional[Union[Union[dict, Association], List[Union[dict, Association]]]])