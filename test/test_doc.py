#!/usr/bin/env python
from datetime import datetime, timedelta
from prov_es.model import ProvEsDocument


def test_ProvEsDocument():
    """Test dataset()."""

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


if __name__ == "__main__":
    test_ProvEsDocument()
