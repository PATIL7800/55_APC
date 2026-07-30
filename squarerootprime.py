import math

n = int(input("Enter a number: "))
r = int(math.sqrt(n))

if r * r != n:
    print("Square root is not an integer")
else:
    prime = True

    for i in range(2, r):
        if r % i == 0:
            prime = False
            break

    if prime and r > 1:
        print("Square root is Prime")
    else:
        print("Square root is Not Prime")