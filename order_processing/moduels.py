class Order:
    def __init__(self,order_id,customer_id,items,total_amount,status="pending"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.total_amount = total_amount
        self.status = status

    def __str__(self):
        return f"Order(ID: {self.order_id}, Customer: {self.customer_id}, Total: ${self.total_amount:.2f}, Status: {self.status})"