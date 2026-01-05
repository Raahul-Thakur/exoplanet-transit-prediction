"""
Streamlit Exoplanet Transit Dashboard

Run with:
    streamlit run streamlit_app.py
"""

import streamlit as st
import pandas as pd
import astropy.units as u
from astropy.time import Time

st.set_page_config(page_title="Exoplanet Transit Predictor", layout="wide")


def run_streamlit_app():
    st.title("🪐 Exoplanet Transit Predictor")

    st.sidebar.header("Orbital Parameters")
    period = st.sidebar.number_input("Period (days)", value=3.5)
    t0 = st.sidebar.number_input("Reference T0 (JD)", value=2459000.0)

    st.sidebar.header("Observer Location")
    lat = st.sidebar.number_input("Latitude (deg)", value=12.9716)
    lon = st.sidebar.number_input("Longitude (deg)", value=77.5946)
    min_alt = st.sidebar.slider("Min Altitude (deg)", 0, 90, 30)

    n_transits = st.sidebar.slider("Number of transits", 1, 30, 10)

    if st.button("Predict Transits"):
        start = Time.now()
        t0_abs = Time(t0, format="jd")
        times = [t0_abs + i * period * u.day for i in range(n_transits)]

        df = pd.DataFrame({
            "Transit #": range(1, n_transits + 1),
            "Mid-transit (UTC)": [t.iso for t in times],
            "JD": [t.jd for t in times],
            "Days from now": [(t - start).jd for t in times],
        })

        st.dataframe(df, use_container_width=True)
        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            file_name="transit_predictions.csv",
        )


if __name__ == "__main__":
    run_streamlit_app()
