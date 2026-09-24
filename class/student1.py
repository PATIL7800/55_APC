class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def display(self):
        percentage = self.marks
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
s1 = Student(1, "Vaishnavi", 85)
s2 = Student(2, "Rahul", 78)
s1.display()
print()
s2.display()