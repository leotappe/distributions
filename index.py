import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import config


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('Probability Distributions'),
    dcc.Dropdown(
        id='dropdown',
        options=sorted(
            [{'label': properties['name'], 'value': distribution}
            for distribution, properties in config.distributions.items()],
            key=lambda option: option['label']
        ),
        value=None,
    ),
    html.Div(id='page-content')
])


@app.callback(
    Output('url', 'pathname'),
    [Input('dropdown', 'value')]
)
def select_distribution(distribution):
    if distribution is None:
        distribution = ''
    return f'/{distribution}'


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_distribution(pathname):
    if pathname[1:] in config.distributions:
        return config.distributions[pathname[1:]]['layout']
    return []


if __name__ == '__main__':
    app.run_server(debug=True)
