marks = [45, 67, 89, 76, 55, 92, 34, 78, 81, 66,
         73, 59, 88, 91, 47, 69, 84, 62, 75, 58]

avg = sum(marks) / len(marks)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", avg)
print("Above average:", sum(x > avg for x in marks))
print("Below average:", sum(x < avg for x in marks))