import feather
import pandas as pd
import numpy as np
import statistics

# df = pd.read_feather('./black-box_results.feather')
df = pd.read_feather('./black-box_results_ECJregressor.feather')
# df = pd.read_feather('./black-box_results_PStree.feather')
# print(df)
# df.to_excel('results/ground-truth_results.xlsx')
df.to_excel('./black-box_results_ECJregressor.xlsx')

uni_values = df['dataset'].unique()

median_mean = 0

algorithms = 'TPFLR'

uni_medians = []
for val in uni_values:
    result = df[(df['dataset']==val) & (df['algorithm']==algorithms)]['r2_test']
    median_mean += np.median(result)
    uni_medians.append(np.median(result))
    if(np.median(result) < 0.5):
        print(f'{val}: {np.median(result)}')

print(f'{algorithms}: ' + '{RESULT}'.format( RESULT= median_mean / len(uni_values)) + '\t{MEDIAN}'.format( MEDIAN= statistics.median(uni_medians)) )


# Convert to a pandas Series
data_series = pd.Series(uni_medians)

# Calculate the median value
median_value = data_series.median()

# Compute the absolute difference from the median
differences = (data_series - median_value).abs()

# Get the index of the element closest to the median
closest_index = differences.idxmin()

print("Index of element closest to the median:", closest_index)