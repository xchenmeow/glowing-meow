#convert tick data into intraday 1 minute data


import os
import csv
import datetime
import types

####
# import csv files containing tick data in a directory
# with format [time, price, -, volume, amt, -]
# the output format would be [time, open, high, low, close, volume, amt]
# change path here
dirpath = 'C:\\users\\cx\\desktop\\data510050highfreq'
if os.path.exists(dirpath+'\intraday1min') == 0:
	os.mkdir(dirpath+'\\intraday1min')
os.chdir(dirpath)
####
def datetime2matlabdn(dt):
   ord = dt.toordinal()
   mdn = dt + datetime.timedelta(days = 366)
   frac = (dt-datetime.datetime(dt.year,dt.month,dt.day,0,0,0)).seconds / (24.0 * 60.0 * 60.0)
   return mdn.toordinal()+frac


data_files = [x[2] for x in os.walk(dirpath)]
filename = data_files[0]
filename.pop()
filename.pop(-1)
for i in range(len(filename)):
	with open(filename[i],'rb') as csvfile:
		itd = csv.reader(csvfile,  delimiter=',')
		data = []
		date = filename[i][0:11]
		t = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), 9,24,30)
		openprice = 0
		highprice = 0
		lowprice = 1000
		closeprice = 0
		volume = 0
		amt = 0
		flag = 0
		for row in itd:
			temp = t
			tempcloseprice = closeprice
			if flag == 1:
				tempvolume += volume
				tempamt += amt
				if closeprice > highprice:
					highprice = closeprice
				if closeprice < lowprice:
					lowprice = closeprice
			else:
				tempvolume = volume
				tempamt = amt
				highprice = closeprice
				lowprice = closeprice
			try:
				t = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), \
					int(row[0][0:2]), int(row[0][3:5]), int(row[0][6:8]))
				if int(t.hour) == 9 and int(t.minute) == 25:
					openprice = float(row[1])
				closeprice = float(row[1])
				volume = int(row[3])*100
				amt = int(row[4])
				if str(temp.hour) == str(t.hour) and str(temp.minute) == str(t.minute):
					flag = 1
					continue
				else:
					data.append([datetime2matlabdn(temp.replace(second=0)), openprice, highprice, \
						lowprice, tempcloseprice, tempvolume, tempamt])
					flag = 0
					tempvolume = 0
					tempamt = 0
					openprice = closeprice
					highprice = closeprice
					lowprice = closeprice
			except:
				continue
		data.append([datetime2matlabdn(t.replace(second=0)), openprice, highprice, lowprice, closeprice, volume, amt])
		data.pop(0)
		dailyfilename = dirpath+'\\intraday1min\\'+filename[i]
		if os.path.isfile(dailyfilename) == 0:
			with open(dailyfilename,'wb') as dailyfile:
				wr = csv.writer(dailyfile)
				wr.writerow(['time', 'open', 'high', 'low', 'close', 'volume', 'amt'])
				for item in data:
					wr.writerow(item)


