from distributions import (
    bernoulli, beta, binomial, exponential, geometric, hypergeometric, normal,
    poisson, uniform
)

distributions = {
    'bernoulli': {
        'name': 'Bernoulli Distribution',
        'layout': bernoulli.layout
    },
    'beta': {
        'name': 'Beta Distribution',
        'layout': beta.layout
    },
    'biomial': {
        'name': 'Binomial Distribution',
        'layout': binomial.layout
    },
    'exponential': {
        'name': 'Exponential Distribution',
        'layout': exponential.layout
    },
    'geometric': {
        'name': 'Geometric Distribution',
        'layout': geometric.layout
    },
    'hypergeometric': {
        'name': 'Hypergeometric Distribution',
        'layout': hypergeometric.layout
    },
    'normal': {
        'name': 'Normal Distribution',
        'layout': normal.layout
    },
    'poisson': {
        'name': 'Poisson Distribution',
        'layout': poisson.layout
    },
    'uniform': {
        'name': 'Uniform Distribution',
        'layout': uniform.layout
    }
}