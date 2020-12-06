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
	stat, p_value = shapiro(data)
	return p_value

def lilliefors_kolmogorov(data):
	stat, p_value = lilliefors(data)
	return p_value

def show_qq_plot(data):
	sm.qqplot(data, line='s')
	pylab.show()

def normalize_boxcox(data):
	normalized_data, _ = boxcox(data)
	return normalized_data

def distribution_of_mean(data):
	return bs.bootstrap(data, stat_func=bs_stats.mean, return_distribution = True)

def confidence_interval_of_mean(data, alpha = 0.05):
	return bs.bootstrap(data, stat_func=bs_stats.mean, alpha = alpha, return_distribution = False)