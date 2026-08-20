morning = {"Amit", "Rahul", "Sneha", "Pooja"}
afternoon = {"Sneha", "Pooja", "Riya", "Neha"}

print("Students in both sessions:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one session:", morning | afternoon)