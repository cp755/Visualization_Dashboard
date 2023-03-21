import pandas as pd
import plotly.express as px
from datetime import datetime
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
from dateutil.relativedelta import relativedelta

# Load the data

df = pd.read_csv('Heatspot_2022.csv')
df['date'] = pd.to_datetime(df['ACQ_DATE'])
df['Date'] = df['date'].dt.date
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['time'] = pd.to_datetime(df['ACQ_TIME']).dt.time
df['hour'] = pd.to_datetime(df['ACQ_TIME']).dt.hour
df.sort_values(by=['date'], inplace=True)
df['lat'] = df['LATITUDE']
df['lon'] = df['LONGITUDE']
df['brightness'] = df['BRIGHTNESS']
df['country'] = df['CT_EN']
df.drop(df[df['country'] == 'Singapore'].index, inplace = True)

# Create the app card

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], suppress_callback_exceptions=True)

pick_date =  html.Div(
    [
        dcc.DatePickerRange(
            min_date_allowed=min(df['date']),
            max_date_allowed=max(df['date']),
            start_date=min(df['date']),
            end_date=max(df['date']),
            display_format='MMM YYYY',
            id='date-picker-range',
            start_date_placeholder_text = 'Start Period',
            end_date_placeholder_text = 'End Period',
            style={
                      'background-color': 'white',
                      'border-color': 'white',
                      'color': 'red',
                      'place-holder-color':'blue'

                     }
        )
    ]
)

pick_country = html.Div(
    [
        dcc.Dropdown(
            id='country-dropdown',
            multi=True,
            placeholder="Select a country",
            options=[{'label': c, 'value': c} for c in df['country'].unique()],
            value=['Thailand', 'Indonesia'],
            className='bg-dark border-secondary',
            style={
                'backgroundColor': 'black',
                'color': 'black'}
        )
    ]
)

card_heat_map = dbc.Card(
    [
        dbc.CardBody(
            dcc.Graph(id='heat_map', config={'displayModeBar': False}, figure={})
        )
    ]
)

card_average_fire = dbc.Card(
    [
        dbc.CardBody(
            [
            html.H5('Average Fire Per Day', className='text-left'),
            html.Div(id='average_fire', className='card-text text-center', style={'font-size': '36px'})
            ]
        )
    ]
)

card_fire_total = dbc.Card(
    [
        dbc.CardBody(
            [
            html.H5('Total Fire', className='text-left'),
            html.Div(id='fire_total', className='card-text text-center', style={'font-size': '36px'})
            ]
        )
    ]
)

card_line_chart = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(id='line_chart', config={'displayModeBar': False}, figure={})
            ]
        )
    ]
)

card_bar_chart = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(id='bar_chart', config={'displayModeBar': False}, figure={})
            ]
        )
    ]
)

####################################################################################


# Create the app layout

app.layout = dbc.Container(
    [
        html.Link(rel='stylesheet', href='/absolute/path/to/custom.css'),
        dbc.Row([
            dbc.Col(html.H3('Fire Monitoring System', className="text-start")),
            dbc.Col(pick_date, className="text-end"),
            dbc.Col(pick_country, className="text-end"),
        ], justify="around"),
        html.Hr(),

        dbc.Row([
            dbc.Col(card_heat_map, width=6),
            dbc.Col([
                dbc.Row([
                    dbc.Col(card_average_fire, width=6),
                    dbc.Col(card_fire_total, width=6),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(card_line_chart, width=12),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(card_bar_chart, width=12),
                ])
            ],),
        ], justify="around"),
    ],
)



####################################################################################

# Create the callbacks

@app.callback(
    Output('heat_map', 'figure'),
    [Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('country-dropdown', 'value')]
)

def update_heat_map(start_date, end_date, country):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['country'].isin(country))]

    filtered_df['month'] = filtered_df['date'].apply(lambda x: x.strftime('%Y-%m'))
    unique_months = len(filtered_df['month'].unique())
    
    if unique_months > 1:  # One month or more
        x = 'month'
    else:  # Less than one month, switch to daily data
        x = 'Date'

    fig = px.density_mapbox(filtered_df, 
                            lat='lat', 
                            lon='lon', 
                            z='brightness', 
                            radius=3,
                            center=dict(lat=filtered_df['lat'].mean(), 
                                        lon=filtered_df['lon'].mean()),
                            zoom=4, 
                            range_color=[200, 400], 
                            height=800, 
                            template='plotly_dark', 
                            mapbox_style='carto-darkmatter',
                            animation_frame=x)
    
    fig.update_layout (margin={"r":0,"t":0,"l":0,"b":0})
    return fig

####################################################################################

@app.callback(
    Output('average_fire', 'children'),
    [Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('country-dropdown', 'value')]
)

def update_average_fire(start_date, end_date, country):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['country'].isin(country))]
    average_fire = round(filtered_df['date'].value_counts().mean())
    
    return average_fire


####################################################################################


@app.callback(
    Output('fire_total', 'children'),
    [Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('country-dropdown', 'value')]
)

def update_fire_total(start_date, end_date, country):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['country'].isin(country))]
    fire_total = filtered_df['date'].value_counts().sum()
    return '{:,.0f}'.format(fire_total)

####################################################################################

@app.callback(
    Output('line_chart', 'figure'),
    [Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('country-dropdown', 'value')]
)


def update_line_chart(start_date, end_date, country):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['country'].isin(country))]
    
    # Check if the filtered data contains at least one full month
    filtered_df['month'] = filtered_df['date'].apply(lambda x: x.strftime('%Y-%m'))
    unique_months = len(filtered_df['month'].unique())
    
    if unique_months > 1:  # One month or more
        filtered_df = filtered_df.groupby(['month', 'country']).size().reset_index(name='fire_count')
        x_axis = 'month'
        x_label = 'Month'
    else:  # Less than one month, switch to daily data
        filtered_df = filtered_df.groupby(['date', 'country']).size().reset_index(name='fire_count')
        x_axis = 'date'
        x_label = 'Date'

    fig = px.line(filtered_df,
                  x=x_axis,
                  y="fire_count",
                  color='country',
                  title='Fires by Country',
                  labels={x_axis: x_label, 'fire_count': 'Fire Count', 'country': 'Country'},
                  template='plotly_dark'
                  )
    fig.update_layout(height=300)

    return fig


####################################################################################

@app.callback(
    Output('bar_chart', 'figure'),
    [Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('country-dropdown', 'value')]

)   

def update_bar_chart(start_date, end_date, country):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['country'].isin(country))]
    filtered_df = filtered_df.groupby(['hour', 'country']).size().reset_index(name='fire_count')
    fig = px.bar(filtered_df, x='hour', y='fire_count', color='country', template='plotly_dark')
    fig.update_layout(height=300)
    return fig

####################################################################################

















if __name__ == '__main__':
    app.run_server(debug=True)


# filtered_df = df.groupby(['time', 'country'])['brightness'].count().reset_index()
# filtered_df.head(20)