import numpy as np
arr = np.array([10, 25, 55, 70, 40, 90, 35, 60, 20, 80])
print("Original array:", arr)
arr[arr > 50] = 0
print("After replacing values greater than 50:", arr)