


class Order(object):
	def __init__(date, forcastmax, forcastmin, realmax, realmin, openprice, closeprice):
		self.date = date
		self.forcastmax = forcastmax
		self.forcastmin = forcastmin
		self.max = realmax
		self.min = realmin
		self.openprice = openprice
		self.closeprice = closeprice

class BuyOrder(object):
	def __init__(date, buyprice, forcastsellprice):
		self.date = date
		self.buyprice = buyprice
		self.forcastsellprice = forcastsellprice

class Account(object):
	def __init__(position, costbasis, value, realized):
		self.position = position
		self.costbasis = costbasis
		self.value = value
		self.realized = realized


class UpdateAccount(object):
	def __init__(account, order, buyorderlist):
		self.account = account
		self.order = order
		self.buyorderlist = buyorderlist

	def buyFlag(self, maxposition):
		if self.order.forcastmin > self.order.min:
			if self.order.forcastmin < self.order.openprice and self.order.forcastmax > self.order.openprice:
				if self.account.position < maxposition:
					return 1

	def sellFlag(self, minposition):
		# this should be adjusted according to leftovers
		if self.order.forcastmax > self.order.max:
			if self.order.forcastmin < self.order.openprice and self.order.forcastmax > self.order.openprice:
				if self.account.position > minposition:
					return 1

	def calcPosition(self):
		position = self.account.position + buyFlag() - sellFlag()
		return position

	def calcCostbasis(self):
		# averaged
		# should be FIFO? or HIFO? or averaged??
		costbasis = buyFlag()*(self.account.position*self.account.costbasis+self.order.forcastmin)\
		/(self.account.position+1) + (buyFlag()==0)*self.account.costbasis

	def calcRealized(self):
		# should be FIFO? or HIFO? or averaged??
		return self.account.realized + sellFlag() * (self.order.forcastmax - self.account.costbasis)

	def calcValue(self):
		return calcPosition() * self.order.close

	def calcLeftOver(self):
		''' if the buy order was not sold out, 
		when price reaches the forcastsellprice(when buying those shares), sell them
		this method will return the buy order's date, price'''
		pass

	def updateBuyOrderList(self):
		pass

	def update(self):
		updatedaccount = Account(calcPosition(), calcCostbasis(), calcValue(), calcRealized())
		return updatedaccount

