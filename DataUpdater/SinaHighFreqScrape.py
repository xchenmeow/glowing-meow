# the class SinaHighFreqUpdater download the historical high frequancy
# data from sina finance. 
# SinaHighFreqUpdater(ticker, startdate, directory).Updater create 
# csv files contain high freq data named with today's date
# sh510050.csv file contains daily data, include open high low close
# add a flag argument in Updater function.
# flag == 1 indicates the date in excel date format
# flag == 0 indicates the date in original format

import urllib
import datetime
import os
import sys

class SinaHighFreqUpdater(object):
	def __init__(self, ticker, startdate, directory):
		self.ticker = ticker
		self.startdate = startdate
		self.directory = directory

	def Updater(self, flag):

		try:
			os.stat(directory)
		except:
			os.mkdir(directory)
		os.chdir(directory)
		today = datetime.date.today()
		numofdate = abs(today - startdate)
		numofdate = int(numofdate.days)
		for i in range(numofdate):
			datetoday = startdate+datetime.timedelta(days=i)
			if datetoday.weekday() == 5 or datetoday.weekday() == 6:
				continue
			else:
				filename = str(datetoday)+'.csv'
				if os.path.isfile(filename):
					if i == numofdate - 1:
						print 'already up to date'
					else:
						continue
				else:
					urlstr = 'http://market.finance.sina.com.cn/downxls.php?date='+str(datetoday)+'&symbol='+ticker
					try:
						f = urllib.urlopen(urlstr)
						lines = f.readlines()
						f.close
						lines.reverse()
						if lines[0] == '</script>':
							print  'Did not trade in {}'.format(datetoday)
							continue
						n = len(lines)
						header = lines.pop(n-1)
						header = 'time,price, ,volume,turnover\n'
						resultFile = open(filename,'wb')
						resultFile.write(header)
						price = []
						for item in lines:
							a = item.split('\t')
							b = ','.join(a)
							resultFile.write(b)
							price.append(float(a[1]))
						resultFile.close()
					except:
						continue
					
					dataopen = price[0]
					dataclose = price[-1]
					datahigh = max(price)
					datalow = min(price)
					dailyfilename = ticker + '.csv'
					if os.path.isfile(dailyfilename):
						dailyfile = open(dailyfilename,'a')
					else:
						dailyfile = open(dailyfilename,'wb')
						header = 'date,open,high,low,close\n'
						dailyfile.write(header)
					if flag == 1:
						dailydate = datetoday - datetime.date(1899,12,30)
						dailytdate = dailydate.days
					elif flag == 0:
						dailytdate = datetoday
					dailyfile.write(str(dailytdate)+','+str(dataopen)+','+str(datahigh)+','+str(datalow)+','+str(dataclose)+'\n')
					dailyfile.close()


# change path here
directory = '/Users/cx/Desktop/510050highfreq'
# change start date here
startdate = datetime.date(2013,11,1)
# change ticker here
ticker = 'sh510050'

foo = SinaHighFreqUpdater(ticker, startdate, directory)
foo.Updater(1)