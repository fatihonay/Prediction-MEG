# MEG Processing

Magnetoencephalography records the tiny magnetic fields produced by
synchronized post-synaptic currents, at millisecond resolution.

## Typical pipeline

1. **Import & inspect** raw data; mark bad channels.
2. **Filter** — band-pass for the effect of interest, notch out line noise.
3. **Artifact removal** — ICA or SSP for cardiac and ocular artifacts.
4. **Epoch** around events and reject residual bad trials.
5. **Average** to obtain evoked responses, or estimate spectra / TFRs.

```{list-table} Common artifact sources
:header-rows: 1

* - Source
  - Signature
  - Typical remedy
* - Eye blinks
  - Large low-frequency frontal deflection
  - ICA / SSP
* - Heartbeat
  - ~1 Hz periodic component
  - ICA / SSP
* - Line noise
  - Sharp peak at 50/60 Hz
  - Notch filter
```

:::{seealso}
{doc}`source_localization` — mapping these cleaned signals back to the cortex.
:::
