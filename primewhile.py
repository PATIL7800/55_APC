n = int(input("Enter a number: "))

i = 2
prime = True

if n < 2:
    prime = False
else:
    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")