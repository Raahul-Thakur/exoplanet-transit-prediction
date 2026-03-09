# Exoplanet Transit Prediction

A modular Python project for generating, detecting, and analyzing exoplanet transit signals.

## What This Project Includes

- Synthetic lightcurve generation with injected transit signals
- Transit detection using Box Least Squares (BLS)
- Multi-planet iterative transit search
- Kepler/TESS lightcurve loading via Lightkurve
- Transit modeling utilities (box model, `batman`, MCMC with `pymc3` + `exoplanet`)
- Supporting astronomy utilities (ephemeris prediction, visibility checks, orbit construction)
- Visualization utilities (phase-fold, posterior corner plots)
- Optional web dashboards (Streamlit, Dash)
- Optional orbit animation with Manim

## Repository Layout

- `transit/`: core source code
- `tests/`: test files
- `notebook/ETP.ipynb`: notebook workflow
- `requirements.txt`: Python dependencies
- `pyproject.toml`: package metadata

## Requirements

- Python 3.9+ recommended
- `pip`
- Internet access for:
  - downloading mission data (Kepler/TESS via Lightkurve)
  - some Skyfield ephemeris resources

## Setup

1. Open terminal in project root:

```powershell
cd "d:\Rahul\Other\Gitlab\Exoplanet Transit Prediction\exoplanet-transit-prediction"
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

4. Optional editable install:

```powershell
pip install -e .
```

## Quick Run Examples

### 1) Generate synthetic data + run BLS + phase-fold plot

```powershell
python -c "from transit.lightcurves.synthetic import generate_synthetic_lightcurve; from transit.detection.bls import run_bls; from transit.plotting.phase_fold import plot_phase_folded; lc,_=generate_synthetic_lightcurve(); t=lc['time']; f=lc['flux']; P,t0,dur,depth,_=run_bls(t,f); print(f'P={P:.4f} d, t0={t0:.4f}, duration={dur:.4f} d, depth={depth:.2e}'); plot_phase_folded(t,f,P,t0,dur,'Synthetic Transit')"
```

### 2) Kepler multi-planet search

```powershell
python -c "from transit.lightcurves.kepler import load_lightcurve_kepler; from transit.detection.bls import search_multiplanet; t,f=load_lightcurve_kepler('KIC 11446443'); planets=search_multiplanet(t,f,max_planets=3); print(planets[:1])"
```

### 3) Run Streamlit app

```powershell
streamlit run transit/apps/streamlit_app.py
```

### 4) Run Dash app

```powershell
python transit/apps/dash_app.py
```

### 5) Run orbit animation (optional)

```powershell
manim -pql transit/animation/orbit_animation.py OrbitScene
```

## Tests

Run:

```powershell
pytest -q
```

Note: current `tests/test_bls.py` is empty, so there are no active assertions yet.

## Known Issues / Important Notes

- Import path inconsistency exists in some pipeline files and `transit/cli.py`:
  - code imports `exoplanet_transit...`
  - actual package folder is `transit/...`
- Spelling mismatch in advanced pipeline imports:
  - file path uses `transit/modelling/...`
  - code imports `...modeling...`
- Because of the above, direct execution of current pipeline/CLI modules may fail without refactoring.
- In `transit/modelling/mcmc.py`, the error message mentions `exoplanet-core`, while requirements list `exoplanet`.
- Some files contain mojibake characters in UI labels/comments; functionality is generally unaffected.

## Suggested Next Cleanup (Optional)

- Normalize package import paths to `transit.*`
- Standardize `modelling` vs `modeling`
- Add meaningful tests for BLS and pipeline workflows
- Add proper CLI entry points in `pyproject.toml`

## License

No license file is currently present in the repository.
