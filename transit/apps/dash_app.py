"""
Dash Interactive Transit Dashboard

Run with:
    python dash_app.py
"""

import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objs as go
import numpy as np


def create_dash_app():
    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H1("🪐 Exoplanet Transit Dashboard"),

        html.Label("Period (days)"),
        dcc.Input(id="period", type="number", value=3.5),

        html.Label("Transit Duration (hours)"),
        dcc.Input(id="duration", type="number", value=3.0),

        html.Button("Generate", id="btn", n_clicks=0),

        dcc.Graph(id="phase-plot"),
    ])

    @app.callback(
        Output("phase-plot", "figure"),
        Input("btn", "n_clicks"),
        State("period", "value"),
        State("duration", "value"),
    )
    def update_plot(n, period, duration):
        if n == 0:
            return go.Figure()

        phase = np.linspace(-0.5, 0.5, 500)
        flux = np.ones_like(phase)
        transit_width = (duration / 24) / period
        flux[np.abs(phase) < transit_width / 2] -= 0.01

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=phase, y=flux, mode="lines"))
        fig.update_layout(
            title="Phase-Folded Transit Model",
            xaxis_title="Phase",
            yaxis_title="Flux",
        )
        return fig

    return app


if __name__ == "__main__":
    create_dash_app().run_server(debug=True)
