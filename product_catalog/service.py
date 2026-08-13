from product_catalog.moduels import Product

class ProductService:
    def __init__(self):
        self.products = {
            "P001": Product("P001", "laptop", 1200.0, 5),
            "P002": Product("P002", "Mouse", 25.0, 50),
            "P003": Product("P003", "Keyboard", 75.0, 30)

        }

    def get_product(self,product_id):
        return self,self.products.get(product_id)

    def update_product_stock(self,product_id,quantity):
        product = self.get_product(product_id)
        if product:
            return product.decrease_stock(quantity)
        return False

    def display_all_products(self):
        print("\n--- Available Product ----")
        for product in self.products.values():
            print(product)
