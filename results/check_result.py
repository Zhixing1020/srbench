import feather
import pandas as pd


# df = pd.read_feather('results/ground-truth_results.feather')
df = pd.read_feather('./black-box_results_ECJregressor.feather')
# print(df)
# df.to_excel('results/ground-truth_results.xlsx')
df.to_excel('./black-box_results_ECJregressor.xlsx')