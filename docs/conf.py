# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import subprocess
import sys
from pathlib import Path


# Add paths to source code
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str((repo_root / "python/pod5/src/").absolute()))


def get_current_release_name():
    try:
        # Run the git command to get the current branch name
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        branch_name = result.stdout.strip()

        if branch_name == "main":
            return "latest"

        # Remove the "release/" prefix if it exists
        return branch_name.removeprefix("release/")
    except subprocess.CalledProcessError as e:
        print(f"Error getting current branch: {e.stderr.strip()}")
        return None


# -- Project information -----------------------------------------------------

project = "ONT Output Specification"
copyright = "2025 Oxford Nanopore Technologies plc"
author = "Oxford Nanopore Technologies plc"

release = version = get_current_release_name()

# -- General configuration ---------------------------------------------------

sys.path.append(str(Path("sphinx_extensions").resolve()))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "myst_parser",
    "bam_directive",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = {
    "theme_overrides.css",
}

add_module_names = False

# -- Options for autosectionlabel --------------------------------------------
autosectionlabel_prefix_document = True


# This is pasted to the end of every .rst file allowing us to set common hyperlinks
# here and use them repeatedly in the source
rst_epilog = """
.. _ont: https://nanoporetech.com/
"""


def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)
