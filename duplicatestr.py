str = input("Enter a string: ")
temp = ""

for i in str:
    if i in temp:
        print("Duplicate value found:", i)
    else:
        temp += i
