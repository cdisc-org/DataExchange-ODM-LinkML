# Auto generated from ODM.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-22T11:56:32
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
DATETIME = CurieNamespace('datetime', 'http://example.org/UNKNOWN/datetime/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCI = CurieNamespace('nci', 'http://ncicb.nci.nih.gov/xml/odm/EVS/CDISC')
ODM = CurieNamespace('odm', 'http://www.cdisc.org/ns/odm/v2.0/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
TEXT = CurieNamespace('text', 'http://example.org/UNKNOWN/text/')
VALUE = CurieNamespace('value', 'http://example.org/UNKNOWN/value/')
XHTML = CurieNamespace('xhtml', 'http://www.w3.org/1999/xhtml')
XML = CurieNamespace('xml', 'http://www.w3.org/XML/1998/namespace')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ODM


# Types
class Text(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.text
    type_class_curie = "odm:text"
    type_name = "text"
    type_model_uri = ODM.Text


class PositiveInteger(int):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.positiveInteger
    type_class_curie = "odm:positiveInteger"
    type_name = "positiveInteger"
    type_model_uri = ODM.PositiveInteger


class HexBinary(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.hexBinary
    type_class_curie = "odm:hexBinary"
    type_name = "hexBinary"
    type_model_uri = ODM.HexBinary


class Base64Binary(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.base64Binary
    type_class_curie = "odm:base64Binary"
    type_name = "base64Binary"
    type_model_uri = ODM.Base64Binary


class HexFloat(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.hexFloat
    type_class_curie = "odm:hexFloat"
    type_name = "hexFloat"
    type_model_uri = ODM.HexFloat


class Base64Float(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.base64Float
    type_class_curie = "odm:base64Float"
    type_name = "base64Float"
    type_model_uri = ODM.Base64Float


class EmptyTag(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.emptyTag
    type_class_curie = "odm:emptyTag"
    type_name = "emptyTag"
    type_model_uri = ODM.EmptyTag


class PartialDate(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.partialDate
    type_class_curie = "odm:partialDate"
    type_name = "partialDate"
    type_model_uri = ODM.PartialDate


class THour(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.tHour
    type_class_curie = "odm:tHour"
    type_name = "tHour"
    type_model_uri = ODM.THour


class PartialTime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.partialTime
    type_class_curie = "odm:partialTime"
    type_name = "partialTime"
    type_model_uri = ODM.PartialTime


class TDatetime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.tDatetime
    type_class_curie = "odm:tDatetime"
    type_name = "tDatetime"
    type_model_uri = ODM.TDatetime


class PartialDatetime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.partialDatetime
    type_class_curie = "odm:partialDatetime"
    type_name = "partialDatetime"
    type_model_uri = ODM.PartialDatetime


class TDuration(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.tDuration
    type_class_curie = "odm:tDuration"
    type_name = "tDuration"
    type_model_uri = ODM.TDuration


class DurationDatetime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.durationDatetime
    type_class_curie = "odm:durationDatetime"
    type_name = "durationDatetime"
    type_model_uri = ODM.DurationDatetime


class TInterval(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.tInterval
    type_class_curie = "odm:tInterval"
    type_name = "tInterval"
    type_model_uri = ODM.TInterval


class IntervalDatetime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.intervalDatetime
    type_class_curie = "odm:intervalDatetime"
    type_name = "intervalDatetime"
    type_model_uri = ODM.IntervalDatetime


class TIncomplete(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.tIncomplete
    type_class_curie = "odm:tIncomplete"
    type_name = "tIncomplete"
    type_model_uri = ODM.TIncomplete


class IncompleteDatetime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.incompleteDatetime
    type_class_curie = "odm:incompleteDatetime"
    type_name = "incompleteDatetime"
    type_model_uri = ODM.IncompleteDatetime


class TIncompleteDate(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.tIncompleteDate
    type_class_curie = "odm:tIncompleteDate"
    type_name = "tIncompleteDate"
    type_model_uri = ODM.TIncompleteDate


class TIncompleteTime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.tIncompleteTime
    type_class_curie = "odm:tIncompleteTime"
    type_name = "tIncompleteTime"
    type_model_uri = ODM.TIncompleteTime


class IncompleteTime(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.incompleteTime
    type_class_curie = "odm:incompleteTime"
    type_name = "incompleteTime"
    type_model_uri = ODM.IncompleteTime


class IncompleteDate(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.incompleteDate
    type_class_curie = "odm:incompleteDate"
    type_name = "incompleteDate"
    type_model_uri = ODM.IncompleteDate


class Oid(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.oid
    type_class_curie = "odm:oid"
    type_name = "oid"
    type_model_uri = ODM.Oid


class Oidref(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.oidref
    type_class_curie = "odm:oidref"
    type_name = "oidref"
    type_model_uri = ODM.Oidref


class Value(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.value
    type_class_curie = "odm:value"
    type_name = "value"
    type_model_uri = ODM.Value


class SubjectKey(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.subjectKey
    type_class_curie = "odm:subjectKey"
    type_name = "subjectKey"
    type_model_uri = ODM.SubjectKey


class RepeatKey(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.repeatKey
    type_class_curie = "odm:repeatKey"
    type_name = "repeatKey"
    type_model_uri = ODM.RepeatKey


class Name(str):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
    type_class_uri = ODM.name
    type_class_curie = "odm:name"
    type_name = "name"
    type_model_uri = ODM.Name


class FileName(URIorCURIE):
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
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
    """ https://wiki.cdisc.org/display/ODM2/Data+Formats """
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
    type_name = "_languageType"
    type_model_uri = ODM.LanguageType


class ContentType(str):
    """ multi-line text content from between XML tags """
    type_class_uri = XHTML.div
    type_class_curie = "xhtml:div"
    type_name = "_contentType"
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


class SourceItemLeafID(extended_str):
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

    ContextRef: str = None
    Name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ContextRef):
            self.MissingRequiredField("ContextRef")
        if not isinstance(self.ContextRef, str):
            self.ContextRef = str(self.ContextRef)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

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

    TranslatedTextRef: Optional[Union[Union[dict, "TranslatedText"], List[Union[dict, "TranslatedText"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    Type: str = None
    _language: Optional[str] = None
    _content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, str):
            self.Type = str(self.Type)

        if self._language is not None and not isinstance(self._language, str):
            self._language = str(self._language)

        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

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
    StudyName: str = None
    ProtocolName: str = None
    VersionID: Optional[str] = None
    VersionName: Optional[str] = None
    Status: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    MetaDataVersionRefRef: Optional[Union[Dict[Union[str, MetaDataVersionOID], Union[dict, "MetaDataVersion"]], List[Union[dict, "MetaDataVersion"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyOID):
            self.OID = StudyOID(self.OID)

        if self._is_empty(self.StudyName):
            self.MissingRequiredField("StudyName")
        if not isinstance(self.StudyName, str):
            self.StudyName = str(self.StudyName)

        if self._is_empty(self.ProtocolName):
            self.MissingRequiredField("ProtocolName")
        if not isinstance(self.ProtocolName, str):
            self.ProtocolName = str(self.ProtocolName)

        if self.VersionID is not None and not isinstance(self.VersionID, str):
            self.VersionID = str(self.VersionID)

        if self.VersionName is not None and not isinstance(self.VersionName, str):
            self.VersionName = str(self.VersionName)

        if self.Status is not None and not isinstance(self.Status, str):
            self.Status = str(self.Status)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        self._normalize_inlined_as_list(slot_name="MetaDataVersionRefRef", slot_type=MetaDataVersion, key_name="OID", keyed=True)

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
    Name: str = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    IncludeRef: Optional[Union[dict, "Include"]] = None
    StandardsRef: Optional[Union[dict, "Standards"]] = None
    AnnotatedCRFRef: Optional[Union[dict, "AnnotatedCRF"]] = None
    SupplementalDocRef: Optional[Union[dict, "SupplementalDoc"]] = None
    ValueListDefRef: Optional[Union[Dict[Union[str, ValueListDefOID], Union[dict, "ValueListDef"]], List[Union[dict, "ValueListDef"]]]] = empty_dict()
    WhereClauseDefRef: Optional[Union[Dict[Union[str, WhereClauseDefOID], Union[dict, "WhereClauseDef"]], List[Union[dict, "WhereClauseDef"]]]] = empty_dict()
    ProtocolRef: Optional[Union[dict, "Protocol"]] = None
    WorkflowDefRef: Optional[Union[Dict[Union[str, WorkflowDefOID], Union[dict, "WorkflowDef"]], List[Union[dict, "WorkflowDef"]]]] = empty_dict()
    StudyEventGroupDefRef: Optional[Union[Dict[Union[str, StudyEventGroupDefOID], Union[dict, "StudyEventGroupDef"]], List[Union[dict, "StudyEventGroupDef"]]]] = empty_dict()
    StudyEventDefRef: Optional[Union[Dict[Union[str, StudyEventDefOID], Union[dict, "StudyEventDef"]], List[Union[dict, "StudyEventDef"]]]] = empty_dict()
    ItemGroupDefRef: Optional[Union[Dict[Union[str, ItemGroupDefOID], Union[dict, "ItemGroupDef"]], List[Union[dict, "ItemGroupDef"]]]] = empty_dict()
    ItemDefRef: Optional[Union[Dict[Union[str, ItemDefOID], Union[dict, "ItemDef"]], List[Union[dict, "ItemDef"]]]] = empty_dict()
    CodeListRefRef: Optional[Union[Dict[Union[str, CodeListOID], Union[dict, "CodeList"]], List[Union[dict, "CodeList"]]]] = empty_dict()
    ConditionDefRef: Optional[Union[Dict[Union[str, ConditionDefOID], Union[dict, "ConditionDef"]], List[Union[dict, "ConditionDef"]]]] = empty_dict()
    MethodDefRef: Optional[Union[Dict[Union[str, MethodDefOID], Union[dict, "MethodDef"]], List[Union[dict, "MethodDef"]]]] = empty_dict()
    CommentDefRef: Optional[Union[Dict[Union[str, CommentDefOID], Union[dict, "CommentDef"]], List[Union[dict, "CommentDef"]]]] = empty_dict()
    LeafRef: Optional[Union[Dict[Union[str, LeafID], Union[dict, "Leaf"]], List[Union[dict, "Leaf"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, MetaDataVersionOID):
            self.OID = MetaDataVersionOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.IncludeRef is not None and not isinstance(self.IncludeRef, Include):
            self.IncludeRef = Include(**as_dict(self.IncludeRef))

        if self.StandardsRef is not None and not isinstance(self.StandardsRef, Standards):
            self.StandardsRef = Standards(**as_dict(self.StandardsRef))

        if self.AnnotatedCRFRef is not None and not isinstance(self.AnnotatedCRFRef, AnnotatedCRF):
            self.AnnotatedCRFRef = AnnotatedCRF(**as_dict(self.AnnotatedCRFRef))

        if self.SupplementalDocRef is not None and not isinstance(self.SupplementalDocRef, SupplementalDoc):
            self.SupplementalDocRef = SupplementalDoc(**as_dict(self.SupplementalDocRef))

        self._normalize_inlined_as_list(slot_name="ValueListDefRef", slot_type=ValueListDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="WhereClauseDefRef", slot_type=WhereClauseDef, key_name="OID", keyed=True)

        if self.ProtocolRef is not None and not isinstance(self.ProtocolRef, Protocol):
            self.ProtocolRef = Protocol(**as_dict(self.ProtocolRef))

        self._normalize_inlined_as_list(slot_name="WorkflowDefRef", slot_type=WorkflowDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="StudyEventGroupDefRef", slot_type=StudyEventGroupDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="StudyEventDefRef", slot_type=StudyEventDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="ItemGroupDefRef", slot_type=ItemGroupDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="ItemDefRef", slot_type=ItemDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="CodeListRefRef", slot_type=CodeList, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="ConditionDefRef", slot_type=ConditionDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="MethodDefRef", slot_type=MethodDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="CommentDefRef", slot_type=CommentDef, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="LeafRef", slot_type=Leaf, key_name="ID", keyed=True)

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

    LeafID: str = None
    PDFPageRefRef: Optional[Union[Union[dict, "PDFPageRef"], List[Union[dict, "PDFPageRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.LeafID):
            self.MissingRequiredField("LeafID")
        if not isinstance(self.LeafID, str):
            self.LeafID = str(self.LeafID)

        if not isinstance(self.PDFPageRefRef, list):
            self.PDFPageRefRef = [self.PDFPageRefRef] if self.PDFPageRefRef is not None else []
        self.PDFPageRefRef = [v if isinstance(v, PDFPageRef) else PDFPageRef(**as_dict(v)) for v in self.PDFPageRefRef]

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

    Type: Union[str, "PDFPageType"] = None
    PageRefs: Optional[str] = None
    FirstPage: Optional[int] = None
    LastPage: Optional[int] = None
    TitleRef: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, PDFPageType):
            self.Type = PDFPageType(self.Type)

        if self.PageRefs is not None and not isinstance(self.PageRefs, str):
            self.PageRefs = str(self.PageRefs)

        if self.FirstPage is not None and not isinstance(self.FirstPage, int):
            self.FirstPage = int(self.FirstPage)

        if self.LastPage is not None and not isinstance(self.LastPage, int):
            self.LastPage = int(self.LastPage)

        if self.TitleRef is not None and not isinstance(self.TitleRef, str):
            self.TitleRef = str(self.TitleRef)

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
    TitleRef: Optional[Union[dict, "Title"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, LeafID):
            self.ID = LeafID(self.ID)

        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, URIorCURIE):
            self.href = URIorCURIE(self.href)

        if self.TitleRef is not None and not isinstance(self.TitleRef, Title):
            self.TitleRef = Title(**as_dict(self.TitleRef))

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    StudyOID: str = None
    MetaDataVersionOID: str = None
    href: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyOID):
            self.MissingRequiredField("StudyOID")
        if not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        if self._is_empty(self.MetaDataVersionOID):
            self.MissingRequiredField("MetaDataVersionOID")
        if not isinstance(self.MetaDataVersionOID, str):
            self.MetaDataVersionOID = str(self.MetaDataVersionOID)

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

    StandardRef: Optional[Union[Dict[Union[str, StandardOID], Union[dict, "Standard"]], List[Union[dict, "Standard"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StandardRef", slot_type=Standard, key_name="OID", keyed=True)

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
    Name: Union[str, "StandardName"] = None
    Type: Union[str, "StandardType"] = None
    Version: str = None
    Status: str = None
    PublishingSet: Optional[Union[str, "StandardPublishingSet"]] = None
    CommentOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StandardOID):
            self.OID = StandardOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, StandardName):
            self.Name = StandardName(self.Name)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, StandardType):
            self.Type = StandardType(self.Type)

        if self._is_empty(self.Version):
            self.MissingRequiredField("Version")
        if not isinstance(self.Version, str):
            self.Version = str(self.Version)

        if self._is_empty(self.Status):
            self.MissingRequiredField("Status")
        if not isinstance(self.Status, str):
            self.Status = str(self.Status)

        if self.PublishingSet is not None and not isinstance(self.PublishingSet, StandardPublishingSet):
            self.PublishingSet = StandardPublishingSet(self.PublishingSet)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

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

    DocumentRefRef: Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.DocumentRefRef, list):
            self.DocumentRefRef = [self.DocumentRefRef] if self.DocumentRefRef is not None else []
        self.DocumentRefRef = [v if isinstance(v, DocumentRef) else DocumentRef(**as_dict(v)) for v in self.DocumentRefRef]

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

    DocumentRefRef: Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.DocumentRefRef, list):
            self.DocumentRefRef = [self.DocumentRefRef] if self.DocumentRefRef is not None else []
        self.DocumentRefRef = [v if isinstance(v, DocumentRef) else DocumentRef(**as_dict(v)) for v in self.DocumentRefRef]

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
    DescriptionRef: Optional[Union[dict, Description]] = None
    ItemRefRef: Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ValueListDefOID):
            self.OID = ValueListDefOID(self.OID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.ItemRefRef, list):
            self.ItemRefRef = [self.ItemRefRef] if self.ItemRefRef is not None else []
        self.ItemRefRef = [v if isinstance(v, ItemRef) else ItemRef(**as_dict(v)) for v in self.ItemRefRef]

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

    WhereClauseOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.WhereClauseOID):
            self.MissingRequiredField("WhereClauseOID")
        if not isinstance(self.WhereClauseOID, str):
            self.WhereClauseOID = str(self.WhereClauseOID)

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
    CommentOID: Optional[str] = None
    RangeCheckRef: Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, WhereClauseDefOID):
            self.OID = WhereClauseDefOID(self.OID)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if not isinstance(self.RangeCheckRef, list):
            self.RangeCheckRef = [self.RangeCheckRef] if self.RangeCheckRef is not None else []
        self.RangeCheckRef = [v if isinstance(v, RangeCheck) else RangeCheck(**as_dict(v)) for v in self.RangeCheckRef]

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

    StudyEventGroupOID: str = None
    Mandatory: Union[str, "YesOrNo"] = None
    OrderNumber: Optional[int] = None
    CollectionExceptionConditionOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyEventGroupOID):
            self.MissingRequiredField("StudyEventGroupOID")
        if not isinstance(self.StudyEventGroupOID, str):
            self.StudyEventGroupOID = str(self.StudyEventGroupOID)

        if self._is_empty(self.Mandatory):
            self.MissingRequiredField("Mandatory")
        if not isinstance(self.Mandatory, YesOrNo):
            self.Mandatory = YesOrNo(self.Mandatory)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

        if self.CollectionExceptionConditionOID is not None and not isinstance(self.CollectionExceptionConditionOID, str):
            self.CollectionExceptionConditionOID = str(self.CollectionExceptionConditionOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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
    Name: str = None
    ArmOID: Optional[str] = None
    EpochOID: Optional[str] = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    WorkflowRefRef: Optional[Union[dict, "WorkflowRef"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    StudyEventGroupRefRef: Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]] = empty_list()
    StudyEventRefRef: Optional[Union[Union[dict, "StudyEventRef"], List[Union[dict, "StudyEventRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEventGroupDefOID):
            self.OID = StudyEventGroupDefOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.ArmOID is not None and not isinstance(self.ArmOID, str):
            self.ArmOID = str(self.ArmOID)

        if self.EpochOID is not None and not isinstance(self.EpochOID, str):
            self.EpochOID = str(self.EpochOID)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.WorkflowRefRef is not None and not isinstance(self.WorkflowRefRef, WorkflowRef):
            self.WorkflowRefRef = WorkflowRef(**as_dict(self.WorkflowRefRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.StudyEventGroupRefRef, list):
            self.StudyEventGroupRefRef = [self.StudyEventGroupRefRef] if self.StudyEventGroupRefRef is not None else []
        self.StudyEventGroupRefRef = [v if isinstance(v, StudyEventGroupRef) else StudyEventGroupRef(**as_dict(v)) for v in self.StudyEventGroupRefRef]

        if not isinstance(self.StudyEventRefRef, list):
            self.StudyEventRefRef = [self.StudyEventRefRef] if self.StudyEventRefRef is not None else []
        self.StudyEventRefRef = [v if isinstance(v, StudyEventRef) else StudyEventRef(**as_dict(v)) for v in self.StudyEventRefRef]

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

    StudyEventOID: str = None
    Mandatory: Union[str, "YesOrNo"] = None
    OrderNumber: Optional[int] = None
    CollectionExceptionConditionOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyEventOID):
            self.MissingRequiredField("StudyEventOID")
        if not isinstance(self.StudyEventOID, str):
            self.StudyEventOID = str(self.StudyEventOID)

        if self._is_empty(self.Mandatory):
            self.MissingRequiredField("Mandatory")
        if not isinstance(self.Mandatory, YesOrNo):
            self.Mandatory = YesOrNo(self.Mandatory)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

        if self.CollectionExceptionConditionOID is not None and not isinstance(self.CollectionExceptionConditionOID, str):
            self.CollectionExceptionConditionOID = str(self.CollectionExceptionConditionOID)

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
    Name: str = None
    Repeating: Union[str, "YesOrNo"] = None
    Type: Union[str, "EventType"] = None
    Category: Optional[str] = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    ItemGroupRefRef: Optional[Union[Union[dict, "ItemGroupRef"], List[Union[dict, "ItemGroupRef"]]]] = empty_list()
    WorkflowRefRef: Optional[Union[dict, "WorkflowRef"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEventDefOID):
            self.OID = StudyEventDefOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Repeating):
            self.MissingRequiredField("Repeating")
        if not isinstance(self.Repeating, YesOrNo):
            self.Repeating = YesOrNo(self.Repeating)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, EventType):
            self.Type = EventType(self.Type)

        if self.Category is not None and not isinstance(self.Category, str):
            self.Category = str(self.Category)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.ItemGroupRefRef, list):
            self.ItemGroupRefRef = [self.ItemGroupRefRef] if self.ItemGroupRefRef is not None else []
        self.ItemGroupRefRef = [v if isinstance(v, ItemGroupRef) else ItemGroupRef(**as_dict(v)) for v in self.ItemGroupRefRef]

        if self.WorkflowRefRef is not None and not isinstance(self.WorkflowRefRef, WorkflowRef):
            self.WorkflowRefRef = WorkflowRef(**as_dict(self.WorkflowRefRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

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

    ItemGroupOID: str = None
    Mandatory: Union[str, "YesOrNo"] = None
    MethodOID: Optional[str] = None
    OrderNumber: Optional[int] = None
    CollectionExceptionConditionOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ItemGroupOID):
            self.MissingRequiredField("ItemGroupOID")
        if not isinstance(self.ItemGroupOID, str):
            self.ItemGroupOID = str(self.ItemGroupOID)

        if self._is_empty(self.Mandatory):
            self.MissingRequiredField("Mandatory")
        if not isinstance(self.Mandatory, YesOrNo):
            self.Mandatory = YesOrNo(self.Mandatory)

        if self.MethodOID is not None and not isinstance(self.MethodOID, str):
            self.MethodOID = str(self.MethodOID)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

        if self.CollectionExceptionConditionOID is not None and not isinstance(self.CollectionExceptionConditionOID, str):
            self.CollectionExceptionConditionOID = str(self.CollectionExceptionConditionOID)

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
    Name: str = None
    Repeating: Union[str, "ItemGroupRepeatingType"] = None
    Type: str = None
    RepeatingLimit: Optional[int] = None
    IsReferenceData: Optional[Union[str, "YesOrNo"]] = None
    Structure: Optional[str] = None
    ArchiveLocationID: Optional[str] = None
    DatasetName: Optional[str] = None
    Domain: Optional[str] = None
    Purpose: Optional[str] = None
    StandardOID: Optional[str] = None
    IsNonStandard: Optional[Union[str, "YesOnly"]] = None
    HasNoData: Optional[Union[str, "YesOnly"]] = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    ClassRef: Optional[Union[dict, "Class"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    WorkflowRefRef: Optional[Union[dict, "WorkflowRef"]] = None
    OriginRef: Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]] = empty_list()
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()
    LeafRef: Optional[Union[str, LeafID]] = None
    ItemGroupRefRef: Optional[Union[Union[dict, ItemGroupRef], List[Union[dict, ItemGroupRef]]]] = empty_list()
    ItemRefRef: Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ItemGroupDefOID):
            self.OID = ItemGroupDefOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Repeating):
            self.MissingRequiredField("Repeating")
        if not isinstance(self.Repeating, ItemGroupRepeatingType):
            self.Repeating = ItemGroupRepeatingType(self.Repeating)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, str):
            self.Type = str(self.Type)

        if self.RepeatingLimit is not None and not isinstance(self.RepeatingLimit, int):
            self.RepeatingLimit = int(self.RepeatingLimit)

        if self.IsReferenceData is not None and not isinstance(self.IsReferenceData, YesOrNo):
            self.IsReferenceData = YesOrNo(self.IsReferenceData)

        if self.Structure is not None and not isinstance(self.Structure, str):
            self.Structure = str(self.Structure)

        if self.ArchiveLocationID is not None and not isinstance(self.ArchiveLocationID, str):
            self.ArchiveLocationID = str(self.ArchiveLocationID)

        if self.DatasetName is not None and not isinstance(self.DatasetName, str):
            self.DatasetName = str(self.DatasetName)

        if self.Domain is not None and not isinstance(self.Domain, str):
            self.Domain = str(self.Domain)

        if self.Purpose is not None and not isinstance(self.Purpose, str):
            self.Purpose = str(self.Purpose)

        if self.StandardOID is not None and not isinstance(self.StandardOID, str):
            self.StandardOID = str(self.StandardOID)

        if self.IsNonStandard is not None and not isinstance(self.IsNonStandard, YesOnly):
            self.IsNonStandard = YesOnly(self.IsNonStandard)

        if self.HasNoData is not None and not isinstance(self.HasNoData, YesOnly):
            self.HasNoData = YesOnly(self.HasNoData)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.ClassRef is not None and not isinstance(self.ClassRef, Class):
            self.ClassRef = Class(**as_dict(self.ClassRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if self.WorkflowRefRef is not None and not isinstance(self.WorkflowRefRef, WorkflowRef):
            self.WorkflowRefRef = WorkflowRef(**as_dict(self.WorkflowRefRef))

        if not isinstance(self.OriginRef, list):
            self.OriginRef = [self.OriginRef] if self.OriginRef is not None else []
        self.OriginRef = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.OriginRef]

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

        if self.LeafRef is not None and not isinstance(self.LeafRef, LeafID):
            self.LeafRef = LeafID(self.LeafRef)

        if not isinstance(self.ItemGroupRefRef, list):
            self.ItemGroupRefRef = [self.ItemGroupRefRef] if self.ItemGroupRefRef is not None else []
        self.ItemGroupRefRef = [v if isinstance(v, ItemGroupRef) else ItemGroupRef(**as_dict(v)) for v in self.ItemGroupRefRef]

        if not isinstance(self.ItemRefRef, list):
            self.ItemRefRef = [self.ItemRefRef] if self.ItemRefRef is not None else []
        self.ItemRefRef = [v if isinstance(v, ItemRef) else ItemRef(**as_dict(v)) for v in self.ItemRefRef]

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

    Name: Union[str, "ItemGroupClass"] = None
    SubClassRef: Optional[Union[Union[dict, "SubClass"], List[Union[dict, "SubClass"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, ItemGroupClass):
            self.Name = ItemGroupClass(self.Name)

        if not isinstance(self.SubClassRef, list):
            self.SubClassRef = [self.SubClassRef] if self.SubClassRef is not None else []
        self.SubClassRef = [v if isinstance(v, SubClass) else SubClass(**as_dict(v)) for v in self.SubClassRef]

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

    Name: Union[str, "ItemGroupSubClass"] = None
    ParentClass: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, ItemGroupSubClass):
            self.Name = ItemGroupSubClass(self.Name)

        if self.ParentClass is not None and not isinstance(self.ParentClass, str):
            self.ParentClass = str(self.ParentClass)

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

    ItemOID: str = None
    Mandatory: Union[str, "YesOrNo"] = None
    KeySequence: Optional[int] = None
    IsNonStandard: Optional[Union[str, "YesOnly"]] = None
    HasNoData: Optional[Union[str, "YesOnly"]] = None
    MethodOID: Optional[str] = None
    UnitsItemOID: Optional[str] = None
    Repeat: Optional[Union[str, "YesOnly"]] = None
    Other: Optional[Union[str, "YesOnly"]] = None
    Role: Optional[str] = None
    RoleCodeListOID: Optional[str] = None
    Core: Optional[str] = None
    PreSpecifiedValue: Optional[str] = None
    OrderNumber: Optional[int] = None
    CollectionExceptionConditionOID: Optional[str] = None
    OriginRef: Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]] = empty_list()
    WhereClauseRefRef: Optional[Union[Union[dict, WhereClauseRef], List[Union[dict, WhereClauseRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ItemOID):
            self.MissingRequiredField("ItemOID")
        if not isinstance(self.ItemOID, str):
            self.ItemOID = str(self.ItemOID)

        if self._is_empty(self.Mandatory):
            self.MissingRequiredField("Mandatory")
        if not isinstance(self.Mandatory, YesOrNo):
            self.Mandatory = YesOrNo(self.Mandatory)

        if self.KeySequence is not None and not isinstance(self.KeySequence, int):
            self.KeySequence = int(self.KeySequence)

        if self.IsNonStandard is not None and not isinstance(self.IsNonStandard, YesOnly):
            self.IsNonStandard = YesOnly(self.IsNonStandard)

        if self.HasNoData is not None and not isinstance(self.HasNoData, YesOnly):
            self.HasNoData = YesOnly(self.HasNoData)

        if self.MethodOID is not None and not isinstance(self.MethodOID, str):
            self.MethodOID = str(self.MethodOID)

        if self.UnitsItemOID is not None and not isinstance(self.UnitsItemOID, str):
            self.UnitsItemOID = str(self.UnitsItemOID)

        if self.Repeat is not None and not isinstance(self.Repeat, YesOnly):
            self.Repeat = YesOnly(self.Repeat)

        if self.Other is not None and not isinstance(self.Other, YesOnly):
            self.Other = YesOnly(self.Other)

        if self.Role is not None and not isinstance(self.Role, str):
            self.Role = str(self.Role)

        if self.RoleCodeListOID is not None and not isinstance(self.RoleCodeListOID, str):
            self.RoleCodeListOID = str(self.RoleCodeListOID)

        if self.Core is not None and not isinstance(self.Core, str):
            self.Core = str(self.Core)

        if self.PreSpecifiedValue is not None and not isinstance(self.PreSpecifiedValue, str):
            self.PreSpecifiedValue = str(self.PreSpecifiedValue)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

        if self.CollectionExceptionConditionOID is not None and not isinstance(self.CollectionExceptionConditionOID, str):
            self.CollectionExceptionConditionOID = str(self.CollectionExceptionConditionOID)

        if not isinstance(self.OriginRef, list):
            self.OriginRef = [self.OriginRef] if self.OriginRef is not None else []
        self.OriginRef = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.OriginRef]

        if not isinstance(self.WhereClauseRefRef, list):
            self.WhereClauseRefRef = [self.WhereClauseRefRef] if self.WhereClauseRefRef is not None else []
        self.WhereClauseRefRef = [v if isinstance(v, WhereClauseRef) else WhereClauseRef(**as_dict(v)) for v in self.WhereClauseRefRef]

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

    Type: Union[str, "OriginType"] = None
    Source: Optional[Union[str, "OriginSource"]] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    SourceItemsRef: Optional[Union[dict, "SourceItems"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    DocumentRefRef: Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, OriginType):
            self.Type = OriginType(self.Type)

        if self.Source is not None and not isinstance(self.Source, OriginSource):
            self.Source = OriginSource(self.Source)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.SourceItemsRef is not None and not isinstance(self.SourceItemsRef, SourceItems):
            self.SourceItemsRef = SourceItems(**as_dict(self.SourceItemsRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.DocumentRefRef, list):
            self.DocumentRefRef = [self.DocumentRefRef] if self.DocumentRefRef is not None else []
        self.DocumentRefRef = [v if isinstance(v, DocumentRef) else DocumentRef(**as_dict(v)) for v in self.DocumentRefRef]

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

    SourceItemRef: Optional[Union[Dict[Union[str, SourceItemLeafID], Union[dict, "SourceItem"]], List[Union[dict, "SourceItem"]]]] = empty_dict()
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="SourceItemRef", slot_type=SourceItem, key_name="leafID", keyed=True)

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

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

    leafID: Union[str, SourceItemLeafID] = None
    ItemOID: Optional[str] = None
    ItemGroupOID: Optional[str] = None
    MetaDataVersionOID: Optional[str] = None
    StudyOID: Optional[str] = None
    Name: Optional[str] = None
    ResourceRef: Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]] = empty_list()
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.leafID):
            self.MissingRequiredField("leafID")
        if not isinstance(self.leafID, SourceItemLeafID):
            self.leafID = SourceItemLeafID(self.leafID)

        if self.ItemOID is not None and not isinstance(self.ItemOID, str):
            self.ItemOID = str(self.ItemOID)

        if self.ItemGroupOID is not None and not isinstance(self.ItemGroupOID, str):
            self.ItemGroupOID = str(self.ItemGroupOID)

        if self.MetaDataVersionOID is not None and not isinstance(self.MetaDataVersionOID, str):
            self.MetaDataVersionOID = str(self.MetaDataVersionOID)

        if self.StudyOID is not None and not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        if self.Name is not None and not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if not isinstance(self.ResourceRef, list):
            self.ResourceRef = [self.ResourceRef] if self.ResourceRef is not None else []
        self.ResourceRef = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.ResourceRef]

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

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

    Type: str = None
    Name: str = None
    Attribute: Optional[str] = None
    Label: Optional[str] = None
    SelectionRef: Optional[Union[Union[dict, "Selection"], List[Union[dict, "Selection"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, str):
            self.Type = str(self.Type)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Attribute is not None and not isinstance(self.Attribute, str):
            self.Attribute = str(self.Attribute)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if not isinstance(self.SelectionRef, list):
            self.SelectionRef = [self.SelectionRef] if self.SelectionRef is not None else []
        self.SelectionRef = [v if isinstance(v, Selection) else Selection(**as_dict(v)) for v in self.SelectionRef]

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

    Path: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Path):
            self.MissingRequiredField("Path")
        if not isinstance(self.Path, str):
            self.Path = str(self.Path)

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
    Name: str = None
    DataTypeRef: Union[str, "DataType"] = None
    Length: Optional[int] = None
    DisplayFormat: Optional[str] = None
    VariableSet: Optional[str] = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    DefinitionRef: Optional[Union[dict, "Definition"]] = None
    QuestionRef: Optional[Union[dict, "Question"]] = None
    PromptRef: Optional[Union[dict, "Prompt"]] = None
    CRFCompletionInstructionsRef: Optional[Union[dict, "CRFCompletionInstructions"]] = None
    ImplementationNotesRef: Optional[Union[dict, "ImplementationNotes"]] = None
    CDISCNotesRef: Optional[Union[dict, "CDISCNotes"]] = None
    RangeCheckRef: Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]] = empty_list()
    CodeListRefRef: Optional[Union[dict, "CodeListRef"]] = None
    ValueListRefRef: Optional[Union[dict, "ValueListRef"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ItemDefOID):
            self.OID = ItemDefOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.DataTypeRef):
            self.MissingRequiredField("DataTypeRef")
        if not isinstance(self.DataTypeRef, DataType):
            self.DataTypeRef = DataType(self.DataTypeRef)

        if self.Length is not None and not isinstance(self.Length, int):
            self.Length = int(self.Length)

        if self.DisplayFormat is not None and not isinstance(self.DisplayFormat, str):
            self.DisplayFormat = str(self.DisplayFormat)

        if self.VariableSet is not None and not isinstance(self.VariableSet, str):
            self.VariableSet = str(self.VariableSet)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.DefinitionRef is not None and not isinstance(self.DefinitionRef, Definition):
            self.DefinitionRef = Definition(**as_dict(self.DefinitionRef))

        if self.QuestionRef is not None and not isinstance(self.QuestionRef, Question):
            self.QuestionRef = Question(**as_dict(self.QuestionRef))

        if self.PromptRef is not None and not isinstance(self.PromptRef, Prompt):
            self.PromptRef = Prompt(**as_dict(self.PromptRef))

        if self.CRFCompletionInstructionsRef is not None and not isinstance(self.CRFCompletionInstructionsRef, CRFCompletionInstructions):
            self.CRFCompletionInstructionsRef = CRFCompletionInstructions(**as_dict(self.CRFCompletionInstructionsRef))

        if self.ImplementationNotesRef is not None and not isinstance(self.ImplementationNotesRef, ImplementationNotes):
            self.ImplementationNotesRef = ImplementationNotes(**as_dict(self.ImplementationNotesRef))

        if self.CDISCNotesRef is not None and not isinstance(self.CDISCNotesRef, CDISCNotes):
            self.CDISCNotesRef = CDISCNotes(**as_dict(self.CDISCNotesRef))

        if not isinstance(self.RangeCheckRef, list):
            self.RangeCheckRef = [self.RangeCheckRef] if self.RangeCheckRef is not None else []
        self.RangeCheckRef = [v if isinstance(v, RangeCheck) else RangeCheck(**as_dict(v)) for v in self.RangeCheckRef]

        if self.CodeListRefRef is not None and not isinstance(self.CodeListRefRef, CodeListRef):
            self.CodeListRefRef = CodeListRef(**as_dict(self.CodeListRefRef))

        if self.ValueListRefRef is not None and not isinstance(self.ValueListRefRef, ValueListRef):
            self.ValueListRefRef = ValueListRef(**as_dict(self.ValueListRefRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    ComparatorRef: Optional[Union[str, "Comparator"]] = None
    SoftHard: Optional[Union[str, "SoftOrHard"]] = None
    ItemOID: Optional[str] = None
    ErrorMessageRef: Optional[Union[dict, "ErrorMessage"]] = None
    MethodSignatureRef: Optional[Union[dict, "MethodSignature"]] = None
    FormalExpressionRef: Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]] = empty_list()
    CheckValueRef: Optional[Union[Union[dict, "CheckValue"], List[Union[dict, "CheckValue"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ComparatorRef is not None and not isinstance(self.ComparatorRef, Comparator):
            self.ComparatorRef = Comparator(self.ComparatorRef)

        if self.SoftHard is not None and not isinstance(self.SoftHard, SoftOrHard):
            self.SoftHard = SoftOrHard(self.SoftHard)

        if self.ItemOID is not None and not isinstance(self.ItemOID, str):
            self.ItemOID = str(self.ItemOID)

        if self.ErrorMessageRef is not None and not isinstance(self.ErrorMessageRef, ErrorMessage):
            self.ErrorMessageRef = ErrorMessage(**as_dict(self.ErrorMessageRef))

        if self.MethodSignatureRef is not None and not isinstance(self.MethodSignatureRef, MethodSignature):
            self.MethodSignatureRef = MethodSignature(**as_dict(self.MethodSignatureRef))

        if not isinstance(self.FormalExpressionRef, list):
            self.FormalExpressionRef = [self.FormalExpressionRef] if self.FormalExpressionRef is not None else []
        self.FormalExpressionRef = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.FormalExpressionRef]

        if not isinstance(self.CheckValueRef, list):
            self.CheckValueRef = [self.CheckValueRef] if self.CheckValueRef is not None else []
        self.CheckValueRef = [v if isinstance(v, CheckValue) else CheckValue(**as_dict(v)) for v in self.CheckValueRef]

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    CodeListOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.CodeListOID):
            self.MissingRequiredField("CodeListOID")
        if not isinstance(self.CodeListOID, str):
            self.CodeListOID = str(self.CodeListOID)

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

    ValueListOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ValueListOID):
            self.MissingRequiredField("ValueListOID")
        if not isinstance(self.ValueListOID, str):
            self.ValueListOID = str(self.ValueListOID)

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
    Name: str = None
    DataTypeRef: Union[str, "CLDataType"] = None
    CommentOID: Optional[str] = None
    StandardOID: Optional[str] = None
    IsNonStandard: Optional[Union[str, "YesOnly"]] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    CodeListItemRef: Optional[Union[Union[dict, "CodeListItem"], List[Union[dict, "CodeListItem"]]]] = empty_list()
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, CodeListOID):
            self.OID = CodeListOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.DataTypeRef):
            self.MissingRequiredField("DataTypeRef")
        if not isinstance(self.DataTypeRef, CLDataType):
            self.DataTypeRef = CLDataType(self.DataTypeRef)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.StandardOID is not None and not isinstance(self.StandardOID, str):
            self.StandardOID = str(self.StandardOID)

        if self.IsNonStandard is not None and not isinstance(self.IsNonStandard, YesOnly):
            self.IsNonStandard = YesOnly(self.IsNonStandard)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.CodeListItemRef, list):
            self.CodeListItemRef = [self.CodeListItemRef] if self.CodeListItemRef is not None else []
        self.CodeListItemRef = [v if isinstance(v, CodeListItem) else CodeListItem(**as_dict(v)) for v in self.CodeListItemRef]

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

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

    CodedValue: str = None
    Rank: Optional[Decimal] = None
    Other: Optional[Union[str, "YesOnly"]] = None
    OrderNumber: Optional[int] = None
    ExtendedValue: Optional[Union[str, "YesOnly"]] = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    DecodeRef: Optional[Union[dict, "Decode"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.CodedValue):
            self.MissingRequiredField("CodedValue")
        if not isinstance(self.CodedValue, str):
            self.CodedValue = str(self.CodedValue)

        if self.Rank is not None and not isinstance(self.Rank, Decimal):
            self.Rank = Decimal(self.Rank)

        if self.Other is not None and not isinstance(self.Other, YesOnly):
            self.Other = YesOnly(self.Other)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

        if self.ExtendedValue is not None and not isinstance(self.ExtendedValue, YesOnly):
            self.ExtendedValue = YesOnly(self.ExtendedValue)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.DecodeRef is not None and not isinstance(self.DecodeRef, Decode):
            self.DecodeRef = Decode(**as_dict(self.DecodeRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

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

    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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
    Name: str = None
    Type: Optional[Union[str, "MethodType"]] = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    MethodSignatureRef: Optional[Union[dict, "MethodSignature"]] = None
    FormalExpressionRef: Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]] = empty_list()
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()
    DocumentRefRef: Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, MethodDefOID):
            self.OID = MethodDefOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Type is not None and not isinstance(self.Type, MethodType):
            self.Type = MethodType(self.Type)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.MethodSignatureRef is not None and not isinstance(self.MethodSignatureRef, MethodSignature):
            self.MethodSignatureRef = MethodSignature(**as_dict(self.MethodSignatureRef))

        if not isinstance(self.FormalExpressionRef, list):
            self.FormalExpressionRef = [self.FormalExpressionRef] if self.FormalExpressionRef is not None else []
        self.FormalExpressionRef = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.FormalExpressionRef]

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

        if not isinstance(self.DocumentRefRef, list):
            self.DocumentRefRef = [self.DocumentRefRef] if self.DocumentRefRef is not None else []
        self.DocumentRefRef = [v if isinstance(v, DocumentRef) else DocumentRef(**as_dict(v)) for v in self.DocumentRefRef]

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

    ParameterRef: Optional[Union[Union[dict, "Parameter"], List[Union[dict, "Parameter"]]]] = empty_list()
    ReturnValueRef: Optional[Union[Union[dict, "ReturnValue"], List[Union[dict, "ReturnValue"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.ParameterRef, list):
            self.ParameterRef = [self.ParameterRef] if self.ParameterRef is not None else []
        self.ParameterRef = [v if isinstance(v, Parameter) else Parameter(**as_dict(v)) for v in self.ParameterRef]

        if not isinstance(self.ReturnValueRef, list):
            self.ReturnValueRef = [self.ReturnValueRef] if self.ReturnValueRef is not None else []
        self.ReturnValueRef = [v if isinstance(v, ReturnValue) else ReturnValue(**as_dict(v)) for v in self.ReturnValueRef]

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

    Name: str = None
    DataTypeRef: Union[str, "DataType"] = None
    DefinitionRef: Optional[str] = None
    OrderNumber: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.DataTypeRef):
            self.MissingRequiredField("DataTypeRef")
        if not isinstance(self.DataTypeRef, DataType):
            self.DataTypeRef = DataType(self.DataTypeRef)

        if self.DefinitionRef is not None and not isinstance(self.DefinitionRef, str):
            self.DefinitionRef = str(self.DefinitionRef)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

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

    Name: str = None
    DataTypeRef: Union[str, "DataType"] = None
    DefinitionRef: Optional[str] = None
    OrderNumber: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.DataTypeRef):
            self.MissingRequiredField("DataTypeRef")
        if not isinstance(self.DataTypeRef, DataType):
            self.DataTypeRef = DataType(self.DataTypeRef)

        if self.DefinitionRef is not None and not isinstance(self.DefinitionRef, str):
            self.DefinitionRef = str(self.DefinitionRef)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

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
    Name: str = None
    CommentOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    MethodSignatureRef: Optional[Union[dict, MethodSignature]] = None
    FormalExpressionRef: Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]] = empty_list()
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ConditionDefOID):
            self.OID = ConditionDefOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.MethodSignatureRef is not None and not isinstance(self.MethodSignatureRef, MethodSignature):
            self.MethodSignatureRef = MethodSignature(**as_dict(self.MethodSignatureRef))

        if not isinstance(self.FormalExpressionRef, list):
            self.FormalExpressionRef = [self.FormalExpressionRef] if self.FormalExpressionRef is not None else []
        self.FormalExpressionRef = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.FormalExpressionRef]

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

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

    ContextRef: Optional[str] = None
    CodeRef: Optional[Union[dict, "Code"]] = None
    ExternalCodeLibRef: Optional[Union[dict, "ExternalCodeLib"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ContextRef is not None and not isinstance(self.ContextRef, str):
            self.ContextRef = str(self.ContextRef)

        if self.CodeRef is not None and not isinstance(self.CodeRef, Code):
            self.CodeRef = Code(**as_dict(self.CodeRef))

        if self.ExternalCodeLibRef is not None and not isinstance(self.ExternalCodeLibRef, ExternalCodeLib):
            self.ExternalCodeLibRef = ExternalCodeLib(**as_dict(self.ExternalCodeLibRef))

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    Library: str = None
    Method: Optional[str] = None
    Version: Optional[str] = None
    ref: Optional[str] = None
    href: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Library):
            self.MissingRequiredField("Library")
        if not isinstance(self.Library, str):
            self.Library = str(self.Library)

        if self.Method is not None and not isinstance(self.Method, str):
            self.Method = str(self.Method)

        if self.Version is not None and not isinstance(self.Version, str):
            self.Version = str(self.Version)

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
    DescriptionRef: Optional[Union[dict, Description]] = None
    DocumentRefRef: Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, CommentDefOID):
            self.OID = CommentDefOID(self.OID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.DocumentRefRef, list):
            self.DocumentRefRef = [self.DocumentRefRef] if self.DocumentRefRef is not None else []
        self.DocumentRefRef = [v if isinstance(v, DocumentRef) else DocumentRef(**as_dict(v)) for v in self.DocumentRefRef]

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

    DescriptionRef: Optional[Union[dict, Description]] = None
    StudySummaryRef: Optional[Union[dict, "StudySummary"]] = None
    StudyStructureRef: Optional[Union[dict, "StudyStructure"]] = None
    TrialPhaseRef: Optional[Union[dict, "TrialPhase"]] = None
    StudyTimingsRef: Optional[Union[dict, "StudyTimings"]] = None
    StudyIndicationsRef: Optional[Union[dict, "StudyIndications"]] = None
    StudyInterventionsRef: Optional[Union[dict, "StudyInterventions"]] = None
    StudyObjectivesRef: Optional[Union[dict, "StudyObjectives"]] = None
    StudyEndPointsRef: Optional[Union[dict, "StudyEndPoints"]] = None
    StudyTargetPopulationRefRef: Optional[Union[str, StudyTargetPopulationOID]] = None
    StudyEstimandsRef: Optional[Union[dict, "StudyEstimands"]] = None
    InclusionExclusionCriteriaRef: Optional[Union[dict, "InclusionExclusionCriteria"]] = None
    StudyEventGroupRefRef: Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]] = empty_list()
    WorkflowRefRef: Optional[Union[dict, "WorkflowRef"]] = None
    AliasRef: Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.StudySummaryRef is not None and not isinstance(self.StudySummaryRef, StudySummary):
            self.StudySummaryRef = StudySummary(**as_dict(self.StudySummaryRef))

        if self.StudyStructureRef is not None and not isinstance(self.StudyStructureRef, StudyStructure):
            self.StudyStructureRef = StudyStructure(**as_dict(self.StudyStructureRef))

        if self.TrialPhaseRef is not None and not isinstance(self.TrialPhaseRef, TrialPhase):
            self.TrialPhaseRef = TrialPhase(**as_dict(self.TrialPhaseRef))

        if self.StudyTimingsRef is not None and not isinstance(self.StudyTimingsRef, StudyTimings):
            self.StudyTimingsRef = StudyTimings(**as_dict(self.StudyTimingsRef))

        if self.StudyIndicationsRef is not None and not isinstance(self.StudyIndicationsRef, StudyIndications):
            self.StudyIndicationsRef = StudyIndications(**as_dict(self.StudyIndicationsRef))

        if self.StudyInterventionsRef is not None and not isinstance(self.StudyInterventionsRef, StudyInterventions):
            self.StudyInterventionsRef = StudyInterventions(**as_dict(self.StudyInterventionsRef))

        if self.StudyObjectivesRef is not None and not isinstance(self.StudyObjectivesRef, StudyObjectives):
            self.StudyObjectivesRef = StudyObjectives(**as_dict(self.StudyObjectivesRef))

        if self.StudyEndPointsRef is not None and not isinstance(self.StudyEndPointsRef, StudyEndPoints):
            self.StudyEndPointsRef = StudyEndPoints(**as_dict(self.StudyEndPointsRef))

        if self.StudyTargetPopulationRefRef is not None and not isinstance(self.StudyTargetPopulationRefRef, StudyTargetPopulationOID):
            self.StudyTargetPopulationRefRef = StudyTargetPopulationOID(self.StudyTargetPopulationRefRef)

        if self.StudyEstimandsRef is not None and not isinstance(self.StudyEstimandsRef, StudyEstimands):
            self.StudyEstimandsRef = StudyEstimands(**as_dict(self.StudyEstimandsRef))

        if self.InclusionExclusionCriteriaRef is not None and not isinstance(self.InclusionExclusionCriteriaRef, InclusionExclusionCriteria):
            self.InclusionExclusionCriteriaRef = InclusionExclusionCriteria(**as_dict(self.InclusionExclusionCriteriaRef))

        if not isinstance(self.StudyEventGroupRefRef, list):
            self.StudyEventGroupRefRef = [self.StudyEventGroupRefRef] if self.StudyEventGroupRefRef is not None else []
        self.StudyEventGroupRefRef = [v if isinstance(v, StudyEventGroupRef) else StudyEventGroupRef(**as_dict(v)) for v in self.StudyEventGroupRefRef]

        if self.WorkflowRefRef is not None and not isinstance(self.WorkflowRefRef, WorkflowRef):
            self.WorkflowRefRef = WorkflowRef(**as_dict(self.WorkflowRefRef))

        if not isinstance(self.AliasRef, list):
            self.AliasRef = [self.AliasRef] if self.AliasRef is not None else []
        self.AliasRef = [v if isinstance(v, Alias) else Alias(**as_dict(v)) for v in self.AliasRef]

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

    DescriptionRef: Optional[Union[dict, Description]] = None
    ArmRef: Optional[Union[Dict[Union[str, ArmOID], Union[dict, "Arm"]], List[Union[dict, "Arm"]]]] = empty_dict()
    EpochRef: Optional[Union[Dict[Union[str, EpochOID], Union[dict, "Epoch"]], List[Union[dict, "Epoch"]]]] = empty_dict()
    WorkflowRefRef: Optional[Union[dict, "WorkflowRef"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        self._normalize_inlined_as_list(slot_name="ArmRef", slot_type=Arm, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="EpochRef", slot_type=Epoch, key_name="OID", keyed=True)

        if self.WorkflowRefRef is not None and not isinstance(self.WorkflowRefRef, WorkflowRef):
            self.WorkflowRefRef = WorkflowRef(**as_dict(self.WorkflowRefRef))

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

    ValueRef: str = None
    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ValueRef):
            self.MissingRequiredField("ValueRef")
        if not isinstance(self.ValueRef, str):
            self.ValueRef = str(self.ValueRef)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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

    StudyIndicationRef: Optional[Union[Dict[Union[str, StudyIndicationOID], Union[dict, "StudyIndication"]], List[Union[dict, "StudyIndication"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StudyIndicationRef", slot_type=StudyIndication, key_name="OID", keyed=True)

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
    DescriptionRef: Optional[Union[dict, Description]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyIndicationOID):
            self.OID = StudyIndicationOID(self.OID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

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

    StudyInterventionRefRef: Optional[Union[Dict[Union[str, StudyInterventionOID], Union[dict, "StudyIntervention"]], List[Union[dict, "StudyIntervention"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StudyInterventionRefRef", slot_type=StudyIntervention, key_name="OID", keyed=True)

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
    DescriptionRef: Optional[Union[dict, Description]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyInterventionOID):
            self.OID = StudyInterventionOID(self.OID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

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

    StudyObjectiveRef: Optional[Union[Dict[Union[str, StudyObjectiveOID], Union[dict, "StudyObjective"]], List[Union[dict, "StudyObjective"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StudyObjectiveRef", slot_type=StudyObjective, key_name="OID", keyed=True)

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
    Name: str = None
    Level: Optional[Union[str, "StudyObjectiveLevel"]] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    StudyEndPointRefRef: Optional[Union[Union[dict, "StudyEndPointRef"], List[Union[dict, "StudyEndPointRef"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyObjectiveOID):
            self.OID = StudyObjectiveOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Level is not None and not isinstance(self.Level, StudyObjectiveLevel):
            self.Level = StudyObjectiveLevel(self.Level)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.StudyEndPointRefRef, list):
            self.StudyEndPointRefRef = [self.StudyEndPointRefRef] if self.StudyEndPointRefRef is not None else []
        self.StudyEndPointRefRef = [v if isinstance(v, StudyEndPointRef) else StudyEndPointRef(**as_dict(v)) for v in self.StudyEndPointRefRef]

        super().__post_init__(**kwargs)


@dataclass
class StudyEndPointRef(YAMLRoot):
    """
    Go to start of metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ODM.StudyEndPointRef
    class_class_curie: ClassVar[str] = "odm:StudyEndPointRef"
    class_name: ClassVar[str] = "StudyEndPointRef"
    class_model_uri: ClassVar[URIRef] = ODM.StudyEndPointRef

    StudyEndPointOID: str = None
    OrderNumber: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyEndPointOID):
            self.MissingRequiredField("StudyEndPointOID")
        if not isinstance(self.StudyEndPointOID, str):
            self.StudyEndPointOID = str(self.StudyEndPointOID)

        if self.OrderNumber is not None and not isinstance(self.OrderNumber, int):
            self.OrderNumber = int(self.OrderNumber)

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

    StudyEndPointRefRef: Optional[Union[Dict[Union[str, StudyEndPointOID], Union[dict, "StudyEndPoint"]], List[Union[dict, "StudyEndPoint"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StudyEndPointRefRef", slot_type=StudyEndPoint, key_name="OID", keyed=True)

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
    Name: str = None
    Type: Optional[Union[str, "StudyEndPointType"]] = None
    Level: Optional[Union[str, "StudyEstimandLevel"]] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    FormalExpressionRef: Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEndPointOID):
            self.OID = StudyEndPointOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Type is not None and not isinstance(self.Type, StudyEndPointType):
            self.Type = StudyEndPointType(self.Type)

        if self.Level is not None and not isinstance(self.Level, StudyEstimandLevel):
            self.Level = StudyEstimandLevel(self.Level)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.FormalExpressionRef, list):
            self.FormalExpressionRef = [self.FormalExpressionRef] if self.FormalExpressionRef is not None else []
        self.FormalExpressionRef = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.FormalExpressionRef]

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
    Name: str = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    FormalExpressionRef: Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyTargetPopulationOID):
            self.OID = StudyTargetPopulationOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.FormalExpressionRef, list):
            self.FormalExpressionRef = [self.FormalExpressionRef] if self.FormalExpressionRef is not None else []
        self.FormalExpressionRef = [v if isinstance(v, FormalExpression) else FormalExpression(**as_dict(v)) for v in self.FormalExpressionRef]

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

    StudyEstimandRef: Optional[Union[Dict[Union[str, StudyEstimandOID], Union[dict, "StudyEstimand"]], List[Union[dict, "StudyEstimand"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StudyEstimandRef", slot_type=StudyEstimand, key_name="OID", keyed=True)

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
    Name: str = None
    Level: Optional[Union[str, "StudyEstimandLevel"]] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    StudyTargetPopulationRefRef: Optional[Union[dict, "StudyTargetPopulationRef"]] = None
    StudyInterventionRefRef: Optional[Union[dict, "StudyInterventionRef"]] = None
    StudyEndPointRefRef: Optional[Union[dict, StudyEndPointRef]] = None
    IntercurrentEventRef: Optional[Union[Union[dict, "IntercurrentEvent"], List[Union[dict, "IntercurrentEvent"]]]] = empty_list()
    SummaryMeasureRef: Optional[Union[dict, "SummaryMeasure"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyEstimandOID):
            self.OID = StudyEstimandOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Level is not None and not isinstance(self.Level, StudyEstimandLevel):
            self.Level = StudyEstimandLevel(self.Level)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.StudyTargetPopulationRefRef is not None and not isinstance(self.StudyTargetPopulationRefRef, StudyTargetPopulationRef):
            self.StudyTargetPopulationRefRef = StudyTargetPopulationRef(**as_dict(self.StudyTargetPopulationRefRef))

        if self.StudyInterventionRefRef is not None and not isinstance(self.StudyInterventionRefRef, StudyInterventionRef):
            self.StudyInterventionRefRef = StudyInterventionRef(**as_dict(self.StudyInterventionRefRef))

        if self.StudyEndPointRefRef is not None and not isinstance(self.StudyEndPointRefRef, StudyEndPointRef):
            self.StudyEndPointRefRef = StudyEndPointRef(**as_dict(self.StudyEndPointRefRef))

        if not isinstance(self.IntercurrentEventRef, list):
            self.IntercurrentEventRef = [self.IntercurrentEventRef] if self.IntercurrentEventRef is not None else []
        self.IntercurrentEventRef = [v if isinstance(v, IntercurrentEvent) else IntercurrentEvent(**as_dict(v)) for v in self.IntercurrentEventRef]

        if self.SummaryMeasureRef is not None and not isinstance(self.SummaryMeasureRef, SummaryMeasure):
            self.SummaryMeasureRef = SummaryMeasure(**as_dict(self.SummaryMeasureRef))

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

    InclusionCriteriaRef: Optional[Union[dict, "InclusionCriteria"]] = None
    ExclusionCriteriaRef: Optional[Union[dict, "ExclusionCriteria"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.InclusionCriteriaRef is not None and not isinstance(self.InclusionCriteriaRef, InclusionCriteria):
            self.InclusionCriteriaRef = InclusionCriteria(**as_dict(self.InclusionCriteriaRef))

        if self.ExclusionCriteriaRef is not None and not isinstance(self.ExclusionCriteriaRef, ExclusionCriteria):
            self.ExclusionCriteriaRef = ExclusionCriteria(**as_dict(self.ExclusionCriteriaRef))

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

    CriterionRef: Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="CriterionRef", slot_type=Criterion, key_name="OID", keyed=True)

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

    CriterionRef: Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="CriterionRef", slot_type=Criterion, key_name="OID", keyed=True)

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

    StudyTargetPopulationOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyTargetPopulationOID):
            self.MissingRequiredField("StudyTargetPopulationOID")
        if not isinstance(self.StudyTargetPopulationOID, str):
            self.StudyTargetPopulationOID = str(self.StudyTargetPopulationOID)

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

    StudyInterventionOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyInterventionOID):
            self.MissingRequiredField("StudyInterventionOID")
        if not isinstance(self.StudyInterventionOID, str):
            self.StudyInterventionOID = str(self.StudyInterventionOID)

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

    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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

    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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
    Name: str = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    WorkflowRefRef: Optional[Union[dict, "WorkflowRef"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, ArmOID):
            self.OID = ArmOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.WorkflowRefRef is not None and not isinstance(self.WorkflowRefRef, WorkflowRef):
            self.WorkflowRefRef = WorkflowRef(**as_dict(self.WorkflowRefRef))

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
    Name: str = None
    SequenceNumber: int = None
    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, EpochOID):
            self.OID = EpochOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.SequenceNumber):
            self.MissingRequiredField("SequenceNumber")
        if not isinstance(self.SequenceNumber, int):
            self.SequenceNumber = int(self.SequenceNumber)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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

    WorkflowOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.WorkflowOID):
            self.MissingRequiredField("WorkflowOID")
        if not isinstance(self.WorkflowOID, str):
            self.WorkflowOID = str(self.WorkflowOID)

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

    StudyParameterRef: Optional[Union[Dict[Union[str, StudyParameterOID], Union[dict, "StudyParameter"]], List[Union[dict, "StudyParameter"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StudyParameterRef", slot_type=StudyParameter, key_name="OID", keyed=True)

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
    Term: str = None
    ShortName: Optional[str] = None
    ParameterValueRef: Optional[Union[dict, "ParameterValue"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyParameterOID):
            self.OID = StudyParameterOID(self.OID)

        if self._is_empty(self.Term):
            self.MissingRequiredField("Term")
        if not isinstance(self.Term, str):
            self.Term = str(self.Term)

        if self.ShortName is not None and not isinstance(self.ShortName, str):
            self.ShortName = str(self.ShortName)

        if self.ParameterValueRef is not None and not isinstance(self.ParameterValueRef, ParameterValue):
            self.ParameterValueRef = ParameterValue(**as_dict(self.ParameterValueRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

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

    ValueRef: str = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ValueRef):
            self.MissingRequiredField("ValueRef")
        if not isinstance(self.ValueRef, str):
            self.ValueRef = str(self.ValueRef)

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

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

    StudyTimingRef: Optional[Union[Dict[Union[str, StudyTimingOID], Union[dict, "StudyTiming"]], List[Union[dict, "StudyTiming"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="StudyTimingRef", slot_type=StudyTiming, key_name="OID", keyed=True)

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
    Name: str = None
    AbsoluteTimingConstraintRef: Optional[Union[Dict[Union[str, AbsoluteTimingConstraintOID], Union[dict, "AbsoluteTimingConstraint"]], List[Union[dict, "AbsoluteTimingConstraint"]]]] = empty_dict()
    RelativeTimingConstraintRef: Optional[Union[Dict[Union[str, RelativeTimingConstraintOID], Union[dict, "RelativeTimingConstraint"]], List[Union[dict, "RelativeTimingConstraint"]]]] = empty_dict()
    TransitionTimingConstraintRef: Optional[Union[Dict[Union[str, TransitionTimingConstraintOID], Union[dict, "TransitionTimingConstraint"]], List[Union[dict, "TransitionTimingConstraint"]]]] = empty_dict()
    DurationTimingConstraintRef: Optional[Union[Dict[Union[str, DurationTimingConstraintOID], Union[dict, "DurationTimingConstraint"]], List[Union[dict, "DurationTimingConstraint"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, StudyTimingOID):
            self.OID = StudyTimingOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        self._normalize_inlined_as_list(slot_name="AbsoluteTimingConstraintRef", slot_type=AbsoluteTimingConstraint, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="RelativeTimingConstraintRef", slot_type=RelativeTimingConstraint, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="TransitionTimingConstraintRef", slot_type=TransitionTimingConstraint, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="DurationTimingConstraintRef", slot_type=DurationTimingConstraint, key_name="OID", keyed=True)

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
    Name: str = None
    TransitionOID: str = None
    TimepointTarget: str = None
    MethodOID: Optional[str] = None
    Type: Optional[Union[str, "RelativeTimingConstraintType"]] = None
    TimepointPreWindow: Optional[str] = None
    TimepointPostWindow: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, TransitionTimingConstraintOID):
            self.OID = TransitionTimingConstraintOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.TransitionOID):
            self.MissingRequiredField("TransitionOID")
        if not isinstance(self.TransitionOID, str):
            self.TransitionOID = str(self.TransitionOID)

        if self._is_empty(self.TimepointTarget):
            self.MissingRequiredField("TimepointTarget")
        if not isinstance(self.TimepointTarget, str):
            self.TimepointTarget = str(self.TimepointTarget)

        if self.MethodOID is not None and not isinstance(self.MethodOID, str):
            self.MethodOID = str(self.MethodOID)

        if self.Type is not None and not isinstance(self.Type, RelativeTimingConstraintType):
            self.Type = RelativeTimingConstraintType(self.Type)

        if self.TimepointPreWindow is not None and not isinstance(self.TimepointPreWindow, str):
            self.TimepointPreWindow = str(self.TimepointPreWindow)

        if self.TimepointPostWindow is not None and not isinstance(self.TimepointPostWindow, str):
            self.TimepointPostWindow = str(self.TimepointPostWindow)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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
    Name: str = None
    TimepointTarget: str = None
    StudyEventGroupOID: Optional[str] = None
    StudyEventOID: Optional[str] = None
    TimepointPreWindow: Optional[str] = None
    TimepointPostWindow: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, AbsoluteTimingConstraintOID):
            self.OID = AbsoluteTimingConstraintOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.TimepointTarget):
            self.MissingRequiredField("TimepointTarget")
        if not isinstance(self.TimepointTarget, str):
            self.TimepointTarget = str(self.TimepointTarget)

        if self.StudyEventGroupOID is not None and not isinstance(self.StudyEventGroupOID, str):
            self.StudyEventGroupOID = str(self.StudyEventGroupOID)

        if self.StudyEventOID is not None and not isinstance(self.StudyEventOID, str):
            self.StudyEventOID = str(self.StudyEventOID)

        if self.TimepointPreWindow is not None and not isinstance(self.TimepointPreWindow, str):
            self.TimepointPreWindow = str(self.TimepointPreWindow)

        if self.TimepointPostWindow is not None and not isinstance(self.TimepointPostWindow, str):
            self.TimepointPostWindow = str(self.TimepointPostWindow)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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
    Name: str = None
    TimepointRelativeTarget: str = None
    PredecessorOID: Optional[str] = None
    SuccessorOID: Optional[str] = None
    Type: Optional[Union[str, "RelativeTimingConstraintType"]] = None
    TimepointPreWindow: Optional[str] = None
    TimepointPostWindow: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, RelativeTimingConstraintOID):
            self.OID = RelativeTimingConstraintOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.TimepointRelativeTarget):
            self.MissingRequiredField("TimepointRelativeTarget")
        if not isinstance(self.TimepointRelativeTarget, str):
            self.TimepointRelativeTarget = str(self.TimepointRelativeTarget)

        if self.PredecessorOID is not None and not isinstance(self.PredecessorOID, str):
            self.PredecessorOID = str(self.PredecessorOID)

        if self.SuccessorOID is not None and not isinstance(self.SuccessorOID, str):
            self.SuccessorOID = str(self.SuccessorOID)

        if self.Type is not None and not isinstance(self.Type, RelativeTimingConstraintType):
            self.Type = RelativeTimingConstraintType(self.Type)

        if self.TimepointPreWindow is not None and not isinstance(self.TimepointPreWindow, str):
            self.TimepointPreWindow = str(self.TimepointPreWindow)

        if self.TimepointPostWindow is not None and not isinstance(self.TimepointPostWindow, str):
            self.TimepointPostWindow = str(self.TimepointPostWindow)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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
    Name: str = None
    StructuralElementOID: str = None
    DurationTarget: str = None
    DurationPreWindow: Optional[str] = None
    DurationPostWindow: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, DurationTimingConstraintOID):
            self.OID = DurationTimingConstraintOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.StructuralElementOID):
            self.MissingRequiredField("StructuralElementOID")
        if not isinstance(self.StructuralElementOID, str):
            self.StructuralElementOID = str(self.StructuralElementOID)

        if self._is_empty(self.DurationTarget):
            self.MissingRequiredField("DurationTarget")
        if not isinstance(self.DurationTarget, str):
            self.DurationTarget = str(self.DurationTarget)

        if self.DurationPreWindow is not None and not isinstance(self.DurationPreWindow, str):
            self.DurationPreWindow = str(self.DurationPreWindow)

        if self.DurationPostWindow is not None and not isinstance(self.DurationPostWindow, str):
            self.DurationPostWindow = str(self.DurationPostWindow)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

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
    Name: str = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    WorkflowStartRef: Optional[Union[dict, "WorkflowStart"]] = None
    WorkflowEndRef: Optional[Union[Union[dict, "WorkflowEnd"], List[Union[dict, "WorkflowEnd"]]]] = empty_list()
    TransitionRef: Optional[Union[Dict[Union[str, TransitionOID], Union[dict, "Transition"]], List[Union[dict, "Transition"]]]] = empty_dict()
    BranchingRef: Optional[Union[Dict[Union[str, BranchingOID], Union[dict, "Branching"]], List[Union[dict, "Branching"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, WorkflowDefOID):
            self.OID = WorkflowDefOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if self.WorkflowStartRef is not None and not isinstance(self.WorkflowStartRef, WorkflowStart):
            self.WorkflowStartRef = WorkflowStart(**as_dict(self.WorkflowStartRef))

        if not isinstance(self.WorkflowEndRef, list):
            self.WorkflowEndRef = [self.WorkflowEndRef] if self.WorkflowEndRef is not None else []
        self.WorkflowEndRef = [v if isinstance(v, WorkflowEnd) else WorkflowEnd(**as_dict(v)) for v in self.WorkflowEndRef]

        self._normalize_inlined_as_list(slot_name="TransitionRef", slot_type=Transition, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="BranchingRef", slot_type=Branching, key_name="OID", keyed=True)

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

    StartOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StartOID):
            self.MissingRequiredField("StartOID")
        if not isinstance(self.StartOID, str):
            self.StartOID = str(self.StartOID)

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
    Name: str = None
    SourceOID: str = None
    TargetOID: str = None
    StartConditionOID: Optional[str] = None
    EndConditionOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, TransitionOID):
            self.OID = TransitionOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.SourceOID):
            self.MissingRequiredField("SourceOID")
        if not isinstance(self.SourceOID, str):
            self.SourceOID = str(self.SourceOID)

        if self._is_empty(self.TargetOID):
            self.MissingRequiredField("TargetOID")
        if not isinstance(self.TargetOID, str):
            self.TargetOID = str(self.TargetOID)

        if self.StartConditionOID is not None and not isinstance(self.StartConditionOID, str):
            self.StartConditionOID = str(self.StartConditionOID)

        if self.EndConditionOID is not None and not isinstance(self.EndConditionOID, str):
            self.EndConditionOID = str(self.EndConditionOID)

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
    Name: str = None
    Type: Union[str, "BranchingType"] = None
    TargetTransitionRef: Optional[Union[Union[dict, "TargetTransition"], List[Union[dict, "TargetTransition"]]]] = empty_list()
    DefaultTransitionRef: Optional[Union[Union[dict, "DefaultTransition"], List[Union[dict, "DefaultTransition"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, BranchingOID):
            self.OID = BranchingOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, BranchingType):
            self.Type = BranchingType(self.Type)

        if not isinstance(self.TargetTransitionRef, list):
            self.TargetTransitionRef = [self.TargetTransitionRef] if self.TargetTransitionRef is not None else []
        self.TargetTransitionRef = [v if isinstance(v, TargetTransition) else TargetTransition(**as_dict(v)) for v in self.TargetTransitionRef]

        if not isinstance(self.DefaultTransitionRef, list):
            self.DefaultTransitionRef = [self.DefaultTransitionRef] if self.DefaultTransitionRef is not None else []
        self.DefaultTransitionRef = [v if isinstance(v, DefaultTransition) else DefaultTransition(**as_dict(v)) for v in self.DefaultTransitionRef]

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

    TargetTransitionOID: str = None
    ConditionOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.TargetTransitionOID):
            self.MissingRequiredField("TargetTransitionOID")
        if not isinstance(self.TargetTransitionOID, str):
            self.TargetTransitionOID = str(self.TargetTransitionOID)

        if self.ConditionOID is not None and not isinstance(self.ConditionOID, str):
            self.ConditionOID = str(self.ConditionOID)

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

    TargetTransitionOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.TargetTransitionOID):
            self.MissingRequiredField("TargetTransitionOID")
        if not isinstance(self.TargetTransitionOID, str):
            self.TargetTransitionOID = str(self.TargetTransitionOID)

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

    EndOID: str = None
    _content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.EndOID):
            self.MissingRequiredField("EndOID")
        if not isinstance(self.EndOID, str):
            self.EndOID = str(self.EndOID)

        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

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
    Name: str = None
    ConditionOID: str = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, CriterionOID):
            self.OID = CriterionOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.ConditionOID):
            self.MissingRequiredField("ConditionOID")
        if not isinstance(self.ConditionOID, str):
            self.ConditionOID = str(self.ConditionOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

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

    StudyOID: Optional[str] = None
    UserRefRef: Optional[Union[Dict[Union[str, UserOID], Union[dict, "User"]], List[Union[dict, "User"]]]] = empty_dict()
    OrganizationRef: Optional[Union[Dict[Union[str, OrganizationOID], Union[dict, "Organization"]], List[Union[dict, "Organization"]]]] = empty_dict()
    LocationRefRef: Optional[Union[Dict[Union[str, LocationOID], Union[dict, "Location"]], List[Union[dict, "Location"]]]] = empty_dict()
    SignatureDefRef: Optional[Union[Dict[Union[str, SignatureDefOID], Union[dict, "SignatureDef"]], List[Union[dict, "SignatureDef"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.StudyOID is not None and not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        self._normalize_inlined_as_list(slot_name="UserRefRef", slot_type=User, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="OrganizationRef", slot_type=Organization, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="LocationRefRef", slot_type=Location, key_name="OID", keyed=True)

        self._normalize_inlined_as_list(slot_name="SignatureDefRef", slot_type=SignatureDef, key_name="OID", keyed=True)

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
    UserTypeRef: Optional[Union[str, "UserType"]] = None
    OrganizationOID: Optional[str] = None
    LocationOID: Optional[str] = None
    UserNameRef: Optional[Union[dict, "UserName"]] = None
    PrefixRef: Optional[Union[dict, "Prefix"]] = None
    SuffixRef: Optional[Union[dict, "Suffix"]] = None
    FullNameRef: Optional[Union[dict, "FullName"]] = None
    GivenNameRef: Optional[Union[dict, "GivenName"]] = None
    FamilyNameRef: Optional[Union[dict, "FamilyName"]] = None
    ImageRef: Optional[Union[dict, "Image"]] = None
    AddressRef: Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]] = empty_list()
    TelecomRef: Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, UserOID):
            self.OID = UserOID(self.OID)

        if self.UserTypeRef is not None and not isinstance(self.UserTypeRef, UserType):
            self.UserTypeRef = UserType(self.UserTypeRef)

        if self.OrganizationOID is not None and not isinstance(self.OrganizationOID, str):
            self.OrganizationOID = str(self.OrganizationOID)

        if self.LocationOID is not None and not isinstance(self.LocationOID, str):
            self.LocationOID = str(self.LocationOID)

        if self.UserNameRef is not None and not isinstance(self.UserNameRef, UserName):
            self.UserNameRef = UserName(**as_dict(self.UserNameRef))

        if self.PrefixRef is not None and not isinstance(self.PrefixRef, Prefix):
            self.PrefixRef = Prefix(**as_dict(self.PrefixRef))

        if self.SuffixRef is not None and not isinstance(self.SuffixRef, Suffix):
            self.SuffixRef = Suffix(**as_dict(self.SuffixRef))

        if self.FullNameRef is not None and not isinstance(self.FullNameRef, FullName):
            self.FullNameRef = FullName(**as_dict(self.FullNameRef))

        if self.GivenNameRef is not None and not isinstance(self.GivenNameRef, GivenName):
            self.GivenNameRef = GivenName(**as_dict(self.GivenNameRef))

        if self.FamilyNameRef is not None and not isinstance(self.FamilyNameRef, FamilyName):
            self.FamilyNameRef = FamilyName(**as_dict(self.FamilyNameRef))

        if self.ImageRef is not None and not isinstance(self.ImageRef, Image):
            self.ImageRef = Image(**as_dict(self.ImageRef))

        if not isinstance(self.AddressRef, list):
            self.AddressRef = [self.AddressRef] if self.AddressRef is not None else []
        self.AddressRef = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.AddressRef]

        if not isinstance(self.TelecomRef, list):
            self.TelecomRef = [self.TelecomRef] if self.TelecomRef is not None else []
        self.TelecomRef = [v if isinstance(v, Telecom) else Telecom(**as_dict(v)) for v in self.TelecomRef]

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    ImageFileName: Optional[URIorCURIE] = None
    href: Optional[str] = None
    MimeType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ImageFileName is not None and not isinstance(self.ImageFileName, URIorCURIE):
            self.ImageFileName = URIorCURIE(self.ImageFileName)

        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.MimeType is not None and not isinstance(self.MimeType, str):
            self.MimeType = str(self.MimeType)

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
    Name: str = None
    Type: Union[str, "OrganizationType"] = None
    Role: Optional[str] = None
    LocationOID: Optional[str] = None
    PartOfOrganizationOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    AddressRef: Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]] = empty_list()
    TelecomRef: Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, OrganizationOID):
            self.OID = OrganizationOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, OrganizationType):
            self.Type = OrganizationType(self.Type)

        if self.Role is not None and not isinstance(self.Role, str):
            self.Role = str(self.Role)

        if self.LocationOID is not None and not isinstance(self.LocationOID, str):
            self.LocationOID = str(self.LocationOID)

        if self.PartOfOrganizationOID is not None and not isinstance(self.PartOfOrganizationOID, str):
            self.PartOfOrganizationOID = str(self.PartOfOrganizationOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.AddressRef, list):
            self.AddressRef = [self.AddressRef] if self.AddressRef is not None else []
        self.AddressRef = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.AddressRef]

        if not isinstance(self.TelecomRef, list):
            self.TelecomRef = [self.TelecomRef] if self.TelecomRef is not None else []
        self.TelecomRef = [v if isinstance(v, Telecom) else Telecom(**as_dict(v)) for v in self.TelecomRef]

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
    Name: str = None
    Role: Optional[str] = None
    OrganizationOID: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    MetaDataVersionRefRef: Optional[Union[Union[dict, "MetaDataVersionRef"], List[Union[dict, "MetaDataVersionRef"]]]] = empty_list()
    AddressRef: Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]] = empty_list()
    TelecomRef: Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]] = empty_list()
    QueryRef: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, LocationOID):
            self.OID = LocationOID(self.OID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Role is not None and not isinstance(self.Role, str):
            self.Role = str(self.Role)

        if self.OrganizationOID is not None and not isinstance(self.OrganizationOID, str):
            self.OrganizationOID = str(self.OrganizationOID)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        if not isinstance(self.MetaDataVersionRefRef, list):
            self.MetaDataVersionRefRef = [self.MetaDataVersionRefRef] if self.MetaDataVersionRefRef is not None else []
        self.MetaDataVersionRefRef = [v if isinstance(v, MetaDataVersionRef) else MetaDataVersionRef(**as_dict(v)) for v in self.MetaDataVersionRefRef]

        if not isinstance(self.AddressRef, list):
            self.AddressRef = [self.AddressRef] if self.AddressRef is not None else []
        self.AddressRef = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.AddressRef]

        if not isinstance(self.TelecomRef, list):
            self.TelecomRef = [self.TelecomRef] if self.TelecomRef is not None else []
        self.TelecomRef = [v if isinstance(v, Telecom) else Telecom(**as_dict(v)) for v in self.TelecomRef]

        self._normalize_inlined_as_list(slot_name="QueryRef", slot_type=Query, key_name="OID", keyed=True)

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

    StreetNameRef: Optional[Union[dict, "StreetName"]] = None
    HouseNumberRef: Optional[Union[dict, "HouseNumber"]] = None
    CityRef: Optional[Union[dict, "City"]] = None
    StateProvRef: Optional[Union[dict, "StateProv"]] = None
    CountryRef: Optional[Union[dict, "Country"]] = None
    PostalCodeRef: Optional[Union[dict, "PostalCode"]] = None
    GeoPositionRef: Optional[Union[dict, "GeoPosition"]] = None
    OtherTextRef: Optional[Union[dict, "OtherText"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.StreetNameRef is not None and not isinstance(self.StreetNameRef, StreetName):
            self.StreetNameRef = StreetName(**as_dict(self.StreetNameRef))

        if self.HouseNumberRef is not None and not isinstance(self.HouseNumberRef, HouseNumber):
            self.HouseNumberRef = HouseNumber(**as_dict(self.HouseNumberRef))

        if self.CityRef is not None and not isinstance(self.CityRef, City):
            self.CityRef = City(**as_dict(self.CityRef))

        if self.StateProvRef is not None and not isinstance(self.StateProvRef, StateProv):
            self.StateProvRef = StateProv(**as_dict(self.StateProvRef))

        if self.CountryRef is not None and not isinstance(self.CountryRef, Country):
            self.CountryRef = Country(**as_dict(self.CountryRef))

        if self.PostalCodeRef is not None and not isinstance(self.PostalCodeRef, PostalCode):
            self.PostalCodeRef = PostalCode(**as_dict(self.PostalCodeRef))

        if self.GeoPositionRef is not None and not isinstance(self.GeoPositionRef, GeoPosition):
            self.GeoPositionRef = GeoPosition(**as_dict(self.GeoPositionRef))

        if self.OtherTextRef is not None and not isinstance(self.OtherTextRef, OtherText):
            self.OtherTextRef = OtherText(**as_dict(self.OtherTextRef))

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

    TelecomType: Union[str, "TelecomTypeType"] = None
    ValueRef: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.TelecomType):
            self.MissingRequiredField("TelecomType")
        if not isinstance(self.TelecomType, TelecomTypeType):
            self.TelecomType = TelecomTypeType(self.TelecomType)

        if self._is_empty(self.ValueRef):
            self.MissingRequiredField("ValueRef")
        if not isinstance(self.ValueRef, str):
            self.ValueRef = str(self.ValueRef)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    Longitude: Optional[Decimal] = None
    Latitude: Optional[Decimal] = None
    Altitude: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Longitude is not None and not isinstance(self.Longitude, Decimal):
            self.Longitude = Decimal(self.Longitude)

        if self.Latitude is not None and not isinstance(self.Latitude, Decimal):
            self.Latitude = Decimal(self.Latitude)

        if self.Altitude is not None and not isinstance(self.Altitude, Decimal):
            self.Altitude = Decimal(self.Altitude)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    StudyOID: str = None
    MetaDataVersionOID: str = None
    EffectiveDate: Union[str, XSDDate] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyOID):
            self.MissingRequiredField("StudyOID")
        if not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        if self._is_empty(self.MetaDataVersionOID):
            self.MissingRequiredField("MetaDataVersionOID")
        if not isinstance(self.MetaDataVersionOID, str):
            self.MetaDataVersionOID = str(self.MetaDataVersionOID)

        if self._is_empty(self.EffectiveDate):
            self.MissingRequiredField("EffectiveDate")
        if not isinstance(self.EffectiveDate, XSDDate):
            self.EffectiveDate = XSDDate(self.EffectiveDate)

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
    Methodology: Optional[Union[str, "SignMethod"]] = None
    MeaningRef: Optional[Union[dict, "Meaning"]] = None
    LegalReasonRef: Optional[Union[dict, "LegalReason"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, SignatureDefOID):
            self.OID = SignatureDefOID(self.OID)

        if self.Methodology is not None and not isinstance(self.Methodology, SignMethod):
            self.Methodology = SignMethod(self.Methodology)

        if self.MeaningRef is not None and not isinstance(self.MeaningRef, Meaning):
            self.MeaningRef = Meaning(**as_dict(self.MeaningRef))

        if self.LegalReasonRef is not None and not isinstance(self.LegalReasonRef, LegalReason):
            self.LegalReasonRef = LegalReason(**as_dict(self.LegalReasonRef))

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    StudyOID: str = None
    MetaDataVersionOID: str = None
    ItemGroupDataRef: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    AuditRecordRef: Optional[Union[dict, "AuditRecord"]] = None
    SignatureRefRef: Optional[Union[str, SignatureID]] = None
    AnnotationRef: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyOID):
            self.MissingRequiredField("StudyOID")
        if not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        if self._is_empty(self.MetaDataVersionOID):
            self.MissingRequiredField("MetaDataVersionOID")
        if not isinstance(self.MetaDataVersionOID, str):
            self.MetaDataVersionOID = str(self.MetaDataVersionOID)

        if not isinstance(self.ItemGroupDataRef, list):
            self.ItemGroupDataRef = [self.ItemGroupDataRef] if self.ItemGroupDataRef is not None else []
        self.ItemGroupDataRef = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.ItemGroupDataRef]

        if self.AuditRecordRef is not None and not isinstance(self.AuditRecordRef, AuditRecord):
            self.AuditRecordRef = AuditRecord(**as_dict(self.AuditRecordRef))

        if self.SignatureRefRef is not None and not isinstance(self.SignatureRefRef, SignatureID):
            self.SignatureRefRef = SignatureID(self.SignatureRefRef)

        if self.AnnotationRef is not None and not isinstance(self.AnnotationRef, AnnotationID):
            self.AnnotationRef = AnnotationID(self.AnnotationRef)

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

    StudyOID: str = None
    MetaDataVersionOID: str = None
    SubjectDataRef: Optional[Union[Union[dict, "SubjectData"], List[Union[dict, "SubjectData"]]]] = empty_list()
    ItemGroupDataRef: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    QueryRef: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    AuditRecordRef: Optional[Union[dict, "AuditRecord"]] = None
    SignatureRefRef: Optional[Union[str, SignatureID]] = None
    AnnotationRef: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyOID):
            self.MissingRequiredField("StudyOID")
        if not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        if self._is_empty(self.MetaDataVersionOID):
            self.MissingRequiredField("MetaDataVersionOID")
        if not isinstance(self.MetaDataVersionOID, str):
            self.MetaDataVersionOID = str(self.MetaDataVersionOID)

        if not isinstance(self.SubjectDataRef, list):
            self.SubjectDataRef = [self.SubjectDataRef] if self.SubjectDataRef is not None else []
        self.SubjectDataRef = [v if isinstance(v, SubjectData) else SubjectData(**as_dict(v)) for v in self.SubjectDataRef]

        if not isinstance(self.ItemGroupDataRef, list):
            self.ItemGroupDataRef = [self.ItemGroupDataRef] if self.ItemGroupDataRef is not None else []
        self.ItemGroupDataRef = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.ItemGroupDataRef]

        self._normalize_inlined_as_list(slot_name="QueryRef", slot_type=Query, key_name="OID", keyed=True)

        if self.AuditRecordRef is not None and not isinstance(self.AuditRecordRef, AuditRecord):
            self.AuditRecordRef = AuditRecord(**as_dict(self.AuditRecordRef))

        if self.SignatureRefRef is not None and not isinstance(self.SignatureRefRef, SignatureID):
            self.SignatureRefRef = SignatureID(self.SignatureRefRef)

        if self.AnnotationRef is not None and not isinstance(self.AnnotationRef, AnnotationID):
            self.AnnotationRef = AnnotationID(self.AnnotationRef)

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

    SubjectKey: str = None
    TransactionTypeRef: Optional[Union[str, "TransactionType"]] = None
    InvestigatorRefRef: Optional[Union[dict, "InvestigatorRef"]] = None
    SiteRefRef: Optional[Union[dict, "SiteRef"]] = None
    StudyEventDataRef: Optional[Union[Union[dict, "StudyEventData"], List[Union[dict, "StudyEventData"]]]] = empty_list()
    QueryRef: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    AuditRecordRef: Optional[Union[dict, "AuditRecord"]] = None
    SignatureRefRef: Optional[Union[str, SignatureID]] = None
    AnnotationRef: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.SubjectKey):
            self.MissingRequiredField("SubjectKey")
        if not isinstance(self.SubjectKey, str):
            self.SubjectKey = str(self.SubjectKey)

        if self.TransactionTypeRef is not None and not isinstance(self.TransactionTypeRef, TransactionType):
            self.TransactionTypeRef = TransactionType(self.TransactionTypeRef)

        if self.InvestigatorRefRef is not None and not isinstance(self.InvestigatorRefRef, InvestigatorRef):
            self.InvestigatorRefRef = InvestigatorRef(**as_dict(self.InvestigatorRefRef))

        if self.SiteRefRef is not None and not isinstance(self.SiteRefRef, SiteRef):
            self.SiteRefRef = SiteRef(**as_dict(self.SiteRefRef))

        if not isinstance(self.StudyEventDataRef, list):
            self.StudyEventDataRef = [self.StudyEventDataRef] if self.StudyEventDataRef is not None else []
        self.StudyEventDataRef = [v if isinstance(v, StudyEventData) else StudyEventData(**as_dict(v)) for v in self.StudyEventDataRef]

        self._normalize_inlined_as_list(slot_name="QueryRef", slot_type=Query, key_name="OID", keyed=True)

        if self.AuditRecordRef is not None and not isinstance(self.AuditRecordRef, AuditRecord):
            self.AuditRecordRef = AuditRecord(**as_dict(self.AuditRecordRef))

        if self.SignatureRefRef is not None and not isinstance(self.SignatureRefRef, SignatureID):
            self.SignatureRefRef = SignatureID(self.SignatureRefRef)

        if self.AnnotationRef is not None and not isinstance(self.AnnotationRef, AnnotationID):
            self.AnnotationRef = AnnotationID(self.AnnotationRef)

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

    LocationOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.LocationOID):
            self.MissingRequiredField("LocationOID")
        if not isinstance(self.LocationOID, str):
            self.LocationOID = str(self.LocationOID)

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

    UserOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.UserOID):
            self.MissingRequiredField("UserOID")
        if not isinstance(self.UserOID, str):
            self.UserOID = str(self.UserOID)

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

    StudyEventOID: str = None
    StudyEventRepeatKey: Optional[str] = None
    TransactionTypeRef: Optional[Union[str, "TransactionType"]] = None
    ItemGroupDataRef: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    QueryRef: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    AuditRecordRef: Optional[Union[dict, "AuditRecord"]] = None
    SignatureRefRef: Optional[Union[str, SignatureID]] = None
    AnnotationRef: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyEventOID):
            self.MissingRequiredField("StudyEventOID")
        if not isinstance(self.StudyEventOID, str):
            self.StudyEventOID = str(self.StudyEventOID)

        if self.StudyEventRepeatKey is not None and not isinstance(self.StudyEventRepeatKey, str):
            self.StudyEventRepeatKey = str(self.StudyEventRepeatKey)

        if self.TransactionTypeRef is not None and not isinstance(self.TransactionTypeRef, TransactionType):
            self.TransactionTypeRef = TransactionType(self.TransactionTypeRef)

        if not isinstance(self.ItemGroupDataRef, list):
            self.ItemGroupDataRef = [self.ItemGroupDataRef] if self.ItemGroupDataRef is not None else []
        self.ItemGroupDataRef = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.ItemGroupDataRef]

        self._normalize_inlined_as_list(slot_name="QueryRef", slot_type=Query, key_name="OID", keyed=True)

        if self.AuditRecordRef is not None and not isinstance(self.AuditRecordRef, AuditRecord):
            self.AuditRecordRef = AuditRecord(**as_dict(self.AuditRecordRef))

        if self.SignatureRefRef is not None and not isinstance(self.SignatureRefRef, SignatureID):
            self.SignatureRefRef = SignatureID(self.SignatureRefRef)

        if self.AnnotationRef is not None and not isinstance(self.AnnotationRef, AnnotationID):
            self.AnnotationRef = AnnotationID(self.AnnotationRef)

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

    ItemGroupOID: str = None
    ItemGroupRepeatKey: Optional[str] = None
    TransactionTypeRef: Optional[Union[str, "TransactionType"]] = None
    ItemGroupDataSeq: Optional[int] = None
    QueryRef: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    ItemGroupDataRef: Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]] = empty_list()
    ItemDataRef: Optional[Union[Union[dict, "ItemData"], List[Union[dict, "ItemData"]]]] = empty_list()
    AuditRecordRef: Optional[Union[dict, "AuditRecord"]] = None
    SignatureRefRef: Optional[Union[str, SignatureID]] = None
    AnnotationRef: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ItemGroupOID):
            self.MissingRequiredField("ItemGroupOID")
        if not isinstance(self.ItemGroupOID, str):
            self.ItemGroupOID = str(self.ItemGroupOID)

        if self.ItemGroupRepeatKey is not None and not isinstance(self.ItemGroupRepeatKey, str):
            self.ItemGroupRepeatKey = str(self.ItemGroupRepeatKey)

        if self.TransactionTypeRef is not None and not isinstance(self.TransactionTypeRef, TransactionType):
            self.TransactionTypeRef = TransactionType(self.TransactionTypeRef)

        if self.ItemGroupDataSeq is not None and not isinstance(self.ItemGroupDataSeq, int):
            self.ItemGroupDataSeq = int(self.ItemGroupDataSeq)

        self._normalize_inlined_as_list(slot_name="QueryRef", slot_type=Query, key_name="OID", keyed=True)

        if not isinstance(self.ItemGroupDataRef, list):
            self.ItemGroupDataRef = [self.ItemGroupDataRef] if self.ItemGroupDataRef is not None else []
        self.ItemGroupDataRef = [v if isinstance(v, ItemGroupData) else ItemGroupData(**as_dict(v)) for v in self.ItemGroupDataRef]

        if not isinstance(self.ItemDataRef, list):
            self.ItemDataRef = [self.ItemDataRef] if self.ItemDataRef is not None else []
        self.ItemDataRef = [v if isinstance(v, ItemData) else ItemData(**as_dict(v)) for v in self.ItemDataRef]

        if self.AuditRecordRef is not None and not isinstance(self.AuditRecordRef, AuditRecord):
            self.AuditRecordRef = AuditRecord(**as_dict(self.AuditRecordRef))

        if self.SignatureRefRef is not None and not isinstance(self.SignatureRefRef, SignatureID):
            self.SignatureRefRef = SignatureID(self.SignatureRefRef)

        if self.AnnotationRef is not None and not isinstance(self.AnnotationRef, AnnotationID):
            self.AnnotationRef = AnnotationID(self.AnnotationRef)

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

    ItemOID: str = None
    TransactionTypeRef: Optional[Union[str, "TransactionType"]] = None
    IsNull: Optional[Union[str, "YesOnly"]] = None
    ValueRef: Optional[Union[Union[dict, "Value"], List[Union[dict, "Value"]]]] = empty_list()
    QueryRef: Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]] = empty_dict()
    AuditRecordRef: Optional[Union[dict, "AuditRecord"]] = None
    SignatureRefRef: Optional[Union[str, SignatureID]] = None
    AnnotationRef: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ItemOID):
            self.MissingRequiredField("ItemOID")
        if not isinstance(self.ItemOID, str):
            self.ItemOID = str(self.ItemOID)

        if self.TransactionTypeRef is not None and not isinstance(self.TransactionTypeRef, TransactionType):
            self.TransactionTypeRef = TransactionType(self.TransactionTypeRef)

        if self.IsNull is not None and not isinstance(self.IsNull, YesOnly):
            self.IsNull = YesOnly(self.IsNull)

        if not isinstance(self.ValueRef, list):
            self.ValueRef = [self.ValueRef] if self.ValueRef is not None else []
        self.ValueRef = [v if isinstance(v, Value) else Value(**as_dict(v)) for v in self.ValueRef]

        self._normalize_inlined_as_list(slot_name="QueryRef", slot_type=Query, key_name="OID", keyed=True)

        if self.AuditRecordRef is not None and not isinstance(self.AuditRecordRef, AuditRecord):
            self.AuditRecordRef = AuditRecord(**as_dict(self.AuditRecordRef))

        if self.SignatureRefRef is not None and not isinstance(self.SignatureRefRef, SignatureID):
            self.SignatureRefRef = SignatureID(self.SignatureRefRef)

        if self.AnnotationRef is not None and not isinstance(self.AnnotationRef, AnnotationID):
            self.AnnotationRef = AnnotationID(self.AnnotationRef)

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

    EditPoint: Optional[Union[str, "EditPointType"]] = None
    UsedMethod: Optional[Union[str, "YesOrNo"]] = None
    UserRefRef: Optional[Union[dict, "UserRef"]] = None
    LocationRefRef: Optional[Union[dict, "LocationRef"]] = None
    DateTimeStampRef: Optional[Union[dict, "DateTimeStamp"]] = None
    ReasonForChangeRef: Optional[Union[dict, "ReasonForChange"]] = None
    SourceIDRef: Optional[Union[dict, "SourceID"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.EditPoint is not None and not isinstance(self.EditPoint, EditPointType):
            self.EditPoint = EditPointType(self.EditPoint)

        if self.UsedMethod is not None and not isinstance(self.UsedMethod, YesOrNo):
            self.UsedMethod = YesOrNo(self.UsedMethod)

        if self.UserRefRef is not None and not isinstance(self.UserRefRef, UserRef):
            self.UserRefRef = UserRef(**as_dict(self.UserRefRef))

        if self.LocationRefRef is not None and not isinstance(self.LocationRefRef, LocationRef):
            self.LocationRefRef = LocationRef(**as_dict(self.LocationRefRef))

        if self.DateTimeStampRef is not None and not isinstance(self.DateTimeStampRef, DateTimeStamp):
            self.DateTimeStampRef = DateTimeStamp(**as_dict(self.DateTimeStampRef))

        if self.ReasonForChangeRef is not None and not isinstance(self.ReasonForChangeRef, ReasonForChange):
            self.ReasonForChangeRef = ReasonForChange(**as_dict(self.ReasonForChangeRef))

        if self.SourceIDRef is not None and not isinstance(self.SourceIDRef, SourceID):
            self.SourceIDRef = SourceID(**as_dict(self.SourceIDRef))

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

    UserOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.UserOID):
            self.MissingRequiredField("UserOID")
        if not isinstance(self.UserOID, str):
            self.UserOID = str(self.UserOID)

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

    LocationOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.LocationOID):
            self.MissingRequiredField("LocationOID")
        if not isinstance(self.LocationOID, str):
            self.LocationOID = str(self.LocationOID)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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

    _content: Optional[str] = None
    range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

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
    UserRefRef: Optional[Union[dict, UserRef]] = None
    LocationRefRef: Optional[Union[dict, LocationRef]] = None
    SignatureRefRef: Optional[Union[dict, "SignatureRef"]] = None
    DateTimeStampRef: Optional[Union[dict, DateTimeStamp]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, SignatureID):
            self.ID = SignatureID(self.ID)

        if self.UserRefRef is not None and not isinstance(self.UserRefRef, UserRef):
            self.UserRefRef = UserRef(**as_dict(self.UserRefRef))

        if self.LocationRefRef is not None and not isinstance(self.LocationRefRef, LocationRef):
            self.LocationRefRef = LocationRef(**as_dict(self.LocationRefRef))

        if self.SignatureRefRef is not None and not isinstance(self.SignatureRefRef, SignatureRef):
            self.SignatureRefRef = SignatureRef(**as_dict(self.SignatureRefRef))

        if self.DateTimeStampRef is not None and not isinstance(self.DateTimeStampRef, DateTimeStamp):
            self.DateTimeStampRef = DateTimeStamp(**as_dict(self.DateTimeStampRef))

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

    SignatureOID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.SignatureOID):
            self.MissingRequiredField("SignatureOID")
        if not isinstance(self.SignatureOID, str):
            self.SignatureOID = str(self.SignatureOID)

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

    StudyOID: str = None
    MetaDataVersionOID: str = None
    KeySetRef: Optional[Union[dict, "KeySet"]] = None
    AnnotationRef: Optional[Union[str, AnnotationID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyOID):
            self.MissingRequiredField("StudyOID")
        if not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        if self._is_empty(self.MetaDataVersionOID):
            self.MissingRequiredField("MetaDataVersionOID")
        if not isinstance(self.MetaDataVersionOID, str):
            self.MetaDataVersionOID = str(self.MetaDataVersionOID)

        if self.KeySetRef is not None and not isinstance(self.KeySetRef, KeySet):
            self.KeySetRef = KeySet(**as_dict(self.KeySetRef))

        if self.KeySetRef is not None and not isinstance(self.KeySetRef, KeySet):
            self.KeySetRef = KeySet(**as_dict(self.KeySetRef))

        if self.AnnotationRef is not None and not isinstance(self.AnnotationRef, AnnotationID):
            self.AnnotationRef = AnnotationID(self.AnnotationRef)

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

    StudyOID: str = None
    SubjectKey: Optional[str] = None
    MetaDataVersionOID: Optional[str] = None
    StudyEventOID: Optional[str] = None
    StudyEventRepeatKey: Optional[str] = None
    ItemGroupOID: Optional[str] = None
    ItemGroupRepeatKey: Optional[str] = None
    ItemOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.StudyOID):
            self.MissingRequiredField("StudyOID")
        if not isinstance(self.StudyOID, str):
            self.StudyOID = str(self.StudyOID)

        if self.SubjectKey is not None and not isinstance(self.SubjectKey, str):
            self.SubjectKey = str(self.SubjectKey)

        if self.MetaDataVersionOID is not None and not isinstance(self.MetaDataVersionOID, str):
            self.MetaDataVersionOID = str(self.MetaDataVersionOID)

        if self.StudyEventOID is not None and not isinstance(self.StudyEventOID, str):
            self.StudyEventOID = str(self.StudyEventOID)

        if self.StudyEventRepeatKey is not None and not isinstance(self.StudyEventRepeatKey, str):
            self.StudyEventRepeatKey = str(self.StudyEventRepeatKey)

        if self.ItemGroupOID is not None and not isinstance(self.ItemGroupOID, str):
            self.ItemGroupOID = str(self.ItemGroupOID)

        if self.ItemGroupRepeatKey is not None and not isinstance(self.ItemGroupRepeatKey, str):
            self.ItemGroupRepeatKey = str(self.ItemGroupRepeatKey)

        if self.ItemOID is not None and not isinstance(self.ItemOID, str):
            self.ItemOID = str(self.ItemOID)

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
    SeqNum: int = None
    TransactionTypeRef: Optional[Union[str, "TransactionType"]] = None
    CommentRef: Optional[Union[dict, "Comment"]] = None
    CodingRef: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    FlagRef: Optional[Union[Union[dict, "Flag"], List[Union[dict, "Flag"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, AnnotationID):
            self.ID = AnnotationID(self.ID)

        if self._is_empty(self.SeqNum):
            self.MissingRequiredField("SeqNum")
        if not isinstance(self.SeqNum, int):
            self.SeqNum = int(self.SeqNum)

        if self.TransactionTypeRef is not None and not isinstance(self.TransactionTypeRef, TransactionType):
            self.TransactionTypeRef = TransactionType(self.TransactionTypeRef)

        if self.CommentRef is not None and not isinstance(self.CommentRef, Comment):
            self.CommentRef = Comment(**as_dict(self.CommentRef))

        if not isinstance(self.CodingRef, list):
            self.CodingRef = [self.CodingRef] if self.CodingRef is not None else []
        self.CodingRef = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.CodingRef]

        if not isinstance(self.FlagRef, list):
            self.FlagRef = [self.FlagRef] if self.FlagRef is not None else []
        self.FlagRef = [v if isinstance(v, Flag) else Flag(**as_dict(v)) for v in self.FlagRef]

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

    SponsorOrSite: Optional[Union[str, "CommentType"]] = None
    TranslatedTextRef: Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.SponsorOrSite is not None and not isinstance(self.SponsorOrSite, CommentType):
            self.SponsorOrSite = CommentType(self.SponsorOrSite)

        if not isinstance(self.TranslatedTextRef, list):
            self.TranslatedTextRef = [self.TranslatedTextRef] if self.TranslatedTextRef is not None else []
        self.TranslatedTextRef = [v if isinstance(v, TranslatedText) else TranslatedText(**as_dict(v)) for v in self.TranslatedTextRef]

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

    FlagValueRef: Optional[Union[dict, "FlagValue"]] = None
    FlagTypeRef: Optional[Union[dict, "FlagType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.FlagValueRef is not None and not isinstance(self.FlagValueRef, FlagValue):
            self.FlagValueRef = FlagValue(**as_dict(self.FlagValueRef))

        if self.FlagTypeRef is not None and not isinstance(self.FlagTypeRef, FlagType):
            self.FlagTypeRef = FlagType(**as_dict(self.FlagTypeRef))

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

    CodeListOID: str = None
    _content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.CodeListOID):
            self.MissingRequiredField("CodeListOID")
        if not isinstance(self.CodeListOID, str):
            self.CodeListOID = str(self.CodeListOID)

        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

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

    CodeListOID: str = None
    _content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.CodeListOID):
            self.MissingRequiredField("CodeListOID")
        if not isinstance(self.CodeListOID, str):
            self.CodeListOID = str(self.CodeListOID)

        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

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

    System: Union[str, URIorCURIE] = None
    CodeRef: Optional[str] = None
    SystemName: Optional[str] = None
    SystemVersion: Optional[str] = None
    Label: Optional[str] = None
    href: Optional[Union[str, URIorCURIE]] = None
    ref: Optional[Union[str, URIorCURIE]] = None
    CommentOID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.System):
            self.MissingRequiredField("System")
        if not isinstance(self.System, URIorCURIE):
            self.System = URIorCURIE(self.System)

        if self.CodeRef is not None and not isinstance(self.CodeRef, str):
            self.CodeRef = str(self.CodeRef)

        if self.SystemName is not None and not isinstance(self.SystemName, str):
            self.SystemName = str(self.SystemName)

        if self.SystemVersion is not None and not isinstance(self.SystemVersion, str):
            self.SystemVersion = str(self.SystemVersion)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.href is not None and not isinstance(self.href, URIorCURIE):
            self.href = URIorCURIE(self.href)

        if self.ref is not None and not isinstance(self.ref, URIorCURIE):
            self.ref = URIorCURIE(self.ref)

        if self.CommentOID is not None and not isinstance(self.CommentOID, str):
            self.CommentOID = str(self.CommentOID)

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
    Source: Union[str, "QuerySourceType"] = None
    State: Union[str, "QueryStateType"] = None
    LastUpdateDatetime: Union[str, XSDDateTime] = None
    Target: Optional[str] = None
    Type: Optional[Union[str, "QueryType"]] = None
    Name: Optional[str] = None
    ValueRef: Optional[Union[dict, "Value"]] = None
    AuditRecordRef: Optional[Union[Union[dict, AuditRecord], List[Union[dict, AuditRecord]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.OID):
            self.MissingRequiredField("OID")
        if not isinstance(self.OID, QueryOID):
            self.OID = QueryOID(self.OID)

        if self._is_empty(self.Source):
            self.MissingRequiredField("Source")
        if not isinstance(self.Source, QuerySourceType):
            self.Source = QuerySourceType(self.Source)

        if self._is_empty(self.State):
            self.MissingRequiredField("State")
        if not isinstance(self.State, QueryStateType):
            self.State = QueryStateType(self.State)

        if self._is_empty(self.LastUpdateDatetime):
            self.MissingRequiredField("LastUpdateDatetime")
        if not isinstance(self.LastUpdateDatetime, XSDDateTime):
            self.LastUpdateDatetime = XSDDateTime(self.LastUpdateDatetime)

        if self.Target is not None and not isinstance(self.Target, str):
            self.Target = str(self.Target)

        if self.Type is not None and not isinstance(self.Type, QueryType):
            self.Type = QueryType(self.Type)

        if self.Name is not None and not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.ValueRef is not None and not isinstance(self.ValueRef, Value):
            self.ValueRef = Value(**as_dict(self.ValueRef))

        if not isinstance(self.AuditRecordRef, list):
            self.AuditRecordRef = [self.AuditRecordRef] if self.AuditRecordRef is not None else []
        self.AuditRecordRef = [v if isinstance(v, AuditRecord) else AuditRecord(**as_dict(v)) for v in self.AuditRecordRef]

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

    SeqNum: Optional[int] = None
    _content: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.SeqNum is not None and not isinstance(self.SeqNum, int):
            self.SeqNum = int(self.SeqNum)

        if self._content is not None and not isinstance(self._content, str):
            self._content = str(self._content)

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

    FileTypeRef: Union[str, "FileType"] = None
    FileOID: str = None
    CreationDateTime: Union[str, XSDDateTime] = None
    GranularityRef: Optional[Union[str, "Granularity"]] = None
    ContextRef: Optional[Union[str, "Context"]] = None
    PriorFileOID: Optional[str] = None
    AsOfDateTime: Optional[Union[str, XSDDateTime]] = None
    ODMVersionRef: Optional[str] = None
    Originator: Optional[str] = None
    SourceSystem: Optional[str] = None
    SourceSystemVersion: Optional[str] = None
    DescriptionRef: Optional[Union[dict, Description]] = None
    StudyRef: Optional[Union[Dict[Union[str, StudyOID], Union[dict, Study]], List[Union[dict, Study]]]] = empty_dict()
    AdminDataRef: Optional[Union[Union[dict, AdminData], List[Union[dict, AdminData]]]] = empty_list()
    ReferenceDataRef: Optional[Union[Union[dict, ReferenceData], List[Union[dict, ReferenceData]]]] = empty_list()
    ClinicalDataRef: Optional[Union[Union[dict, ClinicalData], List[Union[dict, ClinicalData]]]] = empty_list()
    AssociationRef: Optional[Union[Union[dict, Association], List[Union[dict, Association]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.FileTypeRef):
            self.MissingRequiredField("FileTypeRef")
        if not isinstance(self.FileTypeRef, FileType):
            self.FileTypeRef = FileType(self.FileTypeRef)

        if self._is_empty(self.FileOID):
            self.MissingRequiredField("FileOID")
        if not isinstance(self.FileOID, str):
            self.FileOID = str(self.FileOID)

        if self._is_empty(self.CreationDateTime):
            self.MissingRequiredField("CreationDateTime")
        if not isinstance(self.CreationDateTime, XSDDateTime):
            self.CreationDateTime = XSDDateTime(self.CreationDateTime)

        if self.GranularityRef is not None and not isinstance(self.GranularityRef, Granularity):
            self.GranularityRef = Granularity(self.GranularityRef)

        if self.ContextRef is not None and not isinstance(self.ContextRef, Context):
            self.ContextRef = Context(self.ContextRef)

        if self.PriorFileOID is not None and not isinstance(self.PriorFileOID, str):
            self.PriorFileOID = str(self.PriorFileOID)

        if self.AsOfDateTime is not None and not isinstance(self.AsOfDateTime, XSDDateTime):
            self.AsOfDateTime = XSDDateTime(self.AsOfDateTime)

        if self.ODMVersionRef is not None and not isinstance(self.ODMVersionRef, str):
            self.ODMVersionRef = str(self.ODMVersionRef)

        if self.Originator is not None and not isinstance(self.Originator, str):
            self.Originator = str(self.Originator)

        if self.SourceSystem is not None and not isinstance(self.SourceSystem, str):
            self.SourceSystem = str(self.SourceSystem)

        if self.SourceSystemVersion is not None and not isinstance(self.SourceSystemVersion, str):
            self.SourceSystemVersion = str(self.SourceSystemVersion)

        if self.DescriptionRef is not None and not isinstance(self.DescriptionRef, Description):
            self.DescriptionRef = Description(**as_dict(self.DescriptionRef))

        self._normalize_inlined_as_list(slot_name="StudyRef", slot_type=Study, key_name="OID", keyed=True)

        if not isinstance(self.AdminDataRef, list):
            self.AdminDataRef = [self.AdminDataRef] if self.AdminDataRef is not None else []
        self.AdminDataRef = [v if isinstance(v, AdminData) else AdminData(**as_dict(v)) for v in self.AdminDataRef]

        if not isinstance(self.ReferenceDataRef, list):
            self.ReferenceDataRef = [self.ReferenceDataRef] if self.ReferenceDataRef is not None else []
        self.ReferenceDataRef = [v if isinstance(v, ReferenceData) else ReferenceData(**as_dict(v)) for v in self.ReferenceDataRef]

        if not isinstance(self.ClinicalDataRef, list):
            self.ClinicalDataRef = [self.ClinicalDataRef] if self.ClinicalDataRef is not None else []
        self.ClinicalDataRef = [v if isinstance(v, ClinicalData) else ClinicalData(**as_dict(v)) for v in self.ClinicalDataRef]

        if not isinstance(self.AssociationRef, list):
            self.AssociationRef = [self.AssociationRef] if self.AssociationRef is not None else []
        self.AssociationRef = [v if isinstance(v, Association) else Association(**as_dict(v)) for v in self.AssociationRef]

        super().__post_init__(**kwargs)


# Enumerations
class DataType(EnumDefinitionImpl):
    """
    Enumeration used in DataTypeRef
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
        description="Enumeration used in DataTypeRef",
    )

class CLDataType(EnumDefinitionImpl):
    """
    Enumeration used in DataTypeRef
    """
    integer = PermissibleValue(text="integer")
    decimal = PermissibleValue(text="decimal")
    text = PermissibleValue(text="text")
    string = PermissibleValue(text="string")

    _defn = EnumDefinition(
        name="CLDataType",
        description="Enumeration used in DataTypeRef",
    )

class FileType(EnumDefinitionImpl):
    """
    Enumeration used in FileTypeRef
    """
    Snapshot = PermissibleValue(text="Snapshot")
    Transactional = PermissibleValue(text="Transactional")

    _defn = EnumDefinition(
        name="FileType",
        description="Enumeration used in FileTypeRef",
    )

class Granularity(EnumDefinitionImpl):
    """
    Enumeration used in GranularityRef
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
        description="Enumeration used in GranularityRef",
    )

class Context(EnumDefinitionImpl):
    """
    Enumeration used in ContextRef
    """
    Archive = PermissibleValue(text="Archive")
    Exchange = PermissibleValue(text="Exchange")
    Submission = PermissibleValue(text="Submission")

    _defn = EnumDefinition(
        name="Context",
        description="Enumeration used in ContextRef",
    )

class EventType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    Scheduled = PermissibleValue(text="Scheduled")
    Unscheduled = PermissibleValue(text="Unscheduled")
    Common = PermissibleValue(text="Common")

    _defn = EnumDefinition(
        name="EventType",
        description="Enumeration used in Type",
    )

class BranchingType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    Exclusive = PermissibleValue(text="Exclusive")
    Parallel = PermissibleValue(text="Parallel")

    _defn = EnumDefinition(
        name="BranchingType",
        description="Enumeration used in Type",
    )

class StudyObjectiveLevel(EnumDefinitionImpl):
    """
    Enumeration used in Level
    """
    Primary = PermissibleValue(text="Primary")
    Secondary = PermissibleValue(text="Secondary")
    Exploratory = PermissibleValue(text="Exploratory")

    _defn = EnumDefinition(
        name="StudyObjectiveLevel",
        description="Enumeration used in Level",
    )

class TrialPhaseTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TrialPhaseTypeEnum",
        code_set=NCI.ExtCodeID,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "NOT APPLICABLE",
            PermissibleValue(
                text="NOT APPLICABLE",
                meaning=NCI["ExtCodeID:C48660"]))
        setattr(cls, "PHASE 0 TRIAL",
            PermissibleValue(
                text="PHASE 0 TRIAL",
                meaning=NCI["ExtCodeID:C54721"]))
        setattr(cls, "PHASE I TRIAL",
            PermissibleValue(
                text="PHASE I TRIAL",
                meaning=NCI["ExtCodeID:C15600"]))
        setattr(cls, "PHASE I/II TRIAL",
            PermissibleValue(
                text="PHASE I/II TRIAL",
                meaning=NCI["ExtCodeID:C15693"]))
        setattr(cls, "PHASE II TRIAL",
            PermissibleValue(
                text="PHASE II TRIAL",
                meaning=NCI["ExtCodeID:C15601"]))
        setattr(cls, "PHASE II/III TRIAL",
            PermissibleValue(
                text="PHASE II/III TRIAL",
                meaning=NCI["ExtCodeID:C15694"]))
        setattr(cls, "PHASE IIA TRIAL",
            PermissibleValue(
                text="PHASE IIA TRIAL",
                meaning=NCI["ExtCodeID:C49686"]))
        setattr(cls, "PHASE IIB TRIAL",
            PermissibleValue(
                text="PHASE IIB TRIAL",
                meaning=NCI["ExtCodeID:C49688"]))
        setattr(cls, "PHASE III TRIAL",
            PermissibleValue(
                text="PHASE III TRIAL",
                meaning=NCI["ExtCodeID:C15602"]))
        setattr(cls, "PHASE IIIA TRIAL",
            PermissibleValue(
                text="PHASE IIIA TRIAL",
                meaning=NCI["ExtCodeID:C49687"]))
        setattr(cls, "PHASE IIIB TRIAL",
            PermissibleValue(
                text="PHASE IIIB TRIAL",
                meaning=NCI["ExtCodeID:C49689"]))
        setattr(cls, "PHASE IV TRIAL",
            PermissibleValue(
                text="PHASE IV TRIAL",
                meaning=NCI["ExtCodeID:C15603"]))
        setattr(cls, "PHASE V TRIAL",
            PermissibleValue(
                text="PHASE V TRIAL",
                meaning=NCI["ExtCodeID:C47865"]))

class StudyEndPointType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    Simple = PermissibleValue(text="Simple")
    Humane = PermissibleValue(text="Humane")
    Surrogate = PermissibleValue(text="Surrogate")
    Composite = PermissibleValue(text="Composite")

    _defn = EnumDefinition(
        name="StudyEndPointType",
        description="Enumeration used in Type",
    )

class StudyEstimandLevel(EnumDefinitionImpl):
    """
    Enumeration used in Level
    """
    Primary = PermissibleValue(text="Primary")
    Secondary = PermissibleValue(text="Secondary")
    Exploratory = PermissibleValue(text="Exploratory")

    _defn = EnumDefinition(
        name="StudyEstimandLevel",
        description="Enumeration used in Level",
    )

class RelativeTimingConstraintType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    StartToStart = PermissibleValue(text="StartToStart")
    StartToFinish = PermissibleValue(text="StartToFinish")
    FinishToStart = PermissibleValue(text="FinishToStart")
    FinishToFinish = PermissibleValue(text="FinishToFinish")

    _defn = EnumDefinition(
        name="RelativeTimingConstraintType",
        description="Enumeration used in Type",
    )

class Comparator(EnumDefinitionImpl):
    """
    Enumeration used in ComparatorRef
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
        description="Enumeration used in ComparatorRef",
    )

class SoftOrHard(EnumDefinitionImpl):
    """
    Enumeration used in SoftHard
    """
    Soft = PermissibleValue(text="Soft")
    Hard = PermissibleValue(text="Hard")

    _defn = EnumDefinition(
        name="SoftOrHard",
        description="Enumeration used in SoftHard",
    )

class TransactionType(EnumDefinitionImpl):
    """
    Enumeration used in TransactionTypeRef
    """
    Insert = PermissibleValue(text="Insert")
    Update = PermissibleValue(text="Update")
    Remove = PermissibleValue(text="Remove")
    Upsert = PermissibleValue(text="Upsert")
    Context = PermissibleValue(text="Context")

    _defn = EnumDefinition(
        name="TransactionType",
        description="Enumeration used in TransactionTypeRef",
    )

class UserType(EnumDefinitionImpl):
    """
    Enumeration used in UserTypeRef
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
        description="Enumeration used in UserTypeRef",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data analyst",
            PermissibleValue(text="Data analyst"))
        setattr(cls, "Care provider",
            PermissibleValue(text="Care provider"))

class OrganizationType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    Sponsor = PermissibleValue(text="Sponsor")
    Site = PermissibleValue(text="Site")
    CRO = PermissibleValue(text="CRO")
    Lab = PermissibleValue(text="Lab")
    Other = PermissibleValue(text="Other")
    TechnologyProvider = PermissibleValue(text="TechnologyProvider")

    _defn = EnumDefinition(
        name="OrganizationType",
        description="Enumeration used in Type",
    )

class TelecomTypeType(EnumDefinitionImpl):
    """
    Enumeration used in TelecomType
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
        description="Enumeration used in TelecomType",
    )

class CommentType(EnumDefinitionImpl):
    """
    Enumeration used in SponsorOrSite
    """
    Sponsor = PermissibleValue(text="Sponsor")
    Site = PermissibleValue(text="Site")

    _defn = EnumDefinition(
        name="CommentType",
        description="Enumeration used in SponsorOrSite",
    )

class SignMethod(EnumDefinitionImpl):
    """
    Enumeration used in Methodology
    """
    Digital = PermissibleValue(text="Digital")
    Electronic = PermissibleValue(text="Electronic")

    _defn = EnumDefinition(
        name="SignMethod",
        description="Enumeration used in Methodology",
    )

class EditPointType(EnumDefinitionImpl):
    """
    Enumeration used in EditPoint
    """
    Monitoring = PermissibleValue(text="Monitoring")
    DataManagement = PermissibleValue(text="DataManagement")
    DBAudit = PermissibleValue(text="DBAudit")

    _defn = EnumDefinition(
        name="EditPointType",
        description="Enumeration used in EditPoint",
    )

class YesOrNo(EnumDefinitionImpl):
    """
    Enumeration used in Repeating, UsedMethod, IsReferenceData, Mandatory
    """
    Yes = PermissibleValue(text="Yes")
    No = PermissibleValue(text="No")

    _defn = EnumDefinition(
        name="YesOrNo",
        description="Enumeration used in Repeating, UsedMethod, IsReferenceData, Mandatory",
    )

class YesOnly(EnumDefinitionImpl):
    """
    Enumeration used in Repeat, Other, IsNonStandard, ExtendedValue, HasNoData, IsNull
    """
    _defn = EnumDefinition(
        name="YesOnly",
        description="Enumeration used in Repeat, Other, IsNonStandard, ExtendedValue, HasNoData, IsNull",
    )

class MethodType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    Computation = PermissibleValue(text="Computation")
    Imputation = PermissibleValue(text="Imputation")
    Preload = PermissibleValue(text="Preload")
    Transpose = PermissibleValue(text="Transpose")

    _defn = EnumDefinition(
        name="MethodType",
        description="Enumeration used in Type",
    )

class ItemGroupRepeatingType(EnumDefinitionImpl):
    """
    Enumeration used in Repeating
    """
    No = PermissibleValue(text="No")
    Simple = PermissibleValue(text="Simple")
    Dynamic = PermissibleValue(text="Dynamic")
    Static = PermissibleValue(text="Static")

    _defn = EnumDefinition(
        name="ItemGroupRepeatingType",
        description="Enumeration used in Repeating",
    )

class ItemGroupTypeTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ItemGroupTypeTypeEnum",
    )

class QuerySourceType(EnumDefinitionImpl):
    """
    Enumeration used in Source
    """
    System = PermissibleValue(text="System")

    _defn = EnumDefinition(
        name="QuerySourceType",
        description="Enumeration used in Source",
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
    Enumeration used in Type
    """
    Manual = PermissibleValue(text="Manual")
    System = PermissibleValue(text="System")

    _defn = EnumDefinition(
        name="QueryType",
        description="Enumeration used in Type",
    )

class QueryStateType(EnumDefinitionImpl):
    """
    Enumeration used in State
    """
    Candidate = PermissibleValue(text="Candidate")
    Open = PermissibleValue(text="Open")
    Answered = PermissibleValue(text="Answered")
    Closed = PermissibleValue(text="Closed")
    Cancelled = PermissibleValue(text="Cancelled")
    Resolved = PermissibleValue(text="Resolved")

    _defn = EnumDefinition(
        name="QueryStateType",
        description="Enumeration used in State",
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
    Enumeration used in Source
    """
    Investigator = PermissibleValue(
        text="Investigator",
        meaning=NCI["ExtCodeID:C25936"])
    Sponsor = PermissibleValue(
        text="Sponsor",
        meaning=NCI["ExtCodeID:C70793"])
    Subject = PermissibleValue(
        text="Subject",
        meaning=NCI["ExtCodeID:C41189"])
    Vendor = PermissibleValue(
        text="Vendor",
        meaning=NCI["ExtCodeID:C68608"])

    _defn = EnumDefinition(
        name="OriginSource",
        description="Enumeration used in Source",
    )

class OriginType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    Assigned = PermissibleValue(
        text="Assigned",
        meaning=NCI["ExtCodeID:C170547"])
    Collected = PermissibleValue(
        text="Collected",
        meaning=NCI["ExtCodeID:C170548"])
    Derived = PermissibleValue(
        text="Derived",
        meaning=NCI["ExtCodeID:C170549"])
    EHR = PermissibleValue(text="EHR")
    Other = PermissibleValue(
        text="Other",
        meaning=NCI["ExtCodeID:C17649"])
    Predecessor = PermissibleValue(
        text="Predecessor",
        meaning=NCI["ExtCodeID:C170550"])
    Protocol = PermissibleValue(
        text="Protocol",
        meaning=NCI["ExtCodeID:C170551"])

    _defn = EnumDefinition(
        name="OriginType",
        description="Enumeration used in Type",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Available",
            PermissibleValue(
                text="Not Available",
                meaning=NCI["ExtCodeID:C126101"]))

class PDFPageType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    NamedDestination = PermissibleValue(text="NamedDestination")
    PhysicalRef = PermissibleValue(text="PhysicalRef")

    _defn = EnumDefinition(
        name="PDFPageType",
        description="Enumeration used in Type",
    )

class StandardName(EnumDefinitionImpl):
    """
    Enumeration used in Name
    """
    ADaMIG = PermissibleValue(
        text="ADaMIG",
        meaning=NCI["ExtCodeID:C170552"])
    SDTMIG = PermissibleValue(
        text="SDTMIG",
        meaning=NCI["ExtCodeID:C170455"])
    SENDIG = PermissibleValue(
        text="SENDIG",
        meaning=NCI["ExtCodeID:C170456"])

    _defn = EnumDefinition(
        name="StandardName",
        description="Enumeration used in Name",
        code_set=NCI.ExtCodeID,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CDISC/NCI",
            PermissibleValue(
                text="CDISC/NCI",
                meaning=NCI["ExtCodeID:C163415"]))
        setattr(cls, "SDTMIG-AP",
            PermissibleValue(
                text="SDTMIG-AP",
                meaning=NCI["ExtCodeID:C170553"]))
        setattr(cls, "SDTMIG-MD",
            PermissibleValue(
                text="SDTMIG-MD",
                meaning=NCI["ExtCodeID:C170554"]))
        setattr(cls, "SENDIG-AR",
            PermissibleValue(
                text="SENDIG-AR",
                meaning=NCI["ExtCodeID:C181230"]))
        setattr(cls, "SENDIG-DART",
            PermissibleValue(
                text="SENDIG-DART",
                meaning=NCI["ExtCodeID:C170556"]))

class StandardPublishingSet(EnumDefinitionImpl):
    """
    Enumeration used in PublishingSet
    """
    ADaM = PermissibleValue(
        text="ADaM",
        meaning=NCI["ExtCodeID:C180548"])
    CDASH = PermissibleValue(
        text="CDASH",
        meaning=NCI["ExtCodeID:C180549"])
    SDTM = PermissibleValue(
        text="SDTM",
        meaning=NCI["ExtCodeID:C180551"])
    SEND = PermissibleValue(
        text="SEND",
        meaning=NCI["ExtCodeID:C180552"])

    _defn = EnumDefinition(
        name="StandardPublishingSet",
        description="Enumeration used in PublishingSet",
        code_set=NCI.ExtCodeID,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DEFINE-XML",
            PermissibleValue(
                text="DEFINE-XML",
                meaning=NCI["ExtCodeID:C180550"]))

class StandardStatusEnum(EnumDefinitionImpl):

    Draft = PermissibleValue(
        text="Draft",
        meaning=NCI["ExtCodeID:C172453"])
    Final = PermissibleValue(
        text="Final",
        meaning=NCI["ExtCodeID:C172455"])
    Provisional = PermissibleValue(
        text="Provisional",
        meaning=NCI["ExtCodeID:C172454"])

    _defn = EnumDefinition(
        name="StandardStatusEnum",
        code_set=NCI.ExtCodeID,
    )

class StandardType(EnumDefinitionImpl):
    """
    Enumeration used in Type
    """
    CT = PermissibleValue(
        text="CT",
        meaning=NCI["ExtCodeID:C163415"])
    IG = PermissibleValue(
        text="IG",
        meaning=NCI["ExtCodeID:C170454"])

    _defn = EnumDefinition(
        name="StandardType",
        description="Enumeration used in Type",
        code_set=NCI.ExtCodeID,
    )

class DictionaryNameTypeEnum(EnumDefinitionImpl):

    COSTART = PermissibleValue(
        text="COSTART",
        meaning=NCI["ExtCodeID:C49471"])
    CTCAE = PermissibleValue(
        text="CTCAE",
        meaning=NCI["ExtCodeID:C49704"])
    ICD = PermissibleValue(
        text="ICD",
        meaning=NCI["ExtCodeID:C49474"])
    LOINC = PermissibleValue(
        text="LOINC",
        meaning=NCI["ExtCodeID:C49476"])
    MedDRA = PermissibleValue(
        text="MedDRA",
        meaning=NCI["ExtCodeID:C43820"])
    SNOMED = PermissibleValue(
        text="SNOMED",
        meaning=NCI["ExtCodeID:C53489"])
    UNII = PermissibleValue(
        text="UNII",
        meaning=NCI["ExtCodeID:C163417"])
    WHOART = PermissibleValue(
        text="WHOART",
        meaning=NCI["ExtCodeID:C49468"])
    WHODD = PermissibleValue(
        text="WHODD",
        meaning=NCI["ExtCodeID:C49475"])

    _defn = EnumDefinition(
        name="DictionaryNameTypeEnum",
        code_set=NCI.ExtCodeID,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CDISC CT",
            PermissibleValue(
                text="CDISC CT",
                meaning=NCI["ExtCodeID:C163415"]))
        setattr(cls, "D-U-N-S NUMBER",
            PermissibleValue(
                text="D-U-N-S NUMBER",
                meaning=NCI["ExtCodeID:C134003"]))
        setattr(cls, "MED-RT",
            PermissibleValue(
                text="MED-RT",
                meaning=NCI["ExtCodeID:C163416"]))
        setattr(cls, "WHO ATC CLASSIFICATION SYSTEM",
            PermissibleValue(
                text="WHO ATC CLASSIFICATION SYSTEM",
                meaning=NCI["ExtCodeID:C154331"]))

class ItemGroupClass(EnumDefinitionImpl):
    """
    Enumeration used in Name
    """
    EVENTS = PermissibleValue(
        text="EVENTS",
        meaning=NCI["ExtCodeID:C103372"])
    FINDINGS = PermissibleValue(
        text="FINDINGS",
        meaning=NCI["ExtCodeID:C103373"])
    INTERVENTIONS = PermissibleValue(
        text="INTERVENTIONS",
        meaning=NCI["ExtCodeID:C103374"])
    RELATIONSHIP = PermissibleValue(
        text="RELATIONSHIP",
        meaning=NCI["ExtCodeID:C103376"])

    _defn = EnumDefinition(
        name="ItemGroupClass",
        description="Enumeration used in Name",
        code_set=NCI.ExtCodeID,
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ADAM OTHER",
            PermissibleValue(
                text="ADAM OTHER",
                meaning=NCI["ExtCodeID:C103375"]))
        setattr(cls, "BASIC DATA STRUCTURE",
            PermissibleValue(
                text="BASIC DATA STRUCTURE",
                meaning=NCI["ExtCodeID:C103371"]))
        setattr(cls, "DEVICE LEVEL ANALYSIS DATASET",
            PermissibleValue(
                text="DEVICE LEVEL ANALYSIS DATASET",
                meaning=NCI["ExtCodeID:C177921"]))
        setattr(cls, "FINDINGS ABOUT",
            PermissibleValue(
                text="FINDINGS ABOUT",
                meaning=NCI["ExtCodeID:C135396"]))
        setattr(cls, "MEDICAL DEVICE BASIC DATA STRUCTURE",
            PermissibleValue(
                text="MEDICAL DEVICE BASIC DATA STRUCTURE",
                meaning=NCI["ExtCodeID:C177922"]))
        setattr(cls, "MEDICAL DEVICE OCCURRENCE DATA STRUCTURE",
            PermissibleValue(
                text="MEDICAL DEVICE OCCURRENCE DATA STRUCTURE",
                meaning=NCI["ExtCodeID:C177923"]))
        setattr(cls, "OCCURRENCE DATA STRUCTURE",
            PermissibleValue(
                text="OCCURRENCE DATA STRUCTURE",
                meaning=NCI["ExtCodeID:C123454"]))
        setattr(cls, "SPECIAL PURPOSE",
            PermissibleValue(
                text="SPECIAL PURPOSE",
                meaning=NCI["ExtCodeID:C103377"]))
        setattr(cls, "STUDY REFERENCE",
            PermissibleValue(
                text="STUDY REFERENCE",
                meaning=NCI["ExtCodeID:C147271"]))
        setattr(cls, "SUBJECT LEVEL ANALYSIS DATASET",
            PermissibleValue(
                text="SUBJECT LEVEL ANALYSIS DATASET",
                meaning=NCI["ExtCodeID:C103378"]))
        setattr(cls, "TRIAL DESIGN",
            PermissibleValue(
                text="TRIAL DESIGN",
                meaning=NCI["ExtCodeID:C103379"]))

class ItemGroupSubClass(EnumDefinitionImpl):
    """
    Enumeration used in Name
    """
    _defn = EnumDefinition(
        name="ItemGroupSubClass",
        description="Enumeration used in Name",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ADVERSE EVENT",
            PermissibleValue(
                text="ADVERSE EVENT",
                meaning=NCI["ExtCodeID:C176265"]))
        setattr(cls, "MEDICAL DEVICE TIME-TO-EVENT",
            PermissibleValue(
                text="MEDICAL DEVICE TIME-TO-EVENT",
                meaning=NCI["ExtCodeID:C177920"]))
        setattr(cls, "NON-COMPARTMENTAL ANALYSIS",
            PermissibleValue(
                text="NON-COMPARTMENTAL ANALYSIS",
                meaning=NCI["ExtCodeID:C172452"]))
        setattr(cls, "TIME-TO-EVENT",
            PermissibleValue(
                text="TIME-TO-EVENT",
                meaning=NCI["ExtCodeID:C165637"]))

# Slots
class slots:
    pass

slots.StudyEndPointOID = Slot(uri=ODM.StudyEndPointOID, name="StudyEndPointOID", curie=ODM.curie('StudyEndPointOID'),
                   model_uri=ODM.StudyEndPointOID, domain=None, range=Optional[str])

slots.TimepointRelativeTarget = Slot(uri=ODM.TimepointRelativeTarget, name="TimepointRelativeTarget", curie=ODM.curie('TimepointRelativeTarget'),
                   model_uri=ODM.TimepointRelativeTarget, domain=None, range=Optional[str])

slots.LeafID = Slot(uri=ODM.LeafID, name="LeafID", curie=ODM.curie('LeafID'),
                   model_uri=ODM.LeafID, domain=None, range=Optional[str])

slots.UserOID = Slot(uri=ODM.UserOID, name="UserOID", curie=ODM.curie('UserOID'),
                   model_uri=ODM.UserOID, domain=None, range=Optional[str])

slots.VersionName = Slot(uri=ODM.VersionName, name="VersionName", curie=ODM.curie('VersionName'),
                   model_uri=ODM.VersionName, domain=None, range=Optional[str])

slots.ArmOID = Slot(uri=ODM.ArmOID, name="ArmOID", curie=ODM.curie('ArmOID'),
                   model_uri=ODM.ArmOID, domain=None, range=Optional[str])

slots.EpochOID = Slot(uri=ODM.EpochOID, name="EpochOID", curie=ODM.curie('EpochOID'),
                   model_uri=ODM.EpochOID, domain=None, range=Optional[str])

slots.MethodOID = Slot(uri=ODM.MethodOID, name="MethodOID", curie=ODM.curie('MethodOID'),
                   model_uri=ODM.MethodOID, domain=None, range=Optional[str])

slots.IsNull = Slot(uri=ODM.IsNull, name="IsNull", curie=ODM.curie('IsNull'),
                   model_uri=ODM.IsNull, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.KeySequence = Slot(uri=ODM.KeySequence, name="KeySequence", curie=ODM.curie('KeySequence'),
                   model_uri=ODM.KeySequence, domain=None, range=Optional[int])

slots.GranularityRef = Slot(uri=ODM.GranularityRef, name="GranularityRef", curie=ODM.curie('GranularityRef'),
                   model_uri=ODM.GranularityRef, domain=None, range=Optional[Union[str, "Granularity"]])

slots.TransitionOID = Slot(uri=ODM.TransitionOID, name="TransitionOID", curie=ODM.curie('TransitionOID'),
                   model_uri=ODM.TransitionOID, domain=None, range=Optional[str])

slots.ComparatorRef = Slot(uri=ODM.ComparatorRef, name="ComparatorRef", curie=ODM.curie('ComparatorRef'),
                   model_uri=ODM.ComparatorRef, domain=None, range=Optional[Union[str, "Comparator"]])

slots.DurationPostWindow = Slot(uri=ODM.DurationPostWindow, name="DurationPostWindow", curie=ODM.curie('DurationPostWindow'),
                   model_uri=ODM.DurationPostWindow, domain=None, range=Optional[str])

slots.leafID = Slot(uri=ODM.leafID, name="leafID", curie=ODM.curie('leafID'),
                   model_uri=ODM.leafID, domain=None, range=URIRef)

slots.StartConditionOID = Slot(uri=ODM.StartConditionOID, name="StartConditionOID", curie=ODM.curie('StartConditionOID'),
                   model_uri=ODM.StartConditionOID, domain=None, range=Optional[str])

slots.FirstPage = Slot(uri=ODM.FirstPage, name="FirstPage", curie=ODM.curie('FirstPage'),
                   model_uri=ODM.FirstPage, domain=None, range=Optional[int])

slots.SponsorOrSite = Slot(uri=ODM.SponsorOrSite, name="SponsorOrSite", curie=ODM.curie('SponsorOrSite'),
                   model_uri=ODM.SponsorOrSite, domain=None, range=Optional[Union[str, "CommentType"]])

slots._language = Slot(uri=ODM._language, name="_language", curie=ODM.curie('_language'),
                   model_uri=ODM._language, domain=None, range=Optional[str])

slots.Level = Slot(uri=ODM.Level, name="Level", curie=ODM.curie('Level'),
                   model_uri=ODM.Level, domain=None, range=Optional[str])

slots.PublishingSet = Slot(uri=ODM.PublishingSet, name="PublishingSet", curie=ODM.curie('PublishingSet'),
                   model_uri=ODM.PublishingSet, domain=None, range=Optional[Union[str, "StandardPublishingSet"]])

slots.UsedMethod = Slot(uri=ODM.UsedMethod, name="UsedMethod", curie=ODM.curie('UsedMethod'),
                   model_uri=ODM.UsedMethod, domain=None, range=Optional[Union[str, "YesOrNo"]])

slots.Dictionary = Slot(uri=ODM.Dictionary, name="Dictionary", curie=ODM.curie('Dictionary'),
                   model_uri=ODM.Dictionary, domain=None, range=Optional[str])

slots.StudyEventGroupOID = Slot(uri=ODM.StudyEventGroupOID, name="StudyEventGroupOID", curie=ODM.curie('StudyEventGroupOID'),
                   model_uri=ODM.StudyEventGroupOID, domain=None, range=Optional[str])

slots.CodeListOID = Slot(uri=ODM.CodeListOID, name="CodeListOID", curie=ODM.curie('CodeListOID'),
                   model_uri=ODM.CodeListOID, domain=None, range=Optional[str])

slots.TargetTransitionOID = Slot(uri=ODM.TargetTransitionOID, name="TargetTransitionOID", curie=ODM.curie('TargetTransitionOID'),
                   model_uri=ODM.TargetTransitionOID, domain=None, range=Optional[str])

slots.StudyTargetPopulationOID = Slot(uri=ODM.StudyTargetPopulationOID, name="StudyTargetPopulationOID", curie=ODM.curie('StudyTargetPopulationOID'),
                   model_uri=ODM.StudyTargetPopulationOID, domain=None, range=Optional[str])

slots.HasNoData = Slot(uri=ODM.HasNoData, name="HasNoData", curie=ODM.curie('HasNoData'),
                   model_uri=ODM.HasNoData, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.PriorFileOID = Slot(uri=ODM.PriorFileOID, name="PriorFileOID", curie=ODM.curie('PriorFileOID'),
                   model_uri=ODM.PriorFileOID, domain=None, range=Optional[str])

slots.EditPoint = Slot(uri=ODM.EditPoint, name="EditPoint", curie=ODM.curie('EditPoint'),
                   model_uri=ODM.EditPoint, domain=None, range=Optional[Union[str, "EditPointType"]])

slots.Type = Slot(uri=ODM.Type, name="Type", curie=ODM.curie('Type'),
                   model_uri=ODM.Type, domain=None, range=Optional[str])

slots.CodeRef = Slot(uri=ODM.CodeRef, name="CodeRef", curie=ODM.curie('CodeRef'),
                   model_uri=ODM.CodeRef, domain=None, range=Optional[Union[dict, Code]])

slots.Core = Slot(uri=ODM.Core, name="Core", curie=ODM.curie('Core'),
                   model_uri=ODM.Core, domain=None, range=Optional[str])

slots.StudyInterventionOID = Slot(uri=ODM.StudyInterventionOID, name="StudyInterventionOID", curie=ODM.curie('StudyInterventionOID'),
                   model_uri=ODM.StudyInterventionOID, domain=None, range=Optional[str])

slots.IsNonStandard = Slot(uri=ODM.IsNonStandard, name="IsNonStandard", curie=ODM.curie('IsNonStandard'),
                   model_uri=ODM.IsNonStandard, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.Library = Slot(uri=ODM.Library, name="Library", curie=ODM.curie('Library'),
                   model_uri=ODM.Library, domain=None, range=Optional[str])

slots.IsReferenceData = Slot(uri=ODM.IsReferenceData, name="IsReferenceData", curie=ODM.curie('IsReferenceData'),
                   model_uri=ODM.IsReferenceData, domain=None, range=Optional[Union[str, "YesOrNo"]])

slots.RepeatingLimit = Slot(uri=ODM.RepeatingLimit, name="RepeatingLimit", curie=ODM.curie('RepeatingLimit'),
                   model_uri=ODM.RepeatingLimit, domain=None, range=Optional[int])

slots.DataTypeRef = Slot(uri=ODM.DataTypeRef, name="DataTypeRef", curie=ODM.curie('DataTypeRef'),
                   model_uri=ODM.DataTypeRef, domain=None, range=Optional[str])

slots.ImageFileName = Slot(uri=ODM.ImageFileName, name="ImageFileName", curie=ODM.curie('ImageFileName'),
                   model_uri=ODM.ImageFileName, domain=None, range=Optional[URIorCURIE])

slots.Source = Slot(uri=ODM.Source, name="Source", curie=ODM.curie('Source'),
                   model_uri=ODM.Source, domain=None, range=Optional[str])

slots.MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.MetaDataVersionOID, domain=None, range=Optional[str])

slots.ShortName = Slot(uri=ODM.ShortName, name="ShortName", curie=ODM.curie('ShortName'),
                   model_uri=ODM.ShortName, domain=None, range=Optional[str])

slots.ItemGroupOID = Slot(uri=ODM.ItemGroupOID, name="ItemGroupOID", curie=ODM.curie('ItemGroupOID'),
                   model_uri=ODM.ItemGroupOID, domain=None, range=Optional[str])

slots.Status = Slot(uri=ODM.Status, name="Status", curie=ODM.curie('Status'),
                   model_uri=ODM.Status, domain=None, range=Optional[str])

slots.SourceOID = Slot(uri=ODM.SourceOID, name="SourceOID", curie=ODM.curie('SourceOID'),
                   model_uri=ODM.SourceOID, domain=None, range=Optional[str])

slots.ConditionOID = Slot(uri=ODM.ConditionOID, name="ConditionOID", curie=ODM.curie('ConditionOID'),
                   model_uri=ODM.ConditionOID, domain=None, range=Optional[str])

slots.ValueRef = Slot(uri=ODM.ValueRef, name="ValueRef", curie=ODM.curie('ValueRef'),
                   model_uri=ODM.ValueRef, domain=None, range=Optional[Union[dict, Value]])

slots.VersionID = Slot(uri=ODM.VersionID, name="VersionID", curie=ODM.curie('VersionID'),
                   model_uri=ODM.VersionID, domain=None, range=Optional[str])

slots.DefinitionRef = Slot(uri=ODM.DefinitionRef, name="DefinitionRef", curie=ODM.curie('DefinitionRef'),
                   model_uri=ODM.DefinitionRef, domain=None, range=Optional[Union[dict, Definition]])

slots.State = Slot(uri=ODM.State, name="State", curie=ODM.curie('State'),
                   model_uri=ODM.State, domain=None, range=Optional[Union[str, "QueryStateType"]])

slots.TitleRef = Slot(uri=ODM.TitleRef, name="TitleRef", curie=ODM.curie('TitleRef'),
                   model_uri=ODM.TitleRef, domain=None, range=Optional[Union[dict, Title]])

slots.Attribute = Slot(uri=ODM.Attribute, name="Attribute", curie=ODM.curie('Attribute'),
                   model_uri=ODM.Attribute, domain=None, range=Optional[str])

slots.WhereClauseOID = Slot(uri=ODM.WhereClauseOID, name="WhereClauseOID", curie=ODM.curie('WhereClauseOID'),
                   model_uri=ODM.WhereClauseOID, domain=None, range=Optional[str])

slots.ArchiveLocationID = Slot(uri=ODM.ArchiveLocationID, name="ArchiveLocationID", curie=ODM.curie('ArchiveLocationID'),
                   model_uri=ODM.ArchiveLocationID, domain=None, range=Optional[str])

slots.VariableSet = Slot(uri=ODM.VariableSet, name="VariableSet", curie=ODM.curie('VariableSet'),
                   model_uri=ODM.VariableSet, domain=None, range=Optional[str])

slots.UserTypeRef = Slot(uri=ODM.UserTypeRef, name="UserTypeRef", curie=ODM.curie('UserTypeRef'),
                   model_uri=ODM.UserTypeRef, domain=None, range=Optional[Union[str, "UserType"]])

slots.SystemVersion = Slot(uri=ODM.SystemVersion, name="SystemVersion", curie=ODM.curie('SystemVersion'),
                   model_uri=ODM.SystemVersion, domain=None, range=Optional[str])

slots.DisplayFormat = Slot(uri=ODM.DisplayFormat, name="DisplayFormat", curie=ODM.curie('DisplayFormat'),
                   model_uri=ODM.DisplayFormat, domain=None, range=Optional[str])

slots.Originator = Slot(uri=ODM.Originator, name="Originator", curie=ODM.curie('Originator'),
                   model_uri=ODM.Originator, domain=None, range=Optional[str])

slots.ParentClass = Slot(uri=ODM.ParentClass, name="ParentClass", curie=ODM.curie('ParentClass'),
                   model_uri=ODM.ParentClass, domain=None, range=Optional[str])

slots.TimepointTarget = Slot(uri=ODM.TimepointTarget, name="TimepointTarget", curie=ODM.curie('TimepointTarget'),
                   model_uri=ODM.TimepointTarget, domain=None, range=Optional[str])

slots.ItemGroupRepeatKey = Slot(uri=ODM.ItemGroupRepeatKey, name="ItemGroupRepeatKey", curie=ODM.curie('ItemGroupRepeatKey'),
                   model_uri=ODM.ItemGroupRepeatKey, domain=None, range=Optional[str])

slots.PredecessorOID = Slot(uri=ODM.PredecessorOID, name="PredecessorOID", curie=ODM.curie('PredecessorOID'),
                   model_uri=ODM.PredecessorOID, domain=None, range=Optional[str])

slots.CollectionExceptionConditionOID = Slot(uri=ODM.CollectionExceptionConditionOID, name="CollectionExceptionConditionOID", curie=ODM.curie('CollectionExceptionConditionOID'),
                   model_uri=ODM.CollectionExceptionConditionOID, domain=None, range=Optional[str])

slots.SeqNum = Slot(uri=ODM.SeqNum, name="SeqNum", curie=ODM.curie('SeqNum'),
                   model_uri=ODM.SeqNum, domain=None, range=Optional[int])

slots.TransactionTypeRef = Slot(uri=ODM.TransactionTypeRef, name="TransactionTypeRef", curie=ODM.curie('TransactionTypeRef'),
                   model_uri=ODM.TransactionTypeRef, domain=None, range=Optional[Union[str, "TransactionType"]])

slots.TimepointPreWindow = Slot(uri=ODM.TimepointPreWindow, name="TimepointPreWindow", curie=ODM.curie('TimepointPreWindow'),
                   model_uri=ODM.TimepointPreWindow, domain=None, range=Optional[str])

slots.PartOfOrganizationOID = Slot(uri=ODM.PartOfOrganizationOID, name="PartOfOrganizationOID", curie=ODM.curie('PartOfOrganizationOID'),
                   model_uri=ODM.PartOfOrganizationOID, domain=None, range=Optional[str])

slots.PreSpecifiedValue = Slot(uri=ODM.PreSpecifiedValue, name="PreSpecifiedValue", curie=ODM.curie('PreSpecifiedValue'),
                   model_uri=ODM.PreSpecifiedValue, domain=None, range=Optional[str])

slots.OID = Slot(uri=ODM.OID, name="OID", curie=ODM.curie('OID'),
                   model_uri=ODM.OID, domain=None, range=URIRef)

slots.SequenceNumber = Slot(uri=ODM.SequenceNumber, name="SequenceNumber", curie=ODM.curie('SequenceNumber'),
                   model_uri=ODM.SequenceNumber, domain=None, range=Optional[int])

slots.MimeType = Slot(uri=ODM.MimeType, name="MimeType", curie=ODM.curie('MimeType'),
                   model_uri=ODM.MimeType, domain=None, range=Optional[str])

slots.Method = Slot(uri=ODM.Method, name="Method", curie=ODM.curie('Method'),
                   model_uri=ODM.Method, domain=None, range=Optional[str])

slots.SubjectKey = Slot(uri=ODM.SubjectKey, name="SubjectKey", curie=ODM.curie('SubjectKey'),
                   model_uri=ODM.SubjectKey, domain=None, range=Optional[str])

slots.CommentOID = Slot(uri=ODM.CommentOID, name="CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.CommentOID, domain=None, range=Optional[str])

slots.ItemGroupDataSeq = Slot(uri=ODM.ItemGroupDataSeq, name="ItemGroupDataSeq", curie=ODM.curie('ItemGroupDataSeq'),
                   model_uri=ODM.ItemGroupDataSeq, domain=None, range=Optional[int])

slots.ID = Slot(uri=ODM.ID, name="ID", curie=ODM.curie('ID'),
                   model_uri=ODM.ID, domain=None, range=URIRef)

slots.Other = Slot(uri=ODM.Other, name="Other", curie=ODM.curie('Other'),
                   model_uri=ODM.Other, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.Term = Slot(uri=ODM.Term, name="Term", curie=ODM.curie('Term'),
                   model_uri=ODM.Term, domain=None, range=Optional[str])

slots.Target = Slot(uri=ODM.Target, name="Target", curie=ODM.curie('Target'),
                   model_uri=ODM.Target, domain=None, range=Optional[str])

slots.StandardOID = Slot(uri=ODM.StandardOID, name="StandardOID", curie=ODM.curie('StandardOID'),
                   model_uri=ODM.StandardOID, domain=None, range=Optional[str])

slots.EndOID = Slot(uri=ODM.EndOID, name="EndOID", curie=ODM.curie('EndOID'),
                   model_uri=ODM.EndOID, domain=None, range=Optional[str])

slots.SourceSystemVersion = Slot(uri=ODM.SourceSystemVersion, name="SourceSystemVersion", curie=ODM.curie('SourceSystemVersion'),
                   model_uri=ODM.SourceSystemVersion, domain=None, range=Optional[str])

slots.Repeating = Slot(uri=ODM.Repeating, name="Repeating", curie=ODM.curie('Repeating'),
                   model_uri=ODM.Repeating, domain=None, range=Optional[str])

slots.WorkflowOID = Slot(uri=ODM.WorkflowOID, name="WorkflowOID", curie=ODM.curie('WorkflowOID'),
                   model_uri=ODM.WorkflowOID, domain=None, range=Optional[str])

slots.Mandatory = Slot(uri=ODM.Mandatory, name="Mandatory", curie=ODM.curie('Mandatory'),
                   model_uri=ODM.Mandatory, domain=None, range=Optional[Union[str, "YesOrNo"]])

slots.Name = Slot(uri=ODM.Name, name="Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Name, domain=None, range=Optional[str])

slots.RoleCodeListOID = Slot(uri=ODM.RoleCodeListOID, name="RoleCodeListOID", curie=ODM.curie('RoleCodeListOID'),
                   model_uri=ODM.RoleCodeListOID, domain=None, range=Optional[str])

slots.Version = Slot(uri=ODM.Version, name="Version", curie=ODM.curie('Version'),
                   model_uri=ODM.Version, domain=None, range=Optional[str])

slots.SoftHard = Slot(uri=ODM.SoftHard, name="SoftHard", curie=ODM.curie('SoftHard'),
                   model_uri=ODM.SoftHard, domain=None, range=Optional[Union[str, "SoftOrHard"]])

slots.CodedValue = Slot(uri=ODM.CodedValue, name="CodedValue", curie=ODM.curie('CodedValue'),
                   model_uri=ODM.CodedValue, domain=None, range=Optional[str])

slots.Label = Slot(uri=ODM.Label, name="Label", curie=ODM.curie('Label'),
                   model_uri=ODM.Label, domain=None, range=Optional[str])

slots.Role = Slot(uri=ODM.Role, name="Role", curie=ODM.curie('Role'),
                   model_uri=ODM.Role, domain=None, range=Optional[str])

slots.TelecomType = Slot(uri=ODM.TelecomType, name="TelecomType", curie=ODM.curie('TelecomType'),
                   model_uri=ODM.TelecomType, domain=None, range=Optional[Union[str, "TelecomTypeType"]])

slots.DurationTarget = Slot(uri=ODM.DurationTarget, name="DurationTarget", curie=ODM.curie('DurationTarget'),
                   model_uri=ODM.DurationTarget, domain=None, range=Optional[str])

slots.ProtocolName = Slot(uri=ODM.ProtocolName, name="ProtocolName", curie=ODM.curie('ProtocolName'),
                   model_uri=ODM.ProtocolName, domain=None, range=Optional[str])

slots.StudyOID = Slot(uri=ODM.StudyOID, name="StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.StudyOID, domain=None, range=Optional[str])

slots.Length = Slot(uri=ODM.Length, name="Length", curie=ODM.curie('Length'),
                   model_uri=ODM.Length, domain=None, range=Optional[int])

slots.Rank = Slot(uri=ODM.Rank, name="Rank", curie=ODM.curie('Rank'),
                   model_uri=ODM.Rank, domain=None, range=Optional[Decimal])

slots.FileTypeRef = Slot(uri=ODM.FileTypeRef, name="FileTypeRef", curie=ODM.curie('FileTypeRef'),
                   model_uri=ODM.FileTypeRef, domain=None, range=Optional[Union[str, "FileType"]])

slots.Methodology = Slot(uri=ODM.Methodology, name="Methodology", curie=ODM.curie('Methodology'),
                   model_uri=ODM.Methodology, domain=None, range=Optional[Union[str, "SignMethod"]])

slots.SourceSystem = Slot(uri=ODM.SourceSystem, name="SourceSystem", curie=ODM.curie('SourceSystem'),
                   model_uri=ODM.SourceSystem, domain=None, range=Optional[str])

slots.EndConditionOID = Slot(uri=ODM.EndConditionOID, name="EndConditionOID", curie=ODM.curie('EndConditionOID'),
                   model_uri=ODM.EndConditionOID, domain=None, range=Optional[str])

slots.StartOID = Slot(uri=ODM.StartOID, name="StartOID", curie=ODM.curie('StartOID'),
                   model_uri=ODM.StartOID, domain=None, range=Optional[str])

slots.SuccessorOID = Slot(uri=ODM.SuccessorOID, name="SuccessorOID", curie=ODM.curie('SuccessorOID'),
                   model_uri=ODM.SuccessorOID, domain=None, range=Optional[str])

slots.ref = Slot(uri=ODM.ref, name="ref", curie=ODM.curie('ref'),
                   model_uri=ODM.ref, domain=None, range=Optional[str])

slots.ODMVersionRef = Slot(uri=ODM.ODMVersionRef, name="ODMVersionRef", curie=ODM.curie('ODMVersionRef'),
                   model_uri=ODM.ODMVersionRef, domain=None, range=Optional[str])

slots.ContextRef = Slot(uri=ODM.ContextRef, name="ContextRef", curie=ODM.curie('ContextRef'),
                   model_uri=ODM.ContextRef, domain=None, range=Optional[str])

slots.Longitude = Slot(uri=ODM.Longitude, name="Longitude", curie=ODM.curie('Longitude'),
                   model_uri=ODM.Longitude, domain=None, range=Optional[Decimal])

slots.LocationOID = Slot(uri=ODM.LocationOID, name="LocationOID", curie=ODM.curie('LocationOID'),
                   model_uri=ODM.LocationOID, domain=None, range=Optional[str])

slots.StudyName = Slot(uri=ODM.StudyName, name="StudyName", curie=ODM.curie('StudyName'),
                   model_uri=ODM.StudyName, domain=None, range=Optional[str])

slots.Repeat = Slot(uri=ODM.Repeat, name="Repeat", curie=ODM.curie('Repeat'),
                   model_uri=ODM.Repeat, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.Altitude = Slot(uri=ODM.Altitude, name="Altitude", curie=ODM.curie('Altitude'),
                   model_uri=ODM.Altitude, domain=None, range=Optional[Decimal])

slots.ExtendedValue = Slot(uri=ODM.ExtendedValue, name="ExtendedValue", curie=ODM.curie('ExtendedValue'),
                   model_uri=ODM.ExtendedValue, domain=None, range=Optional[Union[str, "YesOnly"]])

slots.AsOfDateTime = Slot(uri=ODM.AsOfDateTime, name="AsOfDateTime", curie=ODM.curie('AsOfDateTime'),
                   model_uri=ODM.AsOfDateTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.EffectiveDate = Slot(uri=ODM.EffectiveDate, name="EffectiveDate", curie=ODM.curie('EffectiveDate'),
                   model_uri=ODM.EffectiveDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.TimepointPostWindow = Slot(uri=ODM.TimepointPostWindow, name="TimepointPostWindow", curie=ODM.curie('TimepointPostWindow'),
                   model_uri=ODM.TimepointPostWindow, domain=None, range=Optional[str])

slots.StructuralElementOID = Slot(uri=ODM.StructuralElementOID, name="StructuralElementOID", curie=ODM.curie('StructuralElementOID'),
                   model_uri=ODM.StructuralElementOID, domain=None, range=Optional[str])

slots.ValueListOID = Slot(uri=ODM.ValueListOID, name="ValueListOID", curie=ODM.curie('ValueListOID'),
                   model_uri=ODM.ValueListOID, domain=None, range=Optional[str])

slots.LastUpdateDatetime = Slot(uri=ODM.LastUpdateDatetime, name="LastUpdateDatetime", curie=ODM.curie('LastUpdateDatetime'),
                   model_uri=ODM.LastUpdateDatetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.StudyEventOID = Slot(uri=ODM.StudyEventOID, name="StudyEventOID", curie=ODM.curie('StudyEventOID'),
                   model_uri=ODM.StudyEventOID, domain=None, range=Optional[str])

slots.ItemOID = Slot(uri=ODM.ItemOID, name="ItemOID", curie=ODM.curie('ItemOID'),
                   model_uri=ODM.ItemOID, domain=None, range=Optional[str])

slots.Category = Slot(uri=ODM.Category, name="Category", curie=ODM.curie('Category'),
                   model_uri=ODM.Category, domain=None, range=Optional[str])

slots.Domain = Slot(uri=ODM.Domain, name="Domain", curie=ODM.curie('Domain'),
                   model_uri=ODM.Domain, domain=None, range=Optional[str])

slots.Path = Slot(uri=ODM.Path, name="Path", curie=ODM.curie('Path'),
                   model_uri=ODM.Path, domain=None, range=Optional[str])

slots.SignatureOID = Slot(uri=ODM.SignatureOID, name="SignatureOID", curie=ODM.curie('SignatureOID'),
                   model_uri=ODM.SignatureOID, domain=None, range=Optional[str])

slots.OrderNumber = Slot(uri=ODM.OrderNumber, name="OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.OrderNumber, domain=None, range=Optional[int])

slots.System = Slot(uri=ODM.System, name="System", curie=ODM.curie('System'),
                   model_uri=ODM.System, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.TargetOID = Slot(uri=ODM.TargetOID, name="TargetOID", curie=ODM.curie('TargetOID'),
                   model_uri=ODM.TargetOID, domain=None, range=Optional[str])

slots.Structure = Slot(uri=ODM.Structure, name="Structure", curie=ODM.curie('Structure'),
                   model_uri=ODM.Structure, domain=None, range=Optional[str])

slots.LastPage = Slot(uri=ODM.LastPage, name="LastPage", curie=ODM.curie('LastPage'),
                   model_uri=ODM.LastPage, domain=None, range=Optional[int])

slots.SystemName = Slot(uri=ODM.SystemName, name="SystemName", curie=ODM.curie('SystemName'),
                   model_uri=ODM.SystemName, domain=None, range=Optional[str])

slots.href = Slot(uri=ODM.href, name="href", curie=ODM.curie('href'),
                   model_uri=ODM.href, domain=None, range=Optional[str])

slots.UnitsItemOID = Slot(uri=ODM.UnitsItemOID, name="UnitsItemOID", curie=ODM.curie('UnitsItemOID'),
                   model_uri=ODM.UnitsItemOID, domain=None, range=Optional[str])

slots.DatasetName = Slot(uri=ODM.DatasetName, name="DatasetName", curie=ODM.curie('DatasetName'),
                   model_uri=ODM.DatasetName, domain=None, range=Optional[str])

slots.PageRefs = Slot(uri=ODM.PageRefs, name="PageRefs", curie=ODM.curie('PageRefs'),
                   model_uri=ODM.PageRefs, domain=None, range=Optional[str])

slots.OrganizationOID = Slot(uri=ODM.OrganizationOID, name="OrganizationOID", curie=ODM.curie('OrganizationOID'),
                   model_uri=ODM.OrganizationOID, domain=None, range=Optional[str])

slots.Purpose = Slot(uri=ODM.Purpose, name="Purpose", curie=ODM.curie('Purpose'),
                   model_uri=ODM.Purpose, domain=None, range=Optional[str])

slots.CreationDateTime = Slot(uri=ODM.CreationDateTime, name="CreationDateTime", curie=ODM.curie('CreationDateTime'),
                   model_uri=ODM.CreationDateTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.StudyEventRepeatKey = Slot(uri=ODM.StudyEventRepeatKey, name="StudyEventRepeatKey", curie=ODM.curie('StudyEventRepeatKey'),
                   model_uri=ODM.StudyEventRepeatKey, domain=None, range=Optional[str])

slots.Latitude = Slot(uri=ODM.Latitude, name="Latitude", curie=ODM.curie('Latitude'),
                   model_uri=ODM.Latitude, domain=None, range=Optional[Decimal])

slots.FileOID = Slot(uri=ODM.FileOID, name="FileOID", curie=ODM.curie('FileOID'),
                   model_uri=ODM.FileOID, domain=None, range=Optional[str])

slots.DurationPreWindow = Slot(uri=ODM.DurationPreWindow, name="DurationPreWindow", curie=ODM.curie('DurationPreWindow'),
                   model_uri=ODM.DurationPreWindow, domain=None, range=Optional[str])

slots.TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.TranslatedTextRef, domain=None, range=Optional[Union[dict, TranslatedText]])

slots._content = Slot(uri=ODM._content, name="_content", curie=ODM.curie('_content'),
                   model_uri=ODM._content, domain=None, range=Optional[str])

slots.DescriptionRef = Slot(uri=ODM.DescriptionRef, name="DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.DescriptionRef, domain=None, range=Optional[Union[dict, Description]])

slots.MetaDataVersionRefRef = Slot(uri=ODM.MetaDataVersionRefRef, name="MetaDataVersionRefRef", curie=ODM.curie('MetaDataVersionRefRef'),
                   model_uri=ODM.MetaDataVersionRefRef, domain=None, range=Optional[Union[dict, MetaDataVersionRef]])

slots.IncludeRef = Slot(uri=ODM.IncludeRef, name="IncludeRef", curie=ODM.curie('IncludeRef'),
                   model_uri=ODM.IncludeRef, domain=None, range=Optional[Union[dict, Include]])

slots.StandardsRef = Slot(uri=ODM.StandardsRef, name="StandardsRef", curie=ODM.curie('StandardsRef'),
                   model_uri=ODM.StandardsRef, domain=None, range=Optional[Union[dict, Standards]])

slots.AnnotatedCRFRef = Slot(uri=ODM.AnnotatedCRFRef, name="AnnotatedCRFRef", curie=ODM.curie('AnnotatedCRFRef'),
                   model_uri=ODM.AnnotatedCRFRef, domain=None, range=Optional[Union[dict, AnnotatedCRF]])

slots.SupplementalDocRef = Slot(uri=ODM.SupplementalDocRef, name="SupplementalDocRef", curie=ODM.curie('SupplementalDocRef'),
                   model_uri=ODM.SupplementalDocRef, domain=None, range=Optional[Union[dict, SupplementalDoc]])

slots.ValueListDefRef = Slot(uri=ODM.ValueListDefRef, name="ValueListDefRef", curie=ODM.curie('ValueListDefRef'),
                   model_uri=ODM.ValueListDefRef, domain=None, range=Optional[Union[str, ValueListDefOID]])

slots.WhereClauseDefRef = Slot(uri=ODM.WhereClauseDefRef, name="WhereClauseDefRef", curie=ODM.curie('WhereClauseDefRef'),
                   model_uri=ODM.WhereClauseDefRef, domain=None, range=Optional[Union[str, WhereClauseDefOID]])

slots.ProtocolRef = Slot(uri=ODM.ProtocolRef, name="ProtocolRef", curie=ODM.curie('ProtocolRef'),
                   model_uri=ODM.ProtocolRef, domain=None, range=Optional[Union[dict, Protocol]])

slots.WorkflowDefRef = Slot(uri=ODM.WorkflowDefRef, name="WorkflowDefRef", curie=ODM.curie('WorkflowDefRef'),
                   model_uri=ODM.WorkflowDefRef, domain=None, range=Optional[Union[str, WorkflowDefOID]])

slots.StudyEventGroupDefRef = Slot(uri=ODM.StudyEventGroupDefRef, name="StudyEventGroupDefRef", curie=ODM.curie('StudyEventGroupDefRef'),
                   model_uri=ODM.StudyEventGroupDefRef, domain=None, range=Optional[Union[str, StudyEventGroupDefOID]])

slots.StudyEventDefRef = Slot(uri=ODM.StudyEventDefRef, name="StudyEventDefRef", curie=ODM.curie('StudyEventDefRef'),
                   model_uri=ODM.StudyEventDefRef, domain=None, range=Optional[Union[str, StudyEventDefOID]])

slots.ItemGroupDefRef = Slot(uri=ODM.ItemGroupDefRef, name="ItemGroupDefRef", curie=ODM.curie('ItemGroupDefRef'),
                   model_uri=ODM.ItemGroupDefRef, domain=None, range=Optional[Union[str, ItemGroupDefOID]])

slots.ItemDefRef = Slot(uri=ODM.ItemDefRef, name="ItemDefRef", curie=ODM.curie('ItemDefRef'),
                   model_uri=ODM.ItemDefRef, domain=None, range=Optional[Union[str, ItemDefOID]])

slots.CodeListRefRef = Slot(uri=ODM.CodeListRefRef, name="CodeListRefRef", curie=ODM.curie('CodeListRefRef'),
                   model_uri=ODM.CodeListRefRef, domain=None, range=Optional[Union[dict, CodeListRef]])

slots.ConditionDefRef = Slot(uri=ODM.ConditionDefRef, name="ConditionDefRef", curie=ODM.curie('ConditionDefRef'),
                   model_uri=ODM.ConditionDefRef, domain=None, range=Optional[Union[str, ConditionDefOID]])

slots.MethodDefRef = Slot(uri=ODM.MethodDefRef, name="MethodDefRef", curie=ODM.curie('MethodDefRef'),
                   model_uri=ODM.MethodDefRef, domain=None, range=Optional[Union[str, MethodDefOID]])

slots.CommentDefRef = Slot(uri=ODM.CommentDefRef, name="CommentDefRef", curie=ODM.curie('CommentDefRef'),
                   model_uri=ODM.CommentDefRef, domain=None, range=Optional[Union[str, CommentDefOID]])

slots.LeafRef = Slot(uri=ODM.LeafRef, name="LeafRef", curie=ODM.curie('LeafRef'),
                   model_uri=ODM.LeafRef, domain=None, range=Optional[Union[str, LeafID]])

slots.PDFPageRefRef = Slot(uri=ODM.PDFPageRefRef, name="PDFPageRefRef", curie=ODM.curie('PDFPageRefRef'),
                   model_uri=ODM.PDFPageRefRef, domain=None, range=Optional[Union[dict, PDFPageRef]])

slots.StandardRef = Slot(uri=ODM.StandardRef, name="StandardRef", curie=ODM.curie('StandardRef'),
                   model_uri=ODM.StandardRef, domain=None, range=Optional[Union[str, StandardOID]])

slots.DocumentRefRef = Slot(uri=ODM.DocumentRefRef, name="DocumentRefRef", curie=ODM.curie('DocumentRefRef'),
                   model_uri=ODM.DocumentRefRef, domain=None, range=Optional[Union[dict, DocumentRef]])

slots.ItemRefRef = Slot(uri=ODM.ItemRefRef, name="ItemRefRef", curie=ODM.curie('ItemRefRef'),
                   model_uri=ODM.ItemRefRef, domain=None, range=Optional[Union[dict, ItemRef]])

slots.RangeCheckRef = Slot(uri=ODM.RangeCheckRef, name="RangeCheckRef", curie=ODM.curie('RangeCheckRef'),
                   model_uri=ODM.RangeCheckRef, domain=None, range=Optional[Union[dict, RangeCheck]])

slots.WorkflowRefRef = Slot(uri=ODM.WorkflowRefRef, name="WorkflowRefRef", curie=ODM.curie('WorkflowRefRef'),
                   model_uri=ODM.WorkflowRefRef, domain=None, range=Optional[Union[dict, WorkflowRef]])

slots.CodingRef = Slot(uri=ODM.CodingRef, name="CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.CodingRef, domain=None, range=Optional[Union[dict, Coding]])

slots.StudyEventGroupRefRef = Slot(uri=ODM.StudyEventGroupRefRef, name="StudyEventGroupRefRef", curie=ODM.curie('StudyEventGroupRefRef'),
                   model_uri=ODM.StudyEventGroupRefRef, domain=None, range=Optional[Union[dict, StudyEventGroupRef]])

slots.StudyEventRefRef = Slot(uri=ODM.StudyEventRefRef, name="StudyEventRefRef", curie=ODM.curie('StudyEventRefRef'),
                   model_uri=ODM.StudyEventRefRef, domain=None, range=Optional[Union[dict, StudyEventRef]])

slots.ItemGroupRefRef = Slot(uri=ODM.ItemGroupRefRef, name="ItemGroupRefRef", curie=ODM.curie('ItemGroupRefRef'),
                   model_uri=ODM.ItemGroupRefRef, domain=None, range=Optional[Union[dict, ItemGroupRef]])

slots.AliasRef = Slot(uri=ODM.AliasRef, name="AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.AliasRef, domain=None, range=Optional[Union[dict, Alias]])

slots.ClassRef = Slot(uri=ODM.ClassRef, name="ClassRef", curie=ODM.curie('ClassRef'),
                   model_uri=ODM.ClassRef, domain=None, range=Optional[Union[dict, Class]])

slots.OriginRef = Slot(uri=ODM.OriginRef, name="OriginRef", curie=ODM.curie('OriginRef'),
                   model_uri=ODM.OriginRef, domain=None, range=Optional[Union[dict, Origin]])

slots.SubClassRef = Slot(uri=ODM.SubClassRef, name="SubClassRef", curie=ODM.curie('SubClassRef'),
                   model_uri=ODM.SubClassRef, domain=None, range=Optional[Union[dict, SubClass]])

slots.WhereClauseRefRef = Slot(uri=ODM.WhereClauseRefRef, name="WhereClauseRefRef", curie=ODM.curie('WhereClauseRefRef'),
                   model_uri=ODM.WhereClauseRefRef, domain=None, range=Optional[Union[dict, WhereClauseRef]])

slots.SourceItemsRef = Slot(uri=ODM.SourceItemsRef, name="SourceItemsRef", curie=ODM.curie('SourceItemsRef'),
                   model_uri=ODM.SourceItemsRef, domain=None, range=Optional[Union[dict, SourceItems]])

slots.SourceItemRef = Slot(uri=ODM.SourceItemRef, name="SourceItemRef", curie=ODM.curie('SourceItemRef'),
                   model_uri=ODM.SourceItemRef, domain=None, range=Optional[Union[str, SourceItemLeafID]])

slots.ResourceRef = Slot(uri=ODM.ResourceRef, name="ResourceRef", curie=ODM.curie('ResourceRef'),
                   model_uri=ODM.ResourceRef, domain=None, range=Optional[Union[dict, Resource]])

slots.SelectionRef = Slot(uri=ODM.SelectionRef, name="SelectionRef", curie=ODM.curie('SelectionRef'),
                   model_uri=ODM.SelectionRef, domain=None, range=Optional[Union[dict, Selection]])

slots.QuestionRef = Slot(uri=ODM.QuestionRef, name="QuestionRef", curie=ODM.curie('QuestionRef'),
                   model_uri=ODM.QuestionRef, domain=None, range=Optional[Union[dict, Question]])

slots.PromptRef = Slot(uri=ODM.PromptRef, name="PromptRef", curie=ODM.curie('PromptRef'),
                   model_uri=ODM.PromptRef, domain=None, range=Optional[Union[dict, Prompt]])

slots.CRFCompletionInstructionsRef = Slot(uri=ODM.CRFCompletionInstructionsRef, name="CRFCompletionInstructionsRef", curie=ODM.curie('CRFCompletionInstructionsRef'),
                   model_uri=ODM.CRFCompletionInstructionsRef, domain=None, range=Optional[Union[dict, CRFCompletionInstructions]])

slots.ImplementationNotesRef = Slot(uri=ODM.ImplementationNotesRef, name="ImplementationNotesRef", curie=ODM.curie('ImplementationNotesRef'),
                   model_uri=ODM.ImplementationNotesRef, domain=None, range=Optional[Union[dict, ImplementationNotes]])

slots.CDISCNotesRef = Slot(uri=ODM.CDISCNotesRef, name="CDISCNotesRef", curie=ODM.curie('CDISCNotesRef'),
                   model_uri=ODM.CDISCNotesRef, domain=None, range=Optional[Union[dict, CDISCNotes]])

slots.ValueListRefRef = Slot(uri=ODM.ValueListRefRef, name="ValueListRefRef", curie=ODM.curie('ValueListRefRef'),
                   model_uri=ODM.ValueListRefRef, domain=None, range=Optional[Union[dict, ValueListRef]])

slots.ErrorMessageRef = Slot(uri=ODM.ErrorMessageRef, name="ErrorMessageRef", curie=ODM.curie('ErrorMessageRef'),
                   model_uri=ODM.ErrorMessageRef, domain=None, range=Optional[Union[dict, ErrorMessage]])

slots.MethodSignatureRef = Slot(uri=ODM.MethodSignatureRef, name="MethodSignatureRef", curie=ODM.curie('MethodSignatureRef'),
                   model_uri=ODM.MethodSignatureRef, domain=None, range=Optional[Union[dict, MethodSignature]])

slots.FormalExpressionRef = Slot(uri=ODM.FormalExpressionRef, name="FormalExpressionRef", curie=ODM.curie('FormalExpressionRef'),
                   model_uri=ODM.FormalExpressionRef, domain=None, range=Optional[Union[dict, FormalExpression]])

slots.CheckValueRef = Slot(uri=ODM.CheckValueRef, name="CheckValueRef", curie=ODM.curie('CheckValueRef'),
                   model_uri=ODM.CheckValueRef, domain=None, range=Optional[Union[dict, CheckValue]])

slots.CodeListItemRef = Slot(uri=ODM.CodeListItemRef, name="CodeListItemRef", curie=ODM.curie('CodeListItemRef'),
                   model_uri=ODM.CodeListItemRef, domain=None, range=Optional[Union[dict, CodeListItem]])

slots.DecodeRef = Slot(uri=ODM.DecodeRef, name="DecodeRef", curie=ODM.curie('DecodeRef'),
                   model_uri=ODM.DecodeRef, domain=None, range=Optional[Union[dict, Decode]])

slots.ParameterRef = Slot(uri=ODM.ParameterRef, name="ParameterRef", curie=ODM.curie('ParameterRef'),
                   model_uri=ODM.ParameterRef, domain=None, range=Optional[Union[dict, Parameter]])

slots.ReturnValueRef = Slot(uri=ODM.ReturnValueRef, name="ReturnValueRef", curie=ODM.curie('ReturnValueRef'),
                   model_uri=ODM.ReturnValueRef, domain=None, range=Optional[Union[dict, ReturnValue]])

slots.ExternalCodeLibRef = Slot(uri=ODM.ExternalCodeLibRef, name="ExternalCodeLibRef", curie=ODM.curie('ExternalCodeLibRef'),
                   model_uri=ODM.ExternalCodeLibRef, domain=None, range=Optional[Union[dict, ExternalCodeLib]])

slots.StudySummaryRef = Slot(uri=ODM.StudySummaryRef, name="StudySummaryRef", curie=ODM.curie('StudySummaryRef'),
                   model_uri=ODM.StudySummaryRef, domain=None, range=Optional[Union[dict, StudySummary]])

slots.StudyStructureRef = Slot(uri=ODM.StudyStructureRef, name="StudyStructureRef", curie=ODM.curie('StudyStructureRef'),
                   model_uri=ODM.StudyStructureRef, domain=None, range=Optional[Union[dict, StudyStructure]])

slots.TrialPhaseRef = Slot(uri=ODM.TrialPhaseRef, name="TrialPhaseRef", curie=ODM.curie('TrialPhaseRef'),
                   model_uri=ODM.TrialPhaseRef, domain=None, range=Optional[Union[dict, TrialPhase]])

slots.StudyTimingsRef = Slot(uri=ODM.StudyTimingsRef, name="StudyTimingsRef", curie=ODM.curie('StudyTimingsRef'),
                   model_uri=ODM.StudyTimingsRef, domain=None, range=Optional[Union[dict, StudyTimings]])

slots.StudyIndicationsRef = Slot(uri=ODM.StudyIndicationsRef, name="StudyIndicationsRef", curie=ODM.curie('StudyIndicationsRef'),
                   model_uri=ODM.StudyIndicationsRef, domain=None, range=Optional[Union[dict, StudyIndications]])

slots.StudyInterventionsRef = Slot(uri=ODM.StudyInterventionsRef, name="StudyInterventionsRef", curie=ODM.curie('StudyInterventionsRef'),
                   model_uri=ODM.StudyInterventionsRef, domain=None, range=Optional[Union[dict, StudyInterventions]])

slots.StudyObjectivesRef = Slot(uri=ODM.StudyObjectivesRef, name="StudyObjectivesRef", curie=ODM.curie('StudyObjectivesRef'),
                   model_uri=ODM.StudyObjectivesRef, domain=None, range=Optional[Union[dict, StudyObjectives]])

slots.StudyEndPointsRef = Slot(uri=ODM.StudyEndPointsRef, name="StudyEndPointsRef", curie=ODM.curie('StudyEndPointsRef'),
                   model_uri=ODM.StudyEndPointsRef, domain=None, range=Optional[Union[dict, StudyEndPoints]])

slots.StudyTargetPopulationRefRef = Slot(uri=ODM.StudyTargetPopulationRefRef, name="StudyTargetPopulationRefRef", curie=ODM.curie('StudyTargetPopulationRefRef'),
                   model_uri=ODM.StudyTargetPopulationRefRef, domain=None, range=Optional[Union[dict, StudyTargetPopulationRef]])

slots.StudyEstimandsRef = Slot(uri=ODM.StudyEstimandsRef, name="StudyEstimandsRef", curie=ODM.curie('StudyEstimandsRef'),
                   model_uri=ODM.StudyEstimandsRef, domain=None, range=Optional[Union[dict, StudyEstimands]])

slots.InclusionExclusionCriteriaRef = Slot(uri=ODM.InclusionExclusionCriteriaRef, name="InclusionExclusionCriteriaRef", curie=ODM.curie('InclusionExclusionCriteriaRef'),
                   model_uri=ODM.InclusionExclusionCriteriaRef, domain=None, range=Optional[Union[dict, InclusionExclusionCriteria]])

slots.ArmRef = Slot(uri=ODM.ArmRef, name="ArmRef", curie=ODM.curie('ArmRef'),
                   model_uri=ODM.ArmRef, domain=None, range=Optional[Union[str, ArmOID]])

slots.EpochRef = Slot(uri=ODM.EpochRef, name="EpochRef", curie=ODM.curie('EpochRef'),
                   model_uri=ODM.EpochRef, domain=None, range=Optional[Union[str, EpochOID]])

slots.StudyIndicationRef = Slot(uri=ODM.StudyIndicationRef, name="StudyIndicationRef", curie=ODM.curie('StudyIndicationRef'),
                   model_uri=ODM.StudyIndicationRef, domain=None, range=Optional[Union[str, StudyIndicationOID]])

slots.StudyInterventionRefRef = Slot(uri=ODM.StudyInterventionRefRef, name="StudyInterventionRefRef", curie=ODM.curie('StudyInterventionRefRef'),
                   model_uri=ODM.StudyInterventionRefRef, domain=None, range=Optional[Union[dict, StudyInterventionRef]])

slots.StudyObjectiveRef = Slot(uri=ODM.StudyObjectiveRef, name="StudyObjectiveRef", curie=ODM.curie('StudyObjectiveRef'),
                   model_uri=ODM.StudyObjectiveRef, domain=None, range=Optional[Union[str, StudyObjectiveOID]])

slots.StudyEndPointRefRef = Slot(uri=ODM.StudyEndPointRefRef, name="StudyEndPointRefRef", curie=ODM.curie('StudyEndPointRefRef'),
                   model_uri=ODM.StudyEndPointRefRef, domain=None, range=Optional[Union[dict, StudyEndPointRef]])

slots.StudyEstimandRef = Slot(uri=ODM.StudyEstimandRef, name="StudyEstimandRef", curie=ODM.curie('StudyEstimandRef'),
                   model_uri=ODM.StudyEstimandRef, domain=None, range=Optional[Union[str, StudyEstimandOID]])

slots.IntercurrentEventRef = Slot(uri=ODM.IntercurrentEventRef, name="IntercurrentEventRef", curie=ODM.curie('IntercurrentEventRef'),
                   model_uri=ODM.IntercurrentEventRef, domain=None, range=Optional[Union[dict, IntercurrentEvent]])

slots.SummaryMeasureRef = Slot(uri=ODM.SummaryMeasureRef, name="SummaryMeasureRef", curie=ODM.curie('SummaryMeasureRef'),
                   model_uri=ODM.SummaryMeasureRef, domain=None, range=Optional[Union[dict, SummaryMeasure]])

slots.InclusionCriteriaRef = Slot(uri=ODM.InclusionCriteriaRef, name="InclusionCriteriaRef", curie=ODM.curie('InclusionCriteriaRef'),
                   model_uri=ODM.InclusionCriteriaRef, domain=None, range=Optional[Union[dict, InclusionCriteria]])

slots.ExclusionCriteriaRef = Slot(uri=ODM.ExclusionCriteriaRef, name="ExclusionCriteriaRef", curie=ODM.curie('ExclusionCriteriaRef'),
                   model_uri=ODM.ExclusionCriteriaRef, domain=None, range=Optional[Union[dict, ExclusionCriteria]])

slots.CriterionRef = Slot(uri=ODM.CriterionRef, name="CriterionRef", curie=ODM.curie('CriterionRef'),
                   model_uri=ODM.CriterionRef, domain=None, range=Optional[Union[str, CriterionOID]])

slots.StudyParameterRef = Slot(uri=ODM.StudyParameterRef, name="StudyParameterRef", curie=ODM.curie('StudyParameterRef'),
                   model_uri=ODM.StudyParameterRef, domain=None, range=Optional[Union[str, StudyParameterOID]])

slots.ParameterValueRef = Slot(uri=ODM.ParameterValueRef, name="ParameterValueRef", curie=ODM.curie('ParameterValueRef'),
                   model_uri=ODM.ParameterValueRef, domain=None, range=Optional[Union[dict, ParameterValue]])

slots.StudyTimingRef = Slot(uri=ODM.StudyTimingRef, name="StudyTimingRef", curie=ODM.curie('StudyTimingRef'),
                   model_uri=ODM.StudyTimingRef, domain=None, range=Optional[Union[str, StudyTimingOID]])

slots.AbsoluteTimingConstraintRef = Slot(uri=ODM.AbsoluteTimingConstraintRef, name="AbsoluteTimingConstraintRef", curie=ODM.curie('AbsoluteTimingConstraintRef'),
                   model_uri=ODM.AbsoluteTimingConstraintRef, domain=None, range=Optional[Union[str, AbsoluteTimingConstraintOID]])

slots.RelativeTimingConstraintRef = Slot(uri=ODM.RelativeTimingConstraintRef, name="RelativeTimingConstraintRef", curie=ODM.curie('RelativeTimingConstraintRef'),
                   model_uri=ODM.RelativeTimingConstraintRef, domain=None, range=Optional[Union[str, RelativeTimingConstraintOID]])

slots.TransitionTimingConstraintRef = Slot(uri=ODM.TransitionTimingConstraintRef, name="TransitionTimingConstraintRef", curie=ODM.curie('TransitionTimingConstraintRef'),
                   model_uri=ODM.TransitionTimingConstraintRef, domain=None, range=Optional[Union[str, TransitionTimingConstraintOID]])

slots.DurationTimingConstraintRef = Slot(uri=ODM.DurationTimingConstraintRef, name="DurationTimingConstraintRef", curie=ODM.curie('DurationTimingConstraintRef'),
                   model_uri=ODM.DurationTimingConstraintRef, domain=None, range=Optional[Union[str, DurationTimingConstraintOID]])

slots.WorkflowStartRef = Slot(uri=ODM.WorkflowStartRef, name="WorkflowStartRef", curie=ODM.curie('WorkflowStartRef'),
                   model_uri=ODM.WorkflowStartRef, domain=None, range=Optional[Union[dict, WorkflowStart]])

slots.WorkflowEndRef = Slot(uri=ODM.WorkflowEndRef, name="WorkflowEndRef", curie=ODM.curie('WorkflowEndRef'),
                   model_uri=ODM.WorkflowEndRef, domain=None, range=Optional[Union[dict, WorkflowEnd]])

slots.TransitionRef = Slot(uri=ODM.TransitionRef, name="TransitionRef", curie=ODM.curie('TransitionRef'),
                   model_uri=ODM.TransitionRef, domain=None, range=Optional[Union[str, TransitionOID]])

slots.BranchingRef = Slot(uri=ODM.BranchingRef, name="BranchingRef", curie=ODM.curie('BranchingRef'),
                   model_uri=ODM.BranchingRef, domain=None, range=Optional[Union[str, BranchingOID]])

slots.TargetTransitionRef = Slot(uri=ODM.TargetTransitionRef, name="TargetTransitionRef", curie=ODM.curie('TargetTransitionRef'),
                   model_uri=ODM.TargetTransitionRef, domain=None, range=Optional[Union[dict, TargetTransition]])

slots.DefaultTransitionRef = Slot(uri=ODM.DefaultTransitionRef, name="DefaultTransitionRef", curie=ODM.curie('DefaultTransitionRef'),
                   model_uri=ODM.DefaultTransitionRef, domain=None, range=Optional[Union[dict, DefaultTransition]])

slots.UserRefRef = Slot(uri=ODM.UserRefRef, name="UserRefRef", curie=ODM.curie('UserRefRef'),
                   model_uri=ODM.UserRefRef, domain=None, range=Optional[Union[dict, UserRef]])

slots.OrganizationRef = Slot(uri=ODM.OrganizationRef, name="OrganizationRef", curie=ODM.curie('OrganizationRef'),
                   model_uri=ODM.OrganizationRef, domain=None, range=Optional[Union[str, OrganizationOID]])

slots.LocationRefRef = Slot(uri=ODM.LocationRefRef, name="LocationRefRef", curie=ODM.curie('LocationRefRef'),
                   model_uri=ODM.LocationRefRef, domain=None, range=Optional[Union[dict, LocationRef]])

slots.SignatureDefRef = Slot(uri=ODM.SignatureDefRef, name="SignatureDefRef", curie=ODM.curie('SignatureDefRef'),
                   model_uri=ODM.SignatureDefRef, domain=None, range=Optional[Union[str, SignatureDefOID]])

slots.UserNameRef = Slot(uri=ODM.UserNameRef, name="UserNameRef", curie=ODM.curie('UserNameRef'),
                   model_uri=ODM.UserNameRef, domain=None, range=Optional[Union[dict, UserName]])

slots.PrefixRef = Slot(uri=ODM.PrefixRef, name="PrefixRef", curie=ODM.curie('PrefixRef'),
                   model_uri=ODM.PrefixRef, domain=None, range=Optional[Union[dict, Prefix]])

slots.SuffixRef = Slot(uri=ODM.SuffixRef, name="SuffixRef", curie=ODM.curie('SuffixRef'),
                   model_uri=ODM.SuffixRef, domain=None, range=Optional[Union[dict, Suffix]])

slots.FullNameRef = Slot(uri=ODM.FullNameRef, name="FullNameRef", curie=ODM.curie('FullNameRef'),
                   model_uri=ODM.FullNameRef, domain=None, range=Optional[Union[dict, FullName]])

slots.GivenNameRef = Slot(uri=ODM.GivenNameRef, name="GivenNameRef", curie=ODM.curie('GivenNameRef'),
                   model_uri=ODM.GivenNameRef, domain=None, range=Optional[Union[dict, GivenName]])

slots.FamilyNameRef = Slot(uri=ODM.FamilyNameRef, name="FamilyNameRef", curie=ODM.curie('FamilyNameRef'),
                   model_uri=ODM.FamilyNameRef, domain=None, range=Optional[Union[dict, FamilyName]])

slots.ImageRef = Slot(uri=ODM.ImageRef, name="ImageRef", curie=ODM.curie('ImageRef'),
                   model_uri=ODM.ImageRef, domain=None, range=Optional[Union[dict, Image]])

slots.AddressRef = Slot(uri=ODM.AddressRef, name="AddressRef", curie=ODM.curie('AddressRef'),
                   model_uri=ODM.AddressRef, domain=None, range=Optional[Union[dict, Address]])

slots.TelecomRef = Slot(uri=ODM.TelecomRef, name="TelecomRef", curie=ODM.curie('TelecomRef'),
                   model_uri=ODM.TelecomRef, domain=None, range=Optional[Union[dict, Telecom]])

slots.QueryRef = Slot(uri=ODM.QueryRef, name="QueryRef", curie=ODM.curie('QueryRef'),
                   model_uri=ODM.QueryRef, domain=None, range=Optional[Union[str, QueryOID]])

slots.StreetNameRef = Slot(uri=ODM.StreetNameRef, name="StreetNameRef", curie=ODM.curie('StreetNameRef'),
                   model_uri=ODM.StreetNameRef, domain=None, range=Optional[Union[dict, StreetName]])

slots.HouseNumberRef = Slot(uri=ODM.HouseNumberRef, name="HouseNumberRef", curie=ODM.curie('HouseNumberRef'),
                   model_uri=ODM.HouseNumberRef, domain=None, range=Optional[Union[dict, HouseNumber]])

slots.CityRef = Slot(uri=ODM.CityRef, name="CityRef", curie=ODM.curie('CityRef'),
                   model_uri=ODM.CityRef, domain=None, range=Optional[Union[dict, City]])

slots.StateProvRef = Slot(uri=ODM.StateProvRef, name="StateProvRef", curie=ODM.curie('StateProvRef'),
                   model_uri=ODM.StateProvRef, domain=None, range=Optional[Union[dict, StateProv]])

slots.CountryRef = Slot(uri=ODM.CountryRef, name="CountryRef", curie=ODM.curie('CountryRef'),
                   model_uri=ODM.CountryRef, domain=None, range=Optional[Union[dict, Country]])

slots.PostalCodeRef = Slot(uri=ODM.PostalCodeRef, name="PostalCodeRef", curie=ODM.curie('PostalCodeRef'),
                   model_uri=ODM.PostalCodeRef, domain=None, range=Optional[Union[dict, PostalCode]])

slots.GeoPositionRef = Slot(uri=ODM.GeoPositionRef, name="GeoPositionRef", curie=ODM.curie('GeoPositionRef'),
                   model_uri=ODM.GeoPositionRef, domain=None, range=Optional[Union[dict, GeoPosition]])

slots.OtherTextRef = Slot(uri=ODM.OtherTextRef, name="OtherTextRef", curie=ODM.curie('OtherTextRef'),
                   model_uri=ODM.OtherTextRef, domain=None, range=Optional[Union[dict, OtherText]])

slots.MeaningRef = Slot(uri=ODM.MeaningRef, name="MeaningRef", curie=ODM.curie('MeaningRef'),
                   model_uri=ODM.MeaningRef, domain=None, range=Optional[Union[dict, Meaning]])

slots.LegalReasonRef = Slot(uri=ODM.LegalReasonRef, name="LegalReasonRef", curie=ODM.curie('LegalReasonRef'),
                   model_uri=ODM.LegalReasonRef, domain=None, range=Optional[Union[dict, LegalReason]])

slots.ItemGroupDataRef = Slot(uri=ODM.ItemGroupDataRef, name="ItemGroupDataRef", curie=ODM.curie('ItemGroupDataRef'),
                   model_uri=ODM.ItemGroupDataRef, domain=None, range=Optional[Union[dict, ItemGroupData]])

slots.AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.AuditRecordRef, domain=None, range=Optional[Union[dict, AuditRecord]])

slots.SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.SignatureRefRef, domain=None, range=Optional[Union[dict, SignatureRef]])

slots.AnnotationRef = Slot(uri=ODM.AnnotationRef, name="AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.AnnotationRef, domain=None, range=Optional[Union[str, AnnotationID]])

slots.SubjectDataRef = Slot(uri=ODM.SubjectDataRef, name="SubjectDataRef", curie=ODM.curie('SubjectDataRef'),
                   model_uri=ODM.SubjectDataRef, domain=None, range=Optional[Union[dict, SubjectData]])

slots.InvestigatorRefRef = Slot(uri=ODM.InvestigatorRefRef, name="InvestigatorRefRef", curie=ODM.curie('InvestigatorRefRef'),
                   model_uri=ODM.InvestigatorRefRef, domain=None, range=Optional[Union[dict, InvestigatorRef]])

slots.SiteRefRef = Slot(uri=ODM.SiteRefRef, name="SiteRefRef", curie=ODM.curie('SiteRefRef'),
                   model_uri=ODM.SiteRefRef, domain=None, range=Optional[Union[dict, SiteRef]])

slots.StudyEventDataRef = Slot(uri=ODM.StudyEventDataRef, name="StudyEventDataRef", curie=ODM.curie('StudyEventDataRef'),
                   model_uri=ODM.StudyEventDataRef, domain=None, range=Optional[Union[dict, StudyEventData]])

slots.ItemDataRef = Slot(uri=ODM.ItemDataRef, name="ItemDataRef", curie=ODM.curie('ItemDataRef'),
                   model_uri=ODM.ItemDataRef, domain=None, range=Optional[Union[dict, ItemData]])

slots.DateTimeStampRef = Slot(uri=ODM.DateTimeStampRef, name="DateTimeStampRef", curie=ODM.curie('DateTimeStampRef'),
                   model_uri=ODM.DateTimeStampRef, domain=None, range=Optional[Union[dict, DateTimeStamp]])

slots.ReasonForChangeRef = Slot(uri=ODM.ReasonForChangeRef, name="ReasonForChangeRef", curie=ODM.curie('ReasonForChangeRef'),
                   model_uri=ODM.ReasonForChangeRef, domain=None, range=Optional[Union[dict, ReasonForChange]])

slots.SourceIDRef = Slot(uri=ODM.SourceIDRef, name="SourceIDRef", curie=ODM.curie('SourceIDRef'),
                   model_uri=ODM.SourceIDRef, domain=None, range=Optional[Union[dict, SourceID]])

slots.StudyRef = Slot(uri=ODM.StudyRef, name="StudyRef", curie=ODM.curie('StudyRef'),
                   model_uri=ODM.StudyRef, domain=None, range=Optional[Union[str, StudyOID]])

slots.AdminDataRef = Slot(uri=ODM.AdminDataRef, name="AdminDataRef", curie=ODM.curie('AdminDataRef'),
                   model_uri=ODM.AdminDataRef, domain=None, range=Optional[Union[dict, AdminData]])

slots.ReferenceDataRef = Slot(uri=ODM.ReferenceDataRef, name="ReferenceDataRef", curie=ODM.curie('ReferenceDataRef'),
                   model_uri=ODM.ReferenceDataRef, domain=None, range=Optional[Union[dict, ReferenceData]])

slots.ClinicalDataRef = Slot(uri=ODM.ClinicalDataRef, name="ClinicalDataRef", curie=ODM.curie('ClinicalDataRef'),
                   model_uri=ODM.ClinicalDataRef, domain=None, range=Optional[Union[dict, ClinicalData]])

slots.AssociationRef = Slot(uri=ODM.AssociationRef, name="AssociationRef", curie=ODM.curie('AssociationRef'),
                   model_uri=ODM.AssociationRef, domain=None, range=Optional[Union[dict, Association]])

slots.KeySetRef = Slot(uri=ODM.KeySetRef, name="KeySetRef", curie=ODM.curie('KeySetRef'),
                   model_uri=ODM.KeySetRef, domain=None, range=Optional[Union[dict, KeySet]])

slots.CommentRef = Slot(uri=ODM.CommentRef, name="CommentRef", curie=ODM.curie('CommentRef'),
                   model_uri=ODM.CommentRef, domain=None, range=Optional[Union[dict, Comment]])

slots.FlagRef = Slot(uri=ODM.FlagRef, name="FlagRef", curie=ODM.curie('FlagRef'),
                   model_uri=ODM.FlagRef, domain=None, range=Optional[Union[dict, Flag]])

slots.FlagValueRef = Slot(uri=ODM.FlagValueRef, name="FlagValueRef", curie=ODM.curie('FlagValueRef'),
                   model_uri=ODM.FlagValueRef, domain=None, range=Optional[Union[dict, FlagValue]])

slots.FlagTypeRef = Slot(uri=ODM.FlagTypeRef, name="FlagTypeRef", curie=ODM.curie('FlagTypeRef'),
                   model_uri=ODM.FlagTypeRef, domain=None, range=Optional[Union[dict, FlagType]])

slots.range = Slot(uri=ODM.range, name="range", curie=ODM.curie('range'),
                   model_uri=ODM.range, domain=None, range=Optional[str])

slots.Alias_ContextRef = Slot(uri=ODM.ContextRef, name="Alias_ContextRef", curie=ODM.curie('ContextRef'),
                   model_uri=ODM.Alias_ContextRef, domain=Alias, range=str)

slots.Alias_Name = Slot(uri=ODM.Name, name="Alias_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Alias_Name, domain=Alias, range=str)

slots.Description_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="Description_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.Description_TranslatedTextRef, domain=Description, range=Optional[Union[Union[dict, "TranslatedText"], List[Union[dict, "TranslatedText"]]]])

slots.TranslatedText__language = Slot(uri=ODM._language, name="TranslatedText__language", curie=ODM.curie('_language'),
                   model_uri=ODM.TranslatedText__language, domain=TranslatedText, range=Optional[str])

slots.TranslatedText_Type = Slot(uri=ODM.Type, name="TranslatedText_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.TranslatedText_Type, domain=TranslatedText, range=str)

slots.TranslatedText__content = Slot(uri=ODM._content, name="TranslatedText__content", curie=ODM.curie('_content'),
                   model_uri=ODM.TranslatedText__content, domain=TranslatedText, range=Optional[str])

slots.Study_OID = Slot(uri=ODM.OID, name="Study_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Study_OID, domain=Study, range=Union[str, StudyOID])

slots.Study_StudyName = Slot(uri=ODM.StudyName, name="Study_StudyName", curie=ODM.curie('StudyName'),
                   model_uri=ODM.Study_StudyName, domain=Study, range=str)

slots.Study_ProtocolName = Slot(uri=ODM.ProtocolName, name="Study_ProtocolName", curie=ODM.curie('ProtocolName'),
                   model_uri=ODM.Study_ProtocolName, domain=Study, range=str)

slots.Study_VersionID = Slot(uri=ODM.VersionID, name="Study_VersionID", curie=ODM.curie('VersionID'),
                   model_uri=ODM.Study_VersionID, domain=Study, range=Optional[str])

slots.Study_VersionName = Slot(uri=ODM.VersionName, name="Study_VersionName", curie=ODM.curie('VersionName'),
                   model_uri=ODM.Study_VersionName, domain=Study, range=Optional[str])

slots.Study_Status = Slot(uri=ODM.Status, name="Study_Status", curie=ODM.curie('Status'),
                   model_uri=ODM.Study_Status, domain=Study, range=Optional[str])

slots.Study_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Study_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Study_DescriptionRef, domain=Study, range=Optional[Union[dict, Description]])

slots.Study_MetaDataVersionRefRef = Slot(uri=ODM.MetaDataVersionRefRef, name="Study_MetaDataVersionRefRef", curie=ODM.curie('MetaDataVersionRefRef'),
                   model_uri=ODM.Study_MetaDataVersionRefRef, domain=Study, range=Optional[Union[Dict[Union[str, MetaDataVersionOID], Union[dict, "MetaDataVersion"]], List[Union[dict, "MetaDataVersion"]]]])

slots.MetaDataVersion_OID = Slot(uri=ODM.OID, name="MetaDataVersion_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.MetaDataVersion_OID, domain=MetaDataVersion, range=Union[str, MetaDataVersionOID])

slots.MetaDataVersion_Name = Slot(uri=ODM.Name, name="MetaDataVersion_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.MetaDataVersion_Name, domain=MetaDataVersion, range=str)

slots.MetaDataVersion_CommentOID = Slot(uri=ODM.CommentOID, name="MetaDataVersion_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.MetaDataVersion_CommentOID, domain=MetaDataVersion, range=Optional[str])

slots.MetaDataVersion_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="MetaDataVersion_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.MetaDataVersion_DescriptionRef, domain=MetaDataVersion, range=Optional[Union[dict, Description]])

slots.MetaDataVersion_IncludeRef = Slot(uri=ODM.IncludeRef, name="MetaDataVersion_IncludeRef", curie=ODM.curie('IncludeRef'),
                   model_uri=ODM.MetaDataVersion_IncludeRef, domain=MetaDataVersion, range=Optional[Union[dict, "Include"]])

slots.MetaDataVersion_StandardsRef = Slot(uri=ODM.StandardsRef, name="MetaDataVersion_StandardsRef", curie=ODM.curie('StandardsRef'),
                   model_uri=ODM.MetaDataVersion_StandardsRef, domain=MetaDataVersion, range=Optional[Union[dict, "Standards"]])

slots.MetaDataVersion_AnnotatedCRFRef = Slot(uri=ODM.AnnotatedCRFRef, name="MetaDataVersion_AnnotatedCRFRef", curie=ODM.curie('AnnotatedCRFRef'),
                   model_uri=ODM.MetaDataVersion_AnnotatedCRFRef, domain=MetaDataVersion, range=Optional[Union[dict, "AnnotatedCRF"]])

slots.MetaDataVersion_SupplementalDocRef = Slot(uri=ODM.SupplementalDocRef, name="MetaDataVersion_SupplementalDocRef", curie=ODM.curie('SupplementalDocRef'),
                   model_uri=ODM.MetaDataVersion_SupplementalDocRef, domain=MetaDataVersion, range=Optional[Union[dict, "SupplementalDoc"]])

slots.MetaDataVersion_ValueListDefRef = Slot(uri=ODM.ValueListDefRef, name="MetaDataVersion_ValueListDefRef", curie=ODM.curie('ValueListDefRef'),
                   model_uri=ODM.MetaDataVersion_ValueListDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ValueListDefOID], Union[dict, "ValueListDef"]], List[Union[dict, "ValueListDef"]]]])

slots.MetaDataVersion_WhereClauseDefRef = Slot(uri=ODM.WhereClauseDefRef, name="MetaDataVersion_WhereClauseDefRef", curie=ODM.curie('WhereClauseDefRef'),
                   model_uri=ODM.MetaDataVersion_WhereClauseDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, WhereClauseDefOID], Union[dict, "WhereClauseDef"]], List[Union[dict, "WhereClauseDef"]]]])

slots.MetaDataVersion_ProtocolRef = Slot(uri=ODM.ProtocolRef, name="MetaDataVersion_ProtocolRef", curie=ODM.curie('ProtocolRef'),
                   model_uri=ODM.MetaDataVersion_ProtocolRef, domain=MetaDataVersion, range=Optional[Union[dict, "Protocol"]])

slots.MetaDataVersion_WorkflowDefRef = Slot(uri=ODM.WorkflowDefRef, name="MetaDataVersion_WorkflowDefRef", curie=ODM.curie('WorkflowDefRef'),
                   model_uri=ODM.MetaDataVersion_WorkflowDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, WorkflowDefOID], Union[dict, "WorkflowDef"]], List[Union[dict, "WorkflowDef"]]]])

slots.MetaDataVersion_StudyEventGroupDefRef = Slot(uri=ODM.StudyEventGroupDefRef, name="MetaDataVersion_StudyEventGroupDefRef", curie=ODM.curie('StudyEventGroupDefRef'),
                   model_uri=ODM.MetaDataVersion_StudyEventGroupDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, StudyEventGroupDefOID], Union[dict, "StudyEventGroupDef"]], List[Union[dict, "StudyEventGroupDef"]]]])

slots.MetaDataVersion_StudyEventDefRef = Slot(uri=ODM.StudyEventDefRef, name="MetaDataVersion_StudyEventDefRef", curie=ODM.curie('StudyEventDefRef'),
                   model_uri=ODM.MetaDataVersion_StudyEventDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, StudyEventDefOID], Union[dict, "StudyEventDef"]], List[Union[dict, "StudyEventDef"]]]])

slots.MetaDataVersion_ItemGroupDefRef = Slot(uri=ODM.ItemGroupDefRef, name="MetaDataVersion_ItemGroupDefRef", curie=ODM.curie('ItemGroupDefRef'),
                   model_uri=ODM.MetaDataVersion_ItemGroupDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ItemGroupDefOID], Union[dict, "ItemGroupDef"]], List[Union[dict, "ItemGroupDef"]]]])

slots.MetaDataVersion_ItemDefRef = Slot(uri=ODM.ItemDefRef, name="MetaDataVersion_ItemDefRef", curie=ODM.curie('ItemDefRef'),
                   model_uri=ODM.MetaDataVersion_ItemDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ItemDefOID], Union[dict, "ItemDef"]], List[Union[dict, "ItemDef"]]]])

slots.MetaDataVersion_CodeListRefRef = Slot(uri=ODM.CodeListRefRef, name="MetaDataVersion_CodeListRefRef", curie=ODM.curie('CodeListRefRef'),
                   model_uri=ODM.MetaDataVersion_CodeListRefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, CodeListOID], Union[dict, "CodeList"]], List[Union[dict, "CodeList"]]]])

slots.MetaDataVersion_ConditionDefRef = Slot(uri=ODM.ConditionDefRef, name="MetaDataVersion_ConditionDefRef", curie=ODM.curie('ConditionDefRef'),
                   model_uri=ODM.MetaDataVersion_ConditionDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, ConditionDefOID], Union[dict, "ConditionDef"]], List[Union[dict, "ConditionDef"]]]])

slots.MetaDataVersion_MethodDefRef = Slot(uri=ODM.MethodDefRef, name="MetaDataVersion_MethodDefRef", curie=ODM.curie('MethodDefRef'),
                   model_uri=ODM.MetaDataVersion_MethodDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, MethodDefOID], Union[dict, "MethodDef"]], List[Union[dict, "MethodDef"]]]])

slots.MetaDataVersion_CommentDefRef = Slot(uri=ODM.CommentDefRef, name="MetaDataVersion_CommentDefRef", curie=ODM.curie('CommentDefRef'),
                   model_uri=ODM.MetaDataVersion_CommentDefRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, CommentDefOID], Union[dict, "CommentDef"]], List[Union[dict, "CommentDef"]]]])

slots.MetaDataVersion_LeafRef = Slot(uri=ODM.LeafRef, name="MetaDataVersion_LeafRef", curie=ODM.curie('LeafRef'),
                   model_uri=ODM.MetaDataVersion_LeafRef, domain=MetaDataVersion, range=Optional[Union[Dict[Union[str, LeafID], Union[dict, "Leaf"]], List[Union[dict, "Leaf"]]]])

slots.DocumentRef_LeafID = Slot(uri=ODM.LeafID, name="DocumentRef_LeafID", curie=ODM.curie('LeafID'),
                   model_uri=ODM.DocumentRef_LeafID, domain=DocumentRef, range=str)

slots.DocumentRef_PDFPageRefRef = Slot(uri=ODM.PDFPageRefRef, name="DocumentRef_PDFPageRefRef", curie=ODM.curie('PDFPageRefRef'),
                   model_uri=ODM.DocumentRef_PDFPageRefRef, domain=DocumentRef, range=Optional[Union[Union[dict, "PDFPageRef"], List[Union[dict, "PDFPageRef"]]]])

slots.PDFPageRef_PageRefs = Slot(uri=ODM.PageRefs, name="PDFPageRef_PageRefs", curie=ODM.curie('PageRefs'),
                   model_uri=ODM.PDFPageRef_PageRefs, domain=PDFPageRef, range=Optional[str])

slots.PDFPageRef_FirstPage = Slot(uri=ODM.FirstPage, name="PDFPageRef_FirstPage", curie=ODM.curie('FirstPage'),
                   model_uri=ODM.PDFPageRef_FirstPage, domain=PDFPageRef, range=Optional[int])

slots.PDFPageRef_LastPage = Slot(uri=ODM.LastPage, name="PDFPageRef_LastPage", curie=ODM.curie('LastPage'),
                   model_uri=ODM.PDFPageRef_LastPage, domain=PDFPageRef, range=Optional[int])

slots.PDFPageRef_Type = Slot(uri=ODM.Type, name="PDFPageRef_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.PDFPageRef_Type, domain=PDFPageRef, range=Union[str, "PDFPageType"])

slots.PDFPageRef_TitleRef = Slot(uri=ODM.TitleRef, name="PDFPageRef_TitleRef", curie=ODM.curie('TitleRef'),
                   model_uri=ODM.PDFPageRef_TitleRef, domain=PDFPageRef, range=Optional[str])

slots.Leaf_ID = Slot(uri=ODM.ID, name="Leaf_ID", curie=ODM.curie('ID'),
                   model_uri=ODM.Leaf_ID, domain=Leaf, range=Union[str, LeafID])

slots.Leaf_href = Slot(uri=ODM.href, name="Leaf_href", curie=ODM.curie('href'),
                   model_uri=ODM.Leaf_href, domain=Leaf, range=Union[str, URIorCURIE])

slots.Leaf_TitleRef = Slot(uri=ODM.TitleRef, name="Leaf_TitleRef", curie=ODM.curie('TitleRef'),
                   model_uri=ODM.Leaf_TitleRef, domain=Leaf, range=Optional[Union[dict, "Title"]])

slots.Title_range = Slot(uri=ODM.range, name="Title_range", curie=ODM.curie('range'),
                   model_uri=ODM.Title_range, domain=Title, range=Optional[str])

slots.Include_StudyOID = Slot(uri=ODM.StudyOID, name="Include_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.Include_StudyOID, domain=Include, range=str)

slots.Include_MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="Include_MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.Include_MetaDataVersionOID, domain=Include, range=str)

slots.Include_href = Slot(uri=ODM.href, name="Include_href", curie=ODM.curie('href'),
                   model_uri=ODM.Include_href, domain=Include, range=Optional[Union[str, URIorCURIE]])

slots.Standards_StandardRef = Slot(uri=ODM.StandardRef, name="Standards_StandardRef", curie=ODM.curie('StandardRef'),
                   model_uri=ODM.Standards_StandardRef, domain=Standards, range=Optional[Union[Dict[Union[str, StandardOID], Union[dict, "Standard"]], List[Union[dict, "Standard"]]]])

slots.Standard_OID = Slot(uri=ODM.OID, name="Standard_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Standard_OID, domain=Standard, range=Union[str, StandardOID])

slots.Standard_Name = Slot(uri=ODM.Name, name="Standard_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Standard_Name, domain=Standard, range=Union[str, "StandardName"])

slots.Standard_Type = Slot(uri=ODM.Type, name="Standard_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.Standard_Type, domain=Standard, range=Union[str, "StandardType"])

slots.Standard_PublishingSet = Slot(uri=ODM.PublishingSet, name="Standard_PublishingSet", curie=ODM.curie('PublishingSet'),
                   model_uri=ODM.Standard_PublishingSet, domain=Standard, range=Optional[Union[str, "StandardPublishingSet"]])

slots.Standard_Version = Slot(uri=ODM.Version, name="Standard_Version", curie=ODM.curie('Version'),
                   model_uri=ODM.Standard_Version, domain=Standard, range=str)

slots.Standard_Status = Slot(uri=ODM.Status, name="Standard_Status", curie=ODM.curie('Status'),
                   model_uri=ODM.Standard_Status, domain=Standard, range=str)

slots.Standard_CommentOID = Slot(uri=ODM.CommentOID, name="Standard_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.Standard_CommentOID, domain=Standard, range=Optional[str])

slots.AnnotatedCRF_DocumentRefRef = Slot(uri=ODM.DocumentRefRef, name="AnnotatedCRF_DocumentRefRef", curie=ODM.curie('DocumentRefRef'),
                   model_uri=ODM.AnnotatedCRF_DocumentRefRef, domain=AnnotatedCRF, range=Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]])

slots.SupplementalDoc_DocumentRefRef = Slot(uri=ODM.DocumentRefRef, name="SupplementalDoc_DocumentRefRef", curie=ODM.curie('DocumentRefRef'),
                   model_uri=ODM.SupplementalDoc_DocumentRefRef, domain=SupplementalDoc, range=Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]])

slots.ValueListDef_OID = Slot(uri=ODM.OID, name="ValueListDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ValueListDef_OID, domain=ValueListDef, range=Union[str, ValueListDefOID])

slots.ValueListDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="ValueListDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.ValueListDef_DescriptionRef, domain=ValueListDef, range=Optional[Union[dict, Description]])

slots.ValueListDef_ItemRefRef = Slot(uri=ODM.ItemRefRef, name="ValueListDef_ItemRefRef", curie=ODM.curie('ItemRefRef'),
                   model_uri=ODM.ValueListDef_ItemRefRef, domain=ValueListDef, range=Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]])

slots.WhereClauseRef_WhereClauseOID = Slot(uri=ODM.WhereClauseOID, name="WhereClauseRef_WhereClauseOID", curie=ODM.curie('WhereClauseOID'),
                   model_uri=ODM.WhereClauseRef_WhereClauseOID, domain=WhereClauseRef, range=str)

slots.WhereClauseDef_OID = Slot(uri=ODM.OID, name="WhereClauseDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.WhereClauseDef_OID, domain=WhereClauseDef, range=Union[str, WhereClauseDefOID])

slots.WhereClauseDef_CommentOID = Slot(uri=ODM.CommentOID, name="WhereClauseDef_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.WhereClauseDef_CommentOID, domain=WhereClauseDef, range=Optional[str])

slots.WhereClauseDef_RangeCheckRef = Slot(uri=ODM.RangeCheckRef, name="WhereClauseDef_RangeCheckRef", curie=ODM.curie('RangeCheckRef'),
                   model_uri=ODM.WhereClauseDef_RangeCheckRef, domain=WhereClauseDef, range=Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]])

slots.StudyEventGroupRef_StudyEventGroupOID = Slot(uri=ODM.StudyEventGroupOID, name="StudyEventGroupRef_StudyEventGroupOID", curie=ODM.curie('StudyEventGroupOID'),
                   model_uri=ODM.StudyEventGroupRef_StudyEventGroupOID, domain=StudyEventGroupRef, range=str)

slots.StudyEventGroupRef_OrderNumber = Slot(uri=ODM.OrderNumber, name="StudyEventGroupRef_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.StudyEventGroupRef_OrderNumber, domain=StudyEventGroupRef, range=Optional[int])

slots.StudyEventGroupRef_Mandatory = Slot(uri=ODM.Mandatory, name="StudyEventGroupRef_Mandatory", curie=ODM.curie('Mandatory'),
                   model_uri=ODM.StudyEventGroupRef_Mandatory, domain=StudyEventGroupRef, range=Union[str, "YesOrNo"])

slots.StudyEventGroupRef_CollectionExceptionConditionOID = Slot(uri=ODM.CollectionExceptionConditionOID, name="StudyEventGroupRef_CollectionExceptionConditionOID", curie=ODM.curie('CollectionExceptionConditionOID'),
                   model_uri=ODM.StudyEventGroupRef_CollectionExceptionConditionOID, domain=StudyEventGroupRef, range=Optional[str])

slots.StudyEventGroupRef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyEventGroupRef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyEventGroupRef_DescriptionRef, domain=StudyEventGroupRef, range=Optional[Union[dict, Description]])

slots.StudyEventGroupDef_OID = Slot(uri=ODM.OID, name="StudyEventGroupDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEventGroupDef_OID, domain=StudyEventGroupDef, range=Union[str, StudyEventGroupDefOID])

slots.StudyEventGroupDef_Name = Slot(uri=ODM.Name, name="StudyEventGroupDef_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.StudyEventGroupDef_Name, domain=StudyEventGroupDef, range=str)

slots.StudyEventGroupDef_ArmOID = Slot(uri=ODM.ArmOID, name="StudyEventGroupDef_ArmOID", curie=ODM.curie('ArmOID'),
                   model_uri=ODM.StudyEventGroupDef_ArmOID, domain=StudyEventGroupDef, range=Optional[str])

slots.StudyEventGroupDef_EpochOID = Slot(uri=ODM.EpochOID, name="StudyEventGroupDef_EpochOID", curie=ODM.curie('EpochOID'),
                   model_uri=ODM.StudyEventGroupDef_EpochOID, domain=StudyEventGroupDef, range=Optional[str])

slots.StudyEventGroupDef_CommentOID = Slot(uri=ODM.CommentOID, name="StudyEventGroupDef_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.StudyEventGroupDef_CommentOID, domain=StudyEventGroupDef, range=Optional[str])

slots.StudyEventGroupDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyEventGroupDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyEventGroupDef_DescriptionRef, domain=StudyEventGroupDef, range=Optional[Union[dict, Description]])

slots.StudyEventGroupDef_WorkflowRefRef = Slot(uri=ODM.WorkflowRefRef, name="StudyEventGroupDef_WorkflowRefRef", curie=ODM.curie('WorkflowRefRef'),
                   model_uri=ODM.StudyEventGroupDef_WorkflowRefRef, domain=StudyEventGroupDef, range=Optional[Union[dict, "WorkflowRef"]])

slots.StudyEventGroupDef_CodingRef = Slot(uri=ODM.CodingRef, name="StudyEventGroupDef_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.StudyEventGroupDef_CodingRef, domain=StudyEventGroupDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyEventGroupDef_StudyEventGroupRefRef = Slot(uri=ODM.StudyEventGroupRefRef, name="StudyEventGroupDef_StudyEventGroupRefRef", curie=ODM.curie('StudyEventGroupRefRef'),
                   model_uri=ODM.StudyEventGroupDef_StudyEventGroupRefRef, domain=StudyEventGroupDef, range=Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]])

slots.StudyEventGroupDef_StudyEventRefRef = Slot(uri=ODM.StudyEventRefRef, name="StudyEventGroupDef_StudyEventRefRef", curie=ODM.curie('StudyEventRefRef'),
                   model_uri=ODM.StudyEventGroupDef_StudyEventRefRef, domain=StudyEventGroupDef, range=Optional[Union[Union[dict, "StudyEventRef"], List[Union[dict, "StudyEventRef"]]]])

slots.StudyEventRef_StudyEventOID = Slot(uri=ODM.StudyEventOID, name="StudyEventRef_StudyEventOID", curie=ODM.curie('StudyEventOID'),
                   model_uri=ODM.StudyEventRef_StudyEventOID, domain=StudyEventRef, range=str)

slots.StudyEventRef_OrderNumber = Slot(uri=ODM.OrderNumber, name="StudyEventRef_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.StudyEventRef_OrderNumber, domain=StudyEventRef, range=Optional[int])

slots.StudyEventRef_Mandatory = Slot(uri=ODM.Mandatory, name="StudyEventRef_Mandatory", curie=ODM.curie('Mandatory'),
                   model_uri=ODM.StudyEventRef_Mandatory, domain=StudyEventRef, range=Union[str, "YesOrNo"])

slots.StudyEventRef_CollectionExceptionConditionOID = Slot(uri=ODM.CollectionExceptionConditionOID, name="StudyEventRef_CollectionExceptionConditionOID", curie=ODM.curie('CollectionExceptionConditionOID'),
                   model_uri=ODM.StudyEventRef_CollectionExceptionConditionOID, domain=StudyEventRef, range=Optional[str])

slots.StudyEventDef_OID = Slot(uri=ODM.OID, name="StudyEventDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEventDef_OID, domain=StudyEventDef, range=Union[str, StudyEventDefOID])

slots.StudyEventDef_Name = Slot(uri=ODM.Name, name="StudyEventDef_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.StudyEventDef_Name, domain=StudyEventDef, range=str)

slots.StudyEventDef_Repeating = Slot(uri=ODM.Repeating, name="StudyEventDef_Repeating", curie=ODM.curie('Repeating'),
                   model_uri=ODM.StudyEventDef_Repeating, domain=StudyEventDef, range=Union[str, "YesOrNo"])

slots.StudyEventDef_Type = Slot(uri=ODM.Type, name="StudyEventDef_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.StudyEventDef_Type, domain=StudyEventDef, range=Union[str, "EventType"])

slots.StudyEventDef_Category = Slot(uri=ODM.Category, name="StudyEventDef_Category", curie=ODM.curie('Category'),
                   model_uri=ODM.StudyEventDef_Category, domain=StudyEventDef, range=Optional[str])

slots.StudyEventDef_CommentOID = Slot(uri=ODM.CommentOID, name="StudyEventDef_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.StudyEventDef_CommentOID, domain=StudyEventDef, range=Optional[str])

slots.StudyEventDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyEventDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyEventDef_DescriptionRef, domain=StudyEventDef, range=Optional[Union[dict, Description]])

slots.StudyEventDef_ItemGroupRefRef = Slot(uri=ODM.ItemGroupRefRef, name="StudyEventDef_ItemGroupRefRef", curie=ODM.curie('ItemGroupRefRef'),
                   model_uri=ODM.StudyEventDef_ItemGroupRefRef, domain=StudyEventDef, range=Optional[Union[Union[dict, "ItemGroupRef"], List[Union[dict, "ItemGroupRef"]]]])

slots.StudyEventDef_WorkflowRefRef = Slot(uri=ODM.WorkflowRefRef, name="StudyEventDef_WorkflowRefRef", curie=ODM.curie('WorkflowRefRef'),
                   model_uri=ODM.StudyEventDef_WorkflowRefRef, domain=StudyEventDef, range=Optional[Union[dict, "WorkflowRef"]])

slots.StudyEventDef_CodingRef = Slot(uri=ODM.CodingRef, name="StudyEventDef_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.StudyEventDef_CodingRef, domain=StudyEventDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyEventDef_AliasRef = Slot(uri=ODM.AliasRef, name="StudyEventDef_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.StudyEventDef_AliasRef, domain=StudyEventDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.ItemGroupRef_ItemGroupOID = Slot(uri=ODM.ItemGroupOID, name="ItemGroupRef_ItemGroupOID", curie=ODM.curie('ItemGroupOID'),
                   model_uri=ODM.ItemGroupRef_ItemGroupOID, domain=ItemGroupRef, range=str)

slots.ItemGroupRef_MethodOID = Slot(uri=ODM.MethodOID, name="ItemGroupRef_MethodOID", curie=ODM.curie('MethodOID'),
                   model_uri=ODM.ItemGroupRef_MethodOID, domain=ItemGroupRef, range=Optional[str])

slots.ItemGroupRef_OrderNumber = Slot(uri=ODM.OrderNumber, name="ItemGroupRef_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.ItemGroupRef_OrderNumber, domain=ItemGroupRef, range=Optional[int])

slots.ItemGroupRef_Mandatory = Slot(uri=ODM.Mandatory, name="ItemGroupRef_Mandatory", curie=ODM.curie('Mandatory'),
                   model_uri=ODM.ItemGroupRef_Mandatory, domain=ItemGroupRef, range=Union[str, "YesOrNo"])

slots.ItemGroupRef_CollectionExceptionConditionOID = Slot(uri=ODM.CollectionExceptionConditionOID, name="ItemGroupRef_CollectionExceptionConditionOID", curie=ODM.curie('CollectionExceptionConditionOID'),
                   model_uri=ODM.ItemGroupRef_CollectionExceptionConditionOID, domain=ItemGroupRef, range=Optional[str])

slots.ItemGroupDef_OID = Slot(uri=ODM.OID, name="ItemGroupDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ItemGroupDef_OID, domain=ItemGroupDef, range=Union[str, ItemGroupDefOID])

slots.ItemGroupDef_Name = Slot(uri=ODM.Name, name="ItemGroupDef_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.ItemGroupDef_Name, domain=ItemGroupDef, range=str)

slots.ItemGroupDef_Repeating = Slot(uri=ODM.Repeating, name="ItemGroupDef_Repeating", curie=ODM.curie('Repeating'),
                   model_uri=ODM.ItemGroupDef_Repeating, domain=ItemGroupDef, range=Union[str, "ItemGroupRepeatingType"])

slots.ItemGroupDef_RepeatingLimit = Slot(uri=ODM.RepeatingLimit, name="ItemGroupDef_RepeatingLimit", curie=ODM.curie('RepeatingLimit'),
                   model_uri=ODM.ItemGroupDef_RepeatingLimit, domain=ItemGroupDef, range=Optional[int])

slots.ItemGroupDef_IsReferenceData = Slot(uri=ODM.IsReferenceData, name="ItemGroupDef_IsReferenceData", curie=ODM.curie('IsReferenceData'),
                   model_uri=ODM.ItemGroupDef_IsReferenceData, domain=ItemGroupDef, range=Optional[Union[str, "YesOrNo"]])

slots.ItemGroupDef_Structure = Slot(uri=ODM.Structure, name="ItemGroupDef_Structure", curie=ODM.curie('Structure'),
                   model_uri=ODM.ItemGroupDef_Structure, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_ArchiveLocationID = Slot(uri=ODM.ArchiveLocationID, name="ItemGroupDef_ArchiveLocationID", curie=ODM.curie('ArchiveLocationID'),
                   model_uri=ODM.ItemGroupDef_ArchiveLocationID, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_DatasetName = Slot(uri=ODM.DatasetName, name="ItemGroupDef_DatasetName", curie=ODM.curie('DatasetName'),
                   model_uri=ODM.ItemGroupDef_DatasetName, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_Domain = Slot(uri=ODM.Domain, name="ItemGroupDef_Domain", curie=ODM.curie('Domain'),
                   model_uri=ODM.ItemGroupDef_Domain, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_Type = Slot(uri=ODM.Type, name="ItemGroupDef_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.ItemGroupDef_Type, domain=ItemGroupDef, range=str)

slots.ItemGroupDef_Purpose = Slot(uri=ODM.Purpose, name="ItemGroupDef_Purpose", curie=ODM.curie('Purpose'),
                   model_uri=ODM.ItemGroupDef_Purpose, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_StandardOID = Slot(uri=ODM.StandardOID, name="ItemGroupDef_StandardOID", curie=ODM.curie('StandardOID'),
                   model_uri=ODM.ItemGroupDef_StandardOID, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_IsNonStandard = Slot(uri=ODM.IsNonStandard, name="ItemGroupDef_IsNonStandard", curie=ODM.curie('IsNonStandard'),
                   model_uri=ODM.ItemGroupDef_IsNonStandard, domain=ItemGroupDef, range=Optional[Union[str, "YesOnly"]])

slots.ItemGroupDef_HasNoData = Slot(uri=ODM.HasNoData, name="ItemGroupDef_HasNoData", curie=ODM.curie('HasNoData'),
                   model_uri=ODM.ItemGroupDef_HasNoData, domain=ItemGroupDef, range=Optional[Union[str, "YesOnly"]])

slots.ItemGroupDef_CommentOID = Slot(uri=ODM.CommentOID, name="ItemGroupDef_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.ItemGroupDef_CommentOID, domain=ItemGroupDef, range=Optional[str])

slots.ItemGroupDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="ItemGroupDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.ItemGroupDef_DescriptionRef, domain=ItemGroupDef, range=Optional[Union[dict, Description]])

slots.ItemGroupDef_ClassRef = Slot(uri=ODM.ClassRef, name="ItemGroupDef_ClassRef", curie=ODM.curie('ClassRef'),
                   model_uri=ODM.ItemGroupDef_ClassRef, domain=ItemGroupDef, range=Optional[Union[dict, "Class"]])

slots.ItemGroupDef_CodingRef = Slot(uri=ODM.CodingRef, name="ItemGroupDef_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.ItemGroupDef_CodingRef, domain=ItemGroupDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.ItemGroupDef_WorkflowRefRef = Slot(uri=ODM.WorkflowRefRef, name="ItemGroupDef_WorkflowRefRef", curie=ODM.curie('WorkflowRefRef'),
                   model_uri=ODM.ItemGroupDef_WorkflowRefRef, domain=ItemGroupDef, range=Optional[Union[dict, "WorkflowRef"]])

slots.ItemGroupDef_OriginRef = Slot(uri=ODM.OriginRef, name="ItemGroupDef_OriginRef", curie=ODM.curie('OriginRef'),
                   model_uri=ODM.ItemGroupDef_OriginRef, domain=ItemGroupDef, range=Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]])

slots.ItemGroupDef_AliasRef = Slot(uri=ODM.AliasRef, name="ItemGroupDef_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.ItemGroupDef_AliasRef, domain=ItemGroupDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.ItemGroupDef_LeafRef = Slot(uri=ODM.LeafRef, name="ItemGroupDef_LeafRef", curie=ODM.curie('LeafRef'),
                   model_uri=ODM.ItemGroupDef_LeafRef, domain=ItemGroupDef, range=Optional[Union[str, LeafID]])

slots.ItemGroupDef_ItemGroupRefRef = Slot(uri=ODM.ItemGroupRefRef, name="ItemGroupDef_ItemGroupRefRef", curie=ODM.curie('ItemGroupRefRef'),
                   model_uri=ODM.ItemGroupDef_ItemGroupRefRef, domain=ItemGroupDef, range=Optional[Union[Union[dict, ItemGroupRef], List[Union[dict, ItemGroupRef]]]])

slots.ItemGroupDef_ItemRefRef = Slot(uri=ODM.ItemRefRef, name="ItemGroupDef_ItemRefRef", curie=ODM.curie('ItemRefRef'),
                   model_uri=ODM.ItemGroupDef_ItemRefRef, domain=ItemGroupDef, range=Optional[Union[Union[dict, "ItemRef"], List[Union[dict, "ItemRef"]]]])

slots.Class_Name = Slot(uri=ODM.Name, name="Class_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Class_Name, domain=Class, range=Union[str, "ItemGroupClass"])

slots.Class_SubClassRef = Slot(uri=ODM.SubClassRef, name="Class_SubClassRef", curie=ODM.curie('SubClassRef'),
                   model_uri=ODM.Class_SubClassRef, domain=Class, range=Optional[Union[Union[dict, "SubClass"], List[Union[dict, "SubClass"]]]])

slots.SubClass_Name = Slot(uri=ODM.Name, name="SubClass_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.SubClass_Name, domain=SubClass, range=Union[str, "ItemGroupSubClass"])

slots.SubClass_ParentClass = Slot(uri=ODM.ParentClass, name="SubClass_ParentClass", curie=ODM.curie('ParentClass'),
                   model_uri=ODM.SubClass_ParentClass, domain=SubClass, range=Optional[str])

slots.ItemRef_ItemOID = Slot(uri=ODM.ItemOID, name="ItemRef_ItemOID", curie=ODM.curie('ItemOID'),
                   model_uri=ODM.ItemRef_ItemOID, domain=ItemRef, range=str)

slots.ItemRef_KeySequence = Slot(uri=ODM.KeySequence, name="ItemRef_KeySequence", curie=ODM.curie('KeySequence'),
                   model_uri=ODM.ItemRef_KeySequence, domain=ItemRef, range=Optional[int])

slots.ItemRef_IsNonStandard = Slot(uri=ODM.IsNonStandard, name="ItemRef_IsNonStandard", curie=ODM.curie('IsNonStandard'),
                   model_uri=ODM.ItemRef_IsNonStandard, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_HasNoData = Slot(uri=ODM.HasNoData, name="ItemRef_HasNoData", curie=ODM.curie('HasNoData'),
                   model_uri=ODM.ItemRef_HasNoData, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_MethodOID = Slot(uri=ODM.MethodOID, name="ItemRef_MethodOID", curie=ODM.curie('MethodOID'),
                   model_uri=ODM.ItemRef_MethodOID, domain=ItemRef, range=Optional[str])

slots.ItemRef_UnitsItemOID = Slot(uri=ODM.UnitsItemOID, name="ItemRef_UnitsItemOID", curie=ODM.curie('UnitsItemOID'),
                   model_uri=ODM.ItemRef_UnitsItemOID, domain=ItemRef, range=Optional[str])

slots.ItemRef_Repeat = Slot(uri=ODM.Repeat, name="ItemRef_Repeat", curie=ODM.curie('Repeat'),
                   model_uri=ODM.ItemRef_Repeat, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_Other = Slot(uri=ODM.Other, name="ItemRef_Other", curie=ODM.curie('Other'),
                   model_uri=ODM.ItemRef_Other, domain=ItemRef, range=Optional[Union[str, "YesOnly"]])

slots.ItemRef_Role = Slot(uri=ODM.Role, name="ItemRef_Role", curie=ODM.curie('Role'),
                   model_uri=ODM.ItemRef_Role, domain=ItemRef, range=Optional[str])

slots.ItemRef_RoleCodeListOID = Slot(uri=ODM.RoleCodeListOID, name="ItemRef_RoleCodeListOID", curie=ODM.curie('RoleCodeListOID'),
                   model_uri=ODM.ItemRef_RoleCodeListOID, domain=ItemRef, range=Optional[str])

slots.ItemRef_Core = Slot(uri=ODM.Core, name="ItemRef_Core", curie=ODM.curie('Core'),
                   model_uri=ODM.ItemRef_Core, domain=ItemRef, range=Optional[str])

slots.ItemRef_PreSpecifiedValue = Slot(uri=ODM.PreSpecifiedValue, name="ItemRef_PreSpecifiedValue", curie=ODM.curie('PreSpecifiedValue'),
                   model_uri=ODM.ItemRef_PreSpecifiedValue, domain=ItemRef, range=Optional[str])

slots.ItemRef_OrderNumber = Slot(uri=ODM.OrderNumber, name="ItemRef_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.ItemRef_OrderNumber, domain=ItemRef, range=Optional[int])

slots.ItemRef_Mandatory = Slot(uri=ODM.Mandatory, name="ItemRef_Mandatory", curie=ODM.curie('Mandatory'),
                   model_uri=ODM.ItemRef_Mandatory, domain=ItemRef, range=Union[str, "YesOrNo"])

slots.ItemRef_CollectionExceptionConditionOID = Slot(uri=ODM.CollectionExceptionConditionOID, name="ItemRef_CollectionExceptionConditionOID", curie=ODM.curie('CollectionExceptionConditionOID'),
                   model_uri=ODM.ItemRef_CollectionExceptionConditionOID, domain=ItemRef, range=Optional[str])

slots.ItemRef_OriginRef = Slot(uri=ODM.OriginRef, name="ItemRef_OriginRef", curie=ODM.curie('OriginRef'),
                   model_uri=ODM.ItemRef_OriginRef, domain=ItemRef, range=Optional[Union[Union[dict, "Origin"], List[Union[dict, "Origin"]]]])

slots.ItemRef_WhereClauseRefRef = Slot(uri=ODM.WhereClauseRefRef, name="ItemRef_WhereClauseRefRef", curie=ODM.curie('WhereClauseRefRef'),
                   model_uri=ODM.ItemRef_WhereClauseRefRef, domain=ItemRef, range=Optional[Union[Union[dict, WhereClauseRef], List[Union[dict, WhereClauseRef]]]])

slots.Origin_Type = Slot(uri=ODM.Type, name="Origin_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.Origin_Type, domain=Origin, range=Union[str, "OriginType"])

slots.Origin_Source = Slot(uri=ODM.Source, name="Origin_Source", curie=ODM.curie('Source'),
                   model_uri=ODM.Origin_Source, domain=Origin, range=Optional[Union[str, "OriginSource"]])

slots.Origin_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Origin_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Origin_DescriptionRef, domain=Origin, range=Optional[Union[dict, Description]])

slots.Origin_SourceItemsRef = Slot(uri=ODM.SourceItemsRef, name="Origin_SourceItemsRef", curie=ODM.curie('SourceItemsRef'),
                   model_uri=ODM.Origin_SourceItemsRef, domain=Origin, range=Optional[Union[dict, "SourceItems"]])

slots.Origin_CodingRef = Slot(uri=ODM.CodingRef, name="Origin_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.Origin_CodingRef, domain=Origin, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Origin_DocumentRefRef = Slot(uri=ODM.DocumentRefRef, name="Origin_DocumentRefRef", curie=ODM.curie('DocumentRefRef'),
                   model_uri=ODM.Origin_DocumentRefRef, domain=Origin, range=Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]])

slots.SourceItems_SourceItemRef = Slot(uri=ODM.SourceItemRef, name="SourceItems_SourceItemRef", curie=ODM.curie('SourceItemRef'),
                   model_uri=ODM.SourceItems_SourceItemRef, domain=SourceItems, range=Optional[Union[Dict[Union[str, SourceItemLeafID], Union[dict, "SourceItem"]], List[Union[dict, "SourceItem"]]]])

slots.SourceItems_CodingRef = Slot(uri=ODM.CodingRef, name="SourceItems_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.SourceItems_CodingRef, domain=SourceItems, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.SourceItem_ItemOID = Slot(uri=ODM.ItemOID, name="SourceItem_ItemOID", curie=ODM.curie('ItemOID'),
                   model_uri=ODM.SourceItem_ItemOID, domain=SourceItem, range=Optional[str])

slots.SourceItem_ItemGroupOID = Slot(uri=ODM.ItemGroupOID, name="SourceItem_ItemGroupOID", curie=ODM.curie('ItemGroupOID'),
                   model_uri=ODM.SourceItem_ItemGroupOID, domain=SourceItem, range=Optional[str])

slots.SourceItem_MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="SourceItem_MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.SourceItem_MetaDataVersionOID, domain=SourceItem, range=Optional[str])

slots.SourceItem_StudyOID = Slot(uri=ODM.StudyOID, name="SourceItem_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.SourceItem_StudyOID, domain=SourceItem, range=Optional[str])

slots.SourceItem_leafID = Slot(uri=ODM.leafID, name="SourceItem_leafID", curie=ODM.curie('leafID'),
                   model_uri=ODM.SourceItem_leafID, domain=SourceItem, range=Union[str, SourceItemLeafID])

slots.SourceItem_Name = Slot(uri=ODM.Name, name="SourceItem_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.SourceItem_Name, domain=SourceItem, range=Optional[str])

slots.SourceItem_ResourceRef = Slot(uri=ODM.ResourceRef, name="SourceItem_ResourceRef", curie=ODM.curie('ResourceRef'),
                   model_uri=ODM.SourceItem_ResourceRef, domain=SourceItem, range=Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]])

slots.SourceItem_CodingRef = Slot(uri=ODM.CodingRef, name="SourceItem_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.SourceItem_CodingRef, domain=SourceItem, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Resource_Type = Slot(uri=ODM.Type, name="Resource_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.Resource_Type, domain=Resource, range=str)

slots.Resource_Name = Slot(uri=ODM.Name, name="Resource_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Resource_Name, domain=Resource, range=str)

slots.Resource_Attribute = Slot(uri=ODM.Attribute, name="Resource_Attribute", curie=ODM.curie('Attribute'),
                   model_uri=ODM.Resource_Attribute, domain=Resource, range=Optional[str])

slots.Resource_Label = Slot(uri=ODM.Label, name="Resource_Label", curie=ODM.curie('Label'),
                   model_uri=ODM.Resource_Label, domain=Resource, range=Optional[str])

slots.Resource_SelectionRef = Slot(uri=ODM.SelectionRef, name="Resource_SelectionRef", curie=ODM.curie('SelectionRef'),
                   model_uri=ODM.Resource_SelectionRef, domain=Resource, range=Optional[Union[Union[dict, "Selection"], List[Union[dict, "Selection"]]]])

slots.Selection_Path = Slot(uri=ODM.Path, name="Selection_Path", curie=ODM.curie('Path'),
                   model_uri=ODM.Selection_Path, domain=Selection, range=str)

slots.ItemDef_OID = Slot(uri=ODM.OID, name="ItemDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ItemDef_OID, domain=ItemDef, range=Union[str, ItemDefOID])

slots.ItemDef_Name = Slot(uri=ODM.Name, name="ItemDef_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.ItemDef_Name, domain=ItemDef, range=str)

slots.ItemDef_DataTypeRef = Slot(uri=ODM.DataTypeRef, name="ItemDef_DataTypeRef", curie=ODM.curie('DataTypeRef'),
                   model_uri=ODM.ItemDef_DataTypeRef, domain=ItemDef, range=Union[str, "DataType"])

slots.ItemDef_Length = Slot(uri=ODM.Length, name="ItemDef_Length", curie=ODM.curie('Length'),
                   model_uri=ODM.ItemDef_Length, domain=ItemDef, range=Optional[int])

slots.ItemDef_DisplayFormat = Slot(uri=ODM.DisplayFormat, name="ItemDef_DisplayFormat", curie=ODM.curie('DisplayFormat'),
                   model_uri=ODM.ItemDef_DisplayFormat, domain=ItemDef, range=Optional[str])

slots.ItemDef_VariableSet = Slot(uri=ODM.VariableSet, name="ItemDef_VariableSet", curie=ODM.curie('VariableSet'),
                   model_uri=ODM.ItemDef_VariableSet, domain=ItemDef, range=Optional[str])

slots.ItemDef_CommentOID = Slot(uri=ODM.CommentOID, name="ItemDef_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.ItemDef_CommentOID, domain=ItemDef, range=Optional[str])

slots.ItemDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="ItemDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.ItemDef_DescriptionRef, domain=ItemDef, range=Optional[Union[dict, Description]])

slots.ItemDef_DefinitionRef = Slot(uri=ODM.DefinitionRef, name="ItemDef_DefinitionRef", curie=ODM.curie('DefinitionRef'),
                   model_uri=ODM.ItemDef_DefinitionRef, domain=ItemDef, range=Optional[Union[dict, "Definition"]])

slots.ItemDef_QuestionRef = Slot(uri=ODM.QuestionRef, name="ItemDef_QuestionRef", curie=ODM.curie('QuestionRef'),
                   model_uri=ODM.ItemDef_QuestionRef, domain=ItemDef, range=Optional[Union[dict, "Question"]])

slots.ItemDef_PromptRef = Slot(uri=ODM.PromptRef, name="ItemDef_PromptRef", curie=ODM.curie('PromptRef'),
                   model_uri=ODM.ItemDef_PromptRef, domain=ItemDef, range=Optional[Union[dict, "Prompt"]])

slots.ItemDef_CRFCompletionInstructionsRef = Slot(uri=ODM.CRFCompletionInstructionsRef, name="ItemDef_CRFCompletionInstructionsRef", curie=ODM.curie('CRFCompletionInstructionsRef'),
                   model_uri=ODM.ItemDef_CRFCompletionInstructionsRef, domain=ItemDef, range=Optional[Union[dict, "CRFCompletionInstructions"]])

slots.ItemDef_ImplementationNotesRef = Slot(uri=ODM.ImplementationNotesRef, name="ItemDef_ImplementationNotesRef", curie=ODM.curie('ImplementationNotesRef'),
                   model_uri=ODM.ItemDef_ImplementationNotesRef, domain=ItemDef, range=Optional[Union[dict, "ImplementationNotes"]])

slots.ItemDef_CDISCNotesRef = Slot(uri=ODM.CDISCNotesRef, name="ItemDef_CDISCNotesRef", curie=ODM.curie('CDISCNotesRef'),
                   model_uri=ODM.ItemDef_CDISCNotesRef, domain=ItemDef, range=Optional[Union[dict, "CDISCNotes"]])

slots.ItemDef_RangeCheckRef = Slot(uri=ODM.RangeCheckRef, name="ItemDef_RangeCheckRef", curie=ODM.curie('RangeCheckRef'),
                   model_uri=ODM.ItemDef_RangeCheckRef, domain=ItemDef, range=Optional[Union[Union[dict, "RangeCheck"], List[Union[dict, "RangeCheck"]]]])

slots.ItemDef_CodeListRefRef = Slot(uri=ODM.CodeListRefRef, name="ItemDef_CodeListRefRef", curie=ODM.curie('CodeListRefRef'),
                   model_uri=ODM.ItemDef_CodeListRefRef, domain=ItemDef, range=Optional[Union[dict, "CodeListRef"]])

slots.ItemDef_ValueListRefRef = Slot(uri=ODM.ValueListRefRef, name="ItemDef_ValueListRefRef", curie=ODM.curie('ValueListRefRef'),
                   model_uri=ODM.ItemDef_ValueListRefRef, domain=ItemDef, range=Optional[Union[dict, "ValueListRef"]])

slots.ItemDef_CodingRef = Slot(uri=ODM.CodingRef, name="ItemDef_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.ItemDef_CodingRef, domain=ItemDef, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.ItemDef_AliasRef = Slot(uri=ODM.AliasRef, name="ItemDef_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.ItemDef_AliasRef, domain=ItemDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.Question_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="Question_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.Question_TranslatedTextRef, domain=Question, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.Definition_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="Definition_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.Definition_TranslatedTextRef, domain=Definition, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.Prompt_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="Prompt_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.Prompt_TranslatedTextRef, domain=Prompt, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.CRFCompletionInstructions_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="CRFCompletionInstructions_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.CRFCompletionInstructions_TranslatedTextRef, domain=CRFCompletionInstructions, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.ImplementationNotes_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="ImplementationNotes_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.ImplementationNotes_TranslatedTextRef, domain=ImplementationNotes, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.CDISCNotes_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="CDISCNotes_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.CDISCNotes_TranslatedTextRef, domain=CDISCNotes, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.RangeCheck_ComparatorRef = Slot(uri=ODM.ComparatorRef, name="RangeCheck_ComparatorRef", curie=ODM.curie('ComparatorRef'),
                   model_uri=ODM.RangeCheck_ComparatorRef, domain=RangeCheck, range=Optional[Union[str, "Comparator"]])

slots.RangeCheck_SoftHard = Slot(uri=ODM.SoftHard, name="RangeCheck_SoftHard", curie=ODM.curie('SoftHard'),
                   model_uri=ODM.RangeCheck_SoftHard, domain=RangeCheck, range=Optional[Union[str, "SoftOrHard"]])

slots.RangeCheck_ItemOID = Slot(uri=ODM.ItemOID, name="RangeCheck_ItemOID", curie=ODM.curie('ItemOID'),
                   model_uri=ODM.RangeCheck_ItemOID, domain=RangeCheck, range=Optional[str])

slots.RangeCheck_ErrorMessageRef = Slot(uri=ODM.ErrorMessageRef, name="RangeCheck_ErrorMessageRef", curie=ODM.curie('ErrorMessageRef'),
                   model_uri=ODM.RangeCheck_ErrorMessageRef, domain=RangeCheck, range=Optional[Union[dict, "ErrorMessage"]])

slots.RangeCheck_MethodSignatureRef = Slot(uri=ODM.MethodSignatureRef, name="RangeCheck_MethodSignatureRef", curie=ODM.curie('MethodSignatureRef'),
                   model_uri=ODM.RangeCheck_MethodSignatureRef, domain=RangeCheck, range=Optional[Union[dict, "MethodSignature"]])

slots.RangeCheck_FormalExpressionRef = Slot(uri=ODM.FormalExpressionRef, name="RangeCheck_FormalExpressionRef", curie=ODM.curie('FormalExpressionRef'),
                   model_uri=ODM.RangeCheck_FormalExpressionRef, domain=RangeCheck, range=Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]])

slots.RangeCheck_CheckValueRef = Slot(uri=ODM.CheckValueRef, name="RangeCheck_CheckValueRef", curie=ODM.curie('CheckValueRef'),
                   model_uri=ODM.RangeCheck_CheckValueRef, domain=RangeCheck, range=Optional[Union[Union[dict, "CheckValue"], List[Union[dict, "CheckValue"]]]])

slots.CheckValue_range = Slot(uri=ODM.range, name="CheckValue_range", curie=ODM.curie('range'),
                   model_uri=ODM.CheckValue_range, domain=CheckValue, range=Optional[str])

slots.ErrorMessage_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="ErrorMessage_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.ErrorMessage_TranslatedTextRef, domain=ErrorMessage, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.CodeListRef_CodeListOID = Slot(uri=ODM.CodeListOID, name="CodeListRef_CodeListOID", curie=ODM.curie('CodeListOID'),
                   model_uri=ODM.CodeListRef_CodeListOID, domain=CodeListRef, range=str)

slots.ValueListRef_ValueListOID = Slot(uri=ODM.ValueListOID, name="ValueListRef_ValueListOID", curie=ODM.curie('ValueListOID'),
                   model_uri=ODM.ValueListRef_ValueListOID, domain=ValueListRef, range=str)

slots.CodeList_OID = Slot(uri=ODM.OID, name="CodeList_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.CodeList_OID, domain=CodeList, range=Union[str, CodeListOID])

slots.CodeList_Name = Slot(uri=ODM.Name, name="CodeList_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.CodeList_Name, domain=CodeList, range=str)

slots.CodeList_DataTypeRef = Slot(uri=ODM.DataTypeRef, name="CodeList_DataTypeRef", curie=ODM.curie('DataTypeRef'),
                   model_uri=ODM.CodeList_DataTypeRef, domain=CodeList, range=Union[str, "CLDataType"])

slots.CodeList_CommentOID = Slot(uri=ODM.CommentOID, name="CodeList_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.CodeList_CommentOID, domain=CodeList, range=Optional[str])

slots.CodeList_StandardOID = Slot(uri=ODM.StandardOID, name="CodeList_StandardOID", curie=ODM.curie('StandardOID'),
                   model_uri=ODM.CodeList_StandardOID, domain=CodeList, range=Optional[str])

slots.CodeList_IsNonStandard = Slot(uri=ODM.IsNonStandard, name="CodeList_IsNonStandard", curie=ODM.curie('IsNonStandard'),
                   model_uri=ODM.CodeList_IsNonStandard, domain=CodeList, range=Optional[Union[str, "YesOnly"]])

slots.CodeList_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="CodeList_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.CodeList_DescriptionRef, domain=CodeList, range=Optional[Union[dict, Description]])

slots.CodeList_CodeListItemRef = Slot(uri=ODM.CodeListItemRef, name="CodeList_CodeListItemRef", curie=ODM.curie('CodeListItemRef'),
                   model_uri=ODM.CodeList_CodeListItemRef, domain=CodeList, range=Optional[Union[Union[dict, "CodeListItem"], List[Union[dict, "CodeListItem"]]]])

slots.CodeList_CodingRef = Slot(uri=ODM.CodingRef, name="CodeList_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.CodeList_CodingRef, domain=CodeList, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.CodeList_AliasRef = Slot(uri=ODM.AliasRef, name="CodeList_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.CodeList_AliasRef, domain=CodeList, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.CodeListItem_CodedValue = Slot(uri=ODM.CodedValue, name="CodeListItem_CodedValue", curie=ODM.curie('CodedValue'),
                   model_uri=ODM.CodeListItem_CodedValue, domain=CodeListItem, range=str)

slots.CodeListItem_Rank = Slot(uri=ODM.Rank, name="CodeListItem_Rank", curie=ODM.curie('Rank'),
                   model_uri=ODM.CodeListItem_Rank, domain=CodeListItem, range=Optional[Decimal])

slots.CodeListItem_Other = Slot(uri=ODM.Other, name="CodeListItem_Other", curie=ODM.curie('Other'),
                   model_uri=ODM.CodeListItem_Other, domain=CodeListItem, range=Optional[Union[str, "YesOnly"]])

slots.CodeListItem_OrderNumber = Slot(uri=ODM.OrderNumber, name="CodeListItem_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.CodeListItem_OrderNumber, domain=CodeListItem, range=Optional[int])

slots.CodeListItem_ExtendedValue = Slot(uri=ODM.ExtendedValue, name="CodeListItem_ExtendedValue", curie=ODM.curie('ExtendedValue'),
                   model_uri=ODM.CodeListItem_ExtendedValue, domain=CodeListItem, range=Optional[Union[str, "YesOnly"]])

slots.CodeListItem_CommentOID = Slot(uri=ODM.CommentOID, name="CodeListItem_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.CodeListItem_CommentOID, domain=CodeListItem, range=Optional[str])

slots.CodeListItem_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="CodeListItem_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.CodeListItem_DescriptionRef, domain=CodeListItem, range=Optional[Union[dict, Description]])

slots.CodeListItem_DecodeRef = Slot(uri=ODM.DecodeRef, name="CodeListItem_DecodeRef", curie=ODM.curie('DecodeRef'),
                   model_uri=ODM.CodeListItem_DecodeRef, domain=CodeListItem, range=Optional[Union[dict, "Decode"]])

slots.CodeListItem_CodingRef = Slot(uri=ODM.CodingRef, name="CodeListItem_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.CodeListItem_CodingRef, domain=CodeListItem, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.CodeListItem_AliasRef = Slot(uri=ODM.AliasRef, name="CodeListItem_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.CodeListItem_AliasRef, domain=CodeListItem, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.Decode_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="Decode_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.Decode_TranslatedTextRef, domain=Decode, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.MethodDef_OID = Slot(uri=ODM.OID, name="MethodDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.MethodDef_OID, domain=MethodDef, range=Union[str, MethodDefOID])

slots.MethodDef_Name = Slot(uri=ODM.Name, name="MethodDef_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.MethodDef_Name, domain=MethodDef, range=str)

slots.MethodDef_Type = Slot(uri=ODM.Type, name="MethodDef_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.MethodDef_Type, domain=MethodDef, range=Optional[Union[str, "MethodType"]])

slots.MethodDef_CommentOID = Slot(uri=ODM.CommentOID, name="MethodDef_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.MethodDef_CommentOID, domain=MethodDef, range=Optional[str])

slots.MethodDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="MethodDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.MethodDef_DescriptionRef, domain=MethodDef, range=Optional[Union[dict, Description]])

slots.MethodDef_MethodSignatureRef = Slot(uri=ODM.MethodSignatureRef, name="MethodDef_MethodSignatureRef", curie=ODM.curie('MethodSignatureRef'),
                   model_uri=ODM.MethodDef_MethodSignatureRef, domain=MethodDef, range=Optional[Union[dict, "MethodSignature"]])

slots.MethodDef_FormalExpressionRef = Slot(uri=ODM.FormalExpressionRef, name="MethodDef_FormalExpressionRef", curie=ODM.curie('FormalExpressionRef'),
                   model_uri=ODM.MethodDef_FormalExpressionRef, domain=MethodDef, range=Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]])

slots.MethodDef_AliasRef = Slot(uri=ODM.AliasRef, name="MethodDef_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.MethodDef_AliasRef, domain=MethodDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.MethodDef_DocumentRefRef = Slot(uri=ODM.DocumentRefRef, name="MethodDef_DocumentRefRef", curie=ODM.curie('DocumentRefRef'),
                   model_uri=ODM.MethodDef_DocumentRefRef, domain=MethodDef, range=Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]])

slots.MethodSignature_ParameterRef = Slot(uri=ODM.ParameterRef, name="MethodSignature_ParameterRef", curie=ODM.curie('ParameterRef'),
                   model_uri=ODM.MethodSignature_ParameterRef, domain=MethodSignature, range=Optional[Union[Union[dict, "Parameter"], List[Union[dict, "Parameter"]]]])

slots.MethodSignature_ReturnValueRef = Slot(uri=ODM.ReturnValueRef, name="MethodSignature_ReturnValueRef", curie=ODM.curie('ReturnValueRef'),
                   model_uri=ODM.MethodSignature_ReturnValueRef, domain=MethodSignature, range=Optional[Union[Union[dict, "ReturnValue"], List[Union[dict, "ReturnValue"]]]])

slots.Parameter_Name = Slot(uri=ODM.Name, name="Parameter_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Parameter_Name, domain=Parameter, range=str)

slots.Parameter_DataTypeRef = Slot(uri=ODM.DataTypeRef, name="Parameter_DataTypeRef", curie=ODM.curie('DataTypeRef'),
                   model_uri=ODM.Parameter_DataTypeRef, domain=Parameter, range=Union[str, "DataType"])

slots.Parameter_DefinitionRef = Slot(uri=ODM.DefinitionRef, name="Parameter_DefinitionRef", curie=ODM.curie('DefinitionRef'),
                   model_uri=ODM.Parameter_DefinitionRef, domain=Parameter, range=Optional[str])

slots.Parameter_OrderNumber = Slot(uri=ODM.OrderNumber, name="Parameter_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.Parameter_OrderNumber, domain=Parameter, range=Optional[int])

slots.ReturnValue_Name = Slot(uri=ODM.Name, name="ReturnValue_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.ReturnValue_Name, domain=ReturnValue, range=str)

slots.ReturnValue_DataTypeRef = Slot(uri=ODM.DataTypeRef, name="ReturnValue_DataTypeRef", curie=ODM.curie('DataTypeRef'),
                   model_uri=ODM.ReturnValue_DataTypeRef, domain=ReturnValue, range=Union[str, "DataType"])

slots.ReturnValue_DefinitionRef = Slot(uri=ODM.DefinitionRef, name="ReturnValue_DefinitionRef", curie=ODM.curie('DefinitionRef'),
                   model_uri=ODM.ReturnValue_DefinitionRef, domain=ReturnValue, range=Optional[str])

slots.ReturnValue_OrderNumber = Slot(uri=ODM.OrderNumber, name="ReturnValue_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.ReturnValue_OrderNumber, domain=ReturnValue, range=Optional[int])

slots.ConditionDef_OID = Slot(uri=ODM.OID, name="ConditionDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.ConditionDef_OID, domain=ConditionDef, range=Union[str, ConditionDefOID])

slots.ConditionDef_Name = Slot(uri=ODM.Name, name="ConditionDef_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.ConditionDef_Name, domain=ConditionDef, range=str)

slots.ConditionDef_CommentOID = Slot(uri=ODM.CommentOID, name="ConditionDef_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.ConditionDef_CommentOID, domain=ConditionDef, range=Optional[str])

slots.ConditionDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="ConditionDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.ConditionDef_DescriptionRef, domain=ConditionDef, range=Optional[Union[dict, Description]])

slots.ConditionDef_MethodSignatureRef = Slot(uri=ODM.MethodSignatureRef, name="ConditionDef_MethodSignatureRef", curie=ODM.curie('MethodSignatureRef'),
                   model_uri=ODM.ConditionDef_MethodSignatureRef, domain=ConditionDef, range=Optional[Union[dict, MethodSignature]])

slots.ConditionDef_FormalExpressionRef = Slot(uri=ODM.FormalExpressionRef, name="ConditionDef_FormalExpressionRef", curie=ODM.curie('FormalExpressionRef'),
                   model_uri=ODM.ConditionDef_FormalExpressionRef, domain=ConditionDef, range=Optional[Union[Union[dict, "FormalExpression"], List[Union[dict, "FormalExpression"]]]])

slots.ConditionDef_AliasRef = Slot(uri=ODM.AliasRef, name="ConditionDef_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.ConditionDef_AliasRef, domain=ConditionDef, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.FormalExpression_ContextRef = Slot(uri=ODM.ContextRef, name="FormalExpression_ContextRef", curie=ODM.curie('ContextRef'),
                   model_uri=ODM.FormalExpression_ContextRef, domain=FormalExpression, range=Optional[str])

slots.FormalExpression_CodeRef = Slot(uri=ODM.CodeRef, name="FormalExpression_CodeRef", curie=ODM.curie('CodeRef'),
                   model_uri=ODM.FormalExpression_CodeRef, domain=FormalExpression, range=Optional[Union[dict, "Code"]])

slots.FormalExpression_ExternalCodeLibRef = Slot(uri=ODM.ExternalCodeLibRef, name="FormalExpression_ExternalCodeLibRef", curie=ODM.curie('ExternalCodeLibRef'),
                   model_uri=ODM.FormalExpression_ExternalCodeLibRef, domain=FormalExpression, range=Optional[Union[dict, "ExternalCodeLib"]])

slots.Code_range = Slot(uri=ODM.range, name="Code_range", curie=ODM.curie('range'),
                   model_uri=ODM.Code_range, domain=Code, range=Optional[str])

slots.ExternalCodeLib_Library = Slot(uri=ODM.Library, name="ExternalCodeLib_Library", curie=ODM.curie('Library'),
                   model_uri=ODM.ExternalCodeLib_Library, domain=ExternalCodeLib, range=str)

slots.ExternalCodeLib_Method = Slot(uri=ODM.Method, name="ExternalCodeLib_Method", curie=ODM.curie('Method'),
                   model_uri=ODM.ExternalCodeLib_Method, domain=ExternalCodeLib, range=Optional[str])

slots.ExternalCodeLib_Version = Slot(uri=ODM.Version, name="ExternalCodeLib_Version", curie=ODM.curie('Version'),
                   model_uri=ODM.ExternalCodeLib_Version, domain=ExternalCodeLib, range=Optional[str])

slots.ExternalCodeLib_ref = Slot(uri=ODM.ref, name="ExternalCodeLib_ref", curie=ODM.curie('ref'),
                   model_uri=ODM.ExternalCodeLib_ref, domain=ExternalCodeLib, range=Optional[str])

slots.ExternalCodeLib_href = Slot(uri=ODM.href, name="ExternalCodeLib_href", curie=ODM.curie('href'),
                   model_uri=ODM.ExternalCodeLib_href, domain=ExternalCodeLib, range=Optional[Union[str, URIorCURIE]])

slots.CommentDef_OID = Slot(uri=ODM.OID, name="CommentDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.CommentDef_OID, domain=CommentDef, range=Union[str, CommentDefOID])

slots.CommentDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="CommentDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.CommentDef_DescriptionRef, domain=CommentDef, range=Optional[Union[dict, Description]])

slots.CommentDef_DocumentRefRef = Slot(uri=ODM.DocumentRefRef, name="CommentDef_DocumentRefRef", curie=ODM.curie('DocumentRefRef'),
                   model_uri=ODM.CommentDef_DocumentRefRef, domain=CommentDef, range=Optional[Union[Union[dict, DocumentRef], List[Union[dict, DocumentRef]]]])

slots.Protocol_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Protocol_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Protocol_DescriptionRef, domain=Protocol, range=Optional[Union[dict, Description]])

slots.Protocol_StudySummaryRef = Slot(uri=ODM.StudySummaryRef, name="Protocol_StudySummaryRef", curie=ODM.curie('StudySummaryRef'),
                   model_uri=ODM.Protocol_StudySummaryRef, domain=Protocol, range=Optional[Union[dict, "StudySummary"]])

slots.Protocol_StudyStructureRef = Slot(uri=ODM.StudyStructureRef, name="Protocol_StudyStructureRef", curie=ODM.curie('StudyStructureRef'),
                   model_uri=ODM.Protocol_StudyStructureRef, domain=Protocol, range=Optional[Union[dict, "StudyStructure"]])

slots.Protocol_TrialPhaseRef = Slot(uri=ODM.TrialPhaseRef, name="Protocol_TrialPhaseRef", curie=ODM.curie('TrialPhaseRef'),
                   model_uri=ODM.Protocol_TrialPhaseRef, domain=Protocol, range=Optional[Union[dict, "TrialPhase"]])

slots.Protocol_StudyTimingsRef = Slot(uri=ODM.StudyTimingsRef, name="Protocol_StudyTimingsRef", curie=ODM.curie('StudyTimingsRef'),
                   model_uri=ODM.Protocol_StudyTimingsRef, domain=Protocol, range=Optional[Union[dict, "StudyTimings"]])

slots.Protocol_StudyIndicationsRef = Slot(uri=ODM.StudyIndicationsRef, name="Protocol_StudyIndicationsRef", curie=ODM.curie('StudyIndicationsRef'),
                   model_uri=ODM.Protocol_StudyIndicationsRef, domain=Protocol, range=Optional[Union[dict, "StudyIndications"]])

slots.Protocol_StudyInterventionsRef = Slot(uri=ODM.StudyInterventionsRef, name="Protocol_StudyInterventionsRef", curie=ODM.curie('StudyInterventionsRef'),
                   model_uri=ODM.Protocol_StudyInterventionsRef, domain=Protocol, range=Optional[Union[dict, "StudyInterventions"]])

slots.Protocol_StudyObjectivesRef = Slot(uri=ODM.StudyObjectivesRef, name="Protocol_StudyObjectivesRef", curie=ODM.curie('StudyObjectivesRef'),
                   model_uri=ODM.Protocol_StudyObjectivesRef, domain=Protocol, range=Optional[Union[dict, "StudyObjectives"]])

slots.Protocol_StudyEndPointsRef = Slot(uri=ODM.StudyEndPointsRef, name="Protocol_StudyEndPointsRef", curie=ODM.curie('StudyEndPointsRef'),
                   model_uri=ODM.Protocol_StudyEndPointsRef, domain=Protocol, range=Optional[Union[dict, "StudyEndPoints"]])

slots.Protocol_StudyTargetPopulationRefRef = Slot(uri=ODM.StudyTargetPopulationRefRef, name="Protocol_StudyTargetPopulationRefRef", curie=ODM.curie('StudyTargetPopulationRefRef'),
                   model_uri=ODM.Protocol_StudyTargetPopulationRefRef, domain=Protocol, range=Optional[Union[str, StudyTargetPopulationOID]])

slots.Protocol_StudyEstimandsRef = Slot(uri=ODM.StudyEstimandsRef, name="Protocol_StudyEstimandsRef", curie=ODM.curie('StudyEstimandsRef'),
                   model_uri=ODM.Protocol_StudyEstimandsRef, domain=Protocol, range=Optional[Union[dict, "StudyEstimands"]])

slots.Protocol_InclusionExclusionCriteriaRef = Slot(uri=ODM.InclusionExclusionCriteriaRef, name="Protocol_InclusionExclusionCriteriaRef", curie=ODM.curie('InclusionExclusionCriteriaRef'),
                   model_uri=ODM.Protocol_InclusionExclusionCriteriaRef, domain=Protocol, range=Optional[Union[dict, "InclusionExclusionCriteria"]])

slots.Protocol_StudyEventGroupRefRef = Slot(uri=ODM.StudyEventGroupRefRef, name="Protocol_StudyEventGroupRefRef", curie=ODM.curie('StudyEventGroupRefRef'),
                   model_uri=ODM.Protocol_StudyEventGroupRefRef, domain=Protocol, range=Optional[Union[Union[dict, StudyEventGroupRef], List[Union[dict, StudyEventGroupRef]]]])

slots.Protocol_WorkflowRefRef = Slot(uri=ODM.WorkflowRefRef, name="Protocol_WorkflowRefRef", curie=ODM.curie('WorkflowRefRef'),
                   model_uri=ODM.Protocol_WorkflowRefRef, domain=Protocol, range=Optional[Union[dict, "WorkflowRef"]])

slots.Protocol_AliasRef = Slot(uri=ODM.AliasRef, name="Protocol_AliasRef", curie=ODM.curie('AliasRef'),
                   model_uri=ODM.Protocol_AliasRef, domain=Protocol, range=Optional[Union[Union[dict, Alias], List[Union[dict, Alias]]]])

slots.StudyStructure_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyStructure_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyStructure_DescriptionRef, domain=StudyStructure, range=Optional[Union[dict, Description]])

slots.StudyStructure_ArmRef = Slot(uri=ODM.ArmRef, name="StudyStructure_ArmRef", curie=ODM.curie('ArmRef'),
                   model_uri=ODM.StudyStructure_ArmRef, domain=StudyStructure, range=Optional[Union[Dict[Union[str, ArmOID], Union[dict, "Arm"]], List[Union[dict, "Arm"]]]])

slots.StudyStructure_EpochRef = Slot(uri=ODM.EpochRef, name="StudyStructure_EpochRef", curie=ODM.curie('EpochRef'),
                   model_uri=ODM.StudyStructure_EpochRef, domain=StudyStructure, range=Optional[Union[Dict[Union[str, EpochOID], Union[dict, "Epoch"]], List[Union[dict, "Epoch"]]]])

slots.StudyStructure_WorkflowRefRef = Slot(uri=ODM.WorkflowRefRef, name="StudyStructure_WorkflowRefRef", curie=ODM.curie('WorkflowRefRef'),
                   model_uri=ODM.StudyStructure_WorkflowRefRef, domain=StudyStructure, range=Optional[Union[dict, "WorkflowRef"]])

slots.TrialPhase_ValueRef = Slot(uri=ODM.ValueRef, name="TrialPhase_ValueRef", curie=ODM.curie('ValueRef'),
                   model_uri=ODM.TrialPhase_ValueRef, domain=TrialPhase, range=str)

slots.TrialPhase_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="TrialPhase_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.TrialPhase_DescriptionRef, domain=TrialPhase, range=Optional[Union[dict, Description]])

slots.StudyIndications_StudyIndicationRef = Slot(uri=ODM.StudyIndicationRef, name="StudyIndications_StudyIndicationRef", curie=ODM.curie('StudyIndicationRef'),
                   model_uri=ODM.StudyIndications_StudyIndicationRef, domain=StudyIndications, range=Optional[Union[Dict[Union[str, StudyIndicationOID], Union[dict, "StudyIndication"]], List[Union[dict, "StudyIndication"]]]])

slots.StudyIndication_OID = Slot(uri=ODM.OID, name="StudyIndication_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyIndication_OID, domain=StudyIndication, range=Union[str, StudyIndicationOID])

slots.StudyIndication_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyIndication_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyIndication_DescriptionRef, domain=StudyIndication, range=Optional[Union[dict, Description]])

slots.StudyIndication_CodingRef = Slot(uri=ODM.CodingRef, name="StudyIndication_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.StudyIndication_CodingRef, domain=StudyIndication, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyInterventions_StudyInterventionRefRef = Slot(uri=ODM.StudyInterventionRefRef, name="StudyInterventions_StudyInterventionRefRef", curie=ODM.curie('StudyInterventionRefRef'),
                   model_uri=ODM.StudyInterventions_StudyInterventionRefRef, domain=StudyInterventions, range=Optional[Union[Dict[Union[str, StudyInterventionOID], Union[dict, "StudyIntervention"]], List[Union[dict, "StudyIntervention"]]]])

slots.StudyIntervention_OID = Slot(uri=ODM.OID, name="StudyIntervention_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyIntervention_OID, domain=StudyIntervention, range=Union[str, StudyInterventionOID])

slots.StudyIntervention_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyIntervention_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyIntervention_DescriptionRef, domain=StudyIntervention, range=Optional[Union[dict, Description]])

slots.StudyIntervention_CodingRef = Slot(uri=ODM.CodingRef, name="StudyIntervention_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.StudyIntervention_CodingRef, domain=StudyIntervention, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyObjectives_StudyObjectiveRef = Slot(uri=ODM.StudyObjectiveRef, name="StudyObjectives_StudyObjectiveRef", curie=ODM.curie('StudyObjectiveRef'),
                   model_uri=ODM.StudyObjectives_StudyObjectiveRef, domain=StudyObjectives, range=Optional[Union[Dict[Union[str, StudyObjectiveOID], Union[dict, "StudyObjective"]], List[Union[dict, "StudyObjective"]]]])

slots.StudyObjective_OID = Slot(uri=ODM.OID, name="StudyObjective_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyObjective_OID, domain=StudyObjective, range=Union[str, StudyObjectiveOID])

slots.StudyObjective_Name = Slot(uri=ODM.Name, name="StudyObjective_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.StudyObjective_Name, domain=StudyObjective, range=str)

slots.StudyObjective_Level = Slot(uri=ODM.Level, name="StudyObjective_Level", curie=ODM.curie('Level'),
                   model_uri=ODM.StudyObjective_Level, domain=StudyObjective, range=Optional[Union[str, "StudyObjectiveLevel"]])

slots.StudyObjective_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyObjective_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyObjective_DescriptionRef, domain=StudyObjective, range=Optional[Union[dict, Description]])

slots.StudyObjective_StudyEndPointRefRef = Slot(uri=ODM.StudyEndPointRefRef, name="StudyObjective_StudyEndPointRefRef", curie=ODM.curie('StudyEndPointRefRef'),
                   model_uri=ODM.StudyObjective_StudyEndPointRefRef, domain=StudyObjective, range=Optional[Union[Union[dict, "StudyEndPointRef"], List[Union[dict, "StudyEndPointRef"]]]])

slots.StudyEndPointRef_StudyEndPointOID = Slot(uri=ODM.StudyEndPointOID, name="StudyEndPointRef_StudyEndPointOID", curie=ODM.curie('StudyEndPointOID'),
                   model_uri=ODM.StudyEndPointRef_StudyEndPointOID, domain=StudyEndPointRef, range=str)

slots.StudyEndPointRef_OrderNumber = Slot(uri=ODM.OrderNumber, name="StudyEndPointRef_OrderNumber", curie=ODM.curie('OrderNumber'),
                   model_uri=ODM.StudyEndPointRef_OrderNumber, domain=StudyEndPointRef, range=Optional[int])

slots.StudyEndPoints_StudyEndPointRefRef = Slot(uri=ODM.StudyEndPointRefRef, name="StudyEndPoints_StudyEndPointRefRef", curie=ODM.curie('StudyEndPointRefRef'),
                   model_uri=ODM.StudyEndPoints_StudyEndPointRefRef, domain=StudyEndPoints, range=Optional[Union[Dict[Union[str, StudyEndPointOID], Union[dict, "StudyEndPoint"]], List[Union[dict, "StudyEndPoint"]]]])

slots.StudyEndPoint_OID = Slot(uri=ODM.OID, name="StudyEndPoint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEndPoint_OID, domain=StudyEndPoint, range=Union[str, StudyEndPointOID])

slots.StudyEndPoint_Name = Slot(uri=ODM.Name, name="StudyEndPoint_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.StudyEndPoint_Name, domain=StudyEndPoint, range=str)

slots.StudyEndPoint_Type = Slot(uri=ODM.Type, name="StudyEndPoint_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.StudyEndPoint_Type, domain=StudyEndPoint, range=Optional[Union[str, "StudyEndPointType"]])

slots.StudyEndPoint_Level = Slot(uri=ODM.Level, name="StudyEndPoint_Level", curie=ODM.curie('Level'),
                   model_uri=ODM.StudyEndPoint_Level, domain=StudyEndPoint, range=Optional[Union[str, "StudyEstimandLevel"]])

slots.StudyEndPoint_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyEndPoint_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyEndPoint_DescriptionRef, domain=StudyEndPoint, range=Optional[Union[dict, Description]])

slots.StudyEndPoint_FormalExpressionRef = Slot(uri=ODM.FormalExpressionRef, name="StudyEndPoint_FormalExpressionRef", curie=ODM.curie('FormalExpressionRef'),
                   model_uri=ODM.StudyEndPoint_FormalExpressionRef, domain=StudyEndPoint, range=Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]])

slots.StudyTargetPopulation_OID = Slot(uri=ODM.OID, name="StudyTargetPopulation_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyTargetPopulation_OID, domain=StudyTargetPopulation, range=Union[str, StudyTargetPopulationOID])

slots.StudyTargetPopulation_Name = Slot(uri=ODM.Name, name="StudyTargetPopulation_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.StudyTargetPopulation_Name, domain=StudyTargetPopulation, range=str)

slots.StudyTargetPopulation_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyTargetPopulation_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyTargetPopulation_DescriptionRef, domain=StudyTargetPopulation, range=Optional[Union[dict, Description]])

slots.StudyTargetPopulation_CodingRef = Slot(uri=ODM.CodingRef, name="StudyTargetPopulation_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.StudyTargetPopulation_CodingRef, domain=StudyTargetPopulation, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyTargetPopulation_FormalExpressionRef = Slot(uri=ODM.FormalExpressionRef, name="StudyTargetPopulation_FormalExpressionRef", curie=ODM.curie('FormalExpressionRef'),
                   model_uri=ODM.StudyTargetPopulation_FormalExpressionRef, domain=StudyTargetPopulation, range=Optional[Union[Union[dict, FormalExpression], List[Union[dict, FormalExpression]]]])

slots.StudyEstimands_StudyEstimandRef = Slot(uri=ODM.StudyEstimandRef, name="StudyEstimands_StudyEstimandRef", curie=ODM.curie('StudyEstimandRef'),
                   model_uri=ODM.StudyEstimands_StudyEstimandRef, domain=StudyEstimands, range=Optional[Union[Dict[Union[str, StudyEstimandOID], Union[dict, "StudyEstimand"]], List[Union[dict, "StudyEstimand"]]]])

slots.StudyEstimand_OID = Slot(uri=ODM.OID, name="StudyEstimand_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyEstimand_OID, domain=StudyEstimand, range=Union[str, StudyEstimandOID])

slots.StudyEstimand_Name = Slot(uri=ODM.Name, name="StudyEstimand_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.StudyEstimand_Name, domain=StudyEstimand, range=str)

slots.StudyEstimand_Level = Slot(uri=ODM.Level, name="StudyEstimand_Level", curie=ODM.curie('Level'),
                   model_uri=ODM.StudyEstimand_Level, domain=StudyEstimand, range=Optional[Union[str, "StudyEstimandLevel"]])

slots.StudyEstimand_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="StudyEstimand_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.StudyEstimand_DescriptionRef, domain=StudyEstimand, range=Optional[Union[dict, Description]])

slots.StudyEstimand_StudyTargetPopulationRefRef = Slot(uri=ODM.StudyTargetPopulationRefRef, name="StudyEstimand_StudyTargetPopulationRefRef", curie=ODM.curie('StudyTargetPopulationRefRef'),
                   model_uri=ODM.StudyEstimand_StudyTargetPopulationRefRef, domain=StudyEstimand, range=Optional[Union[dict, "StudyTargetPopulationRef"]])

slots.StudyEstimand_StudyInterventionRefRef = Slot(uri=ODM.StudyInterventionRefRef, name="StudyEstimand_StudyInterventionRefRef", curie=ODM.curie('StudyInterventionRefRef'),
                   model_uri=ODM.StudyEstimand_StudyInterventionRefRef, domain=StudyEstimand, range=Optional[Union[dict, "StudyInterventionRef"]])

slots.StudyEstimand_StudyEndPointRefRef = Slot(uri=ODM.StudyEndPointRefRef, name="StudyEstimand_StudyEndPointRefRef", curie=ODM.curie('StudyEndPointRefRef'),
                   model_uri=ODM.StudyEstimand_StudyEndPointRefRef, domain=StudyEstimand, range=Optional[Union[dict, StudyEndPointRef]])

slots.StudyEstimand_IntercurrentEventRef = Slot(uri=ODM.IntercurrentEventRef, name="StudyEstimand_IntercurrentEventRef", curie=ODM.curie('IntercurrentEventRef'),
                   model_uri=ODM.StudyEstimand_IntercurrentEventRef, domain=StudyEstimand, range=Optional[Union[Union[dict, "IntercurrentEvent"], List[Union[dict, "IntercurrentEvent"]]]])

slots.StudyEstimand_SummaryMeasureRef = Slot(uri=ODM.SummaryMeasureRef, name="StudyEstimand_SummaryMeasureRef", curie=ODM.curie('SummaryMeasureRef'),
                   model_uri=ODM.StudyEstimand_SummaryMeasureRef, domain=StudyEstimand, range=Optional[Union[dict, "SummaryMeasure"]])

slots.InclusionExclusionCriteria_InclusionCriteriaRef = Slot(uri=ODM.InclusionCriteriaRef, name="InclusionExclusionCriteria_InclusionCriteriaRef", curie=ODM.curie('InclusionCriteriaRef'),
                   model_uri=ODM.InclusionExclusionCriteria_InclusionCriteriaRef, domain=InclusionExclusionCriteria, range=Optional[Union[dict, "InclusionCriteria"]])

slots.InclusionExclusionCriteria_ExclusionCriteriaRef = Slot(uri=ODM.ExclusionCriteriaRef, name="InclusionExclusionCriteria_ExclusionCriteriaRef", curie=ODM.curie('ExclusionCriteriaRef'),
                   model_uri=ODM.InclusionExclusionCriteria_ExclusionCriteriaRef, domain=InclusionExclusionCriteria, range=Optional[Union[dict, "ExclusionCriteria"]])

slots.InclusionCriteria_CriterionRef = Slot(uri=ODM.CriterionRef, name="InclusionCriteria_CriterionRef", curie=ODM.curie('CriterionRef'),
                   model_uri=ODM.InclusionCriteria_CriterionRef, domain=InclusionCriteria, range=Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]])

slots.ExclusionCriteria_CriterionRef = Slot(uri=ODM.CriterionRef, name="ExclusionCriteria_CriterionRef", curie=ODM.curie('CriterionRef'),
                   model_uri=ODM.ExclusionCriteria_CriterionRef, domain=ExclusionCriteria, range=Optional[Union[Dict[Union[str, CriterionOID], Union[dict, "Criterion"]], List[Union[dict, "Criterion"]]]])

slots.StudyTargetPopulationRef_StudyTargetPopulationOID = Slot(uri=ODM.StudyTargetPopulationOID, name="StudyTargetPopulationRef_StudyTargetPopulationOID", curie=ODM.curie('StudyTargetPopulationOID'),
                   model_uri=ODM.StudyTargetPopulationRef_StudyTargetPopulationOID, domain=StudyTargetPopulationRef, range=str)

slots.StudyInterventionRef_StudyInterventionOID = Slot(uri=ODM.StudyInterventionOID, name="StudyInterventionRef_StudyInterventionOID", curie=ODM.curie('StudyInterventionOID'),
                   model_uri=ODM.StudyInterventionRef_StudyInterventionOID, domain=StudyInterventionRef, range=str)

slots.IntercurrentEvent_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="IntercurrentEvent_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.IntercurrentEvent_DescriptionRef, domain=IntercurrentEvent, range=Optional[Union[dict, Description]])

slots.SummaryMeasure_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="SummaryMeasure_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.SummaryMeasure_DescriptionRef, domain=SummaryMeasure, range=Optional[Union[dict, Description]])

slots.Arm_OID = Slot(uri=ODM.OID, name="Arm_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Arm_OID, domain=Arm, range=Union[str, ArmOID])

slots.Arm_Name = Slot(uri=ODM.Name, name="Arm_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Arm_Name, domain=Arm, range=str)

slots.Arm_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Arm_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Arm_DescriptionRef, domain=Arm, range=Optional[Union[dict, Description]])

slots.Arm_WorkflowRefRef = Slot(uri=ODM.WorkflowRefRef, name="Arm_WorkflowRefRef", curie=ODM.curie('WorkflowRefRef'),
                   model_uri=ODM.Arm_WorkflowRefRef, domain=Arm, range=Optional[Union[dict, "WorkflowRef"]])

slots.Epoch_OID = Slot(uri=ODM.OID, name="Epoch_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Epoch_OID, domain=Epoch, range=Union[str, EpochOID])

slots.Epoch_Name = Slot(uri=ODM.Name, name="Epoch_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Epoch_Name, domain=Epoch, range=str)

slots.Epoch_SequenceNumber = Slot(uri=ODM.SequenceNumber, name="Epoch_SequenceNumber", curie=ODM.curie('SequenceNumber'),
                   model_uri=ODM.Epoch_SequenceNumber, domain=Epoch, range=int)

slots.Epoch_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Epoch_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Epoch_DescriptionRef, domain=Epoch, range=Optional[Union[dict, Description]])

slots.WorkflowRef_WorkflowOID = Slot(uri=ODM.WorkflowOID, name="WorkflowRef_WorkflowOID", curie=ODM.curie('WorkflowOID'),
                   model_uri=ODM.WorkflowRef_WorkflowOID, domain=WorkflowRef, range=str)

slots.StudySummary_StudyParameterRef = Slot(uri=ODM.StudyParameterRef, name="StudySummary_StudyParameterRef", curie=ODM.curie('StudyParameterRef'),
                   model_uri=ODM.StudySummary_StudyParameterRef, domain=StudySummary, range=Optional[Union[Dict[Union[str, StudyParameterOID], Union[dict, "StudyParameter"]], List[Union[dict, "StudyParameter"]]]])

slots.StudyParameter_OID = Slot(uri=ODM.OID, name="StudyParameter_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyParameter_OID, domain=StudyParameter, range=Union[str, StudyParameterOID])

slots.StudyParameter_Term = Slot(uri=ODM.Term, name="StudyParameter_Term", curie=ODM.curie('Term'),
                   model_uri=ODM.StudyParameter_Term, domain=StudyParameter, range=str)

slots.StudyParameter_ShortName = Slot(uri=ODM.ShortName, name="StudyParameter_ShortName", curie=ODM.curie('ShortName'),
                   model_uri=ODM.StudyParameter_ShortName, domain=StudyParameter, range=Optional[str])

slots.StudyParameter_ParameterValueRef = Slot(uri=ODM.ParameterValueRef, name="StudyParameter_ParameterValueRef", curie=ODM.curie('ParameterValueRef'),
                   model_uri=ODM.StudyParameter_ParameterValueRef, domain=StudyParameter, range=Optional[Union[dict, "ParameterValue"]])

slots.StudyParameter_CodingRef = Slot(uri=ODM.CodingRef, name="StudyParameter_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.StudyParameter_CodingRef, domain=StudyParameter, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.ParameterValue_ValueRef = Slot(uri=ODM.ValueRef, name="ParameterValue_ValueRef", curie=ODM.curie('ValueRef'),
                   model_uri=ODM.ParameterValue_ValueRef, domain=ParameterValue, range=str)

slots.ParameterValue_CodingRef = Slot(uri=ODM.CodingRef, name="ParameterValue_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.ParameterValue_CodingRef, domain=ParameterValue, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyTimings_StudyTimingRef = Slot(uri=ODM.StudyTimingRef, name="StudyTimings_StudyTimingRef", curie=ODM.curie('StudyTimingRef'),
                   model_uri=ODM.StudyTimings_StudyTimingRef, domain=StudyTimings, range=Optional[Union[Dict[Union[str, StudyTimingOID], Union[dict, "StudyTiming"]], List[Union[dict, "StudyTiming"]]]])

slots.StudyTiming_OID = Slot(uri=ODM.OID, name="StudyTiming_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.StudyTiming_OID, domain=StudyTiming, range=Union[str, StudyTimingOID])

slots.StudyTiming_Name = Slot(uri=ODM.Name, name="StudyTiming_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.StudyTiming_Name, domain=StudyTiming, range=str)

slots.StudyTiming_AbsoluteTimingConstraintRef = Slot(uri=ODM.AbsoluteTimingConstraintRef, name="StudyTiming_AbsoluteTimingConstraintRef", curie=ODM.curie('AbsoluteTimingConstraintRef'),
                   model_uri=ODM.StudyTiming_AbsoluteTimingConstraintRef, domain=StudyTiming, range=Optional[Union[Dict[Union[str, AbsoluteTimingConstraintOID], Union[dict, "AbsoluteTimingConstraint"]], List[Union[dict, "AbsoluteTimingConstraint"]]]])

slots.StudyTiming_RelativeTimingConstraintRef = Slot(uri=ODM.RelativeTimingConstraintRef, name="StudyTiming_RelativeTimingConstraintRef", curie=ODM.curie('RelativeTimingConstraintRef'),
                   model_uri=ODM.StudyTiming_RelativeTimingConstraintRef, domain=StudyTiming, range=Optional[Union[Dict[Union[str, RelativeTimingConstraintOID], Union[dict, "RelativeTimingConstraint"]], List[Union[dict, "RelativeTimingConstraint"]]]])

slots.StudyTiming_TransitionTimingConstraintRef = Slot(uri=ODM.TransitionTimingConstraintRef, name="StudyTiming_TransitionTimingConstraintRef", curie=ODM.curie('TransitionTimingConstraintRef'),
                   model_uri=ODM.StudyTiming_TransitionTimingConstraintRef, domain=StudyTiming, range=Optional[Union[Dict[Union[str, TransitionTimingConstraintOID], Union[dict, "TransitionTimingConstraint"]], List[Union[dict, "TransitionTimingConstraint"]]]])

slots.StudyTiming_DurationTimingConstraintRef = Slot(uri=ODM.DurationTimingConstraintRef, name="StudyTiming_DurationTimingConstraintRef", curie=ODM.curie('DurationTimingConstraintRef'),
                   model_uri=ODM.StudyTiming_DurationTimingConstraintRef, domain=StudyTiming, range=Optional[Union[Dict[Union[str, DurationTimingConstraintOID], Union[dict, "DurationTimingConstraint"]], List[Union[dict, "DurationTimingConstraint"]]]])

slots.TransitionTimingConstraint_OID = Slot(uri=ODM.OID, name="TransitionTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.TransitionTimingConstraint_OID, domain=TransitionTimingConstraint, range=Union[str, TransitionTimingConstraintOID])

slots.TransitionTimingConstraint_Name = Slot(uri=ODM.Name, name="TransitionTimingConstraint_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.TransitionTimingConstraint_Name, domain=TransitionTimingConstraint, range=str)

slots.TransitionTimingConstraint_TransitionOID = Slot(uri=ODM.TransitionOID, name="TransitionTimingConstraint_TransitionOID", curie=ODM.curie('TransitionOID'),
                   model_uri=ODM.TransitionTimingConstraint_TransitionOID, domain=TransitionTimingConstraint, range=str)

slots.TransitionTimingConstraint_MethodOID = Slot(uri=ODM.MethodOID, name="TransitionTimingConstraint_MethodOID", curie=ODM.curie('MethodOID'),
                   model_uri=ODM.TransitionTimingConstraint_MethodOID, domain=TransitionTimingConstraint, range=Optional[str])

slots.TransitionTimingConstraint_Type = Slot(uri=ODM.Type, name="TransitionTimingConstraint_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.TransitionTimingConstraint_Type, domain=TransitionTimingConstraint, range=Optional[Union[str, "RelativeTimingConstraintType"]])

slots.TransitionTimingConstraint_TimepointTarget = Slot(uri=ODM.TimepointTarget, name="TransitionTimingConstraint_TimepointTarget", curie=ODM.curie('TimepointTarget'),
                   model_uri=ODM.TransitionTimingConstraint_TimepointTarget, domain=TransitionTimingConstraint, range=str)

slots.TransitionTimingConstraint_TimepointPreWindow = Slot(uri=ODM.TimepointPreWindow, name="TransitionTimingConstraint_TimepointPreWindow", curie=ODM.curie('TimepointPreWindow'),
                   model_uri=ODM.TransitionTimingConstraint_TimepointPreWindow, domain=TransitionTimingConstraint, range=Optional[str])

slots.TransitionTimingConstraint_TimepointPostWindow = Slot(uri=ODM.TimepointPostWindow, name="TransitionTimingConstraint_TimepointPostWindow", curie=ODM.curie('TimepointPostWindow'),
                   model_uri=ODM.TransitionTimingConstraint_TimepointPostWindow, domain=TransitionTimingConstraint, range=Optional[str])

slots.TransitionTimingConstraint_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="TransitionTimingConstraint_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.TransitionTimingConstraint_DescriptionRef, domain=TransitionTimingConstraint, range=Optional[Union[dict, Description]])

slots.AbsoluteTimingConstraint_OID = Slot(uri=ODM.OID, name="AbsoluteTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.AbsoluteTimingConstraint_OID, domain=AbsoluteTimingConstraint, range=Union[str, AbsoluteTimingConstraintOID])

slots.AbsoluteTimingConstraint_Name = Slot(uri=ODM.Name, name="AbsoluteTimingConstraint_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.AbsoluteTimingConstraint_Name, domain=AbsoluteTimingConstraint, range=str)

slots.AbsoluteTimingConstraint_StudyEventGroupOID = Slot(uri=ODM.StudyEventGroupOID, name="AbsoluteTimingConstraint_StudyEventGroupOID", curie=ODM.curie('StudyEventGroupOID'),
                   model_uri=ODM.AbsoluteTimingConstraint_StudyEventGroupOID, domain=AbsoluteTimingConstraint, range=Optional[str])

slots.AbsoluteTimingConstraint_StudyEventOID = Slot(uri=ODM.StudyEventOID, name="AbsoluteTimingConstraint_StudyEventOID", curie=ODM.curie('StudyEventOID'),
                   model_uri=ODM.AbsoluteTimingConstraint_StudyEventOID, domain=AbsoluteTimingConstraint, range=Optional[str])

slots.AbsoluteTimingConstraint_TimepointTarget = Slot(uri=ODM.TimepointTarget, name="AbsoluteTimingConstraint_TimepointTarget", curie=ODM.curie('TimepointTarget'),
                   model_uri=ODM.AbsoluteTimingConstraint_TimepointTarget, domain=AbsoluteTimingConstraint, range=str)

slots.AbsoluteTimingConstraint_TimepointPreWindow = Slot(uri=ODM.TimepointPreWindow, name="AbsoluteTimingConstraint_TimepointPreWindow", curie=ODM.curie('TimepointPreWindow'),
                   model_uri=ODM.AbsoluteTimingConstraint_TimepointPreWindow, domain=AbsoluteTimingConstraint, range=Optional[str])

slots.AbsoluteTimingConstraint_TimepointPostWindow = Slot(uri=ODM.TimepointPostWindow, name="AbsoluteTimingConstraint_TimepointPostWindow", curie=ODM.curie('TimepointPostWindow'),
                   model_uri=ODM.AbsoluteTimingConstraint_TimepointPostWindow, domain=AbsoluteTimingConstraint, range=Optional[str])

slots.AbsoluteTimingConstraint_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="AbsoluteTimingConstraint_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.AbsoluteTimingConstraint_DescriptionRef, domain=AbsoluteTimingConstraint, range=Optional[Union[dict, Description]])

slots.RelativeTimingConstraint_OID = Slot(uri=ODM.OID, name="RelativeTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.RelativeTimingConstraint_OID, domain=RelativeTimingConstraint, range=Union[str, RelativeTimingConstraintOID])

slots.RelativeTimingConstraint_Name = Slot(uri=ODM.Name, name="RelativeTimingConstraint_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.RelativeTimingConstraint_Name, domain=RelativeTimingConstraint, range=str)

slots.RelativeTimingConstraint_PredecessorOID = Slot(uri=ODM.PredecessorOID, name="RelativeTimingConstraint_PredecessorOID", curie=ODM.curie('PredecessorOID'),
                   model_uri=ODM.RelativeTimingConstraint_PredecessorOID, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_SuccessorOID = Slot(uri=ODM.SuccessorOID, name="RelativeTimingConstraint_SuccessorOID", curie=ODM.curie('SuccessorOID'),
                   model_uri=ODM.RelativeTimingConstraint_SuccessorOID, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_Type = Slot(uri=ODM.Type, name="RelativeTimingConstraint_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.RelativeTimingConstraint_Type, domain=RelativeTimingConstraint, range=Optional[Union[str, "RelativeTimingConstraintType"]])

slots.RelativeTimingConstraint_TimepointRelativeTarget = Slot(uri=ODM.TimepointRelativeTarget, name="RelativeTimingConstraint_TimepointRelativeTarget", curie=ODM.curie('TimepointRelativeTarget'),
                   model_uri=ODM.RelativeTimingConstraint_TimepointRelativeTarget, domain=RelativeTimingConstraint, range=str)

slots.RelativeTimingConstraint_TimepointPreWindow = Slot(uri=ODM.TimepointPreWindow, name="RelativeTimingConstraint_TimepointPreWindow", curie=ODM.curie('TimepointPreWindow'),
                   model_uri=ODM.RelativeTimingConstraint_TimepointPreWindow, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_TimepointPostWindow = Slot(uri=ODM.TimepointPostWindow, name="RelativeTimingConstraint_TimepointPostWindow", curie=ODM.curie('TimepointPostWindow'),
                   model_uri=ODM.RelativeTimingConstraint_TimepointPostWindow, domain=RelativeTimingConstraint, range=Optional[str])

slots.RelativeTimingConstraint_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="RelativeTimingConstraint_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.RelativeTimingConstraint_DescriptionRef, domain=RelativeTimingConstraint, range=Optional[Union[dict, Description]])

slots.DurationTimingConstraint_OID = Slot(uri=ODM.OID, name="DurationTimingConstraint_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.DurationTimingConstraint_OID, domain=DurationTimingConstraint, range=Union[str, DurationTimingConstraintOID])

slots.DurationTimingConstraint_Name = Slot(uri=ODM.Name, name="DurationTimingConstraint_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.DurationTimingConstraint_Name, domain=DurationTimingConstraint, range=str)

slots.DurationTimingConstraint_StructuralElementOID = Slot(uri=ODM.StructuralElementOID, name="DurationTimingConstraint_StructuralElementOID", curie=ODM.curie('StructuralElementOID'),
                   model_uri=ODM.DurationTimingConstraint_StructuralElementOID, domain=DurationTimingConstraint, range=str)

slots.DurationTimingConstraint_DurationTarget = Slot(uri=ODM.DurationTarget, name="DurationTimingConstraint_DurationTarget", curie=ODM.curie('DurationTarget'),
                   model_uri=ODM.DurationTimingConstraint_DurationTarget, domain=DurationTimingConstraint, range=str)

slots.DurationTimingConstraint_DurationPreWindow = Slot(uri=ODM.DurationPreWindow, name="DurationTimingConstraint_DurationPreWindow", curie=ODM.curie('DurationPreWindow'),
                   model_uri=ODM.DurationTimingConstraint_DurationPreWindow, domain=DurationTimingConstraint, range=Optional[str])

slots.DurationTimingConstraint_DurationPostWindow = Slot(uri=ODM.DurationPostWindow, name="DurationTimingConstraint_DurationPostWindow", curie=ODM.curie('DurationPostWindow'),
                   model_uri=ODM.DurationTimingConstraint_DurationPostWindow, domain=DurationTimingConstraint, range=Optional[str])

slots.DurationTimingConstraint_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="DurationTimingConstraint_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.DurationTimingConstraint_DescriptionRef, domain=DurationTimingConstraint, range=Optional[Union[dict, Description]])

slots.WorkflowDef_OID = Slot(uri=ODM.OID, name="WorkflowDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.WorkflowDef_OID, domain=WorkflowDef, range=Union[str, WorkflowDefOID])

slots.WorkflowDef_Name = Slot(uri=ODM.Name, name="WorkflowDef_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.WorkflowDef_Name, domain=WorkflowDef, range=str)

slots.WorkflowDef_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="WorkflowDef_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.WorkflowDef_DescriptionRef, domain=WorkflowDef, range=Optional[Union[dict, Description]])

slots.WorkflowDef_WorkflowStartRef = Slot(uri=ODM.WorkflowStartRef, name="WorkflowDef_WorkflowStartRef", curie=ODM.curie('WorkflowStartRef'),
                   model_uri=ODM.WorkflowDef_WorkflowStartRef, domain=WorkflowDef, range=Optional[Union[dict, "WorkflowStart"]])

slots.WorkflowDef_WorkflowEndRef = Slot(uri=ODM.WorkflowEndRef, name="WorkflowDef_WorkflowEndRef", curie=ODM.curie('WorkflowEndRef'),
                   model_uri=ODM.WorkflowDef_WorkflowEndRef, domain=WorkflowDef, range=Optional[Union[Union[dict, "WorkflowEnd"], List[Union[dict, "WorkflowEnd"]]]])

slots.WorkflowDef_TransitionRef = Slot(uri=ODM.TransitionRef, name="WorkflowDef_TransitionRef", curie=ODM.curie('TransitionRef'),
                   model_uri=ODM.WorkflowDef_TransitionRef, domain=WorkflowDef, range=Optional[Union[Dict[Union[str, TransitionOID], Union[dict, "Transition"]], List[Union[dict, "Transition"]]]])

slots.WorkflowDef_BranchingRef = Slot(uri=ODM.BranchingRef, name="WorkflowDef_BranchingRef", curie=ODM.curie('BranchingRef'),
                   model_uri=ODM.WorkflowDef_BranchingRef, domain=WorkflowDef, range=Optional[Union[Dict[Union[str, BranchingOID], Union[dict, "Branching"]], List[Union[dict, "Branching"]]]])

slots.WorkflowStart_StartOID = Slot(uri=ODM.StartOID, name="WorkflowStart_StartOID", curie=ODM.curie('StartOID'),
                   model_uri=ODM.WorkflowStart_StartOID, domain=WorkflowStart, range=str)

slots.Transition_OID = Slot(uri=ODM.OID, name="Transition_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Transition_OID, domain=Transition, range=Union[str, TransitionOID])

slots.Transition_Name = Slot(uri=ODM.Name, name="Transition_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Transition_Name, domain=Transition, range=str)

slots.Transition_SourceOID = Slot(uri=ODM.SourceOID, name="Transition_SourceOID", curie=ODM.curie('SourceOID'),
                   model_uri=ODM.Transition_SourceOID, domain=Transition, range=str)

slots.Transition_TargetOID = Slot(uri=ODM.TargetOID, name="Transition_TargetOID", curie=ODM.curie('TargetOID'),
                   model_uri=ODM.Transition_TargetOID, domain=Transition, range=str)

slots.Transition_StartConditionOID = Slot(uri=ODM.StartConditionOID, name="Transition_StartConditionOID", curie=ODM.curie('StartConditionOID'),
                   model_uri=ODM.Transition_StartConditionOID, domain=Transition, range=Optional[str])

slots.Transition_EndConditionOID = Slot(uri=ODM.EndConditionOID, name="Transition_EndConditionOID", curie=ODM.curie('EndConditionOID'),
                   model_uri=ODM.Transition_EndConditionOID, domain=Transition, range=Optional[str])

slots.Branching_OID = Slot(uri=ODM.OID, name="Branching_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Branching_OID, domain=Branching, range=Union[str, BranchingOID])

slots.Branching_Name = Slot(uri=ODM.Name, name="Branching_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Branching_Name, domain=Branching, range=str)

slots.Branching_Type = Slot(uri=ODM.Type, name="Branching_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.Branching_Type, domain=Branching, range=Union[str, "BranchingType"])

slots.Branching_TargetTransitionRef = Slot(uri=ODM.TargetTransitionRef, name="Branching_TargetTransitionRef", curie=ODM.curie('TargetTransitionRef'),
                   model_uri=ODM.Branching_TargetTransitionRef, domain=Branching, range=Optional[Union[Union[dict, "TargetTransition"], List[Union[dict, "TargetTransition"]]]])

slots.Branching_DefaultTransitionRef = Slot(uri=ODM.DefaultTransitionRef, name="Branching_DefaultTransitionRef", curie=ODM.curie('DefaultTransitionRef'),
                   model_uri=ODM.Branching_DefaultTransitionRef, domain=Branching, range=Optional[Union[Union[dict, "DefaultTransition"], List[Union[dict, "DefaultTransition"]]]])

slots.TargetTransition_TargetTransitionOID = Slot(uri=ODM.TargetTransitionOID, name="TargetTransition_TargetTransitionOID", curie=ODM.curie('TargetTransitionOID'),
                   model_uri=ODM.TargetTransition_TargetTransitionOID, domain=TargetTransition, range=str)

slots.TargetTransition_ConditionOID = Slot(uri=ODM.ConditionOID, name="TargetTransition_ConditionOID", curie=ODM.curie('ConditionOID'),
                   model_uri=ODM.TargetTransition_ConditionOID, domain=TargetTransition, range=Optional[str])

slots.DefaultTransition_TargetTransitionOID = Slot(uri=ODM.TargetTransitionOID, name="DefaultTransition_TargetTransitionOID", curie=ODM.curie('TargetTransitionOID'),
                   model_uri=ODM.DefaultTransition_TargetTransitionOID, domain=DefaultTransition, range=str)

slots.WorkflowEnd_EndOID = Slot(uri=ODM.EndOID, name="WorkflowEnd_EndOID", curie=ODM.curie('EndOID'),
                   model_uri=ODM.WorkflowEnd_EndOID, domain=WorkflowEnd, range=str)

slots.WorkflowEnd__content = Slot(uri=ODM._content, name="WorkflowEnd__content", curie=ODM.curie('_content'),
                   model_uri=ODM.WorkflowEnd__content, domain=WorkflowEnd, range=Optional[str])

slots.Criterion_OID = Slot(uri=ODM.OID, name="Criterion_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Criterion_OID, domain=Criterion, range=Union[str, CriterionOID])

slots.Criterion_Name = Slot(uri=ODM.Name, name="Criterion_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Criterion_Name, domain=Criterion, range=str)

slots.Criterion_ConditionOID = Slot(uri=ODM.ConditionOID, name="Criterion_ConditionOID", curie=ODM.curie('ConditionOID'),
                   model_uri=ODM.Criterion_ConditionOID, domain=Criterion, range=str)

slots.Criterion_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Criterion_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Criterion_DescriptionRef, domain=Criterion, range=Optional[Union[dict, Description]])

slots.Criterion_CodingRef = Slot(uri=ODM.CodingRef, name="Criterion_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.Criterion_CodingRef, domain=Criterion, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.AdminData_StudyOID = Slot(uri=ODM.StudyOID, name="AdminData_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.AdminData_StudyOID, domain=AdminData, range=Optional[str])

slots.AdminData_UserRefRef = Slot(uri=ODM.UserRefRef, name="AdminData_UserRefRef", curie=ODM.curie('UserRefRef'),
                   model_uri=ODM.AdminData_UserRefRef, domain=AdminData, range=Optional[Union[Dict[Union[str, UserOID], Union[dict, "User"]], List[Union[dict, "User"]]]])

slots.AdminData_OrganizationRef = Slot(uri=ODM.OrganizationRef, name="AdminData_OrganizationRef", curie=ODM.curie('OrganizationRef'),
                   model_uri=ODM.AdminData_OrganizationRef, domain=AdminData, range=Optional[Union[Dict[Union[str, OrganizationOID], Union[dict, "Organization"]], List[Union[dict, "Organization"]]]])

slots.AdminData_LocationRefRef = Slot(uri=ODM.LocationRefRef, name="AdminData_LocationRefRef", curie=ODM.curie('LocationRefRef'),
                   model_uri=ODM.AdminData_LocationRefRef, domain=AdminData, range=Optional[Union[Dict[Union[str, LocationOID], Union[dict, "Location"]], List[Union[dict, "Location"]]]])

slots.AdminData_SignatureDefRef = Slot(uri=ODM.SignatureDefRef, name="AdminData_SignatureDefRef", curie=ODM.curie('SignatureDefRef'),
                   model_uri=ODM.AdminData_SignatureDefRef, domain=AdminData, range=Optional[Union[Dict[Union[str, SignatureDefOID], Union[dict, "SignatureDef"]], List[Union[dict, "SignatureDef"]]]])

slots.User_OID = Slot(uri=ODM.OID, name="User_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.User_OID, domain=User, range=Union[str, UserOID])

slots.User_UserTypeRef = Slot(uri=ODM.UserTypeRef, name="User_UserTypeRef", curie=ODM.curie('UserTypeRef'),
                   model_uri=ODM.User_UserTypeRef, domain=User, range=Optional[Union[str, "UserType"]])

slots.User_OrganizationOID = Slot(uri=ODM.OrganizationOID, name="User_OrganizationOID", curie=ODM.curie('OrganizationOID'),
                   model_uri=ODM.User_OrganizationOID, domain=User, range=Optional[str])

slots.User_LocationOID = Slot(uri=ODM.LocationOID, name="User_LocationOID", curie=ODM.curie('LocationOID'),
                   model_uri=ODM.User_LocationOID, domain=User, range=Optional[str])

slots.User_UserNameRef = Slot(uri=ODM.UserNameRef, name="User_UserNameRef", curie=ODM.curie('UserNameRef'),
                   model_uri=ODM.User_UserNameRef, domain=User, range=Optional[Union[dict, "UserName"]])

slots.User_PrefixRef = Slot(uri=ODM.PrefixRef, name="User_PrefixRef", curie=ODM.curie('PrefixRef'),
                   model_uri=ODM.User_PrefixRef, domain=User, range=Optional[Union[dict, "Prefix"]])

slots.User_SuffixRef = Slot(uri=ODM.SuffixRef, name="User_SuffixRef", curie=ODM.curie('SuffixRef'),
                   model_uri=ODM.User_SuffixRef, domain=User, range=Optional[Union[dict, "Suffix"]])

slots.User_FullNameRef = Slot(uri=ODM.FullNameRef, name="User_FullNameRef", curie=ODM.curie('FullNameRef'),
                   model_uri=ODM.User_FullNameRef, domain=User, range=Optional[Union[dict, "FullName"]])

slots.User_GivenNameRef = Slot(uri=ODM.GivenNameRef, name="User_GivenNameRef", curie=ODM.curie('GivenNameRef'),
                   model_uri=ODM.User_GivenNameRef, domain=User, range=Optional[Union[dict, "GivenName"]])

slots.User_FamilyNameRef = Slot(uri=ODM.FamilyNameRef, name="User_FamilyNameRef", curie=ODM.curie('FamilyNameRef'),
                   model_uri=ODM.User_FamilyNameRef, domain=User, range=Optional[Union[dict, "FamilyName"]])

slots.User_ImageRef = Slot(uri=ODM.ImageRef, name="User_ImageRef", curie=ODM.curie('ImageRef'),
                   model_uri=ODM.User_ImageRef, domain=User, range=Optional[Union[dict, "Image"]])

slots.User_AddressRef = Slot(uri=ODM.AddressRef, name="User_AddressRef", curie=ODM.curie('AddressRef'),
                   model_uri=ODM.User_AddressRef, domain=User, range=Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]])

slots.User_TelecomRef = Slot(uri=ODM.TelecomRef, name="User_TelecomRef", curie=ODM.curie('TelecomRef'),
                   model_uri=ODM.User_TelecomRef, domain=User, range=Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]])

slots.UserName_range = Slot(uri=ODM.range, name="UserName_range", curie=ODM.curie('range'),
                   model_uri=ODM.UserName_range, domain=UserName, range=Optional[str])

slots.Prefix_range = Slot(uri=ODM.range, name="Prefix_range", curie=ODM.curie('range'),
                   model_uri=ODM.Prefix_range, domain=Prefix, range=Optional[str])

slots.Suffix_range = Slot(uri=ODM.range, name="Suffix_range", curie=ODM.curie('range'),
                   model_uri=ODM.Suffix_range, domain=Suffix, range=Optional[str])

slots.FullName_range = Slot(uri=ODM.range, name="FullName_range", curie=ODM.curie('range'),
                   model_uri=ODM.FullName_range, domain=FullName, range=Optional[str])

slots.GivenName_range = Slot(uri=ODM.range, name="GivenName_range", curie=ODM.curie('range'),
                   model_uri=ODM.GivenName_range, domain=GivenName, range=Optional[str])

slots.FamilyName_range = Slot(uri=ODM.range, name="FamilyName_range", curie=ODM.curie('range'),
                   model_uri=ODM.FamilyName_range, domain=FamilyName, range=Optional[str])

slots.Image_ImageFileName = Slot(uri=ODM.ImageFileName, name="Image_ImageFileName", curie=ODM.curie('ImageFileName'),
                   model_uri=ODM.Image_ImageFileName, domain=Image, range=Optional[URIorCURIE])

slots.Image_href = Slot(uri=ODM.href, name="Image_href", curie=ODM.curie('href'),
                   model_uri=ODM.Image_href, domain=Image, range=Optional[str])

slots.Image_MimeType = Slot(uri=ODM.MimeType, name="Image_MimeType", curie=ODM.curie('MimeType'),
                   model_uri=ODM.Image_MimeType, domain=Image, range=Optional[str])

slots.Organization_OID = Slot(uri=ODM.OID, name="Organization_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Organization_OID, domain=Organization, range=Union[str, OrganizationOID])

slots.Organization_Name = Slot(uri=ODM.Name, name="Organization_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Organization_Name, domain=Organization, range=str)

slots.Organization_Role = Slot(uri=ODM.Role, name="Organization_Role", curie=ODM.curie('Role'),
                   model_uri=ODM.Organization_Role, domain=Organization, range=Optional[str])

slots.Organization_Type = Slot(uri=ODM.Type, name="Organization_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.Organization_Type, domain=Organization, range=Union[str, "OrganizationType"])

slots.Organization_LocationOID = Slot(uri=ODM.LocationOID, name="Organization_LocationOID", curie=ODM.curie('LocationOID'),
                   model_uri=ODM.Organization_LocationOID, domain=Organization, range=Optional[str])

slots.Organization_PartOfOrganizationOID = Slot(uri=ODM.PartOfOrganizationOID, name="Organization_PartOfOrganizationOID", curie=ODM.curie('PartOfOrganizationOID'),
                   model_uri=ODM.Organization_PartOfOrganizationOID, domain=Organization, range=Optional[str])

slots.Organization_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Organization_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Organization_DescriptionRef, domain=Organization, range=Optional[Union[dict, Description]])

slots.Organization_AddressRef = Slot(uri=ODM.AddressRef, name="Organization_AddressRef", curie=ODM.curie('AddressRef'),
                   model_uri=ODM.Organization_AddressRef, domain=Organization, range=Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]])

slots.Organization_TelecomRef = Slot(uri=ODM.TelecomRef, name="Organization_TelecomRef", curie=ODM.curie('TelecomRef'),
                   model_uri=ODM.Organization_TelecomRef, domain=Organization, range=Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]])

slots.Location_OID = Slot(uri=ODM.OID, name="Location_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Location_OID, domain=Location, range=Union[str, LocationOID])

slots.Location_Name = Slot(uri=ODM.Name, name="Location_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Location_Name, domain=Location, range=str)

slots.Location_Role = Slot(uri=ODM.Role, name="Location_Role", curie=ODM.curie('Role'),
                   model_uri=ODM.Location_Role, domain=Location, range=Optional[str])

slots.Location_OrganizationOID = Slot(uri=ODM.OrganizationOID, name="Location_OrganizationOID", curie=ODM.curie('OrganizationOID'),
                   model_uri=ODM.Location_OrganizationOID, domain=Location, range=Optional[str])

slots.Location_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="Location_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.Location_DescriptionRef, domain=Location, range=Optional[Union[dict, Description]])

slots.Location_MetaDataVersionRefRef = Slot(uri=ODM.MetaDataVersionRefRef, name="Location_MetaDataVersionRefRef", curie=ODM.curie('MetaDataVersionRefRef'),
                   model_uri=ODM.Location_MetaDataVersionRefRef, domain=Location, range=Optional[Union[Union[dict, "MetaDataVersionRef"], List[Union[dict, "MetaDataVersionRef"]]]])

slots.Location_AddressRef = Slot(uri=ODM.AddressRef, name="Location_AddressRef", curie=ODM.curie('AddressRef'),
                   model_uri=ODM.Location_AddressRef, domain=Location, range=Optional[Union[Union[dict, "Address"], List[Union[dict, "Address"]]]])

slots.Location_TelecomRef = Slot(uri=ODM.TelecomRef, name="Location_TelecomRef", curie=ODM.curie('TelecomRef'),
                   model_uri=ODM.Location_TelecomRef, domain=Location, range=Optional[Union[Union[dict, "Telecom"], List[Union[dict, "Telecom"]]]])

slots.Location_QueryRef = Slot(uri=ODM.QueryRef, name="Location_QueryRef", curie=ODM.curie('QueryRef'),
                   model_uri=ODM.Location_QueryRef, domain=Location, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.Address_StreetNameRef = Slot(uri=ODM.StreetNameRef, name="Address_StreetNameRef", curie=ODM.curie('StreetNameRef'),
                   model_uri=ODM.Address_StreetNameRef, domain=Address, range=Optional[Union[dict, "StreetName"]])

slots.Address_HouseNumberRef = Slot(uri=ODM.HouseNumberRef, name="Address_HouseNumberRef", curie=ODM.curie('HouseNumberRef'),
                   model_uri=ODM.Address_HouseNumberRef, domain=Address, range=Optional[Union[dict, "HouseNumber"]])

slots.Address_CityRef = Slot(uri=ODM.CityRef, name="Address_CityRef", curie=ODM.curie('CityRef'),
                   model_uri=ODM.Address_CityRef, domain=Address, range=Optional[Union[dict, "City"]])

slots.Address_StateProvRef = Slot(uri=ODM.StateProvRef, name="Address_StateProvRef", curie=ODM.curie('StateProvRef'),
                   model_uri=ODM.Address_StateProvRef, domain=Address, range=Optional[Union[dict, "StateProv"]])

slots.Address_CountryRef = Slot(uri=ODM.CountryRef, name="Address_CountryRef", curie=ODM.curie('CountryRef'),
                   model_uri=ODM.Address_CountryRef, domain=Address, range=Optional[Union[dict, "Country"]])

slots.Address_PostalCodeRef = Slot(uri=ODM.PostalCodeRef, name="Address_PostalCodeRef", curie=ODM.curie('PostalCodeRef'),
                   model_uri=ODM.Address_PostalCodeRef, domain=Address, range=Optional[Union[dict, "PostalCode"]])

slots.Address_GeoPositionRef = Slot(uri=ODM.GeoPositionRef, name="Address_GeoPositionRef", curie=ODM.curie('GeoPositionRef'),
                   model_uri=ODM.Address_GeoPositionRef, domain=Address, range=Optional[Union[dict, "GeoPosition"]])

slots.Address_OtherTextRef = Slot(uri=ODM.OtherTextRef, name="Address_OtherTextRef", curie=ODM.curie('OtherTextRef'),
                   model_uri=ODM.Address_OtherTextRef, domain=Address, range=Optional[Union[dict, "OtherText"]])

slots.Telecom_TelecomType = Slot(uri=ODM.TelecomType, name="Telecom_TelecomType", curie=ODM.curie('TelecomType'),
                   model_uri=ODM.Telecom_TelecomType, domain=Telecom, range=Union[str, "TelecomTypeType"])

slots.Telecom_ValueRef = Slot(uri=ODM.ValueRef, name="Telecom_ValueRef", curie=ODM.curie('ValueRef'),
                   model_uri=ODM.Telecom_ValueRef, domain=Telecom, range=str)

slots.StreetName_range = Slot(uri=ODM.range, name="StreetName_range", curie=ODM.curie('range'),
                   model_uri=ODM.StreetName_range, domain=StreetName, range=Optional[str])

slots.HouseNumber_range = Slot(uri=ODM.range, name="HouseNumber_range", curie=ODM.curie('range'),
                   model_uri=ODM.HouseNumber_range, domain=HouseNumber, range=Optional[str])

slots.City_range = Slot(uri=ODM.range, name="City_range", curie=ODM.curie('range'),
                   model_uri=ODM.City_range, domain=City, range=Optional[str])

slots.StateProv_range = Slot(uri=ODM.range, name="StateProv_range", curie=ODM.curie('range'),
                   model_uri=ODM.StateProv_range, domain=StateProv, range=Optional[str])

slots.Country_range = Slot(uri=ODM.range, name="Country_range", curie=ODM.curie('range'),
                   model_uri=ODM.Country_range, domain=Country, range=Optional[str])

slots.PostalCode_range = Slot(uri=ODM.range, name="PostalCode_range", curie=ODM.curie('range'),
                   model_uri=ODM.PostalCode_range, domain=PostalCode, range=Optional[str])

slots.GeoPosition_Longitude = Slot(uri=ODM.Longitude, name="GeoPosition_Longitude", curie=ODM.curie('Longitude'),
                   model_uri=ODM.GeoPosition_Longitude, domain=GeoPosition, range=Optional[Decimal])

slots.GeoPosition_Latitude = Slot(uri=ODM.Latitude, name="GeoPosition_Latitude", curie=ODM.curie('Latitude'),
                   model_uri=ODM.GeoPosition_Latitude, domain=GeoPosition, range=Optional[Decimal])

slots.GeoPosition_Altitude = Slot(uri=ODM.Altitude, name="GeoPosition_Altitude", curie=ODM.curie('Altitude'),
                   model_uri=ODM.GeoPosition_Altitude, domain=GeoPosition, range=Optional[Decimal])

slots.OtherText_range = Slot(uri=ODM.range, name="OtherText_range", curie=ODM.curie('range'),
                   model_uri=ODM.OtherText_range, domain=OtherText, range=Optional[str])

slots.MetaDataVersionRef_StudyOID = Slot(uri=ODM.StudyOID, name="MetaDataVersionRef_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.MetaDataVersionRef_StudyOID, domain=MetaDataVersionRef, range=str)

slots.MetaDataVersionRef_MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="MetaDataVersionRef_MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.MetaDataVersionRef_MetaDataVersionOID, domain=MetaDataVersionRef, range=str)

slots.MetaDataVersionRef_EffectiveDate = Slot(uri=ODM.EffectiveDate, name="MetaDataVersionRef_EffectiveDate", curie=ODM.curie('EffectiveDate'),
                   model_uri=ODM.MetaDataVersionRef_EffectiveDate, domain=MetaDataVersionRef, range=Union[str, XSDDate])

slots.SignatureDef_OID = Slot(uri=ODM.OID, name="SignatureDef_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.SignatureDef_OID, domain=SignatureDef, range=Union[str, SignatureDefOID])

slots.SignatureDef_Methodology = Slot(uri=ODM.Methodology, name="SignatureDef_Methodology", curie=ODM.curie('Methodology'),
                   model_uri=ODM.SignatureDef_Methodology, domain=SignatureDef, range=Optional[Union[str, "SignMethod"]])

slots.SignatureDef_MeaningRef = Slot(uri=ODM.MeaningRef, name="SignatureDef_MeaningRef", curie=ODM.curie('MeaningRef'),
                   model_uri=ODM.SignatureDef_MeaningRef, domain=SignatureDef, range=Optional[Union[dict, "Meaning"]])

slots.SignatureDef_LegalReasonRef = Slot(uri=ODM.LegalReasonRef, name="SignatureDef_LegalReasonRef", curie=ODM.curie('LegalReasonRef'),
                   model_uri=ODM.SignatureDef_LegalReasonRef, domain=SignatureDef, range=Optional[Union[dict, "LegalReason"]])

slots.Meaning_range = Slot(uri=ODM.range, name="Meaning_range", curie=ODM.curie('range'),
                   model_uri=ODM.Meaning_range, domain=Meaning, range=Optional[str])

slots.LegalReason_range = Slot(uri=ODM.range, name="LegalReason_range", curie=ODM.curie('range'),
                   model_uri=ODM.LegalReason_range, domain=LegalReason, range=Optional[str])

slots.ReferenceData_StudyOID = Slot(uri=ODM.StudyOID, name="ReferenceData_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.ReferenceData_StudyOID, domain=ReferenceData, range=str)

slots.ReferenceData_MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="ReferenceData_MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.ReferenceData_MetaDataVersionOID, domain=ReferenceData, range=str)

slots.ReferenceData_ItemGroupDataRef = Slot(uri=ODM.ItemGroupDataRef, name="ReferenceData_ItemGroupDataRef", curie=ODM.curie('ItemGroupDataRef'),
                   model_uri=ODM.ReferenceData_ItemGroupDataRef, domain=ReferenceData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.ReferenceData_AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="ReferenceData_AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.ReferenceData_AuditRecordRef, domain=ReferenceData, range=Optional[Union[dict, "AuditRecord"]])

slots.ReferenceData_SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="ReferenceData_SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.ReferenceData_SignatureRefRef, domain=ReferenceData, range=Optional[Union[str, SignatureID]])

slots.ReferenceData_AnnotationRef = Slot(uri=ODM.AnnotationRef, name="ReferenceData_AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.ReferenceData_AnnotationRef, domain=ReferenceData, range=Optional[Union[str, AnnotationID]])

slots.ClinicalData_StudyOID = Slot(uri=ODM.StudyOID, name="ClinicalData_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.ClinicalData_StudyOID, domain=ClinicalData, range=str)

slots.ClinicalData_MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="ClinicalData_MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.ClinicalData_MetaDataVersionOID, domain=ClinicalData, range=str)

slots.ClinicalData_SubjectDataRef = Slot(uri=ODM.SubjectDataRef, name="ClinicalData_SubjectDataRef", curie=ODM.curie('SubjectDataRef'),
                   model_uri=ODM.ClinicalData_SubjectDataRef, domain=ClinicalData, range=Optional[Union[Union[dict, "SubjectData"], List[Union[dict, "SubjectData"]]]])

slots.ClinicalData_ItemGroupDataRef = Slot(uri=ODM.ItemGroupDataRef, name="ClinicalData_ItemGroupDataRef", curie=ODM.curie('ItemGroupDataRef'),
                   model_uri=ODM.ClinicalData_ItemGroupDataRef, domain=ClinicalData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.ClinicalData_QueryRef = Slot(uri=ODM.QueryRef, name="ClinicalData_QueryRef", curie=ODM.curie('QueryRef'),
                   model_uri=ODM.ClinicalData_QueryRef, domain=ClinicalData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.ClinicalData_AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="ClinicalData_AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.ClinicalData_AuditRecordRef, domain=ClinicalData, range=Optional[Union[dict, "AuditRecord"]])

slots.ClinicalData_SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="ClinicalData_SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.ClinicalData_SignatureRefRef, domain=ClinicalData, range=Optional[Union[str, SignatureID]])

slots.ClinicalData_AnnotationRef = Slot(uri=ODM.AnnotationRef, name="ClinicalData_AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.ClinicalData_AnnotationRef, domain=ClinicalData, range=Optional[Union[str, AnnotationID]])

slots.SubjectData_SubjectKey = Slot(uri=ODM.SubjectKey, name="SubjectData_SubjectKey", curie=ODM.curie('SubjectKey'),
                   model_uri=ODM.SubjectData_SubjectKey, domain=SubjectData, range=str)

slots.SubjectData_TransactionTypeRef = Slot(uri=ODM.TransactionTypeRef, name="SubjectData_TransactionTypeRef", curie=ODM.curie('TransactionTypeRef'),
                   model_uri=ODM.SubjectData_TransactionTypeRef, domain=SubjectData, range=Optional[Union[str, "TransactionType"]])

slots.SubjectData_InvestigatorRefRef = Slot(uri=ODM.InvestigatorRefRef, name="SubjectData_InvestigatorRefRef", curie=ODM.curie('InvestigatorRefRef'),
                   model_uri=ODM.SubjectData_InvestigatorRefRef, domain=SubjectData, range=Optional[Union[dict, "InvestigatorRef"]])

slots.SubjectData_SiteRefRef = Slot(uri=ODM.SiteRefRef, name="SubjectData_SiteRefRef", curie=ODM.curie('SiteRefRef'),
                   model_uri=ODM.SubjectData_SiteRefRef, domain=SubjectData, range=Optional[Union[dict, "SiteRef"]])

slots.SubjectData_StudyEventDataRef = Slot(uri=ODM.StudyEventDataRef, name="SubjectData_StudyEventDataRef", curie=ODM.curie('StudyEventDataRef'),
                   model_uri=ODM.SubjectData_StudyEventDataRef, domain=SubjectData, range=Optional[Union[Union[dict, "StudyEventData"], List[Union[dict, "StudyEventData"]]]])

slots.SubjectData_QueryRef = Slot(uri=ODM.QueryRef, name="SubjectData_QueryRef", curie=ODM.curie('QueryRef'),
                   model_uri=ODM.SubjectData_QueryRef, domain=SubjectData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.SubjectData_AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="SubjectData_AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.SubjectData_AuditRecordRef, domain=SubjectData, range=Optional[Union[dict, "AuditRecord"]])

slots.SubjectData_SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="SubjectData_SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.SubjectData_SignatureRefRef, domain=SubjectData, range=Optional[Union[str, SignatureID]])

slots.SubjectData_AnnotationRef = Slot(uri=ODM.AnnotationRef, name="SubjectData_AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.SubjectData_AnnotationRef, domain=SubjectData, range=Optional[Union[str, AnnotationID]])

slots.SiteRef_LocationOID = Slot(uri=ODM.LocationOID, name="SiteRef_LocationOID", curie=ODM.curie('LocationOID'),
                   model_uri=ODM.SiteRef_LocationOID, domain=SiteRef, range=str)

slots.InvestigatorRef_UserOID = Slot(uri=ODM.UserOID, name="InvestigatorRef_UserOID", curie=ODM.curie('UserOID'),
                   model_uri=ODM.InvestigatorRef_UserOID, domain=InvestigatorRef, range=str)

slots.StudyEventData_StudyEventOID = Slot(uri=ODM.StudyEventOID, name="StudyEventData_StudyEventOID", curie=ODM.curie('StudyEventOID'),
                   model_uri=ODM.StudyEventData_StudyEventOID, domain=StudyEventData, range=str)

slots.StudyEventData_StudyEventRepeatKey = Slot(uri=ODM.StudyEventRepeatKey, name="StudyEventData_StudyEventRepeatKey", curie=ODM.curie('StudyEventRepeatKey'),
                   model_uri=ODM.StudyEventData_StudyEventRepeatKey, domain=StudyEventData, range=Optional[str])

slots.StudyEventData_TransactionTypeRef = Slot(uri=ODM.TransactionTypeRef, name="StudyEventData_TransactionTypeRef", curie=ODM.curie('TransactionTypeRef'),
                   model_uri=ODM.StudyEventData_TransactionTypeRef, domain=StudyEventData, range=Optional[Union[str, "TransactionType"]])

slots.StudyEventData_ItemGroupDataRef = Slot(uri=ODM.ItemGroupDataRef, name="StudyEventData_ItemGroupDataRef", curie=ODM.curie('ItemGroupDataRef'),
                   model_uri=ODM.StudyEventData_ItemGroupDataRef, domain=StudyEventData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.StudyEventData_QueryRef = Slot(uri=ODM.QueryRef, name="StudyEventData_QueryRef", curie=ODM.curie('QueryRef'),
                   model_uri=ODM.StudyEventData_QueryRef, domain=StudyEventData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.StudyEventData_AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="StudyEventData_AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.StudyEventData_AuditRecordRef, domain=StudyEventData, range=Optional[Union[dict, "AuditRecord"]])

slots.StudyEventData_SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="StudyEventData_SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.StudyEventData_SignatureRefRef, domain=StudyEventData, range=Optional[Union[str, SignatureID]])

slots.StudyEventData_AnnotationRef = Slot(uri=ODM.AnnotationRef, name="StudyEventData_AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.StudyEventData_AnnotationRef, domain=StudyEventData, range=Optional[Union[str, AnnotationID]])

slots.ItemGroupData_ItemGroupOID = Slot(uri=ODM.ItemGroupOID, name="ItemGroupData_ItemGroupOID", curie=ODM.curie('ItemGroupOID'),
                   model_uri=ODM.ItemGroupData_ItemGroupOID, domain=ItemGroupData, range=str)

slots.ItemGroupData_ItemGroupRepeatKey = Slot(uri=ODM.ItemGroupRepeatKey, name="ItemGroupData_ItemGroupRepeatKey", curie=ODM.curie('ItemGroupRepeatKey'),
                   model_uri=ODM.ItemGroupData_ItemGroupRepeatKey, domain=ItemGroupData, range=Optional[str])

slots.ItemGroupData_TransactionTypeRef = Slot(uri=ODM.TransactionTypeRef, name="ItemGroupData_TransactionTypeRef", curie=ODM.curie('TransactionTypeRef'),
                   model_uri=ODM.ItemGroupData_TransactionTypeRef, domain=ItemGroupData, range=Optional[Union[str, "TransactionType"]])

slots.ItemGroupData_ItemGroupDataSeq = Slot(uri=ODM.ItemGroupDataSeq, name="ItemGroupData_ItemGroupDataSeq", curie=ODM.curie('ItemGroupDataSeq'),
                   model_uri=ODM.ItemGroupData_ItemGroupDataSeq, domain=ItemGroupData, range=Optional[int])

slots.ItemGroupData_QueryRef = Slot(uri=ODM.QueryRef, name="ItemGroupData_QueryRef", curie=ODM.curie('QueryRef'),
                   model_uri=ODM.ItemGroupData_QueryRef, domain=ItemGroupData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.ItemGroupData_ItemGroupDataRef = Slot(uri=ODM.ItemGroupDataRef, name="ItemGroupData_ItemGroupDataRef", curie=ODM.curie('ItemGroupDataRef'),
                   model_uri=ODM.ItemGroupData_ItemGroupDataRef, domain=ItemGroupData, range=Optional[Union[Union[dict, "ItemGroupData"], List[Union[dict, "ItemGroupData"]]]])

slots.ItemGroupData_ItemDataRef = Slot(uri=ODM.ItemDataRef, name="ItemGroupData_ItemDataRef", curie=ODM.curie('ItemDataRef'),
                   model_uri=ODM.ItemGroupData_ItemDataRef, domain=ItemGroupData, range=Optional[Union[Union[dict, "ItemData"], List[Union[dict, "ItemData"]]]])

slots.ItemGroupData_AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="ItemGroupData_AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.ItemGroupData_AuditRecordRef, domain=ItemGroupData, range=Optional[Union[dict, "AuditRecord"]])

slots.ItemGroupData_SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="ItemGroupData_SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.ItemGroupData_SignatureRefRef, domain=ItemGroupData, range=Optional[Union[str, SignatureID]])

slots.ItemGroupData_AnnotationRef = Slot(uri=ODM.AnnotationRef, name="ItemGroupData_AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.ItemGroupData_AnnotationRef, domain=ItemGroupData, range=Optional[Union[str, AnnotationID]])

slots.ItemData_ItemOID = Slot(uri=ODM.ItemOID, name="ItemData_ItemOID", curie=ODM.curie('ItemOID'),
                   model_uri=ODM.ItemData_ItemOID, domain=ItemData, range=str)

slots.ItemData_TransactionTypeRef = Slot(uri=ODM.TransactionTypeRef, name="ItemData_TransactionTypeRef", curie=ODM.curie('TransactionTypeRef'),
                   model_uri=ODM.ItemData_TransactionTypeRef, domain=ItemData, range=Optional[Union[str, "TransactionType"]])

slots.ItemData_IsNull = Slot(uri=ODM.IsNull, name="ItemData_IsNull", curie=ODM.curie('IsNull'),
                   model_uri=ODM.ItemData_IsNull, domain=ItemData, range=Optional[Union[str, "YesOnly"]])

slots.ItemData_ValueRef = Slot(uri=ODM.ValueRef, name="ItemData_ValueRef", curie=ODM.curie('ValueRef'),
                   model_uri=ODM.ItemData_ValueRef, domain=ItemData, range=Optional[Union[Union[dict, "Value"], List[Union[dict, "Value"]]]])

slots.ItemData_QueryRef = Slot(uri=ODM.QueryRef, name="ItemData_QueryRef", curie=ODM.curie('QueryRef'),
                   model_uri=ODM.ItemData_QueryRef, domain=ItemData, range=Optional[Union[Dict[Union[str, QueryOID], Union[dict, "Query"]], List[Union[dict, "Query"]]]])

slots.ItemData_AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="ItemData_AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.ItemData_AuditRecordRef, domain=ItemData, range=Optional[Union[dict, "AuditRecord"]])

slots.ItemData_SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="ItemData_SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.ItemData_SignatureRefRef, domain=ItemData, range=Optional[Union[str, SignatureID]])

slots.ItemData_AnnotationRef = Slot(uri=ODM.AnnotationRef, name="ItemData_AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.ItemData_AnnotationRef, domain=ItemData, range=Optional[Union[str, AnnotationID]])

slots.AuditRecord_EditPoint = Slot(uri=ODM.EditPoint, name="AuditRecord_EditPoint", curie=ODM.curie('EditPoint'),
                   model_uri=ODM.AuditRecord_EditPoint, domain=AuditRecord, range=Optional[Union[str, "EditPointType"]])

slots.AuditRecord_UsedMethod = Slot(uri=ODM.UsedMethod, name="AuditRecord_UsedMethod", curie=ODM.curie('UsedMethod'),
                   model_uri=ODM.AuditRecord_UsedMethod, domain=AuditRecord, range=Optional[Union[str, "YesOrNo"]])

slots.AuditRecord_UserRefRef = Slot(uri=ODM.UserRefRef, name="AuditRecord_UserRefRef", curie=ODM.curie('UserRefRef'),
                   model_uri=ODM.AuditRecord_UserRefRef, domain=AuditRecord, range=Optional[Union[dict, "UserRef"]])

slots.AuditRecord_LocationRefRef = Slot(uri=ODM.LocationRefRef, name="AuditRecord_LocationRefRef", curie=ODM.curie('LocationRefRef'),
                   model_uri=ODM.AuditRecord_LocationRefRef, domain=AuditRecord, range=Optional[Union[dict, "LocationRef"]])

slots.AuditRecord_DateTimeStampRef = Slot(uri=ODM.DateTimeStampRef, name="AuditRecord_DateTimeStampRef", curie=ODM.curie('DateTimeStampRef'),
                   model_uri=ODM.AuditRecord_DateTimeStampRef, domain=AuditRecord, range=Optional[Union[dict, "DateTimeStamp"]])

slots.AuditRecord_ReasonForChangeRef = Slot(uri=ODM.ReasonForChangeRef, name="AuditRecord_ReasonForChangeRef", curie=ODM.curie('ReasonForChangeRef'),
                   model_uri=ODM.AuditRecord_ReasonForChangeRef, domain=AuditRecord, range=Optional[Union[dict, "ReasonForChange"]])

slots.AuditRecord_SourceIDRef = Slot(uri=ODM.SourceIDRef, name="AuditRecord_SourceIDRef", curie=ODM.curie('SourceIDRef'),
                   model_uri=ODM.AuditRecord_SourceIDRef, domain=AuditRecord, range=Optional[Union[dict, "SourceID"]])

slots.UserRef_UserOID = Slot(uri=ODM.UserOID, name="UserRef_UserOID", curie=ODM.curie('UserOID'),
                   model_uri=ODM.UserRef_UserOID, domain=UserRef, range=str)

slots.LocationRef_LocationOID = Slot(uri=ODM.LocationOID, name="LocationRef_LocationOID", curie=ODM.curie('LocationOID'),
                   model_uri=ODM.LocationRef_LocationOID, domain=LocationRef, range=str)

slots.DateTimeStamp_range = Slot(uri=ODM.range, name="DateTimeStamp_range", curie=ODM.curie('range'),
                   model_uri=ODM.DateTimeStamp_range, domain=DateTimeStamp, range=Optional[str])

slots.ReasonForChange_range = Slot(uri=ODM.range, name="ReasonForChange_range", curie=ODM.curie('range'),
                   model_uri=ODM.ReasonForChange_range, domain=ReasonForChange, range=Optional[str])

slots.SourceID_range = Slot(uri=ODM.range, name="SourceID_range", curie=ODM.curie('range'),
                   model_uri=ODM.SourceID_range, domain=SourceID, range=Optional[str])

slots.Signature_ID = Slot(uri=ODM.ID, name="Signature_ID", curie=ODM.curie('ID'),
                   model_uri=ODM.Signature_ID, domain=Signature, range=Union[str, SignatureID])

slots.Signature_UserRefRef = Slot(uri=ODM.UserRefRef, name="Signature_UserRefRef", curie=ODM.curie('UserRefRef'),
                   model_uri=ODM.Signature_UserRefRef, domain=Signature, range=Optional[Union[dict, UserRef]])

slots.Signature_LocationRefRef = Slot(uri=ODM.LocationRefRef, name="Signature_LocationRefRef", curie=ODM.curie('LocationRefRef'),
                   model_uri=ODM.Signature_LocationRefRef, domain=Signature, range=Optional[Union[dict, LocationRef]])

slots.Signature_SignatureRefRef = Slot(uri=ODM.SignatureRefRef, name="Signature_SignatureRefRef", curie=ODM.curie('SignatureRefRef'),
                   model_uri=ODM.Signature_SignatureRefRef, domain=Signature, range=Optional[Union[dict, "SignatureRef"]])

slots.Signature_DateTimeStampRef = Slot(uri=ODM.DateTimeStampRef, name="Signature_DateTimeStampRef", curie=ODM.curie('DateTimeStampRef'),
                   model_uri=ODM.Signature_DateTimeStampRef, domain=Signature, range=Optional[Union[dict, DateTimeStamp]])

slots.SignatureRef_SignatureOID = Slot(uri=ODM.SignatureOID, name="SignatureRef_SignatureOID", curie=ODM.curie('SignatureOID'),
                   model_uri=ODM.SignatureRef_SignatureOID, domain=SignatureRef, range=str)

slots.Association_StudyOID = Slot(uri=ODM.StudyOID, name="Association_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.Association_StudyOID, domain=Association, range=str)

slots.Association_MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="Association_MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.Association_MetaDataVersionOID, domain=Association, range=str)

slots.Association_KeySetRef = Slot(uri=ODM.KeySetRef, name="Association_KeySetRef", curie=ODM.curie('KeySetRef'),
                   model_uri=ODM.Association_KeySetRef, domain=Association, range=Optional[Union[dict, "KeySet"]])

slots.Association_AnnotationRef = Slot(uri=ODM.AnnotationRef, name="Association_AnnotationRef", curie=ODM.curie('AnnotationRef'),
                   model_uri=ODM.Association_AnnotationRef, domain=Association, range=Optional[Union[str, AnnotationID]])

slots.KeySet_StudyOID = Slot(uri=ODM.StudyOID, name="KeySet_StudyOID", curie=ODM.curie('StudyOID'),
                   model_uri=ODM.KeySet_StudyOID, domain=KeySet, range=str)

slots.KeySet_SubjectKey = Slot(uri=ODM.SubjectKey, name="KeySet_SubjectKey", curie=ODM.curie('SubjectKey'),
                   model_uri=ODM.KeySet_SubjectKey, domain=KeySet, range=Optional[str])

slots.KeySet_MetaDataVersionOID = Slot(uri=ODM.MetaDataVersionOID, name="KeySet_MetaDataVersionOID", curie=ODM.curie('MetaDataVersionOID'),
                   model_uri=ODM.KeySet_MetaDataVersionOID, domain=KeySet, range=Optional[str])

slots.KeySet_StudyEventOID = Slot(uri=ODM.StudyEventOID, name="KeySet_StudyEventOID", curie=ODM.curie('StudyEventOID'),
                   model_uri=ODM.KeySet_StudyEventOID, domain=KeySet, range=Optional[str])

slots.KeySet_StudyEventRepeatKey = Slot(uri=ODM.StudyEventRepeatKey, name="KeySet_StudyEventRepeatKey", curie=ODM.curie('StudyEventRepeatKey'),
                   model_uri=ODM.KeySet_StudyEventRepeatKey, domain=KeySet, range=Optional[str])

slots.KeySet_ItemGroupOID = Slot(uri=ODM.ItemGroupOID, name="KeySet_ItemGroupOID", curie=ODM.curie('ItemGroupOID'),
                   model_uri=ODM.KeySet_ItemGroupOID, domain=KeySet, range=Optional[str])

slots.KeySet_ItemGroupRepeatKey = Slot(uri=ODM.ItemGroupRepeatKey, name="KeySet_ItemGroupRepeatKey", curie=ODM.curie('ItemGroupRepeatKey'),
                   model_uri=ODM.KeySet_ItemGroupRepeatKey, domain=KeySet, range=Optional[str])

slots.KeySet_ItemOID = Slot(uri=ODM.ItemOID, name="KeySet_ItemOID", curie=ODM.curie('ItemOID'),
                   model_uri=ODM.KeySet_ItemOID, domain=KeySet, range=Optional[str])

slots.Annotation_SeqNum = Slot(uri=ODM.SeqNum, name="Annotation_SeqNum", curie=ODM.curie('SeqNum'),
                   model_uri=ODM.Annotation_SeqNum, domain=Annotation, range=int)

slots.Annotation_TransactionTypeRef = Slot(uri=ODM.TransactionTypeRef, name="Annotation_TransactionTypeRef", curie=ODM.curie('TransactionTypeRef'),
                   model_uri=ODM.Annotation_TransactionTypeRef, domain=Annotation, range=Optional[Union[str, "TransactionType"]])

slots.Annotation_ID = Slot(uri=ODM.ID, name="Annotation_ID", curie=ODM.curie('ID'),
                   model_uri=ODM.Annotation_ID, domain=Annotation, range=Union[str, AnnotationID])

slots.Annotation_CommentRef = Slot(uri=ODM.CommentRef, name="Annotation_CommentRef", curie=ODM.curie('CommentRef'),
                   model_uri=ODM.Annotation_CommentRef, domain=Annotation, range=Optional[Union[dict, "Comment"]])

slots.Annotation_CodingRef = Slot(uri=ODM.CodingRef, name="Annotation_CodingRef", curie=ODM.curie('CodingRef'),
                   model_uri=ODM.Annotation_CodingRef, domain=Annotation, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Annotation_FlagRef = Slot(uri=ODM.FlagRef, name="Annotation_FlagRef", curie=ODM.curie('FlagRef'),
                   model_uri=ODM.Annotation_FlagRef, domain=Annotation, range=Optional[Union[Union[dict, "Flag"], List[Union[dict, "Flag"]]]])

slots.Comment_SponsorOrSite = Slot(uri=ODM.SponsorOrSite, name="Comment_SponsorOrSite", curie=ODM.curie('SponsorOrSite'),
                   model_uri=ODM.Comment_SponsorOrSite, domain=Comment, range=Optional[Union[str, "CommentType"]])

slots.Comment_TranslatedTextRef = Slot(uri=ODM.TranslatedTextRef, name="Comment_TranslatedTextRef", curie=ODM.curie('TranslatedTextRef'),
                   model_uri=ODM.Comment_TranslatedTextRef, domain=Comment, range=Optional[Union[Union[dict, TranslatedText], List[Union[dict, TranslatedText]]]])

slots.Flag_FlagValueRef = Slot(uri=ODM.FlagValueRef, name="Flag_FlagValueRef", curie=ODM.curie('FlagValueRef'),
                   model_uri=ODM.Flag_FlagValueRef, domain=Flag, range=Optional[Union[dict, "FlagValue"]])

slots.Flag_FlagTypeRef = Slot(uri=ODM.FlagTypeRef, name="Flag_FlagTypeRef", curie=ODM.curie('FlagTypeRef'),
                   model_uri=ODM.Flag_FlagTypeRef, domain=Flag, range=Optional[Union[dict, "FlagType"]])

slots.FlagValue_CodeListOID = Slot(uri=ODM.CodeListOID, name="FlagValue_CodeListOID", curie=ODM.curie('CodeListOID'),
                   model_uri=ODM.FlagValue_CodeListOID, domain=FlagValue, range=str)

slots.FlagValue__content = Slot(uri=ODM._content, name="FlagValue__content", curie=ODM.curie('_content'),
                   model_uri=ODM.FlagValue__content, domain=FlagValue, range=Optional[str])

slots.FlagType_CodeListOID = Slot(uri=ODM.CodeListOID, name="FlagType_CodeListOID", curie=ODM.curie('CodeListOID'),
                   model_uri=ODM.FlagType_CodeListOID, domain=FlagType, range=str)

slots.FlagType__content = Slot(uri=ODM._content, name="FlagType__content", curie=ODM.curie('_content'),
                   model_uri=ODM.FlagType__content, domain=FlagType, range=Optional[str])

slots.Coding_CodeRef = Slot(uri=ODM.CodeRef, name="Coding_CodeRef", curie=ODM.curie('CodeRef'),
                   model_uri=ODM.Coding_CodeRef, domain=Coding, range=Optional[str])

slots.Coding_System = Slot(uri=ODM.System, name="Coding_System", curie=ODM.curie('System'),
                   model_uri=ODM.Coding_System, domain=Coding, range=Union[str, URIorCURIE])

slots.Coding_SystemName = Slot(uri=ODM.SystemName, name="Coding_SystemName", curie=ODM.curie('SystemName'),
                   model_uri=ODM.Coding_SystemName, domain=Coding, range=Optional[str])

slots.Coding_SystemVersion = Slot(uri=ODM.SystemVersion, name="Coding_SystemVersion", curie=ODM.curie('SystemVersion'),
                   model_uri=ODM.Coding_SystemVersion, domain=Coding, range=Optional[str])

slots.Coding_Label = Slot(uri=ODM.Label, name="Coding_Label", curie=ODM.curie('Label'),
                   model_uri=ODM.Coding_Label, domain=Coding, range=Optional[str])

slots.Coding_href = Slot(uri=ODM.href, name="Coding_href", curie=ODM.curie('href'),
                   model_uri=ODM.Coding_href, domain=Coding, range=Optional[Union[str, URIorCURIE]])

slots.Coding_ref = Slot(uri=ODM.ref, name="Coding_ref", curie=ODM.curie('ref'),
                   model_uri=ODM.Coding_ref, domain=Coding, range=Optional[Union[str, URIorCURIE]])

slots.Coding_CommentOID = Slot(uri=ODM.CommentOID, name="Coding_CommentOID", curie=ODM.curie('CommentOID'),
                   model_uri=ODM.Coding_CommentOID, domain=Coding, range=Optional[str])

slots.Query_OID = Slot(uri=ODM.OID, name="Query_OID", curie=ODM.curie('OID'),
                   model_uri=ODM.Query_OID, domain=Query, range=Union[str, QueryOID])

slots.Query_Source = Slot(uri=ODM.Source, name="Query_Source", curie=ODM.curie('Source'),
                   model_uri=ODM.Query_Source, domain=Query, range=Union[str, "QuerySourceType"])

slots.Query_Target = Slot(uri=ODM.Target, name="Query_Target", curie=ODM.curie('Target'),
                   model_uri=ODM.Query_Target, domain=Query, range=Optional[str])

slots.Query_Type = Slot(uri=ODM.Type, name="Query_Type", curie=ODM.curie('Type'),
                   model_uri=ODM.Query_Type, domain=Query, range=Optional[Union[str, "QueryType"]])

slots.Query_State = Slot(uri=ODM.State, name="Query_State", curie=ODM.curie('State'),
                   model_uri=ODM.Query_State, domain=Query, range=Union[str, "QueryStateType"])

slots.Query_LastUpdateDatetime = Slot(uri=ODM.LastUpdateDatetime, name="Query_LastUpdateDatetime", curie=ODM.curie('LastUpdateDatetime'),
                   model_uri=ODM.Query_LastUpdateDatetime, domain=Query, range=Union[str, XSDDateTime])

slots.Query_Name = Slot(uri=ODM.Name, name="Query_Name", curie=ODM.curie('Name'),
                   model_uri=ODM.Query_Name, domain=Query, range=Optional[str])

slots.Query_ValueRef = Slot(uri=ODM.ValueRef, name="Query_ValueRef", curie=ODM.curie('ValueRef'),
                   model_uri=ODM.Query_ValueRef, domain=Query, range=Optional[Union[dict, "Value"]])

slots.Query_AuditRecordRef = Slot(uri=ODM.AuditRecordRef, name="Query_AuditRecordRef", curie=ODM.curie('AuditRecordRef'),
                   model_uri=ODM.Query_AuditRecordRef, domain=Query, range=Optional[Union[Union[dict, AuditRecord], List[Union[dict, AuditRecord]]]])

slots.Value_SeqNum = Slot(uri=ODM.SeqNum, name="Value_SeqNum", curie=ODM.curie('SeqNum'),
                   model_uri=ODM.Value_SeqNum, domain=Value, range=Optional[int])

slots.Value__content = Slot(uri=ODM._content, name="Value__content", curie=ODM.curie('_content'),
                   model_uri=ODM.Value__content, domain=Value, range=Optional[str])

slots.ODMFileMetadata_FileTypeRef = Slot(uri=ODM.FileTypeRef, name="ODMFileMetadata_FileTypeRef", curie=ODM.curie('FileTypeRef'),
                   model_uri=ODM.ODMFileMetadata_FileTypeRef, domain=ODMFileMetadata, range=Union[str, "FileType"])

slots.ODMFileMetadata_GranularityRef = Slot(uri=ODM.GranularityRef, name="ODMFileMetadata_GranularityRef", curie=ODM.curie('GranularityRef'),
                   model_uri=ODM.ODMFileMetadata_GranularityRef, domain=ODMFileMetadata, range=Optional[Union[str, "Granularity"]])

slots.ODMFileMetadata_ContextRef = Slot(uri=ODM.ContextRef, name="ODMFileMetadata_ContextRef", curie=ODM.curie('ContextRef'),
                   model_uri=ODM.ODMFileMetadata_ContextRef, domain=ODMFileMetadata, range=Optional[Union[str, "Context"]])

slots.ODMFileMetadata_FileOID = Slot(uri=ODM.FileOID, name="ODMFileMetadata_FileOID", curie=ODM.curie('FileOID'),
                   model_uri=ODM.ODMFileMetadata_FileOID, domain=ODMFileMetadata, range=str)

slots.ODMFileMetadata_CreationDateTime = Slot(uri=ODM.CreationDateTime, name="ODMFileMetadata_CreationDateTime", curie=ODM.curie('CreationDateTime'),
                   model_uri=ODM.ODMFileMetadata_CreationDateTime, domain=ODMFileMetadata, range=Union[str, XSDDateTime])

slots.ODMFileMetadata_PriorFileOID = Slot(uri=ODM.PriorFileOID, name="ODMFileMetadata_PriorFileOID", curie=ODM.curie('PriorFileOID'),
                   model_uri=ODM.ODMFileMetadata_PriorFileOID, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_AsOfDateTime = Slot(uri=ODM.AsOfDateTime, name="ODMFileMetadata_AsOfDateTime", curie=ODM.curie('AsOfDateTime'),
                   model_uri=ODM.ODMFileMetadata_AsOfDateTime, domain=ODMFileMetadata, range=Optional[Union[str, XSDDateTime]])

slots.ODMFileMetadata_ODMVersionRef = Slot(uri=ODM.ODMVersionRef, name="ODMFileMetadata_ODMVersionRef", curie=ODM.curie('ODMVersionRef'),
                   model_uri=ODM.ODMFileMetadata_ODMVersionRef, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_Originator = Slot(uri=ODM.Originator, name="ODMFileMetadata_Originator", curie=ODM.curie('Originator'),
                   model_uri=ODM.ODMFileMetadata_Originator, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_SourceSystem = Slot(uri=ODM.SourceSystem, name="ODMFileMetadata_SourceSystem", curie=ODM.curie('SourceSystem'),
                   model_uri=ODM.ODMFileMetadata_SourceSystem, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_SourceSystemVersion = Slot(uri=ODM.SourceSystemVersion, name="ODMFileMetadata_SourceSystemVersion", curie=ODM.curie('SourceSystemVersion'),
                   model_uri=ODM.ODMFileMetadata_SourceSystemVersion, domain=ODMFileMetadata, range=Optional[str])

slots.ODMFileMetadata_DescriptionRef = Slot(uri=ODM.DescriptionRef, name="ODMFileMetadata_DescriptionRef", curie=ODM.curie('DescriptionRef'),
                   model_uri=ODM.ODMFileMetadata_DescriptionRef, domain=ODMFileMetadata, range=Optional[Union[dict, Description]])

slots.ODMFileMetadata_StudyRef = Slot(uri=ODM.StudyRef, name="ODMFileMetadata_StudyRef", curie=ODM.curie('StudyRef'),
                   model_uri=ODM.ODMFileMetadata_StudyRef, domain=ODMFileMetadata, range=Optional[Union[Dict[Union[str, StudyOID], Union[dict, Study]], List[Union[dict, Study]]]])

slots.ODMFileMetadata_AdminDataRef = Slot(uri=ODM.AdminDataRef, name="ODMFileMetadata_AdminDataRef", curie=ODM.curie('AdminDataRef'),
                   model_uri=ODM.ODMFileMetadata_AdminDataRef, domain=ODMFileMetadata, range=Optional[Union[Union[dict, AdminData], List[Union[dict, AdminData]]]])

slots.ODMFileMetadata_ReferenceDataRef = Slot(uri=ODM.ReferenceDataRef, name="ODMFileMetadata_ReferenceDataRef", curie=ODM.curie('ReferenceDataRef'),
                   model_uri=ODM.ODMFileMetadata_ReferenceDataRef, domain=ODMFileMetadata, range=Optional[Union[Union[dict, ReferenceData], List[Union[dict, ReferenceData]]]])

slots.ODMFileMetadata_ClinicalDataRef = Slot(uri=ODM.ClinicalDataRef, name="ODMFileMetadata_ClinicalDataRef", curie=ODM.curie('ClinicalDataRef'),
                   model_uri=ODM.ODMFileMetadata_ClinicalDataRef, domain=ODMFileMetadata, range=Optional[Union[Union[dict, ClinicalData], List[Union[dict, ClinicalData]]]])

slots.ODMFileMetadata_AssociationRef = Slot(uri=ODM.AssociationRef, name="ODMFileMetadata_AssociationRef", curie=ODM.curie('AssociationRef'),
                   model_uri=ODM.ODMFileMetadata_AssociationRef, domain=ODMFileMetadata, range=Optional[Union[Union[dict, Association], List[Union[dict, Association]]]])