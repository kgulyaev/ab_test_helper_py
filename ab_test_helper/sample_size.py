import scipy.stats as st
import statsmodels.stats.api as sms

from math import ceil

__author__ = 'Kirill Guliaev'

def get_sample_size_for_binomial(p0, p1, power = 0.8, significance = 0.05):
    """
    Calculate the sample size for the binomial distribution

    Parameters
    ----------
    p0 : [0, 1] current proportion value
    p1 : [0, 1] expected proportion value
    power : power of the test, e.g. 0.8,
    is one minus the probability of a type II error. 
    Power is the probability that the test correctly
    rejects the Null Hypothesis if the Alternative Hypothesis is true.
    significance : significance level, e.g. 0.05, is the probability
    of a type I error, that is wrong rejections
    if the Null Hypothesis is true.

    Returns
    -------
    required_n : Number of observations per sample.
    """
    effect_size = sms.proportion_effectsize(p0, p1)
    required_n = sms.NormalIndPower().solve_power(effect_size, power=power, alpha=significance)
    return ceil(required_n)

def get_sample_size_for_continuous(mu1, mu2, standard_deviation, power = 0.8, significance = 0.05):
    """
    Calculate the sample size for the continuous distribution

    Parameters
    ----------
    mu1 : current mean value
    mu2 : expected mean value
    standard_deviation : standard deviation of the mean
    power : power of the test, e.g. 0.8,
    is one minus the probability of a type II error. 
    Power is the probability that the test correctly
    rejects the Null Hypothesis if the Alternative Hypothesis is true.
    significance : significance level, e.g. 0.05, is the probability
    of a type I error, that is wrong rejections
    if the Null Hypothesis is true.

    Returns
    -------
    required_n : Number of observations per sample.
    """
    gamma = (mu1 - mu2) / standard_deviation
    z1 = st.norm(loc = 0, scale = 1).ppf(1 - significance / 2)
    z2 = st.norm(loc = 0, scale = 1).ppf(power)
    required_n = 2 * (z1 + z2) ** 2 / gamma ** 2
    return ceil(required_n)