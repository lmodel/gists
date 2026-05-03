# Auto generated from gistl.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T23:43:34
# Schema: gistl
#
# id: https://w3id.org/model/gistl
# description: gist  is a minimalist upper ontology created by Semantic Arts for enterprise knowledge graph applications. This LinkML schema (version 14.1.0) aggregates the gist modules: Core (classes and properties), MediaTypes (IANA media type instances), and PrefixDeclarations (SHACL namespace bindings). Supplementary schemas gist_rdfs_annotations and gist_sub_class_assertions are available for annotation enrichment and OWL RL reasoner support.
# license: CC-BY-4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Decimal, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Decimal, XSDDateTime

metamodel_version = "1.11.0"
version = "14.1.0"

# Namespaces
GIST_UPSTREAM = CurieNamespace('gist_upstream', 'https://w3id.org/semanticarts/ns/ontology/gist/')
GISTD = CurieNamespace('gistd', 'https://w3id.org/semanticarts/ns/data/gist/')
GISTL = CurieNamespace('gistl', 'https://w3id.org/model/gistl/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MEDIA_APP = CurieNamespace('media_app', 'https://www.iana.org/assignments/media-types/application/')
MEDIA_IMG = CurieNamespace('media_img', 'https://www.iana.org/assignments/media-types/image/')
MEDIA_TXT = CurieNamespace('media_txt', 'https://www.iana.org/assignments/media-types/text/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = GISTL


# Types

# Class references



@dataclass(repr=False)
class Aspect(YAMLRoot):
    """
    A measurable characteristic.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Aspect"]
    class_class_curie: ClassVar[str] = "gist_upstream:Aspect"
    class_name: ClassVar[str] = "Aspect"
    class_model_uri: ClassVar[URIRef] = GISTL.Aspect

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(YAMLRoot):
    """
    A structured entity formed to achieve specific goals, typically involving members with defined roles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Organization"]
    class_class_curie: ClassVar[str] = "gist_upstream:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = GISTL.Organization

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class GovernmentOrganization(Organization):
    """
    An independent organization exercising political and/or regulatory authority over a political unit, people,
    geographical region, etc., as well as performing certain functions for this unit or body.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GovernmentOrganization"]
    class_class_curie: ClassVar[str] = "gist_upstream:GovernmentOrganization"
    class_name: ClassVar[str] = "GovernmentOrganization"
    class_model_uri: ClassVar[URIRef] = GISTL.GovernmentOrganization


@dataclass(repr=False)
class PhysicalIdentifiableItem(YAMLRoot):
    """
    A discrete physical object which, if subdivided, will result in parts that are distinguishable in nature from the
    whole and in general also from the other parts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["PhysicalIdentifiableItem"]
    class_class_curie: ClassVar[str] = "gist_upstream:PhysicalIdentifiableItem"
    class_name: ClassVar[str] = "PhysicalIdentifiableItem"
    class_model_uri: ClassVar[URIRef] = GISTL.PhysicalIdentifiableItem

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(YAMLRoot):
    """
    Something that occurs over a period of time, often characterized as an activity being carried out by some person,
    organization, or software application or brought about by natural forces.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Event"]
    class_class_curie: ClassVar[str] = "gist_upstream:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = GISTL.Event

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class ContemporaryEvent(Event):
    """
    An event that has started but has not yet ended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ContemporaryEvent"]
    class_class_curie: ClassVar[str] = "gist_upstream:ContemporaryEvent"
    class_name: ClassVar[str] = "ContemporaryEvent"
    class_model_uri: ClassVar[URIRef] = GISTL.ContemporaryEvent


@dataclass(repr=False)
class Content(YAMLRoot):
    """
    Information available in some medium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Content"]
    class_class_curie: ClassVar[str] = "gist_upstream:Content"
    class_name: ClassVar[str] = "Content"
    class_model_uri: ClassVar[URIRef] = GISTL.Content

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class ContentExpression(Content):
    """
    Content reduced to text, audio, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ContentExpression"]
    class_class_curie: ClassVar[str] = "gist_upstream:ContentExpression"
    class_name: ClassVar[str] = "ContentExpression"
    class_model_uri: ClassVar[URIRef] = GISTL.ContentExpression


class Text(ContentExpression):
    """
    Content expressed as a written sequence of characters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Text"]
    class_class_curie: ClassVar[str] = "gist_upstream:Text"
    class_name: ClassVar[str] = "Text"
    class_model_uri: ClassVar[URIRef] = GISTL.Text


@dataclass(repr=False)
class GeoLocation(YAMLRoot):
    """
    A physical location, with the earth as a frame of reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GeoLocation"]
    class_class_curie: ClassVar[str] = "gist_upstream:GeoLocation"
    class_name: ClassVar[str] = "GeoLocation"
    class_model_uri: ClassVar[URIRef] = GISTL.GeoLocation

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class GeoPoint(GeoLocation):
    """
    An individual point on or above the Earth's surface, identified by latitude, longitude and altitude. Altitude is
    the distance measured from sea level. If altitude is missing, the point is assumed to be at the Earth's surface.
    These points are described using decimal latitude/longitude.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GeoPoint"]
    class_class_curie: ClassVar[str] = "gist_upstream:GeoPoint"
    class_name: ClassVar[str] = "GeoPoint"
    class_model_uri: ClassVar[URIRef] = GISTL.GeoPoint


class GeoRegion(GeoLocation):
    """
    A bounded region (or set of regions) on the surface of the Earth.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GeoRegion"]
    class_class_curie: ClassVar[str] = "gist_upstream:GeoRegion"
    class_name: ClassVar[str] = "GeoRegion"
    class_model_uri: ClassVar[URIRef] = GISTL.GeoRegion


class ContingentEvent(Event):
    """
    An event with a probability of happening in the future, and usually dependent upon some other event or condition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ContingentEvent"]
    class_class_curie: ClassVar[str] = "gist_upstream:ContingentEvent"
    class_name: ClassVar[str] = "ContingentEvent"
    class_model_uri: ClassVar[URIRef] = GISTL.ContingentEvent


class LivingThing(PhysicalIdentifiableItem):
    """
    Something that is currently, or at some point in time was, alive.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["LivingThing"]
    class_class_curie: ClassVar[str] = "gist_upstream:LivingThing"
    class_name: ClassVar[str] = "LivingThing"
    class_model_uri: ClassVar[URIRef] = GISTL.LivingThing


@dataclass(repr=False)
class Language(YAMLRoot):
    """
    A recognized, organized set of symbols and grammar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Language"]
    class_class_curie: ClassVar[str] = "gist_upstream:Language"
    class_name: ClassVar[str] = "Language"
    class_model_uri: ClassVar[URIRef] = GISTL.Language

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Component(YAMLRoot):
    """
    Something that, while having an independent existence, is inherently part of or designed to be part of a larger
    entity, such as a system or network.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Component"]
    class_class_curie: ClassVar[str] = "gist_upstream:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = GISTL.Component

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class OrderedMember(Component):
    """
    A member of an ordered collection serving as a proxy for a real world item, which can appear in different orders
    in different collections. The ordered member appears in exactly one ordered collection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["OrderedMember"]
    class_class_curie: ClassVar[str] = "gist_upstream:OrderedMember"
    class_name: ClassVar[str] = "OrderedMember"
    class_model_uri: ClassVar[URIRef] = GISTL.OrderedMember


class NetworkLink(Component):
    """
    An abstract representation of the connection between two or more nodes in a network.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["NetworkLink"]
    class_class_curie: ClassVar[str] = "gist_upstream:NetworkLink"
    class_name: ClassVar[str] = "NetworkLink"
    class_model_uri: ClassVar[URIRef] = GISTL.NetworkLink


class GovernedGeoRegion(GeoRegion):
    """
    A geographic region governed by at least one government organization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GovernedGeoRegion"]
    class_class_curie: ClassVar[str] = "gist_upstream:GovernedGeoRegion"
    class_name: ClassVar[str] = "GovernedGeoRegion"
    class_model_uri: ClassVar[URIRef] = GISTL.GovernedGeoRegion


@dataclass(repr=False)
class PhysicalSubstance(YAMLRoot):
    """
    An undifferentiated amount of physical material which, when subdivided, results in each part being
    indistinguishable in nature from the whole and from every other part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["PhysicalSubstance"]
    class_class_curie: ClassVar[str] = "gist_upstream:PhysicalSubstance"
    class_name: ClassVar[str] = "PhysicalSubstance"
    class_model_uri: ClassVar[URIRef] = GISTL.PhysicalSubstance

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeInterval(YAMLRoot):
    """
    A span of time with a known start time, end time, and duration. As long as two of the three are known, the third
    can be inferred.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["TimeInterval"]
    class_class_curie: ClassVar[str] = "gist_upstream:TimeInterval"
    class_name: ClassVar[str] = "TimeInterval"
    class_model_uri: ClassVar[URIRef] = GISTL.TimeInterval

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class GeoVolume(GeoLocation):
    """
    A three-dimensional space on or near the surface of the Earth.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GeoVolume"]
    class_class_curie: ClassVar[str] = "gist_upstream:GeoVolume"
    class_name: ClassVar[str] = "GeoVolume"
    class_model_uri: ClassVar[URIRef] = GISTL.GeoVolume


class SubCountryGovernment(GovernmentOrganization):
    """
    The government of a governed geographic region other than a country which is under the direct or indirect control
    of a country government.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["SubCountryGovernment"]
    class_class_curie: ClassVar[str] = "gist_upstream:SubCountryGovernment"
    class_name: ClassVar[str] = "SubCountryGovernment"
    class_model_uri: ClassVar[URIRef] = GISTL.SubCountryGovernment


@dataclass(repr=False)
class IntellectualProperty(YAMLRoot):
    """
    An intangible work, invention, or concept, independent of its being expressed in text, audio, video, image, or
    live performance. IP can also be tacit knowledge, know-how, or skill.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["IntellectualProperty"]
    class_class_curie: ClassVar[str] = "gist_upstream:IntellectualProperty"
    class_name: ClassVar[str] = "IntellectualProperty"
    class_model_uri: ClassVar[URIRef] = GISTL.IntellectualProperty

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemporalRelation(YAMLRoot):
    """
    A relationship existing for a period of time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["TemporalRelation"]
    class_class_curie: ClassVar[str] = "gist_upstream:TemporalRelation"
    class_name: ClassVar[str] = "TemporalRelation"
    class_model_uri: ClassVar[URIRef] = GISTL.TemporalRelation

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class FormattedContent(ContentExpression):
    """
    Content encoded in a specific format, but existing as data independent of any particular physical medium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["FormattedContent"]
    class_class_curie: ClassVar[str] = "gist_upstream:FormattedContent"
    class_name: ClassVar[str] = "FormattedContent"
    class_model_uri: ClassVar[URIRef] = GISTL.FormattedContent


@dataclass(repr=False)
class Template(YAMLRoot):
    """
    Something used to make objects in its own image.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Template"]
    class_class_curie: ClassVar[str] = "gist_upstream:Template"
    class_name: ClassVar[str] = "Template"
    class_model_uri: ClassVar[URIRef] = GISTL.Template

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class TaskTemplate(Template):
    """
    An outline of a task of a particular type, which is the basis for executing such tasks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["TaskTemplate"]
    class_class_curie: ClassVar[str] = "gist_upstream:TaskTemplate"
    class_name: ClassVar[str] = "TaskTemplate"
    class_model_uri: ClassVar[URIRef] = GISTL.TaskTemplate


class Equipment(PhysicalIdentifiableItem):
    """
    Human-made, tangible property other than land or buildings used to perform a task or activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Equipment"]
    class_class_curie: ClassVar[str] = "gist_upstream:Equipment"
    class_name: ClassVar[str] = "Equipment"
    class_model_uri: ClassVar[URIRef] = GISTL.Equipment


class HistoricalEvent(Event):
    """
    An event which occurred in time, with an actual end earlier than the present moment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["HistoricalEvent"]
    class_class_curie: ClassVar[str] = "gist_upstream:HistoricalEvent"
    class_name: ClassVar[str] = "HistoricalEvent"
    class_model_uri: ClassVar[URIRef] = GISTL.HistoricalEvent


class IntergovernmentalOrganization(Organization):
    """
    An organization whose members are government organizations. This can comprise regional, municipal, state/province,
    or national level entities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["IntergovernmentalOrganization"]
    class_class_curie: ClassVar[str] = "gist_upstream:IntergovernmentalOrganization"
    class_name: ClassVar[str] = "IntergovernmentalOrganization"
    class_model_uri: ClassVar[URIRef] = GISTL.IntergovernmentalOrganization


class Task(Event):
    """
    An activity or piece of work that is either proposed, planned, scheduled, underway, or completed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Task"]
    class_class_curie: ClassVar[str] = "gist_upstream:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = GISTL.Task


class ScheduledTask(Task):
    """
    A task with a planned start datetime.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ScheduledTask"]
    class_class_curie: ClassVar[str] = "gist_upstream:ScheduledTask"
    class_name: ClassVar[str] = "ScheduledTask"
    class_model_uri: ClassVar[URIRef] = GISTL.ScheduledTask


class Project(Task):
    """
    A task, usually of longer duration, made up of other tasks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Project"]
    class_class_curie: ClassVar[str] = "gist_upstream:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = GISTL.Project


@dataclass(repr=False)
class Magnitude(YAMLRoot):
    """
    The amount of a measurable characteristic (aspect).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Magnitude"]
    class_class_curie: ClassVar[str] = "gist_upstream:Magnitude"
    class_name: ClassVar[str] = "Magnitude"
    class_model_uri: ClassVar[URIRef] = GISTL.Magnitude

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class CountryGovernment(GovernmentOrganization):
    """
    A government organization which asserts both sovereignty (i.e., it is not governed by some other government
    organization) and governance over an entity generally recognized as a country.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["CountryGovernment"]
    class_class_curie: ClassVar[str] = "gist_upstream:CountryGovernment"
    class_name: ClassVar[str] = "CountryGovernment"
    class_model_uri: ClassVar[URIRef] = GISTL.CountryGovernment


class CountryGeoRegion(GovernedGeoRegion):
    """
    A geographic region governed by exactly one country government.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["CountryGeoRegion"]
    class_class_curie: ClassVar[str] = "gist_upstream:CountryGeoRegion"
    class_name: ClassVar[str] = "CountryGeoRegion"
    class_model_uri: ClassVar[URIRef] = GISTL.CountryGeoRegion


class PhysicalEvent(Event):
    """
    An event that can be said to have occurred at some place in space.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["PhysicalEvent"]
    class_class_curie: ClassVar[str] = "gist_upstream:PhysicalEvent"
    class_name: ClassVar[str] = "PhysicalEvent"
    class_model_uri: ClassVar[URIRef] = GISTL.PhysicalEvent


@dataclass(repr=False)
class Intention(YAMLRoot):
    """
    A goal, desire, or aspiration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Intention"]
    class_class_curie: ClassVar[str] = "gist_upstream:Intention"
    class_name: ClassVar[str] = "Intention"
    class_model_uri: ClassVar[URIRef] = GISTL.Intention

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class Permission(Intention):
    """
    A description of things one is permitted to do.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Permission"]
    class_class_curie: ClassVar[str] = "gist_upstream:Permission"
    class_name: ClassVar[str] = "Permission"
    class_model_uri: ClassVar[URIRef] = GISTL.Permission


class Requirement(Intention):
    """
    The obligation of a person or organization to behave in a certain way.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Requirement"]
    class_class_curie: ClassVar[str] = "gist_upstream:Requirement"
    class_name: ClassVar[str] = "Requirement"
    class_model_uri: ClassVar[URIRef] = GISTL.Requirement


class Restriction(Intention):
    """
    A description of things one is prevented from doing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Restriction"]
    class_class_curie: ClassVar[str] = "gist_upstream:Restriction"
    class_name: ClassVar[str] = "Restriction"
    class_model_uri: ClassVar[URIRef] = GISTL.Restriction


class Function(Intention):
    """
    The activity that a human-made item is intended to perform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Function"]
    class_class_curie: ClassVar[str] = "gist_upstream:Function"
    class_name: ClassVar[str] = "Function"
    class_model_uri: ClassVar[URIRef] = GISTL.Function


class Specification(Intention):
    """
    The set of characteristics and constraints on their values that specify what it means to be a particular type of
    thing, such as a material, product, service or event. A specification is sufficiently precise to allow evaluating
    conformance to the specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Specification"]
    class_class_curie: ClassVar[str] = "gist_upstream:Specification"
    class_name: ClassVar[str] = "Specification"
    class_model_uri: ClassVar[URIRef] = GISTL.Specification


class ContractTerm(Specification):
    """
    A specification of some aspect of a contract.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ContractTerm"]
    class_class_curie: ClassVar[str] = "gist_upstream:ContractTerm"
    class_name: ClassVar[str] = "ContractTerm"
    class_model_uri: ClassVar[URIRef] = GISTL.ContractTerm


class CatalogItem(Specification):
    """
    A description of a product or service to be delivered, given in a sufficient level of detail that a receiver could
    determine whether delivery constituted discharge of the obligation to deliver.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["CatalogItem"]
    class_class_curie: ClassVar[str] = "gist_upstream:CatalogItem"
    class_name: ClassVar[str] = "CatalogItem"
    class_model_uri: ClassVar[URIRef] = GISTL.CatalogItem


class BundledCatalogItem(CatalogItem):
    """
    Any combination of descriptions of things offered together.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["BundledCatalogItem"]
    class_class_curie: ClassVar[str] = "gist_upstream:BundledCatalogItem"
    class_name: ClassVar[str] = "BundledCatalogItem"
    class_model_uri: ClassVar[URIRef] = GISTL.BundledCatalogItem


class ProductSpecification(CatalogItem):
    """
    A description of something that could be physically warehoused or digitally stored and physically or digitally
    delivered.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ProductSpecification"]
    class_class_curie: ClassVar[str] = "gist_upstream:ProductSpecification"
    class_name: ClassVar[str] = "ProductSpecification"
    class_model_uri: ClassVar[URIRef] = GISTL.ProductSpecification


class Person(LivingThing):
    """
    A human being who was or is alive.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Person"]
    class_class_curie: ClassVar[str] = "gist_upstream:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = GISTL.Person


class Commitment(Intention):
    """
    A promise made by a single party to one or more parties to do or not do something or act in a particular way.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Commitment"]
    class_class_curie: ClassVar[str] = "gist_upstream:Commitment"
    class_name: ClassVar[str] = "Commitment"
    class_model_uri: ClassVar[URIRef] = GISTL.Commitment


class ContingentObligation(Commitment):
    """
    An obligation that is not yet firm. There is some contingent event whose occurrence will cause the obligation to
    become firm.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ContingentObligation"]
    class_class_curie: ClassVar[str] = "gist_upstream:ContingentObligation"
    class_name: ClassVar[str] = "ContingentObligation"
    class_model_uri: ClassVar[URIRef] = GISTL.ContingentObligation


class Offer(ContingentObligation):
    """
    A contingent commitment to buy, sell, swap or provide one or more described or identified goods or services in
    exchange for another (or others).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Offer"]
    class_class_curie: ClassVar[str] = "gist_upstream:Offer"
    class_name: ClassVar[str] = "Offer"
    class_model_uri: ClassVar[URIRef] = GISTL.Offer


class ID(Content):
    """
    Content that is used to uniquely identify something or someone.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ID"]
    class_class_curie: ClassVar[str] = "gist_upstream:ID"
    class_name: ClassVar[str] = "ID"
    class_model_uri: ClassVar[URIRef] = GISTL.ID


@dataclass(repr=False)
class UnitOfMeasure(YAMLRoot):
    """
    A standard amount used to measure or specify things.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["UnitOfMeasure"]
    class_class_curie: ClassVar[str] = "gist_upstream:UnitOfMeasure"
    class_name: ClassVar[str] = "UnitOfMeasure"
    class_model_uri: ClassVar[URIRef] = GISTL.UnitOfMeasure

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class Address(Content):
    """
    A reference to a place (real or virtual) that can be located by some routing algorithm and where messages or
    things can be sent or received.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Address"]
    class_class_curie: ClassVar[str] = "gist_upstream:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = GISTL.Address


class PhysicalAddress(Address):
    """
    An address that refers to a locatable place within the physical universe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["PhysicalAddress"]
    class_class_curie: ClassVar[str] = "gist_upstream:PhysicalAddress"
    class_name: ClassVar[str] = "PhysicalAddress"
    class_model_uri: ClassVar[URIRef] = GISTL.PhysicalAddress


class ElectronicAddress(Address):
    """
    An address referring to a locatable virtual place that does not physically exist but is made by software or
    electronics to appear to do so.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ElectronicAddress"]
    class_class_curie: ClassVar[str] = "gist_upstream:ElectronicAddress"
    class_name: ClassVar[str] = "ElectronicAddress"
    class_model_uri: ClassVar[URIRef] = GISTL.ElectronicAddress


class Landmark(PhysicalIdentifiableItem):
    """
    Something permanently attached to the Earth.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Landmark"]
    class_class_curie: ClassVar[str] = "gist_upstream:Landmark"
    class_name: ClassVar[str] = "Landmark"
    class_model_uri: ClassVar[URIRef] = GISTL.Landmark


@dataclass(repr=False)
class Composite(YAMLRoot):
    """
    Something which is made up of various parts or elements that are independently identifiable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Composite"]
    class_class_curie: ClassVar[str] = "gist_upstream:Composite"
    class_name: ClassVar[str] = "Composite"
    class_model_uri: ClassVar[URIRef] = GISTL.Composite

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class Network(Composite):
    """
    A composite consisting of nodes connected by links.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Network"]
    class_class_curie: ClassVar[str] = "gist_upstream:Network"
    class_name: ClassVar[str] = "Network"
    class_model_uri: ClassVar[URIRef] = GISTL.Network


class Collection(Composite):
    """
    A grouping of things.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Collection"]
    class_class_curie: ClassVar[str] = "gist_upstream:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = GISTL.Collection


class UnitGroup(Collection):
    """
    A collection of units of measure that can all be used to measure the same aspects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["UnitGroup"]
    class_class_curie: ClassVar[str] = "gist_upstream:UnitGroup"
    class_name: ClassVar[str] = "UnitGroup"
    class_model_uri: ClassVar[URIRef] = GISTL.UnitGroup


class ControlledVocabulary(Collection):
    """
    A collection of terms approved and managed by some organization or person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ControlledVocabulary"]
    class_class_curie: ClassVar[str] = "gist_upstream:ControlledVocabulary"
    class_name: ClassVar[str] = "ControlledVocabulary"
    class_model_uri: ClassVar[URIRef] = GISTL.ControlledVocabulary


class System(Composite):
    """
    A composite made up of interacting or interdependent components that together operate as a whole.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["System"]
    class_class_curie: ClassVar[str] = "gist_upstream:System"
    class_name: ClassVar[str] = "System"
    class_model_uri: ClassVar[URIRef] = GISTL.System


class OrderedCollection(Collection):
    """
    A collection whose members are ordered in some way.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["OrderedCollection"]
    class_class_curie: ClassVar[str] = "gist_upstream:OrderedCollection"
    class_name: ClassVar[str] = "OrderedCollection"
    class_model_uri: ClassVar[URIRef] = GISTL.OrderedCollection


class GeoRoute(OrderedCollection):
    """
    An ordered set of geographic points that defines a path from a starting point to an ending point.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GeoRoute"]
    class_class_curie: ClassVar[str] = "gist_upstream:GeoRoute"
    class_name: ClassVar[str] = "GeoRoute"
    class_model_uri: ClassVar[URIRef] = GISTL.GeoRoute


class Transaction(Event):
    """
    An exchange or transfer of goods, services, or funds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Transaction"]
    class_class_curie: ClassVar[str] = "gist_upstream:Transaction"
    class_name: ClassVar[str] = "Transaction"
    class_model_uri: ClassVar[URIRef] = GISTL.Transaction


class KnowledgeConcept(IntellectualProperty):
    """
    An abstract concept that arises from the distillation of experience. It is similar to a category but, rather than
    being a simple tag, it has rich structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["KnowledgeConcept"]
    class_class_curie: ClassVar[str] = "gist_upstream:KnowledgeConcept"
    class_name: ClassVar[str] = "KnowledgeConcept"
    class_model_uri: ClassVar[URIRef] = GISTL.KnowledgeConcept


class RenderedContent(FormattedContent):
    """
    Content expressed via some physical medium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["RenderedContent"]
    class_class_curie: ClassVar[str] = "gist_upstream:RenderedContent"
    class_name: ClassVar[str] = "RenderedContent"
    class_model_uri: ClassVar[URIRef] = GISTL.RenderedContent


class Building(Landmark):
    """
    A relatively permanent man-made structure situated on a plot of land, having a roof and walls, commonly used for
    dwelling, entertaining, or working.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Building"]
    class_class_curie: ClassVar[str] = "gist_upstream:Building"
    class_name: ClassVar[str] = "Building"
    class_model_uri: ClassVar[URIRef] = GISTL.Building


class ServiceSpecification(CatalogItem):
    """
    A description of something that can be done for a person or organization (which produces some form of an act).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ServiceSpecification"]
    class_class_curie: ClassVar[str] = "gist_upstream:ServiceSpecification"
    class_name: ClassVar[str] = "ServiceSpecification"
    class_model_uri: ClassVar[URIRef] = GISTL.ServiceSpecification


class Agreement(Intention):
    """
    A mutually understood arrangement in which two or more parties make commitments to one another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Agreement"]
    class_class_curie: ClassVar[str] = "gist_upstream:Agreement"
    class_name: ClassVar[str] = "Agreement"
    class_model_uri: ClassVar[URIRef] = GISTL.Agreement


class Contract(Agreement):
    """
    An agreement which can be enforced by law.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Contract"]
    class_class_curie: ClassVar[str] = "gist_upstream:Contract"
    class_name: ClassVar[str] = "Contract"
    class_model_uri: ClassVar[URIRef] = GISTL.Contract


class Account(Agreement):
    """
    An agreement having a balance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Account"]
    class_class_curie: ClassVar[str] = "gist_upstream:Account"
    class_name: ClassVar[str] = "Account"
    class_model_uri: ClassVar[URIRef] = GISTL.Account


class ScheduledEvent(Event):
    """
    An event with a planned start datetime.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ScheduledEvent"]
    class_class_curie: ClassVar[str] = "gist_upstream:ScheduledEvent"
    class_name: ClassVar[str] = "ScheduledEvent"
    class_model_uri: ClassVar[URIRef] = GISTL.ScheduledEvent


@dataclass(repr=False)
class Category(YAMLRoot):
    """
    A concept or label used to categorize other instances without specifying any formal semantics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Category"]
    class_class_curie: ClassVar[str] = "gist_upstream:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = GISTL.Category

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class MediaType(Category):
    """
    A digitized type that computer applications can recognize.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["MediaType"]
    class_class_curie: ClassVar[str] = "gist_upstream:MediaType"
    class_name: ClassVar[str] = "MediaType"
    class_model_uri: ClassVar[URIRef] = GISTL.MediaType


class DegreeOfCommitment(Category):
    """
    The difficulty of reversing a commitment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["DegreeOfCommitment"]
    class_class_curie: ClassVar[str] = "gist_upstream:DegreeOfCommitment"
    class_name: ClassVar[str] = "DegreeOfCommitment"
    class_model_uri: ClassVar[URIRef] = GISTL.DegreeOfCommitment


class EquipmentType(Category):
    """
    A category of equipment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["EquipmentType"]
    class_class_curie: ClassVar[str] = "gist_upstream:EquipmentType"
    class_name: ClassVar[str] = "EquipmentType"
    class_model_uri: ClassVar[URIRef] = GISTL.EquipmentType


class ElectronicAddressType(Category):
    """
    A category indicating a kind of electronic address. Such a category is usually based on the technology that
    enables routing to the address referent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ElectronicAddressType"]
    class_class_curie: ClassVar[str] = "gist_upstream:ElectronicAddressType"
    class_name: ClassVar[str] = "ElectronicAddressType"
    class_model_uri: ClassVar[URIRef] = GISTL.ElectronicAddressType


class Tag(Category):
    """
    A term in a folksonomy used to categorize things. Tags can be made up on the fly by users.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Tag"]
    class_class_curie: ClassVar[str] = "gist_upstream:Tag"
    class_name: ClassVar[str] = "Tag"
    class_model_uri: ClassVar[URIRef] = GISTL.Tag


class Behavior(Category):
    """
    A category indicating the nature of an activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Behavior"]
    class_class_curie: ClassVar[str] = "gist_upstream:Behavior"
    class_name: ClassVar[str] = "Behavior"
    class_model_uri: ClassVar[URIRef] = GISTL.Behavior


class GeneralMediaType(Category):
    """
    The real-world media type for content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["GeneralMediaType"]
    class_class_curie: ClassVar[str] = "gist_upstream:GeneralMediaType"
    class_name: ClassVar[str] = "GeneralMediaType"
    class_model_uri: ClassVar[URIRef] = GISTL.GeneralMediaType


class AddressUsageType(Category):
    """
    A category indicating the context or manner in which an address may be used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["AddressUsageType"]
    class_class_curie: ClassVar[str] = "gist_upstream:AddressUsageType"
    class_name: ClassVar[str] = "AddressUsageType"
    class_model_uri: ClassVar[URIRef] = GISTL.AddressUsageType


class Discipline(Category):
    """
    An area of study or practice.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Discipline"]
    class_class_curie: ClassVar[str] = "gist_upstream:Discipline"
    class_name: ClassVar[str] = "Discipline"
    class_model_uri: ClassVar[URIRef] = GISTL.Discipline


class Medium(Category):
    """
    A physical material on which a work can be rendered, represented, or implemented.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Medium"]
    class_class_curie: ClassVar[str] = "gist_upstream:Medium"
    class_name: ClassVar[str] = "Medium"
    class_model_uri: ClassVar[URIRef] = GISTL.Medium


class ProductCategory(Category):
    """
    Any of many ways of categorizing products.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ProductCategory"]
    class_class_curie: ClassVar[str] = "gist_upstream:ProductCategory"
    class_name: ClassVar[str] = "ProductCategory"
    class_model_uri: ClassVar[URIRef] = GISTL.ProductCategory


class PhysicalActionType(Category):
    """
    A category indicating the type of an action based on its effect in the physical world.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["PhysicalActionType"]
    class_class_curie: ClassVar[str] = "gist_upstream:PhysicalActionType"
    class_name: ClassVar[str] = "PhysicalActionType"
    class_model_uri: ClassVar[URIRef] = GISTL.PhysicalActionType


class PhysicalAddressType(Category):
    """
    A category indicating local customary characterizations of physical addresses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["PhysicalAddressType"]
    class_class_curie: ClassVar[str] = "gist_upstream:PhysicalAddressType"
    class_name: ClassVar[str] = "PhysicalAddressType"
    class_model_uri: ClassVar[URIRef] = GISTL.PhysicalAddressType


class Assignment(TemporalRelation):
    """
    A temporal relationship between an assignee, the thing assigned, and the resource that made the assignment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Assignment"]
    class_class_curie: ClassVar[str] = "gist_upstream:Assignment"
    class_name: ClassVar[str] = "Assignment"
    class_model_uri: ClassVar[URIRef] = GISTL.Assignment


@dataclass(repr=False)
class SchemaMetaData(YAMLRoot):
    """
    Superclass for all types of metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["SchemaMetaData"]
    class_class_curie: ClassVar[str] = "gist_upstream:SchemaMetaData"
    class_name: ClassVar[str] = "SchemaMetaData"
    class_model_uri: ClassVar[URIRef] = GISTL.SchemaMetaData

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class Message(ContentExpression):
    """
    A specific instance of content sent from a sender to at least one other recipient.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Message"]
    class_class_curie: ClassVar[str] = "gist_upstream:Message"
    class_name: ClassVar[str] = "Message"
    class_model_uri: ClassVar[URIRef] = GISTL.Message


class NetworkNode(Component):
    """
    A node in a network.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["NetworkNode"]
    class_class_curie: ClassVar[str] = "gist_upstream:NetworkNode"
    class_name: ClassVar[str] = "NetworkNode"
    class_model_uri: ClassVar[URIRef] = GISTL.NetworkNode


class ReferenceValue(Magnitude):
    """
    A magnitude that was neither measured nor estimated but set by fiat.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["ReferenceValue"]
    class_class_curie: ClassVar[str] = "gist_upstream:ReferenceValue"
    class_name: ClassVar[str] = "ReferenceValue"
    class_model_uri: ClassVar[URIRef] = GISTL.ReferenceValue


class Determination(Event):
    """
    An event whose purpose is to establish a specific result, value, or outcome, usually by research, measuring,
    evaluating, or calculating.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["Determination"]
    class_class_curie: ClassVar[str] = "gist_upstream:Determination"
    class_name: ClassVar[str] = "Determination"
    class_model_uri: ClassVar[URIRef] = GISTL.Determination


class EventSpecification(Specification):
    """
    A characterization of an event that might happen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GIST_UPSTREAM["EventSpecification"]
    class_class_curie: ClassVar[str] = "gist_upstream:EventSpecification"
    class_name: ClassVar[str] = "EventSpecification"
    class_model_uri: ClassVar[URIRef] = GISTL.EventSpecification


@dataclass(repr=False)
class GistThing(YAMLRoot):
    """
    Mixin providing universal slots applicable to any GIST entity. Covers OWL properties with no rdfs:domain
    (open-world).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GISTL["GistThing"]
    class_class_curie: ClassVar[str] = "gistl:GistThing"
    class_name: ClassVar[str] = "GistThing"
    class_model_uri: ClassVar[URIRef] = GISTL.GistThing

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class AspectInstance(EnumDefinitionImpl):
    """
    Named instances of gistl:Aspect from gist reference data.
    """
    ASPECT_ALTITUDE = PermissibleValue(
        text="ASPECT_ALTITUDE",
        title="altitude",
        description="The aspect altitude.",
        meaning=GISTD["_Aspect_altitude"])
    ASPECT_AREA = PermissibleValue(
        text="ASPECT_AREA",
        title="area",
        description="The aspect area.",
        meaning=GISTD["_Aspect_area"])
    ASPECT_DURATION = PermissibleValue(
        text="ASPECT_DURATION",
        title="duration",
        description="The aspect duration.",
        meaning=GISTD["_Aspect_duration"])
    ASPECT_FINANCIAL_BALANCE = PermissibleValue(
        text="ASPECT_FINANCIAL_BALANCE",
        title="balance",
        description="The aspect financial balance.",
        meaning=GISTD["_Aspect_financial_balance"])
    ASPECT_MASS = PermissibleValue(
        text="ASPECT_MASS",
        title="mass",
        description="The aspect mass.",
        meaning=GISTD["_Aspect_mass"])
    ASPECT_MONETARY_VALUE = PermissibleValue(
        text="ASPECT_MONETARY_VALUE",
        title="monetary value",
        description="The aspect monetary value.",
        meaning=GISTD["_Aspect_monetary_value"])
    ASPECT_PROBABILITY = PermissibleValue(
        text="ASPECT_PROBABILITY",
        title="probability",
        description="The aspect probability.",
        meaning=GISTD["_Aspect_probability"])
    ASPECT_VOLUME = PermissibleValue(
        text="ASPECT_VOLUME",
        title="volume",
        description="The aspect volume.",
        meaning=GISTD["_Aspect_volume"])

    _defn = EnumDefinition(
        name="AspectInstance",
        description="Named instances of gistl:Aspect from gist reference data.",
    )

class MediaTypeInstance(EnumDefinitionImpl):
    """
    Named instances of gistl:MediaType from gist reference data.
    """
    JSON = PermissibleValue(
        text="JSON",
        title="JSON",
        meaning=MEDIA_APP["json"])
    LD_PLUS_JSON = PermissibleValue(
        text="LD_PLUS_JSON",
        title="JSON-LD",
        meaning=MEDIA_APP["ld+json"])
    N_QUADS = PermissibleValue(
        text="N_QUADS",
        title="N-Quads",
        meaning=MEDIA_APP["n-quads"])
    N_TRIPLES = PermissibleValue(
        text="N_TRIPLES",
        title="N-Triples",
        meaning=MEDIA_APP["n-triples"])
    RDF_PLUS_XML = PermissibleValue(
        text="RDF_PLUS_XML",
        title="RDF/XML",
        meaning=MEDIA_APP["rdf+xml"])
    SPARQL_RESULTS_PLUS_JSON = PermissibleValue(
        text="SPARQL_RESULTS_PLUS_JSON",
        title="SPARQL 1.1 Query Results JSON",
        meaning=MEDIA_APP["sparql-results+json"])
    SPARQL_RESULTS_PLUS_XML = PermissibleValue(
        text="SPARQL_RESULTS_PLUS_XML",
        title="SPARQL 1.1 Query Results XML",
        meaning=MEDIA_APP["sparql-results+xml"])
    TRIG = PermissibleValue(
        text="TRIG",
        title="TriG",
        meaning=MEDIA_APP["trig"])
    JPG = PermissibleValue(
        text="JPG",
        title="JPG",
        meaning=MEDIA_IMG["jpg"])
    PNG = PermissibleValue(
        text="PNG",
        title="PNG",
        meaning=MEDIA_IMG["png"])
    CSV = PermissibleValue(
        text="CSV",
        title="CSV",
        meaning=MEDIA_TXT["csv"])
    HTML = PermissibleValue(
        text="HTML",
        title="HTML",
        meaning=MEDIA_TXT["html"])
    PLAIN = PermissibleValue(
        text="PLAIN",
        title="Plain Text",
        meaning=MEDIA_TXT["plain"])
    TURTLE = PermissibleValue(
        text="TURTLE",
        title="Turtle",
        meaning=MEDIA_TXT["turtle"])

    _defn = EnumDefinition(
        name="MediaTypeInstance",
        description="Named instances of gistl:MediaType from gist reference data.",
    )

class PrefixDeclarationInstance(EnumDefinitionImpl):
    """
    Named SHACL prefix declarations from the gist ontology.
    """
    PREFIXDECLARATION_GIST = PermissibleValue(
        text="PREFIXDECLARATION_GIST",
        title="gist",
        description="Prefix 'gist' for namespace <https://w3id.org/semanticarts/ns/ontology/gist/>.",
        meaning=GIST_UPSTREAM["_PrefixDeclaration_gist"])
    PREFIXDECLARATION_OWL = PermissibleValue(
        text="PREFIXDECLARATION_OWL",
        title="owl",
        description="Prefix 'owl' for namespace <http://www.w3.org/2002/07/owl#>.",
        meaning=GIST_UPSTREAM["_PrefixDeclaration_owl"])
    PREFIXDECLARATION_RDF = PermissibleValue(
        text="PREFIXDECLARATION_RDF",
        title="rdf",
        description="Prefix 'rdf' for namespace <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.",
        meaning=GIST_UPSTREAM["_PrefixDeclaration_rdf"])
    PREFIXDECLARATION_RDFS = PermissibleValue(
        text="PREFIXDECLARATION_RDFS",
        title="rdfs",
        description="Prefix 'rdfs' for namespace <http://www.w3.org/2000/01/rdf-schema#>.",
        meaning=GIST_UPSTREAM["_PrefixDeclaration_rdfs"])
    PREFIXDECLARATION_SH = PermissibleValue(
        text="PREFIXDECLARATION_SH",
        title="sh",
        description="Prefix 'sh' for namespace <http://www.w3.org/ns/shacl#>.",
        meaning=GIST_UPSTREAM["_PrefixDeclaration_sh"])
    PREFIXDECLARATION_SKOS = PermissibleValue(
        text="PREFIXDECLARATION_SKOS",
        title="skos",
        description="Prefix 'skos' for namespace <http://www.w3.org/2004/02/skos/core#>.",
        meaning=GIST_UPSTREAM["_PrefixDeclaration_skos"])
    PREFIXDECLARATION_XSD = PermissibleValue(
        text="PREFIXDECLARATION_XSD",
        title="xsd",
        description="Prefix 'xsd' for namespace <http://www.w3.org/2001/XMLSchema#>.",
        meaning=GIST_UPSTREAM["_PrefixDeclaration_xsd"])

    _defn = EnumDefinition(
        name="PrefixDeclarationInstance",
        description="Named SHACL prefix declarations from the gist ontology.",
    )

# Slots
class slots:
    pass

slots.is_rendered_on = Slot(uri=GIST_UPSTREAM.isRenderedOn, name="is_rendered_on", curie=GIST_UPSTREAM.curie('isRenderedOn'),
                   model_uri=GISTL.is_rendered_on, domain=None, range=Optional[Union[str, list[str]]])

slots.is_made_up_of = Slot(uri=GIST_UPSTREAM.isMadeUpOf, name="is_made_up_of", curie=GIST_UPSTREAM.curie('isMadeUpOf'),
                   model_uri=GISTL.is_made_up_of, domain=None, range=Optional[Union[Union[dict, PhysicalSubstance], list[Union[dict, PhysicalSubstance]]]])

slots.is_based_on = Slot(uri=GIST_UPSTREAM.isBasedOn, name="is_based_on", curie=GIST_UPSTREAM.curie('isBasedOn'),
                   model_uri=GISTL.is_based_on, domain=None, range=Optional[Union[str, list[str]]])

slots.has_unique_navigational_parent = Slot(uri=GIST_UPSTREAM.hasUniqueNavigationalParent, name="has_unique_navigational_parent", curie=GIST_UPSTREAM.curie('hasUniqueNavigationalParent'),
                   model_uri=GISTL.has_unique_navigational_parent, domain=None, range=Optional[Union[str, list[str]]])

slots.goes_to_place = Slot(uri=GIST_UPSTREAM.goesToPlace, name="goes_to_place", curie=GIST_UPSTREAM.curie('goesToPlace'),
                   model_uri=GISTL.goes_to_place, domain=None, range=Optional[Union[str, list[str]]])

slots.has_unique_broader = Slot(uri=GIST_UPSTREAM.hasUniqueBroader, name="has_unique_broader", curie=GIST_UPSTREAM.curie('hasUniqueBroader'),
                   model_uri=GISTL.has_unique_broader, domain=None, range=Optional[Union[str, list[str]]])

slots.is_first_member_of = Slot(uri=GIST_UPSTREAM.isFirstMemberOf, name="is_first_member_of", curie=GIST_UPSTREAM.curie('isFirstMemberOf'),
                   model_uri=GISTL.is_first_member_of, domain=OrderedMember, range=Optional[Union[Union[dict, "OrderedCollection"], list[Union[dict, "OrderedCollection"]]]])

slots.has_address = Slot(uri=GIST_UPSTREAM.hasAddress, name="has_address", curie=GIST_UPSTREAM.curie('hasAddress'),
                   model_uri=GISTL.has_address, domain=None, range=Optional[Union[Union[dict, Address], list[Union[dict, Address]]]])

slots.has_biological_parent = Slot(uri=GIST_UPSTREAM.hasBiologicalParent, name="has_biological_parent", curie=GIST_UPSTREAM.curie('hasBiologicalParent'),
                   model_uri=GISTL.has_biological_parent, domain=LivingThing, range=Optional[Union[Union[dict, "LivingThing"], list[Union[dict, "LivingThing"]]]])

slots.has_goal = Slot(uri=GIST_UPSTREAM.hasGoal, name="has_goal", curie=GIST_UPSTREAM.curie('hasGoal'),
                   model_uri=GISTL.has_goal, domain=None, range=Optional[Union[str, list[str]]])

slots.has_direct_broader = Slot(uri=GIST_UPSTREAM.hasDirectBroader, name="has_direct_broader", curie=GIST_UPSTREAM.curie('hasDirectBroader'),
                   model_uri=GISTL.has_direct_broader, domain=None, range=Optional[Union[str, list[str]]])

slots.is_member_of = Slot(uri=GIST_UPSTREAM.isMemberOf, name="is_member_of", curie=GIST_UPSTREAM.curie('isMemberOf'),
                   model_uri=GISTL.is_member_of, domain=None, range=Optional[Union[str, list[str]]])

slots.is_triggered_by = Slot(uri=GIST_UPSTREAM.isTriggeredBy, name="is_triggered_by", curie=GIST_UPSTREAM.curie('isTriggeredBy'),
                   model_uri=GISTL.is_triggered_by, domain=None, range=Optional[Union[str, list[str]]])

slots.refers_to = Slot(uri=GIST_UPSTREAM.refersTo, name="refers_to", curie=GIST_UPSTREAM.curie('refersTo'),
                   model_uri=GISTL.refers_to, domain=None, range=Optional[Union[str, list[str]]])

slots.is_identified_by = Slot(uri=GIST_UPSTREAM.isIdentifiedBy, name="is_identified_by", curie=GIST_UPSTREAM.curie('isIdentifiedBy'),
                   model_uri=GISTL.is_identified_by, domain=None, range=Optional[Union[Union[dict, ID], list[Union[dict, ID]]]])

slots.has_unit_group = Slot(uri=GIST_UPSTREAM.hasUnitGroup, name="has_unit_group", curie=GIST_UPSTREAM.curie('hasUnitGroup'),
                   model_uri=GISTL.has_unit_group, domain=Aspect, range=Optional[Union[Union[dict, "UnitGroup"], list[Union[dict, "UnitGroup"]]]])

slots.is_about = Slot(uri=GIST_UPSTREAM.isAbout, name="is_about", curie=GIST_UPSTREAM.curie('isAbout'),
                   model_uri=GISTL.is_about, domain=Content, range=Optional[Union[str, list[str]]])

slots.has_recipient = Slot(uri=GIST_UPSTREAM.hasRecipient, name="has_recipient", curie=GIST_UPSTREAM.curie('hasRecipient'),
                   model_uri=GISTL.has_recipient, domain=None, range=Optional[Union[str, list[str]]])

slots.has_accuracy = Slot(uri=GIST_UPSTREAM.hasAccuracy, name="has_accuracy", curie=GIST_UPSTREAM.curie('hasAccuracy'),
                   model_uri=GISTL.has_accuracy, domain=None, range=Optional[Union[Union[dict, Magnitude], list[Union[dict, Magnitude]]]])

slots.links_from = Slot(uri=GIST_UPSTREAM.linksFrom, name="links_from", curie=GIST_UPSTREAM.curie('linksFrom'),
                   model_uri=GISTL.links_from, domain=None, range=Optional[Union[Union[dict, NetworkNode], list[Union[dict, NetworkNode]]]])

slots.is_under_jurisdiction_of = Slot(uri=GIST_UPSTREAM.isUnderJurisdictionOf, name="is_under_jurisdiction_of", curie=GIST_UPSTREAM.curie('isUnderJurisdictionOf'),
                   model_uri=GISTL.is_under_jurisdiction_of, domain=None, range=Optional[Union[Union[dict, GovernmentOrganization], list[Union[dict, GovernmentOrganization]]]])

slots.goes_to_agent = Slot(uri=GIST_UPSTREAM.goesToAgent, name="goes_to_agent", curie=GIST_UPSTREAM.curie('goesToAgent'),
                   model_uri=GISTL.goes_to_agent, domain=None, range=Optional[Union[str, list[str]]])

slots.precedes_directly = Slot(uri=GIST_UPSTREAM.precedesDirectly, name="precedes_directly", curie=GIST_UPSTREAM.curie('precedesDirectly'),
                   model_uri=GISTL.precedes_directly, domain=None, range=Optional[Union[str, list[str]]])

slots.is_expressed_in = Slot(uri=GIST_UPSTREAM.isExpressedIn, name="is_expressed_in", curie=GIST_UPSTREAM.curie('isExpressedIn'),
                   model_uri=GISTL.is_expressed_in, domain=None, range=Optional[Union[Union[dict, Language], list[Union[dict, Language]]]])

slots.comes_from_agent = Slot(uri=GIST_UPSTREAM.comesFromAgent, name="comes_from_agent", curie=GIST_UPSTREAM.curie('comesFromAgent'),
                   model_uri=GISTL.comes_from_agent, domain=None, range=Optional[Union[str, list[str]]])

slots.prohibits = Slot(uri=GIST_UPSTREAM.prohibits, name="prohibits", curie=GIST_UPSTREAM.curie('prohibits'),
                   model_uri=GISTL.prohibits, domain=Intention, range=Optional[Union[Union[dict, "Behavior"], list[Union[dict, "Behavior"]]]])

slots.offers_to_provide = Slot(uri=GIST_UPSTREAM.offersToProvide, name="offers_to_provide", curie=GIST_UPSTREAM.curie('offersToProvide'),
                   model_uri=GISTL.offers_to_provide, domain=None, range=Optional[Union[str, list[str]]])

slots.comes_from_place = Slot(uri=GIST_UPSTREAM.comesFromPlace, name="comes_from_place", curie=GIST_UPSTREAM.curie('comesFromPlace'),
                   model_uri=GISTL.comes_from_place, domain=None, range=Optional[Union[str, list[str]]])

slots.has_broader = Slot(uri=GIST_UPSTREAM.hasBroader, name="has_broader", curie=GIST_UPSTREAM.curie('hasBroader'),
                   model_uri=GISTL.has_broader, domain=None, range=Optional[Union[str, list[str]]])

slots.is_categorized_by = Slot(uri=GIST_UPSTREAM.isCategorizedBy, name="is_categorized_by", curie=GIST_UPSTREAM.curie('isCategorizedBy'),
                   model_uri=GISTL.is_categorized_by, domain=None, range=Optional[Union[Union[dict, Category], list[Union[dict, Category]]]])

slots.requires = Slot(uri=GIST_UPSTREAM.requires, name="requires", curie=GIST_UPSTREAM.curie('requires'),
                   model_uri=GISTL.requires, domain=None, range=Optional[Union[str, list[str]]])

slots.conforms_to = Slot(uri=GIST_UPSTREAM.conformsTo, name="conforms_to", curie=GIST_UPSTREAM.curie('conformsTo'),
                   model_uri=GISTL.conforms_to, domain=None, range=Optional[Union[Union[dict, Intention], list[Union[dict, Intention]]]])

slots.has_multiplier = Slot(uri=GIST_UPSTREAM.hasMultiplier, name="has_multiplier", curie=GIST_UPSTREAM.curie('hasMultiplier'),
                   model_uri=GISTL.has_multiplier, domain=None, range=Optional[Union[str, list[str]]])

slots.links_to = Slot(uri=GIST_UPSTREAM.linksTo, name="links_to", curie=GIST_UPSTREAM.curie('linksTo'),
                   model_uri=GISTL.links_to, domain=None, range=Optional[Union[Union[dict, NetworkNode], list[Union[dict, NetworkNode]]]])

slots.is_produced_by = Slot(uri=GIST_UPSTREAM.isProducedBy, name="is_produced_by", curie=GIST_UPSTREAM.curie('isProducedBy'),
                   model_uri=GISTL.is_produced_by, domain=None, range=Optional[Union[str, list[str]]])

slots.is_assignment_to = Slot(uri=GIST_UPSTREAM.isAssignmentTo, name="is_assignment_to", curie=GIST_UPSTREAM.curie('isAssignmentTo'),
                   model_uri=GISTL.is_assignment_to, domain=None, range=Optional[Union[str, list[str]]])

slots.precedes = Slot(uri=GIST_UPSTREAM.precedes, name="precedes", curie=GIST_UPSTREAM.curie('precedes'),
                   model_uri=GISTL.precedes, domain=None, range=Optional[Union[str, list[str]]])

slots.is_affected_by = Slot(uri=GIST_UPSTREAM.isAffectedBy, name="is_affected_by", curie=GIST_UPSTREAM.curie('isAffectedBy'),
                   model_uri=GISTL.is_affected_by, domain=None, range=Optional[Union[str, list[str]]])

slots.is_recognized_by = Slot(uri=GIST_UPSTREAM.isRecognizedBy, name="is_recognized_by", curie=GIST_UPSTREAM.curie('isRecognizedBy'),
                   model_uri=GISTL.is_recognized_by, domain=None, range=Optional[Union[str, list[str]]])

slots.occurs_in = Slot(uri=GIST_UPSTREAM.occursIn, name="occurs_in", curie=GIST_UPSTREAM.curie('occursIn'),
                   model_uri=GISTL.occurs_in, domain=None, range=Optional[Union[str, list[str]]])

slots.has_participant = Slot(uri=GIST_UPSTREAM.hasParticipant, name="has_participant", curie=GIST_UPSTREAM.curie('hasParticipant'),
                   model_uri=GISTL.has_participant, domain=None, range=Optional[Union[str, list[str]]])

slots.has_navigational_parent = Slot(uri=GIST_UPSTREAM.hasNavigationalParent, name="has_navigational_parent", curie=GIST_UPSTREAM.curie('hasNavigationalParent'),
                   model_uri=GISTL.has_navigational_parent, domain=None, range=Optional[Union[str, list[str]]])

slots.is_connected_to = Slot(uri=GIST_UPSTREAM.isConnectedTo, name="is_connected_to", curie=GIST_UPSTREAM.curie('isConnectedTo'),
                   model_uri=GISTL.is_connected_to, domain=None, range=Optional[Union[str, list[str]]])

slots.has_physical_location = Slot(uri=GIST_UPSTREAM.hasPhysicalLocation, name="has_physical_location", curie=GIST_UPSTREAM.curie('hasPhysicalLocation'),
                   model_uri=GISTL.has_physical_location, domain=None, range=Optional[Union[Union[dict, GeoLocation], list[Union[dict, GeoLocation]]]])

slots.is_part_of = Slot(uri=GIST_UPSTREAM.isPartOf, name="is_part_of", curie=GIST_UPSTREAM.curie('isPartOf'),
                   model_uri=GISTL.is_part_of, domain=None, range=Optional[Union[str, list[str]]])

slots.has_giver = Slot(uri=GIST_UPSTREAM.hasGiver, name="has_giver", curie=GIST_UPSTREAM.curie('hasGiver'),
                   model_uri=GISTL.has_giver, domain=None, range=Optional[Union[str, list[str]]])

slots.is_geo_contained_in = Slot(uri=GIST_UPSTREAM.isGeoContainedIn, name="is_geo_contained_in", curie=GIST_UPSTREAM.curie('isGeoContainedIn'),
                   model_uri=GISTL.is_geo_contained_in, domain=GeoLocation, range=Optional[Union[Union[dict, "GeoLocation"], list[Union[dict, "GeoLocation"]]]])

slots.has_aspect = Slot(uri=GIST_UPSTREAM.hasAspect, name="has_aspect", curie=GIST_UPSTREAM.curie('hasAspect'),
                   model_uri=GISTL.has_aspect, domain=None, range=Optional[Union[Union[dict, Aspect], list[Union[dict, Aspect]]]])

slots.has_divisor = Slot(uri=GIST_UPSTREAM.hasDivisor, name="has_divisor", curie=GIST_UPSTREAM.curie('hasDivisor'),
                   model_uri=GISTL.has_divisor, domain=None, range=Optional[Union[str, list[str]]])

slots.has_party = Slot(uri=GIST_UPSTREAM.hasParty, name="has_party", curie=GIST_UPSTREAM.curie('hasParty'),
                   model_uri=GISTL.has_party, domain=None, range=Optional[Union[str, list[str]]])

slots.is_allocated_by = Slot(uri=GIST_UPSTREAM.isAllocatedBy, name="is_allocated_by", curie=GIST_UPSTREAM.curie('isAllocatedBy'),
                   model_uri=GISTL.is_allocated_by, domain=None, range=Optional[Union[str, list[str]]])

slots.has_addend = Slot(uri=GIST_UPSTREAM.hasAddend, name="has_addend", curie=GIST_UPSTREAM.curie('hasAddend'),
                   model_uri=GISTL.has_addend, domain=None, range=Optional[Union[str, list[str]]])

slots.has_magnitude = Slot(uri=GIST_UPSTREAM.hasMagnitude, name="has_magnitude", curie=GIST_UPSTREAM.curie('hasMagnitude'),
                   model_uri=GISTL.has_magnitude, domain=None, range=Optional[Union[Union[dict, Magnitude], list[Union[dict, Magnitude]]]])

slots.is_assignment_of = Slot(uri=GIST_UPSTREAM.isAssignmentOf, name="is_assignment_of", curie=GIST_UPSTREAM.curie('isAssignmentOf'),
                   model_uri=GISTL.is_assignment_of, domain=None, range=Optional[Union[str, list[str]]])

slots.allows = Slot(uri=GIST_UPSTREAM.allows, name="allows", curie=GIST_UPSTREAM.curie('allows'),
                   model_uri=GISTL.allows, domain=None, range=Optional[Union[str, list[str]]])

slots.is_governed_by = Slot(uri=GIST_UPSTREAM.isGovernedBy, name="is_governed_by", curie=GIST_UPSTREAM.curie('isGovernedBy'),
                   model_uri=GISTL.is_governed_by, domain=None, range=Optional[Union[str, list[str]]])

slots.is_direct_part_of = Slot(uri=GIST_UPSTREAM.isDirectPartOf, name="is_direct_part_of", curie=GIST_UPSTREAM.curie('isDirectPartOf'),
                   model_uri=GISTL.is_direct_part_of, domain=None, range=Optional[Union[str, list[str]]])

slots.has_subtrahend = Slot(uri=GIST_UPSTREAM.hasSubtrahend, name="has_subtrahend", curie=GIST_UPSTREAM.curie('hasSubtrahend'),
                   model_uri=GISTL.has_subtrahend, domain=None, range=Optional[Union[str, list[str]]])

slots.has_incumbent = Slot(uri=GIST_UPSTREAM.hasIncumbent, name="has_incumbent", curie=GIST_UPSTREAM.curie('hasIncumbent'),
                   model_uri=GISTL.has_incumbent, domain=None, range=Optional[Union[str, list[str]]])

slots.has_unit_of_measure = Slot(uri=GIST_UPSTREAM.hasUnitOfMeasure, name="has_unit_of_measure", curie=GIST_UPSTREAM.curie('hasUnitOfMeasure'),
                   model_uri=GISTL.has_unit_of_measure, domain=Magnitude, range=Optional[Union[Union[dict, "UnitOfMeasure"], list[Union[dict, "UnitOfMeasure"]]]])

slots.prevents = Slot(uri=GIST_UPSTREAM.prevents, name="prevents", curie=GIST_UPSTREAM.curie('prevents'),
                   model_uri=GISTL.prevents, domain=Intention, range=Optional[Union[Union[dict, "Behavior"], list[Union[dict, "Behavior"]]]])

slots.offers_to_receive = Slot(uri=GIST_UPSTREAM.offersToReceive, name="offers_to_receive", curie=GIST_UPSTREAM.curie('offersToReceive'),
                   model_uri=GISTL.offers_to_receive, domain=None, range=Optional[Union[str, list[str]]])

slots.owns = Slot(uri=GIST_UPSTREAM.owns, name="owns", curie=GIST_UPSTREAM.curie('owns'),
                   model_uri=GISTL.owns, domain=Organization, range=Optional[Union[str, list[str]]])

slots.provides_order_for = Slot(uri=GIST_UPSTREAM.providesOrderFor, name="provides_order_for", curie=GIST_UPSTREAM.curie('providesOrderFor'),
                   model_uri=GISTL.provides_order_for, domain=OrderedMember, range=Optional[Union[str, list[str]]])

slots.links = Slot(uri=GIST_UPSTREAM.links, name="links", curie=GIST_UPSTREAM.curie('links'),
                   model_uri=GISTL.links, domain=None, range=Optional[Union[Union[dict, NetworkNode], list[Union[dict, NetworkNode]]]])

slots.contributes_to = Slot(uri=GIST_UPSTREAM.contributesTo, name="contributes_to", curie=GIST_UPSTREAM.curie('contributesTo'),
                   model_uri=GISTL.contributes_to, domain=None, range=Optional[Union[str, list[str]]])

slots.symbol = Slot(uri=GIST_UPSTREAM.symbol, name="symbol", curie=GIST_UPSTREAM.curie('symbol'),
                   model_uri=GISTL.symbol, domain=None, range=Optional[str])

slots.exponent_of_steradian = Slot(uri=GIST_UPSTREAM.exponentOfSteradian, name="exponent_of_steradian", curie=GIST_UPSTREAM.curie('exponentOfSteradian'),
                   model_uri=GISTL.exponent_of_steradian, domain=UnitGroup, range=Optional[Decimal])

slots.actual_start_minute = Slot(uri=GIST_UPSTREAM.actualStartMinute, name="actual_start_minute", curie=GIST_UPSTREAM.curie('actualStartMinute'),
                   model_uri=GISTL.actual_start_minute, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.latitude = Slot(uri=GIST_UPSTREAM.latitude, name="latitude", curie=GIST_UPSTREAM.curie('latitude'),
                   model_uri=GISTL.latitude, domain=GeoPoint, range=Optional[float])

slots.planned_start_date = Slot(uri=GIST_UPSTREAM.plannedStartDate, name="planned_start_date", curie=GIST_UPSTREAM.curie('plannedStartDate'),
                   model_uri=GISTL.planned_start_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.end_date_time = Slot(uri=GIST_UPSTREAM.endDateTime, name="end_date_time", curie=GIST_UPSTREAM.curie('endDateTime'),
                   model_uri=GISTL.end_date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.planned_end_date_time = Slot(uri=GIST_UPSTREAM.plannedEndDateTime, name="planned_end_date_time", curie=GIST_UPSTREAM.curie('plannedEndDateTime'),
                   model_uri=GISTL.planned_end_date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.actual_end_minute = Slot(uri=GIST_UPSTREAM.actualEndMinute, name="actual_end_minute", curie=GIST_UPSTREAM.curie('actualEndMinute'),
                   model_uri=GISTL.actual_end_minute, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exponent_of_mole = Slot(uri=GIST_UPSTREAM.exponentOfMole, name="exponent_of_mole", curie=GIST_UPSTREAM.curie('exponentOfMole'),
                   model_uri=GISTL.exponent_of_mole, domain=UnitGroup, range=Optional[Decimal])

slots.start_date_time = Slot(uri=GIST_UPSTREAM.startDateTime, name="start_date_time", curie=GIST_UPSTREAM.curie('startDateTime'),
                   model_uri=GISTL.start_date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.conversion_offset = Slot(uri=GIST_UPSTREAM.conversionOffset, name="conversion_offset", curie=GIST_UPSTREAM.curie('conversionOffset'),
                   model_uri=GISTL.conversion_offset, domain=UnitOfMeasure, range=Optional[Decimal])

slots.exponent_of_bit = Slot(uri=GIST_UPSTREAM.exponentOfBit, name="exponent_of_bit", curie=GIST_UPSTREAM.curie('exponentOfBit'),
                   model_uri=GISTL.exponent_of_bit, domain=UnitGroup, range=Optional[Decimal])

slots.exponent_of_meter = Slot(uri=GIST_UPSTREAM.exponentOfMeter, name="exponent_of_meter", curie=GIST_UPSTREAM.curie('exponentOfMeter'),
                   model_uri=GISTL.exponent_of_meter, domain=UnitGroup, range=Optional[Decimal])

slots.contained_text = Slot(uri=GIST_UPSTREAM.containedText, name="contained_text", curie=GIST_UPSTREAM.curie('containedText'),
                   model_uri=GISTL.contained_text, domain=None, range=Optional[str])

slots.conversion_factor = Slot(uri=GIST_UPSTREAM.conversionFactor, name="conversion_factor", curie=GIST_UPSTREAM.curie('conversionFactor'),
                   model_uri=GISTL.conversion_factor, domain=UnitOfMeasure, range=Optional[str])

slots.encrypted_text = Slot(uri=GIST_UPSTREAM.encryptedText, name="encrypted_text", curie=GIST_UPSTREAM.curie('encryptedText'),
                   model_uri=GISTL.encrypted_text, domain=None, range=Optional[str])

slots.actual_start_year = Slot(uri=GIST_UPSTREAM.actualStartYear, name="actual_start_year", curie=GIST_UPSTREAM.curie('actualStartYear'),
                   model_uri=GISTL.actual_start_year, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exponent_of_us_dollar = Slot(uri=GIST_UPSTREAM.exponentOfUSDollar, name="exponent_of_us_dollar", curie=GIST_UPSTREAM.curie('exponentOfUSDollar'),
                   model_uri=GISTL.exponent_of_us_dollar, domain=UnitGroup, range=Optional[Decimal])

slots.exponent_of_kelvin = Slot(uri=GIST_UPSTREAM.exponentOfKelvin, name="exponent_of_kelvin", curie=GIST_UPSTREAM.curie('exponentOfKelvin'),
                   model_uri=GISTL.exponent_of_kelvin, domain=UnitGroup, range=Optional[Decimal])

slots.exponent_of_ampere = Slot(uri=GIST_UPSTREAM.exponentOfAmpere, name="exponent_of_ampere", curie=GIST_UPSTREAM.curie('exponentOfAmpere'),
                   model_uri=GISTL.exponent_of_ampere, domain=UnitGroup, range=Optional[Decimal])

slots.exponent_of_radian = Slot(uri=GIST_UPSTREAM.exponentOfRadian, name="exponent_of_radian", curie=GIST_UPSTREAM.curie('exponentOfRadian'),
                   model_uri=GISTL.exponent_of_radian, domain=UnitGroup, range=Optional[Decimal])

slots.id_text = Slot(uri=GIST_UPSTREAM.idText, name="id_text", curie=GIST_UPSTREAM.curie('idText'),
                   model_uri=GISTL.id_text, domain=None, range=Optional[str])

slots.actual_start_date_time = Slot(uri=GIST_UPSTREAM.actualStartDateTime, name="actual_start_date_time", curie=GIST_UPSTREAM.curie('actualStartDateTime'),
                   model_uri=GISTL.actual_start_date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.actual_end_year = Slot(uri=GIST_UPSTREAM.actualEndYear, name="actual_end_year", curie=GIST_UPSTREAM.curie('actualEndYear'),
                   model_uri=GISTL.actual_end_year, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.actual_start_microsecond = Slot(uri=GIST_UPSTREAM.actualStartMicrosecond, name="actual_start_microsecond", curie=GIST_UPSTREAM.curie('actualStartMicrosecond'),
                   model_uri=GISTL.actual_start_microsecond, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.actual_end_microsecond = Slot(uri=GIST_UPSTREAM.actualEndMicrosecond, name="actual_end_microsecond", curie=GIST_UPSTREAM.curie('actualEndMicrosecond'),
                   model_uri=GISTL.actual_end_microsecond, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.is_recorded_at = Slot(uri=GIST_UPSTREAM.isRecordedAt, name="is_recorded_at", curie=GIST_UPSTREAM.curie('isRecordedAt'),
                   model_uri=GISTL.is_recorded_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.planned_start_date_time = Slot(uri=GIST_UPSTREAM.plannedStartDateTime, name="planned_start_date_time", curie=GIST_UPSTREAM.curie('plannedStartDateTime'),
                   model_uri=GISTL.planned_start_date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exponent_of_candela = Slot(uri=GIST_UPSTREAM.exponentOfCandela, name="exponent_of_candela", curie=GIST_UPSTREAM.curie('exponentOfCandela'),
                   model_uri=GISTL.exponent_of_candela, domain=UnitGroup, range=Optional[Decimal])

slots.description = Slot(uri=GIST_UPSTREAM.description, name="description", curie=GIST_UPSTREAM.curie('description'),
                   model_uri=GISTL.description, domain=None, range=Optional[str])

slots.exponent_of_second = Slot(uri=GIST_UPSTREAM.exponentOfSecond, name="exponent_of_second", curie=GIST_UPSTREAM.curie('exponentOfSecond'),
                   model_uri=GISTL.exponent_of_second, domain=UnitGroup, range=Optional[Decimal])

slots.planned_end_date = Slot(uri=GIST_UPSTREAM.plannedEndDate, name="planned_end_date", curie=GIST_UPSTREAM.curie('plannedEndDate'),
                   model_uri=GISTL.planned_end_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exponent_of_kilogram = Slot(uri=GIST_UPSTREAM.exponentOfKilogram, name="exponent_of_kilogram", curie=GIST_UPSTREAM.curie('exponentOfKilogram'),
                   model_uri=GISTL.exponent_of_kilogram, domain=UnitGroup, range=Optional[Decimal])

slots.unique_text = Slot(uri=GIST_UPSTREAM.uniqueText, name="unique_text", curie=GIST_UPSTREAM.curie('uniqueText'),
                   model_uri=GISTL.unique_text, domain=None, range=Optional[str])

slots.actual_start_date = Slot(uri=GIST_UPSTREAM.actualStartDate, name="actual_start_date", curie=GIST_UPSTREAM.curie('actualStartDate'),
                   model_uri=GISTL.actual_start_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exponent_of_number = Slot(uri=GIST_UPSTREAM.exponentOfNumber, name="exponent_of_number", curie=GIST_UPSTREAM.curie('exponentOfNumber'),
                   model_uri=GISTL.exponent_of_number, domain=UnitGroup, range=Optional[Decimal])

slots.sequence = Slot(uri=GIST_UPSTREAM.sequence, name="sequence", curie=GIST_UPSTREAM.curie('sequence'),
                   model_uri=GISTL.sequence, domain=None, range=Optional[int])

slots.planned_end_year = Slot(uri=GIST_UPSTREAM.plannedEndYear, name="planned_end_year", curie=GIST_UPSTREAM.curie('plannedEndYear'),
                   model_uri=GISTL.planned_end_year, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.at_date_time = Slot(uri=GIST_UPSTREAM.atDateTime, name="at_date_time", curie=GIST_UPSTREAM.curie('atDateTime'),
                   model_uri=GISTL.at_date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.name = Slot(uri=GIST_UPSTREAM.name, name="name", curie=GIST_UPSTREAM.curie('name'),
                   model_uri=GISTL.name, domain=None, range=Optional[str])

slots.planned_start_year = Slot(uri=GIST_UPSTREAM.plannedStartYear, name="planned_start_year", curie=GIST_UPSTREAM.curie('plannedStartYear'),
                   model_uri=GISTL.planned_start_year, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.birth_date = Slot(uri=GIST_UPSTREAM.birthDate, name="birth_date", curie=GIST_UPSTREAM.curie('birthDate'),
                   model_uri=GISTL.birth_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.planned_end_minute = Slot(uri=GIST_UPSTREAM.plannedEndMinute, name="planned_end_minute", curie=GIST_UPSTREAM.curie('plannedEndMinute'),
                   model_uri=GISTL.planned_end_minute, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.actual_end_date_time = Slot(uri=GIST_UPSTREAM.actualEndDateTime, name="actual_end_date_time", curie=GIST_UPSTREAM.curie('actualEndDateTime'),
                   model_uri=GISTL.actual_end_date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.actual_end_date = Slot(uri=GIST_UPSTREAM.actualEndDate, name="actual_end_date", curie=GIST_UPSTREAM.curie('actualEndDate'),
                   model_uri=GISTL.actual_end_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exponent_of_other = Slot(uri=GIST_UPSTREAM.exponentOfOther, name="exponent_of_other", curie=GIST_UPSTREAM.curie('exponentOfOther'),
                   model_uri=GISTL.exponent_of_other, domain=UnitGroup, range=Optional[Decimal])

slots.planned_start_minute = Slot(uri=GIST_UPSTREAM.plannedStartMinute, name="planned_start_minute", curie=GIST_UPSTREAM.curie('plannedStartMinute'),
                   model_uri=GISTL.planned_start_minute, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.longitude = Slot(uri=GIST_UPSTREAM.longitude, name="longitude", curie=GIST_UPSTREAM.curie('longitude'),
                   model_uri=GISTL.longitude, domain=GeoPoint, range=Optional[float])

slots.numeric_value = Slot(uri=GIST_UPSTREAM.numericValue, name="numeric_value", curie=GIST_UPSTREAM.curie('numericValue'),
                   model_uri=GISTL.numeric_value, domain=None, range=Optional[str])

slots.death_date = Slot(uri=GIST_UPSTREAM.deathDate, name="death_date", curie=GIST_UPSTREAM.curie('deathDate'),
                   model_uri=GISTL.death_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.is_superseded_by = Slot(uri=GIST_UPSTREAM.isSupersededBy, name="is_superseded_by", curie=GIST_UPSTREAM.curie('isSupersededBy'),
                   model_uri=GISTL.is_superseded_by, domain=None, range=Optional[str])

slots.domain_includes = Slot(uri=GIST_UPSTREAM.domainIncludes, name="domain_includes", curie=GIST_UPSTREAM.curie('domainIncludes'),
                   model_uri=GISTL.domain_includes, domain=None, range=Optional[str])

slots.license = Slot(uri=GIST_UPSTREAM.license, name="license", curie=GIST_UPSTREAM.curie('license'),
                   model_uri=GISTL.license, domain=None, range=Optional[str])

slots.range_includes = Slot(uri=GIST_UPSTREAM.rangeIncludes, name="range_includes", curie=GIST_UPSTREAM.curie('rangeIncludes'),
                   model_uri=GISTL.range_includes, domain=None, range=Optional[str])
