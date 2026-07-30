# Take integer input from the user
n = int(input("Enter the limit value (n): "))
for shift in range(n + 1):
    term = 1 << shift
    if term > n:
        break
        
    print(term, end=" ")
