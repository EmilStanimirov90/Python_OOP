class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name: str):
        current_capacity = 0
        for k, v in self.items.items():
            current_capacity += v
        if item_name not in self.items.keys():
            self.items[item_name] = 0
        if self.capacity > current_capacity:
            self.items[item_name] += 1
            self.capacity -= 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name, amount: int):
        if item_name in self.items:
            if amount <= self.items[item_name]:
                self.items[item_name] -= amount
                self.capacity += amount
            if self.items[item_name] == 0:
                self.items.pop(item_name)
                return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


#test code:
fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)