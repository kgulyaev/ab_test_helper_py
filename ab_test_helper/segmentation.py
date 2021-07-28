import seaborn as sns

__author__ = 'Kirill Guliaev'

def show_segments_splitting(df, user_id, segment_columns_array, split_column, height = 6, aspect = 2):
    """
    Show bar chart for the different segments of the sample

    Parameters
    ----------
    df : source dataframe
    user_id : column name of user identificators
    segment_columns_array : array of columns for segmentations (e.g. country, channel)
    split_column : column that contains splitting values (e.g. control & treatment)
    height : height (in inches) of each facet.
    aspect : aspect ratio of each facet, so that aspect * height gives the width of each facet in inches.
    """
    for column in segment_columns_array:
        aggregated_data = df.groupby(by = [split_column, column])[user_id].count().reset_index()
        sns.catplot(x = column, y = 'user_id', hue = split_column, data = aggregated_data, kind = "bar", height = height, aspect = aspect)