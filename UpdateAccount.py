'''
Module docstring
'''

class Order(object):
    """
    class docstring
    """
    def __init__(self, date,
    	forcastmax, forcastmin,
    	realmax, realmin,
    	openprice, closeprice):
        self.date = date
        self.forcastmax = forcastmax
        self.forcastmin = forcastmin
        self.max = realmax
        self.min = realmin
        self.openprice = openprice
        self.closeprice = closeprice

class BuyOrder(object):
    """
    class docstring
    """
    def __init__(self, date, buyprice, forcastsellprice):
        self.date = date
        self.buyprice = buyprice
        self.forcastsellprice = forcastsellprice

class Account(object):
    """
    class docstring
    """
    def __init__(self, position, costbasis, value, realized):
        self.position = position
        self.costbasis = costbasis
        self.value = value
        self.realized = realized


class UpdateAccount(object):
    """
    class docstring
    """
    def __init__(self, account, order, buyorderlist):
        self.account = account
        self.order = order
        self.buyorderlist = buyorderlist

    def buy_flag(self, maxposition):
        """
        method docstring
        """
        if self.order.forcastmin > self.order.min:
            if self.order.forcastmin < self.order.openprice \
            and self.order.forcastmax > self.order.openprice:
                if self.account.position < maxposition:
                    return 1

    def sell_flag(self, minposition):
        """
        method docstring
        """
        # this should be adjusted according to leftovers
        if self.order.forcastmax > self.order.max:
            if self.order.forcastmin < self.order.openprice \
                        and self.order.forcastmax > self.order.openprice:
                if self.account.position > minposition:
                    return 1

    def calc_position(self):
        """
        method docstring
        """
        position = self.account.position + self.buy_flag(0) - self.sell_flag(0)
        return position

    def calc_cost_basis(self):
        """
        method docstring
        """
        # averaged
        # should be FIFO? or HIFO? or averaged??
        costbasis = \
        	self.buy_flag(0) * \
        	(self.account.position * self.account.costbasis \
        	+ self.order.forcastmin) / (self.account.position + 1) \
        	+ (self.buy_flag(0) == 0) * self.account.costbasis
        return costbasis

    def calc_realized(self):
        """
        method docstring
        """
        # should be FIFO? or HIFO? or averaged??
        return self.account.realized + self.sell_flag(0) \
        	* (self.order.forcastmax - self.account.costbasis)

    def calc_value(self):
        """
        method docstring
        """
        return self.calc_position() * self.order.close

    def calc_leftover(self):
        '''
        if the buy order was not sold out, 
        when price reaches the forcastsellprice(when buying those shares),
        sell them
        this method will return the buy order's date, price
        '''
        pass

    def update_buy_order_list(self):
        """
        docstring
        """
        pass

    def update(self):
        """
        docstring
        """
        updatedaccount = Account(
        	self.calc_position(), self.calc_cost_basis(),
        	self.calc_value(), self.calc_realized())
        return updatedaccount

