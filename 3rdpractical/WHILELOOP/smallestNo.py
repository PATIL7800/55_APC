n = int(input("How many numbers: "))

i = 1
num = int(input("Enter number: "))
smallest = num

while i < n:
    num = int(input("Enter number: "))

    if num < smallest:
        smallest = num

    i = i + 1

print("Smallest number =", smallest)