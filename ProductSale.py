# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __inventory = 0

    def __init__(self, sale: Sale, inventory):
        self.__lastSale = sale
        self.__inventory = inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self
    
    def setInventory(amount):
        __inventory = amount
    
    def getInventory(self):
        return self.__inventory
    
    def removeInventory(self):
        self.__inventory = self.__inventory - 1

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  #, saleNumber: int = 1):
        Sale.__saleTimes +=1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product.removeInventory()
            

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, inventory = 10)
productTwo = Product(sale=None, inventory = 5)

print("Product one and two's inventory is", productOne.getInventory(), "and" , productTwo.getInventory(), "respectively")

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])

print("After sales numbered", productOne.getLastSale.getSaleNumber, "and" , productTwo.getLastSale.getSaleNumber)
print("Product one and two's inventory is", productOne.getInventory(), "and" , productTwo.getInventory(), "respectively")