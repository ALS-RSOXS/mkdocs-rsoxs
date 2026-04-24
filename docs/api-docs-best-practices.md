# API Docs Best Practices

This project follows ALS Computing guidance for MkDocs + `mkdocstrings` API documentation.

## Setup

Install docs dependencies for the `mkdocs-rsoxs` theme using `uv` dependency groups:

```toml
[dependency-groups]
docs = [
    "mkdocstrings-python>=2.0.1",
    "pymdown-extensions>=10.0.0",
    "mkdocs-rsoxs>=0.1.0",
]
```

## MkDocs Configuration Template

### Set Configuration
```yaml
site_name: My ALS Project
site_description: Short description of the project.
repo_url: https://github.com/als-computing/my-project

extra:
  als_group:
    full_name: My ALS Project Grroup
    acronym: My Group Acronym
    github_url: https://github.com/my-project-group
    reixs_url: https://als.lbl.gov/science/photon-science-programs/program-slug/
```

### Set Theme
```yaml
theme:
  name: rsoxs
  show_title: true
  show_stargazers: true
  topbar_sections: false
  features:
    - content.code.copy
    - content.code.annotate
    - navigation.instant
    - navigation.tracking
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
    - toc.follow
```
### Set Plugins
```yaml
plugins:
  - rsoxs
  - search
  - mkdocstrings:
      handlers:
        python:
          paths:
            - src
          options:
            docstring_style: google # or numpy
            show_source: true
            show_root_heading: true
            show_root_toc_entry: true
            merge_init_into_class: true
```

### Set Navigation
```yaml
nav:
  - Home: index.md
  - API Reference:
    - Flows: api/flows.md
    - Tasks: api/tasks.md
    - CLI: api/cli.md
```

## Auto-generated Module Stubs

Create one doc page per module and let `mkdocstrings` render API objects from docstrings.

```markdown
# Flows

::: my_project.flows.bl832
::: my_project.flows.bl733
```

For package-level API pages, point directives at your top-level package:

```markdown
# API Reference

::: my_project
    options:
      members: true
      show_submodules: true
      inherited_members: true
```

## Docstring Style Selection

Select docstring style explicitly from user/project preference:

- `google` for Google-style `Args`/`Returns` sections.
- `numpy` for NumPy-style sectioned scientific APIs.

```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: numpy # or google
```

## Documentation Scope

Include:

- Public functions and classes
- `@flow` and `@task` functions
- Pydantic models and dataclasses
- CLI commands

Exclude:

- Private helpers (leading underscore)
- Internal utility functions
- Test-only utilities
- `conftest.py`

## Local Commands

```bash
uv run mkdocs serve
uv run mkdocs build
```

## Recommended `docs/` Layout

```text
docs/
├── index.md
├── installation.md
├── usage.md
└── api/
    ├── flows.md
    ├── tasks.md
    └── cli.md
```

`index.md` should describe project purpose, audience, and a minimal working example. Keep implementation details in docstrings and avoid duplication.
