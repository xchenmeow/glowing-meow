
import datetime
import math
settlement = '2008-02-15'   # yyyy-mm-dd
maturity = '2016-11-15'    # yyyy-mm-dd
coupon = 0.0575
ytm = 0.0650
redemption = 100
freq = 2
basis = 1


settleTime = datetime.date(int(settlement[0:4]), int(settlement[5:7]), int(settlement[8:10]))
y1 = settleTime.year
m1 = settleTime.month
d1 = settleTime.day
matureTime = datetime.date(int(maturity[0:4]), int(maturity[5:7]), int(maturity[8:10]))
y2 = matureTime.year
m2 = matureTime.month
d2 = matureTime.day

timedelta = matureTime - settleTime
firstCPmt = datetime.date(y1,m2 - (m2-m1)/(12/freq) *(12/freq), d2)
numCPmt = (y2-firstCPmt.year)*freq + (m2-firstCPmt.month) /(12/freq)
cashFlow = [redemption + redemption*coupon/freq] +  [redemption*coupon/freq for i in range(numCPmt)]
y = [(y2-i/freq) for i in range(numCPmt)]
a = [m2 - (12/freq)*i for i in range(freq)]
m = a * (numCPmt/freq) + a[0:(numCPmt%freq)]
d = [d2 for i in range(numCPmt)]
temp = zip(y,m,d)
timeCPmt = [datetime.date(y[i],m[i],d[i]) for i in range(numCPmt)]
timeCPmt.append(firstCPmt)
if firstCPmt.month > 12/freq:
	previousCPmt = datetime.date(y1, firstCPmt.month-12/freq, firstCPmt.day)
else:
	previousCPmt = datetime.date(y1-1, firstCPmt.month-12/freq+12, firstCPmt.day)
# daycount convention 30/360
# the detail should be added: Feb,28 -> 30, Dec,31 -> 30
def daycount0(day1, day2):
	a1 = ((day2.month-1)*30 + (day2.day))/float(360)
	a2 = day2.year - day1.year - 1
	a3 = ((12-day1.month)*30 + (30 - day1.day))/float(360)
	return (a1+a2+a3)*freq

discCF = [cashFlow[i] / math.pow((1+ytm/freq),(daycount0(settleTime, timeCPmt[i]))) for i in range(numCPmt+1)]
accruedInterest = redemption*coupon/freq * daycount0(settleTime, firstCPmt)/daycount0(previousCPmt, firstCPmt)


price = sum(discCF) - accruedInterest
print price