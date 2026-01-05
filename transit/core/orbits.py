import numpy as np
import astropy.units as u
from astropy.constants import G, M_sun
from poliastro.bodies import Sun
from poliastro.twobody import Orbit

def build_orbit(period_days, star_mass_solar=1.0, ecc=0.0, inc_deg=0.0):
    P = period_days * u.day
    M = star_mass_solar * M_sun
    a = ((G * M * P**2) / (4 * np.pi**2)) ** (1 / 3)
    return Orbit.from_classical(
        Sun,
        a.to(u.AU),
        ecc * u.one,
        inc_deg * u.deg,
        0 * u.deg,
        0 * u.deg,
        0 * u.deg,
    ), a.to(u.AU)
