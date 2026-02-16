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


# -- Project information -----------------------------------------------------

project = 'AUP AI & HPC Cluster'
copyright = '2023-2026, Advanced Micro Devices, Inc. All Rights Reserved.'
author = 'AMD Research'
myst_substitutions = {
    "devel_weight": "0.1",
    "mi2101x_weight": "0.1",
    "mi2104x_weight": "0.4",
    "mi2508x_weight": "0.8",
    "mi3001x_weight": "0.125",
    "mi3008x_weight": "1.0",
    "mi3258x_weight": "1.2",
    "mi3501x_weight": "0.175",
    "mi3508x_weight": "1.4",
}


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "myst_parser",
]

# Enable MyST extensions
myst_enable_extensions = [
    "substitution",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

html_show_sphinx = False


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "images/amd-header-logo.svg"
html_theme_options = {
    "analytics_id": "G-W441NL02TT",
    "analytics_anonymize_ip": False,    
    'logo_only': True,
    'display_version': False,
    }
# So we can override layout/color...
html_css_files = [
    'css/custom.css',
]

