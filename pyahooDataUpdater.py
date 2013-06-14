# download historical data from yahoo finance
# if there is no file named ticker.csv in folder, the file will be created with the data from 2013-01-01 till today
# if such file exists, the data from the last line till now will be appended to the csv file

import urllib
import datetime
import sys
import os


class DataUpdater(object):
    
    def __init__(self, ticker):
        self.ticker = ticker
    
    def updater(self):
        today = datetime.datetime.today()
        year = today.year
        month = today.month
        day = today.day
        filename = self.ticker + ".csv"
        if os.path.isfile(filename):
            file = open(filename,'r')
            line = file.readlines()
            lastline = line[-1]
            date = lastline[0:10]
            # m1 = "0" + str(month-1)
            # d1 = str(day-3)
            # y1 = str(year)
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
                # sys.exit(0)
                return 0
            date_read = lines[1]
            month_read = "0" + str(int(date_read[5:7])-1)
            day_read = date_read[8:10]
            year_read = date_read[0:4]
            if m1 == month_read and d1 == day_read and y1 == year_read:
                print "The data is already up to date"
                # sys.exit(0)
                return 0
            resultFile = open(filename,'a')
            resultFile.write(lines[1])
        else:
            m1 = "00"
            d1 = "3"
            y1 = "2000"
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


tickerList = ["%5EGSPC", "SPY", "%5EVIX"]
for ticker in tickerList:
    foo = DataUpdater(ticker)
    foo.updater()
