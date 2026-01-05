import numpy as np
import matplotlib.pyplot as plt

def fit_batman_transit(
    time,
    flux,
    period,
    t0,
    rp_over_rs=0.1,
    a_over_rs=15.0,
    inc_deg=90.0,
    ecc=0.0,
    w_deg=90.0,
    limb_dark="quadratic",
    u_params=(0.1, 0.3),
):
    try:
        import batman
    except ImportError:
        raise ImportError("Install batman-package to use this module")

    params = batman.TransitParams()
    params.t0 = t0
    params.per = period
    params.rp = rp_over_rs
    params.a = a_over_rs
    params.inc = inc_deg
    params.ecc = ecc
    params.w = w_deg
    params.limb_dark = limb_dark
    params.u = list(u_params)

    model = batman.TransitModel(params, time)
    flux_model = model.light_curve(params)

    return flux_model, params


def plot_batman_fit(time, flux, period, t0, model_flux):
    phase = ((time - t0 + 0.5 * period) % period) / period - 0.5
    s = np.argsort(phase)

    plt.figure(figsize=(10, 4))
    plt.scatter(phase[s], flux[s], s=6, alpha=0.4, label="Data")
    plt.plot(phase[s], model_flux[s], "r-", lw=2, label="Batman model")
    plt.xlabel("Phase")
    plt.ylabel("Normalized Flux")
    plt.legend()
    plt.tight_layout()
    plt.show()
