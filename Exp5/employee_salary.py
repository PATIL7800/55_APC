salary = [25000, 35000, 52000, 60000, 28000, 75000, 45000]

avg = sum(salary) / len(salary)

print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", avg)
print("Above 50000:", sum(x > 50000 for x in salary))
print("Below 30000:", sum(x < 30000 for x in salary))