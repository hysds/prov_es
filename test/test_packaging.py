"""Test packaging configuration and metadata."""
import sys
from importlib.metadata import version, requires

import pytest


def test_version_starts_with_7():
    """Verify package version starts with 7."""
    v = version("hysds-prov-es")
    assert v.startswith("7."), f"Expected version 7.x, got {v}"


def test_future_not_a_dependency():
    """Verify 'future' package is not a dependency."""
    deps = requires("hysds-prov-es")
    assert deps is not None
    
    for dep in deps:
        dep_name = dep.split()[0].split(";")[0].split(">=")[0].split("~=")[0].split("<")[0]
        assert dep_name != "future", "'future' should not be a dependency on Python 3.12+"


def test_core_modules_importable():
    """Verify core prov_es modules can be imported."""
    import prov_es
    assert hasattr(prov_es, "__version__")


def test_python_version_requirement():
    """Verify running on Python 3.12+."""
    assert sys.version_info >= (3, 12), "Requires Python 3.12+"


def test_package_name_is_hysds_prov_es():
    """Verify package is published as hysds-prov-es."""
    v = version("hysds-prov-es")
    assert v is not None, "Package 'hysds-prov-es' not found"


def test_import_name_is_prov_es():
    """Verify import name remains 'prov_es' (not hysds_prov_es)."""
    import prov_es
    assert prov_es.__name__ == "prov_es"


def test_prov_dependency_pinned():
    """Verify prov dependency is pinned to 1.3.1."""
    deps = requires("hysds-prov-es")
    assert deps is not None
    
    prov_deps = [d for d in deps if d.startswith("prov")]
    assert prov_deps, "prov dependency not found"
    
    for dep in prov_deps:
        assert "1.3.1" in dep, f"prov should be pinned to 1.3.1, found: {dep}"
