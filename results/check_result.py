import feather
import pandas as pd


df = pd.read_feather('results/ground-truth_results.feather')
# print(df)
df.to_excel('results/ground-truth_results.xlsx')