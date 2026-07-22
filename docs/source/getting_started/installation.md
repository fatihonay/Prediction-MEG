# Installation

Set up a clean environment and install the analysis stack.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install mne numpy scipy matplotlib
```

:::{tip}
For MEG work, [MNE-Python](https://mne.tools/) is the de-facto toolbox and
pulls in most of what you need.
:::

## Building these docs locally

```bash
pip install -r docs/requirements.txt
sphinx-build -b html docs/source docs/_build/html
```

Then open `docs/_build/html/index.html` in a browser.
