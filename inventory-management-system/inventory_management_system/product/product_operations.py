# product_operations.py
class ProductOperations:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.product_id] = product

    def edit_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if not product:
            raise ValueError("Product not found")
        for key, value in kwargs.items():
            setattr(product, key, value)

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product not found")

    def view_products(self):
        return self.products.values()
