from urllib2 import urlopen
from bs4 import BeautifulSoup

class open_position(object):
	"""Open Positions"""
	def __init__(self, symbol, quantity):
		super(open_position, self).__init__()
		self.arg = arg
		

class open_sub_position(object):
	"""position for each transaction"""
	def __init__(self, symbol, acquired_on, quantity, cost_basis):
		super(open_sub_position, self).__init__()
		self.symbol = symbol
		self.acquired_on = acquired_on
		self.quantity = quantity
		self.cost_basis = cost_basis
		
	def most_recent_price(self):
		# todo
		# how : send self.symbol to "data center" 
		# and get the most recent price.
		ibburl = 'http://www.marketwatch.com/investing/fund/' + self.symbol
		html = urlopen(ibburl).read()
		soup = BeautifulSoup(html)
		price = soup.find_all('p', class_='data bgLast')
		# 265.46
		return float(price[0].get_text())

	def most_recent_value(self):
		return self.most_recent_price() * self.quantity


if __name__ == '__main__':
	ibb_position0 = open_sub_position('IBB', '2/11/2014', 19, 254.43)
	print ibb_position0.most_recent_value()
