from returns import *
import os
import sys
import pandas as pd

if __name__ == '__main__':
	# df_file = 'IYR.csv'
	# return_file = 'IYR_returns.csv'

	df_dir = sys.argv[1]
	# return_file = sys.argv[2]

	files_in_dir = os.listdir(df_dir)

	for df_file in files_in_dir:
		if df_file[-3:] != 'csv':
			continue
		# print df_file
		symbol = df_file[:-4]
		df = pd.DataFrame.from_csv(df_dir + "\\" + df_file)
		ts = yahoo_df_to_timeseries(df)
		return_series = timeseries_level_to_return(ts)
		return_series.to_csv(df_dir + "\\" + symbol + '_returns.csv')
