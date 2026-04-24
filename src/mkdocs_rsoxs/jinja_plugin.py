from functools import partial

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
