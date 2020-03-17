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
        expression=r'f_X(x) = {n \choose x} p^x (1 - p)^{n - x}',
        displayMode=True
    ),
    dcc.Graph(id='binomial_graph'),
    dash_katex.DashKatex(expression=r'n'),
    dcc.Slider(
        id='binomial_n',
        value=10,
        min=0,
        max=50,
        marks={i: str(i) for i in range(51) if i % 10 == 0},
        tooltip={'placement': 'top'}
    ),
    dash_katex.DashKatex(expression=r'p'),
    dcc.Slider(
        id='binomial_p',
        value=0.5,
        min=0,
        max=1,
        marks={p: f'{p:.1f}' for p in [i * 0.1 for i in range(1, 11)]},
        step=0.01,
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    Output('binomial_graph', 'figure'),
    [Input('binomial_n', 'value'),
     Input('binomial_p', 'value')]
)
def plot(n, p):
    x = np.arange(0, n + 1)
    y = stats.binom.pmf(x, n, p)
    range_x = [-1, 51]
    range_y = [-0.2, 1.2]
    figure = px.scatter(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
