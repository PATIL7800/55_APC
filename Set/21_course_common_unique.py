python_students = {"Amit", "Rahul", "Sneha", "Pooja"}
java_students = {"Sneha", "Pooja", "Riya", "Neha"}

both = python_students & java_students
only_one = python_students ^ java_students

print("Students in both courses:", both)
print("Students in only one course:", only_one)