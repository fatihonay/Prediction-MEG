# Source Localization

Source localization estimates the cortical generators of the measured sensor
signals by inverting a physical **forward model**.

## Forward and inverse problem

The forward model relates source activity $\mathbf{j}$ to sensor measurements
$\mathbf{x}$ through a leadfield (gain) matrix $\mathbf{L}$:

$$
\mathbf{x} = \mathbf{L}\,\mathbf{j} + \boldsymbol{\varepsilon}
$$

The inverse problem — recovering $\mathbf{j}$ from $\mathbf{x}$ — is
ill-posed and requires priors or constraints.

## Common approaches

- **Minimum-norm estimate (MNE / dSPM / sLORETA)** — distributed, L2-penalized.
- **Beamformers (LCMV, DICS)** — spatial filters, good for oscillatory power.
- **Dipole fitting** — few focal sources, hypothesis-driven.

:::{admonition} Rule of thumb
:class: important

Beamformers shine for induced/oscillatory activity; minimum-norm methods are a
robust default for evoked responses.
:::
