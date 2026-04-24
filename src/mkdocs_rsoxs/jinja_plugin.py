import tomllib
from functools import partial
from pathlib import Path
from urllib.parse import urlparse

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files

from mkdocs_rsoxs.filters import (
    active_section,
    file_exists,
    first_page,
    iconify,
    is_http_url,
    parse_author,
    setattribute,
)


class RsoxsJinjaPlugin(BasePlugin):
    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        config_path = Path(config["config_file_path"]).resolve()
        pyproject_path = config_path.parent / "pyproject.toml"
        pyproject_data: dict = {}
        if pyproject_path.exists():
            with pyproject_path.open("rb") as pyproject_file:
                pyproject_data = tomllib.load(pyproject_file)

        project = pyproject_data.get("project", {})
        package_name = str(project.get("name", "mkdocs_rsoxs"))
        package_name_display = package_name.replace("_", "-")
        package_version = str(project.get("version", "0.0.0"))
        package_description = str(project.get("description", ""))

        extra = dict(config.get("extra", {}))
        project_meta = dict(extra.get("project_meta", {}))
        project_meta.setdefault("package_name", package_name)
        project_meta.setdefault("package_name_display", package_name_display)
        project_meta.setdefault("package_version", package_version)
        project_meta.setdefault("package_description", package_description)
        extra["project_meta"] = project_meta

        als_group = dict(extra.get("als_group", {}))
        als_group.setdefault("full_name", "ALS RSOXS Group Project")
        als_group.setdefault("acronym", "REIXS")
        als_group.setdefault("github_url", "https://github.com/ALS-RSOXS")
        als_group.setdefault(
            "reixs_url",
            "https://als.lbl.gov/science/photon-science-programs/rixs-program/",
        )
        extra["als_group"] = als_group
        config["extra"] = extra

        github_url = str(als_group.get("github_url", "")).strip()
        github_slug = ""
        if github_url:
            parsed = urlparse(github_url)
            github_slug = parsed.path.strip("/")

        current_site_name = str(config.get("site_name", "")).strip()
        if current_site_name in ("", package_name, package_name_display):
            if github_slug:
                config["site_name"] = f"{github_slug}/{package_name_display}"
            else:
                config["site_name"] = package_name_display

        return config

    def on_env(
        self,
        env,
        /,
        *,
        config: MkDocsConfig,
        files: Files,
    ):
        env.filters["file_exists"] = partial(file_exists, config=config)
        env.filters["is_http_url"] = is_http_url
        env.filters["iconify"] = iconify
        env.filters["parse_author"] = parse_author
        env.filters["setattribute"] = setattribute
        env.filters["active_section"] = active_section
        env.filters["first_page"] = first_page
        return env
