import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_katex

import numpy as np
import plotly.express as px
from scipy import stats

from app import app

layout = html.Div([
    dash_katex.DashKatex(
        expression=r'f_X(x) = (1 - p)^{x - 1}p',
        displayMode=True
    ),
    dcc.Graph(id='geometric_graph'),
    dash_katex.DashKatex(expression=r'p'),
    dcc.Slider(
        id='geometric_p',
        value=0.5,
        min=0.01,
        max=1.0,
        marks={p: f'{p:.1f}' for p in [i * 0.1 for i in range(1, 11)]},
        step=0.01,
        tooltip={'placement': 'top'}
    ) 
])


@app.callback(
    Output('geometric_graph', 'figure'),
    [Input('geometric_p', 'value')]
)
def plot(p):
    x = np.arange(1, 11)
    y = stats.geom.pmf(x, p)
    range_x = [0, 11]
    range_y = [-0.2, 1.2]
    figure = px.scatter(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
