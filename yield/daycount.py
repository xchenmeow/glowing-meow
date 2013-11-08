from enum import Enum

# DayCountConventions = Enum('30/360', 'actual/actual', 'actual/360', 'actual/365', 'euro 30/360')

class DayCountConventions(Enum):
	"""docstring for DayCountConventions"""
	def __init__(self, arg):
		super(DayCountConventions, self).__init__()
		self.arg = arg
	# Class members
	thirty360 = 0
	actualActual = 1
	actual360 = 2
	actual365 = 3
	euroThirty360 = 4

# print DayCountConventions.thirty360
# print type(DayCountConventions.thirty360)