# MEG Processing & Predictive Brain

```{toctree}
:hidden:
:caption: Getting Started

getting_started/installation
getting_started/quickstart
```

```{toctree}
:hidden:
:caption: Topics

topics/meg_processing
topics/source_localization
topics/predictive_brain
```

```{toctree}
:hidden:
:caption: Reference

reference/api
reference/references
```

Documentation for magnetoencephalography (MEG) signal processing, source
localization, and predictive-coding theories of brain function.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} {octicon}`pulse` MEG Processing
:link: topics/meg_processing
:link-type: doc

Preprocessing, filtering, artifact rejection, and epoching of raw MEG data.
:::

:::{grid-item-card} {octicon}`location` Source Localization
:link: topics/source_localization
:link-type: doc

From sensor space to cortical sources — forward models, inverse solutions,
and beamformers.
:::

:::{grid-item-card} {octicon}`light-bulb` Predictive Brain
:link: topics/predictive_brain
:link-type: doc

Predictive coding, prediction error, and hierarchical inference in the cortex.
:::

:::{grid-item-card} {octicon}`code` API Reference
:link: reference/api
:link-type: doc

Auto-generated documentation for the project's Python modules.
:::

::::

## Quick example

A little MyST math to confirm rendering works — the free-energy bound that
underlies predictive-coding accounts of perception:

$$
F = \underbrace{D_{\mathrm{KL}}\!\left[q(x)\,\|\,p(x\mid s)\right]}_{\text{divergence}}
    - \underbrace{\ln p(s)}_{\text{surprise}}
$$

```python
import mne

raw = mne.io.read_raw_fif("sub-01_meg.fif", preload=True)
raw.filter(l_freq=1.0, h_freq=40.0)
raw.plot_psd(fmax=60)
```

:::{note}
Edit `getting_started/`, `topics/`, and `reference/` under `docs/source/`
to grow these sections. Every page can be written in Markdown (`.md`) or
reStructuredText (`.rst`).
:::
