
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, prc):
        if prc < 0:
            raise ValueError("Price cannot be less than 0(zero)")
        else:
            self.__price = prc


import sys

try:
    pepsi = Product(250)
    print(pepsi.get_price())
    pepsi.set_price(56)
    print(pepsi.get_price())
    # pepsi.set_price(-10)
    # print(pepsi.get_price())
except:
    print("Exception raised.....")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
