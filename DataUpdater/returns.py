# returns

import pandas as pd
import math
import sys
import functools

def yahoo_df_to_return_series(df, return_type='log'):
	df_adj_close = df.ix[:, 'Adj Close']
	df_adj_log_close = df_adj_close.apply(math.log)
	df_adj_log_return = df_adj_log_close.diff()
	return df_adj_log_return


def yahoo_df_to_timeseries(df, col='Adj Close'):
	'''
	yahoo df:
	Date, Open, High, Low, Close, Volume, Adj Close

	timeseries:
	Date, Value
	'''
	return df.ix[:, col]


def timeseries_transform(ts, func):
	ts.apply(func)


def timeseries_level_to_return(ts, return_type='log', drop_na=False):
	if return_type == 'log':
		return ts.apply(math.log).diff()[(1 if drop_na else 0):]
	else:
		raise NotImplementedError

def timeseries_return_to_level(ts, starting_value=1, return_type='log', pivot_date=None):
	'''
	This is ugly...
	'''
	level_ts = ts.copy()
	level_ts.iloc[0] = starting_value
	for i in xrange(1,len(level_ts)):
		if return_type == 'log':
			level_ts.iloc[i] = math.exp(ts.iloc[i]) * level_ts.iloc[i-1]
		elif return_type == 'simple':
			level_ts.iloc[i] = (ts.iloc[i] + 1) * level_ts.iloc[i-1]
	return level_ts
	


def make_printed(f):
	@functools.wraps(f)
	def wrapped(*args):
		print f(*args)
	return wrapped


# def make_csv_output(f):
	# def wrapped(*args):
		# f(*args).to_csv(filepath)
	# return wrapped



@make_printed
def yahoo_df_to_timeseries_printed(df, col='Adj Close'):
	'''
	yahoo df:
	Date, Open, High, Low, Close, Volume, Adj Close

	timeseries:
	Date, Value
	'''
	return df.ix[:, col]

# @make_csv_output
def yahoo_df_to_timeseries_csv(df, col='Adj Close'):
	'''
	yahoo df:
	Date, Open, High, Low, Close, Volume, Adj Close

	timeseries:
	Date, Value
	'''
	return df.ix[:, col]


if __name__ == '__main__':
	df_file = 'IYR.csv'
	return_file = 'IYR_returns.csv'

	# df_file = sys.argv[1]
	# return_file = sys.argv[2]

	df = pd.DataFrame.from_csv(df_file)
	# df_adj_log_return = yahoo_df_to_return_series(df)
	# df_adj_log_return.to_csv(return_file)
	# ts = yahoo_df_to_timeseries(df)
	# return_series = timeseries_level_to_return(ts)
	# print return_series.head()
	# print timeseries_return_to_level(return_series, 1000).head()

	# ts = yahoo_df_to_timeseries_printed(df)
	ts = timeseries_level_to_return(yahoo_df_to_timeseries(df))
	print type(ts)
	print ts.name
	# print ts
	ts.to_csv(return_file, header=True)
	