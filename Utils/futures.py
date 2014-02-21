class Futures(object):
    def __init__(self, name):
        self.name = name
        self.ticker = None
        self.multiplier = None
        
class FuturesContract(Futures):
    def __init__(self, name, expiry, quote):
        super(FuturesContract, self).__init__(name)
        self.expiry = expiry
        self.quote = quote
        
class Order(object):
    def __init__(self, contract, units, price):
        self.contract = contract
        self.units = units
        self.price = price


class Account(object):
    def __init__(self, initial_value):
        self.margin_account = initial_value
        self.position = 0
        self.cost = 0
        self.pv = 0
    def MTM(self, order):
        self.order = order
        self.position += self.order.units
        self.cost += self.order.price * (self.order.units)
        self.pv = self.order.contract.quote * self.position
        self.margin_account += (self.pv - self.cost)
        print self.margin_account
        return 0



account = Account(5000)
contract1 = FuturesContract("SPX", "Jun", 500)
order1 = Order(contract1, 1, 500)
foo1 = account.MTM(order1)
contract2 = FuturesContract("SPX","Jun",490)
order2 = Order(contract2, 1, 490)
foo2 = account.MTM(order2)
contract3 = FuturesContract("SPX","Jun",510)
order3 = Order(contract3, -2, 510)
foo3 = account.MTM(order3)
