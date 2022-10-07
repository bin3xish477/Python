# shopping_cart.py

from typing import List

class ShoppingCart():
    def __init__(self, max_items: int) -> None:
        self._items: List[str] = []
        self._max_items: int = max_items

    @property
    def max_items(self) -> int:
        return self._max_items

    @property
    def size(self) -> int:
        return len(self._items)

    def add(self, item) -> None:
        if self.size == self.max_items:
            raise OverflowError("can't have more than 1000 items in a cart")
        self._items.append(item)

    def clear(self):
        self._items.clear()

    def get_items(self) -> List[str]:
        return self._items

    def get_total_price(self, price_map) -> None:
        pass

