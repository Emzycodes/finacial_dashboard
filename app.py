import os
from dash import Dash, html,dcc,dash_table
import plotly.express as px 
import pandas as pd 
from file import Reports


    
report = Reports() 
app = Dash(__name__)
# App Layouts
app.layout = html.Div(children = [
    html.H1(children='Department Of Financee',
            style = {
                'textAlign': 'center', 
                'fontFamily': 'Arial, sans-serif'
                }),
    
    html.Div(children=
        'Financial Report Dashboard',
        style={'textAlign': 'center',
                 'color': 'blue',
                 'fontFamily': 'Helvetica Neue, Helvetica, Arial, sans-serif',
                 'fontSize': '22px',
                 'fontWeight': 'bold' 
}
    ),
    
    html.Div(children=[
        
    
    dash_table.DataTable(
        data= report.file_dict,
        style_table= {'width': '50%', 'margin-top': '4%','display':'inline-block'},
        style_cell= {'textAlign': 'left', 'padding' : '5px',  'fontFamily': 'Arial, sans-serif',
                     'fontSize': '14px',
                     'color': 'black'},
        style_header= {'backgroundColor': 'lightGrey','fontWeight': 'bold','fontSize': '14px'},
        style_data= {'height': 'auto', 'whiteSpace' : 'normal'},
        
        ),
    
    dcc.Graph(id='time_series_plot',
        figure= {
            'data': [
                {'x': report.date(), 'y': report.revenue(),'type':'line','name':'Revenue' },
                {'x': report.date(), 'y': report.expenses(),'type':'line','name':'Expenses' }
            ]
        },
        style= {'width': '50%','display': 'inline-block', 'float': 'right','position': 'absolute',
                'top': '40px','left': '50%','margin-top': '60px','padding-top': '0px',
                }
    )
    
    ],style= {'width': '100%', 'display':'inline-block'})  
    
])
if __name__ == '__main__':
    app.run(debug=True)