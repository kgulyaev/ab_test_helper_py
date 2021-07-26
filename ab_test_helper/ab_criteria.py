from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import fisher_exact
from scipy.stats import mannwhitneyu
from statsmodels.stats.proportion import proportions_ztest

import numpy as np

__author__ = 'Kirill Guliaev'

def t_student(data1, data2):
	"""
    Calculate the T-test for the means of *two independent* samples of scores.

    This is a two-sided test for the null hypothesis that 2 independent samples
    have identical average (expected) values. This test assumes that the
    populations have identical variances by default.

    Parameters
    ----------
    data1, data2 : One-dimension arrays.

    Returns
    -------
    p_value : The p-value of the test.
    """
	t_statistic, p_value = ttest_ind(data1, data2)
	return p_value

def z_proportions(successes_1, trials_1, successes_2, trials_2, h1='two-sided'):
	"""
    Test for proportions based on normal (z) test

    Parameters
    ----------
    successes_1, successes_2 : Number of successes of two independent samples.
    trials_1, trials_1 : Number of trials or observations of two independent samples.
    h1 : str in ['two-sided', 'smaller', 'larger']
        In the two sample test, smaller means that
        the alternative hypothesis is ``p1 < p2`` and
        larger means ``p1 > p2`` where ``p1`` is the proportion of the first
        sample and ``p2`` of the second one.

    Returns
    -------
    p_value : The p-value for the test.
    """
	z_statistic, p_value = proportions_ztest(
		count=np.array([successes_1, successes_2]),
    	nobs=np.array([trials_1, trials_2]),
        alternative=h1)
	return p_value

def chi_squared(successes_1, trials_1, successes_2, trials_2, yates_correction=True):
	"""
	Chi-square test of independence of variables in a contingency table.

	Parameters
    ----------
    successes_1, successes_2 : Number of successes of two independent samples.
    trials_1, trials_1 : Number of trials or observations of two independent samples.
    yates_correction : optional
        Due to the differences in the data
        (the chi-square distribution is continuous, 
        and the frequencies of the binary exponents are discrete)
        at low frequencies (less than 10), 
        it is necessary to add the Yates correction.

    Returns
    -------
    p_value : The p-value of the test.
	"""
	table = [[successes_1, successes_2], [trials_1, trials_2]]
	chi2_statistic, p_value, df, expected = chi2_contingency(table, correction=yates_correction)
	return p_value

def fisher(successes_1, trials_1, successes_2, trials_2):
	"""
	Perform a Fisher exact test on a 2x2 contingency table.

    Parameters
    ----------
    successes_1, successes_2 : Number of successes of two independent samples.
    trials_1, trials_1 : Number of trials or observations of two independent samples.

    Returns
    -------
    p_value : The p-value of the test.
    """
	table = [[successes_1, successes_2], [trials_1, trials_2]]
	oddsratio, p_value = fisher_exact(table)
	return p_value

def mann_whitneyu(data1, data2):
	"""
	Perform the Mann-Whitney U rank test on two independent samples.

	Parameters
    ----------
    data1, data2 : One-dimension arrays.

    Returns
    -------
    p_value : The p-value of the test.
	"""
	u_stat, p_value = mannwhitneyu(data1, data2)
	return p_value