from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import fisher_exact
from scipy.stats import mannwhitneyu
from statsmodels.stats.proportion import proportions_ztest

import numpy as np

__author__ = 'Kirill Guliaev'

def t_student(data1, data2):
	t_statistic, p_value = ttest_ind(data1, data2)
	return t_statistic, p_value

def z_proportions(successes_1, trials_1, successes_2, trials_2, h1='two-sided'):
	z_statistic, p_value = proportions_ztest(
		count=np.array([successes_1, successes_2]),
    	nobs=np.array([trials_1, trials_2]),
        alternative=h1)
	return z_statistic, p_value

def chi_squared(successes_1, trials_1, successes_2, trials_2, yates_correction=True):
	table = [[successes_1, successes_2], [trials_1, trials_2]]
	chi2_statistic, p_value, df, expected = chi2_contingency(table, correction=yates_correction)
	return chi2_statistic, p_value

def fisher(successes_1, trials_1, successes_2, trials_2):
	table = [[successes_1, successes_2], [trials_1, trials_2]]
	oddsratio, p_value = fisher_exact(table)
	return oddsratio, p_value

def mann_whitneyu(data1, data2):
	u_stat, p_value = mannwhitneyu(data1, data2)
	return u_stat, p_value