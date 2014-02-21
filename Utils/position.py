from urllib2 import urlopen
from bs4 import BeautifulSoup

class open_position(object):
	"""Open Positions"""
	def __init__(self, symbol):
		super(open_position, self).__init__()
		self.symbol = symbol
		self.open_sub_positions = []

	def add_sub_position(self, sub_position):
		self.open_sub_positions.append(sub_position)

	def most_recent_value(self):
		return sum([p.most_recent_value() for p in self.open_sub_positions])

	def most_recent_price(self):
		# todo
		pass

	def show_lots(self):
		print self.open_sub_positions
		

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

	def dolloar_change_since_purchase(self):
		pass

	def percent_change_since_purchase(self):
		pass

	def dolloar_change_since_close(self):
		pass

	def percent_change_since_close(self):
		pass

if __name__ == '__main__':
	ibb_position0 = open_sub_position('IBB', '2/11/2014', 19, 254.43)
	print ibb_position0.most_recent_value()

	ibb_position = open_position('IBB')
	ibb_position.add_sub_position(ibb_position0)
	print ibb_position.most_recent_value()
	print ibb_position.show_lots()
