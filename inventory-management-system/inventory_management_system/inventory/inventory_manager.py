# inventory_manager.py
class InventoryManager:
    LOW_STOCK_THRESHOLD = 10

    def __init__(self, product_operations):
        self.product_operations = product_operations

    def adjust_stock(self, product_id, amount):
        product = self.product_operations.products.get(product_id)
        if not product:
            raise ValueError("Product not found")
        product.stock_quantity += amount

        if product.stock_quantity < self.LOW_STOCK_THRESHOLD:
            self.low_stock_notification(product)

    def low_stock_notification(self, product):
        print(f"Low stock alert for product {product.name}! Only {product.stock_quantity} left.")
