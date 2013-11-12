import datetime
import calendar

t0 = datetime.date.today()
t1 = datetime.date(2014, 2, 16)

t2 = datetime.date(2008, 1, 30)
t3 = datetime.date(2008, 2, 1)

# print(type(t0))
# print(t0)

# print(type(t1))
# print(t1)

# t01 = t1 - t0

# print(type(t01))
# print(t01.days)

def datevec(date):
	'''Date components.'''
	return [date.year, date.month, date.day]

def is_last_day_of_Feb(d):
	'''docstring'''
	if not isinstance(d, datetime.date):
		raise Exception("Can only take datetime.date object.")
	return calendar.monthrange(d.year, d.month)[1] == d.day	

def daysact(start, end):
	'''Actual number of days between serial date numbers.'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	return (end - start).days

def days360_matlab(start, end):
	'''Days between dates based on a 360 day year. (SIA compliant)'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	return (end - start).days

def days360e(start, end):
	'''
	Days between dates based on a 360 day year. (European)
	Ref. MATLAB
	'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	if start.day == 31:
		start.day = 30
	if end.day == 31:
		end.day = 30
	return 360 * (end.year - start.year) + 30 * (end.month - start.month) + (end.day - start.day)

def days360isda(start, end):
	'''
	Days between dates based on a 360 day year. (ISDA compliant)
	Ref. MATLAB
	'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	# if date == 31 in first argument change it to date == 30 in first argument
	if start.day == 31:
		start.day = 30
	# if date == 31 in second argument and date == 30 in first, change date == 30 in second argument
	if end.day == 31 and start.day == 30:
		end.day = 30
	return 360 * (end.year - start.year) + 30 * (end.month - start.month) + (end.day - start.day)

def daysdiff(start, end):
	'''docstring'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	return (end - start).days

try:
	print daysdiff(0, 1)
except Exception, e:
	pass

# print daysdiff(t0, t1)

def days360(start, end, us = True):
	'''Modified Meow'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	start_ymd = datevec(start)
	end_ymd = datevec(end)
	# If both date A and B fall on the last day of February, then date B will be changed to the 30th.
	if is_last_day_of_Feb(start) and is_last_day_of_Feb(end):
		end_ymd[2] = 30
	if start.month == 2 and start.day == 28:
		# so I minus 2 days manully.
		# this change may cause some mistakes when calculating coupon days...
		return (end.year - start.year) * 360 + (end.month - start.month) * 30 + (end.day - 2 - start.day)
	if (start.day == 31 or start.day == 30) and end.day == 31:
		end = datetime.date(end.year, end.month, 30)
	if start.day == 31:
		start = datetime.date(start.year, start.month, 30)
	return (end_ymd[0] - start_ymd[0]) * 360 + (end_ymd[1] - start_ymd[1]) * 30 + (end_ymd[2] - start_ymd[2])

def days360_wiki(start, end, us = True):
	'''http://en.wikipedia.org/wiki/360-day_calendar'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	start_ymd = datevec(start)
	end_ymd = datevec(end)
	# If both date A and B fall on the last day of February, then date B will be changed to the 30th.
	if is_last_day_of_Feb(start) and is_last_day_of_Feb(end):
		end_ymd[2] = 30
	# If date A falls on the 31st of a month or last day of February, then date A will be changed to the 30th.
	if start.day == 31 or is_last_day_of_Feb(start):
		start_ymd[2] = 30
	# If date A falls on the 30th of a month after applying (2) above and date B falls on the 31st of a month,
	# then date B will be changed to the 30th.
	if start_ymd[2] == 30 and end.day == 31:
		end_ymd[2] = 30
	return (end_ymd[0] - start_ymd[0]) * 360 + (end_ymd[1] - start_ymd[1]) * 30 + (end_ymd[2] - start_ymd[2])

def days360_matlab_imp(start, end):
	'''MATLAB's implementation'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	start_ymd = datevec(start)
	end_ymd = datevec(end)
	# If both date A and B fall on the last day of February, then date B will be changed to the 30th.
	if is_last_day_of_Feb(start) and is_last_day_of_Feb(end):
		# print 'Both end of February'
		end_ymd[2] = 30
	# if month == 2 and date ==28|29 in first argument
	if is_last_day_of_Feb(start):
		start_ymd[2] = 30
	# if date == 31 in second argument and date == 30 | 31 in first, 
	if end_ymd[2] == 31 and (start_ymd[2] == 30 or start_ymd[2] == 31):
		end_ymd[2] = 30
	# if date == 31 in first argument change it to date == 30 in first argument
	if start_ymd[2] == 31:
		start_ymd[2] = 30
	return (end_ymd[0] - start_ymd[0]) * 360 + (end_ymd[1] - start_ymd[1]) * 30 + (end_ymd[2] - start_ymd[2])
 
t6 = datetime.date(2013, 1, 20)
t7 = datetime.date(2013, 2, 5)
t8 = datetime.date(2013, 3, 15)
t9 = datetime.date(2014, 3, 15)
t10 = datetime.date(2013, 2, 28)
t11 = datetime.date(2013, 3, 1)
print daysdiff(t10, t11)
print days360(t10, t11)

# basis is defined in another Enum. Should incorporate here.
def yearfrac(start, end, basis = 0):
	'''docstring'''
	if basis == 0:
		# 30/360
		return days360(start, end) / 360.0
	elif basis == 1:
		# Actual/actual
		if daysdiff(datetime.date(start.year + 1 , 1, 1), end) <= 0:
			return daysdiff(start, end) / 365.0
		else:
			part1 = float(daysdiff(start, datetime.date(start.year+1,1,1)))/daysdiff(datetime.date(start.year,1,1),datetime.date(start.year+1,1,1))
			part2 = end.year - start.year - 1
			part3 = float(daysdiff(datetime.date(end.year, 1, 1), end))/daysdiff(datetime.date(end.year,1,1),datetime.date(end.year+1,1,1))
			return part1 + part2 + part3
	elif basis == 2:
		# Actual/360
		return daysdiff(start, end) / 360.0
	elif basis == 3:
		# Actual/365
		return daysdiff(start, end) / 365.0
	elif basis == 4:
		# Euro 30/360
		# Not implemented
		pass
	else:
		raise Exception('basis not recognized.')

# Test yearfrac
t4 = datetime.date(2008, 5, 31)
t5 = datetime.date(2010, 3, 31)
print yearfrac(t4, t5, 1)

def dateoffset(refday, refmonth, refyear, monthoffset, rule = 0):
	'''
	Date offset from a reference date by a number of months.
	Ref. MATLAB
	'''
	# Negative month offsets correspond to dates in the past; 
	# positive month offsets correspond to dates in the future.
	
	coupon_month = (refmonth + monthoffset - 1) % 12
	coupon_month = (coupon_month + 12) % 12 + 1

	coupon_year = refyear + (refmonth + monthoffset - 1) / 12

	coupon_day = refday
	# todo: adjust coupon_day
	# Find all cases for which the reference day is on or after the 28th.
	return [coupon_day, coupon_month, coupon_year]

def coupncd():
	'''
	Returns a number that represents the next coupon date after the settlement date.
	Ref. Excel
	'''
	pass

def cpndaten(settlement, marurity):
	'''
	Next coupon date for fixed-income security
	Ref. MATLAB
	'''
	pass