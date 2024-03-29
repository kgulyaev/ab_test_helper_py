from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import fisher_exact
from scipy.stats import mannwhitneyu
from statsmodels.stats.proportion import proportions_ztest
import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats
import bootstrapped.compare_functions as bs_compare

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
	chi2_statistic, p_value, df, expected = chi2_contingency(table, correction = yates_correction)
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

def bootstrapped_mean_difference_distribution_for_binomial(data1, data2):
    """
    Return the distribution of bootstrapped mean difference for binomial metric

    Parameters
    ----------
    data1, data2 : One-dimension arrays with [0, 1] values.

    Returns
    -------
    bootstrapped_mean_difference : Distribution of the mean difference
    """
    data1['denominator'] = 1
    data2['denominator'] = 1
    bootstrapped_mean_difference = bs.bootstrap_ab(data1, data2, stat_func=bs_stats.sum, compare_func=bs_compare.difference, test_denominator = data1['denominator'], ctrl_denominator = data2['denominator'], return_distribution = True)
    return bootstrapped_mean_difference

def bootstrapped_mean_difference_interval_for_continuous(data1, data2, alpha = 0.05):
    """
    Return the difference of bootstrapped means for continuous metric

    Parameters
    ----------
    data1, data2 : One-dimension arrays with [0, 1] values.
    alpha : The alpha value for the confidence intervals.

    Returns
    -------
    bootstrapped_interval : The bootstrap confidence interval for a given distribution.
    """
    data1['denominator'] = 1
    data2['denominator'] = 1
    bootstrapped_interval = bs.bootstrap_ab(data1, data2, stat_func=bs_stats.sum, compare_func=bs_compare.difference, test_denominator = data1['denominator'], ctrl_denominator = data2['denominator'], alpha = alpha, return_distribution = False)
    return bootstrapped_interval

def bootstrapped_mean_difference_distribution_for_continuous(data1, data2):
	"""
	Return the distribution of bootstrapped mean difference for continuous metric

	Parameters
    ----------
    data1, data2 : One-dimension arrays.

    Returns
    -------
    bootstrapped_mean_difference : Distribution of the mean difference
	"""
	bootstrapped_mean_difference = bs.bootstrap_ab(data1, data2, stat_func=bs_stats.mean, compare_func=bs_compare.difference, return_distribution = True)
	return bootstrapped_mean_difference

def bootstrapped_mean_difference_interval_for_continuous(data1, data2, alpha = 0.05):
	"""
	Return the difference of bootstrapped means for continuous metric

	Parameters
    ----------
    data1, data2 : One-dimension arrays.
    alpha : The alpha value for the confidence intervals.

    Returns
    -------
    bootstrapped_interval : The bootstrap confidence interval for a given distribution.
	"""
	bootstrapped_interval = bs.bootstrap_ab(data1, data2, stat_func=bs_stats.mean, compare_func=bs_compare.difference, alpha = alpha, return_distribution = False)
	return bootstrapped_interval