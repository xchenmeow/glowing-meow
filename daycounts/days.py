import datetime

t0 = datetime.date.today()
t1 = datetime.date(2014, 2, 16)

t2 = datetime.date(2008, 1, 30)
t3 = datetime.date(2008, 2, 1)

print(type(t0))
print(t0)

# print(type(t1))
print(t1)

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
	print "Aha"

print daysdiff(t0, t1)

def days360(start, end, us = True):
	'''docstring'''
	if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
		raise Exception("Can only take datetime.date objects.")
	return (end.year - start.year) * 360 + (end.month - start.month) * 30 + (end.day - start.day)

print days360(t0, t1)
print days360(t2, t3)
try:
	print days360(0, 1)
except Exception, e:
	print "Aha"

# basis is defined in another Enum. Should incorporate here.
def yearfrac(start, end, basis = 0):
	'''docstring'''
	if basis == 0:
		# 30/360
		return days360(start, end) / 360.0
	elif basis == 1:
		# Actual/actual
		# 365 or 366 ?
		return daysdiff(start, end) / 365.0
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
t4 = datetime.date(2007, 1, 1)
t5 = datetime.date(2007, 7, 30)
print yearfrac(t4, t5, 2)