students = {"Vaishnavi", "Aarya", "Shruti", "Pooja", "Sneha"}

name = input("Enter student name: ")

if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist.")