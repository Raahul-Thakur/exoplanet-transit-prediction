# content.md

## LinkedIn Post (999 characters)
Day [X] of my 90 mins after work series: I built an end-to-end Exoplanet Transit Prediction project in Python and shipped it as a modular repo. The workflow includes synthetic lightcurve generation, transit detection with Box Least Squares (BLS), phase-folded visualization, and optional Kepler/TESS ingestion, Bayesian fitting, and app dashboards.

What I focused on: clear module boundaries (lightcurves, detection, modelling, core, plotting, apps), reusable scripts, and documentation so others can run it quickly.

After running the synthetic pipeline, the detector recovered a period close to the injected signal (about 3.5 days) and produced a clear transit dip in the phase-folded plot. That was the milestone: noisy flux in, interpretable transit candidate out.

Next: fix import path inconsistencies, add stronger tests, and publish benchmark runs on real Kepler targets. Happy to share code and notes.

#Python #DataScience #Astronomy #MachineLearning #Exoplanet #OpenSource #BuildInPublic

## 1-Minute Script
Today in my 90 mins after work series, I completed an end-to-end exoplanet transit prediction workflow.

I broke the project into practical modules: lightcurve generation and loading, BLS-based transit detection, transit modelling, and plotting and app interfaces. The goal was to make the code reusable, not just notebook-only.

The key result after running the synthetic pipeline was simple but important: the detector recovered a transit period close to the injected ground truth, around 3.5 days, and the phase-folded chart showed a clear transit dip. So the pipeline worked from noisy flux input to interpretable transit output.

I also prepared optional extensions for Kepler and TESS data, Bayesian fitting, and lightweight Streamlit and Dash apps.

Next, I will clean import paths, add stronger tests, and post benchmark results on real targets.

## Quick Replace Before Posting
- Replace `Day [X]` with today’s episode number.
- Replace `about 3.5 days` with your exact detected value from your run.
- Add one extra metric if available (depth or duration) to strengthen credibility.
