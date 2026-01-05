import numpy as np
import matplotlib.pyplot as plt

def plot_phase_folded(time, flux, period, t0, duration, title=""):
    phase = ((time - t0 + 0.5 * period) % period) / period - 0.5
    s = np.argsort(phase)
    plt.scatter(phase[s], flux[s], s=5, alpha=0.4)
    plt.xlabel("Phase")
    plt.ylabel("Flux")
    plt.title(title)
    plt.show()
