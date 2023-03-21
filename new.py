import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objects as go



# Load the data

df = pd.read_csv('sales.csv')
df.head()

df['Date'] = pd.to_datetime(df['Date'])
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year

ctx = dash.callback_context

# Create the app

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_left = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Revenue", className="card_subtitle"),
                html.Div(id='revenue', style={'font-size': '36px'}, className='text-center')
            ]
        )
    ],
)

card_second_left = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Profit", className="card_subtitle"),
                html.Div(id='profit', style={'font-size': '36px'}, className='text-center')
            ]
        )
    ],
)

card_middle = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Average Sales", className="card_subtitle"),
                html.Div(id='average-sales', style={'font-size': '36px'}, className='text-center')
            ]
        )
    ],
)

card_second_right = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Orders", className="card_subtitle"),
                html.Div(id='orders', style={'font-size': '36px'}, className='text-center')
            ]
        )
    ],
)

card_right = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Expense", className="card_subtitle"),
                html.Div(id='expenses', style={'font-size': '36px'}, className='text-center')
            ]
        )
    ],
)

card_line = dbc.Card(
    [
        dbc.CardBody(

            dcc.Graph(id='revenue_line', figure={}),

        )
    ]
)

card_bar = dbc.Card(
    [
        dbc.CardBody(

            dcc.Graph(id='region_performance', figure={}),
             

        )
    ]
)

card_product_bar = dbc.Card(
    [
        dbc.CardBody(

            dcc.Graph(id='product_bar', figure={}),

        )
    ]
)

card_performance_bar = dbc.Card(
    [
        dbc.CardBody(

            dcc.Graph(id='performance_bar', figure={}),

        )
    ]
)

Fiscal_year_bottom =    html.Div([
                        html.Button('2010', id='btn-nclicks-1', n_clicks=0),
                        html.Button('2011', id='btn-nclicks-2', n_clicks=0),
                        html.Button('All', id='btn-nclicks-3', n_clicks=0),
                        html.Div(id='container-button-timestamp')
])


#####################################################################################################################



app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.H1("Dashboard", className="text-start")),
        dbc.Col(children=[
                html.H3("Fiscal Year: ", className="text-end"),
                Fiscal_year_bottom
], width=5, className='text-end')

    ],justify='around'),
    html.Hr(),
    html.Br(),

    dbc.Row([
        dbc.Col(card_left, width=2),
        dbc.Col(card_second_left, width=2),
        dbc.Col(card_middle, width=2),
        dbc.Col(card_second_right, width=2),
        dbc.Col(card_right, width=2)], justify='around'),

    html.Br(),

    dbc.Row([
        dbc.Col(card_line, width=7),
        dbc.Col(card_bar, width=5)], justify='around'),

    html.Br(),

    dbc.Row([
        dbc.Col(card_product_bar, width=7),
        dbc.Col(card_performance_bar, width=5)], justify='around')

])

##############################################################################################################


# Create the callbacks

@app.callback(
    Output('revenue', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)

def update_revenue(n_clicks_1, n_clicks_2, n_clicks_3):
    total_revenue = df['Sales'].sum()
    if 'btn-nclicks-1'== ctx.triggered_id:
        total_revenue = df[df['year'] == 2010]['Sales'].sum()
    elif 'btn-nclicks-2'== ctx.triggered_id:
        total_revenue = df[df['year'] == 2011]['Sales'].sum()
    elif 'btn-nclicks-3'== ctx.triggered_id:
        total_revenue = df['Sales'].sum()
    
    return '{:,.0f}'.format(total_revenue)


@app.callback(
    Output('profit', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)

def update_profit(n_clicks_1, n_clicks_2, n_clicks_3):
    total_profit = df['Profit'].sum()
    if 'btn-nclicks-1'== ctx.triggered_id:
        total_profit = df[df['year'] == 2010]['Profit'].sum()
    elif 'btn-nclicks-2'== ctx.triggered_id:
        total_profit = df[df['year'] == 2011]['Profit'].sum()
    elif 'btn-nclicks-3'== ctx.triggered_id:
        total_profit = df['Profit'].sum()
    
    return '{:,.0f}'.format(total_profit)

@app.callback(
    Output('average-sales', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)

def update_average_sales(n_clicks_1, n_clicks_2, n_clicks_3):
    average_sales = df['Sales'].sum()/df['Sales'].count()
    if 'btn-nclicks-1'== ctx.triggered_id:
        average_sales = df[df['year'] == 2010]['Sales'].sum()/df[df['year'] == 2010]['Sales'].count()
    elif 'btn-nclicks-2'== ctx.triggered_id:
        average_sales = df[df['year'] == 2011]['Sales'].sum()/df[df['year'] == 2011]['Sales'].count()
    elif 'btn-nclicks-3'== ctx.triggered_id:
        average_sales = df['Sales'].sum()/df['Sales'].count()

    return '{:,.0f}'.format(average_sales)



@app.callback(
    Output('orders', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)

def update_orders(n_clicks_1, n_clicks_2, n_clicks_3):
    total_orders = df['Sales'].count()
    if 'btn-nclicks-1'== ctx.triggered_id:
        total_orders = df[df['year'] == 2010]['Sales'].count()
    elif 'btn-nclicks-2'== ctx.triggered_id:
        total_orders = df[df['year'] == 2011]['Sales'].count()
    elif 'btn-nclicks-3'== ctx.triggered_id:
        total_orders = df['Sales'].count()
    
    return '{:,.0f}'.format(total_orders)



@app.callback(
    Output('expenses', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)

def update_expenses(n_clicks_1, n_clicks_2, n_clicks_3):
    total_expenses = df['Total Expenses'].sum()
    if 'btn-nclicks-1'== ctx.triggered_id:
        total_expenses = df[df['year'] == 2010]['Total Expenses'].sum()
    elif 'btn-nclicks-2'== ctx.triggered_id:
        total_expenses = df[df['year'] == 2011]['Total Expenses'].sum()
    elif 'btn-nclicks-3'== ctx.triggered_id:
        total_expenses = df['Total Expenses'].sum()
    
    return '{:,.0f}'.format(total_expenses)





##############################################################################################################


@app.callback(
    Output('revenue_line', 'figure'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks')
)

def update_revenue_line(n_clicks_1, n_clicks_2):
    if n_clicks_1 > n_clicks_2:
        df_line = df[df['year'] == 2010]
    elif n_clicks_2 > n_clicks_1:
        df_line = df[df['year'] == 2011]
    else:
        df_line = df
    
    df_line = df_line.groupby(['Date'])['Sales'].sum().reset_index()
    
    fig = go.Figure()
    
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'title': {
            'text': 'Revenue by Category',
            'font': {'size': 20}
        },
        'xaxis': {
            'title': 'Order Date',
            'showgrid': False
        },
        'yaxis': {
            'title': 'Revenue',
            'range': [30000, None]
        }
    })

    fig.add_trace(go.Scatter(
        x=df_line['Date'],
        y=df_line['Sales'],
        mode='lines',
        fill='tozeroy',
        line_color='#accbff', #what is the color blue in hex?
        showlegend=False
    ))


    return fig

@app.callback(
    Output('region_performance', 'figure'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks')
)

def update_region_performance(n_clicks_1, n_clicks_2):
    if n_clicks_1 > n_clicks_2:
        df_region = df[df['year'] == 2010]
    elif n_clicks_2 > n_clicks_1:
        df_region = df[df['year'] == 2011]
    else:
        df_region = df
    
    df_region = df_region.groupby(['Market','Product Type'])['Sales'].sum().reset_index().sort_values('Sales', ascending=True)

    fig = px.bar(df_region, y='Market', x='Sales', color = 'Product Type', orientation= 'h')
    fig.update_layout(title='Revenue by Region', xaxis_title='Region', yaxis_title='Revenue')
    return fig

@app.callback(
    Output('product_bar', 'figure'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks')
)

def update_product_bar(n_clicks_1, n_clicks_2):
    if n_clicks_1 > n_clicks_2:
        df_product = df[df['year'] == 2010]
    elif n_clicks_2 > n_clicks_1:
        df_product = df[df['year'] == 2011]
    else:
        df_product = df
    
    df_product = df_product.groupby(['Product'])['Sales'].sum().reset_index()

    fig = px.bar(df_product, x='Product', y='Sales')
    fig.update_layout(title='Revenue by Product', xaxis_title='Product', yaxis_title='Revenue')
    return fig

@app.callback(
    Output('performance_bar', 'figure'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks')
)

def update_performance_bar(n_clicks_1, n_clicks_2):
    if n_clicks_1 > n_clicks_2:
        df_performance = df[df['year'] == 2010]
    elif n_clicks_2 > n_clicks_1:
        df_performance = df[df['year'] == 2011]
    else:
        df_performance = df

    df_performance = df_performance.groupby(['Product'])['Profit'].sum().reset_index()

    fig = px.bar(df_performance, x='Product', y='Profit')
    fig.update_layout(title='Performance by Product', xaxis_title='Product', yaxis_title='Profit')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)

