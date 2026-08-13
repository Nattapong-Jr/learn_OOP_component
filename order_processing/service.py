from order_processing import Order

class OrderService:
    def __init__(self,product_service):
        self.product_service = product_service
        self.order = {}
        self.next_order_id = 1 

    def create_order(self,customer_id,item_quantities):
        total_amount = 0
        processed_items = {}

        for product_id,qunatity in item_quantities.items():
            product = self.product_service.get_product(product_id)
            if not product or not product.is_available(qunatity):
                print(f"ERROR: product '{product_id}' is not available or insufficient stock for quantity{qunatity}")
                return None
            total_amount += product.price * qunatity
            processed_items[product_id] = qunatity

        for product_id, qunatity in processed_items.items():
            self.product_service.update_product_stock(product_id, qunatity)

        order_id = f"ORD{self.next_order_id:03d}"
        order = Order(order_id,customer_id,processed_items,total_amount, "processed")
        self.order[order_id]
        self.next_order_id += 1
        print(f"Oder {order_id} created successfully for customer {customer_id}. Total: $ {total_amount:.2f}")
        return order 
    def get_order(self,order_id):
        return self.orders.get(order_id)