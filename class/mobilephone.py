class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)
    def discount(self):
        discount = self.price * 0.10
        final_price = self.price - discount
        print("Price after discount:", final_price)
m = MobilePhone("Motorola", "Edge 50", "256GB", 30000)
m.display()
m.discount()