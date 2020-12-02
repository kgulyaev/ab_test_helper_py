import scipy.stats as st
import statsmodels.stats.api as sms

from math import ceil

__author__ = 'Kirill Guliaev'

def get_sample_size_for_binomial(p0, p1, power = 0.8, significance = 0.05):
    effect_size = sms.proportion_effectsize(p0, p1)
    required_n = sms.NormalIndPower().solve_power(effect_size, power=power, alpha=significance)
    return ceil(required_n)

def get_sample_size_for_continuous(mu1, mu2, standard_deviation, power = 0.8, significance = 0.05):  
    gamma = (mu1 - mu2) / standard_deviation
    z1 = norm(loc = 0, scale = 1).ppf(1 - significance / 2)
    z2 = norm(loc = 0, scale = 1).ppf(power)
    required_n = 2 * (z1 + z2) ** 2 / gamma ** 2
    return ceil(required_n)