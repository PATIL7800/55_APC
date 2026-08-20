a = [1, 2, 2, 3, 1, 4]

b = []
for x in a:
    if x not in b:
        b.append(x)

print(b)