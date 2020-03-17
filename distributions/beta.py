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
            f_X(x) = \frac{\Gamma(a + b)}{\Gamma(a)\Gamma(b)}
            x^{a - 1}(1 - x)^{b - 1}
        ''',
        displayMode=True
    ),
    dcc.Graph(id='beta_graph'),
    dash_katex.DashKatex(expression=r'a'),
    dcc.Slider(
        id='beta_a',
        min=0.01,
        max=5,
        marks={
            x: str(x) for x in range(6)
        },
        step=0.01,
        value=2,
        tooltip={'placement': 'top'}
    ),
    dash_katex.DashKatex(expression=r'b'),
    dcc.Slider(
        id='beta_b',
        min=0.01,
        max=5,
        marks={
            x: str(x) for x in range(6)
        },
        step=0.01,
        value=2,
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    Output('beta_graph', 'figure'),
    [Input('beta_a', 'value'),
     Input('beta_b', 'value')]
)
def plot(a, b):
    x = np.linspace(0, 1, 100)
    y = stats.beta.pdf(x, a, b)
    range_x=[-0.5, 1.5]
    range_y=[-0.2, max(1.2, max(y) + 0.2)]
    figure = px.line(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
