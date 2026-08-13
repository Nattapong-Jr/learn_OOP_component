from product_catalog.service import ProductService
from order_processing.service import OrderService
from user_management.modules import User

def run_application():
    print("--- starting E-commerce Application ---")

    product_svc = ProductService()
    order_svc = OrderService(product_svc)

    product_svc.display_all_products()

    customer1 = User("Cust001", "Alice Smith", "alice@example.com")
    print(f"\n--- Creating Order for {customer1.username} ---")

    order_items_1 = {"P001": 1, "P002": 2}
    print(f"\n creating Order for {customer1.username} ---")
    new_order = order_svc.create_order(customer1.user_id, order_items_1)

    if new_order:
        print(f"Order create : {new_order}")
    else:
        print("Failed to create order")

    product_svc.display_all_products()

    print("\n --- Attempting another order (insufficient stock) ---")
    order_items_fail = {"P001": 5, "P003": 1}
    failed_order = order_svc.create_order(customer1.user_id, order_items_fail)
    if not failed_order:
        print("Order attempt failed as expexted due to insufficient stock")

    product_svc.display_all_products()

    print("\n--- Application Finished --")

if __name__ == "__main__":
    run_application()