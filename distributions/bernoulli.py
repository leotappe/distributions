import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_katex

import plotly.express as px
from scipy import stats

from app import app

layout = html.Div([
    dash_katex.DashKatex(
        expression=r'''
            f_X(x) = \begin{cases}
            1 - p, \quad &x = 0, \\
            p, \quad &x = 1
            \end{cases}
        ''',
        displayMode=True
    ),
    dcc.Graph(id='bernoulli_graph'),
    dash_katex.DashKatex(expression=r'p'),
    dcc.Slider(
        id='bernoulli_p',
        value=0.5,
        min=0,
        max=1,
        marks={p: f'{p:.1f}' for p in [i * 0.1 for i in range(1, 11)]},
        step=0.01,
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    Output('bernoulli_graph', 'figure'),
    [Input('bernoulli_p', 'value')]
)
def plot(p):
    x = [0, 1]
    y = stats.bernoulli.pmf(x, p)
    figure = px.scatter(x=x, y=y, range_x=[-0.5, 1.5], range_y=[-0.2, 1.2])
    return figure
