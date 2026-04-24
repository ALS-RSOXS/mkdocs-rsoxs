# mkdocs-rsoxs

A mkdocs theme for als rsoxs projects

## Installation

Install using pip:

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

Clone the repository and install dependencies:

```bash
git clone https://github.com/als-rsoxs/mkdocs-rsoxs.git
cd mkdocs-rsoxs
uv sync --group dev
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty check
```

### Prek Hooks

Install prek hooks:

```bash
prek install
```

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](https://github.com/als-rsoxs/mkdocs-rsoxs/blob/main/LICENSE) file for details.
