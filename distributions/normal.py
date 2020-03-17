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
        expression=r'''
            f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
            \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
        ''',
        displayMode=True
    ),
    dcc.Graph(id='normal_graph'),
    dash_katex.DashKatex(expression=r'\mu'),
    dcc.Slider(
        id='normal_mean',
        value=0,
        min=-5,
        max=5,
        marks={x: str(x) for x in range(-5, 6)},
        step=0.01,
        tooltip={'placement': 'top'}
    ),
    dash_katex.DashKatex(expression=r'\sigma^2'),
    dcc.Slider(
        id='normal_variance',
        value=1,
        min=0.01,
        max=10,
        marks={x: str(x) for x in range(11)},
        step=0.01,
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    Output('normal_graph', 'figure'),
    [Input('normal_mean', 'value'),
     Input('normal_variance', 'value')]
)
def plot(mean, variance):
    std = np.sqrt(variance)
    x = np.linspace(-10, 10, 1000)
    y = stats.norm.pdf(x, mean, std)
    range_x = [-10, 10]
    range_y = [-0.2, max(1.2, max(y) + 0.2)]
    figure = px.line(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
