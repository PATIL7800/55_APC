temp = [28, 30, 31, 29, 32, 33, 27, 26, 30, 34,
        35, 31, 29, 28, 33, 36, 30, 27, 29, 32,
        31, 34, 35, 30, 28, 29, 33, 32, 31, 30]

avg = sum(temp) / len(temp)

print("Hottest:", max(temp))
print("Coldest:", min(temp))
print("Average:", avg)
print("Above average:", sum(x > avg for x in temp))
print("Below average:", sum(x < avg for x in temp))