from astropy.time import Time
from exoplanet_transit.lightcurves.synthetic import generate_synthetic_lightcurve
from exoplanet_transit.detection.bls import run_bls
from exoplanet_transit.plotting.phase_fold import plot_phase_folded

def run():
    lc, truth = generate_synthetic_lightcurve()
    time = lc["time"]
    flux = lc["flux"]

    P, t0, dur, depth, _ = run_bls(time, flux)
    plot_phase_folded(time, flux, P, t0, dur, "Synthetic Transit")
