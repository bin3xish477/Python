from src.shopping_cart import ShoppingCart
import pytest

cart: ShoppingCart = ShoppingCart(1000)

def test_can_item_to_cart():
    cart.add("apple")
    assert cart.size == 1

def test_when_item_added_cart_contains_item():
    cart.add("pineapple")
    assert "pineapple" in cart.get_items()

def test_get_items_from_cart():
    cart.clear()
    cart.add("orange")
    cart.add("juice")
    assert cart.get_items() == [ "orange", "juice" ]

def test_max_items_fail():
    cart.clear()
    with pytest.raises(OverflowError):
        for i in range(1001):
            cart.add(i)

