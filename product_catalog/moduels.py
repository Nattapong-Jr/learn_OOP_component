class Product:
    def __init__(self,product_id,name,price,stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
         return f"Product(ID:{self.product_id}, Name:{self.name}, Price:{self.price}, Stock:{self.stock})"

    def is_available(self, quantity):
            return self.stock >= quantity
    
    def decrease_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False