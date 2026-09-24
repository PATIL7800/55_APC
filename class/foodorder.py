class FoodOrder:
    def __init__(self, order_id, customer_name, food, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food = food
        self.quantity = quantity
        self.price = price
    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        final_bill = total + tax
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Food:", self.food)
        print("Total Bill:", final_bill)
    def __del__(self):
        print("Order completed")
order = FoodOrder(101, "Vaishnavi", "Pizza", 2, 200)
order.total_bill()