def header_message(func):
    def wapper_in(self, *args, **kwargs):
        print("你所选取的套餐，请确认...")
        u = func(self, *args, **kwargs)
        return u
    return wapper_in


class Food(object):
    name = ""
    price = 0.0

    def __init__(self):
        pass

class Burger(Food):
    """
    汉堡
    """
    type='BURGER'
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price = price
    def getName(self):
        return self.name

class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price=10.0

class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price=15.0

class Snack(Food):
    """
    小食类
    """
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0

class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

class Beverage(Food):
    """
    饮料
    """
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0

class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


# 订单类(套餐)
class order():
    burger=""
    snack=""
    beverage=""

    def __init__(self,orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    @header_message
    def show(self):
        print("Burger: %s" % self.burger.getName())
        print("Snack: %s" % self.snack.getName())
        print("Beverage: %s" % self.beverage.getName())


class orderBuilder():
    bBurger=""
    bSnack=""
    bBeverage=""

    def addBurger(self, xBurger):
        self.bBurger = xBurger
        
    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return order(self)


if  __name__=="__main__":
    order_builder = orderBuilder()
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())
    _order=order_builder.build()
    _order.show()