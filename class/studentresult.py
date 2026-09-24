class StudentResult:
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
    def total(self):
        return self.m1 + self.m2 + self.m3 + self.m4 + self.m5
    def percentage(self):
        return self.total() / 5
    def grade(self):
        p = self.percentage()
        if p >= 80:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 40:
            return "C"
        else:
            return "Fail"
    def display(self):
        print("Name:", self.name)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())
    def __del__(self):
        print("Student result object destroyed")
s = StudentResult("Vaishnavi", 80, 75, 90, 85, 70)
s.display()