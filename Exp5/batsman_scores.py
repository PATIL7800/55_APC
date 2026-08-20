scores = [45, 102, 67, 120, 34, 89, 55, 150, 42, 78]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total runs:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("Centuries:", sum(x >= 100 for x in scores))
print("Half-centuries:", sum(50 <= x <= 99 for x in scores))