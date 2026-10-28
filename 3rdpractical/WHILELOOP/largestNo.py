n = int(input("How many numbers: "))

i = 1
num = int(input("Enter number: "))
largest = num

while i < n:
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

    i = i + 1

print("Largest number =", largest)