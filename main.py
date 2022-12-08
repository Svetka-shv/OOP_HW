class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} price is {self.price}$"

    def __eq__(self, other):
        return (self.name, self.price) == (other.name, other.price)

    def str(self) -> str:
        return self.name

    def float(self) -> float:
        return self.price

    def get_total(self, quantity: int):
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.quantity = []

    def add_product(self, product: Product, quantity):
        if product in self.products:
            idx = self.products.index(product)
            self.quantity[idx] += quantity
        else:
            self.products.append(product)
            self.quantity.append(quantity)

    def __add__(self, other):
        cart = ShoppingCart()
        cart.products = self.products.copy()
        cart.quantity = self.quantity.copy()
        if isinstance(other, Product):
            cart.add_product(other, 1)
        if isinstance(other, ShoppingCart):
            for product, quantity in zip(other.products, other.quantity):
                cart.add_product(product, quantity)
        return cart

    def get_total(self):
        total = 0
        for product, quantity in zip(self.products, self.quantity):
            total += product.get_total(quantity)
        return total

    def lh(self):
        zipper = list(zip(self.products, self.quantity))
        return zipper

    def float(self) -> float:
        return self.get_total()

apple = Product("Apple", 10.59)
apple2 = Product("Apple", 10.59)
banana = Product("Banana", 60.25)
orange = Product("Orange", 50.50)
tomato = Product("Tomato", 40)
print(apple == tomato)
print(apple == apple2)

cart = ShoppingCart()
cart.add_product(apple, 0.42)
cart.add_product(apple2, 2)
cart.add_product(orange, 4)

cart2 = ShoppingCart()
cart2.add_product(banana, 3)
cart2.add_product(orange, 10)
cart2.add_product(tomato, 8)

cart3 = cart + cart2
print(cart.lh())
print(cart2.lh())
print(cart3.lh())
print(cart3.get_total())