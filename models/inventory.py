from models.product import Product


class Inventory:
    items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def remove_product(self, product_name: str):
        product = next((p for p in self.items if p.name == product_name), None)

        if product:
            product.amount -= 1
            if product.amount < 1:
                self.items.remove(product)
        else:
            raise KeyError("Product not found")

    def get_product(self, product_name: str) -> Product:
        product = next((p for p in self.items if p.name == product_name), None)
        return product

    def total_inventory_value(self) -> float:
        return sum(i.amount * i.price for i in self.items)
