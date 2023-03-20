import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


wine_df = pd.read_csv("data/clean/cleaned_wine_data.csv")

world_df = wine_df.groupby('country').first().reset_index() 
fig = px.scatter_geo(world_df, locations="iso_alpha", color="continent",
                     hover_name="country", size = 'Wine_count', projection="natural earth")
fig.show()


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter