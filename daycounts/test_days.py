import days
import datetime

print '============================'

d1 = datetime.date(2013, 2, 3)

# print days.datevec(d1)[2]

print "Test days360e -- MATLAB"

# Example 1. Use this convention to find the number of days in the month of January.
start = datetime.date(2002, 1, 1)
end = datetime.date(2002, 2, 1)
print days.days360e(start, end)

# Example 2. Use this convention to find the number of days in February during a leap year.
start = datetime.date(2000, 2, 1)
end = datetime.date(2000, 3, 1)
print days.days360e(start, end)

# Example 3. Use this convention to find the number of days in February of a non-leap year.
start = datetime.date(2002, 2, 1)
end = datetime.date(2002, 3, 1)
print days.days360e(start, end)


print "Test last day of February"
d = datetime.date(2013, 2, 28)
print days.is_last_day_of_Feb(d)
d = datetime.date(2008, 2, 28)
print days.is_last_day_of_Feb(d)

print "Test days360 wiki version"
start = datetime.date(2013, 2, 28)
end = datetime.date(2013, 2, 28)
print days.days360_wiki(start, end)
end = datetime.date(2013, 3, 28)
print days.days360_wiki(start, end)
start = datetime.date(2008, 2, 28)
end = datetime.date(2008, 3, 28)
print days.days360_wiki(start, end)
# seems to be a SIFMA ( SIA ) version.
# Neither match Excel nor MATLAB

print "Test days360 MATLAB version"
start = datetime.date(2013, 2, 28)
end = datetime.date(2013, 2, 28)
print days.days360_matlab_imp(start, end)
end = datetime.date(2013, 3, 28)
print days.days360_matlab_imp(start, end)
start = datetime.date(2008, 2, 28)
end = datetime.date(2008, 3, 28)
print days.days360_matlab_imp(start, end)

print "Test days360isda -- MATLAB"
# Example 1. Use this convention to find the number of days in the month of January.
start = datetime.date(2002, 1, 1)
end = datetime.date(2002, 2, 1)
print days.days360isda(start, end)

# Example 2. Use this convention to find the number of days in February during a leap year.
start = datetime.date(2000, 2, 1)
end = datetime.date(2000, 3, 1)
print days.days360isda(start, end)

# Example 3. Use this convention to find the number of days in February of a non-leap year.
start = datetime.date(2002, 2, 1)
end = datetime.date(2002, 3, 1)
print days.days360isda(start, end)

print "Test dateoffset"
print days.dateoffset(1, 2, 2002, 8)