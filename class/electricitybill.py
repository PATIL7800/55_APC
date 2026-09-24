class ElectricityBill:
    def __init__(self, consumer_no, name, units):
        self.consumer_no = consumer_no
        self.name = name
        self.units = units
    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = self.units * 7
        else:
            bill = self.units * 10
        print("Consumer No:", self.consumer_no)
        print("Name:", self.name)
        print("Units:", self.units)
        print("Bill:", bill)
e = ElectricityBill(101, "Vaishnavi", 150)
e.calculate_bill()