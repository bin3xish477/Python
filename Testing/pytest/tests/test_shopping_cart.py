# test_shopping_cart.py

from src.shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(100)

def test_can_item_to_cart(cart) -> None:
    cart.add("apple")
    assert cart.size == 1

def test_when_item_added_cart_contains_item(cart) -> None:
    cart.add("pineapple")
    assert "pineapple" in cart.items

def test_get_items_from_cart(cart) -> None:
    cart.add("orange")
    cart.add("juice")
    assert cart.items == [ "orange", "juice" ]

def test_max_items_fail(cart) -> None:
    with pytest.raises(OverflowError):
        for i in range(101):
            cart.add(i)

def test_can_get_total_price(cart) -> None:
    cart.add("shoes")
    cart.add("milk")

    price_map = {
        "shoes": 100.0,
        "milk": 4.50
    }

    assert cart.get_total_price(price_map) == 104.50

