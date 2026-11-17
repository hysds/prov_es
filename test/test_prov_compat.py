"""Guard the supported `prov` range (>=1.3.1,<1.6): serialization and round-trip."""
import json

from prov.model import ProvDocument

from prov_es.model import ProvEsDocument


def _build():
    doc = ProvEsDocument()
    doc.softwareAgent("hysds:sa1", "123", "node1", role="u", label="l")
    doc.processStep("hysds:ps1", "2020-01-01T00:00:00", "2020-01-01T01:00:00", [],
                    "hysds:sa1", None, [], [], prov_type="hysds:x")
    doc.dataset("hysds:d1", "10.1/x", ["http://x/y"], [], None, "L0")
    return doc


def test_serialize_and_roundtrip():
    doc = _build()
    js = json.loads(doc.serialize())
    assert "hysds:ps1" in js["activity"] and "hysds:d1" in js["entity"]
    # prov 1.3.x writes "prov:QualifiedName", 1.5.x "prov:QUALIFIED_NAME"; both are read back
    back = ProvDocument.deserialize(content=doc.serialize())
    assert len(back.get_records()) == len(doc.get_records())
    assert doc.get_provn()
