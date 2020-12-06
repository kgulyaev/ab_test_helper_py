from scipy.stats import chi2_contingency
import seaborn as sns

__author__ = 'Kirill Guliaev'

def show_segments_splitting(df, user_id, segment_columns_array, split_column):
    for column in segment_columns_array:
        aggregated_data = df.groupby(by = [split_column, column])[user_id].count().reset_index()
        sns.catplot(x = column, y = 'user_id', hue = split_column, data = aggregated_data, kind = "bar")

def chi_squared_segments(segment1_count, segment2_count):
	chi2_statistic, p_value, df, expected = chi2_contingency([segment1_count, segment2_count])
	return p_value