# mkdocs-rsoxs

[![CI](https://github.com/als-rsoxs/mkdocs-rsoxs/actions/workflows/ci.yml/badge.svg)](https://github.com/als-rsoxs/mkdocs-rsoxs/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/mkdocs_rsoxs.svg)](https://badge.fury.io/py/mkdocs_rsoxs)
[![codecov](https://codecov.io/gh/als-rsoxs/mkdocs-rsoxs/branch/main/graph/badge.svg)](https://codecov.io/gh/als-rsoxs/mkdocs-rsoxs)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/type--checked-ty-blue?labelColor=orange)](https://github.com/astral-sh/ty)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://github.com/als-rsoxs/mkdocs-rsoxs/blob/main/LICENSE)
[![Renovate](https://img.shields.io/badge/renovate-enabled-brightgreen.svg?logo=renovate)](https://renovateapp.com/)

A mkdocs theme for als rsoxs projects

## Features

- Fast and modern Python toolchain using Astral's tools (uv, ruff, ty)
- Type-safe with full type annotations
- Comprehensive documentation with MkDocs — [View Docs](https://als-rsoxs.github.io/mkdocs-rsoxs/)

## Installation

```bash
pip install mkdocs_rsoxs
```

Or using uv (recommended):

```bash
uv add mkdocs_rsoxs
```

## Quick Start

```python
import mkdocs_rsoxs

print(mkdocs_rsoxs.__version__)
```

## Development

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

```bash
git clone https://github.com/als-rsoxs/mkdocs-rsoxs.git
cd mkdocs-rsoxs
make install
```

### Running Tests

```bash
make test

# With coverage
make test-cov

# Across all Python versions
make test-matrix
```

### Code Quality

```bash
# Run all checks (lint, format, type-check)
make verify

# Auto-fix lint and format issues
make fix
```

### Prek

```bash
prek install
prek run --all-files
```

### Documentation

The `rsoxs` MkDocs theme ships default ALS header icons and favicon under `src/mkdocs_rsoxs/img/`. Rebuild CSS with `bun run build` (or `make docs-assets`) when you change Tailwind sources.

In your `mkdocs.yml`, add the theme’s Jinja plugin so filters such as `file_exists` resolve theme static files:

```yaml
plugins:
  - rsoxs
  - search
```

```bash
make docs-serve
```
## Dependency Updates

This project uses [Renovate](https://renovateapp.com/) to keep dependencies up to date automatically. Renovate will open pull requests when new versions of dependencies are available.

To enable it, install the [Renovate GitHub App](https://github.com/apps/renovate) and grant it access to this repository.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
