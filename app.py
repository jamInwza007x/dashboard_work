import dash
import pandas as pd
import plotly.express as px

df = px.data.gapminder()
app = dash.Dash(__name__)
