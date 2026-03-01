import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = px.data.gapminder()
app = dash.Dash(__name__)

app.layout = html.Div([html.H1("AI Engineering Dashboard")])