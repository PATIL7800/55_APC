# Print 1 2 4 8 16 32 ... up to n²

n = int(input("Enter n: "))

for i in range(n):
    if 2 ** i <= n * n:
        print(2 ** i)