# Copyright releng-tool
# SPDX-License-Identifier: BSD-2-Clause

from babel import Locale
from sphinx.errors import ConfigError
from sphinx.ext.autodoc import cut_lines
import docutils
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
    'footer_icons': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/releng-tool/releng-tool',
            'html': '''
<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
</svg>
            ''',
            'class': '',
        },
    ],
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

# ######################################################################
# replace docutil's ID generation to help improve this specific
# documentation to have "better" anchor links for various special
# character section names
# ######################################################################

original_make_id = docutils.nodes.make_id

def new_make_id(string):
    # sections with an equals (e.g. "TEST=1"), only use the content before
    # the equal character
    string = string.split('=')[0]

    # if the section starts with a numeric (i.e. a version ID, "1.0 release"),
    # prefix it with a character to not get assigned a generic id target
    if string[:1].isdigit():
        string = f'v{string}'

    # for sections with a dynamic-hint (e.g. "<PKG>_FLAG"), replace the
    # greater-than character with a "var" hint to make it unique; e.g.
    #  "PKG_NAME" and "<PKG>_NAME" resolved to "PKG_NAME"; to
    #  "PKG_NAME" and "<PKG>_NAME" resolved to "PKG_VAR_NAME"
    string = string.replace('>', '-var')

    return original_make_id(string)

docutils.nodes.make_id = new_make_id
