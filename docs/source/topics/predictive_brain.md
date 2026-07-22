# The Predictive Brain

Predictive-coding theories cast perception as hierarchical Bayesian inference:
the cortex continuously predicts its sensory input and propagates only the
**prediction error**.

## Core idea

Each level generates top-down predictions of the level below; the residual
mismatch is passed **upward** to update internal beliefs. Under the
free-energy principle, the brain minimizes variational free energy $F$:

$$
F = \mathbb{E}_{q}\!\left[\ln q(x) - \ln p(x, s)\right]
  \;\ge\; -\ln p(s)
$$

## Why MEG?

MEG's millisecond resolution makes it well suited to test predictions about
the **timing** of feedforward error signals versus feedback predictions —
e.g. mismatch-negativity and repetition-suppression paradigms.

:::{note}
This links directly to source localization: separating feedforward from
feedback contributions benefits from laminar or region-resolved estimates.
:::
