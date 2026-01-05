from lightkurve import search_lightcurvefile

def load_lightcurve_kepler(kepler_id):
    lcf = search_lightcurvefile(kepler_id, mission="Kepler").download()
    lc = lcf.SAP_FLUX.remove_nans().flatten(window_length=401)
    return lc.time.value, lc.flux.value
