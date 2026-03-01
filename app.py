import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = px.data.gapminder()
app = dash.Dash(__name__)

app.layout = html.Div([html.H1("AI Engineering Dashboard"),
                        dcc.Slider(
                        id='year-slider',
                        min=df['year'].min(),
                        max=df['year'].max(),
                        value=df['year'].min(),
                        marks={str(y): str(y) for y in df['year'].unique()}
    ),