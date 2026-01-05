from astropy.table import Table

def load_lightcurve_from_file(filename):
    tab = Table.read(filename, format="csv")
    if not {"time", "flux"} <= set(tab.colnames):
        raise ValueError("CSV must contain 'time' and 'flux'")
    return tab
