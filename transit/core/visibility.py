from skyfield.api import load, wgs84, Star
from skyfield.units import Angle

def visible_from_site(times, ra_deg, dec_deg, lat_deg, lon_deg,
                      elevation_m=0.0, min_alt_deg=30.0):
    ts = load.timescale()
    eph = load("de421.bsp")
    loc = eph["earth"] + wgs84.latlon(lat_deg, lon_deg, elevation_m)
    star = Star(ra=Angle(degrees=ra_deg), dec=Angle(degrees=dec_deg))

    visible, altitudes = [], []
    for t_ast, t_sf in zip(times, ts.from_astropy(times)):
        alt, _, _ = loc.at(t_sf).observe(star).apparent().altaz()
        if alt.degrees >= min_alt_deg:
            visible.append(t_ast)
            altitudes.append(alt.degrees)

    return visible, altitudes
