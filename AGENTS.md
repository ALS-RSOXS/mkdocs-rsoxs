## Learned User Preferences
- Use `bun` for JavaScript and TypeScript package and script management in this workspace.
- Keep explanations concise and technically focused.
- Provide a clear implementation plan before substantial edits.

## Learned Workspace Facts
- This repository builds a custom `mkdocs` theme oriented to ALS design-system styling.
- Transcript memory state is tracked at `.cursor/hooks/state/continual-learning-index.json`.
- The `rsoxs` MkDocs plugin reads `pyproject.toml` project metadata and exposes it under `config.extra.project_meta` for templates and docs.
- ALS group metadata is configured via `mkdocs.yml` `extra.als_group` and is consumed by footer/template rendering.
- GitHub Pages for this repository should use the GitHub Actions deployment source (not branch-based deploy) so workflow-built MkDocs output is not overwritten by README or Jekyll publishing.
- `.github/workflows/docs.yml` limits docs build and deploy jobs to `refs/heads/main` so non-main triggers do not publish unexpected site output.
