def percentage_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))
percentage, grade = percentage_grade(m1, m2, m3, m4, m5)
print("Percentage =", percentage)
print("Grade =", grade)
