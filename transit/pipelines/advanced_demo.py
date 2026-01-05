import numpy as np
from exoplanet_transit.modeling.batman_fit import fit_batman_transit
from exoplanet_transit.modeling.mcmc import run_mcmc_transit_fit

def run(time, flux):
    flux_err = np.std(flux) * np.ones_like(flux)

    print("Running batman fit...")
    model_flux, params = fit_batman_transit(
        time, flux, period=3.5, t0=0.5
    )

    print("Running MCMC...")
    trace = run_mcmc_transit_fit(
        time, flux, flux_err, period_guess=3.5, t0_guess=0.5
    )

    return trace
