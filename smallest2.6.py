n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))
n3 = int(input("Enter a number n3: "))

if n1 < n2 and n1 < n3:
    print(n1, "is smaller")
elif n2 < n1 and n2 < n3:
    print(n2, "is smaller")
else:
    print(n3, "is smaller")