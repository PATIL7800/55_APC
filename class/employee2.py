class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
    def calculate(self):
        hra = self.basic_salary * 0.10
        da = self.basic_salary * 0.05
        gross = self.basic_salary + hra + da
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)
e1 = Employee(101, "Vaishnavi", 30000)
e1.calculate()