class Vehicle:
    def __init__(self, number, model, rate):
        self.number = number
        self.model = model
        self.rate = rate
        self.available = True
    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")
    def return_vehicle(self, days):
        self.available = True
        charge = self.rate * days
        print("Vehicle returned")
        print("Rental Charge:", charge)
v = Vehicle("MH09AB1234", "Swift", 1000)
v.rent()
v.return_vehicle(3)