from prov.identifier import Namespace

HYSDS = Namespace('hysds', 'http://hysds.domain.com/hysds/0.1#')
EOS = Namespace('eos', 'http://nasa.gov/eos.owl#')
GCIS = Namespace('gcis', 'http://data.globalchange.gov/gcis.owl#')
INFO = Namespace('info', 'http://info-uri.info/')
BIBO = Namespace('bibo', 'http://purl.org/ontology/bibo/')
DCTERMS = Namespace('dcterms', 'http://purl.org/dc/terms/')


# EOS convenience defs
EOS_COLLECTION = EOS['collection']
EOS_SHORTNAME = EOS['shortName']
EOS_LONGNAME = EOS['longName']
EOS_LEVEL = EOS['level']
EOS_VERSION = EOS['version']
EOS_DATASET = EOS['dataset']
EOS_PARTOFCOLLECTION = EOS['partOfCollection']
EOS_GRANULE = EOS['granule']
EOS_PRODUCT = EOS['product']
EOS_FILE = EOS['file']
EOS_PLATFORM = EOS['platform']
EOS_INSTRUMENT = EOS['instrument']
EOS_SENSOR = EOS['sensor']
EOS_SOFTWARE = EOS['software']
EOS_ALGORITHM = EOS['algorithm']
EOS_DESCRIBEDBY = EOS['describedBy']
EOS_RUNTIMECONTEXT = EOS['runtimeContext']
EOS_HASRUNTIMEPARAMETER = EOS['hasRuntimeParameter']
EOS_PROCESSSTEP = EOS['processStep']
EOS_USESSOFTWARE = EOS['usesSoftware']

# GCIS convenience defs
GCIS_SOURCEINSTRUMENT = GCIS['sourceInstrument']
GCIS_HASINSTRUMENT = GCIS['hasInstrument']
GCIS_ININSTRUMENT = GCIS['inInstrument']
GCIS_INPLATFORM = GCIS['inPlatform']
GCIS_HASSENSOR = GCIS['hasSensor']
GCIS_HASGOVERNINGORGANIZATION = GCIS['hasGoverningOrganization']
GCIS_IMPLEMENTS = GCIS['implements']
GCIS_IMPLEMENTEDIN = GCIS['implementedIn']

# info convenience defs
INFO_DOI = INFO['doi']

# bibo convenience defs
BIBO_DOCUMENT = BIBO['Document']

# dcterms convenience defs
DCTERMS_TITLE = DCTERMS['title']
