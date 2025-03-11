import pytest

from models.product import Product
from models.inventory import Inventory


@pytest.fixture
def product():
    yield Product("milk", 7.0, 3)


@pytest.fixture(scope="function")
def inventory():
    return Inventory()
