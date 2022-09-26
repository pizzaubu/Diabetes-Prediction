#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output


# In[2]:


df = pd.read_csv("diabetes.csv")
df


# In[ ]:


app = dash.Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H4('Prediction of diabetes'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label':'Pregnancies','value':'Pregnancies'},
        {'label':'Glucose','value':'Glucose'},
        {'label':'BloodPressure','value':'BloodPressure'},
        {'label':'SkinThickness','value':'SkinThickness'},
        {'label':'Insulin','value':'Insulin'},
        {'label':'BMI','value':'BMI'},
        {'label':'DiabetesPedigreeFunction','value':'DiabetesPedigreeFunction'},
        {'label':'Age','value':'Age'},
        {'label':'Outcome','value':'Outcome'}],
        value=['Age','Insulin','BMI'],
        multi = True
    ),
    dcc.Graph(id='graph'),
])

@app.callback(
    Output('graph','figure'),
    Input('dropdown','value'))

def update_bar_chart(dims):
    fig=px.scatter_matrix(
        df,dimensions=dims)
    return fig


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='3021') 


# In[ ]:




