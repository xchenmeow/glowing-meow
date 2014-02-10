# returns

import pandas
import math
import sys

def yahoo_df_to_return_series(df, return_type='log'):
	df_adj_close = df.ix[:, 'Adj Close']
	df_adj_log_close = df_adj_close.apply(math.log)
	df_adj_log_return = df_adj_log_close.diff()
	return df_adj_log_return


if __name__ == '__main__':
	# df_file = 'C:\\Users\\benqing.shen\\Desktop\\Data\\HYG.csv'
	# return_file = 'C:\\Users\\benqing.shen\\Desktop\\Data\\HYG_returns.csv'

	df_file = sys.argv[1]
	return_file = sys.argv[2]

	df = pandas.DataFrame.from_csv(df_file)
	df_adj_log_return = yahoo_df_to_return_series(df)
	df_adj_log_return.to_csv(return_file)