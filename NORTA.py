import numpy as np
from scipy.stats.distributions import poisson
from scipy.stats import pearson
from scipy.stats import norm  

def GenerateMultivariatePoisson(p, samples, R, lmbda):
    normal_mu = np.repeat(0, p)  # Dimensions of Distribution
    normal = np.random.multivariate_normal(mean=normal_mu, cov=R, size=samples).T
    p = norm.cdf(normal)
    pois = poisson.ppf(p, lmbda)  # Inverse Poisson Distribution

    return pois

def CorrectInitialCorrel(lambda1, lambda2, r):
    samples = 500
    u = np.random.uniform(low=0, high=1, size=samples)
    maxcor = pearsonr(poisson.ppf(u, lambda1), poisson.ppf(u, lambda2))
    mincor = pearsonr(poisson.ppf(u, lambda1), poisson.ppf(1 - u, lambda2))
    a = -maxcor[0] * mincor[0] / (maxcor[0] + mincor[0])
    b = np.log((maxcor[0] + a) / a)
    c = -a
    corrected = np.log((r + a) / a) / b
    return np.NaN if corrected > 1 or corrected < -1 else corrected
#TEST Correlations
lambda1 = 5.68   # lambda set 1
lambda2 = 7.75   # lambda set 2
r = -0.02       # Desired Correlation
