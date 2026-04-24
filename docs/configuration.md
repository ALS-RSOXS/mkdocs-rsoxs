# Configuration

This theme reads project metadata from `pyproject.toml` and combines it with `mkdocs.yml` values.

## Metadata Sources

- `pyproject.toml` (`[project]`):
  - `name`
  - `version`
  - `description`
- `mkdocs.yml` (`extra.als_group`):
  - `full_name`
  - `acronym`
  - `github_url`
  - `reixs_url`

## Recommended `mkdocs.yml` Pattern

```yaml
site_name: mkdocs-rsoxs
site_description: A mkdocs theme for als rsoxs projects
site_url: https://als-rsoxs.github.io/mkdocs-rsoxs
repo_url: https://github.com/als-rsoxs/mkdocs-rsoxs

extra:
  als_group:
    full_name: ALS RSOXS Group Project
    acronym: REIXS
    github_url: https://github.com/ALS-RSOXS
    reixs_url: https://als.lbl.gov/science/photon-science-programs/rixs-program/
```

## Automatic Defaults

The `rsoxs` plugin injects these values into `config.extra.project_meta`:

- `package_name`
- `package_name_display`
- `package_version`
- `package_description`

It also computes a `site_name` default from group GitHub + package name when `site_name` is left as the bare package name.

## Template Access

Jinja templates can read:

- `config.extra.project_meta.package_name`
- `config.extra.project_meta.package_version`
- `config.extra.als_group.full_name`
- `config.extra.als_group.acronym`
- `config.extra.als_group.github_url`
- `config.extra.als_group.reixs_url`
