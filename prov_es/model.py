
import os, re, types, json, uuid

from prov.model import (ProvDocument, Namespace, Literal, Identifier,
                        PROV, XSD, PROV_ROLE, PROV_LABEL, PROV_TYPE,
                        PROV_LOCATION)

from .constants import *


def get_uuid(s):
    """Return UUID for the string passed in."""

    return str(uuid.uuid5(uuid.NAMESPACE_OID, str(s)))


class ProvEsDocument(ProvDocument):
    """PROV-ES Document."""

    NAMESPACES = [ HYSDS, EOS, GCIS, INFO, BIBO, DCTERMS ]
                   

    def __init__(self, *args, **kwargs):
        """Constructor."""

        # update namespaces
        if 'namespaces' not in kwargs:
            kwargs['namespaces'] = self.NAMESPACES
        else:
            if isinstance(kwargs['namespaces'], dict):
                kwargs['namespaces'] = [ Namespace(prefix, uri) for prefix, uri in
                                         list(kwargs['namespaces'].items()) ]
            kwargs['namespaces'].extend(self.NAMESPACES)

        # track organizations to remove redundancy
        self.prov_es_orgs = {}

        super(ProvEsDocument, self).__init__(*args, **kwargs)


    def collection(self, id, doi=None, shortName=None, longName=None,
                   location=[], sourceInstrument=[], level=None,
                   version=None, title=None, label=None, bundle=None):
        """Return collection PROV entity."""

        attrs = [( PROV_TYPE, EOS_COLLECTION )]
        if doi is not None:
            attrs.append(( INFO_DOI, "%s" % doi ))
        if shortName is not None:
            attrs.append(( EOS_SHORTNAME, "%s" % shortName ))
        if longName is not None:
            attrs.append(( EOS_LONGNAME, "%s" % longName ))
        if len(location) > 0:
            attrs.append(( PROV_LOCATION, tuple(location) ))
        if len(sourceInstrument) > 0:
            attrs.append(( GCIS_SOURCEINSTRUMENT, tuple(sourceInstrument) ))
        if level is not None:
            attrs.append(( EOS_LEVEL, level ))
        if version is not None:
            attrs.append(( EOS_VERSION, version ))
        if title is not None:
            attrs.append(( DCTERMS_TITLE, title ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def dataset(self, id, doi=None, location=[], sourceInstrument=[],
                collection=None, level=None, version=None, title=None,
                label=None, bundle=None, prov_type=EOS_DATASET):
        """Return dataset PROV entity."""

        attrs = [( PROV_TYPE, prov_type )]
        if doi is not None:
            attrs.append(( INFO_DOI, "%s" % doi ))
        if len(location) > 0:
            attrs.append(( PROV_LOCATION, tuple(location) ))
        if len(sourceInstrument) > 0:
            attrs.append(( GCIS_SOURCEINSTRUMENT, tuple(sourceInstrument) ))
        if collection is not None:
            attrs.append(( EOS_PARTOFCOLLECTION, collection ))
        if level is not None:
            attrs.append(( EOS_LEVEL, level ))
        if version is not None:
            attrs.append(( EOS_VERSION, version ))
        if title is not None:
            attrs.append(( DCTERMS_TITLE, title ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def granule(self, id, doi=None, location=[], sourceInstrument=[],
                collection=None, level=None, version=None, title=None,
                label=None, bundle=None):
        """Return granule PROV entity."""

        return self.dataset(id, doi, location, sourceInstrument, collection,
                            level, version, title, label, bundle, EOS_GRANULE)


    def product(self, id, doi=None, location=[], sourceInstrument=[],
                collection=None, level=None, version=None, title=None,
                label=None, bundle=None):
        """Return product PROV entity."""

        return self.dataset(id, doi, location, sourceInstrument, collection,
                            level, version, title, label, bundle, EOS_PRODUCT)


    def file(self, id, location=[], title=None, label=None, bundle=None,
             prov_type=EOS_FILE):
        """Return file PROV entity."""

        attrs = [( PROV_TYPE, prov_type )]
        if len(location) > 0:
            attrs.append(( PROV_LOCATION, tuple(location) ))
        if title is not None:
            attrs.append(( DCTERMS_TITLE, title ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def platform(self, id, hasInstrument=[], label=None, bundle=None):
        """Return platform PROV entity."""

        attrs = [( PROV_TYPE, EOS_PLATFORM )]
        if len(hasInstrument) > 0:
            attrs.append(( GCIS_HASINSTRUMENT, tuple(hasInstrument) ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def instrument(self, id, inPlatform=None, hasSensor=[],
                   hasGoverningOrganization=[], label=None,
                   bundle=None):
        """Return instrument PROV entity."""

        attrs = [( PROV_TYPE, EOS_INSTRUMENT )]
        if inPlatform is not None:
            attrs.append(( GCIS_INPLATFORM, "%s" % inPlatform ))
        if len(hasSensor) > 0:
            attrs.append(( GCIS_HASSENSOR, tuple(hasSensor) ))
        if len(hasGoverningOrganization) > 0:
            for gov_org in hasGoverningOrganization:
                self.governingOrganization(gov_org, bundle=bundle)
            attrs.append(( GCIS_HASGOVERNINGORGANIZATION, tuple(hasGoverningOrganization) ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def sensor(self, id, inInstrument=None, title=None, label=None, bundle=None):
        """Return sensor PROV entity."""

        attrs = [( PROV_TYPE, EOS_SENSOR )]
        if inInstrument is not None:
            attrs.append(( GCIS_ININSTRUMENT, "%s" % inInstrument ))
        if title is not None:
            attrs.append(( DCTERMS_TITLE, title ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def software(self, id, implements=[], version=None, title=None, label=None,
                 location=None, bundle=None):
        """Return software PROV entity."""

        attrs = [( PROV_TYPE, EOS_SOFTWARE )]
        if len(implements) > 0:
            attrs.append(( GCIS_IMPLEMENTS, tuple(implements) ))
        if version is not None:
            attrs.append(( EOS_VERSION, version ))
        if title is not None:
            attrs.append(( DCTERMS_TITLE, title ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if location is not None:
            attrs.append(( PROV_LOCATION, location ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def document(self, id, doi=None, location=[], version=None, label=None,
                 bundle=None):
        """Return document PROV entity."""

        attrs = [( PROV_TYPE, BIBO_DOCUMENT )]
        if doi is not None:
            attrs.append(( INFO_DOI, "%s" % doi ))
        if len(location) > 0:
            attrs.append(( PROV_LOCATION, tuple(location) ))
        if version is not None:
            attrs.append(( EOS_VERSION, version ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def algorithm(self, id, implementedIn=[], describedBy=[], version=None,
                  label=None, bundle=None):
        """Return algorithm PROV entity."""

        attrs = [( PROV_TYPE, EOS_ALGORITHM )]
        if len(implementedIn) > 0:
            attrs.append(( GCIS_IMPLEMENTEDIN, tuple(implementedIn) ))
        if len(describedBy) > 0:
            attrs.append(( EOS_DESCRIBEDBY, tuple(describedBy) ))
        if version is not None:
            attrs.append(( EOS_VERSION, version ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)


    def softwareAgent(self, id, pid=None, host=None, role=None, label=None,
                      bundle=None):
        """Return SoftwareAgent PROV agent."""

        attrs = [( PROV_TYPE, PROV["SoftwareAgent"] )]
        if pid is not None:
            attrs.append(( "hysds:pid", "%s" % pid ))
        if host is not None:
            attrs.append(( "hysds:host", "%s" % host ))
        if role is not None:
            attrs.append(( PROV_ROLE, role ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.agent(id, attrs)
        return self.agent(id, attrs)


    def governingOrganization(self, id, label=None, bundle=None):
        """Return PROV agent for governing organization."""

        if id not in self.prov_es_orgs:
            attrs = [( PROV_TYPE, PROV["Organization"] )]
            if label is not None:
                attrs.append(( PROV_LABEL, label ))
            if bundle: org = bundle.agent(id, attrs)
            else: org = self.agent(id, attrs)
            self.prov_es_orgs[id] = org
        return self.prov_es_orgs[id]


    def runtimeContext(self, id, hasRuntimeParameter=[], label=None, bundle=None):
        """Return runtime context PROV entity."""

        attrs = [( PROV_TYPE, EOS_RUNTIMECONTEXT )]
        if len(hasRuntimeParameter) > 0:
            attrs.append(( EOS_HASRUNTIMEPARAMETER, tuple(hasRuntimeParameter) ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        if bundle: return bundle.entity(id, attrs)
        return self.entity(id, attrs)
        

    def processStep(self, id, start_time=None, end_time=None, usesSoftware=[],
                    wasAssociatedWith=None, runtimeContext=None, 
                    used=[], generated=[], title=None, label=None,
                    bundle=None, prov_type=EOS_PROCESSSTEP,
                    wasAssociatedWithRole=None):
        """Return processStep PROV entity."""

        attrs = [( PROV_TYPE, prov_type )]
        if len(usesSoftware) > 0:
            attrs.append(( EOS_USESSOFTWARE, tuple(usesSoftware) ))
        if wasAssociatedWith is not None:
            waw_id = "hysds:%s" % get_uuid("%s:%s" % (id, wasAssociatedWith))
            waw_attrs = {}
            if wasAssociatedWithRole is not None:
                waw_attrs[PROV_ROLE] = wasAssociatedWithRole
            if bundle:
                bundle.wasAssociatedWith(id, wasAssociatedWith, None, waw_id, waw_attrs)
            else:
                self.wasAssociatedWith(id, wasAssociatedWith, None, waw_id, waw_attrs)
        if runtimeContext is not None:
            attrs.append(( EOS_RUNTIMECONTEXT, "%s" % runtimeContext ))
        if title is not None:
            attrs.append(( DCTERMS_TITLE, title ))
        if label is not None:
            attrs.append(( PROV_LABEL, label ))
        #if len(used) > 0:
        #    attrs.append(( "prov:used", tuple(used) ))
        #if len(generated) > 0:
        #    attrs.append(( "prov:generated", tuple(generated) ))
        if bundle: ps = bundle.activity(id, start_time, end_time, attrs)
        else: ps = self.activity(id, start_time, end_time, attrs)
        input_attrs = [(PROV_ROLE, "input")]
        for input in used:
            if start_time is not None:
                used_id = "hysds:%s" % get_uuid("%s:%s:%s" % (ps, input, start_time))
                if bundle:
                    bundle.used(ps, input, start_time, used_id, input_attrs)
                else:
                    self.used(ps, input, start_time, used_id, input_attrs)
        output_attrs = [(PROV_ROLE, "output")]
        for output in generated:
            if end_time is not None:
                gen_id = "hysds:%s" % get_uuid("%s:%s:%s" % (output, ps, end_time))
                if bundle:
                    bundle.wasGeneratedBy(output, ps, end_time, gen_id, output_attrs)
                else:
                    self.wasGeneratedBy(output, ps, end_time, gen_id, output_attrs)

        return ps
