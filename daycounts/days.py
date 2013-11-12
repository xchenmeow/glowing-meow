import datetime

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
	'''docstring'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	if start.month == 2 and start.day == 28 and end.month == 2 and end.day == 28:
		# in this case, end.day should be set to 30...
		# but I can not set 2-30, since it is in datetime type...
		pass
	if start.month == 2 and start.day == 28:
		# so I minus 2 days manully.
		# this change may cause some mistakes when calculating coupon days...
		return (end.year - start.year) * 360 + (end.month - start.month) * 30 + (end.day - 2 - start.day)
	if (start.day == 31 or start.day == 30) and end.day == 31:
		end = datetime.date(end.year, end.month, 30)
	if start.day == 31:
		start = datetime.date(start.year, start.month, 30)
	return (end.year - start.year) * 360 + (end.month - start.month) * 30 + (end.day - start.day)
 
# print days360(t0, t1)
# print days360(t2, t3)
try:
	print days360(0, 1)
except Exception, e:
	pass

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
