from array import array

a = array('i', [10, 20, 30, 40])

with open("numbers.bin", "wb") as f:
    a.tofile(f)

print("Array data successfully written to file.")