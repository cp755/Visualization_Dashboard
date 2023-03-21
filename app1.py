import dash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Point
import geopandas
import plotly_express as px
from dash import Dash, dcc, html, Input, Output
from datetime import date
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )


## import file

df1 = pd.read_csv('Heatspot_2022.csv')

## Remove column to only needed columns

df = df1[['index','HotSpotID','LATITUDE','LONGITUDE','BRIGHTNESS','ACQ_DATE', 'ACQ_TIME','CT_EN']]
df.set_index('index', inplace = True)
df = df.rename({'ACQ_DATE' : 'DATE', 'ACQ_TIME' : 'TIME', 'CT_EN':'COUNTRY'}, axis = 'columns')

## Set time index
df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime('%Y-%m-%d')
df['MONTH'] = pd.to_datetime(df['DATE']).dt.month
avg_fires_per_day = df.groupby('MONTH')['HotSpotID'].count().mean()




df = df.sort_values(by='DATE', ascending=True)
df.reset_index(inplace = True)

options = [{'label': country, 'value': country} for country in ['Indonesia', 'Cambodia', 'Thailand', 'Vietnam', 'Malaysia', 'China', 'Myanmar', 'Laos']]


## App layout

app.layout = dbc.Container(
    [
    html.Br(),

    dbc.Row(
        dbc.Col(html.H1('Heat Spot DashBoard', 
        className='text-center mb-3 fw-bold display-1'),
            )
    ),
    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="slct_country",
                 options=options,
                 multi=False,
                 value='Thailand',
                 className='border rounded'),

            html.Br(),

            dcc.Graph(id='heatspot_map', figure={})
        ], width = {'size': 6}),

        dbc.Col([

            html.Div(
                id='fire_average_box',
                className='border rounded p-3 mb-3 text-center'
                    ),

            dcc.Dropdown(id='slct_multi_country', multi=True, value=['Thailand', 'Indonesia', 'Vietnam', 'Malaysia'],
                 options=options),

            html.Br(),

            dcc.Graph(id='heatspot_line', figure={}),

            html.Br(),

            dcc.Dropdown(id='slct_multi_country2', multi=True, value=['Thailand', 'Indonesia', 'Vietnam', 'Malaysia'],
                 options=options),

            html.Br(),

            dcc.Graph(id='heatspot_bar', figure={}),

            html.Br(),

            html.Div(
                [
                    'Data by',
                    html.A(
                        'Gistda.or.th',
                        href='https://fire.gistda.or.th/download/12_summary_hotspot_modis.html',
                        target = 'blank',
                    ),
                ],
            ),
        ], width = {'size': 6},)
    ]),

    dbc.Row([

    ])
], fluid = True)








## Callback for map
@app.callback(
    Output(component_id='heatspot_map', component_property='figure'),
    Input(component_id='slct_country', component_property='value')
)

def update_graph(option_slctd):
    
    dff=df.copy()
    dff = dff[dff["COUNTRY"] == option_slctd]
    Location = {
    'Indonesia': {'lat': -0.7893, 'lon': 113.9213},
    'Cambodia': {'lat': 12.5657, 'lon': 104.9910},
    'Thailand': {'lat': 15.8700, 'lon': 100.9925},
    'Vietnam': {'lat': 14.0583, 'lon': 108.2772},
    'Malaysia': {'lat': 4.2105, 'lon': 101.9758},
    'China': {'lat': 26.8617, 'lon': 104.1954},
    'Myanmar': {'lat': 21.9162, 'lon': 95.9550},
    'Laos': {'lat': 19.8563, 'lon': 102.4955}
}

        # Plotly Express
    fig = px.density_mapbox(dff, lat='LATITUDE', 
                                lon='LONGITUDE', 
                                radius=5,
                                center=dict(lat=Location[option_slctd]['lat'], lon=Location[option_slctd]['lon']), 
                                zoom=5,
                                mapbox_style="open-street-map",
                                hover_name="COUNTRY", 
                                hover_data=["BRIGHTNESS", 'DATE'],
                                animation_frame="MONTH",
                                animation_group="COUNTRY",
                                height=1400
                                )
    return fig


## Callback for average fire box

@app.callback(
    Output('fire_average_box', 'children'),
    Input('slct_country', 'value')
)
def update_fire_average_box(country):
    selected_df = df[df['COUNTRY'] == country]
    average_fires = selected_df.groupby('MONTH').size().mean().round(0)
    return html.H4(f'Average Fires per Day: {average_fires:.2f}')


## Callback for line chart
@app.callback(
    Output(component_id='heatspot_line', component_property='figure'),
    Input(component_id='slct_multi_country', component_property='value')
)

def update_graph(option_slctd):
    dff=df.copy()
    dff = dff[dff["COUNTRY"].isin(option_slctd)]
    dff = dff.groupby(['MONTH', 'COUNTRY'])['index'].count().reset_index()
    fig = px.line(dff, 
                    x="MONTH", 
                    y="index", 
                    color='COUNTRY',)
    return fig

## Callback for bar chart
@app.callback(
    Output(component_id='heatspot_bar', component_property='figure'),
    Input(component_id='slct_multi_country2', component_property='value')
)

def update_graph(option_slctd):
    dff = df.copy()
    dff = dff[dff["COUNTRY"].isin(option_slctd)]
    average_fire_country = dff.groupby('COUNTRY').size().div(12).sort_values(ascending=True)
    bar = px.bar(average_fire_country, 
                    y=average_fire_country.index, 
                    x=average_fire_country.values, 
                    title='Average Heat Spot Per Month',
                    width=1000, height=800,
                    labels={'COUNTRY':'Country', 'Number of Fire':'Number of Fire'},
                    orientation='h')
    return bar


if __name__=='__main__':
    app.run_server(debug=True)
