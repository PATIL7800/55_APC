n = int(input("Enter how many numbers: "))

i = 1
smallest = None

while i <= n:
    num = int(input("Enter number: "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1

print("Smallest number =", smallest)