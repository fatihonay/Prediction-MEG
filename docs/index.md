# Prediction-MEG

> **An open-source framework for investigating predictive neural representations using Magnetoencephalography (MEG).**

:maxdepth: 2
:hidden:

about
installation
quickstart
pipeline
tutorials
theory
api
contributing
citation
roadmap

---

## Why Prediction-MEG?

The brain continuously generates predictions about incoming sensory information.
Prediction-MEG provides reproducible computational tools for studying these predictive
mechanisms using MEG data.

The project integrates

- 🧠 MEG preprocessing
- ⚡ Artifact removal
- 📈 Feature extraction
- 🤖 Machine learning
- 📊 Statistical analysis
- 📚 Publication-quality visualization

---

## Highlights

::::{grid} 3

:::{grid-item-card} 🚀 Reproducible
Built on MNE-Python with reproducible workflows.
:::

:::{grid-item-card} 🧠 Neuroscience
Designed specifically for predictive processing research.
:::

:::{grid-item-card} 📊 Open Science
Fully open-source with transparent documentation.
:::

::::

---

## Workflow

```{mermaid}

flowchart LR

A[Raw MEG]
-->B[Preprocessing]
-->C[Epoching]
-->D[Features]
-->E[Decoding]
-->F[Statistics]
-->G[Visualization]



