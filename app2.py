import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from datetime import datetime


# Load the data
df = pd.read_csv('Heatspot_2022.csv')
df['date'] = pd.to_datetime(df['ACQ_DATE'])
df = df.sort_values('date')
df['month'] = df['date'].dt.month

df['month'].unique()
df['lat'] = df['LATITUDE']
df['lon'] = df['LONGITUDE']
df['brightness'] = df['BRIGHTNESS']
df['country'] = df['CT_EN']
df.drop(df[df['country'] == 'Singapore'].index, inplace = True)



# Create the app and set the layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container([
    html.H1('Fire Hotspots Dashboard', className='text-center mb-5'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
                    html.H4('Filter by Country', className='text-center'),
                    dcc.Dropdown(
            id='country-dropdown',
            multi=True,
            placeholder="Select a country",
            options=[{'label': c, 'value': c} for c in df['country'].unique()],
            value=['Thailand', 'Indonesia'],
            className='border rounded text-secondary bg-dark border-dark',
            style={
                    'background-color': '#1f2630'
                }
),
            html.Br(),
            html.H4('Filter by Date Range', className='text-center'),
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=min(df['date']),
                max_date_allowed=max(df['date']),
                start_date=datetime(year=2022, month=1, day=1),
                end_date=datetime(year=2022, month=12, day=31),
                display_format='MMM YYYY',
                style={
                    'background-color': '#1f2630',
                    'color': 'white',
                    'border': '1px solid white'
                },
                className='text-secondary'
),


            html.Br(),
            html.Br(),
            html.H4('Average Fires per Day',className='text-center'),

            html.Br(),
            html.Div(id='average-fires', style={'font-size': '36px'},className='text-center')
        ], width=2),
        dbc.Col([
            dcc.Graph(id='fire-map')
        ], width=6),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='graph_2')
                ]),
        html.Br(),
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='graph_3')
                ])
            ])
        ], width=4)
    ])
], fluid=True)




# Define the callbacks
@app.callback(
    Output('fire-map', 'figure'),
    Input('country-dropdown', 'value'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
)
def update_map(countries, start_date, end_date):
    filtered_df = df[(df['country'].isin(countries)) & (df['date'] >= start_date) & (df['date'] <= end_date)]

    # Convert 'date' column back to string format
    filtered_df['date'] = filtered_df['date'].dt.strftime('%Y-%m-%d')

    fig = px.density_mapbox(filtered_df, lat='lat', lon='lon', z='brightness', radius=5,
                            center=dict(lat=filtered_df['lat'].mean(), lon=filtered_df['lon'].mean()),
                            zoom=4,animation_frame='month', range_color=[0, 1000], height=900, template='plotly_dark', 
                            mapbox_style='carto-darkmatter')
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    return fig


@app.callback(
    Output('average-fires', 'children'),
    Input('country-dropdown', 'value'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
)
def update_average_fires(countries, start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    filtered_df = df[(df['country'].isin(countries)) & (df['date'] >= start_date) & (df['date'] <= end_date)]
    total_days = (end_date - start_date).days + 1

    if total_days > 0:
        avg_fires = filtered_df['brightness'].count() / total_days
        return str(int(avg_fires))
    else:
        return "N/A"



## Graph 2

@app.callback(
    Output(component_id='graph_2', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value')
)
def update_graph(option_slctd):
    dff = df.copy()
    dff = dff[dff["country"].isin(option_slctd)]
    fires_by_month = dff.groupby(['month', 'country']).size().reset_index(name='fire_count')
    # Create a line chart using Plotly Express
    fig = px.line(fires_by_month,
                  x="month",
                  y="fire_count",
                  color='country',
                  title='Fires by Month',
                  labels={'month': 'Month', 'fire_count': 'Fire Count', 'country': 'Country'},
                  template='plotly_dark'
                  )
    return fig

## Graph 3

@app.callback(
    Output(component_id='graph_3', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value'),
    Input(component_id='date-range', component_property='start_date'),
    Input(component_id='date-range', component_property='end_date')
)
def update_graph_3(option_slctd, start_date, end_date):
    dff = df.copy()
    dff = dff[dff['country'].isin(option_slctd)]
    dff = dff[(dff['date'] >= start_date) & (dff['date'] <= end_date)]
    dff = dff.groupby('country').size().reset_index(name='fire_count')
    dff = dff.sort_values('fire_count', ascending=True)

    dff['avg_heat_spot'] = dff['fire_count']
    fig = px.bar(dff, x='fire_count', y='country', orientation='h', title='Overall Heat Spot per time period',
                 labels={'fire_count': 'Fire Count', 'country': 'Country'},
                 template='plotly_dark'
                 )
    return fig






if __name__ == '__main__':
    app.run_server(debug=True)

