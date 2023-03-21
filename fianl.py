import pandas as pd
import plotly.express as px
from datetime import datetime
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Load the data

df = pd.read_csv('Heatspot_2022.csv')
df['date'] = pd.to_datetime(df['ACQ_DATE'])
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['time'] = pd.to_datetime(df['ACQ_TIME']).dt.time
df.sort_values(by=['date'], inplace=True)
df['lat'] = df['LATITUDE']
df['lon'] = df['LONGITUDE']
df['brightness'] = df['BRIGHTNESS']
df['country'] = df['CT_EN']
df.drop(df[df['country'] == 'Singapore'].index, inplace = True)

# Create the app card

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

pick_date =  html.Div(
    [
        dcc.DatePickerRange(
            min_date_allowed=min(df['date']),
            max_date_allowed=max(df['date']),
            start_date=min(df['date']),
            end_date=max(df['date']),
            display_format='MMM YYYY',
            id='date-picker-range',
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
            value='Thailand',
            className='border rounded text-secondary bg-dark border-dark',
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
            html.H4('Average Fire Per Day', className='text-left card_title'),
            html.Div(id='average_fire', className='card-text text-center')
            ]
        )
    ]
)

card_fire_total = dbc.Card(
    [
        dbc.CardBody(
            [
            html.H4('Total Fire', className='text-left card_title'),
            html.Div(id='fire_total', className='card-text text-center')
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
        dbc.Row([
            dbc.Col(html.H1('Fire Monitoring System', className="text-start")),
            dbc.Col(pick_date, className="text-end"),
            dbc.Col(pick_country, className="text-end"),
        ], justify="between"),

        dbc.Row([
            dbc.Col(card_heat_map, width=6),
            dbc.Col(card_average_fire, width=3),
            dbc.Col(card_fire_total, width=3),
        ], justify="between"),

        dbc.Row([
            dbc.Col(card_line_chart, width=6),
        ]),

        dbc.Row([
            dbc.Col(card_bar_chart, width=6),
        ])
    ],
)

















if __name__ == '__main__':
    app.run_server(debug=True)


df['date'].value_counts()