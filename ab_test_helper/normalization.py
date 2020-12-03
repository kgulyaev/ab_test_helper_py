from scipy.stats import shapiro
from scipy.stats import boxcox
from statsmodels.stats.diagnostic import lilliefors
import statsmodels.api as sm
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