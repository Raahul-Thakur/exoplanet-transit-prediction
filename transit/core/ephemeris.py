import astropy.units as u
from astropy.time import Time

def predict_transit_times(period_days, t0_days, start_time, n_transits=10):
    t0_abs = start_time + t0_days * u.day
    return Time([t0_abs + k * period_days * u.day for k in range(n_transits)])
