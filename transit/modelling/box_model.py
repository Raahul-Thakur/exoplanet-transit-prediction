import numpy as np

def box_transit_model(time, period, t0, duration, depth):
    """
    Simple box-shaped transit model.

    Returns normalized flux array.
    """
    phase = ((time - t0 + 0.5 * period) % period) - 0.5 * period
    flux = np.ones_like(time)
    in_transit = np.abs(phase) < duration / 2
    flux[in_transit] -= depth
    return flux
