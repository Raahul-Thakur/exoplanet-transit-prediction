from lightkurve import search_lightcurvefile

def load_lightcurve_tess(tic_id):
    lcf = search_lightcurvefile(f"TIC {tic_id}", mission="TESS").download()
    lc = lcf.SAP_FLUX.remove_nans().flatten(window_length=301)
    return lc.time.value, lc.flux.value
