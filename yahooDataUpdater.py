# download historical data from yahoo finance
# if there is no such file named ticker.csv(all the dot and percent are removed from the filename) in folder,
# the file will be created with the data from 2009-01-01 till today
# if such file exists, the data from the last line till now will be appended to the csv file
# all the files are saved in a folder '/Users/cr/desktop/HistoricalData'
# the tickers can be read from a csv file 'SSEtickers.csv'

import urllib
import datetime
import sys
import os


class DataUpdater(object):
    
    def __init__(self, ticker, directory):
        self.ticker = ticker
        self.directory = directory
    
    def updater(self):
        today = datetime.datetime.today()
        year = today.year
        month = today.month
        day = today.day
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)
        os.chdir(directory)
        filename = self.ticker.replace(".","").replace("%","") + ".csv"
        if os.path.isfile(filename):
            file = open(filename,'r')
            line = file.readlines()
            lastline = line[-1]
            date = lastline[0:10]
            m1 = "0" + str(int(date[5:7])-1)
            d1 = date[8:10]
            y1 = date[0:4]
            m2 = "0" + str(month-1)
            d2 = str(day)
            y2 = str(year)
            if m1 == m2 and d1 == d2 and y1 ==y2:
                print "The data is already up to date"
                return 0
            symbol = self.ticker
            urlstr = "http://ichart.yahoo.com/table.csv?s=" + symbol + \
                    "&a=" + m1 + "&b=" + d1 + "&c=" + y1 +\
                    "&d=" + m2 + "&e=" + d2 + "&f=" + y2 +\
                    "&g=d&ignore=.csv"

            f = urllib.urlopen(urlstr)
            lines = f.readlines()
            f.close()
            if lines == "<html><head><title>Yahoo! - 404 Not Found</title><style>":
                print "Error"
                return 0
            date_read = lines[1]
            month_read = "0" + str(int(date_read[5:7])-1)
            day_read = date_read[8:10]
            year_read = date_read[0:4]
            if m1 == month_read and d1 == day_read and y1 == year_read:
                print "The data is already up to date"
                return 0
            lines.pop()
            lines.reverse()
            lines.pop()
            n = len(lines)
            resultFile = open(filename,'a')
            for item in lines:
                resultFile.write(item)
        else:
            m1 = "00"
            d1 = "3"
            y1 = "2009"
            m2 = "0" + str(month-1)
            d2 = str(day)
            y2 = str(year)
            symbol = self.ticker
            urlstr = "http://ichart.yahoo.com/table.csv?s=" + symbol + \
                    "&a=" + m1 + "&b=" + d1 + "&c=" + y1 +\
                    "&d=" + m2 + "&e=" + d2 + "&f=" + y2 +\
                    "&g=d&ignore=.csv"
            # urllib.urlretrieve(urlstr, "yahoo_data.csv")
            f = urllib.urlopen(urlstr)
            lines = f.readlines()
            f.close
            lines.reverse()
            n = len(lines)
            header = lines.pop(n-1)
            resultFile = open(filename,'wb')
            resultFile.write(header)
            for item in lines:
                resultFile.write(item)

# read tickers from a csv file
file = open('SSEtickers.csv')   # change file name here
tickerList = file.readlines()
file.close()
tickerlist = [item.strip() for item in tickerList]

# or read tickers from a list
# tickerlist = ["%5EGSPC", "SPY", "%5EVIX"]

# update...
directory = '/Users/cr/desktop/HistoricalData'  # change directory path here
for ticker in tickerlist:
    foo = DataUpdater(ticker,directory)
    foo.updater()
