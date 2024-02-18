import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define vehicle types and recession status options
vehicle_types = data['Vehicle_Type'].unique()
recession_statuses = data['Recession'].unique()

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Automobile Sales Analysis', style={'textAlign': 'center'}),

    html.Div(children='''
        Explore the impact of different factors on automobile sales.
    ''', style={'textAlign': 'center'}),

    html.Label('Select Vehicle Type:'),
    dcc.Dropdown(
        id='vehicle-type-dropdown',
        options=[{'label': vehicle_type, 'value': vehicle_type} for vehicle_type in vehicle_types],
        value=vehicle_types[0]
    ),

    html.Label('Select Recession Status:'),
    dcc.Dropdown(
        id='recession-dropdown',
        options=[{'label': 'Recession', 'value': 1}, {'label': 'Non-Recession', 'value': 0}],
        value=1
    ),

    # Output container
    html.Div(id='output-display', className='output-container'),

    # Graphs
    dcc.Graph(id='pie-chart'),
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bubble-chart'),
])

# Callback to update the output display based on dropdown selections
@app.callback(
    Output('output-display', 'children'),
    [Input('vehicle-type-dropdown', 'value'),
     Input('recession-dropdown', 'value')]
)
def update_output(selected_vehicle_type, selected_recession_status):
    return f'Selected Vehicle Type: {selected_vehicle_type}, Selected Recession Status: {selected_recession_status}'

# Callbacks to update the graphs based on dropdown selections
@app.callback(
    Output('pie-chart', 'figure'),
    Output('bar-chart', 'figure'),
    Output('line-chart', 'figure'),
    Output('bubble-chart', 'figure'),
    [Input('vehicle-type-dropdown', 'value'),
     Input('recession-dropdown', 'value')]
)
def update_graphs(selected_vehicle_type, selected_recession_status):
    filtered_data = data[(data['Vehicle_Type'] == selected_vehicle_type) & (data['Recession'] == selected_recession_status)]

    # Pie Chart
    pie_chart = px.pie(filtered_data, names='Year', title='Yearly Distribution',
                      labels={'Year': 'Year', 'value': 'Sales'},
                      hole=0.4)

    # Bar Chart
    bar_chart = px.bar(filtered_data, x='Year', y='Automobile_Sales', title='Yearly Sales',
                       labels={'Year': 'Year', 'Automobile_Sales': 'Sales'})

    # Line Chart
    line_chart = px.line(filtered_data, x='Year', y='Automobile_Sales', title='Yearly Sales Trend',
                         labels={'Year': 'Year', 'Automobile_Sales': 'Sales'})

    # Bubble Chart
    bubble_chart = px.scatter(filtered_data, x='Year', y='Automobile_Sales', size='Advertising_Expenditure',
                              title='Yearly Sales vs. Advertising Expenditure',
                              labels={'Year': 'Year', 'Automobile_Sales': 'Sales', 'Advertising_Expenditure': 'Advertising'},
                              size_max=30)

    return pie_chart, bar_chart, line_chart, bubble_chart

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
