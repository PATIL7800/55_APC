n = int(input("Enter how many numbers: "))
i = 1
largest = None

while i <= n:
    num = int(input("Enter number: "))
    if largest is None or num > largest:
        largest = num
    i += 1

print("Largest number =", largest)