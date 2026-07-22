# Quickstart

A minimal end-to-end pass from raw recording to a sensor-space evoked response.

```python
import mne

# 1. Load
raw = mne.io.read_raw_fif("sub-01_meg.fif", preload=True)

# 2. Preprocess
raw.filter(l_freq=1.0, h_freq=40.0)
raw.notch_filter(freqs=[50, 100])          # line noise (50 Hz in EU)

# 3. Epoch around events
events = mne.find_events(raw)
epochs = mne.Epochs(raw, events, tmin=-0.2, tmax=0.5, baseline=(None, 0))

# 4. Average
evoked = epochs["stimulus"].average()
evoked.plot_joint()
```

Continue to the topic pages for the details behind each step.
