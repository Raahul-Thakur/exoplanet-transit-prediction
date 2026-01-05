import matplotlib.pyplot as plt

def plot_corner(trace, var_names=("period", "t0", "ror", "b")):
    try:
        import corner
        import arviz as az
    except ImportError:
        raise ImportError("Install corner and arviz")

    samples = az.extract(trace, var_names=var_names).to_dataframe()

    fig = corner.corner(
        samples,
        labels=var_names,
        quantiles=[0.16, 0.5, 0.84],
        show_titles=True,
    )
    plt.show()
