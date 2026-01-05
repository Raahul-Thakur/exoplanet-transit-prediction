import astropy.units as u
from astropy.constants import k_B, m_p, G, M_earth, R_earth

def estimate_atmospheric_scale_height(
    planet_mass_earth,
    planet_radius_earth,
    temperature_k,
    mean_molecular_weight=2.3,
):
    M = planet_mass_earth * M_earth
    R = planet_radius_earth * R_earth
    g = (G * M / R**2).to(u.m / u.s**2)

    H = (k_B * temperature_k * u.K) / (
        mean_molecular_weight * m_p * g
    )

    return H.to(u.km).value
