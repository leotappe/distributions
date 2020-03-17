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
        expression=r'f_X(x) = \lambda e^{-\lambda x}',
        displayMode=True
    ),
    dcc.Graph(id='exponential_graph'),
    dash_katex.DashKatex(expression=r'\lambda'),
    dcc.Slider(
        id='exponential_rate',
        value=1,
        min=0.01,
        max=10,
        marks={i: str(i) for i in range(11)},
        step=0.01,
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    Output('exponential_graph', 'figure'),
    [Input('exponential_rate', 'value')]
)
def plot(rate):
    x = np.linspace(0.01, 10, 1000)
    y = stats.expon.pdf(x, scale=(1 / rate))
    range_x = [-1, 11]
    range_y = [-0.2, max(1.2, max(y) + 0.2)]
    figure = px.line(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
