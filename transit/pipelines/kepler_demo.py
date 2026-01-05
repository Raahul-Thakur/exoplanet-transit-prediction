from astropy.time import Time
from exoplanet_transit.lightcurves.kepler import load_lightcurve_kepler
from exoplanet_transit.detection.bls import search_multiplanet
from exoplanet_transit.plotting.phase_fold import plot_phase_folded

def run():
    time, flux = load_lightcurve_kepler("KIC 11446443")

    planets = search_multiplanet(time, flux, max_planets=3)

    if not planets:
        print("No planets detected.")
        return

    P, t0, dur, depth, _ = planets[0]

    print(f"Detected planet: P={P:.4f} d, depth={depth:.2e}")
    plot_phase_folded(time, flux, P, t0, dur, "Kepler Planet 1")
