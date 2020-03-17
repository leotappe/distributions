import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_katex

import numpy as np
import plotly.express as px
from scipy import stats
import math

from app import app

layout = html.Div([
    dash_katex.DashKatex(
        expression=r'''
            f_X(x) = \frac{\lambda^x e^{-\lambda}}{x!}
        ''',
        displayMode=True
    ),
    dcc.Graph(id='poisson_graph'),
    dash_katex.DashKatex(expression=r'\lambda'),
    dcc.Slider(
        id='poisson_rate',
        value=1,
        min=0.01,
        max=10,
        marks={i: str(i) for i in range(11)},
        step=0.01,
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    Output('poisson_graph', 'figure'),
    [Input('poisson_rate', 'value'),]
)
def plot(rate):
    x = np.arange(0, 11)
    y = stats.poisson.pmf(x, rate)
    range_x = [-1, 11]
    range_y = [-0.2, 1.2]
    figure = px.scatter(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
