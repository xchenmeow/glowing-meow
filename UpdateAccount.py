import datetime


class Order(object):
	def __init__(self, date, forecastmax, forecastmin, realmax, realmin, openprice, closeprice):
		self.date = date
		self.forecastmax = forecastmax
		self.forecastmin = forecastmin
		self.max = realmax
		self.min = realmin
		self.openprice = openprice
		self.closeprice = closeprice

class BuyOrder(object):
	def __init__(self, date, buyprice, forecastsellprice):
		self.date = date
		self.buyprice = buyprice
		self.forecastsellprice = forecastsellprice

class SellOrder(object):
	def __init__(self, date, sellprice, forecastbuyprice):
		self.date = date
		self.sellprice = sellprice
		self.forecastbuyprice = forecastbuyprice

class Account(object):
	def __init__(self, position, costbasis, value, realized):
		self.position = position
		self.costbasis = costbasis
		self.value = value
		self.realized = realized


class UpdateAccount(object):
	def __init__(self, account, order, buyorderlist, sellorderlist):
		self.account = account
		self.order = order
		self.buyorderlist = buyorderlist
		self.sellorderlist = sellorderlist

	def buyFlag(self, maxposition):
		if self.order.forecastmin > self.order.min:
			if self.order.forecastmin < self.order.openprice and self.order.forecastmax > self.order.openprice:
				if self.account.position < maxposition:
					newbuyorder = BuyOrder(self.order.date, self.order.forecastmin, self.order.forecastmax)
					self.buyorderlist.append(newbuyorder)
					self.account.costbasis = self.calcCostbasis(self.account.costbasis, self.account.position, 1, self.order.forecastmin, 0, 0)
					self.account.position += 1
					return 1

	def sellFlag(self, minposition):
		if self.order.forecastmax < self.order.max:
			if self.order.forecastmin < self.order.openprice and self.order.forecastmax > self.order.openprice:
				if self.account.position > minposition:
					newsellorder = SellOrder(self.order.date, self.order.forecastmax, self.order.forecastmin)
					self.sellorderlist.append(newsellorder)
					self.account.costbasis = self.calcCostbasis(self.account.costbasis, self.account.position, 0, 0, 1, self.order.forecastmax)
					self.account.position -= 1
					self.account.realized += (self.order.forecastmin - self.buyorderlist[0].buyprice)
					return 1


	def buyflagleft(self, maxposition):
		for i in range(len(sellorderlist)):
			if self.account.position <= maxposition:
				if sellorderlist[i].forecastbuyprice > self.order.min and sellorderlist[i].forecastbuyprice < self.order.max:
					self.account.costbasis = self.calcCostbasis(self.account.costbasis, self.account.position, 1, sellorderlist[i].forecastbuyprice, 0, 0)
					self.sellorderlist.remove(sellorderlist[i])
					self.account.position += 1
					return 1
		
	def sellflagleft(self, minposition):
		for i in range(len(buyorderlist)):
			if self.account.position >= minposition:
				if buyorderlist[i].forecastsellprice > self.order.min and buyorderlist[i].forecastsellprice < self.order.max:					
					self.account.costbasis = self.calcCostbasis(self.account.costbasis, self.account.position, 0, 0, 1, buyorderlist[i].forecastsellprice)
					self.account.position -= 1
					self.account.realized += (self.buyorderlist[i].forcastsellprice - self.buyorderlist[0].buyprice)
					buyorderlist.remove(buyorderlist[i])
					return 1


	# def calcPosition(self):
	# 	position = self.account.position + buyFlag() - sellFlag()
	# 	return position

	def calcCostbasis(self, oldcostbasis, oldposition, buyind, buyprice, sellind, sellprice):
		# averaged
		costbasis = (oldcostbasis*oldposition + buyind*buyprice-sellind*sellprice) / (oldposition+buyind-sellind)
		return costbasis

	# def calcRealized(self):
	# 	# should be FIFO? or HIFO? or averaged??
	# 	return self.account.realized + sellFlag() * (self.order.forecastmax - self.account.costbasis)

	def calcValue(self):
		return self.account.position * self.order.closeprice

	def update(self):
		self.buyFlag(5)
		self.sellFlag(2)
		self.buyflagleft(5)
		self.sellflagleft(2)
		updatedaccount = Account(self.account.position, self.account.costbasis, self.calcValue(), self.account.realized)
		return updatedaccount


myaccount = Account(2, 1.61, 3.22, 0)
buyorderlist = [BuyOrder(datetime.date(2012,1,4), 1.61, 1.81), BuyOrder(datetime.date(2012,1,4), 1.61, 1.81)]
sellorderlist = []
order = Order(datetime.date(2012,1,5), 1.85, 1.45, 1.75, 1.4, 1.65, 1.7)
foo = UpdateAccount(myaccount, order, buyorderlist, sellorderlist)
newaccount = foo.update()
print newaccount.position
print newaccount.costbasis
print newaccount.realized
print newaccount.value
