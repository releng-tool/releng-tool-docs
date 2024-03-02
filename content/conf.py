# Copyright releng-tool
# SPDX-License-Identifier: BSD-2-Clause

from babel import Locale
from sphinx.errors import ConfigError
from sphinx.ext.autodoc import cut_lines
import os
import sys

# meta
project = 'releng-tool'
copyright = 'releng-tool'
author = 'releng-tool'

# options
releng_tool_domain = os.environ.get('RELENG_DOMAIN', 'docs.releng.io')
languages = os.environ.get('RELENG_LANGUAGES', 'en')

# sphinx extensions
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_inline_tabs',
]

suppress_warnings = [
    # suppress various header levels with the use of includes
    'myst.header',
    # suppress strikethrough warning ~ we only build html documentation
    'myst.strikethrough',
]

# add root for autodoc documentation
doc_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(doc_dir)
container_dir = os.path.dirname(root_dir)
rt_dir = os.path.join(container_dir, 'releng-tool')
if not os.path.exists(rt_dir):
    raise ConfigError('''
missing releng-tool repository

Ensure the releng-tool repository is checked out in the following path
before attempting to generate documentation:

    releng-tool: {}
'''.format(rt_dir))
sys.path.insert(0, rt_dir)

# myst configuration
myst_enable_extensions = [
    'colon_fence',
    'strikethrough',
]

# i8n
locale_dirs = ['locale/']
gettext_compact = False

langmap = {}
for lang in languages.split(','):
    langmap[lang] = Locale.parse(lang).get_display_name(lang)

# output - html
html_context = {
    'languages': langmap,
    'releng_tool_domain': releng_tool_domain,
}
html_copy_source = False
html_permalinks_icon = '¶'
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = True
html_static_path = ['_static']
html_theme = 'furo'
html_theme_options = {
    'navigation_with_keys': True,
}
html_use_index = False

templates_path = [
    os.path.join(doc_dir, 'templates/'),
]

# output - latex
latex_elements = {
    # remove empty pages
    'extraclassoptions': 'openany,oneside',
    # custom title
    'maketitle': r'''
        \begin{titlepage}
            \vspace*{\stretch{1.0}}
                \sphinxlogo
            \vspace*{\stretch{1.2}}
        \end{titlepage}
    ''',
    # disable hyphenatation
    # disable justified text
    # remove italics from links
    # color tweaks
    'preamble': r'''
        \usepackage[none]{hyphenat}
        \usepackage[document]{ragged2e}
        \usepackage{url}
        \def\sphinxcrossref#1{#1}
        \definecolor{InnerLinkColor}{rgb}{0.04,0.08,0.21}
        \definecolor{OuterLinkColor}{rgb}{0.04,0.08,0.21}
        \definecolor{TitleColor}{rgb}{0,0,0}
        \definecolor{VerbatimColor}{rgb}{0.98,0.98,0.98}
    ''',
}

latex_engine = 'xelatex'
latex_logo = '_static/logo.png'


# documentation setup
def setup(app):
    app.add_css_file('theme_overrides.css')

    # remove first line description docstrings in documentation
    app.connect('autodoc-process-docstring', cut_lines(1))

    # listen for configuration events
    app.connect("config-inited", on_conf)


def on_conf(app=None, config=None):
    if app.config.language == 'ja':
        app.config.latex_engine = 'uplatex'
