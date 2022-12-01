class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def product_show(self):
        return f"{self.name} price is {self.price}$"

    def all_price(self, quantity: int):
        return self.price * quantity

class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.quantity = []

    def add_product(self, product: Product, quantity):
        self.products.append(product)
        self.quantity.append(quantity)


    def get_total(self):
        total = 0
        for (i) in range(0, len(self.products)):
            total += self.products[i].all_price(self.quantity[i])
        return total

banana = Product("Banana", 10)
orange = Product("Orange", 5)
# print(banana.product_show())
# print(banana.all_price())
# print(orange.product_show())
# print(orange.all_price())
cart = ShoppingCart()
cart.add_product(banana, 2)
cart.add_product(orange, 10)
print(cart.get_total())