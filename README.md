# distributions
This small [Dash](https://plot.ly/dash/open-source/) app lets you dynamically visualize the density / mass functions of various common probability distributions. Pick a distribution and play around with the parameters to see how they affect the shape of the density function.

![beta](images/beta.png)

## Usage
Make sure you have Python 3.6+ installed. First, clone and enter the repo:
```
git clone https://github.com/leotappe/distributions.git
cd distributions
```
Then, create a virtual environment and install the dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Finally, run the app:
```
python index.py
```
You can now access the app with your browser at `http://127.0.0.1:8050/`.

## Supported Probability Distributions
Currently, the app allows you to visualize the following distributions:

### Discrete
* [Bernoulli](https://en.wikipedia.org/wiki/Bernoulli_distribution)
* [Binomial](https://en.wikipedia.org/wiki/Binomial_distribution)
* [Geometric](https://en.wikipedia.org/wiki/Geometric_distribution)
* [Hypergeometric](https://en.wikipedia.org/wiki/Hypergeometric_distribution)
* [Poisson](https://en.wikipedia.org/wiki/Poisson_distribution)

### Continuous
* [Beta](https://en.wikipedia.org/wiki/Beta_distribution)
* [Exponential](https://en.wikipedia.org/wiki/Exponential_distribution)
* [Normal](https://en.wikipedia.org/wiki/Normal_distribution)
* [Uniform](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous))
