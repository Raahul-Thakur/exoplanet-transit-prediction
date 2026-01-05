import numpy as np
import astropy.units as u
from astropy.timeseries import BoxLeastSquares

def run_bls(time, flux):
    flux = flux / np.median(flux)
    mask = np.isfinite(time) & np.isfinite(flux)
    time, flux = time[mask], flux[mask]

    periods = np.linspace(0.5, 30.0, 8000)
    durations = np.linspace(0.5, 8.0, 10) * u.hour

    bls = BoxLeastSquares(time * u.day, flux)
    res = bls.power(periods * u.day, durations)

    i = np.argmax(res.power)
    return (
        res.period[i].value,
        res.transit_time[i].value,
        res.duration[i].value,
        res.depth[i],
        res,
    )

def remove_planet_signal(time, flux, period, t0, duration):
    phase = ((time - t0 + 0.5 * period) % period) - 0.5 * period
    in_tr = abs(phase) < duration / 2
    depth = 1 - np.median(flux[in_tr])
    flux[in_tr] += depth
    return flux

def search_multiplanet(time, flux, max_planets=3):
    residual = flux.copy()
    planets = []
    for _ in range(max_planets):
        try:
            P, t0, dur, depth, res = run_bls(time, residual)
            planets.append((P, t0, dur, depth, res))
            residual = remove_planet_signal(time, residual, P, t0, dur)
        except Exception:
            break
    return planets
