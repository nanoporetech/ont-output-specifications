# stdlib
from typing import List

# 3rd party
from docutils.nodes import Node
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from domdf_python_tools.utils import strtobool
from sphinx.application import Sphinx
from sphinx.domains import ObjType
from sphinx.domains.std import GenericObject
from sphinx.roles import XRefRole

# this package
from sphinx_toolbox.utils import (
    OptionSpec,
    SphinxExtMetadata,
    flag,
    metadata_add_version,
)

__all__ = ("FileFieldValue", "setup")


class FileFieldValue(GenericObject):
    """
    The filefield directive.
    """

    indextemplate: str = "%s (configuration value)"

    option_spec: OptionSpec = {  # type: ignore[assignment]
        "name": directives.unchanged_required,
        "required": flag,
        "content": directives.unchanged_required,
        "regex": directives.unchanged_required,
    }

    def add_target_and_index(self, name_cls, sig, signode):
        signode["ids"].append("filefield" + "-" + sig)

    def run(self) -> List[Node]:
        """
        Process the content of the directive.
        """

        content: List[str] = []

        if self.options and set(self.options.keys()) != {"noindex"}:
            content.extend(("", ".. raw:: latex", "", r"    \vspace{-45px}", ""))

        if "name" in self.options:
            content.append(f"| **Name:** {self.options['name']}")
        if "required" in self.options:
            content.append(f"| **Required:** ``{strtobool(self.options['required'])}``")
        if "content" in self.options:
            content.append(f"| **Content:** {self.options['content']}")
        if "regex" in self.options:
            content.append(f"| **Regex:** ``{self.options['regex']}``")
        if "example" in self.options:
            content.append(f"| **Example:** {self.options['example']}")

        if self.content:
            content.extend(
                (
                    "",
                    ".. raw:: latex",
                    "",
                    r"    \vspace{-25px}",
                    "",
                )
            )
            content.extend(self.content)

        self.content = StringList(content)

        return super().run()


@metadata_add_version
def setup(app: Sphinx) -> SphinxExtMetadata:
    name = "filefield"

    app.add_role(name, XRefRole())
    app.add_directive(name, FileFieldValue)

    object_types = app.registry.domain_object_types.setdefault("std", {})

    object_types[name] = ObjType(name, name)

    return {"parallel_read_safe": True}
