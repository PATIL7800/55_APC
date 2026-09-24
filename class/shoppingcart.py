class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []
        self.total = 0
    def add_product(self, name, price):
        self.products.append(name)
        self.total += price
        print(name, "added")
    def remove_product(self, name, price):
        if name in self.products:
            self.products.remove(name)
            self.total -= price
            print(name, "removed")
    def total_bill(self):
        print("Total Bill:", self.total)
    def __del__(self):
        print("Shopping cart destroyed")
cart = ShoppingCart("Vaishnavi", 101)
cart.add_product("Pen", 20)
cart.add_product("Book", 100)
cart.add_product("Bag", 500)
cart.remove_product("Pen", 20)
cart.total_bill()