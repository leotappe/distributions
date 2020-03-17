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
            f_X(x) = \frac{{M \choose x}{{N - M} \choose {n - x}}}{N \choose n}
        ''',
        displayMode=True
    ),
    dcc.Graph(id='hypergeometric_graph'),
    dash_katex.DashKatex(expression=r'N'),
    dcc.Slider(
        id='hypergeometric_N',
        value=20,
        min=0,
        max=50,
        marks={i: str(i) for i in range(51) if i % 10 == 0},
        tooltip={'placement': 'top'}
    ),
    dash_katex.DashKatex(expression=r'M'),
    dcc.Slider(
        id='hypergeometric_M',
        value=12,
        min=0,
        max=20,
        marks={i: str(i) for i in range(21) if i % 2 == 0},
        tooltip={'placement': 'top'}
    ),
    dash_katex.DashKatex(expression=r'n'),
    dcc.Slider(
        id='hypergeometric_n',
        value=7,
        min=0,
        max=20,
        marks={i: str(i) for i in range(21) if i % 2 == 0},
        tooltip={'placement': 'top'}
    )
])


@app.callback(
    [Output('hypergeometric_M', 'value'),
     Output('hypergeometric_M', 'max'),
     Output('hypergeometric_M', 'marks'),
     Output('hypergeometric_n', 'value'),
     Output('hypergeometric_n', 'max'),
     Output('hypergeometric_n', 'marks')], 
    [Input('hypergeometric_N', 'value')],
    [State('hypergeometric_M', 'value'),
     State('hypergeometric_n', 'value')]
)
def adjust_sliders(N, M, n):
    M, n = min(N, M), min(N, n)
    marks = {i: str(i) for i in range(N + 1) if i % math.ceil(N / 10) == 0}
    return M, N, marks, n, N, marks


@app.callback(
    Output('hypergeometric_graph', 'figure'),
    [Input('hypergeometric_M', 'value'),
     Input('hypergeometric_n', 'value')],
    [State('hypergeometric_N', 'value')]
)
def plot(M, n, N):
    x = np.arange(max(0, n - N + M), min(M, n) + 1)
    y = stats.hypergeom.pmf(x, N, M, n)
    range_x = [-1, N + 1]
    range_y = [-0.2, 1.2]
    figure = px.scatter(x=x, y=y, range_x=range_x, range_y=range_y)
    return figure
