# task.md

This document lists each code file and what it currently contains.

## Root-Level Files

- `pyproject.toml`: Build metadata (`setuptools` backend), project name/version/description/author, no runtime dependencies declared under `[project].dependencies`.
- `requirements.txt`: Dependency list used by the project (numpy, astropy, lightkurve, skyfield, poliastro, scipy, batman-package, pymc3, exoplanet, corner, arviz, astroquery, streamlit, dash, plotly, manim, etc.).
- `README.md`: Project setup and run instructions.

## Notebook

- `notebook/ETP.ipynb`: Interactive notebook for exoplanet transit prediction workflow; includes package install cells and exploratory analysis code.

## Tests

- `tests/test_bls.py`: Empty placeholder test file (no active tests).

## Package: `transit/`

- `transit/__init__.py`: Re-exports selected top-level utilities (`generate_synthetic_lightcurve`, `search_multiplanet`, `predict_transit_times`).
- `transit/config.py`: Default observation config values (minimum altitude and default observer coordinates).
- `transit/cli.py`: Minimal CLI parser with `--demo`; currently wired to synthetic pipeline import path that does not match package layout.

## Subpackage: `transit/lightcurves/`

- `transit/lightcurves/__init__.py`: Re-exports synthetic, Kepler, TESS, and CSV lightcurve loaders.
- `transit/lightcurves/synthetic.py`: Generates synthetic time/flux series with injected box transit plus Gaussian noise; returns Astropy Table and truth metadata.
- `transit/lightcurves/kepler.py`: Downloads and flattens Kepler SAP_FLUX via Lightkurve; returns `(time, flux)` arrays.
- `transit/lightcurves/tess.py`: Downloads and flattens TESS SAP_FLUX via Lightkurve; returns `(time, flux)` arrays.
- `transit/lightcurves/io.py`: Reads CSV lightcurve file and validates required `time`/`flux` columns.

## Subpackage: `transit/detection/`

- `transit/detection/__init__.py`: Exports BLS and multi-planet search utilities.
- `transit/detection/bls.py`: Implements BLS transit search (`run_bls`), signal subtraction (`remove_planet_signal`), and iterative multi-planet detection (`search_multiplanet`).

## Subpackage: `transit/modelling/`

- `transit/modelling/__init__.py`: Re-exports box model, batman fit, and MCMC utilities.
- `transit/modelling/box_model.py`: Simple box-shaped transit model over phased time.
- `transit/modelling/batman_fit.py`: Builds limb-darkened transit model with `batman`; includes phase-fold plotting helper.
- `transit/modelling/mcmc.py`: Bayesian transit fit using `pymc3` + `exoplanet` (period, t0, radius ratio, impact parameter inference).

## Subpackage: `transit/plotting/`

- `transit/plotting/__init__.py`: Exports plotting helpers.
- `transit/plotting/phase_fold.py`: Phase-folded scatter plot visualization for transit signals.
- `transit/plotting/corner.py`: Posterior corner plot utility using `arviz` extraction + `corner` plotting.

## Subpackage: `transit/core/`

- `transit/core/__init__.py`: Exports ephemeris, visibility, and orbit utilities.
- `transit/core/ephemeris.py`: Predicts upcoming transit mid-times from period and reference epoch.
- `transit/core/visibility.py`: Computes whether target altitudes exceed a minimum threshold for an observer site using Skyfield.
- `transit/core/orbits.py`: Constructs orbit from period via Kepler's third law and returns Poliastro orbit + semi-major axis.

## Subpackage: `transit/spectroscopy/`

- `transit/spectroscopy/__init__.py`: Exports spectroscopy helper functions.
- `transit/spectroscopy/scale_height.py`: Estimates atmospheric scale height from mass, radius, temperature, and mean molecular weight.
- `transit/spectroscopy/ranking.py`: Scores/ranks planets for transmission spectroscopy using scale height, stellar brightness proxy, and transit depth.

## Subpackage: `transit/pipelines/`

- `transit/pipelines/__init__.py`: Pipeline package docstring only.
- `transit/pipelines/synthetic_demo.py`: End-to-end synthetic pipeline (generate data -> detect with BLS -> phase-fold plot).
- `transit/pipelines/kepler_demo.py`: Kepler lightcurve pipeline with iterative multi-planet search and plotting of first detected planet.
- `transit/pipelines/advanced_demo.py`: Runs batman model fit and MCMC inference on provided `(time, flux)` arrays.

## Subpackage: `transit/apps/`

- `transit/apps/__init__.py`: Exports app constructors/runners.
- `transit/apps/streamlit_app.py`: Streamlit dashboard for simple transit schedule table generation and CSV export.
- `transit/apps/dash_app.py`: Dash app that generates a simple phase-folded synthetic transit curve from user inputs.

## Subpackage: `transit/animation/`

- `transit/animation/__init__.py`: Exports Manim orbit scene.
- `transit/animation/orbit_animation.py`: 3D Manim scene animating an inclined eccentric orbit and displaying derived orbital parameters.

## Current Technical Notes

- Several files import `exoplanet_transit.*`, but code lives in `transit.*`.
- Some modules use `modeling` while directory name is `modelling`.
- These inconsistencies affect direct execution of certain pipeline/CLI files.
