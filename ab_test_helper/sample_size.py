import statsmodels.stats.api as sms
from math import ceil

__author__ = 'Kirill Guliaev'

def get_sample_size_for_binomial(p0, p1, power = 0.8, significance = 0.05):
    effect_size = sms.proportion_effectsize(p0, p1)
    required_n = sms.NormalIndPower().solve_power(effect_size, power=power, alpha=significance)
    return ceil(required_n)