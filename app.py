import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


# wine_df = pd.read_csv("data/clean/cleaned_wine_data.csv")

# world_df = wine_df.groupby('country').first().reset_index() 
# fig = px.scatter_geo(world_df, locations="iso_alpha", color="continent",
#                      hover_name="country", size = 'Wine_count', projection="natural earth")
# fig.show()


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter





app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

wine_df = pd.read_csv("data/clean/cleaned_wine_data.csv")

province_list = wine_df['province'].unique().tolist()
variety_list = wine_df['variety'].unique().tolist()
    
app.layout = dbc.Container([
    
    # Header
        html.Div(
            [        html.H1('WineSense Dashboard'),        html.H3('A Comprehensive Dashboard for Assessing Wine Quality')    ],
            style={
                'backgroundColor': 'blue',
                'padding': 20,
                'color': 'lightgray',
                'margin-top': 20,
                'margin-bottom': 20,
                'text-align': 'center',
                'font-size': '48px',
                'border-radius': 3
            }
        ),

    # Filters
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    html.Label('Select By Province'),
                    dcc.Dropdown(
                        id="row-dropdown1",
                        options=[
                            {"label": row, "value": row} for row in province_list
                        ],
                        value="California",
                    )
                ],
                style={'margin': '10px'}
            ),
            width={"size": 3, "offset": 1}
        ),
        dbc.Col(
            html.Div(
                [
                    html.Label('Select the Variety of Wine'),
                    dcc.Dropdown(
                        id="row-dropdown2",
                        options=[
                            {"label": row, "value": row} for row in variety_list
                        ],
                        value="Pinot Noir",
                    )
                ],
                style={'margin': '10px'}
            ),
            width={"size": 3}
        )
    ],
        style={
            'background-color': '#f8f9fa',
            'padding': '15px',
            'margin': '20px',
            'border-radius': '3px',
            'box-shadow': '0px 0px 10px #ddd'
        }
    ),

    # Charts
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='pie_chart'),
            width={"size": 5, "offset": 1},
            style={'margin': '10px'}
        ),
        dbc.Col(
            dcc.Graph(id='world_map'),
            width={"size": 5},
            style={'margin': '10px'}
        )
    ],
        style={
            'background-color': '#f8f9fa',
            'padding': '15px',
            'margin': '20px',
            'border-radius': '3px',
            'box-shadow': '0px 0px 10px #ddd'
        }
    ),

    # Price Chart
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='variety_price'),
            width={"size": 10, "offset": 1},
            style={'margin': '10px'}
        )
    ],
        style={
            'background-color': '#f8f9fa',
            'padding': '15px',
            'margin': '20px',
            'border-radius': '3px',
            'box-shadow': '0px 0px 10px #ddd'
        }
    )

], fluid=True)



# Set up callbacks/backend
@app.callback(
    Output('pie_chart', 'figure'),
    Output('world_map', 'figure'),
    Output('variety_price', 'figure'),
    Input("row-dropdown1", "value"),
    Input("row-dropdown2", "value")
)
def generate_chart(drop1, drop2):
    if (drop1 is not None and drop2 is not None ):

        pie_data = wine_df[wine_df['province'] == drop1]
        pie_data = pie_data.groupby('variety').agg({'Wine_count': 'sum'}).reset_index()
        pie_data['percentage'] = round(pie_data['Wine_count'] / pie_data['Wine_count'].sum() * 100, 2)
        

        pie_chart = go.Figure(
            data=[go.Bar(
                x=pie_data['percentage'],
                y=pie_data['variety'],
                orientation='h',
                marker=dict(color='#1f77b4'),
                text=pie_data['percentage'].astype(str) + '%',
                textposition='auto',
                hovertemplate='Variety: %{y}<br>' + 'Percentage: %{x}%<br>',
                hoverlabel=dict(bgcolor='#1f77b4', font_size=12),
            )],
            layout=go.Layout(
                title=go.layout.Title(
                    text='Percentage of Wines by Variety in {}'.format(drop1),
                    font=dict(size=16, color='#212529', family='Arial, sans-serif')
                ),
                xaxis=go.layout.XAxis(
                    title=go.layout.xaxis.Title(
                        text='Percentage of Wines',
                        font=dict(size=14, color='#212529', family='Arial, sans-serif')
                    ),
                    tickfont=dict(size=12, color='#212529', family='Arial, sans-serif'),
                    tickformat='%{x:.1f}%',
                    showgrid=False,
                    zeroline=False,
                ),
                yaxis=go.layout.YAxis(
                    title=go.layout.yaxis.Title(
                        text='Variety',
                        font=dict(size=14, color='#212529', family='Arial, sans-serif')
                    ),
                    tickfont=dict(size=12, color='#212529', family='Arial, sans-serif'),
                    showgrid=False,
                    zeroline=False,
                ),
                margin=dict(l=50, r=50, t=70, b=50),
            )
        )
        world_df = wine_df.groupby('country').first().reset_index() 
        world_map = px.scatter_geo(world_df, locations="iso_alpha", color="continent",
                            hover_name="country", size = 'Wine_count', projection="natural earth")
        
        world_map.update_layout(
        title={
            'text': "Wine Production by Country",
            'font': {'size': 20}
            }
        )
        variety_data = wine_df[(wine_df['province'] == drop1) & (wine_df['variety'] == drop2)]
        variety_price = px.box(variety_data, x="province", y="price", 
                                    labels={'province': 'Province', 'price': 'Price'},
                                    title='Price distribution of {} in {}'.format(drop2, drop1),
                                    color="province")
        variety_price.update_traces(marker=dict(opacity=0.8))
    
                
                
    return pie_chart,world_map,variety_price

if __name__ == '__main__':
    app.run_server(debug=True)