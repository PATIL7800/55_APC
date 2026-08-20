from array import array

a = array('i', [10, 20])

b = array('i', [30, 40])

data = b.tobytes()

a.frombytes(data)

print("Array:", a)