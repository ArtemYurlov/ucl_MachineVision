import numpy as np
from normal import normal

def log_normal(X, mu, sigma):
    """Return log-likelihood of data given parameters"

    Computes the log-likelihood that the data X have been generated
    from the given parameters (mu, sigma) of the one-dimensional
    normal distribution.

    Args:
        X: vector of point samples
        mu: mean
        sigma: standard deviation
    Returns:
        a scalar log-likelihood
    """
    N = len(X)
    loglik =  -(N/2)*np.log(2*np.pi) - (N/2)*np.log(sigma**2) - (1/(2*sigma**2))*(np.sum((X-mu)**2))
    return loglik
 