from scipy.stats import shapiro
from scipy.stats import boxcox
from statsmodels.stats.diagnostic import lilliefors
import statsmodels.api as sm
import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats
import bootstrapped.compare_functions as bs_compare
import pylab

__author__ = 'Kirill Guliaev'

def shapiro_wilk(data):
	"""
	Perform the Shapiro-Wilk test for normality.

    The Shapiro-Wilk test tests the null hypothesis that the
    data was drawn from a normal distribution.

	Parameters
    ----------
    data : Array of sample data.

    Returns
    -------
    p-value : The p-value of the test.
    """
	stat, p_value = shapiro(data)
	return p_value

def lilliefors_kolmogorov(data):
	"""
	Test assumed normal or exponential distribution using Lilliefors’ test.

	Lilliefors’ test is a Kolmogorov-Smirnov test
	with estimated parameters.

	Parameters
    ----------
    data : Array of sample data.

    Returns
    -------
    p-value : The p-value of the test.
	"""
	stat, p_value = lilliefors(data)
	return p_value

def show_qq_plot(data):
	"""
	Show Q-Q plot of the quantiles of x versus the quantiles/ppf of a distribution.

	Parameters
    ----------
    data : One-dimension array of sample data.
	"""
	sm.qqplot(data, line='s')
	pylab.show()

def normalize_boxcox(data):
	"""
	Return a dataset transformed by a Box-Cox power transformation.

	Parameters
    ----------
    data : One-dimension array of sample data.

    Returns
    -------
    normalized_data : Box-Cox power transformed array.
	"""
	normalized_data, _ = boxcox(data)
	return normalized_data

def distribution_of_mean(data):
	"""
	Returns bootstrapped mean distribution.

	Parameters
    ----------
    data : One-dimension array of sample data.

    Returns
    -------
    bootstrapped_mean : Distribution of the mean
	"""
	bootstrapped_mean = bs.bootstrap(data, stat_func=bs_stats.mean, return_distribution = True)
	return bootstrapped_mean

def confidence_interval_of_mean(data, alpha = 0.05):
	"""
	Returns bootstrapped mean interval.

	Parameters
    ----------
    data : One-dimension array of sample data.
    alpha : The alpha value for the confidence intervals.

    Returns
    -------
    bootstraped_interval : The bootstrap confidence interval for a given distribution.
	"""
	bootstraped_interval = bs.bootstrap(data, stat_func=bs_stats.mean, alpha = alpha, return_distribution = False)
	return bootstraped_interval