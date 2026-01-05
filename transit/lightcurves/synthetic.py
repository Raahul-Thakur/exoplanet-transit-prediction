import numpy as np
from astropy.table import Table

def generate_synthetic_lightcurve(
    period_days=3.5,
    duration_hours=3.0,
    depth_ppm=8000,
    t0=0.5,
    n_days=40,
    cadence_min=30,
    noise_ppm=500,
):
    cadence_days = cadence_min / (60 * 24)
    time = np.arange(0, n_days, cadence_days)

    duration = duration_hours / 24
    depth = depth_ppm / 1e6

    flux = np.ones_like(time) + np.random.normal(
        0, noise_ppm / 1e6, size=time.size
    )

    phase = ((time - t0 + 0.5 * period_days) % period_days) - 0.5 * period_days
    flux[np.abs(phase) < duration / 2] -= depth

    return Table({"time": time, "flux": flux}), {
        "true_period": period_days,
        "true_t0": t0,
        "true_duration": duration,
        "true_depth": depth_ppm,
    }
