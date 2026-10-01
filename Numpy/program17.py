import numpy as np
marks = np.array([65, 78, 45, 89, 92, 56, 73, 81, 68, 95,
                  52, 76, 88, 61, 70, 84, 49, 90, 72, 80])
average = np.mean(marks)
print("Marks:", marks)
print("Class Average:", average)
print("Students above average:")
print(marks[marks > average])