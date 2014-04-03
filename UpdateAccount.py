import datetime


class Order(object):
	'''data structure includes date, open, high, low, close and forecasthigh, forecastlow'''
	def __init__(self, date, forecastmax, forecastmin, realmax, realmin, openprice, closeprice):
		self.date = date
		self.forecastmax = forecastmax
		self.forecastmin = forecastmin
		self.max = realmax
		self.min = realmin
		self.openprice = openprice
		self.closeprice = closeprice

class BuyOrder(object):
	'''data structure stores the info when shares reaching the forecastbuyprice and waiting to be sold'''
	def __init__(self, date, buyprice, forecastsellprice):
		self.date = date
		self.buyprice = buyprice
		self.forecastsellprice = forecastsellprice

class SellOrder(object):
	'''data structure stores the info when shares reaching the forecastsellprice and waiting to be bought'''
	def __init__(self, date, sellprice, forecastbuyprice):
		self.date = date
		self.sellprice = sellprice
		self.forecastbuyprice = forecastbuyprice

class AccountOrder(object):
	'''data structure holds the order in the account'''
	def __init__(self, date, buyprice):
		self.date = date
		self.buyprice = buyprice

class Account(object):
	'''data structure stores the account info'''
	def __init__(self, position, costbasis, value, cash, totalvalue):
		self.position = position
		self.costbasis = costbasis
		self.value = value
		self.cash = cash
		self.totalvalue = totalvalue


class UpdateAccount(object):
	'''this class includes methods to update the account info based on the forecasthigh and forecastlow'''
	def __init__(self, account, order, buyorderlist, sellorderlist, accountorderlist):
		self.account = account
		self.order = order
		self.buyorderlist = buyorderlist
		self.sellorderlist = sellorderlist
		self.accountorderlist = accountorderlist

	def buyFlag(self, maxposition):
		'''if reaching the condition of buying(forecast)'''
		if self.order.forecastmin > self.order.min:
			if self.order.forecastmin < self.order.openprice and self.order.forecastmax > self.order.openprice:
				if self.account.position < maxposition:
					newbuyorder = BuyOrder(self.order.date, self.order.forecastmin, self.order.forecastmax)
					newaccountorder = AccountOrder(self.order.date, self.order.forecastmin)
					self.buyorderlist.append(newbuyorder)
					self.accountorderlist.append(newaccountorder)
					self.account.cash -= self.order.forecastmin
					self.account.position += 1
					return 1
		return 0

	def sellFlag(self, minposition):
		'''if reaching the condition of selling(forecast)'''
		if self.order.forecastmax < self.order.max:
			if self.order.forecastmin < self.order.openprice and self.order.forecastmax > self.order.openprice:
				if self.account.position > minposition:
					newsellorder = SellOrder(self.order.date, self.order.forecastmax, self.order.forecastmin)
					self.sellorderlist.append(newsellorder)
					sell = self.accountorderlist.pop(0)
					self.account.position -= 1
					self.account.cash += sell.buyprice
					return 1
		return 0


	def buyflagleft(self, maxposition):
		'''if reaching the condition of buying the shares sold before'''
		buyleft = [item for item in self.sellorderlist if item.forecastbuyprice > self.order.min and item.forecastbuyprice < self.order.max]
		for i in range(len(buyleft)):
			if self.account.position <= maxposition:
				self.sellorderlist.remove(buyleft[i])
				newaccountorder = AccountOrder(self.order.date, buyleft[i].forecastbuyprice)
				self.accountorderlist.append(newaccountorder)
				self.account.cash -= newaccountorder.buyprice
				self.account.position += 1
				return 1
		return 0
		
	def sellflagleft(self, minposition):
		'''if reaching the condition of selling the shares bought before'''
		sellleft = [item for item in self.buyorderlist if item.forecastsellprice > self.order.min and item.forecastsellprice < self.order.max]
		for i in range(len(sellleft)):
			if self.account.position >= minposition:					
				self.account.position -= 1
				sell = self.accountorderlist.pop(0)
				self.account.cash += sellleft[i].forecastsellprice
				buyorderlist.remove(sellleft[i])
				return 1
		return 0

	# to be added: a method decides the maxposition and minposition based on a technical indicator


	def calcValue(self):
		return self.account.position * self.order.closeprice

	def update(self):
		'''updating the account info'''
		# the maxposition and min position should be decided by a technical indicator
		buyflag = self.buyFlag(5) # if forecast buy price reached first
		if not buyflag:
			self.sellFlag(2)
		# should add an ind to see forecast buy price come first or the forecast sell price
		# then self.sellFlag(2) could be executed first
		self.buyflagleft(5)
		self.sellflagleft(2)
		orderlist = [a.buyprice for a in self.accountorderlist]
		self.account.costbasis = sum(orderlist) / float(len(orderlist))
		totalvalue = self.account.cash + self.calcValue()
		updatedaccount = Account(self.account.position, self.account.costbasis, self.calcValue(), self.account.cash, totalvalue)
		return updatedaccount


myaccount = Account(2, 1.61, 3.22, 6.78, 10)
buyorderlist = [BuyOrder(datetime.date(2012,1,4), 1.61, 1.73), BuyOrder(datetime.date(2012,1,4), 1.61, 1.70)]
accountorderlist = [AccountOrder(datetime.date(2012,1,4), 1.61), AccountOrder(datetime.date(2012,1,4), 1.61)]
sellorderlist = []
order = Order(datetime.date(2012,1,5), 1.81, 1.60, 1.80, 1.55, 1.65, 1.7)
foo = UpdateAccount(myaccount, order, buyorderlist, sellorderlist, accountorderlist)
newaccount = foo.update()
print newaccount.position
print newaccount.costbasis
print newaccount.cash
print newaccount.value 
print newaccount.totalvalue
