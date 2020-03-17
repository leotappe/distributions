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
        expression=r'f_X(x) = \frac{1}{b - a}',
        displayMode=True
    ),
    dcc.Graph(id='uniform_graph'),
    dash_katex.DashKatex(expression=r'a, b'),
    dcc.RangeSlider(
        id='uniform_interval',
        min=-10,
        max=10,
        marks={
            x: str(x) for x in range(-10, 11)
        },
        step=0.01,
        value=[2, 4],
        allowCross=False,
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    Output('uniform_graph', 'figure'),
    [Input('uniform_interval', 'value')]
)
def plot(interval):
    a, b = interval
    x = np.linspace(a, b, 1000)
    y = stats.uniform.pdf(x, a, b - a)
    range_x=[-11, 11]
    range_y=[-0.2, max(1.2, max(y) + 0.2)]
    figure = px.line(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
