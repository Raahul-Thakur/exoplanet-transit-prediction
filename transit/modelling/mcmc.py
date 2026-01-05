import numpy as np

def run_mcmc_transit_fit(
    time,
    flux,
    flux_err,
    period_guess,
    t0_guess,
    n_samples=2000,
    n_tune=1000,
    chains=2,
):
    try:
        import pymc3 as pm
        import exoplanet as xo
    except ImportError:
        raise ImportError("Install pymc3 and exoplanet-core")

    with pm.Model() as model:
        mean_flux = pm.Normal("mean", mu=1.0, sigma=0.1)
        u = xo.distributions.QuadLimbDark("u")

        log_period = pm.Normal("log_period", mu=np.log(period_guess), sigma=0.1)
        period = pm.Deterministic("period", pm.math.exp(log_period))
        t0 = pm.Normal("t0", mu=t0_guess, sigma=1.0)

        log_ror = pm.Normal("log_ror", mu=np.log(0.1), sigma=1.0)
        ror = pm.Deterministic("ror", pm.math.exp(log_ror))
        b = xo.distributions.ImpactParameter("b", ror=ror)

        orbit = xo.orbits.KeplerianOrbit(period=period, t0=t0, b=b)

        lc = xo.LimbDarkLightCurve(u).get_light_curve(
            orbit=orbit, r=ror, t=time
        )
        model_flux = pm.math.sum(lc, axis=-1) + mean_flux

        pm.Normal("obs", mu=model_flux, sigma=flux_err, observed=flux)

        map_soln = xo.optimize(start=model.test_point)

        trace = pm.sample(
            draws=n_samples,
            tune=n_tune,
            chains=chains,
            start=map_soln,
            return_inferencedata=True,
        )

    return trace
