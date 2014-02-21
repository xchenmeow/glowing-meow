import pandas as pd
import numpy as np

symbols = ['^GSPC', 'AGG']

return_files = [s + '_returns.csv' for s in symbols]
# print return_files

# ts1 = pd.Series.from_csv(return_files[0])
# print ts1

tss = [pd.Series.from_csv(f) for f in return_files]

two_assets_returns_df = pd.concat(tss, axis=1, join='inner').dropna().convert_objects(convert_numeric=True)
# print two_assets_returns_df.columns
# print two_assets_returns_df.convert_objects(convert_numeric=True).dtypes
# print two_assets_returns_df
# print two_assets_returns_df.shape
# print two_assets_returns_df.index
# print two_assets_returns_df.dtypes

weights_for_asset1 = np.random.normal(0.5, 0.5/3.0, two_assets_returns_df.shape[0])
weights_for_asset2 = 1 - weights_for_asset1
# print weights_for_asset2

two_assets_weights_df = pd.DataFrame(data={0: weights_for_asset1, 1: weights_for_asset2},
	index=two_assets_returns_df.index)
# print two_assets_weights_df.dtypes
# print two_assets_weights_df
# print two_assets_returns_df.columns

result = two_assets_returns_df.mul(two_assets_weights_df).sum(axis=1)
print result
result.to_csv('returns.csv')