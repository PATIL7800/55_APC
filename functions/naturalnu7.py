def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
n=int(input("Enter number: "))
print("Sum=", natural_sum(n))
