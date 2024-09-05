import feather
import pandas as pd
import numpy as np


# df = pd.read_feather('./black-box_results.feather')
df = pd.read_feather('./black-box_results_ECJregressor.feather')
# print(df)
# df.to_excel('results/ground-truth_results.xlsx')
df.to_excel('./black-box_results_ECJregressor.xlsx')

uni_values = df['dataset'].unique()

median_mean = 0

algorithms = 'LGR'


for val in uni_values:
    result = df[(df['dataset']==val) & (df['algorithm']==algorithms)]['r2_test']
    median_mean += np.median(result)

print(f'{algorithms}: ' + '{RESULT}'.format( RESULT= median_mean / len(uni_values)) )