# HySDS Prov-ES Packaging Migration Summary

## Migration Completed: March 24, 2026

This document summarizes the migration of the `prov_es` repository from legacy `setup.py` to modern `pyproject.toml` packaging.

---

## Changes Made

### ✅ Files Created

1. **`pyproject.toml`** - Modern packaging configuration
   - Package name: `hysds-prov-es` (PyPI) / `prov_es` (import)
   - Version: Dynamic from git tags via `hatch-vcs`
   - Dependencies: 1 third-party package

2. **`.github/workflows/publish.yml`** - PyPI publishing automation
   - Triggered on git tags (`v*`)
   - Uses PyPI Trusted Publishers (OIDC)

### ✅ Files Modified

1. **`prov_es/__init__.py`**
   - Updated package name from `prov_es` to `hysds-prov-es` in version call

2. **`setup.py`**
   - Replaced with minimal shim for backward compatibility
   - Delegates all configuration to `pyproject.toml`
   - Will be removed in v7.1.0+

---

## Key Dependency Changes

### Fixed Issues

| Issue | Before | After |
|-------|--------|-------|
| future dependency | `future>=0.17.1` | Removed |

### Dependencies Preserved Exactly

Single dependency maintained with exact pin from original `setup.py`:
- `prov==1.3.1`

---

## Build Verification

```bash
$ python -m build
Successfully built hysds_prov_es-0.3.0.post1.dev0+gcc3cc5a49.d20260324.tar.gz
Successfully built hysds_prov_es-0.3.0.post1.dev0+gcc3cc5a49.d20260324-py3-none-any.whl
```

---

## Next Steps

### Before Publishing to PyPI

1. **Tag version 7.0.0**
   ```bash
   git tag -a v7.0.0 -m "Release 7.0.0 - Modern packaging migration"
   git push origin v7.0.0
   ```

2. **Configure PyPI Trusted Publisher**
   - Go to https://pypi.org/manage/account/publishing/
   - Add GitHub Actions publisher for `hysds/prov_es` repo
   - Workflow: `publish.yml`
   - Environment: `pypi`

### Installation Methods

#### Development (Local)
```bash
pip install -e .
```

#### Development (From Git Branch)
```bash
pip install "git+https://github.com/hysds/prov_es.git@feature-branch"
```

#### Production (After PyPI Publishing)
```bash
pip install hysds-prov-es

# Or as dependency of other packages
pip install hysds-core  # Includes hysds-prov-es~=7.0
```

---

## Backward Compatibility

### Import Names (Unchanged)
```python
# All existing imports continue to work
import prov_es
from prov_es.model import ProvEsDocument
```

### Package Name Change
- **PyPI package**: `prov_es` → `hysds-prov-es`
- **Import name**: `prov_es` (unchanged)

---

## Migration Checklist

- [x] Create `pyproject.toml` with all dependencies
- [x] Remove `future` from dependencies
- [x] Preserve prov dependency pin exactly
- [x] Update `prov_es/__init__.py` package name
- [x] Add GitHub Actions workflow for PyPI publishing
- [x] Keep minimal `setup.py` shim for backward compatibility
- [x] Verify `python -m build` succeeds
- [ ] Tag v7.0.0 release
- [ ] Configure PyPI Trusted Publisher
- [ ] Publish to PyPI

---

## Contact

For questions about this migration, contact the HySDS team at hysds-help@jpl.nasa.gov
