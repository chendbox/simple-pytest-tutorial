from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] =  []
        self.max_size = max_size
     


    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more item")
        self.items.append(item)
  

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
       return self.items
   

    def get_total_price(self, price_map):
        # cart = ShoppingCart(5)
        # cart.add("apple")
        # cart.add("orange")

        # price_map = {"apple": 1.0, "orange": 2.0}
        # assert cart.get_total_price(price_map) == 3.0
        # pass
        total_price = 0
        for item in self.items:
            total_price = 0
            for item in self.items:
                total_price += price_map.get(item)
            return total_price