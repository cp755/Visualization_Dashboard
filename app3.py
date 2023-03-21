import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from datetime import datetime

##https://fire.gistda.or.th/

# Load the data
df = pd.read_csv('Heatspot_2022.csv')

df = pd.read_csv('Heatspot_2022.csv')
df['date'] = pd.to_datetime(df['ACQ_DATE'])
df = df.sort_values('date')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df = df[df['year'] == 2022]
df['lat'] = df['LATITUDE']
df['lon'] = df['LONGITUDE']
df['brightness'] = df['BRIGHTNESS']
df['country'] = df['CT_EN']
df.drop(df[df['country'] == 'Singapore'].index, inplace = True)


# Create the app and set the layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container([
    html.Br(),
    html.H1('Fire Monitoring System', className='text-center mb-5'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
                    html.H4('Select Country', className='text-center'),
                    dcc.Dropdown(
            id='country-dropdown',
            multi=True,
            placeholder="Select a country",
            options=[{'label': c, 'value': c} for c in df['country'].unique()],
            value=['Thailand', 'Indonesia','China','Laos'],
            className='border rounded text-secondary bg-dark border-dark',
            style={
                    'background-color': '#1f2630'
                }
),
            html.Br(),
            html.H4('Select Date Range', className='text-center'),
            
          dcc.RangeSlider(
            id='date-slider',
            min=df['date'].min().date().toordinal(),
            max=df['date'].max().date().toordinal(),
            step=1,
            marks={date.toordinal(): date.strftime('%b') if date.month % 2 == 0 else '' for date in pd.date_range(start=df['date'].min().date(), end=df['date'].max().date(), freq='D') if date.day == 1},
            value=[df['date'].min().date().toordinal(), df['date'].max().date().toordinal()],
            className='border rounded text-secondary bg-dark',
            allowCross=False
),

            html.Br(),
            html.Br(),
            html.H4('Average Fires Per Day',className='text-center'),

            html.Br(),
            html.Div(id='average-fires', style={'font-size': '36px'},className='text-center')
        ], width=3),

        dbc.Col([
            dcc.Graph(id='fire-map')
        ], width=5),

        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='graph_2')
                ]),

        
            ]),
        html.Br(),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='graph_3')
                ])
            ])
        ], width=4)
    ]),

        html.Div([
                html.A('Data Source', 
                        href='https://fire.gistda.or.th/download/12_summary_hotspot_modis.html', 
                        target='_blank'),
            ], style={'position': 'fixed', 'bottom': '10px', 'left': '10px'})], 
            fluid=True)


# Graph 1

@app.callback(
    Output('fire-map', 'figure'),
    Input('country-dropdown', 'value'),
    Input('date-slider', 'value')
)
def update_map(countries, date_range):
    start_date = datetime.fromordinal(date_range[0])
    end_date = datetime.fromordinal(date_range[1])
    
    filtered_df = df[(df['country'].isin(countries)) & (df['date'] >= start_date) & (df['date'] <= end_date)]

    # # Convert 'date' column back to string format
    # filtered_df['date'] = filtered_df['date'].dt.strftime('%Y-%m-%d')

    
    fig = px.scatter_mapbox(filtered_df, lat="lat", lon="lon", zoom=3, 
                            center=dict(lat=filtered_df['lat'].mean(), 
                            lon=filtered_df['lon'].mean()),
                            mapbox_style='carto-darkmatter',
                            height=920, 
                            template='plotly_dark',)
    fig.update_traces(cluster=dict(enabled=True))

    print(filtered_df)

    # fig = px.density_mapbox(filtered_df, 
    #                         lat='lat', 
    #                         lon='lon', 
    #                         z='brightness', 
    #                         radius=5,
    #                         center=dict(lat=filtered_df['lat'].mean(), 
    #                                     lon=filtered_df['lon'].mean()),
    #                         zoom=4,animation_frame='month', 
    #                         range_color=[200, 400], 
    #                         height=920, 
    #                         template='plotly_dark', 
    #                         mapbox_style='carto-darkmatter')

    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    return fig

## Average Fires Per Day


@app.callback(
    Output('average-fires', 'children'),
    Input('country-dropdown', 'value'),
    Input('date-slider', 'value')
)
def update_average_fires(countries, date_range):
    start_date = datetime.fromordinal(date_range[0])
    end_date = datetime.fromordinal(date_range[1])

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
                  title='Monthly Fires by Country',
                  labels={'month': 'Month', 'fire_count': 'Fire Count', 'country': 'Country'},
                  template='plotly_dark'
                  )
    return fig


## Graph 3

@app.callback(
    Output(component_id='graph_3', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value'),
    Input(component_id='date-slider', component_property='value')
)
def update_graph_3(option_slctd, date_range):
    start_date = datetime.fromordinal(date_range[0])
    end_date = datetime.fromordinal(date_range[1])
    dff = df.copy()
    dff = dff[dff['country'].isin(option_slctd)]
    dff = dff[(dff['date'] >= start_date) & (dff['date'] <= end_date)]
    dff = dff.groupby('country').size().reset_index(name='fire_count')
    dff = dff.sort_values('fire_count', ascending=True)

    dff['avg_heat_spot'] = dff['fire_count']
    fig = px.bar(dff, x='fire_count', y='country', orientation='h', title='Fire Count by time period',
                 labels={'fire_count': 'Fire Count', 'country': 'Country'},
                 template='plotly_dark'
                 )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)



# fig = go.Figure()

#     fig.update_layout({
#         'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#         'paper_bgcolor': 'rgba(0, 0, 0, 0)',
#         'title': {
#             'text': 'Revenue by Category',
#             'font': {'size': 20}
#         },
#         'xaxis': {
#             'title': 'Order Date',
#             'showgrid': False
#         },
#         'yaxis': {
#             'title': 'Revenue'
#         }
#     })

#     fig.add_trace(go.Scatter(
#         x=df_line['Date'],
#         y=df_line['Sales'],
#         mode='lines',
#         fill='tozeroy',
#         line_color='#F63366',
#         showlegend=False
#     ))

#     df_line = df_line.groupby(['Date'])['Sales'].sum().reset_index()
#     fig = px.line(df_line, x='Date', y='Sales', title='Revenue by Date')
#     fig.update_layout(title='Revenue by Category', xaxis_title='Order Date', yaxis_title='Revenue', xaxis=dict(showgrid=False))
#     fig.update_layout({
#     'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'
#     }) 



import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=110, scope="asia",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()