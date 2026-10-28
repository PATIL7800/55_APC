# Check whether the square root of a number is prime or not

n = int(input("Enter a number: "))
root = int(n ** 0.5)

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

if prime:
    print(root, "is Prime")
else:
    print(root, "is Not Prime")