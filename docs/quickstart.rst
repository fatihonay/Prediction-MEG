Quick Start
===========

Example workflow

1. Load MEG data
2. Inspect channels
3. Preprocess
4. Epoch
5. Extract features
6. Train decoder
7. Visualize results

Example

.. code-block:: python

    import mne

    raw = mne.io.read_raw_fif("sample_raw.fif")
    raw.plot()
