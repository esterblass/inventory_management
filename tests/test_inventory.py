import pytest

from models.product import Product


class TestInventory:

    @pytest.mark.parametrize("product", [Product("bread", 8.5, 10), Product("suger", 4, 2)])
    def test_add_product(self, product, inventory):
        inventory.add_product(product)
        assert product in inventory.items, f"product {product.name} not added"

    def test_remove_product(self, product, inventory):
        inventory.add_product(product)
        amount = product.amount
        inventory.remove_product(product.name)
        product = next(p for p in inventory.items if p.name == product.name)
        assert product.amount == amount - 1

    def test_total_inventory_value(self, inventory):
        inventory.items = [Product("bread", 8.5, 6), Product("milk", 5, 9), Product("sugar", 7, 3)]
        assert inventory.total_inventory_value() == 117

    def test_remove_product_from_list(self, inventory):
        product = Product("egg", 5, 1)
        inventory.add_product(product)
        inventory.remove_product("egg")
        assert product not in inventory.items, "remove failed"

    def test_remove_not_exit_product(self, inventory):
        with pytest.raises(KeyError, match="Product not found"):
            inventory.remove_product("water")
