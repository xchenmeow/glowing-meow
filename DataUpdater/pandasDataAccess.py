import pandas.io.data as web

import datetime


def get_prices(ticker, start, end, out='', src='yahoo'):
	df = web.DataReader(ticker, src, start, end)
	if out == '':
		return df
	elif out == 'csv':
		df.to_csv(ticker + '.csv')

def get_all_prices(tickers, start, end, out='csv', src='yahoo'):
	for ticker in tickers:
		get_prices(ticker, start, end, out, src)


if __name__ == '__main__':
	start = datetime.datetime(2014, 1, 1)
	end = datetime.datetime(2014, 2, 7)
	df = get_prices('IJH', start, end)
	# print df
	df = get_prices('IBB', start, end, out='csv')
	print df