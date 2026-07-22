# Configuration file for the Sphinx documentation builder.
# Full reference: https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import datetime

# -- Project information -----------------------------------------------------

project = "MEG Processing & Predictive Brain"
author = "Fatih"
copyright = f"{datetime.now().year}, {author}"
release = "0.1.0"
version = "0.1"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",              # write pages in Markdown as well as reStructuredText
    "sphinx.ext.autodoc",       # pull docstrings from your Python code
    "sphinx.ext.napoleon",      # understand NumPy / Google style docstrings
    "sphinx.ext.viewcode",      # add links to highlighted source code
    "sphinx.ext.intersphinx",   # cross-link to other projects' docs
    "sphinx.ext.mathjax",       # render LaTeX math (useful for signal processing)
    "sphinx.ext.githubpages",   # emit a .nojekyll file for GitHub Pages
    "sphinx_copybutton",        # a "copy" button on code blocks
    "sphinx_design",            # grids, cards, tabs, dropdowns
]

# Accept both .rst and .md source files.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# MyST (Markdown) extensions — enables nicer syntax in .md files.
myst_enable_extensions = [
    "amsmath",       # LaTeX math environments
    "dollarmath",    # $inline$ and $$block$$ math
    "colon_fence",   # ::: fenced directives
    "deflist",       # definition lists
    "tasklist",      # - [ ] checkboxes
    "fieldlist",
    "html_image",
]
myst_heading_anchors = 3  # auto-generate anchors for h1-h3

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "MEG Processing & Predictive Brain"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

# Point the little edit/source buttons and the repo link at your GitHub repo.
# >>> EDIT the two placeholders below to match your GitHub account/repo. <<<
GITHUB_USER = "your-username"
GITHUB_REPO = "your-repo"

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_buttons": ["view", "edit"],
    "source_repository": f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "light_css_variables": {
        "color-brand-primary": "#1f6feb",
        "color-brand-content": "#1f6feb",
    },
    "dark_css_variables": {
        "color-brand-primary": "#58a6ff",
        "color-brand-content": "#58a6ff",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0"
                     viewBox="0 0 16 16" width="1em" height="1em">
                  <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53
                  5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49
                  -2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58
                  1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89
                  -3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21
                  2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82
                  .44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95
                  .29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013
                  8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

# -- intersphinx: link out to project docs you commonly reference ------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "mne": ("https://mne.tools/stable/", None),
}

# -- copybutton: don't copy prompt characters --------------------------------

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
