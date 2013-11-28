# the class SinaHighFreqUpdater download the historical high frequancy
# data from sina finance. 
# SinaHighFreqUpdater(ticker, startdate, directory).Updater create 
# xls files contain high freq data named with today's date
 

import urllib
import datetime
import os
import sys

class SinaHighFreqUpdater(object):
	def __init__(self, ticker, startdate, directory):
		self.ticker = ticker
		self.startdate = startdate
		self.directory = directory

	def Updater(self):

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
						resultFile = open(filename,'wb')
						resultFile.write(header)
						for item in lines:
							a = item.split('\t')
							b = ','.join(a)
							resultFile.write(b)
						resultFile.close()
					except:
						continue


# change path here
directory = '/Users/cx/Desktop/510050highfreq'
# change start date here
startdate = datetime.date(2013,10,1)
# change ticker here
ticker = 'sh510050'

foo = SinaHighFreqUpdater(ticker, startdate, directory)
foo.Updater()