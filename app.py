import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
from datetime import datetime as dt
import plotly.express as px
from dash_auth import BasicAuth

px.set_mapbox_access_token(r'pk.eyJ1IjoiZGF2ZTcwNTUiLCJhIjoiY2s1cGw2eDE5MDJ0ZjNucW9saWxvcXNxbCJ9.M4GmLRvRQ-ehFt4G7TZNYw')

username_passwords = [['admin','password']]

# Load and process data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
risk_data = pd.read_pickle('./data/risk_data.pickle')

# Build Dashboard

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

auth = BasicAuth(app,username_passwords)

# Defining Dash Core Components

placetypes = dcc.Dropdown(id='placetypes', options=[{'label':place_type, 'value':place_type} for place_type in risk_data['Type'].unique()], value='Supermarket')

visit_date = dcc.DatePickerSingle(id='visit_date', date=dt.today())

visit_times = ['7am-11am', '11am-3pm', '3pm-7pm', '7pm-11pm']

visit_time = dcc.RadioItems(id='visit_time',options=[{'label':i, 'value':i} for i in visit_times], value='7am-11am', labelStyle={'display': 'inline-block'})

graph_map = dcc.Graph(id='graph_map')

# Defining Dash Layout

app.layout = html.Div(children=[
    html.H1(children='Traceable : Technology to stop the pandemic'),
    html.Div(),
    html.Label(id='label_placetype', children='Place Type', style={'display':'inline-block', 'width':'150px','height':'1em','marginBottom':'15px'}),
    html.Div(children=[placetypes], style={'display':'inline-block', 'width':'600px','height':'1em','marginBottom':'15px'}),
    html.Div(),
    html.Label(id='label_visitdate', children='Visit Date', style={'display':'inline-block', 'width':'150px','height':'1em','marginBottom':'15px'}),
    html.Div(children=visit_date, style={'display':'inline-block', 'width':'150px','height':'1em','marginBottom':'25px'}),
    html.Div(children=visit_time, style={'display':'inline-block', 'width':'500px','height':'1em','marginBottom':'25px'}),
    html.Div(),
    graph_map
    ], style = {'align-items':'center', 'marginLeft':'50px', 'marginRight':'50px'})

# Linking Interactive Components

@app.callback(
    Output(component_id='graph_map',component_property='figure'),
    [Input(component_id='placetypes',component_property='value'),
    Input(component_id='visit_date',component_property='date'),
    Input(component_id='visit_time',component_property='value'),]
)
def update_graph(place_type, visit_date, visit_time):
    global risk_data, visit_times
    risk_data['visit_date'] = pd.to_datetime(risk_data['visit_date'])
    select_data = risk_data[(risk_data['Type']==place_type) & (risk_data['visit_time']==visit_time) & (risk_data['visit_date']==visit_date)]
    fig = px.scatter_mapbox(
        data_frame=select_data, 
        lat='lat', 
        lon='lng',
        size='visitor_count',
        hover_name='name',
        hover_data=['risk_level'],
        width=800, height=600, 
        title='Risk Score', 
        color='risk_level', 
        center={'lat':51.58, 'lon':-0.34},
        zoom=13,
        color_continuous_scale=px.colors.cyclical.IceFire
    )
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
    return fig





if __name__ == '__main__':
    app.run_server(debug=True)