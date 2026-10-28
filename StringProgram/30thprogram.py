s1 = input("First String: ")
s2 = input("Second String: ")

if len(s1) == len(s2) and s2 in s1+s1:
    print("Yes")
else:
    print("No")