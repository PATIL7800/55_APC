def total_bill(prices, quantities, discount):
    total = 0
    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]
    discount_amount = total * discount / 100
    final_bill = total - discount_amount
    return final_bill
prices = [100, 200, 300]
quantities = [2, 1, 3]
discount = 10
print("Total Bill =", total_bill(prices, quantities, discount))
