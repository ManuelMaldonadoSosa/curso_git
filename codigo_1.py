from dataclasses import dataclass


@dataclass
class Product:
    name:str
    price:float
    discountPercent:int
    
    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDiscountAmount(self):
        return self.price*self.discountPercent/100
    
    def getDiscountPrice(self):
        return self.price-self.getDiscountAmount()
    
    
from figure413 import Product

product1=Product("Stanley 13",12.94,10)

#print data for product1 to console
print("PRODUCT DATA")
print(f"Name:                   {product1.name}")
print(f"Price:                  {product1.price: .2f}")
print(f"Discount percent:       {product1.discountPercent:d}%")
print(f"Discount amount:        {product1.getDiscountAmount():.2f}")
print(f"Discount price:         {product1.getDiscountPrice():.2f}")