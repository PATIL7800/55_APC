names = ["Amit", "Riya", "Sneha"]
ages = [25, 30, 22]

names.append("Rahul")
ages.append(35)

names.remove("Amit")
ages.pop(0)

print("Search:", "Riya" in names)
print("Patients:", names)
print("Ages:", ages)
print("Total patients:", len(names))