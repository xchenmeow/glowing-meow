from enum import Enum

class Frequency(Enum):
	"""docstring for Frequency"""
	def __init__(self, arg):
		super(Frequency, self).__init__()
		self.arg = arg
	# Class members
	annual = 1
	semiannual = 2
	quarterly = 4
