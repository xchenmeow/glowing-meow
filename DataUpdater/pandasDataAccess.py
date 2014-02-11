import pandas.io.data as web
from pandas import Series
import datetime
import multiprocessing


def get_prices(ticker, start, end, out='', src='yahoo'):
	df = web.DataReader(ticker, src, start, end)
	
	if out == '':
		return df
	elif out == 'csv':
		df.to_csv(ticker + '.csv')


def get_all_prices(tickers, start, end, out='csv', src='yahoo'):
	jobs = []
	for ticker in tickers:
		p = multiprocessing.Process(target=get_prices, args=(ticker, start, end, out, src))
		# get_prices(ticker, start, end, out, src)
		jobs.append(p)
		p.start()


def get_all_prices_procedural(tickers, start, end, out='csv', src='yahoo'):
	jobs = []
	for ticker in tickers:
		# p = multiprocessing.Process(target=get_prices, args=(ticker, start, end, out, src))
		get_prices(ticker, start, end, out, src)
		# jobs.append(p)
		# p.start()
		# p.join()


if __name__ == '__main__':
	start = datetime.datetime(2014, 1, 1)
	end = datetime.datetime(2014, 2, 7)
	# df = get_prices('IJH', start, end)
	# print df
	# df = get_prices('IBB', start, end, out='csv')
	# print df

	symbol_list = []
	with open('symbols.csv', 'rb') as f:
		for line in f:
			symbol_list.append(line.rstrip())

	# print symbol_list[1:]
	# todo: time here
	get_all_prices_procedural(symbol_list[1:], start, end)
	# todo : time here
	# get_all_prices(symbol_list[1:], start, end)
	# todo : time here