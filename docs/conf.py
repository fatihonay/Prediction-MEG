import os
import sys


project = "Prediction-MEG"
copyright = "2026, Fatih Onay"
author = "Fatih Onay"

release = "0.1.0"


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
]


autosummary_generate = True


templates_path = ["_templates"]

exclude_patterns = []


html_theme = "pydata-sphinx-theme"


html_theme_options = {
    "github_url": "https://github.com/fatihonay/Prediction-MEG",
    "navigation_with_keys": True,
    "show_nav_level": 2,
}


html_static_path = ["_static"]


html_title = "Prediction-MEG"
    "navigation_with_keys": True,

    "show_nav_level": 3,

    "collapse_navigation": False,

    "use_edit_page_button": True,

    "secondary_sidebar_items": ["page-toc"],

    "logo": {
        "text": "Prediction-MEG"
    }
}

html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"
