########
Tutorial
########

Installation
============

Download the code::

  git clone http://github.com/pymonger/prov_es.git

and install::

  cd prov_es
  python setup.py install


Quick Start
===========

Create PROV-ES document::

    from datetime import datetime, timedelta
    from prov_es.model import ProvEsDocument

    # create doc
    doc = ProvEsDocument()

    # input dataset
    id = "hysds:INSAR2_RAW_HI_06_HH_RA_20140922062622_20140922062629"
    doi = "10.5067/ARIAMH/INSAR/Scene"
    downloadURL = 'https://dav.domain.com/repository/products/insar/v0.2/2014/09/22/INSAR2_RAW_HI_06_HH_RA_20140922062622_20140922062629/INSAR20140922_913686_3720875'
    instrument = "eos:INSAR2-SAR"
    level = "L0"
    doc.dataset(id, doi, [downloadURL], [instrument], None, level)

    # input DEM
    dem_id = "hysds:srtm/version2_1/SRTM1/Region_01/N31W114"
    dem_doi = None
    dem_downloadURL = 'https://dav.domain.com/repository/products/srtm/version2_1/SRTM1/Region_01/N31W114.hgt.zip'
    dem_level = "L0"
    doc.dataset(dem_id, dem_doi, [dem_downloadURL], [], None, dem_level)

    # platform
    platform = "eos:INSAR2"
    doc.platform(platform, [instrument])

    # second instrument/platform from same org
    instrument2 = "eos:INSAR4-SAR"
    platform2 = "eos:INSAR4"
    doc.platform(platform2, [instrument2])

    # instrument
    sensor = "eos:SAR"
    gov_org = "eos:ASI"
    doc.instrument(instrument, platform, [sensor], [gov_org])
    doc.sensor(sensor, instrument)
    doc.instrument(instrument2, platform2, [sensor], [gov_org])
    doc.sensor(sensor, instrument2)

    # software
    software = "eos:ISCE"
    algorithm = "eos:interferogram_creation"
    doc.software(software, [algorithm])

    # document
    atbd_id = "eos:interferogram_creation_atbd"
    atbd_doi = "10.5067/SOME/FAKE/ATBD_DOI"
    atbd_url = "http://aria.domain.com/docs/ATBD.pdf"
    doc.document(atbd_id, atbd_doi, [atbd_url])

    # algorithm
    doc.algorithm(algorithm, [software], [atbd_id])

    # output dataset
    out_id = "hysds:interferogram__T22_F314-330_INSAR1_20130828-INSAR1_20130609"
    out_doi = "10.5067/ARIAMH/INSAR/Interferogram"
    out_accessURL = 'https://aria-search.domain.com/?source={"query":{"bool":{"must":[{"term":{"dataset":"interferogram"}},{"query_string":{"query":"\"interferogram__T111_F330-343_INSAR1_20140922-INSAR1_20140906\"","default_operator":"OR"}}]}},"sort":[{"_timestamp":{"order":"desc"}}],"fields":["_timestamp","_source"]}'
    out_downloadURL = 'https://dav.domain.com/repository/products/interferograms/v0.2/2014/09/06/interferogram__T111_F330-343_INSAR1_20140922-INSAR1_20140906/2014-09-22T224943.621648'
    out_level = "L1"
    doc.dataset(out_id, out_doi, [out_downloadURL], [instrument], None, out_level)

    # software agent
    sa_id = "hysds:ariamh-worker-32.domain.com/12353"
    pid = "12353"
    worker_node = "ariamh-worker-32.domain.com"
    doc.softwareAgent(sa_id, pid, worker_node)

    # runtime context
    rt_ctx_id = "hysds:runtime_context"
    doc.runtimeContext(rt_ctx_id, [downloadURL])

    # process step
    proc_id = "hysds:create_interferogram-INSAR20130625_673969_2940232"
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(seconds=12233)
    ps = doc.processStep(proc_id, start_time.isoformat() + 'Z',
                         end_time.isoformat() + 'Z', [software],
                         sa_id, rt_ctx_id, [id, dem_id], [out_id],
                         wasAssociatedWithRole="softwareAgent")
    
    print doc.serialize(indent=2)

Outputs::

  {
    "wasAssociatedWith": {
      "hysds:c67a35aa-ccef-5d4a-bdb2-44012953e805": {
        "prov:role": "softwareAgent", 
        "prov:agent": "hysds:ariamh-worker-32.domain.com/12353", 
        "prov:activity": "hysds:create_interferogram-INSAR20130625_673969_2940232"
      }
    }, 
    "used": {
      "hysds:af8d3158-3db0-59ea-be51-2b67edc4b12b": {
        "prov:role": "input", 
        "prov:time": "2015-07-15T00:44:24.127786+00:00", 
        "prov:entity": "hysds:srtm/version2_1/SRTM1/Region_01/N31W114", 
        "prov:activity": "hysds:create_interferogram-INSAR20130625_673969_2940232"
      }, 
      "hysds:cd86fc28-6be6-55c3-bdd6-df46e652d5c2": {
        "prov:role": "input", 
        "prov:time": "2015-07-15T00:44:24.127786+00:00", 
        "prov:entity": "hysds:INSAR2_RAW_HI_06_HH_RA_20140922062622_20140922062629", 
        "prov:activity": "hysds:create_interferogram-INSAR20130625_673969_2940232"
      }
    }, 
    "agent": {
      "hysds:ariamh-worker-32.domain.com/12353": {
        "hysds:pid": "12353", 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "prov:SoftwareAgent"
        }, 
        "hysds:host": "ariamh-worker-32.domain.com"
      }, 
      "eos:ASI": {
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "prov:Organization"
        }
      }
    }, 
    "entity": {
      "hysds:interferogram__T22_F314-330_INSAR1_20130828-INSAR1_20130609": {
        "gcis:sourceInstrument": [
          "eos:INSAR2-SAR"
        ], 
        "eos:level": "L1", 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:dataset"
        }, 
        "prov:location": [
          "https://dav.domain.com/repository/products/interferograms/v0.2/2014/09/06/interferogram__T111_F330-343_INSAR1_20140922-INSAR1_20140906/2014-09-22T224943.621648"
        ], 
        "info:doi": "10.5067/ARIAMH/INSAR/Interferogram"
      }, 
      "eos:ISCE": {
        "gcis:implements": [
          "eos:interferogram_creation"
        ], 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:software"
        }
      }, 
      "hysds:INSAR2_RAW_HI_06_HH_RA_20140922062622_20140922062629": {
        "gcis:sourceInstrument": [
          "eos:INSAR2-SAR"
        ], 
        "eos:level": "L0", 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:dataset"
        }, 
        "prov:location": [
          "https://dav.domain.com/repository/products/insar/v0.2/2014/09/22/INSAR2_RAW_HI_06_HH_RA_20140922062622_20140922062629/INSAR20140922_913686_3720875"
        ], 
        "info:doi": "10.5067/ARIAMH/INSAR/Scene"
      }, 
      "eos:INSAR4-SAR": {
        "gcis:hasSensor": [
          "eos:SAR"
        ], 
        "gcis:inPlatform": "eos:INSAR4", 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:instrument"
        }, 
        "gcis:hasGoverningOrganization": [
          "eos:ASI"
        ]
      }, 
      "hysds:runtime_context": {
        "eos:hasRuntimeParameter": [
          "https://dav.domain.com/repository/products/insar/v0.2/2014/09/22/INSAR2_RAW_HI_06_HH_RA_20140922062622_20140922062629/INSAR20140922_913686_3720875"
        ], 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:runtimeContext"
        }
      }, 
      "eos:SAR": [
        {
          "gcis:inInstrument": "eos:INSAR2-SAR", 
          "prov:type": {
            "type": "prov:QualifiedName", 
            "$": "eos:sensor"
          }
        }, 
        {
          "gcis:inInstrument": "eos:INSAR4-SAR", 
          "prov:type": {
            "type": "prov:QualifiedName", 
            "$": "eos:sensor"
          }
        }
      ], 
      "eos:interferogram_creation": {
        "eos:describedBy": [
          "eos:interferogram_creation_atbd"
        ], 
        "gcis:implementedIn": [
          "eos:ISCE"
        ], 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:algorithm"
        }
      }, 
      "eos:INSAR4": {
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:platform"
        }, 
        "gcis:hasInstrument": [
          "eos:INSAR4-SAR"
        ]
      }, 
      "eos:interferogram_creation_atbd": {
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "bibo:Document"
        }, 
        "prov:location": [
          "http://aria.domain.com/docs/ATBD.pdf"
        ], 
        "info:doi": "10.5067/SOME/FAKE/ATBD_DOI"
      }, 
      "hysds:srtm/version2_1/SRTM1/Region_01/N31W114": {
        "eos:level": "L0", 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:dataset"
        }, 
        "prov:location": [
          "https://dav.domain.com/repository/products/srtm/version2_1/SRTM1/Region_01/N31W114.hgt.zip"
        ]
      }, 
      "eos:INSAR2": {
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:platform"
        }, 
        "gcis:hasInstrument": [
          "eos:INSAR2-SAR"
        ]
      }, 
      "eos:INSAR2-SAR": {
        "gcis:hasSensor": [
          "eos:SAR"
        ], 
        "gcis:inPlatform": "eos:INSAR2", 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:instrument"
        }, 
        "gcis:hasGoverningOrganization": [
          "eos:ASI"
        ]
      }
    }, 
    "prefix": {
      "info": "http://info-uri.info/", 
      "bibo": "http://purl.org/ontology/bibo/", 
      "hysds": "http://hysds.domain.com/hysds/0.1#", 
      "eos": "http://nasa.gov/eos.owl#", 
      "gcis": "http://data.globalchange.gov/gcis.owl#", 
      "dcterms": "http://purl.org/dc/terms/"
    }, 
    "activity": {
      "hysds:create_interferogram-INSAR20130625_673969_2940232": {
        "eos:runtimeContext": "hysds:runtime_context", 
        "eos:usesSoftware": [
          "eos:ISCE"
        ], 
        "prov:startTime": "2015-07-15T00:44:24.127786+00:00", 
        "prov:endTime": "2015-07-15T04:08:17.127786+00:00", 
        "prov:type": {
          "type": "prov:QualifiedName", 
          "$": "eos:processStep"
        }
      }
    }, 
    "wasGeneratedBy": {
      "hysds:8ca384ea-5df7-5c56-9003-e8c38ee5d991": {
        "prov:role": "output", 
        "prov:time": "2015-07-15T04:08:17.127786+00:00", 
        "prov:entity": "hysds:interferogram__T22_F314-330_INSAR1_20130828-INSAR1_20130609", 
        "prov:activity": "hysds:create_interferogram-INSAR20130625_673969_2940232"
      }
    }
  }
